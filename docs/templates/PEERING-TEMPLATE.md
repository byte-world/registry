# Byte World Peering Template

This document provides a standardized template for publishing your peering
information within Byte World. Create a file under:

```

peering/AS<yourasn>.md

```

Example:
```

peering/AS4200001234.md

```

Fill in all applicable sections below.

---

# Peering Information for AS<YOUR ASN>

## 1. General Information

**AS Number:** AS<YOUR ASN>  
**AS Name:** <YOUR AS-NAME>  
**Operator Name:** <YOUR NAME / HANDLE>  
**Contact Email:** <you@example.com>  
**NOC Contact:** <noc@example.com> (Optional)  
**Website:** <https://your-site.example> (Optional)  
**Time Zone:** <UTC±X>  
**Location:** <Country / Region / VM>  

---

## 2. Peering Policy

Choose one:

- **Open** – Anyone may peer with this ASN.  
- **Selective** – Basic requirements listed below.  
- **Closed** – Peering only with approved networks.  

If selective or closed:

**Requirements to peer:**
- <example: must have IRR objects>
- <example: must support IPv6>
- <example: must maintain uptime of >70%>

---

## 3. WireGuard Tunnel Details

### Endpoint Information

**Endpoint IPv4:** <your public IPv4 or endpoint>  
**Endpoint IPv6:** <your IPv6 endpoint>  
**Port:** <51820 unless different>  
**Transport:** WireGuard / GRE / OpenVPN / IPIP / Other  

### WireGuard Configuration

```

[Interface]
PrivateKey = <REDACTED>
Address    = <your tunnel IPs>

[Peer]
PublicKey  = <your public key>
AllowedIPs = <peer tunnel IPs>
Endpoint   = <your endpoint:port>
PersistentKeepalive = 25

```

> ⚠️ **Do NOT publish private keys.**  
Only place your *public* keys and tunnel IPs.

---

## 4. Tunnel IP Assignments

```

My IPv4:  <your tunnel IPv4>
My IPv6:  <your tunnel IPv6>

Peer IPv4: <peer tunnel IPv4>
Peer IPv6: <peer tunnel IPv6>

```

You may also list additional tunnels if needed.

---

## 5. BGP Session Details

### IPv4 Session
```

Local ASN:   AS<YOUR ASN>
Remote ASN:  AS<PEER ASN>
Local IP:    <your v4 tunnel IP>
Remote IP:   <peer v4 tunnel IP>
Multihop:    <yes/no>
MD5:         <optional>

```

### IPv6 Session
```

Local ASN:   AS<YOUR ASN>
Remote ASN:  AS<PEER ASN>
Local IP:    <your v6 tunnel IP>
Remote IP:   <peer v6 tunnel IP>
Multihop:    <yes/no>
MD5:         <optional>

```

---

## 6. Prefixes Originated by This ASN

```

IPv4:

* <10.100.X.0/24>
* <other prefixes>

IPv6:

* [fd42:4242:xxxx::/64](fd42:4242:xxxx::/64)
* <other prefixes>

```

---

## 7. IRR (Internet Routing Registry) Records

```

aut-num:   AS<YOUR ASN>
mntner:    BW-MNT-<YOURNAME>
as-set:    AS-SET-<YOURNAME> (optional)
route:     <list your IPv4 routes>
route6:    <list your IPv6 routes>

```

---

## 8. Notes / Additional Information

- <any operational notes>
- <maintenance windows>
- <backup endpoints>
- <latency expectations>
- <QoS or routing policy details>

---

## 9. Last Updated

**Date:** YYYY-MM-DD  
**Maintainer:** <YOUR NAME / HANDLE>  

---

Thank you for peering with **Byte World**!
