---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: From Established Oncology Use to Predicted "New" Indication in Ewing Sarcoma

## ⚠️ Critical Data Quality Note

Before reading further: this Evidence Pack has an important limitation. The `drug.original_indications` field is **empty** and `original_moa` is marked as a data gap. As a direct consequence, the AI system's own rationale for the top-ranked prediction states explicitly:

> *"此為已確立適應症而非新預測，資料庫 original_indications 缺失導致誤標為候選"*
> ("This is an already-established indication, not a new prediction — the missing `original_indications` field caused the system to mislabel it as a candidate.")

Doxorubicin's use in **Ewing sarcoma** (as part of the VDC/IE regimen: Vincristine-Doxorubicin-Cyclophosphamide alternating with Ifosfamide-Etoposide) is decades-old, guideline-standard chemotherapy — not a genuine repurposing discovery. This report presents the evidence exactly as retrieved, but the "prediction" should be treated as a **data-quality artifact requiring correction**, not a novel drug repurposing opportunity. Ranks 2–10 in the underlying pack are genuinely more speculative (L3–L5) and are summarized briefly at the end of this report for completeness.

---

## One-Sentence Summary

Doxorubicin is an anthracycline cytotoxic agent whose original indications are not recorded in this Evidence Pack (data gap). The TxGNN model's top-ranked association is **Ewing Sarcoma**, but this is in fact doxorubicin's long-established standard-of-care indication (via the VDC/IE chemotherapy regimen), supported by **47 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs — evidence of confirmed clinical use rather than a new hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this Evidence Pack (`original_indications` field is empty) |
| Predicted New Indication | Ewing Sarcoma *(in practice, an already-established indication — see caveat above)* |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed (per this Evidence Pack) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails *(conditional on resolving the blocking safety data gap below)* |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action (MOA) data for doxorubicin is not available in this Evidence Pack. Based on the clinical evidence that *is* present, doxorubicin acts as a DNA-intercalating agent and Topoisomerase II inhibitor, producing cytotoxic effects in highly proliferative cells. It is one of the five core drugs (alongside vincristine, cyclophosphamide, ifosfamide, and etoposide) in the VDC/IE regimen — the internationally recognized standard-of-care chemotherapy backbone for Ewing sarcoma, a highly proliferative small round blue cell tumour of bone and soft tissue.

Because the drug's original indication(s) were not captured in this pack's `original_indications` field, the relationship between "original" and "new" indication cannot be meaningfully assessed here. What the underlying clinical trial and literature evidence actually demonstrates is that doxorubicin already has extensive, high-quality (multiple completed Phase 3 RCT) evidence in Ewing sarcoma — this is a case of the evidence pack surfacing a confirmed use, not uncovering a mechanistically novel application.

