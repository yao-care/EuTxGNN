---
layout: default
title: Cinacalcet
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Cinacalcet
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

# Cinacalcet: From Secondary Hyperparathyroidism to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Cinacalcet (Sensipar/Mimpara) is a calcimimetic agent used to treat secondary hyperparathyroidism in chronic kidney disease patients on dialysis and hypercalcemia in parathyroid carcinoma.
The TxGNN model assigns its highest score (98.48%) to **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, yet this direction has **no supporting clinical trials or publications** at this time.
Importantly, the rank-4 prediction — **Multiple Endocrine Neoplasia (MEN)** — is far better supported with **3 clinical trials** (including a completed Phase 3 study) and **19 publications**, and carries a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Secondary hyperparathyroidism (CKD dialysis patients); hypercalcemia in parathyroid carcinoma |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 (AI prediction only — no clinical studies) |
| EU/TW Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cinacalcet is a positive allosteric modulator of the calcium-sensing receptor (CaSR). By sensitizing CaSR to extracellular calcium, it suppresses PTH secretion from parathyroid glands, thereby lowering serum calcium. This mechanism directly addresses the PTH dysregulation underlying secondary hyperparathyroidism in dialysis patients and the autonomous PTH/calcium elevation in parathyroid carcinoma.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is caused by gain-of-function mutations in AVPR2 — the gene encoding the V2 vasopressin receptor — which drives constitutive water reabsorption in the renal collecting duct independent of plasma osmolality. While CaSR is expressed in the renal collecting duct and may influence aquaporin-2 (AQP2) water channel expression in theory, this putative link does not intersect with the AVPR2 gain-of-function pathway that directly causes NSIAD. No experimental or clinical data currently support CaSR agonism as a strategy for managing this condition.

Currently, detailed mechanism of action data from DrugBank is not available. Based on established pharmacology, cinacalcet's biological effects are largely confined to calcium/PTH homeostasis via CaSR. The high TxGNN score for NSIAD most likely reflects indirect graph-level co-associations in the knowledge graph rather than a direct biological rationale. Without preclinical validation of this CaSR–AQP2–AVPR2 hypothesis, advancement beyond the model-prediction stage is not justified.

> **Higher-evidence alert:** The rank-4 prediction for **Multiple Endocrine Neoplasia (MEN)** is the most actionable finding in this Evidence Pack. MEN1's hallmark manifestation is primary hyperparathyroidism (multi-glandular parathyroid disease), a direct target of cinacalcet's CaSR mechanism. A completed Phase 3 trial (NCT00325104, n=25) and a cohort study with 10+ publications directly demonstrate cinacalcet efficacy in MEN1-associated hyperparathyroidism. This warrants independent evaluation as a priority repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Nephrogenic Syndrome of Inappropriate Antidiuresis.

---

## Literature Evidence

Currently no related literature available for Nephrogenic Syndrome of Inappropriate Antidiuresis.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN score of 98.48%, no mechanistic bridge has been established between CaSR agonism and the AVPR2 gain-of-function pathway that drives NSIAD, and there are no supporting preclinical or clinical studies of any kind.

**To proceed, the following is needed:**
- Preclinical studies (in vitro renal collecting duct models or in vivo AVPR2 gain-of-function models) to test whether CaSR activation can modulate water reabsorption independently of AVPR2 signaling
- MOA data from DrugBank to formally map CaSR downstream pathways against AVPR2/AQP2 biology
- TFDA/SmPC safety data to complete the S1 safety screen (currently a blocking data gap)
- Consider redirecting evaluation resources to the MEN (rank 4) prediction, which has L2-level evidence and a "Proceed with Guardrails" recommendation already supported by a completed Phase 3 trial (NCT00325104)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

