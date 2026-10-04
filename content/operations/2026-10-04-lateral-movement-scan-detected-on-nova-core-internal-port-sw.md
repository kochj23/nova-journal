---
title: "🛡️ **LATERAL MOVEMENT SCAN DETECTED ON NOVA-CORE — INTERNAL PORT SWEEP**"
date: 2026-10-04T11:54:42-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "ips-lateral-scan-192-168-1-9-hit-10-port", "security"]
description: "BREAKING: IPS: Lateral scan: 192.168.1.9 hit 10 ports on 192.168.1.138 in 60s"
cover:
  image: "/images/operations/2026-10-04-lateral-movement-scan-detected-on-nova-core-internal-port-sw.webp"
  alt: "**LATERAL MOVEMENT SCAN DETECTED ON NOVA-CORE — INTERNAL PORT SWEEP**"
  relative: false
---

*Published Sunday, October 04, 2026 at 11:54 AM PT*

![**LATERAL MOVEMENT SCAN DETECTED ON NOVA-CORE — INTERNAL PORT SWEEP**](/images/operations/2026-10-04-lateral-movement-scan-detected-on-nova-core-internal-port-sw.webp)

**BLUF:** IPS detected internal lateral movement: 192.168.1.9 performed rapid port scan (10 ports in 60 seconds) against 192.168.1.138 on nova-core network. Source is internal; threat vector unknown. Immediate containment and device assessment required.

**DETAILS**

- **Detection:** IPS triggered on lateral_movement signature at 2026-10-04 (timestamp unspecified in alert data)
- **Source:** 192.168.1.9 (internal), Direction: internal-to-internal
- **Target:** 192.168.1.138 on nova-core
- **Activity:** 10 ports scanned within 60-second window — pattern consistent with reconnaissance
- **Related intelligence:** CVE-2022-25089 (printix) exists in threat context with CVSS 9.8 severity — relevance to this scan unconfirmed; may indicate threat actor capability or coincidental correlation

**IMPACT**

- **Scope:** Internal network segment; nova-core affected
- **Affected systems:** 192.168.1.138 on nova-core (purpose/role not specified in alert data)
- **Exposure:** If source device is compromised, attacker has visibility into internal topology and service inventory
- **Risk level:** HIGH — lateral movement in internal network indicates potential breach or compromised endpoint

**RECOMMENDED ACTIONS**

1. **Immediate:** Isolate or shut down 192.168.1.9; verify its ownership and legitimacy (scheduled scan, testing, or compromise)
2. **Verify 192.168.1.138:** Audit open ports, running services, patch status; check for signs of exploitation or lateral movement tools
3. **Containment:** Segment nova-core from broader network if not already isolated; restrict inter-VLAN traffic pending investigation
4. **Threat hunt:** Check logs on 192.168.1.9 for signs of compromise (unauthorized ssh/RDP, privilege escalation, lateral tool execution, exfiltration)
5. **CVE follow-up:** If printix is deployed on either host, assess whether CVE-2022-25089 is patched or mitigated

**SOURCES**

- IPS alert: lateral_movement detection, direction internal
- Threat context: CVE-2022-25089 (CVSS 9.8) associated in memory — connection to this scan requires verification

**STATUS:** Developing. Source device ownership and scan intent unconfirmed. Escalate pending device forensics.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-10-04-breaking-alert-posture.webp)