---
layout: default
title: Fondaparinux
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
---

# Fondaparinux
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

# Fondaparinux: From Anticoagulant Therapy to Primary Release Disorder of Platelets

## One-Sentence Summary

Fondaparinux is a synthetic pentasaccharide anticoagulant (Factor Xa inhibitor); the evidence pack does not contain a formal original-indication text or DrugBank MOA record. TxGNN predicts possible relevance to **Primary Release Disorder of Platelets**, but the only supporting evidence retrieved (**2 clinical trials, 2 publications**) actually concerns heparin-induced thrombocytopenia (HIT), not platelet release disorders — a likely disease-label mismatch flagged directly in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (pharmacologically an anticoagulant / Factor Xa inhibitor, per rationale text) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 93.06% |
| Evidence Level | L3 |
| Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action record is available for Fondaparinux (`original_moa` = Data Gap). However, the repurposing rationale collected as part of this evidence pack does describe the mechanism: Fondaparinux is a synthetic pentasaccharide that selectively inhibits Factor Xa via antithrombin binding, and it does not bind platelet factor 4 (PF4). Because of this, it does not cross-react with heparin-induced thrombocytopenia (HIT) antibodies, and it is already used clinically as an alternative anticoagulant in HIT patients.

The predicted new indication, "primary release disorder of platelets," refers to a primary defect in platelet granule release (e.g., storage pool disease) — a mechanistically distinct condition from HIT. Both retrieved clinical trials and one of the two retrieved publications concern HIT, not platelet release disorders. This strongly suggests an ontology/disease-label mismatch between the TxGNN node and the retrieved evidence, exactly as noted in the pack's own rationale text. The mechanistic plausibility of fondaparinux for HIT-related anticoagulation is real and well-established; its plausibility for a genuine primary platelet-release disorder is not supported by any evidence in this pack and would need a separate, correctly targeted evidence search.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00911300](https://clinicaltrials.gov/study/NCT00911300) | Phase 2 | Completed | 349 | International multicentre RCT comparing fondaparinux vs. heparin/vitamin-K antagonists for anticoagulation in atrial fibrillation patients undergoing electric cardioversion. Relevance grade B — mechanistically tied to fondaparinux's low HIT cross-reactivity, but not a direct study of platelet release disorder. |
| [NCT01178333](https://clinicaltrials.gov/study/NCT01178333) | N/A (retrospective) | Completed | 668 | Retrospective analysis of HIT incidence and outcomes (HIT-RADIO study) using existing medical records (platelet counts, treatments, outcomes). Relevance grade C — background epidemiology only, non-interventional, no direct causal support. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28646118](https://pubmed.ncbi.nlm.nih.gov/28646118/) | 2017 | Review | Blood | Review of direct oral anticoagulants for HIT treatment, updating the Hamilton group's clinical experience; not specific to platelet release disorders. |
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Case Report | Journal of the Advanced Practitioner in Oncology | Case study on palliative chemotherapy in a patient with metastatic adenocarcinoma; unrelated to Fondaparinux or platelet mechanisms — appears to be a low-relevance/mismatched retrieval. |

---

## Market Information

Fondaparinux is currently **not marketed** in this jurisdiction, with **0 authorizations** on record. No product license data is available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data were all unavailable in this evidence pack; DDI query returned "not_found.")*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical/literature evidence retrieved supports fondaparinux's known role in HIT-related anticoagulation, not the specifically predicted "primary release disorder of platelets" — the pack itself flags this as a likely ontology mismatch requiring manual confirmation. Combined with a **blocking** data gap on TFDA warnings/contraindications (DG001) and the drug not currently being marketed in this jurisdiction, the evidence base does not yet support advancing this candidate.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) to clear the blocking S1 safety gap (DG001)
- Verified DrugBank MOA record (DG002)
- Manual review confirming whether the TxGNN "primary release disorder of platelets" node genuinely maps to the retrieved HIT trials, or whether a corrected, disease-specific evidence search is required
- Market-entry feasibility assessment, given zero current authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

