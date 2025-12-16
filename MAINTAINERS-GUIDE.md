# Byte World Maintainers Guide

This document is intended for **registry maintainers and administrators**.
It defines responsibilities, workflows, and best practices.

---

## 1. Role of a Maintainer

Maintainers are trusted stewards of Byte World.
They are responsible for:
- Registry integrity
- Fair resource allocation
- Policy enforcement
- Community safety

Maintainers should act impartially and professionally.

---

## 2. Registry Responsibilities

Maintainers must:
- Review Pull Requests
- Validate object formatting
- Prevent duplicate allocations
- Ensure policy compliance
- Maintain directory structure consistency

---

## 3. Allocation Guidelines

When assigning resources:
- Allocate minimally by default
- Require justification for large requests
- Prefer `/64` for IPv6, `/28` or smaller for IPv4
- Assign one ASN per participant unless justified

Consistency is more important than speed.

---

## 4. PR Review Checklist

Before merging:
- Objects follow naming conventions
- ASN/IP not already assigned
- Correct `mnt-by` references
- Valid `origin:` ASN
- No unauthorized edits

If unsure, request changes.

---

## 5. Incident Handling

In case of:
- Route leaks
- Hijacks
- Abuse
- Misconfigurations

Maintainers may:
- Temporarily filter routes
- Suspend peering
- Request immediate fixes

Document major incidents when resolved.

---

## 6. Security & Privacy

Maintainers must:
- Protect private keys and credentials
- Avoid sharing personal data
- Use secure authentication
- Limit access to sensitive systems

---

## 7. Conflict Resolution

Maintainers should:
- Remain neutral
- De-escalate conflicts
- Encourage cooperation
- Apply policy consistently

Personal disputes must not influence decisions.

---

## 8. Stepping Down

Maintainers may step down at any time.
Inactive maintainers may be removed after notice.

Smooth handover is encouraged.

---

## 9. Final Notes

Being a maintainer is a responsibility, not a privilege.
Lead by example, communicate clearly, and prioritize the community.
