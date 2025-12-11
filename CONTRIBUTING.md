# Contributing to the Byte World Registry

Thank you for your interest in contributing to **Byte World**!  
This document explains how to submit changes, request new resources, and follow the rules that keep the Byte World registry consistent and stable.

Byte World is a community-driven private network.  
All changes are made through **Git pull requests**.

---

# 📌 Requirements

To contribute, you must:

- Have a GitHub account (or equivalent system)
- Understand basic Git workflow (fork, commit, PR)
- Follow registry naming rules
- Ensure objects are **valid IRR-style formats**
- Only modify objects that **belong to you**
- Submit changes through **pull requests** (PRs)

---

# 🗂 Directory Overview

Your contribution will involve one or more of these folders:

```

asn/        # Your ASN object (aut-num)
person/     # Your person/role entry
mntner/     # Your maintainer object
inetnum/    # IPv4 allocations
inet6num/   # IPv6 allocations
route/      # IPv4 route objects
route6/     # IPv6 route objects
peering/    # Peering metadata (optional)
as-set/     # AS-SET definitions

```

---

# 🆕 How to Request an ASN and IP Prefix

1. **Fork this repository**
2. Create the following objects:
   - A `person/` object
   - A `mntner/` object
   - An `asn/AS420000XXXX` object
3. Request allocations by opening a **pull request**
4. A registry admin will:
   - Review your objects
   - Assign IP blocks (IPv4 and/or IPv6)
   - Add route objects
   - Merge your PR

Your ASN will be assigned from:

```

ASN Range: 4200000000 – 4294967294
IPv4 Pool: 10.100.0.0/16
IPv6 Pool: fd42:4242:4242::/48

```

---

# ✍️ Editing Existing Entries

You may update:

- Your own `person/` object (email, contacts)
- Your own `mntner/`
- Your own routes
- Your ASN import/export policies
- Your `peering/` metadata
- Your AS-SET memberships

You **may NOT** edit:

- Another user's objects
- Core allocations (unless approved)
- Global policy files

Unauthorized edits will be rejected.

---

# 🧱 Object Naming Conventions

### Person Objects
```

person/BW-PERSON-XXX

```

### Maintainer Objects
```

mntner/BW-MNT-<YOURNAME>

```

### ASNs
```

asn/AS420000XXXX

```

### IPv4 Allocations
```

inetnum/10.100.X.0_24

```

### IPv6 Allocations
```

inet6num/fd42_4242_XXXX__64

```

### Routes
```

route/10.100.X.0_24
route6/fd42_4242_XXXX__64

```

---

# ✔ PR Requirements

Your pull request must:

- Use one commit per logical change
- Include readable commit messages (e.g., `Add ASN for user MWANGA`)
- Pass basic format validation (spacing, fields, syntax)
- Contain only the objects you own
- Match one of the following PR types:

### ✔ New Member Join  
Adds:
- person
- mntner
- aut-num
- peering (optional)

### ✔ New Prefix Allocation  
Adds or updates:
- inetnum / inet6num
- route / route6

### ✔ Metadata Update  
Update:
- Contact info
- Maintainer auth keys
- Peering details

### ✔ Routing Policy Update  
Update import/export in your ASN file.

---

# 🧪 Validating Your Objects

Before submitting a PR:

- Make sure your objects follow the IRR formatting used in examples  
- Ensure all fields end with a newline  
- No trailing spaces  
- All required attributes (`admin-c`, `tech-c`, `mnt-by`, `source`) must exist  

A simple rule:  
> **If DN42’s registry format accepts it, Byte World will accept it too.**

---

# 🤝 How PR Review Works

1. A registry admin checks:
   - Format correctness
   - Naming conventions
   - Duplicate allocations
   - ASN/IP conflicts

2. Admin may request changes:
   - Fix indentation
   - Correct origin ASN
   - Rename files
   - Update mntner references

3. Once approved:
   - Allocations are added (if required)
   - PR is merged
   - Your member state becomes "active"

---

# ❗ Rules for Participants

To keep Byte World stable:

- No harmful traffic
- No real Internet routes may be announced
- No scanning external networks
- No hijacking other Byte World prefixes
- Maintain accurate contact info
- Keep tunnel endpoints reachable

Violations may result in:
- ASN suspension  
- Prefix revocation  
- Removal from the registry  

---

# 📣 Need Help?

You may:
- Open an Issue  
- Ping a registry admin  
- Check sample objects in `/samples/`  

---

# 🎉 Welcome to Byte World!

Thank you for contributing to this experiment in community networking!
