---
layout: default
title: Cyclosporine
parent: Medium Evidence (L3-L4)
nav_order: 162
evidence_level: L4
indication_count: 7
last_modified_at: 2026-11-12
description: "Cyclosporine: predicted new indication Granulomatous disease, chronic, autosomal recessive (evidence level L4). Approved use: Treatment of moderate to severe dry eye disease (keratoconjunctivitis…"
monitor_inn: "cyclosporine"
predicted_indications: ["granulomatous disease, chronic, autosomal recessive", "brain aneurysm", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congenital ichthyosiform erythroderma", "fetal erythroblastosis", "brachydactyly-syndactyly syndrome", "prolapse of lacrimal gland"]
---

# Cyclosporine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Cyclosporine: From Dry Eye Disease to granulomatous disease, chronic, autosomal recessive
{: .text-alpha }

## One-Sentence Summary

Cyclosporine is a calcineurin inhibitor, authorized in the EU as an ophthalmic product for dry eye disease and vernal keratoconjunctivitis.
The TxGNN model predicts it may be effective for **autosomal recessive chronic granulomatous disease (CGD)**, but there are currently **0 clinical trials** and only **1 publication**, which is indirect evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of moderate to severe dry eye disease (keratoconjunctivitis sicca) in adult patients, which has not improved despite treatment with tear substitutes |
| Predicted New Indication | Granulomatous disease, chronic, autosomal recessive |
| TxGNN Prediction Score | 0.9968 |
| Evidence Level | L4 |
| EU Market Status | Marketed (valid licences: 3 of 3) |
| Number of Authorizations | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, cyclosporine is a calcineurin inhibitor that suppresses T-cell activation. Its efficacy in inflammatory eye disease (dry eye disease, vernal keratoconjunctivitis) is established, and mechanistically it might be applicable to immune-dysregulation conditions.

The link to CGD is weak. The only retrieved publication is a 2012 cohort study on stem cell transplantation for CGD. In transplantation, calcineurin inhibitors are typically used for graft-versus-host disease prophylaxis. This does not show that cyclosporine treats CGD itself. The high TxGNN score most likely reflects network proximity to immune and inflammatory pathways rather than demonstrated efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohort | J Allergy Clin Immunol | Survival after sibling or unrelated donor stem cell transplantation in CGD was excellent. This is indirect evidence, as it does not evaluate cyclosporine as a treatment for CGD. |

---

## EU Market Information

All three authorizations are currently valid.

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002066 | Ikervis | ciclosporin | Valid |
| EMEA/H/C/004411 | Verkazia | ciclosporin | Valid |
| EMEA/H/C/006250 | Vevizye | ciclosporin | Valid |

<!-- licenses:end -->

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The drug-disease contraindication links in the TxGNN knowledge graph include hypertension, kidney disease, liver disease, epilepsy, infectious diseases (including eye infections and conjunctivitis), hyperbilirubinemia (including Gilbert syndrome), hypertriglyceridemia, thrombocytopenic purpura, intracranial hypertension (pseudotumor cerebri), and cancers (including lymphoma and primary CNS lymphoma). These need to be checked against the SmPC.
- **Drug Interactions:** 823 interactions were recorded. Examples include:
  - **Major:** Loperamide
  - **Moderate:** Rabeprazole, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, amphotericin B, bupropion, aprepitant, mesalazine, acetylsalicylic acid, metronidazole
  - **Minor:** Ranitidine, doxycycline

Please refer to the SmPC for the full label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no clinical trials, and the single publication concerns stem cell transplantation, not cyclosporine treatment. The label safety data is unavailable.

<!-- review:begin eu-lic-20261106-cyclosporine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The EU authorizations are all cancelled, and the label safety data is unavailable." Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 3 EU marketing authorisations for this drug, 3 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-cyclosporine-1 -->

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to enable a mechanistic analysis
- Label warnings and contraindications from the EU product information
- Direct preclinical or clinical evidence of cyclosporine in CGD
- Assessment of route and formulation compatibility, since existing EU products are ophthalmic and CGD would likely need systemic exposure

<!-- review:begin eu-lic-20261106-cyclosporine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Assessment of route and formulation compatibility, since existing EU products are ophthalmic and CGD would likely need systemic exposure / Clarification of why the EU authorizations were cancelled" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 3 EU marketing authorisations for this drug, 3 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-cyclosporine-2 -->

---

**Other predicted indications (all on hold):**

| Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|
| Brain aneurysm | 0.9950 | L5 | Only small 1990s studies on vasospasm after subarachnoid hemorrhage, a complication of rupture rather than aneurysm treatment. A 2017 animal study found T cells are dispensable for aneurysm formation. |
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9939 | L5 | Prediction only |
| Congenital ichthyosiform erythroderma | 0.9938 | L5 | Prediction only; speculative link to skin inflammation |
| Fetal erythroblastosis | 0.9937 | L5 | Only an in vitro bilirubin transport study |
| Brachydactyly-syndactyly syndrome | 0.9931 | L5 | Prediction only |
| Prolapse of lacrimal gland | 0.9908 | L5 | Prediction only; structural problem with loose proximity to approved eye indications |

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "he EU authorizations are all cancelled, and t" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-06 | Removed: "Clarification of why the EU authorizations were cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

