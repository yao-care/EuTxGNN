---
layout: default
title: Ivabradine
parent: AI Predictions (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ivabradine: From Chronic Stable Angina Pectoris and Chronic Heart Failure to Hypertrichosis

## One-Sentence Summary

Ivabradine is a heart-rate-lowering drug, originally used for chronic stable angina pectoris and chronic heart failure.
The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** currently support this prediction.
The high score most likely reflects a computational artifact rather than a biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of chronic stable angina pectoris; chronic heart failure (NYHA II–IV, systolic dysfunction) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| EU Market Status | ✗ Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 5 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Ivabradine is known to inhibit the HCN (If, "funny current") channel in the sinoatrial node, which slows the heart rate. This explains its use in angina and heart failure.

No plausible mechanistic link was identified between this action and hair follicle growth regulation. The very high TxGNN score (0.998) most likely comes from shared neighbours in the knowledge graph, not from biological reasoning. Several other top-ranked predictions are also hair-related or congenital syndromes, which points to the same artifact. Without a mechanistic bridge or supporting studies, this prediction should be treated as a computational output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

All five authorizations are listed as cancelled. Dosage form was not specified in the data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000597 | Procoralan | — | Symptomatic treatment of chronic stable angina pectoris Ivabradine is indicated for the symptomatic treatm... |
| EMEA/H/C/000598 | Corlentor | — | Symptomatic treatment of chronic stable angina pectoris Ivabradine is indicated for the symptomatic treatm... |
| EMEA/H/C/004117 | Ivabradine Zentiva | — | Symptomatic treatment of chronic stable angina pectoris Ivabradine is indicated for the symptomatic treatm... |
| EMEA/H/C/004187 | Ivabradine Anpharm | — | Symptomatic treatment of chronic stable angina pectoris Ivabradine is indicated for the symptomatic treatm... |
| EMEA/H/C/004241 | Ivabradine Accord | — | Symptomatic treatment of chronic stable angina pectoris Ivabradine is indicated for the symptomatic treatm... |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The first 20 retrieved included these **Major** interactions: aprepitant, clarithromycin, clotrimazole, cobicistat, cisapride, dolasetron, granisetron, levofloxacin, ondansetron, palonosetron and papaverine.
- **Moderate interactions** included famotidine, ranitidine, cimetidine, nizatidine, dexamethasone, miconazole, metreleptin and troglitazone.

Warnings and contraindications were not available in the compiled data. Please refer to the SmPC for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no publications and no plausible mechanistic link to ivabradine's HCN-channel action. It is supported only by a model score, so the evidence level is L5. In addition, no EU authorization for ivabradine is currently valid.

**Other predictions from the same analysis:**
Among the other predicted indications, **pulmonary hypertension** (score 98.5%, rank 7) is the only one with a plausible rationale and published studies. These include preclinical work showing improved right ventricular function and reduced fibrosis, and small clinical studies in COPD-associated and systemic-sclerosis-related pulmonary hypertension. Evidence there is limited to L3, with no registered trials. Heart-rate dependence of right ventricular output means bradycardia could be harmful in some patients. This is better pursued as a separate research question than through the hypertrichosis prediction.

**To proceed, the following is needed:**
- Any mechanistic or biological evidence linking HCN-channel inhibition to hair growth, or a decision to deprioritize this prediction
- Detailed mechanism-of-action data (MOA) from DrugBank
- Warnings and contraindications from the EMA product information
- Confirmation of the current EU regulatory status, since all authorizations are listed as cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

