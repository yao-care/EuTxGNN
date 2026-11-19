---
layout: default
title: Privacy Policy
parent: Documentation
nav_order: 4
description: "EuTxGNN Privacy Policy"
permalink: /privacy-policy/
---

# Privacy Policy
{: .fs-9 }

Last updated: 5 November 2026
{: .fs-6 .fw-300 }

---

## Overview

EuTxGNN ("we", "our", or "the platform") is committed to protecting your privacy. This policy explains how we handle information when you use our drug repurposing prediction platform.

---

## Information We Collect

### Automatically Collected Information

When you visit EuTxGNN, Google Analytics 4 collects the following through analytics cookies, which are set when a page loads:

- **Technical data**: Browser type, operating system, IP address
- **Usage data**: Pages visited, time spent, navigation patterns
- **Device information**: Screen resolution, device type

### SMART on FHIR Data

If you use the SMART on FHIR application:

- **Patient context**: The patient ID, name, birth date and gender read from your EHR, shown in the app
- **Medication data**: Current medications for repurposing lookup
- **Session data**: Temporary session tokens for EHR integration

**Note**: We do not store patient health information. Patient identity and EHR data are not sent to this site's servers (this is a static site with no backend) and are not retained. To match drug names, the app sends the medications' RxNorm codes (no patient identifiers) to the US National Library of Medicine's RxNav service; when you ask for clinical trials, the drug and indication names are sent to ClinicalTrials.gov. The SMART on FHIR client library keeps the EHR authorisation state in the browser's sessionStorage, which is cleared when the tab is closed.

---

## How We Use Information

We use collected information to:

- Provide and improve the platform
- Generate aggregated usage statistics
- Ensure platform security
- Support research and development

---

## Data Sharing

We do not sell personal information. We may share data with:

- **Service providers**: Hosting, analytics services
- **Research collaborators**: Aggregated, anonymized data only
- **Legal requirements**: When required by law

---

## Cookies and Tracking

The only cookies on this site are the Google Analytics 4 analytics cookies (such as `_ga`), used to compile usage statistics. They are set when a page loads. The site sets no cookies of its own for sessions or preferences.

You can disable cookies in your browser settings.

---

## Data Security

We implement appropriate security measures including:

- HTTPS encryption
- Regular security updates
- Access controls
- Data minimization

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Applicable law

For visitors in the EU and EEA the relevant law is the [General Data Protection Regulation (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj), applied together with national law in each member state; analytics cookies are also subject to the ePrivacy rules as implemented nationally. Each country has its own supervisory authority, listed by the [European Data Protection Board](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en). The operator is based in Taiwan with no EU establishment.

## Your rights and how to use them

- Right of access (Article 15) and rectification (Article 16).
- Right to erasure (Article 17) and restriction (Article 18).
- Right to object (Article 21), including to analytics.
- Right to lodge a complaint with the supervisory authority of your member state (Article 77).

Requests: service@yao.care (there are no accounts, so tell us the date and pages of your visit). Analytics cookies can be blocked or deleted in your browser.

## Copyright and data sources

Copyright in the EU is national law harmonised by [Directive 2001/29/EC](https://eur-lex.europa.eu/eli/dir/2001/29/oj); databases are covered by [Directive 96/9/EC](https://eur-lex.europa.eu/eli/dir/1996/9/oj). The site's code is published under the MIT License in the [GitHub repository](https://github.com/yao-care/EuTxGNN); report texts are © 藥提醒科技有限公司 (yao.care).

Data sources used on this site and their terms:

- **TxGNN** data (Harvard Dataverse): CC0 1.0; cite Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov**, **PubMed**: [ClinicalTrials.gov terms](https://clinicaltrials.gov/about-site/terms-conditions), [NCBI policies](https://www.ncbi.nlm.nih.gov/home/about/policies/).
- **DrugBank**: [DrugBank](https://go.drugbank.com/) licence terms, non-commercial use.
- **Local dataset** – [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), published by European Medicines Agency (EMA); reuse is governed by the publisher's terms, and this site does not grant any further rights.

<!-- privacy-law:end -->

---

## Third-Party Services

The site loads the following third-party resources, which may log access according to their own policies:

| Service | Purpose | Privacy policy |
|---------|---------|----------------|
| GitHub Pages | Site hosting | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Visit statistics (pages viewed, referrer); uses analytics cookies. Search terms, form contents and URL query strings are not sent. | [Google Privacy Policy](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Script libraries: d3 charts on every page; Fuse.js name matching and the SMART on FHIR client on the SMART pages and in the home-page drug lookup | [jsDelivr Privacy Policy](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Clinical-trial lookup on the SMART pages: only when you ask for trials, the drug and indication names are sent to the ClinicalTrials.gov API | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART app: the RxNorm codes of the medications read from your EHR are sent to the NLM RxNav API to look up ingredient names (no patient identifiers) | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |

---

## Third-Party Links

Our platform may contain links to external sites. We are not responsible for their privacy practices.

---

## Children's Privacy

EuTxGNN is intended for healthcare professionals and researchers. We do not knowingly collect information from children under 16.

---

## Changes to This Policy

We may update this policy periodically. Significant changes will be announced on the platform.

---

## Contact

For privacy-related inquiries, please open an issue on our [GitHub repository](https://github.com/yao-care/EuTxGNN).

---

## Research Use

This platform is provided for research purposes only. Use of prediction data should follow applicable ethical guidelines and institutional policies.
