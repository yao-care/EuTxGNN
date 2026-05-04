---
layout: default
title: Abiraterone
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Abiraterone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Abiraterone: From Prostate Cancer to Migraine Disorder

## One-Sentence Summary

Abiraterone is a CYP17A1 inhibitor used for castration-resistant prostate cancer, suppressing androgen synthesis to deprive androgen-driven tumors of their growth signals. The TxGNN model predicts it may be effective for **Migraine Disorder** (score: 98.81%), but there are currently **no clinical trials** and **no direct publications** supporting this repurposing direction. Evidence is entirely model-derived, placing this candidate at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (castration-resistant) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Abiraterone irreversibly inhibits CYP17A1 (17α-hydroxylase/C17,20-lyase), a key enzyme in the steroidogenesis cascade. By blocking this step, abiraterone dramatically lowers circulating testosterone and DHEA levels — a mechanism specifically designed to starve androgen-sensitive prostate tumors of their primary growth driver.

Sex hormones, including androgens, have documented roles in migraine biology. Menstrual migraine is a well-characterized clinical entity, and fluctuations in sex hormone levels are known to affect trigeminal sensitization and CGRP-mediated nociceptive pathways. Androgens have also been shown to modulate pain perception via trigeminal vascular tone. On this basis, the TxGNN model may have identified a hormonal axis connecting androgen suppression to migraine vulnerability.

However, the mechanistic direction is uncertain and potentially unfavorable. Reducing androgens via CYP17A1 inhibition might either attenuate or exacerbate migraine depending on the patient's hormonal context (e.g., postmenopausal women vs. men vs. premenopausal women). No preclinical migraine model data, no mechanistic studies, and no clinical observations have examined this pairing. The prediction score reflects AI-derived graph patterns, not biological validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature directly investigating Abiraterone for migraine is available.

> **Note:** A PubMed search for the related indication "migraine with or without aura, susceptibility to" returned 20 publications. However, upon review, all 20 papers address epilepsy-migraine comorbidity genetics (MTHFR polymorphism, KCNJ10 variants, shared channelopathies, etc.) and contain no investigation of Abiraterone as a treatment candidate. These papers are therefore excluded from evidence tabulation.

---

## Taiwan Market Information

Abiraterone is not currently approved or marketed in Taiwan. No regulatory authorizations are on record.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted hormone therapy — Androgen biosynthesis inhibitor (CYP17A1 inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not a direct mechanism of toxicity; no bone marrow suppression via cytotoxic pathway) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT/AST), serum potassium (mineralocorticoid excess risk), blood pressure, fluid retention, cardiac function |
| Handling Protection | Standard precautions for orally administered hormone-active antineoplastic agents; dedicated cytotoxic handling protocols may not be mandatory but institutional guidelines should be followed |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (98.81%), there is zero supporting clinical or preclinical evidence for Abiraterone in migraine. The mechanistic hypothesis — androgen pathway modulation influencing trigeminal sensitization — is biologically plausible in direction but entirely unvalidated, and the net clinical effect of profound androgen suppression on migraine remains unknown and potentially harmful.

**To proceed, the following is needed:**
- Preclinical studies examining the effect of CYP17A1 inhibition on validated migraine animal models (e.g., CGRP-sensitization models, NTG-induced allodynia models)
- Mechanistic data clarifying whether androgen reduction suppresses or augments trigeminal vascular activation
- Epidemiological analysis of migraine incidence in prostate cancer patients receiving Abiraterone vs. other androgen deprivation therapies
- Full safety profile review via the TFDA SmPC (currently not available for Taiwan)
- Pharmacokinetic assessment for CNS penetration, as migraine treatment may require central nervous system exposure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

