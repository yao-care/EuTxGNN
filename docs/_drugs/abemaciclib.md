---
layout: default
title: Abemaciclib
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib (Verzenio) is a selective CDK4/6 inhibitor approved for the treatment of hormone receptor-positive (HR+), HER2-negative breast cancer.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **1 publication** currently supporting this direction.
Evidence remains at the indirect/pharmacovigilance stage, and a **Hold** decision is recommended pending mechanistic and preclinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HR+/HER2- Breast Cancer |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Abemaciclib is a selective CDK4/6 inhibitor: it blocks cyclin-dependent kinases 4 and 6, preventing phosphorylation of the retinoblastoma protein (Rb) and arresting the cell cycle at the G1/S checkpoint. This mechanism is established for HR+/HER2- breast cancer, where uncontrolled tumor cell proliferation is the primary driver.

The biological rationale for rheumatoid arthritis stems from the shared role of cell cycle dysregulation in inflammatory disease. CDK4/6 inhibition has been hypothesized to suppress proliferation of synovial fibroblasts and autoreactive T cells — two central mediators of RA pathology — thereby potentially dampening joint inflammation. This mechanistic overlap makes the TxGNN prediction biologically coherent at a theoretical level.

However, the only identified literature (PMID 40504547) is a retrospective pharmacovigilance study documenting the prevalence of **immune-mediated adverse events** (including autoimmune diseases) in breast cancer patients receiving CDK4/6 inhibitors. This evidence reflects safety surveillance, not therapeutic efficacy in RA. The mechanistic hypothesis therefore remains unvalidated, and the current evidence is insufficient to support clinical development in this indication without further preclinical work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Retrospective / Pharmacovigilance | The Oncologist | Documents prevalence of pre-existing and emerging autoimmune diseases in HR+/HER2- breast cancer patients receiving CDK4/6 inhibitors with endocrine therapy; identifies immune-mediated conditions as adverse events, not therapeutic outcomes — does not assess benefit in RA |

---

## Taiwan Market Information

Abemaciclib is not currently authorized in Taiwan. No product licenses are on record, and no dosage forms are registered.

> Note: Abemaciclib (Verzenio) holds regulatory approval in the United States (FDA, 2017) and the European Union (EMA) for HR+/HER2- breast cancer. Taiwan authorization status should be independently verified via the TFDA website.

---

## Cytotoxicity

Abemaciclib is a targeted antineoplastic agent (CDK4/6 inhibitor) used in breast cancer treatment. The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — CDK4/6 inhibitor (non-conventional cytotoxic; not an alkylating agent or antimetabolite) |
| Myelosuppression Risk | Moderate — neutropenia and lymphopenia are documented class effects; abemaciclib generally causes less grade 3/4 neutropenia than palbociclib but more diarrhea |
| Emetogenicity Classification | Low |
| Monitoring Items | Complete blood count (CBC) with differential, liver function tests (ALT/AST), renal function, signs of interstitial lung disease / pneumonitis |
| Handling Protection | Standard oral targeted therapy precautions; follow institutional cytotoxic handling guidelines for preparation and disposal |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Data gap: TFDA prescribing information (warnings and contraindications) was not available for this review (DG001 — Blocking severity). This represents a critical gap before any safety-dependent decision can be made. Drug-drug interaction data was also not retrieved (query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole available publication is a pharmacovigilance study reporting autoimmune conditions as adverse events in breast cancer patients treated with CDK4/6 inhibitors — this evidence works against the repurposing hypothesis rather than supporting it. While the mechanistic premise (CDK4/6 inhibition suppressing synovial fibroblast and T-cell proliferation) is biologically plausible, it is entirely unvalidated in any RA-specific model or patient population.

**To proceed, the following is needed:**

- **Preclinical studies**: In vitro and animal model data directly evaluating abemaciclib in RA contexts (e.g., collagen-induced arthritis or adjuvant-induced arthritis mouse models)
- **Mechanism data**: Retrieve full MOA profile from DrugBank API (DG002) to confirm CDK4/6 pathway relevance in immune cell biology
- **Safety baseline**: Obtain TFDA SmPC (DG001 — currently Blocking) to complete S1 safety pre-screening
- **Immune biology assessment**: Review CDK4/6 expression and activity data in RA synovial tissue and peripheral blood T cells from existing datasets

---

> **Note on secondary candidates:** Among the 10 TxGNN predictions evaluated in this batch, **Amyotrophic Lateral Sclerosis (ALS)** (Rank 10) carries the most mechanistically compelling repurposing rationale. Abemaciclib has been directly shown in cell-based assays (PMID 38596406) to accelerate autophagic clearance of TDP-43 aggregates — a pathological hallmark present in ~97% of ALS patients. Despite its lower TxGNN rank (97.32% vs. 96.23%), ALS warrants prioritized preclinical follow-up over the top-ranked RA indication given the strength of its mechanistic hypothesis and the high unmet medical need.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

