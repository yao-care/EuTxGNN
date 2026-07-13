---
layout: default
title: Dapagliflozin
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Dapagliflozin
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

# Dapagliflozin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Dapagliflozin is a well-established SGLT2 inhibitor, internationally approved for type 2 diabetes mellitus, heart failure with reduced ejection fraction, and chronic kidney disease — though no Taiwan marketing authorization records appear in the current dataset.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome (SPS)**, with **0 clinical trials** and **0 publications** currently supporting this specific direction.
The prediction achieves a high TxGNN score of 98.20%, but the mechanistic bridge between SGLT2 inhibition and the GABAergic autoimmune pathology of SPS remains unestablished.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved from Taiwan regulatory data; internationally recognized for Type 2 Diabetes, Heart Failure, and Chronic Kidney Disease |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known information, Dapagliflozin belongs to the SGLT2 (sodium-glucose cotransporter 2) inhibitor class. It works by blocking glucose reabsorption in the proximal renal tubule, leading to urinary glucose excretion and downstream metabolic benefits. Beyond glycosuria, SGLT2 inhibitors are recognized to activate AMPK, reduce reactive oxygen species, suppress pro-inflammatory cytokines (NF-κB, IL-6, TNF-α), and confer cardioprotective and renoprotective effects that extend well beyond glycemic control.

Classic Stiff Person Syndrome is a rare autoimmune neurological disorder driven by anti-GAD65 (glutamic acid decarboxylase 65) antibodies, which impair GABAergic inhibitory neurotransmission and result in progressive muscle rigidity, episodic spasms, and heightened sensitivity to external stimuli. The therapeutic backbone of SPS is GABA enhancement (diazepam, baclofen) and immunosuppression (intravenous immunoglobulin, rituximab). Dapagliflozin has no known direct effect on GABAergic neurotransmission, anti-GAD65 antibody production, or the specific T-cell / B-cell immune checkpoints implicated in SPS pathogenesis.

The high TxGNN score (98.20%) most likely reflects indirect co-occurrence of neuro-metabolic disease nodes within the knowledge graph — for example, shared metabolic stress pathways or inflammatory node overlaps — rather than a direct biological mechanistic link. Without supporting preclinical or clinical evidence, this prediction should be treated as a hypothesis-generating signal only, requiring independent mechanistic justification before any further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dapagliflozin in Classic Stiff Person Syndrome.

---

## Literature Evidence

Currently no related literature available for Dapagliflozin in Classic Stiff Person Syndrome.

---

## Taiwan Market Status

No Taiwan marketing authorization on record for Dapagliflozin. The drug is not marketed in Taiwan according to the current dataset (0 authorizations retrieved). Note that Dapagliflozin is internationally approved and marketed under the brand names Farxiga (AstraZeneca, USA) and Forxiga (AstraZeneca, EU/Taiwan TFDA approval may exist but was not captured in this dataset).

---

## Safety Considerations

Please refer to the official prescribing information / SmPC for safety information. Taiwan-specific TFDA prescribing information was not available in this dataset (Data Gap: TFDA warnings and contraindications — Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (98.20%), there is a fundamental mechanistic mismatch between Dapagliflozin's SGLT2 inhibition profile and the GABAergic autoimmune pathology of classic stiff person syndrome; zero clinical trials and zero publications support this pairing, leaving it as a model-only prediction with no biological validation.

**To proceed, the following is needed:**

- **MOA data gap closure**: Retrieve Dapagliflozin's complete mechanism of action from DrugBank API to assess any secondary neurological or immunomodulatory pathways (current severity: High)
- **TFDA SmPC retrieval**: Download and parse the TFDA prescribing information PDF to complete the safety profile before any S1 safety evaluation can proceed (current severity: Blocking)
- **Preclinical mechanistic study**: Assess whether SGLT2 inhibition or AMPK activation has any measurable effect on GABAergic transmission, anti-GAD65 antibody titres, or related autoimmune markers in animal models
- **Knowledge graph audit**: Investigate why TxGNN assigns a 98.20% score to SPS — identify the intermediate KG nodes driving this prediction to determine whether the signal reflects biological plausibility or graph topology artefacts
- **Broader indication landscape review**: Among the 10 predicted indications in this evidence pack, rank 9 (Pancreatic Agenesis, L4) has one relevant preclinical publication (PMID [33559163](https://pubmed.ncbi.nlm.nih.gov/33559163/)) showing dapagliflozin ameliorates pancreatic injury via AMPK/mTOR signalling in obese rats — though this addresses pancreatic *injury* (not congenital *agenesis*) and represents a disease-matching mismatch requiring separate review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

