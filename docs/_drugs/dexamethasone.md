---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Inflammatory & Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid widely used for its anti-inflammatory and immunosuppressive effects across allergic reactions, autoimmune disorders, and a broad range of inflammatory conditions. The TxGNN model predicts it may be effective for **Alopecia Areata** — an autoimmune hair loss disorder in which CD8+ T cells disrupt the immune privilege of hair follicles — with a prediction score of **99.99%**. This is supported by **20 publications**, including 1 RCT, a 2024 network meta-analysis, and multiple prospective cohort studies directly examining dexamethasone in alopecia areata treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from regulatory dataset |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Market Status | 未上市 (Not Marketed — regulatory data may be incomplete) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dexamethasone is a synthetic glucocorticoid approximately 25 times more potent than cortisol. Although full DrugBank pharmacology data is not included in this evidence pack, dexamethasone's mechanism is well established: it binds glucocorticoid receptors (GR) and triggers both genomic and non-genomic effects that suppress NF-κB signaling, reduce pro-inflammatory cytokine production (IFN-γ, IL-1β, TNF-α), and inhibit T-cell proliferation and activation across multiple immune compartments.

Alopecia areata is an autoimmune disease in which CD8+ cytotoxic T cells breach the hair follicle's immune privilege zone — a site normally protected by local expression of MHC-Ib and immunosuppressive mediators such as IL-10 and TGF-β. In AA, this protection collapses, leading to follicular attack and non-scarring hair loss. Dexamethasone is mechanistically well-matched to this pathology: it (1) inhibits CD8+ T-cell activation at the follicular level; (2) downregulates the key pro-inflammatory cytokines that drive follicular destruction; and (3) promotes IL-10 and MHC-Ib expression to help restore immune privilege. The mechanistic alignment is direct, not inferential.

A clinically important refinement is the **Oral Mini-Pulse (OMP) strategy**, in which dexamethasone is administered at 2.5–5 mg on two consecutive days per week rather than continuously. This regimen delivers meaningful systemic immunosuppression while substantially reducing HPA axis suppression — the central concern with long-term corticosteroid use. Multiple prospective studies and one head-to-head RCT have validated this dosing approach specifically for alopecia areata, and it represents an accessible alternative in settings where JAK inhibitors are unavailable or contraindicated.

---

## Clinical Trial Evidence

