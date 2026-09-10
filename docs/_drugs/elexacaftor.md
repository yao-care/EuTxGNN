---
layout: default
title: Elexacaftor
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Elexacaftor
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

# Elexacaftor: From Cystic Fibrosis to Rheumatoid Arthritis

## One-Sentence Summary

Elexacaftor is a CFTR corrector and one of three active components in the Trikafta/Kaftrio (elexacaftor-tezacaftor-ivacaftor, "ETI") combination, originally developed to treat Cystic Fibrosis in patients with at least one F508del mutation. The TxGNN model predicts a high association with **Rheumatoid Arthritis** (score 98.11%), but currently only **1 loosely-related clinical trial** and **no supporting literature** exist for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic Fibrosis (inferred from clinical trial/literature context; not confirmed by TFDA/EMA licensing data — drug not currently marketed) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.11% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for elexacaftor is not available (data gap, High severity). Based on known information, elexacaftor is a CFTR corrector used as part of the ETI triple combination, and its efficacy in Cystic Fibrosis — improving lung function and reducing pulmonary exacerbations — is well established.

However, for the Rheumatoid Arthritis prediction specifically, the model's own rationale indicates the association is weak: the high TxGNN score likely arises from proximity between CFTR-related pathways and inflammatory/immune-regulation pathways within the knowledge graph, rather than from any demonstrated pharmacological effect. No literature or mechanistic study currently supports elexacaftor acting on RA's autoimmune pathology (e.g., RF/anti-CCP-driven synovial inflammation). The one retrieved clinical trial (NCT04970225) studies neutrophil phenotype in CF patients — a basic immunology study unrelated to RA treatment — and was graded "C" relevance by the evidence pipeline. This prediction should be treated as a hypothesis-generating signal only, not a mechanistically supported repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | N/A | Completed | 47 | Studied blood neutrophil function/phenotype in Cystic Fibrosis patients (impact of chronic *P. aeruginosa* infection, CFTR modulator treatment, and exacerbations). Does not evaluate elexacaftor in RA patients — graded low relevance (C) to this indication. |

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Rheumatoid Arthritis prediction rests solely on TxGNN's knowledge-graph score (L5, no direct clinical or literature support), and the only retrieved trial is unrelated to RA treatment. There is currently no mechanistic, clinical, or observational evidence to justify advancing this candidate.

**To proceed, the following is needed:**
- Elexacaftor mechanism of action (MOA) data (DG002, High severity)
- TFDA/EMA label warnings and contraindications (DG001, Blocking severity — required before any S1 safety screening)
- Dedicated preclinical or mechanistic studies linking CFTR modulation to RA immunopathology
- Direct RA-specific clinical trial or case-level evidence for elexacaftor (or the ETI combination)

*Note: Among this drug's other predicted indications, Pulmonary Hypertension (rank 10, L4, "Research Question" stage) shows a more plausible indirect mechanistic rationale via CF-associated pulmonary vascular remodeling, and may warrant separate evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

