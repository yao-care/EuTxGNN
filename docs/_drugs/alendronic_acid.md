---
layout: default
title: Alendronic Acid
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alendronic Acid
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

# Alendronic acid: From Osteoporosis to HIV Infectious Disease

## One-Sentence Summary

Alendronic acid is a bisphosphonate with well-established efficacy in treating osteoporosis by inhibiting osteoclast-mediated bone resorption.
The TxGNN model predicts it may be effective for **HIV infectious disease** — specifically in managing the accelerated bone mineral density loss caused by HIV infection and antiretroviral therapy —
with **4 clinical trials** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis (established use; not registered in Taiwan) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 96.78% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from our dataset. Based on known pharmacological information, alendronic acid is a bisphosphonate that inhibits osteoclast-mediated bone resorption by binding to hydroxyapatite crystals in bone. Its efficacy in preventing and treating osteoporosis has been well-established across multiple patient populations worldwide.

HIV infection and antiretroviral therapy (ART) — particularly tenofovir-containing regimens — are independently associated with accelerated bone mineral density (BMD) loss, frequently progressing to secondary osteoporosis and elevated fracture risk. The underlying mechanism is two-fold: chronic HIV-related immune activation disrupts the balance between osteoblasts and osteoclasts, while tenofovir directly impairs renal phosphate reabsorption, further reducing BMD.

Alendronic acid addresses this complication directly by suppressing osteoclast activity and halting further bone loss in HIV-infected patients. Importantly, this is a **repurposing for a HIV-related complication (secondary osteoporosis)**, not a claim of direct antiviral activity. The landmark ANRS 120 Fosivir Phase 3 trial directly confirms this efficacy, making the TxGNN prediction both mechanistically sound and clinically validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00120757](https://clinicaltrials.gov/study/NCT00120757) | Phase 3 | Completed | 140 | ANRS 120 Fosivir: Alendronate vs. placebo in HIV-1-associated primary osteoporosis over 2 years, with all patients receiving calcium and vitamin D supplementation |
| [NCT00061256](https://clinicaltrials.gov/study/NCT00061256) | Phase 2 | Completed | 80 | Double-blind, placebo-controlled RCT of once-weekly alendronate plus calcium/vitamin D in HIV-infected subjects with decreased BMD; assessed safety and efficacy |
| [NCT00921557](https://clinicaltrials.gov/study/NCT00921557) | Phase 2 | Completed | 52 | Oral alendronate for low BMD in HIV-infected children and adolescents; measured lumbar spine BMD changes at 24 and 48 weeks — important paediatric cohort extension |
| [NCT02322099](https://clinicaltrials.gov/study/NCT02322099) | Phase 4 | Terminated | 53 | Short-course alendronate vs. placebo to prevent ART-initiation-related BMD loss in ART-naïve HIV-1-infected adults; terminated early, limiting interpretability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [25300622](https://pubmed.ncbi.nlm.nih.gov/25300622/) | 2014 | Systematic Review / Meta-analysis | AIDS Reviews | Pooled analysis of 8 RCTs evaluating bisphosphonates (including alendronate) in HIV-infected adults; assessed BMD changes at lumbar spine, femoral neck, and total hip using fixed-effects model |
| [26890207](https://pubmed.ncbi.nlm.nih.gov/26890207/) | 2016 | Narrative Review | Current Opinion in HIV and AIDS | Clinical review of pharmacologic strategies to prevent and manage low BMD in people living with HIV, highlighting fracture risk, monitoring recommendations, and bisphosphonate utility |

---

## Taiwan Market Information

Alendronic acid is currently **not registered in Taiwan** (市場狀態：未上市). No marketing authorizations have been issued by the Taiwan Food and Drug Administration (TFDA). Clinicians should consult international regulatory approvals (e.g., FDA, EMA) and the corresponding Summary of Product Characteristics (SmPC) when assessing dosing, contraindications, and drug interactions.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> ⚠️ **Note**: TFDA prescribing information (warnings and contraindications) has not been retrieved for this report. This is a **blocking data gap** (DG001) that must be resolved before clinical use assessment. In particular, alendronate has a known risk of oesophageal irritation, which is relevant given its oral administration requirements (patient must remain upright for 30 minutes post-dose).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ANRS 120 Fosivir Phase 3 RCT (NCT00120757) directly demonstrates alendronate's efficacy for HIV-1-associated osteoporosis, corroborated by two additional completed Phase 2 RCTs and a meta-analysis covering 8 randomised trials — satisfying the L1 evidence threshold. The mechanistic link is well-understood and the target population (HIV patients with bone loss on ART) is clearly defined.

**To proceed, the following is needed:**

- **DG001 (Blocking)**: Retrieve TFDA prescribing information for local warnings and contraindications — required before any safety assessment can proceed
- **DG002 (High)**: Confirm mechanism of action via DrugBank API to support mechanistic gap analysis
- **Population scoping**: Formally define the target indication as "secondary osteoporosis in HIV-infected patients on ART" rather than HIV itself, to align regulatory framing and avoid misrepresentation
- **Safety monitoring plan**: Address renal function monitoring (especially in tenofovir-treated patients), oesophageal tolerability, and calcium/vitamin D co-supplementation requirements
- **Paediatric consideration**: The Phase 2 paediatric trial (NCT00921557) signals potential use in perinatally HIV-infected children — a distinct regulatory pathway may be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

