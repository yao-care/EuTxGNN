---
layout: default
title: Azilsartan Medoxomil
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Azilsartan Medoxomil
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

# Azilsartan Medoxomil: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Azilsartan medoxomil is an angiotensin II type 1 (AT1) receptor blocker approved internationally for hypertension, though it currently holds no EU marketing authorization.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism** (TxGNN score: **97.78%**),
however **no clinical trials** and **no direct publications** for this drug-disease pair were identified — this remains a purely model-driven prediction at evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (approved internationally; no EU marketing authorization on record) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 97.78% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Azilsartan medoxomil is a potent and highly selective AT1 receptor blocker — regarded as one of the most efficacious ARBs in its class, with stronger receptor binding affinity and more sustained AT1 blockade than comparators such as olmesartan and valsartan. Its proven benefit in lowering systemic blood pressure through durable RAAS inhibition underpins its established international use.

The mechanistic case for pulmonary hypertension rests on angiotensin II's role in driving pulmonary vascular remodeling: AT1 receptor activation promotes pulmonary smooth muscle proliferation, endothelial dysfunction, and fibrotic changes that progressively increase pulmonary vascular resistance. Blocking AT1 receptors could theoretically attenuate these processes and reduce right ventricular afterload. This reasoning is a plausible class-effect extrapolation applicable to ARBs broadly.

However, the specific target here — pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5 PH) — is pathophysiologically heterogeneous and distinct from idiopathic PAH. RAAS blockade is not established as a primary treatment strategy for Group 5 PH, and no direct evidence of any kind exists for Azilsartan in pulmonary hypertension. The TxGNN prediction reflects mechanistic plausibility within the ARB drug class, not clinical or preclinical validation for this compound specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on Rank 2 Search Results:** A PubMed search for "pulmonary hypertension owing to lung disease and/or hypoxia" returned 20 publications, but these all concern general hypoxia biology (HIF-1α signaling, altitude physiology, neurological effects of hypoxia) and contain no data on Azilsartan or ARBs in hypoxic pulmonary hypertension. They are not counted as supporting evidence.

---

## EU Market Information

Azilsartan medoxomil currently holds no European Medicines Agency (EMA) marketing authorization. The drug is approved in other jurisdictions (notably the United States as **Edarbi®**), but has not been authorized for use within the European Union. No product-specific SmPC is available through EMA at this time.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Critical safety flag for Rank 4 prediction — Malignant renovascular hypertension:** Bilateral renal artery stenosis is a recognized contraindication for ARBs and ACE inhibitors. AT1 blockade in this setting causes efferent arteriolar dilation, abolishing the compensatory mechanism for maintaining glomerular filtration rate (GFR), and may precipitate acute renal failure. This candidate must not be advanced.

> **Model artifact warning for Rank 10 prediction — Hypotrichosis simplex of the scalp:** ARBs are associated with drug-induced alopecia as an established side effect. The gene-level pathology of hypotrichosis simplex (LPAR6/LIPH mutations) has no known relationship with the RAAS. This TxGNN prediction is likely a spurious association and should be disregarded.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top-ranked TxGNN predictions for Azilsartan medoxomil are rated L5 — model prediction only, with no clinical trials or direct publications identified for any indication. The drug is not authorized in the EU, and two blocking data gaps (safety warnings and MOA) remain unresolved, precluding a reliable safety or mechanistic evaluation.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain prescribing information (US label or SmPC equivalent) to assess contraindications, key warnings, and special population restrictions
- **Resolve DG002 (High):** Query DrugBank API to confirm and document the mechanism of action
- **Reprioritize candidates for research framing:**
  - **Rank 3 — Malignant hypertensive renal disease** (Research Question): Strongest mechanistic rationale within the ARB class (renoprotection via RAAS blockade); best candidate for hypothesis-driven investigation once safety data confirmed
  - **Rank 6 — Cerebrovascular disorder** (Research Question): Supported by ARB class-level evidence from the LIFE (Losartan) and VALUE (Valsartan) trials; warrants a targeted literature review on stroke prevention with ARBs before scoping an Azilsartan-specific study
- **Retire immediately:** Rank 4 (malignant renovascular hypertension — contraindicated), Rank 7 (obsolete disease ontology term), Rank 10 (likely model artifact with adverse pharmacological signal)
- **Pending EU regulatory pathway review:** If mechanistic evidence matures, assess whether an EU orphan designation or repurposing pathway (EMA PRIME scheme) could apply
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

