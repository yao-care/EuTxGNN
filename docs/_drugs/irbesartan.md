---
layout: default
title: Irbesartan
parent: AI Predictions (L5)
nav_order: 334
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Irbesartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Treatment of essential hypertension. Treatment of renal disease in pa…"
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Irbesartan: From Essential Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker, originally used to treat essential hypertension and renal disease in patients with hypertension and type 2 diabetes.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a very high prediction score.
However, **no clinical trials and no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of essential hypertension. Treatment of renal disease in patients with hypertension and type-2 diabetes mellitus as part of an antihypertensive medicinal-product regimen. |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 5 of 5) |
| Number of Authorizations | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, irbesartan is an AT1 receptor blocker (an angiotensin II receptor antagonist). Its efficacy in hypertension and in renal disease associated with hypertension and type 2 diabetes is already established.

Malignant hypertensive renal disease is kidney injury driven by severe, accelerated hypertension, which is closely related to the approved indications. Blocking the renin-angiotensin system could lower blood pressure and reduce renal injury, so the prediction is biologically plausible as a close extension of the approved use.

There are important caveats. Malignant hypertension is a hypertensive emergency, usually managed with intravenous agents. ARBs also carry risks of acute kidney injury and hyperkalaemia in this setting. The high TxGNN score is a network-based prediction and not clinical proof.

Other top predictions (pulmonary hypertension subtypes) likewise have no clinical trial support. Only preclinical or indirect literature exists for the hypoxia-related pulmonary hypertension prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

## EU Market Information

All five authorizations are valid; irbesartan as a single agent is currently marketed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000785 | Irbesartan Zentiva (previously Irbesartan Winthrop) | Not specified | Treatment of essential hypertension. Treatment of renal disease in patients with hypertension and type-2 diabetes mellitus as part of an antihyp... |
| EMEA/H/C/000962 | Ifirmasta (previously Irbesartan Krka) | Not specified | Treatment of essential hypertension. Treatment of renal disease in patients with hypertension and type 2 diabetes mellitus as part of an anti... |
| EMEA/H/C/001093 | Irbesartan Teva | Not specified | Treatment of essential hypertension. Treatment of renal disease in patients with hypertension and type 2 diabetes mellitus as part of an anti... |
| EMEA/H/C/000142 | Karvea | Not specified | Treatment of essential hypertension. Treatment of renal disease in patients with hypertension and type-2 diabetes mellitus as part of an antihyp... |
| EMEA/H/C/000141 | Aprovel | Not specified | Treatment of essential hypertension. Treatment of renal disease in patients with hypertension and type-2 diabetes mellitus as part of an antihyp... |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links, not label text): angioedema (including RAAS-blocker-induced and hereditary forms), pancreatitis, systemic lupus erythematosus, anuria, renal artery obstruction, hypotensive disorders, hepatic coma/encephalopathy, diabetic ketoacidosis, gout, hypercalcaemia, hyperparathyroidism, myopathy/rhabdomyolysis, and potassium-related disorders such as familial periodic paralysis.
- **Drug Interactions**: 100 interactions were identified. The two Major interactions among those listed are **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, degludec), bupropion, aprepitant, morphine, dronabinol, and several bowel-preparation agents.
- **Setting-specific risk**: in renovascular hypertension, ARBs are a concern in bilateral renal artery stenosis or stenosis in a solitary kidney (risk of acute renal failure).

Please refer to the SmPC for the full label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but has no clinical trial or literature support, resting only on the TxGNN score (evidence level L5). The condition is a hypertensive emergency where ARBs carry notable renal and potassium risks, and the drug is marketed, with all 5 authorizations currently valid.

**To proceed, the following is needed:**
- Retrieval of EMA label warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search and trial registry review for irbesartan in malignant hypertension and hypertensive nephropathy
- Clarification of current EU regulatory status and available dosage forms and routes
- A safety assessment covering acute kidney injury and hyperkalaemia in severe hypertension
- Remapping of obsolete ontology terms (such as "susceptibility to ischemic stroke") before evaluating other predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

