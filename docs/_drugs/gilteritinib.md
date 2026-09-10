---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Gilteritinib
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

# Gilteritinib: From FLT3-Mutated Acute Myeloid Leukemia to Myelodysplastic/Myeloproliferative Disease

## One-Sentence Summary

Gilteritinib is a FLT3/AXL tyrosine kinase inhibitor approved for FLT3-mutation-positive relapsed/refractory acute myeloid leukemia (AML). The TxGNN model's evidence pack contains 10 candidate indications, but 8 of them (including the top-ranked "bulbar polio") are flagged by the model itself as biologically implausible noise with no supporting evidence. The one candidate with genuine clinical and mechanistic support is **Myelodysplastic/Myeloproliferative Disease**, backed by **4 clinical trials (1 directly testing gilteritinib)** and **1 supporting publication**. This report focuses on that candidate rather than the raw top TxGNN score.

> **Note on candidate selection:** TxGNN's rank-1 prediction ("bulbar polio," score 99.10%) is explicitly annotated in the evidence pack as "model noise with no plausible mechanistic link" and is not evaluated further here. Ranks 2–9 are similarly either mechanistically implausible (unrelated congenital/neurologic syndromes) or lack any clinical/literature evidence (L4–L5, decision stage S0). Rank 10, myelodysplastic/myeloproliferative disease, is the only candidate reaching evidence level L2 / decision stage S2, so it is presented as the primary finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | FLT3-mutation-positive relapsed/refractory acute myeloid leukemia (per repurposing rationale; no Taiwan license data available) |
| Predicted New Indication | Myelodysplastic/Myeloproliferative Disease |
| TxGNN Prediction Score | 96.99% (rank 23,875 by raw score) |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available in DrugBank for this evidence pack (flagged as a High-severity data gap). However, the evidence pack's own repurposing rationale documents that gilteritinib is a FLT3 (including ITD/TKD mutations) and AXL kinase inhibitor, already approved for FLT3-mutant relapsed/refractory AML.

Myelodysplastic/myeloproliferative (MDS/MPN) overlap syndromes share substantial biology with AML — both are clonal myeloid disorders in which activating FLT3 or related receptor tyrosine kinase (RTK) mutations drive abnormal proliferation of myeloid progenitors. Because gilteritinib's approved mechanism directly targets this pathway, extending its use to FLT3-mutant MDS/MPN is a mechanistically coherent extrapolation rather than a speculative one.

This is reinforced by a directly relevant, currently recruiting Phase 1/2 trial (NCT04140487) that tests gilteritinib itself — in combination with azacitidine and venetoclax — specifically in FLT3-mutant AML, chronic myelomonocytic leukemia, and high-risk MDS/MPN, indicating that clinical investigators already consider this extension worth testing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04140487](https://clinicaltrials.gov/study/NCT04140487) | Phase 1/2 | Recruiting | 97 | Gilteritinib + azacitidine + venetoclax in FLT3-mutation-positive AML, CMML, or high-risk MDS/MPN that is relapsed or refractory. **Direct evidence** — this trial uses gilteritinib itself. |
| [NCT05564390](https://clinicaltrials.gov/study/NCT05564390) | Phase 2 | Recruiting | 2000 | NCI MyeloMATCH master screening/reassessment platform for AML and MDS patients; biomarker-based trial triage. Indirect evidence — a screening platform, not a gilteritinib-specific trial. |
| [NCT03922100](https://clinicaltrials.gov/study/NCT03922100) | Phase 1/2 | Terminated | 63 | Tests NMS-03592088 (a different FLT3/KIT/CSF1R inhibitor, not gilteritinib) in relapsed/refractory AML or CMML. Same-class supportive evidence only; trial terminated. |
| [NCT02115295](https://clinicaltrials.gov/study/NCT02115295) | Phase 2 | Recruiting | 508 | Cladribine + idarubicin + cytarabine (+venetoclax) regimen in AML/high-risk MDS/CML blast phase; does **not** use gilteritinib — weak/possibly mismatched association. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33792628](https://pubmed.ncbi.nlm.nih.gov/33792628/) | 2021 | Case Report | Blood Advances | Describes an infant with ETV6-FLT3 fusion-driven myeloid/lymphoid neoplasm with eosinophilia; leukemia cells showed increased ex vivo sensitivity to type I FLT3 inhibitors (the class gilteritinib belongs to), supporting the mechanistic rationale for FLT3-driven myeloid disease. |

## Taiwan Market Information

Gilteritinib currently has **no marketing authorization in Taiwan** (market status: 未上市, 0 licenses on record). This is a Blocking-severity data gap (DG001: TFDA label/warnings unavailable) — safety labeling and local regulatory approval status must be confirmed via the TFDA before any repurposing pathway can proceed locally.

## Cytotoxicity

Gilteritinib is an antineoplastic agent (targeted kinase inhibitor used in AML, a hematologic malignancy).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FLT3/AXL tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack — DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A directly relevant Phase 1/2 trial is actively testing gilteritinib in FLT3-mutant AML/high-risk MDS/MPN, and the mechanistic rationale (shared FLT3-driven biology between AML and MDS/MPN) is sound. However, evidence is still limited to one direct trial plus indirect/same-class support, and Taiwan-specific regulatory and safety data are entirely missing.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-severity gap, DG002)
- Results from NCT04140487 once available (currently recruiting, estimated completion 2028-09-01)
- Assessment of Taiwan market entry pathway, since gilteritinib is not currently licensed in Taiwan
- Drug-drug interaction data, currently unavailable ("not_found" in DDI query)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

