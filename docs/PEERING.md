# ByteWorld Peering Guide

How to bring up a link with another ByteWorld node once you both have
registry entries.

## 1. Prerequisites

- You have a merged `aut-num` object (your ASN) and at least one
  `inetnum`/`inet6num` block.
- You've agreed out-of-band (Matrix/IRC) with your peer on a transfer
  `/31` (v4) and `/127` (v6) — usually carved from whichever side has
  free space closest to the link.
- Both sides run WireGuard for the underlay tunnel, and Bird2, FRR, or
  MikroTik RouterOS for BGP over it. Examples below cover all three.

## 2. WireGuard tunnel

```ini
# /etc/wireguard/bw-peername.conf
[Interface]
PrivateKey = <your-private-key>
ListenPort = 21000
Address = 172.20.0.1/31, fd00:beef:cafe:food::1/127

[Peer]
PublicKey = <their-public-key>
Endpoint = <their-ip-or-hostname>:21000
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```

Bring it up with `wg-quick up bw-peername`. Pick a distinct `ListenPort`
per peer if you're multi-homed.

## 3. BGP session

Run eBGP directly over the tunnel, AS-per-node (no route reflectors
needed for a mesh this size yet). Always filter to what's registered.

### Bird2

```
protocol bgp bw_peername {
    local as 4243000012;
    neighbor fd00:beef:cafe:food::2 as 4243000045;
    multihop 2;
    path metric 1;

    ipv4 {
        import filter { if (net ~ [172.20.0.0/14+]) then accept; else reject; };
        export where source = RTS_STATIC || source = RTS_BGP;
    };
    ipv6 {
        import filter { if (net ~ [fd00::/8+]) then accept; else reject; };
        export where source = RTS_STATIC || source = RTS_BGP;
    };
}
```

### FRR

```
router bgp 4243000012
 neighbor bw-peername peer-group
 neighbor fd00:beef:cafe:food::2 peer-group bw-peername
 neighbor fd00:beef:cafe:food::2 remote-as 4243000045
 !
 address-family ipv6 unicast
  neighbor bw-peername prefix-list BWNET-IN in
  neighbor bw-peername prefix-list BWNET-OUT out
 exit-address-family

ip prefix-list BWNET-IN seq 5 permit fd00::/8 le 32
```

### MikroTik RouterOS 7

```
/routing bgp connection
add name=bw-peername remote.address=fd00:beef:cafe:food::2 \
    remote.as=4243000045 local.as=4243000012 \
    input.filter=bwnet-import output.filter=bwnet-export \
    multihop=yes
```

## 4. Filtering — always filter to the registry

Never accept a full table or default from a bwnet peer, and never accept
prefixes that don't have a matching `route`/`route6` object with the
peer's ASN as origin. A future iteration of `scripts/validate.py` will
export generated prefix-lists per ASN so filters can be built
automatically rather than by hand — until then, check `registry/route/`
and `registry/route6/` manually when adding a peer.

## 5. Byte IX (optional)

If you're colocated at a Byte IX exchange point, you can peer over the
shared IX LAN instead of point-to-point WireGuard — see the IX page for
the LAN prefix and route server details. Route servers only reflect
routes that already pass registry validation, so IX peers still need
their objects merged first.
