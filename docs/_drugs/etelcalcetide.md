---
layout: default
title: Etelcalcetide
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Etelcalcetide
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

# Etelcalcetide: From Secondary Hyperparathyroidism to Hyperphosphatemia

## One-Sentence Summary

Etelcalcetide is a calcimimetic used to control secondary hyperparathyroidism (SHPT) in hemodialysis patients, though this original indication is not captured as a formal regulatory record in the current dataset. The TxGNN model predicts it may also be effective for **Hyperphosphatemia**, with **1 clinical trial** and **3 publications** currently supporting this direction. Note: the drug is not currently marketed under the regulatory registry reviewed here (0 authorizations on record).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Secondary hyperparathyroidism (SHPT) in hemodialysis patients (based on known drug-class use; not reflected as a formal license in the current regulatory dataset) |
| Predicted New Indication | Hyperphosphatemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for etelcalcetide is currently a data gap in this dataset (DG002). Based on known information, etelcalcetide is a **calcium-sensing receptor (CaSR) agonist (calcimimetic)** administered intravenously at the end of hemodialysis sessions. It acts directly on the parathyroid gland to suppress parathyroid hormone (PTH) secretion.

Because PTH is a key upstream driver of bone calcium/phosphate release and renal/intestinal phosphate handling, suppressing PTH commonly produces a secondary, clinically observed reduction in serum phosphate. The drug's known use in secondary hyperparathyroidism and the predicted new indication of hyperphosphatemia therefore sit on the same pathological axis (CKD-Mineral and Bone Disorder, CKD-MBD) rather than being unrelated conditions.

This makes the mechanistic link an upstream/downstream pharmacological connection rather than a purely coincidental network-based extrapolation — the CaSR → PTH → phosphate homeostasis pathway plausibly explains why a drug approved for PTH control could also modulate phosphate levels in CKD patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completed | 21 | Mechanistic study of active vitamin D plus etelcalcetide on osteoclast activity in CKD patients; relevant to CKD-MBD pathway (hypocalcemia, hyperphosphatemia, hyperparathyroidism) but not designed with hyperphosphatemia as the primary efficacy endpoint. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney International Reports | DUET trial: prospective RCT evaluating etelcalcetide for control of secondary hyperparathyroidism in hemodialysis patients, targeting the CKD-MBD mechanism including mineral metabolism. |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | International Journal of Nephrology and Renovascular Disease | Reviews etelcalcetide's role in managing SHPT in hemodialysis; PTH reduction is associated with secondary declines in serum phosphate. |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case Report | Clinical Nephrology | Case report of metastatic pulmonary calcification in a dialysis patient with hyperparathyroidism, illustrating the shared calcium-phosphate pathology relevant to this disease axis (not direct etelcalcetide efficacy data). |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-interaction data are currently data gaps — DG001, classified as **Blocking** severity, preventing S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is supported by one RCT (DUET trial) and consistent mechanistic literature linking PTH suppression to secondary phosphate reduction, but no clinical trial has directly tested hyperphosphatemia as a primary endpoint, and critical safety/label data are missing.

**To proceed, the following is needed:**
- TFDA/official label warnings and contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- Drug-drug interaction data (currently not found)
- A trial or post-hoc analysis using serum phosphate as a primary/secondary endpoint to directly confirm the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