> **Context:** A ClinicalTrials.gov search returned 13 records, but the majority reflect dexamethasone as **supportive medication in oncology** (e.g., premedication before pemetrexed, anti-emesis, brain edema control) rather than as primary therapy for alopecia areata. No directly relevant AA-specific interventional trials were identified in the registry. The entries below are the most contextually informative for safety and tolerability assessment.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Observational study examining the effects of abnormal steroid metabolome (dexamethasone suppression test ≥1.8 mcg/dL) on bone density, bone strength, and body composition in MACS patients and healthy volunteers — directly relevant to long-term glucocorticoid safety profiling |
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | Unknown | 74 | Randomized, placebo-controlled study evaluating prophylactic dexamethasone for fatigue and malaise caused by regorafenib in colorectal cancer; not AA-specific, but provides tolerability data for systemic dexamethasone in a 74-patient controlled setting |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | Completed | 56 | Dexamethasone combined with lenalidomide ± durvalumab in newly diagnosed multiple myeloma; dexamethasone here functions as a primary treatment agent with full pharmacovigilance tracking across 56 patients |
| [NCT02004275](https://clinicaltrials.gov/study/NCT02004275) | Phase 1/2 | Unknown | 118 | Randomized study of pomalidomide + dexamethasone ± ixazomib in relapsed myeloma; largest trial with dexamethasone as primary component (n=118), offering substantial safety data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / Network Meta-analysis | Archives of Dermatological Research | PRISMA-compliant network meta-analysis comparing systemic steroids, oral JAK inhibitors, and contact immunotherapy for severe AA (SALT ≥50%); positions dexamethasone within the current treatment landscape |
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Randomized open-label trial in 30 pediatric AA patients comparing low-dose dexamethasone OMP vs. DPCP contact sensitization; the only head-to-head RCT evaluating dexamethasone directly in AA |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Real-world cohort study assessing effectiveness and safety of oral mini-pulse corticosteroids in AA patients; identifies clinical and demographic factors associated with successful response |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Cohort / Case Series | Journal of Dermatological Treatment | Documents durable remission of severe AA with dexamethasone OMP in patients ineligible for JAK inhibitors; includes focused review of corticosteroid pulse regimens as systemic alternatives |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Prospective Study | Dermatologic Therapy | Multicentric European study of oral dexamethasone mini-pulse for moderate-to-severe AA; highlights cost and accessibility advantages over JAK inhibitors in current European practice |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Prospective Study | Dermatologic Therapy | 73 pediatric AA patients (>30% scalp involvement) receiving IV dexamethasone pulse (1-day vs. 3-day regimens) combined with topical clobetasol; compares regimen duration and response rates |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Longitudinal Prospective Study | Dermatologic Therapy | Long-term follow-up (median 96 months) of 65 children with severe AA treated with oral dexamethasone pulse; provides the most durable efficacy and relapse data available in the pediatric population |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Literature synthesis of pulse-dose corticosteroid dosing regimens for pediatric AA; consolidates available dosing and safety evidence where no standardized protocol exists |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Study | Dermatology (Basel) | Compares efficacy, relapse rates, and side effect profiles of three systemic corticosteroid modalities for extensive AA, providing head-to-head data for treatment selection |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Prospective Study | The Journal of Dermatology | Foundational study: twice-weekly 5 mg dexamethasone oral pulse in 30 patients with widespread AA (mean 4.2 years disease duration); establishes the original dosing rationale for the OMP approach |

---

## EU Market Information

No authorization records are available in the provided dataset (market status: 未上市; total authorizations: 0). Dexamethasone is a long-established generic corticosteroid present in pharmacopeias worldwide — the absence of authorization data likely reflects a retrieval gap in the current pipeline rather than true absence of approval. Manual verification against the EMA product database is recommended before any regulatory assessment.

---

## Safety Considerations

Please refer to the SmPC for safety information. Note that formal safety data retrieval (TFDA package insert warnings and contraindications) is currently incomplete and identified as a **Blocking** data gap (DG001) — this must be resolved before this candidate can enter S1 safety screening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic alignment between dexamethasone's glucocorticoid immunosuppression and alopecia areata's autoimmune pathophysiology is direct and pharmacologically coherent. A 2024 network meta-analysis, 1 RCT, and at least six prospective studies collectively establish the Oral Mini-Pulse strategy as a clinically active and accessible treatment approach — sufficient evidence to advance to structured safety and feasibility evaluation.

**To proceed, the following is needed:**

- **Resolve Blocking data gap (DG001):** Retrieve TFDA package insert (仿單) to extract warnings, contraindications, and drug interaction data — required before S1 safety review can proceed
- **Resolve MOA data gap (DG002):** Query DrugBank API for DB01234 to formally document glucocorticoid receptor mechanism, receptor binding affinity, and known off-target effects
- **Conduct targeted clinical trial search:** Re-run ClinicalTrials.gov with AA-specific MeSH terms combined with dexamethasone as the primary intervention to capture any registry entries missed by the current evidence search
- **Clarify regulatory status:** Verify current EMA/EU authorization status for dexamethasone — existing data showing "未上市" is inconsistent with dexamethasone's known global availability and may reflect a pipeline error
- **Assess formulation pathway:** Evaluate whether standard oral or IV pulse routes are clinically optimal, or whether novel follicle-targeting nanoparticle formulations (e.g., dexamethasone-loaded lipomers, PMID [33920403](https://pubmed.ncbi.nlm.nih.gov/33920403/) and [34452283](https://pubmed.ncbi.nlm.nih.gov/34452283/)) warrant inclusion in a development roadmap
- **Define pediatric safety protocol:** Given that a disproportionate share of the evidence base involves pediatric patients, any clinical development plan should include age-stratified safety monitoring criteria and dose-adjustment guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

