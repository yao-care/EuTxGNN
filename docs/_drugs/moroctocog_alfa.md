---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Moroctocog Alfa
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

# Moroctocog Alfa: From Coagulation Factor VIII Replacement Therapy to Primary Release Disorder of Platelets

## One-Sentence Summary

> Moroctocog alfa is a recombinant coagulation Factor VIII (B-domain deleted) product; formal original-indication and local regulatory data are not available in this evidence pack, and the drug is currently **not marketed** in this jurisdiction. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but this direction is currently supported only by **7 clinical trials** — all graded low relevance ("C") — and **no literature evidence**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no local license record exists. (Contextually, per the drug's own class description in this pack, moroctocog alfa is a recombinant Factor VIII replacement product, typically used in Hemophilia A.) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for this drug record. Based on information present elsewhere in this evidence pack, moroctocog alfa is a **recombinant Factor VIII (B-domain deleted)** product, whose established mechanism is to replace deficient coagulation Factor VIII within the coagulation cascade — i.e., it addresses a *coagulation factor deficiency*, not a *platelet function/release defect*.

Primary release disorder of platelets is caused by a defect in platelet granule release, a mechanism entirely distinct from the coagulation cascade that Factor VIII acts on. There is no direct pharmacological pathway by which FVIII replacement would correct a platelet granule secretion defect.

The very high TxGNN score (99.97%) most likely reflects an indirect knowledge-graph linkage — both conditions share a "bleeding tendency / hemostatic disorder" comorbidity node — rather than a genuine, validated pharmacological relationship. This is corroborated by the clinical trial evidence below, where every retrieved trial was graded "C" (low relevance) by the evidence pipeline, meaning none directly tested moroctocog alfa (or any FVIII product) in this specific platelet disorder.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Post-COVID-19-vaccination syndrome lab/symptom evaluation — coagulation-adjacent but not related to platelet release disorder or FVIII therapy |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Coagulation profiles in newly diagnosed AML patients undergoing induction chemotherapy — no FVIII intervention |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system (DPMAS + TPE) effects on primary coagulation in acute-on-chronic liver failure — unrelated |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | PEGylated rFVIII (BAX 855) safety/efficacy in severe Hemophilia A patients undergoing surgery — FVIII product, but for hemophilia, not platelet disorder |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | rFVIIIFc-VWF-XTEN (BIVV001) prophylaxis in severe Hemophilia A (≥12 yrs) — FVIII product, hemophilia indication only |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | Same BIVV001 program in pediatric severe Hemophilia A (<12 yrs) — FVIII product, hemophilia indication only |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic/portal hemostasis in patients undergoing TIPS placement — no direct FVIII/platelet disorder link |

**All 7 trials were graded "C" (low relevance)** by the evidence pipeline: reasoning consistently notes keyword co-occurrence only, with no trial directly testing an intervention for primary release disorder of platelets.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA label warnings/contraindications and detailed MOA are flagged as data gaps in this pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the underlying mechanistic rationale is weak-to-contradictory (FVIII replacement does not address a platelet granule-release defect), and all 7 available clinical trials are graded low relevance with zero literature support. This corresponds to Evidence Level L5 (model prediction only) and Decision Stage S0.

**To proceed, the following is needed:**
- **[Blocking]** TFDA-equivalent label warnings/contraindications (DG001) — required before any S1 safety pre-screening can begin
- **[High]** Confirmed mechanism-of-action data via DrugBank API (DG002) — needed to properly assess mechanistic relevance
- Independent pharmacological/hematology expert review of whether FVIII has any plausible role in platelet granule-release disorders
- Consider redirecting evaluation resources toward **rank 4 candidate ("acquired coagulation factor deficiency")** in this same pack, which reaches L3/S1 with a stronger, more direct mechanistic link (acquired Hemophilia A via anti-FVIII autoantibodies) and multiple Phase 2/3 trial precedents for FVIII-class products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

