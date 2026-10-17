---
layout: default
title: Cyclosporine
parent: Medium Evidence (L3-L4)
nav_order: 162
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-15
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

# Cyclosporine: From Dry Eye Disease to Chronic Granulomatous Disease

## One-Sentence Summary

Cyclosporine is a calcineurin inhibitor, authorized in the EU as an ophthalmic product for dry eye disease and vernal keratoconjunctivitis.
The TxGNN model predicts it may be effective for **autosomal recessive chronic granulomatous disease (CGD)**, but there are currently **0 clinical trials** and only **1 publication**, which is indirect evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of moderate to severe dry eye disease (keratoconjunctivitis sicca) in adult patients, which has not improved despite treatment with tear substitutes |
| Predicted New Indication | Granulomatous disease, chronic, autosomal recessive |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
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

All three authorizations are currently cancelled.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/006250 | Vevizye | Not specified | Treatment of moderate to severe dry eye disease (keratoconjunctivitis sicca) in adult patients, which has not improved despite treatment with tear substitutes. |
| EMEA/H/C/004411 | Verkazia | Not specified | Treatment of severe vernal keratoconjunctivitis (VKC) in children from 4 years of age and adolescents. |
| EMEA/H/C/002066 | Ikervis | Not specified | Treatment of severe keratitis in adult patients with dry eye disease, which has not improved despite treatment with tear substitutes. |

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
The prediction rests on a computational score alone. There are no clinical trials, and the single publication concerns stem cell transplantation, not cyclosporine treatment. The EU authorizations are all cancelled, and the label safety data is unavailable.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to enable a mechanistic analysis
- Label warnings and contraindications from the EU product information
- Direct preclinical or clinical evidence of cyclosporine in CGD
- Assessment of route and formulation compatibility, since existing EU products are ophthalmic and CGD would likely need systemic exposure
- Clarification of why the EU authorizations were cancelled

---

**Other predicted indications (all on hold):**

| Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|
| Brain aneurysm | 99.50% | L3 | Only small 1990s studies on vasospasm after subarachnoid hemorrhage, a complication of rupture rather than aneurysm treatment. A 2017 animal study found T cells are dispensable for aneurysm formation. |
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.39% | L5 | Prediction only |
| Congenital ichthyosiform erythroderma | 99.38% | L5 | Prediction only; speculative link to skin inflammation |
| Fetal erythroblastosis | 99.37% | L5 | Only an in vitro bilirubin transport study |
| Brachydactyly-syndactyly syndrome | 99.31% | L5 | Prediction only |
| Prolapse of lacrimal gland | 99.08% | L5 | Prediction only; structural problem with loose proximity to approved eye indications |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

