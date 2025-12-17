# Byte World Security Policy

This Security Policy defines how security, incident response, reporting,
vulnerability disclosure, and operational integrity are handled within  
**Byte World**, a collaborative private networking environment focused on
learning and experimentation.

Byte World is not the public Internet — but security still matters.  
All participants are expected to follow these guidelines to ensure that the
network remains stable, safe, and enjoyable for all.

---

# 1. Purpose

The goals of this security policy are to:

- Protect the Byte World network from accidental or intentional harm  
- Establish clear expectations for responsible behavior  
- Define how incidents should be reported and handled  
- Encourage responsible experimentation with minimal disruption  
- Maintain trust between participants  

This applies to all systems, ASNs, tunnels, BGP sessions, and services within
Byte World.

---

# 2. Security Principles

Byte World follows these core principles:

### ✔ **Safety First**
Activities must not cause harm or significant disruption to the shared network.

### ✔ **Transparency**
Participants should report suspected issues openly and promptly.

### ✔ **Accountability**
Each ASN operator is responsible for the security and behavior of their network.

### ✔ **Minimal Privilege**
Only access or announce what is necessary for your ASN’s operation.

### ✔ **Isolation of Experiments**
High-risk experiments should be performed on separate tunnels or test ASNs.

---

# 3. Participant Responsibilities

Every member ASN must:

### 3.1 Maintain Secure Infrastructure
- Keep tunnel endpoints updated and patched  
- Use strong keys for WireGuard/OpenVPN  
- Secure routers against unauthorized access  
- Keep administrative interfaces private or authenticated  

### 3.2 Protect Peering Sessions
- Use BGP MD5 authentication where possible  
- Avoid exposing tunnels to the public internet without protections  
- Monitor for session flaps or suspicious behavior  

### 3.3 Keep Registry Data Accurate
- Update route/route6 objects immediately when allocations change  
- Remove stale or unused tunnels  
- Maintain active and reachable contact information  

### 3.4 Monitor Their Own Network
Participants are expected to:
- Detect misconfigurations  
- Fix leaks or incorrect advertisements quickly  
- Mitigate any instability they cause  

---

# 4. Prohibited Actions

The following actions are strictly forbidden in Byte World:

### ❌ Malicious Behavior
- Route hijacking  
- Fake IRR objects  
- Intentionally breaking or poisoning BGP  
- Injecting harmful attributes (AS_PATH poisoning without consent)  

### ❌ Attacks or Scanning
- DDoS or DoS attacks  
- Unauthorized port scanning  
- Attempting access to other participants' routers or services  
- Exploiting vulnerabilities without permission  

### ❌ Routing Misconduct
- Announcing public Internet prefixes  
- Announcing prefixes not assigned to your ASN  
- Creating routing loops intentionally  
- Excessive route flap storms  

Byte World is for learning — not chaos.

---

# 5. Vulnerability Reporting

Participants who discover a weakness, misconfiguration, or vulnerability are
expected to report it immediately and privately.

### Report via:
- Creating a *private* GitHub security issue (if enabled)  
- Contacting the registry maintainers  
- Messaging core operators via official community channels  

### Reports should include:
- Nature of the issue  
- Impact assessment (if known)  
- Steps to reproduce  
- Suggested mitigations  

**No public disclosure** should be made until the issue is resolved.

---

# 6. Incident Response Process

When a security event or major misconfiguration occurs:

### Step 1 — Detection  
A participant or monitoring system identifies abnormal behavior.

### Step 2 — Notification  
Affected peers and core operators are notified promptly.

### Step 3 — Containment  
Actions may include:
- Shutting down tunnels  
- Filtering malicious routes  
- Disabling BGP sessions  
- Temporarily removing the ASN from global announcements  

### Step 4 — Mitigation  
The operator responsible must resolve the issue as quickly as possible.

### Step 5 — Restoration  
Peering sessions and routes are restored once the network is safe.

### Step 6 — Post-Incident Review  
A short summary may be shared to help improve community practices.

---

# 7. Security Expectations for Core Services

Core services (registry, route-reflectors, monitoring nodes) must:

- Run stable and patched software  
- Maintain access logs  
- Restrict administrative access  
- Have backup plans and redundancy  
- Avoid sharing sensitive information  

Transparency is encouraged, exposure is not.

---

# 8. Cryptographic Requirements

### 8.1 Tunnel Security
- WireGuard keys **must not** be shared publicly  
- Periodically rotate keys  
- Use PersistentKeepalive (Optional but recommended)  

### 8.2 Authentication
- MD5 passwords for BGP sessions are recommended  
- SSH keys preferred over passwords  
- Avoid plaintext credentials in configs or public files  

---

# 9. Acceptable Research / Experiments

Allowed:
- BGP topology experiments  
- Route redistribution (within your ASN)  
- MPLS, EVPN, VXLAN in private tunnels  
- Traffic engineering between consenting peers  

Not allowed:
- Experiments that affect peers without consent  
- Experiments that intentionally break global Byte World stability  

When in doubt: isolate your experiment.

---

# 10. Enforcement

Security violations may result in:

1. **Warning**  
2. **Temporary suspension of peering**  
3. **Removal from core routing**  
4. **Permanent ban from Byte World**  

Severity depends on intent, impact, and cooperation.

---

# 11. Updates to This Policy

The Security Policy may evolve. Updates will be announced on the registry or
Byte World communication channels.

Participants are encouraged to suggest improvements.

---

# 12. Contact

For security incidents, vulnerabilities, or questions:

**Security Team / Registry Maintainers**  
Use official Byte World communication channels or GitHub private issues.

---

# Together We Keep Byte World Safe

Responsible experimentation builds trust, enables learning, and ensures the
network remains stable for everyone.  
Thank you for helping secure Byte World!
