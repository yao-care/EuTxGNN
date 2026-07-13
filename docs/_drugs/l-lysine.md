---
layout: default
title: L-Lysine
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# L-Lysine
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

# L-Lysine: From Nutritional Supplement to Gastroparesis

## One-Sentence Summary

L-Lysine is an essential amino acid primarily used as a dietary nutritional supplement to support protein synthesis, collagen formation, and carnitine biosynthesis.
The TxGNN model predicts it may be effective for **Gastroparesis**,
with **0 clinical trials** and **1 publication** currently supporting this direction — neither of which directly tests L-Lysine as a therapeutic agent for this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nutritional supplementation (essential amino acid) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, L-Lysine is an essential amino acid indispensable for several biosynthetic pathways: it serves as a structural substrate for lysyl oxidase (required for collagen and elastin cross-linking), as a precursor in carnitine biosynthesis (jointly with methionine), and there is limited animal model evidence suggesting it may modulate 5-HT (serotonin) receptor activity, which could theoretically influence gastrointestinal motility. Its efficacy as a nutritional supplement has been established in protein metabolism contexts.

Gastroparesis is a disorder defined by delayed gastric emptying without mechanical obstruction, driven by dysfunction of interstitial cells of Cajal (ICC), enteric neurons, and the autonomic nervous system. Regenerative approaches — such as mesenchymal stem cell therapy aimed at restoring ICC populations — represent an active area of exploratory research.

The mechanistic connection between L-Lysine supplementation and gastroparesis is highly indirect at best. While L-Lysine participates in collagen cross-linking and tissue repair, the core pathology of gastroparesis (autonomic neuropathy, ICC depletion, smooth muscle dysfunction) is not known to be directly addressable through amino acid supplementation alone. The TxGNN model's high prediction score (99.77%) most likely reflects knowledge graph structural relationships rather than a direct pharmacological mechanism, and should be interpreted cautiously at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Animal/Biomaterial Study | Bioengineering (Basel) | Mesenchymal stem cells delivered via gelatin-alginate hydrogels to restore ICC populations and enteric neurons in a gastroparesis animal model — not directly related to L-Lysine supplementation |

> **Note:** The single retrieved publication does not investigate L-Lysine as a therapeutic agent. It was retrieved based on keyword co-occurrence in the knowledge graph context and has no direct evidentiary value for this repurposing hypothesis.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (99.77%), there are zero registered clinical trials and no literature directly supporting L-Lysine supplementation as a treatment for gastroparesis. The proposed mechanistic link is speculative and does not map onto the established pathophysiology of the disease.

**To proceed, the following is needed:**
- Preclinical in vivo studies directly testing L-Lysine supplementation in validated gastroparesis animal models (e.g., STZ-diabetic mouse model)
- Mechanistic studies investigating whether L-Lysine or its metabolites (particularly carnitine via the L-Lysine → carnitine biosynthesis pathway) influence gastric emptying or ICC regeneration
- Retrieval of complete MOA data from DrugBank (currently unavailable — DG002, High severity)
- Evaluation of whether the 5-HT receptor modulation reported in animal anxiety models has any translatable effect in gastrointestinal functional contexts
- Safety profile characterization, including review of TFDA SmPC data (DG001, Blocking severity)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

