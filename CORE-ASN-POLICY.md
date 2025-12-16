# Byte World Core ASN Policy

This document defines the role, responsibilities, and routing behavior of the
**Byte World Core ASN (AS4200000000)**.

The Core ASN acts as the backbone and coordination point for Byte World.
It exists to improve connectivity, not to control participants.

---

## 1. Purpose of the Core ASN

The Core ASN provides:

- Initial connectivity for new participants
- A stable routing anchor
- Optional route reflection
- Optional default routing (disabled by default)
- Core services reachability (DNS, registry, monitoring)

The Core ASN is **neutral infrastructure**, not a transit monopoly.

---

## 2. Core ASN Principles

The Core ASN operates under these principles:

- **Neutrality** — no preference between participants
- **Transparency** — documented behavior
- **Minimal filtering** — only what is required for safety
- **Stability-first** — avoid experimental configs
- **Opt-in services** — nothing is forced

---

## 3. Import Policy (Core ASN)

The Core ASN imports:

- Routes originated by registered Byte World ASNs
- Prefixes within authorized Byte World address space
- Routes with valid IRR objects

The Core ASN rejects:
- Public Internet prefixes
- Unregistered space
- Mis-originated routes
- Default routes (unless explicitly enabled)

---

## 4. Export Policy (Core ASN)

The Core ASN exports:

- All validated Byte World routes
- Core infrastructure prefixes
- Optional default route (explicit request only)

Exports may be filtered if:
- A participant misbehaves
- A prefix causes instability
- Security incidents occur

---

## 5. Default Route Policy

Default routes (`0.0.0.0/0`, `::/0`) are:

- **Disabled by default**
- Provided only upon request
- Intended for:
  - New users
  - Lab simplicity
  - Controlled experiments

Default routes may be withdrawn at any time.

---

## 6. Route Reflection & Servers

The Core ASN may operate:

- Route reflectors
- Route servers
- IX-style RS instances

Participation is:
- Optional
- Non-exclusive
- Clearly documented

Route servers do not modify policy beyond basic safety filtering.

---

## 7. Filtering & Safety Controls

The Core ASN enforces:

- Prefix length sanity checks
- ASN range validation
- IRR existence checks
- Max-prefix limits
- Dampening for excessive flaps

These controls protect the mesh, not restrict learning.

---

## 8. Anycast & Core Services

The Core ASN may announce Anycast prefixes for:

- DNS
- NTP
- WHOIS / IRR
- Monitoring
- Registry access

These prefixes are:
- Clearly documented
- Stable
- Not used for experiments

---

## 9. Abuse Handling

If a participant connected to the Core ASN:

- Leaks routes
- Hijacks prefixes
- Causes instability
- Violates security policy

The Core ASN may:
1. Filter the offending routes
2. Disable peering temporarily
3. Suspend announcements
4. Escalate to registry maintainers

Restoration requires corrective action.

---

## 10. Operational Transparency

Core ASN operators commit to:

- Documenting major changes
- Announcing maintenance
- Explaining filtering actions when possible
- Remaining reachable during incidents

---

## 11. Changes to This Policy

This policy may evolve.
Changes follow the Governance process and will be documented publicly.

---

## 12. Final Statement

The Byte World Core ASN exists to **enable**, not dominate.
Its role is to help participants learn, connect, and build
their own networks safely.

Trust the core — and verify it.
