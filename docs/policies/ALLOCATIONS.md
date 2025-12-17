# 📦 Byte World Address Allocation Policy

This document describes how IP address space is allocated within **Byte World**, including:
- IPv4 allocation rules  
- IPv6 allocation rules  
- ASN assignment policy  
- Request procedures  
- Usage expectations  
- Revocation rules  

Byte World is a private, experimental network.  
All resources are assigned **for lab and educational use only**.

---

# 🧭 Address Space Overview

Byte World uses the following internal address pools:

## IPv4 Pool
```

10.100.0.0/16

```
Used for:
- Point-to-point links  
- LAN subnets  
- Anycast prefixes  
- Internal services  

### Default IPv4 allocation sizes:
| Use Case | Recommended Allocation |
|----------|------------------------|
| Single router/lab | `/32` or `/31` |
| Small network | `/30` or `/29` |
| Standard participant allocation | `/28` or `/27` |
| Larger networks | `/26`+ (requires justification) |

---

## IPv6 Pool
```

fd42:4242:4242::/48

```
Allocated as ULA (Unique Local Addressing).

### Default IPv6 allocation sizes:
| Use Case | Recommended Allocation |
|----------|------------------------|
| Standard user allocation | `/64` |
| Multi-subnet network | `/60` |
| Advanced users | `/56` or `/48` (with justification) |
| Anycast services | `/64` |

---

## ASN Pool
Byte World uses private 32-bit ASNs:

```

4200000000 – 4294967294

```

### Default ASN assignment:
- **One ASN per participant**
- Additional ASNs require a valid use case (IXP, transit lab, multi-homing testing, etc.)

---

# 📬 How to Request Allocations

All resource requests are made through a **Pull Request** to the registry.

### Your PR must include:
1. `person/` object  
2. `mntner/` object  
3. `asn/AS420000XXXX` object  
4. (Optional) `peering/` object  
5. A request message describing what you need

---

# 📝 IPv4 Allocation Rules

1. IPv4 space is allocated from `10.100.0.0/16`
2. Smallest block: `/32`  
3. Largest block without justification: `/27`  
4. Bigger prefixes (`/26` to `/24`) require:
   - Routing labs  
   - Multi-site setups  
   - IXP or BGP experiments  
5. Participants must:
   - Announce only their allocated space  
   - Maintain matching `route` objects  
   - Run correct `origin:` ASN values  

### Example IPv4 Allocation Block:
```

inetnum:        10.100.10.0 - 10.100.10.255
netname:        USER1-SUBNET
descr:          Allocation for AS4200001000
mnt-by:         BW-MNT-USER1
source:         BYTEWORLD

```

---

# 🌐 IPv6 Allocation Rules

1. IPv6 is allocated from `fd42:4242:4242::/48`
2. Default allocation: `/64`
3. Larger blocks allowed with justification:
   - `/60` = multiple LANs  
   - `/56` = larger topologies  
   - `/48` = multi-site or advanced labs  
4. Participants must:
   - Publish matching `route6` objects  
   - Use valid IPv6 addressing  
   - Announce the exact prefix assigned  

### Example IPv6 Allocation:
```

inet6num:       fd42:4242:1000::/64
netname:        USER1-V6
mnt-by:         BW-MNT-USER1
source:         BYTEWORLD

```

---

# 🛰 ASN Assignment Rules

1. Each participant receives one ASN by default
2. ASN range:
```

4200000000 – 4294967294

```
3. Additional ASNs require justification:
- Route server simulation  
- IXP project  
- Multihoming experiments  
- Transit provider simulation  
4. ASN must have:
- `aut-num` object
- Correct imports/exports
- Maintainer references

---

# 🧩 Routing & IRR Requirements

Participants must:

- Maintain accurate objects
- Match route prefixes to correct origin ASN
- Ensure all `route` and `route6` objects exist before announcing
- Include `mnt-by:` fields
- Set `source:` to `BYTEWORLD`

Announcements *without* matching IRR objects may be filtered.

---

# 🕊 Anycast Allocations

Byte World supports Anycast testing.

### Default Anycast allocation:
- IPv4: `/32`
- IPv6: `/128`

Larger Anycast blocks allowed with:
- DNS services  
- NTP  
- WHOIS  
- Registry infrastructure  

Participants must:
- Label anycast objects clearly  
- Maintain route consistency  

---

# 🚫 Resource Revocation Policy

Resources may be reclaimed if:

- Participant becomes unreachable for > 60 days  
- Prefixes are hijacked or abused  
- Unsupported or invalid IRR objects remain unfixed  
- Repeated policy violations  
- Malicious routing behavior  

Participants may reapply anytime.

---

# 📣 Questions or Issues?

Open an **Issue** or contact a registry admin.

---

# 🎉 Welcome to Byte World!

Experiment, learn, build, and have fun creating your own Internet.
