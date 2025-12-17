# Byte World Peering Policy

This document defines the official peering policy for **Byte World**, a
community-driven private networking project designed for BGP learning,
experimentation, and collaboration.

Peering with the Byte World Core (AS4200000000) or other participants enables
exchange of routes and participation in the global Byte World topology.

This policy applies to all ASNs operating within Byte World.

---

# 1. Peering Philosophy

Byte World encourages:
- Open, education-friendly peering
- Simple, predictable routing
- Responsible BGP experimentation
- Collaboration between participants

Peering is a privilege, not a right. All participants are expected to maintain
network stability, provide accurate IRR data, and follow the Code of Conduct.

---

# 2. Peering Model

Byte World uses a **semi-open peering model**:

### ✔ Open within the Community
Any compliant participant may peer with:
- **Byte World Core**
- **Regional Route Reflectors (where available)**
- **Other member ASNs**

### ✔ Selective Peering Allowed
Individual ASNs may define their own requirements, including:
- Minimum uptime expectations
- IRR object accuracy
- Operational responsiveness

---

# 3. Requirements for Peering

To establish peering with the Byte World Core or other members, your ASN must:

### 3.1 Registry Requirements
- Have a valid **aut-num** object in the Byte World registry.
- Have assigned address space (`inetnum` / `inet6num`) documented.
- Ensure `route` and `route6` objects are correct and kept up to date.
- Maintain a valid **maintainer (mntner)** object and contact details.

### 3.2 Technical Requirements
- Support **BGPv4** (mandatory)
- Support **BGP over IPv6** (recommended)
- Maintain stable tunnel endpoints (WireGuard, GRE, IPIP, OpenVPN, etc.)
- Announce only prefixes allocated to your ASN
- Maintain consistent `origin:` and `mnt-by:` information in IRR objects

### 3.3 Operational Requirements
- Ensure tunnels remain reachable and stable
- Respond to routing/security incidents within a reasonable timeframe
- Notify peers of significant maintenance when possible

---

# 4. Prefix Announcements

Participants **may announce** within Byte World:
- Their assigned IPv4 RFC1918 subnets  
- Their assigned IPv6 ULA prefixes  
- Optional lab/test prefixes with prior notice

Participants **may NOT announce**:
- Public Internet routes  
- Routes not assigned to their ASN  
- Bogons, malformed, or intentionally harmful prefixes  

Route filtering is enforced by the Byte World Core.

---

# 5. Routing Policy

### 5.1 Import Policy
The Byte World Core imports:
- Valid routes originated by known Byte World ASNs
- Routes with correct IRR entries
- Routes within authorized Byte World address space

Invalid or suspicious routes may be:
- Filtered
- Dampened
- Rejected
- Investigated

### 5.2 Export Policy
The Byte World Core exports:
- All validated routes from participating networks
- Default route (optional and disabled by default)
- Core infrastructure prefixes (RR, monitoring, optional services)

---

# 6. Tunnel Types Supported

Participants may use:
- **WireGuard** (recommended)
- GRE / IPIP
- VXLAN (optional)
- OpenVPN
- Tinc (optional)
- Direct physical connections (rare but allowed)

WireGuard is preferred due to:
- Low overhead
- High stability
- Simplicity
- Built-in roaming capability

---

# 7. Peering Process

### Step 1 — Submit Your ASN  
Ensure your aut-num and related objects exist in the registry.

### Step 2 — Create a Peering File  
Add your details under:
```

peering/AS<yourasn>.md

```
Use the provided **PEERING-TEMPLATE.md**.

### Step 3 — Contact a Core Operator  
Open an Issue or send a message requesting peering.

### Step 4 — Exchange Tunnel & BGP Info  
Share:
- Tunnel endpoints  
- Public keys (WireGuard)  
- IPv4/IPv6 tunnel IPs  
- Desired MD5 secrets (optional)

### Step 5 — Testing  
Both sides bring up tunnels and sessions.

### Step 6 — Final Validation  
The route reflector/core verifies:
- Origin ASN match
- Route objects exist and correspond
- No invalid prefixes are propagated

After successful validation, full peering is enabled.

---

# 8. Traffic & Acceptable Use

Participants **must not**:
- Attempt DoS/DDoS against the Byte World network
- Inject malformed or experimental routes globally
- Perform unauthorized scanning of peer networks
- Cause excessive churn, flaps, or route storms
- Influence routing maliciously

Byte World is for learning and collaboration—not disruption.

---

# 9. Termination of Peering

Peering may be terminated if:
- You behave maliciously or irresponsibly
- You violate the Code of Conduct
- Your tunnels or infrastructure remain broken for extended periods
- IRR objects become inconsistent or invalid
- You repeatedly inject invalid or harmful routes

Re-establishing peering may require corrective action.

---

# 10. Modification of Policy

This document may be updated periodically.  
Participants will be notified through the registry or community channels.

---

# 11. Contact

For peering requests with the Byte World Core:
- Create a GitHub Issue  
- Contact registry administrators  
- Join official community chat channels  

---

# Thank You for Peering with Byte World

Byte World exists to help people learn BGP, routing security, and Internet-style
network design in a safe environment.  
Your cooperation keeps the network stable and fun for everyone!
