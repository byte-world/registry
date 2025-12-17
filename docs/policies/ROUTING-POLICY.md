# 🌐 Byte World Global Routing Policy

This document defines the routing standards and expectations for all
participants in the Byte World network.  
It ensures a stable, secure, and predictable routing environment for learning,
experimentation, and interconnection.

Byte World uses BGP as its core protocol, with routing policies similar to DN42
and Internet exchange environments.

---

# 🧩 1. Addressing and ASN Summary

**IPv4 Space:**  
```

10.100.0.0/16

```

**IPv6 Space:**  
```

fd42:4242:4242::/48

```

**ASN Range:**  
Private 32-bit ASNs  
```

4200000000 – 4294967294

```

All prefixes MUST have corresponding IRR objects before announcements.

---

# 🔄 2. General Routing Requirements

All participants must:

- Run BGP-4 or BGP-4+ (IPv6) with their peers  
- Announce only their assigned prefixes  
- Maintain accurate `route` and `route6` objects  
- Use correct `origin:` ASN in IRR  
- Use filtering to prevent leaks or hijacks  
- Keep tunnel endpoints reachable and stable  
- Ensure no forwarding of real Internet traffic through Byte World  

---

# 🛡 3. Export Policy (Outbound Announcements)

You MUST only export:

- Your own assigned IPv4/IPv6 blocks
- Anycast prefixes assigned to you
- Sub-allocations you issued (if applicable)

You MUST NOT announce:

- Another participant’s prefixes
- Unallocated or reserved space
- Larger aggregates unless assigned
- Real Internet prefixes (PUBLIC BGP IS NOT ALLOWED)

Violations will result in filtering or suspension.

---

# 📥 4. Import Policy (Inbound Acceptance)

Participants MAY choose:

1. **Import ANY** (default for most labs)
2. Import **only specific peers**
3. Apply strict filtering (recommended for advanced setups)

Filters must be based on:

- Valid assigned prefixes from IRR
- Known, reachable peers
- Peers in your AS-SET (optional)

---

# 🧱 5. IRR Requirements

Every BGP announcement MUST have:

### IPv4:
```

route: <prefix>
origin: <asn>
mnt-by: <mntner>
source: BYTEWORLD

```

### IPv6:
```

route6: <prefix>
origin: <asn>
mnt-by: <mntner>
source: BYTEWORLD

```

Routes *without* matching IRR objects may be filtered.

---

# ⚙ 6. Peering Requirements

Each peer should define:

- IPv4 and IPv6 tunnel endpoints  
- Peer ASN  
- WireGuard/OpenVPN/GRE/Direct interface details  
- Supported protocols (IPv4, IPv6, or both)  
- Optional MD5 password  

Example Peering Policy:
```

import: from AS4200000000 accept ANY
export: to AS4200000000 announce AS4200001000:AS-ROUTES

```

---

# 🕸 7. Topology and Transit Rules

Byte World uses a **multi-mesh topology**, meaning:

- You MAY peer with any other ASN
- You MAY provide transit if you wish
- You MUST NOT force transit on others
- Transit is OPTIONAL and voluntary

### Allowed:
- Multihop transit labs
- Route server labs
- IXP experimentation
- Anycast traffic engineering

### Not allowed:
- Creating a “default route only ISP”
- Blackholing or attacking other networks
- Simulating malicious routing (prefix hijacks)

---

# 🌍 8. AS-SETs

Participants may create AS-SETs in:

```

as-set/AS-<NAME>

```

AS-SETs help with:

- Import filtering
- Multihoming
- Peering groups

Example:
```

as-set: AS-BYTEWORLD
members: AS4200000000, AS4200001000, AS4200001001

```

---

# 🛰 9. Anycast Routing Rules

Anycast is allowed for:

- DNS  
- NTP  
- Web services  
- Registry services  
- Custom labs  

Rules:
- Prefix must be <= /32 (IPv4) or /128 (IPv6)
- Announced consistently from multiple locations
- Mark route objects with a remark: "ANYCAST PREFIX"

---

# 🛑 10. Filtering Recommendations

Operators SHOULD filter:

- Bogon prefixes  
- Private ASNs not in Byte World range  
- Any unregistered prefixes  
- Misoriginated routes  
- Peers advertising more than 20 prefixes (unless expected)  
- Default routes (0.0.0.0/0, ::/0) unless explicitly allowed  

Filtering protects the mesh from accidental leaks.

---

# 🚫 11. Prohibited Routing Behavior

The following are strictly forbidden:

- Prefix hijacks  
- Announcing real Internet routes  
- Traffic injection attacks  
- Route leaks  
- Abusing Byte World for scanning the real Internet  
- DDoS or malicious experiments  

Any violation results in:

- Prefix revocation  
- ASN suspension  
- Removal from registry (last resort)  

---

# 📣 12. Recommended BGP Defaults

### For new participants:
```

import: from ANY accept ANY
export: to ANY announce AS-MYASN

```

### For advanced users:
- Set max-prefix limits
- Apply IRR-based filtering
- Use AS-PATH filters
- Avoid relying on default routes
- Prefer shortest AS-PATH or MED policies

---

# 🧵 13. Example ASN Routing Policy

```

aut-num:        AS4200001000
as-name:        USER1-NET
import:         from AS4200000000 accept ANY
import:         from AS4200001001 accept AS-USER2
export:         to AS4200000000 announce AS4200001000:AS-ROUTES
export:         to AS4200001001 announce AS4200001000
source:         BYTEWORLD

```

---

# 🤝 14. Changes to Routing Policy

You may update your routing policy by submitting a PR modifying your `asn/` object.

---

# 🎉 Welcome to Byte World Routing

Experiment, learn BGP deeply, and build your own miniature Internet!
