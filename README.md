# ByteWorld Registry — bwnet

A [dn42](https://dn42.eu)-style decentralized routing registry and peering
network for **ByteWorld**, the volunteer-run community mesh network in
Nairobi, Kenya.

`bwnet` gives every ByteWorld node, relay, and member link a single source
of truth for address space, ASNs, and route origination — the same way
dn42 coordinates a global amateur internet, but scoped to our own mesh and
its private numbering plan.

## Why this exists

ByteWorld is growing past the point where informal "just pick an IP that's
free" coordination works. As more neighborhoods stand up relay nodes and
peer with each other over WireGuard, we need:

- A collision-free private address plan (IPv4 + IPv6 ULA)
- A private ASN block so nodes can run real BGP between each other
- A registry of who owns what, so route filters can be built automatically
- A lightweight, git-based workflow — no central admin bottleneck

## Repository layout

```
docs/
  POLICY.md      addressing & ASN allocation policy
  PEERING.md     how to set up a WireGuard + BGP session with a peer
  REGISTRY.md    object types, RPSL-style syntax, submission workflow
registry/
  mntner/        maintainer objects (who can edit what)
  person/        contact objects
  aut-num/       ASN objects (one per node/operator)
  inetnum/       IPv4 allocations
  inet6num/      IPv6 (ULA) allocations
  route/         IPv4 route origination objects
  route6/        IPv6 route origination objects
  dns/           reverse DNS delegation objects
scripts/
  validate.py    CI validator — schema, mnt-by references, range checks
.github/workflows/validate.yml   runs the validator on every PR
```

## Quick start — joining the mesh

1. Read `docs/POLICY.md` to understand the address plan and pick your region.
2. Read `docs/REGISTRY.md` and submit a `mntner` + `person` object for
   yourself (this is your identity in the registry).
3. Request (or self-assign, per policy) an ASN and a `/24` (IPv4) or `/48`
   (IPv6) block for your node, and file the corresponding `aut-num`,
   `inetnum`/`inet6num`, and `route`/`route6` objects.
4. Open a PR. CI validates the objects automatically.
5. Once merged, follow `docs/PEERING.md` to bring up a WireGuard tunnel and
   BGP session with your nearest ByteWorld relay.

## Philosophy

ByteWorld's registry borrows dn42's core idea — a community can run its
own internet-style routing coordination without a RIR, using git and plain
text as the source of truth — and applies it to a real, physical mesh
network instead of a purely virtual overlay. Every object in this repo
corresponds to an actual node, link, or person in Nairobi.

See also: [byteworld mesh homepage](https://byteworld.mesh) ·
[Byte IX](https://byteworld.mesh/ix) · IRC/Matrix community channels.
