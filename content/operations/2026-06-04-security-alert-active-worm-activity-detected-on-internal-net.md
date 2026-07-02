---
title: "🛡️ 🚨 SECURITY ALERT — ACTIVE WORM ACTIVITY DETECTED ON INTERNAL NETWORK"
date: 2026-06-04T12:46:48-07:00
draft: false
categories: ["operations"]
tags: ["breaking", "alert", "ips:", "worm:", "et"]
description: "BREAKING: IPS: worm: ET WORM TheMoon.linksys.router 1 SRC=192.168.1.42 DST=192.168.1.1 SPT=5432"
cover:
  image: "/images/operations/2026-06-04-security-alert-active-worm-activity-detected-on-internal-net.webp"
  alt: "🚨 SECURITY ALERT — ACTIVE WORM ACTIVITY DETECTED ON INTERNAL NETWORK"
  relative: false
---

![🚨 SECURITY ALERT — ACTIVE WORM ACTIVITY DETECTED ON INTERNAL NETWORK](/images/operations/2026-06-04-security-alert-active-worm-activity-detected-on-internal-net.webp)

**BLUF:** A device at 192.168.1.42 is exhibiting worm behavior consistent with TheMoon malware targeting Linksys routers. The attack was directed at the network gateway (192.168.1.1). The UDM-Pro IPS blocked the attempt. Immediate device isolation and investigation required.

---

## DETAILS

- IPS signature **ET WORM TheMoon.linksys.router** triggered on UDM-Pro; action taken was **block** — the attack did not reach the gateway
- Source device **192.168.1.42** initiated the connection on source port **5432** targeting the gateway at **192.168.1.1**
- TheMoon is a known worm that exploits vulnerabilities in Linksys (and similar SOHO) routers to propagate, execute unauthorized commands, and enlist devices into proxy botnets
- Direction logged as **inbound** to the UDM-Pro's inspection engine — originating from inside the local network segment
- **No additional context is available** on the identity, type, or current state of the device at 192.168.1.42 — nature and extent of compromise on that host is **unconfirmed**

---

## IMPACT

- **Affected:** Device at 192.168.1.42 (identity unknown — investigate immediately); network gateway 192.168.1.1
- **Scope:** Contained to local network segment at this time; IPS block prevented gateway exploitation
- **Risk if unmitigated:** Successful router compromise could enable traffic interception, DNS hijacking, lateral movement, or enrollment in a proxy botnet
- **Unknown:** Whether 192.168.1.42 has made additional outbound or lateral connections not captured by this alert; whether other internal hosts have been targeted

---

## RECOMMENDED ACTIONS

1. **Isolate 192.168.1.42 immediately** — remove from network or apply a block rule at the UDM-Pro until the device is identified and assessed
2. **Identify the device** — check DHCP leases, ARP tables, and UDM-Pro client lists to determine device type and owner
3. **Review IPS/firewall logs** for any additional signatures or connections from 192.168.1.42, particularly outbound to known TheMoon C2 infrastructure
4. **Check the gateway (192.168.1.1)** for signs of tampering — verify firmware integrity, admin credentials, and configuration
5. **Scan the network** for additional devices exhibiting similar behavior; TheMoon is self-propagating and may have spread from another host
6. **Do not reconnect** 192.168.1.42 until it has been fully reimaged or confirmed clean

---

## SOURCES

- UDM-Pro IPS Event Log — ET WORM TheMoon.linksys.router 1
- Emerging Threats signature database (ET WORM ruleset)
- TheMoon worm — publicly documented threat (first observed 2014; variants active through present)