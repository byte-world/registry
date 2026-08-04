# BYTEWORLD Registry Objects

Objects use RPSL-style `key: value` syntax, one object per file, one
object per PR unless objects are logically tied together (e.g. a new
node's `aut-num` + `inetnum` + `route`).

File naming: `registry/<type>/<primary-key>`, primary key with `/` and `:`
replaced by `_` (e.g. `registry/inetnum/172.20.0.0_14`).

## Object types

### `mntner` — maintainer

Your identity in the registry; every other object you own references you
via `mnt-by:`.

```
mntner:     BW-JDOE-MNT
descr:      Jane Doe, BYTEWORLD INTERNET EXCHANGE
admin-c:    JDOE-BW
auth:       pgp-fingerprint <your-key-fingerprint>
mnt-by:     BW-JDOE-MNT
source:     BYTEWORLD
```

### `person` — contact

```
person:     Jane Doe
nic-hdl:    JDOE-BW
contact:    matrix:@jdoe:byteworld.mesh
mnt-by:     BW-JDOE-MNT
source:     BYTEWORLD
```

### `aut-num` — ASN registration

```
aut-num:    AS4243000012
as-name:    BYTE-IX
descr:      BYTE WORLD INTERNET EXCHANGE
admin-c:    JDOE-BW
mnt-by:     BW-JDOE-MNT
source:     BYTEWORLD
```

### `inetnum` / `inet6num` — address allocation

```
inetnum:    10.127.0.0/24
netname:    BYTE-IX
descr:      BYTEWORLD INTERNET EXCHANGE
country:    KE
admin-c:    JDOE-BW
mnt-by:     BW-JDOE-MNT
source:     BYTEWORLD
```

### `route` / `route6` — origination

```
route:      172.21.12.0/24
origin:     AS4230000012
descr:      Kibera relay 1 announced space
mnt-by:     BW-JDOE-MNT
source:     BYTEWORLD
```

### `dns` — reverse delegation (optional)

```
dns:        20.30.172.in-addr.arpa
nserver:    ns1.byteworld.mesh
nserver:    ns2.byteworld.mesh
mnt-by:     BW-JDOE-MNT
source:     BYTEWORLD
```

## Submission workflow

1. Fork this repo.
2. Add/edit your object file(s) under the correct `registry/<type>/`
   directory.
3. Open a PR. `scripts/validate.py` runs automatically via GitHub
   Actions and checks:
   - required fields present per object type
   - `mnt-by:` points to a `mntner` object that exists
   - ASNs fall inside the range defined in `docs/POLICY.md`
   - prefixes fall inside the parent BYTEWORLD blocks and don't overlap an
     existing `inetnum`/`inet6num` owned by someone else
4. A maintainer (or, once auth is wired up, an automated check against
   your `mntner` PGP key) approves and merges.
5. Your object is now live — peers building filters from this repo will
   pick it up.

## Editing objects you own

Only touch objects whose `mnt-by:` is yours, unless you're a registry
admin fixing something on request. Disputed edits get resolved in the
Matrix room, not by force-pushing.
