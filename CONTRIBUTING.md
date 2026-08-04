# Contributing to bwnet

## What goes in a PR

- A new node joining the mesh: `mntner` + `person` (if you're new) plus
  `aut-num`, `inetnum`/`inet6num`, and `route`/`route6` for your space.
- A policy change: edit `docs/POLICY.md` directly and flag it in the
  ByteWorld Matrix room first — it affects everyone's filters.
- A correction to an object you own: edit it in place, same PR rules.

## Rules

- One conceptual change per PR (a new node's full object set counts as one).
- Only edit objects whose `mnt-by:` is yours, unless you're a registry
  admin acting on request.
- `scripts/validate.py` runs on every PR via GitHub Actions — fix any
  errors it reports before requesting review.
- Object file names are the primary key with `/` and `:` replaced by `_`
  (see `docs/REGISTRY.md` for examples).

## Local validation

```
python3 scripts/validate.py
```

Run this before opening a PR — it's the same check CI runs, so you'll
catch problems immediately instead of waiting on the pipeline.

## Getting help

Ask in the ByteWorld Matrix room or IRC channel — see the main
[byteworld mesh homepage](https://byteworld.mesh) for links.