**Recommendation:** Treat this as a prompt to backfill `original_indications` for doxorubicin (DrugBank DB00997) rather than to advance it through a repurposing-specific workflow.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Randomized trial optimizing treatment intensity (standard vs. intensive) for non-metastatic Ewing sarcoma; doxorubicin-containing regimen as standard backbone |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Randomized trial adding vincristine-topotecan-cyclophosphamide to standard 5-drug regimen (incl. doxorubicin) for non-metastatic Ewing sarcoma |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Randomized comparison of chemotherapy intensification via interval compression combined with radiotherapy/surgery in Ewing sarcoma family tumours |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, Not Recruiting | 312 | Randomized trial of ganitumab (anti-IGF-1R) added to standard multiagent chemotherapy (incl. doxorubicin) for newly diagnosed metastatic Ewing sarcoma |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, Not Recruiting | 437 | Compares VIrR (vincristine-irinotecan-regorafenib) added to standard VDC/IE (incl. doxorubicin) for newly diagnosed metastatic Ewing sarcoma |
| [NCT03011528](https://clinicaltrials.gov/study/NCT03011528) | Phase 2 | Completed | 45 | First-line treatment of Ewing tumours with primary extrapulmonary dissemination; graded "A" — directly relevant |
| [NCT00334867](https://clinicaltrials.gov/study/NCT00334867) | Phase 3 | Withdrawn | 0 | Historical trial design intent (VTC addition) for non-metastatic Ewing sarcoma; withdrawn, not executed |
| [NCT00001209](https://clinicaltrials.gov/study/NCT00001209) | Phase 1 | Completed | 120 | Pilot study of vincristine/doxorubicin/cyclophosphamide alternating with ifosfamide/etoposide in metastatic/high-risk sarcomas including Ewing's |
| [NCT06699472](https://clinicaltrials.gov/study/NCT06699472) | Phase 2 | Recruiting | 22 | Prospective RCT of trilaciclib to prevent VDC/IE chemotherapy-related myelosuppression in Ewing sarcoma — directly relevant to safety monitoring |
| [NCT07321912](https://clinicaltrials.gov/study/NCT07321912) | Phase 2 | Not Yet Recruiting | 406 | Basket trial adding eflornithine (DFMO) as maintenance therapy for Ewing sarcoma and osteosarcoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012 open-label randomized Phase 3 trial comparing two chemotherapy regimens (both doxorubicin-based) for newly diagnosed Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT | Trials | EURO EWING 2012 protocol — international RCT comparing induction/consolidation chemotherapy regimens for Ewing sarcoma family tumours |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | COG Phase 3 RCT: addition of ganitumab (anti-IGF-1R) to interval-compressed chemotherapy for metastatic Ewing sarcoma |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | RCT | J Clin Oncol | High-dose treosulfan/melphalan consolidation vs. standard therapy for high-risk (metastatic) Ewing sarcoma |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | COG RCT of interval-compressed chemotherapy (vincristine-doxorubicin-cyclophosphamide/ifosfamide-etoposide) for localized Ewing sarcoma |
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | New England Journal of Medicine | Landmark trial establishing addition of ifosfamide/etoposide to standard regimen for Ewing sarcoma / PNET of bone |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncology | Comprehensive review of Ewing's sarcoma diagnosis and multidisciplinary treatment |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management and future directions in Ewing sarcoma treatment |
| [38904887](https://pubmed.ncbi.nlm.nih.gov/38904887/) | 2024 | Systematic Review | Int J Clin Oncol | G-CSF primary prophylaxis for chemotherapy-induced myelosuppression in Ewing sarcoma (JSCO guideline) |
| [25993235](https://pubmed.ncbi.nlm.nih.gov/25993235/) | 2015 | Review | ASCO Educational Book | Systemic therapy overview for osteosarcoma and Ewing sarcoma |

---

## EU Market Information

This drug is recorded as **Not Marketed** in this Evidence Pack, with **0 authorizations** on file (`taiwan_regulatory.licenses` is empty). No marketing authorization data is available to summarize.

---

## Cytotoxicity

Doxorubicin is a conventional cytotoxic chemotherapy agent (anthracycline class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Anthracycline class — DNA intercalation + Topoisomerase II inhibition) |
| Myelosuppression Risk | High — standard doxorubicin-containing regimens (e.g., VDC/IE) are associated with significant myelosuppression; this pack contains a dedicated RCT on prophylaxis (NCT06699472, trilaciclib) and a 2024 systematic review on G-CSF support (PMID 38904887) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | CBC with differential; cardiac function (LVEF/echocardiography, troponin/natriuretic peptides — anthracycline cardiotoxicity is specifically studied in this pack via NCT01112800 and NCT01095926); liver and renal function |
| Handling Protection | Cytotoxic drug handling precautions required per institutional hazardous-drug protocols |

---

## Safety Considerations

Please refer to the SmPC for safety information. This Evidence Pack's `safety.key_warnings`, `safety.contraindications`, and DDI query all returned no usable data (DDI query status: not found).

**Note:** The accompanying `meta.data_gaps` flags this as a **Blocking** severity issue (DG001 — "TFDA label warnings/contraindications," impact: "cannot proceed to S1 initial safety assessment"). This should be resolved before any clinical decision-making proceeds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(with the caveat below)*

**Rationale:**
The clinical trial and literature evidence base for doxorubicin in Ewing sarcoma is extensive and high-quality (multiple completed Phase 3 RCTs), meeting L1 evidence-level criteria. However, this reflects doxorubicin's **already-established** role in standard Ewing sarcoma chemotherapy rather than a new repurposing signal — the underlying data quality issue (missing `original_indications`) means this candidate should be reclassified rather than progressed as novel. Separately, the safety data gap (DG001) is rated **Blocking** and must be resolved before any S1 safety assessment can occur.

**To proceed, the following is needed:**
- Backfill `drug.original_indications` and `original_moa` for doxorubicin (DB00997) to correct the mislabeling of Ewing sarcoma as a "new" candidate
- Obtain the TFDA/SmPC label (warnings, contraindications) to resolve the Blocking data gap (DG001) before any S1 safety review
- Confirm actual marketing/regulatory status, since this pack shows 0 authorizations despite doxorubicin being a globally marketed generic oncology drug — this is likely itself a data gap rather than true non-availability
- If the intent was to evaluate genuinely novel repurposing candidates, review ranks 2–10 in the underlying pack instead (see summary below), all of which carry lower evidence levels (L3–L5) and were not mechanistically confounded with existing use

---

### Appendix: Lower-Ranked Candidates (Ranks 2–10, Not Detailed Above)

For completeness, the remaining candidates in this pack — none reaching L1/L2 evidence with a clean "novel indication" signal — were: well-differentiated fetal lung adenocarcinoma (L5, Hold), primary pulmonary lymphoma (L3, Research Question), pulmonary blastoma (L4, Research Question), CML BCR-ABL1+ (L3, Research Question), monocytic leukemia (L4, Research Question), botryoid-type vaginal embryonal rhabdomyosarcoma (L4, Hold), parameningeal embryonal rhabdomyosarcoma (L3, Research Question), rhabdomyosarcoma — general (L1, but same "already-established indication" caveat applies), and ganglioneuroblastoma (L3, Research Question). None of these are recommended for advancement without further mechanistic and safety review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

