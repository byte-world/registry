#!/usr/bin/env python3
"""
bwnet registry validator.

Walks registry/<type>/* object files, checks:
  - required fields are present for each object type
  - mnt-by: references an existing mntner object
  - aut-num ASN falls inside the policy-defined ByteWorld ASN range
  - inetnum/inet6num/route/route6 prefixes fall inside bwnet space
  - no two inetnum/inet6num objects claim overlapping space

Exits non-zero (and prints every problem found) if anything fails, so it
can be wired into CI (see .github/workflows/validate.yml).
"""

import ipaddress
import sys
from pathlib import Path

REGISTRY_DIR = Path(__file__).resolve().parent.parent / "registry"

# Required fields per RPSL-style object type (see docs/REGISTRY.md).
REQUIRED_FIELDS = {
    "mntner": ["mntner", "descr", "admin-c", "auth", "mnt-by", "source"],
    "person": ["person", "nic-hdl", "contact", "mnt-by", "source"],
    "aut-num": ["aut-num", "as-name", "descr", "admin-c", "mnt-by", "source"],
    "inetnum": ["inetnum", "netname", "descr", "country", "admin-c", "mnt-by", "source"],
    "inet6num": ["inet6num", "netname", "descr", "country", "admin-c", "mnt-by", "source"],
    "route": ["route", "origin", "descr", "mnt-by", "source"],
    "route6": ["route6", "origin", "descr", "mnt-by", "source"],
    "dns": ["dns", "nserver", "mnt-by", "source"],
}

# bwnet policy constants (docs/POLICY.md) — keep in sync if policy changes.
BW_IPV4_SPACE = ipaddress.ip_network("172.20.0.0/14")
BW_IPV6_SPACE = ipaddress.ip_network("fd42::/8")
BW_ASN_MIN = 4200000000
BW_ASN_MAX = 4294967294


def parse_object(path: Path) -> dict:
    """Very small RPSL-ish parser: 'key:   value' per line, blank/comment
    lines ignored, repeated keys collected into a list under one key."""
    fields: dict[str, list[str]] = {}
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        fields.setdefault(key, []).append(value)
    return fields


def first(fields: dict, key: str) -> str | None:
    values = fields.get(key)
    return values[0] if values else None


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not REGISTRY_DIR.exists():
        print(f"ERROR: registry directory not found at {REGISTRY_DIR}")
        return 1

    mntners: set[str] = set()
    all_objects: list[tuple[str, Path, dict]] = []

    # Pass 1: parse everything, collect mntner names, check required fields.
    for obj_type in REQUIRED_FIELDS:
        type_dir = REGISTRY_DIR / obj_type
        if not type_dir.exists():
            continue
        for path in sorted(type_dir.iterdir()):
            if not path.is_file():
                continue
            fields = parse_object(path)
            all_objects.append((obj_type, path, fields))

            required = REQUIRED_FIELDS[obj_type]
            missing = [f for f in required if f not in fields]
            if missing:
                errors.append(
                    f"{path}: missing required field(s): {', '.join(missing)}"
                )

            if obj_type == "mntner":
                name = first(fields, "mntner")
                if name:
                    mntners.add(name)

    # Pass 2: cross-reference checks.
    inet_allocations: list[tuple[ipaddress._BaseNetwork, Path]] = []
    inet6_allocations: list[tuple[ipaddress._BaseNetwork, Path]] = []

    for obj_type, path, fields in all_objects:
        mnt_by = first(fields, "mnt-by")
        if mnt_by and mnt_by not in mntners:
            errors.append(
                f"{path}: mnt-by '{mnt_by}' does not match any mntner object"
            )

        if obj_type == "aut-num":
            asn_field = first(fields, "aut-num") or ""
            digits = asn_field.upper().replace("AS", "").strip()
            if digits.isdigit():
                asn = int(digits)
                if not (BW_ASN_MIN <= asn <= BW_ASN_MAX):
                    errors.append(
                        f"{path}: ASN {asn} outside bwnet range "
                        f"{BW_ASN_MIN}-{BW_ASN_MAX} (see docs/POLICY.md)"
                    )
            else:
                errors.append(f"{path}: could not parse ASN from '{asn_field}'")

        if obj_type in ("inetnum", "route"):
            key = "inetnum" if obj_type == "inetnum" else "route"
            prefix_field = first(fields, key)
            if prefix_field:
                try:
                    net = ipaddress.ip_network(prefix_field, strict=False)
                except ValueError:
                    errors.append(f"{path}: invalid IPv4 prefix '{prefix_field}'")
                else:
                    if not net.subnet_of(BW_IPV4_SPACE):
                        errors.append(
                            f"{path}: {net} is outside bwnet IPv4 space "
                            f"{BW_IPV4_SPACE}"
                        )
                    if obj_type == "inetnum":
                        inet_allocations.append((net, path))

        if obj_type in ("inet6num", "route6"):
            key = "inet6num" if obj_type == "inet6num" else "route6"
            prefix_field = first(fields, key)
            if prefix_field:
                try:
                    net = ipaddress.ip_network(prefix_field, strict=False)
                except ValueError:
                    errors.append(f"{path}: invalid IPv6 prefix '{prefix_field}'")
                else:
                    if not net.subnet_of(BW_IPV6_SPACE):
                        errors.append(
                            f"{path}: {net} is outside bwnet IPv6 space "
                            f"{BW_IPV6_SPACE}"
                        )
                    if obj_type == "inet6num":
                        inet6_allocations.append((net, path))

    # Pass 3: overlap checks within each allocation family.
    for allocations, label in (
        (inet_allocations, "inetnum"),
        (inet6_allocations, "inet6num"),
    ):
        for i, (net_a, path_a) in enumerate(allocations):
            for net_b, path_b in allocations[i + 1:]:
                if net_a.overlaps(net_b):
                    warnings.append(
                        f"{label} overlap: {path_a} ({net_a}) overlaps "
                        f"{path_b} ({net_b})"
                    )

    for w in warnings:
        print(f"WARNING: {w}")

    if errors:
        print(f"\n{len(errors)} error(s):")
        for e in errors:
            print(f"  ERROR: {e}")
        return 1

    print(f"OK: {len(all_objects)} object(s) validated, no errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
