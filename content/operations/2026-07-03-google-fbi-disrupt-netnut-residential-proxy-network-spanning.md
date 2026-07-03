---
title: "🛡️ **GOOGLE, FBI DISRUPT NETNUT RESIDENTIAL PROXY NETWORK SPANNING ~2 MILLION COMPROMISED DEVICES**"
date: 2026-07-03T07:30:26-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "securityweek-google-fbi-disrupt-netnut-r", "security"]
description: "BREAKING: SecurityWeek: Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices"
cover:
  image: "/images/operations/2026-07-03-google-fbi-disrupt-netnut-residential-proxy-network-spanning.webp"
  alt: "**GOOGLE, FBI DISRUPT NETNUT RESIDENTIAL PROXY NETWORK SPANNING ~2 MILLION COMPROMISED DEVICES**"
  relative: false
---

*Published Friday, July 03, 2026 at 07:30 AM PT*

![**GOOGLE, FBI DISRUPT NETNUT RESIDENTIAL PROXY NETWORK SPANNING ~2 MILLION COMPROMISED DEVICES**](/images/operations/2026-07-03-google-fbi-disrupt-netnut-residential-proxy-network-spanning.webp)

**BLUF:** U.S. law enforcement and Google have disrupted NetNut, a residential proxy service that rented access to millions of compromised home devices to cybercriminals and state-sponsored actors for masking attack origins. Organizations should assume devices on their networks may have been compromised and review proxy/VPN traffic logs for suspicious activity.

---

**DETAILS**

- NetNut operated a residential proxy network leveraging approximately 2 million compromised home devices, providing anonymization services to malicious actors
- Google and FBI coordinated the disruption; FBI seized the NetNut platform infrastructure
- The service enabled threat actors—including nation-state operators—to conduct attacks while masking their true IP addresses and geographic origin
- Related disruption activity also targeted the Popa botnet and associated malware infrastructure (Amadey, StealC malware families mentioned in concurrent enforcement actions)
- Exact timeline of compromise for individual devices remains unclear; some devices may have been infected for extended periods

---

**IMPACT**

- **Scope:** Potentially millions of residential internet users globally whose devices were unknowingly enrolled in the proxy network
- **Affected parties:** Home network administrators, ISPs, organizations conducting threat intelligence on proxy infrastructure
- **Attack surface:** Compromised devices could have been used for credential theft, malware distribution, DDoS attacks, reconnaissance, and fraud
- **Residual risk:** Devices may remain infected with underlying malware; disruption of proxy access does not guarantee device remediation

---

**RECOMMENDED ACTIONS**

- Review firewall and proxy logs for suspicious outbound connections or unusual traffic patterns to residential IP ranges
- If managing home networks: run updated antivirus/anti-malware scans; check for unauthorized proxy configurations
- Monitor for indicators of compromise (IoCs) released by Google Threat Intelligence and FBI
- Coordinate with ISPs if suspicious device behavior is detected on your network perimeter
- Assume credential exposure if devices accessed corporate VPNs or authentication systems

---

**SOURCES**

SecurityWeek, The Hacker News, The Register, Krebs on Security, Google Threat Intelligence, FBI, CISA