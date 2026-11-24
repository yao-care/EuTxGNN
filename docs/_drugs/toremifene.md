---
layout: default
title: Toremifene
parent: AI Predictions (L5)
nav_order: 630
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Toremifene: predicted new indication HIV infectious disease (evidence level L5). Approved use: First line hormone treatment of hormone-dependent metastatic breast c…"
monitor_inn: "Toremifene"
predicted_indications: ["HIV infectious disease"]
---

# Toremifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Toremifene: From Hormone-Dependent Metastatic Breast Cancer to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Toremifene was originally approved in the EU as first-line hormone treatment for hormone-dependent metastatic breast cancer in postmenopausal patients.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **0 clinical trials** and only **1 preclinical publication** (on an antifungal effect, not on HIV itself) supporting this direction.
The prediction is therefore a computational signal with no clinical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | First line hormone treatment of hormone-dependent metastatic breast cancer in postmenopausal patients. Fareston is not recommended for patients with estrogen receptor negative tumours. |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 (model prediction only; no actual studies on HIV) |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for toremifene: "Toremifene is a nonsteroidal triphenylethylene derivative. Toremifene binds to estrogen receptors and may exert estrogenic, antiestrogenic, or both activities, depending upon the duration of treatment, animal species, gender, target organ, or endpoint selected." ([DailyMed: Fareston (toremifene citrate) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2cab8dd1-3a10-48e6-86ce-0e5275ed49e5), label version 2024-11-13; accessed 2026-11-19.) Based on known information, toremifene is a selective estrogen receptor modulator (SERM) related to tamoxifen. Its efficacy in hormone-dependent breast cancer is established, but no direct mechanism links it to HIV.

The only linked paper (PMID 24520056) shows that estrogen receptor antagonists, including toremifene, have antifungal activity against *Cryptococcus*. They act by binding EF-hand proteins such as calmodulin and work together with fluconazole in the laboratory. This is relevant to an opportunistic fungal infection that affects people with HIV, not to HIV replication or disease progression. The high score of 0.9941 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Preclinical (in vitro/in vivo antifungal study) | mBio | Tamoxifen and toremifene are fungicidal against *Cryptococcus* and synergize with fluconazole and amphotericin B. Activity is linked to binding of EF-hand proteins. This does not show an effect on HIV. |

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000091 | Fareston | toremifene | Valid |

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, SERM class. It is not a conventional cytotoxic agent. |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions. Leukopenia and thrombocytopenia appear among the knowledge-graph contraindication links. |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions. Given the QT-related concerns below, ECG and electrolyte monitoring are reasonable considerations. |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes, thrombocytopenia, potassium deficiency disease, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, leukopenia, endometrial hyperplasia.
- **Drug interactions:** 100 interactions are recorded. The 20 reviewed include these **Major** interactions: dexamethasone, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), dolasetron, palonosetron, sodium sulfate and levofloxacin. Many of these are QT-prolonging or electrolyte-altering drugs. Moderate interactions include famotidine, cimetidine, pioglitazone, loperamide, aprepitant, bisacodyl, miconazole, nateglinide, lactitol and lactulose.

Please refer to the SmPC for the full label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction has a very high model score but no clinical trials and no evidence of anti-HIV activity. The single linked paper concerns an antifungal effect. The QT-related and interaction risks are significant in a population that often takes many medicines.

<!-- review:begin eu-lic-20261106-toremifene-2 -->

> **Review correction (2026-11-24)**: Originally stated: "The EU authorization is cancelled, and the QT-related and interaction risks are significant in a population that often takes many medicines." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-toremifene-2 -->

**To proceed, the following is needed:**
- Laboratory evidence that toremifene directly inhibits HIV replication, or a defined mechanism linking it to HIV disease
- Mechanism of action (MOA) data
- Safety, QT-risk and interaction assessment for people with HIV on antiretroviral therapy
- Review of the SmPC warnings and contraindications, which are not yet available

<!-- review:begin eu-lic-20261031-toremifene-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Review of the SmPC warnings and contraindications, which are not yet available / Clarification of current availability, since the only EU authorization is cancelled" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-toremifene-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Clarification of current availability, since the only EU authorization is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-24 | Removed: "he EU authorization is cancelled, and t" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fareston (toremifene citrate) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2cab8dd1-3a10-48e6-86ce-0e5275ed49e5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

