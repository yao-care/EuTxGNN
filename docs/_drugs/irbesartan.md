---
layout: default
title: Irbesartan
parent: AI Predictions (L5)
nav_order: 334
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
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
| EU Market Status | Marketed (valid licences: 10 of 13) |
| Number of Authorizations | 13 (valid: 10) |
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

<!-- review:begin eu-lic-20261106-irbesartan-1 -->

> **Review correction (2026-11-06)**: Originally stated: "All five authorizations are valid; irbesartan as a single agent is currently marketed." Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 13 EU marketing authorisations for this drug, 10 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-irbesartan-1 -->

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000141 | Aprovel | irbesartan | Valid |
| EMEA/H/C/000142 | Karvea | irbesartan | Valid |
| EMEA/H/C/000785 | Irbesartan Zentiva | irbesartan | Valid |
| EMEA/H/C/000962 | Ifirmasta | irbesartan hydrochloride | Valid |
| EMEA/H/C/001093 | Irbesartan Teva |  | Valid |
| EMEA/H/C/000221 | Karvezide | irbesartan; hydrochlorothiazide | Valid |
| EMEA/H/C/000222 | CoAprovel | irbesartan; hydrochlorothiazide | Valid |
| EMEA/H/C/000783 | Irbesartan Hydrochlorothiazide Zentiva | irbesartan; hydrochlorothiazide | Valid |
| EMEA/H/C/001112 | Irbesartan/Hydrochlorothiazide Teva | irbesartan; hydrochlorothiazide | Valid |
| EMEA/H/C/002302 | Ifirmacombi | irbesartan; hydrochlorothiazide | Valid |
| EMEA/H/C/000786 | Irbesartan BMS | irbesartan | Withdrawn |
| EMEA/H/C/002510 | Sabervel | irbesartan | Expired |
| EMEA/H/C/000784 | Irbesartan Hydrochlorothiazide BMS | irbesartan; hydrochlorothiazide | Withdrawn |

<!-- licenses:end -->

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links, not label text): angioedema (including RAAS-blocker-induced and hereditary forms), pancreatitis, systemic lupus erythematosus, anuria, renal artery obstruction, hypotensive disorders, hepatic coma/encephalopathy, diabetic ketoacidosis, gout, hypercalcaemia, hyperparathyroidism, myopathy/rhabdomyolysis, and potassium-related disorders such as familial periodic paralysis.
- **Drug Interactions**: 100 interactions were identified. The two Major interactions among those listed are **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, degludec), bupropion, aprepitant, morphine, dronabinol, and several bowel-preparation agents.
- **Setting-specific risk**: in renovascular hypertension, ARBs are a concern in bilateral renal artery stenosis or stenosis in a solitary kidney (risk of acute renal failure).

Please refer to the SmPC for the full label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but has no clinical trial or literature support, resting only on the TxGNN score (evidence level L5). The condition is a hypertensive emergency where ARBs carry notable renal and potassium risks, and the drug is marketed.

<!-- review:begin eu-lic-20261106-irbesartan-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The condition is a hypertensive emergency where ARBs carry notable renal and potassium risks, and the drug is marketed, with all 5 authorizations currently valid." Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 13 EU marketing authorisations for this drug, 10 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-irbesartan-2 -->

**To proceed, the following is needed:**
- Retrieval of EMA label warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search and trial registry review for irbesartan in malignant hypertension and hypertensive nephropathy
- Clarification of current EU regulatory status and available dosage forms and routes
- A safety assessment covering acute kidney injury and hyperkalaemia in severe hypertension
- Remapping of obsolete ontology terms (such as "susceptibility to ischemic stroke") before evaluating other predictions

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "All five authorizations are valid; irbesartan as a single agent is currently marketed" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-06 | Removed: "with all 5 authorizations currently valid" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

