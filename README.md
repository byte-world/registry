# 🌐 Byte World Registry

Welcome to the **Byte World Registry**, the authoritative database for
allocations, ASNs, routes, peering information, and membership records
within the **Byte World private network**.

Byte World is a DN42-style experimental networking environment designed for:
- BGP practice  
- IP allocation and routing simulation  
- Community-based networking experiments  
- Learning IRR, RPKI (optional), Anycast, DNS, and IX design  
- Hobby and lab-scale multi-AS networking  

This registry contains authoritative information about:
- AS numbers (aut-num objects)
- IPv4 and IPv6 allocations
- Route and Route6 objects
- Maintainers (mntner)
- Contacts (person)
- AS-SETs
- Peering metadata

---

## 📁 Directory Structure

```

registry/
├── asn/          # ASNs (aut-num objects)
├── inetnum/      # IPv4 allocations
├── inet6num/     # IPv6 allocations
├── route/        # Route objects (IPv4)
├── route6/       # Route6 objects (IPv6)
├── person/       # Person / contact objects
├── mntner/       # Maintainers
├── as-set/       # AS-SET definitions
└── peering/      # Optional peering metadata

```

Each file contains a single IRR-style object.

---

## 🆕 How to Join Byte World

To join Byte World and receive:
- An ASN  
- IPv4 and/or IPv6 space  
- Entry in IRR  
- Peering policy integration  

Follow these steps:

1. **Fork this repository**
2. Create a directory under:
   - `person/`
   - `mntner/`
   - `asn/`
3. Add your objects (examples are in `samples/`)
4. Submit a **Pull Request**
5. A registry admin will review and merge your allocation

---

## 📝 Object Naming Conventions

### 🔹 Persons
```

person/BW-PERSON-XXX

```

### 🔹 Maintainers
```

mntner/BW-MNT-<YOURNAME>

```

### 🔹 ASN Files
```

asn/AS420000XXXX

```

### 🔹 IPv4 Allocations
```

inetnum/10.100.X.0_24

```

### 🔹 IPv6 Allocations
```

inet6num/fd42_4242_XXXX__64

```

### 🔹 Routes
```

route/10.100.X.0_24
route6/fd42_4242_XXXX__64

```

---

## 🛡 Routing Policy

Byte World uses:
- **Private ASNs** in the 4200000000–4294967294 range  
- **RFC1918 IPv4** space (10.100.0.0/16)
- **ULA IPv6** space (fd42:4242:4242::/48)

### General BGP Guidelines
- Export only your own prefixes
- Ensure correct `origin:` in route objects
- Maintain accurate contact and mntner information
- No default routes unless via the core (AS4200000000)

---

## 🔄 Peering in Byte World

Each participant may optionally publish a **peering metadata file** in:

```

peering/AS<yourasn>

```

This can include:
- WireGuard endpoints
- Public keys
- IPv4/IPv6 tunnel endpoints
- BGP MD5 secrets (optional)
- Suggested policies

---

## 📜 Example Object

```

aut-num:        AS4200001000
as-name:        USER1-NET
admin-c:        BW-PERSON-002
tech-c:         BW-PERSON-002
mnt-by:         BW-MNT-USER1
import:         from AS4200000000 accept ANY
export:         to AS4200000000 announce AS4200001000:AS-ROUTES
source:         BYTEWORLD

```

---

## 🔧 Tools & Software

To interact with Byte World, these tools are recommended:
- **FRRouting / BIRD / OpenBGPD** (for BGP)
- **WireGuard** (tunnels)
- **OpenVPN / GRE / IPIP** (optional)
- **pebble** or **routinator** (optional RPKI labs)
- **IRRd v4** (IRR server support)

---

## 📬 Contact & Support

For registry help, allocations, or peering:
- Open an Issue
- Submit a Pull Request
- Contact the registry maintainers

---

## 🛑 Rules

To keep Byte World stable:
- No darknet/illegal content  
- No scanning the real Internet  
- No announcing public Internet routes  
- No malicious BGP experiments  
- Keep your objects up to date  

---

## 🎉 Welcome to Byte World!

Experiment, break things (responsibly), learn, and build your own mini-Internet!
