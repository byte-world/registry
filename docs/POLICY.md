# bwnet Addressing & ASN Policy

This document defines the private numbering plan for the ByteWorld mesh
registry. It mirrors dn42's approach: space carved out of ranges reserved
for private use (RFC 1918 / RFC 4193 / RFC 6996), coordinated entirely
through this registry so no two nodes ever collide.

**bwnet space is not routed on the public internet.** It is only valid
between ByteWorld peers who have agreed to accept these announcements.
-
---

## 1. IPv4 — `172.16.0.0/12`

ByteWorld IPv4 space is a single `/12` out of RFC 1918 space, chosen to
avoid the ranges most home/office LANs already use (`10.0.0.0/8`, `192.168.0.0/16`, `172.16.0.0/12` first octets).

The `/12` is divided into four `/14` blocks, one per Nairobi coverage
region. Regions are assigned in order as coverage expands; unused regions
are reserved for future neighborhoods.
 _______________________________________________
| Allocation               | Block              |
|--------------------------|--------------------|
| Reserved                 | `172.16.0.0/14`    |
| Active Pool              | `172.20.0/14`      |
| Reserved for allocation after depletion  | `172.24.0.0/20`    |
| Reserved for future use  | `172.28.0.0/14`    |

Within a block `/14`, node operators receive a `/24` to `/22` depending
on projected link count. A node uses its block for point-to-point
transfer nets (usually `/31` or `/30` per WireGuard link) and any loopback
or LAN space it wants to advertise.

Region names above are working defaults — rename them in a PR if the
neighborhood you're bringing online isn't listed yet; that just needs a
one-line edit here plus your `inetnum` object.

## 2. IPv6 — `fd00::/8` (ULA)

ByteWorld uses a locally-assigned Unique Local Address prefix,
`fd00::/8`, chosen inside the ULA range (`fc00::/7`, specifically
the locally-assigned `fd00::/8` half) per RFC 4193. Because ULA prefixes
are meant to be randomly generated, this one is intentionally
memorable/branded rather than random — acceptable for a private registry
like this one, same as dn42 conventions.


## 3. ASNs — `4200000000`–`4294967294`

ByteWorld uses 32-bit private ASNs (RFC 6996 range is
`4200000000`–`4294967294`) from the entire reserved block:

```
4230000000 – 4239999999   (10,000,000 ASNs)
```

- `4200000000`–`4229999999` — reserved for Byte IX route servers and core infrastructure
- `4230000000`–`4239999999` — assigned to nodes/operators on request, sequentially, tracked via `aut-num` objects in this registry

If you'd rather run a 16-bit private ASN (`64512`–`65534`) on
older/limited hardware (some MikroTik RouterOS 6 setups prefer this),
that's fine — just note it clearly in your `aut-num` object so peers don't
assume the 32-bit block.

## 4. Route origination rules

- A prefix may only be announced if a matching `route`/`route6` object
  exists in the registry, with `origin:` matching the announcing ASN.
- Sub-allocations (a node announcing a smaller block than its `inetnum`)
  are allowed and encouraged for traffic engineering, but each announced
  prefix needs its own `route` object.
- Peers are expected to build IRR-style filters from this registry (see
  `docs/PEERING.md`) and reject anything not registered.

## 5. Changing this policy

Policy changes go through a PR against this file, same as any registry
object, and should be flagged in the ByteWorld Matrix room before merging
since they affect everyone's filters.
