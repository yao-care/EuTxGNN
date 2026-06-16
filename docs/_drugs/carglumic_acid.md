---
layout: default
title: Carglumic Acid
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Carglumic Acid
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

# Carglumic Acid: From N-acetylglutamate Synthase Deficiency to Cystic Teratoma

## One-Sentence Summary

Carglumic acid (brand name: Carbaglu) is a synthetic analogue of N-acetylglutamate (NAG), originally approved for the treatment of hyperammonemia caused by N-acetylglutamate synthase (NAGS) deficiency — an ultra-rare urea cycle disorder.
The TxGNN model predicts it may be effective for **Cystic Teratoma**, with **0 clinical trials** and **0 publications** currently supporting this direction, making this an AI-prediction-only finding with no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperammonemia due to N-acetylglutamate synthase (NAGS) deficiency |
| Predicted New Indication | Cystic Teratoma |
| TxGNN Prediction Score | 86.61% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, Carglumic acid acts as a synthetic structural analogue of N-acetylglutamate (NAG) — the essential allosteric activator of carbamoyl phosphate synthetase 1 (CPS1), which catalyzes the first committed step of the urea cycle. By mimicking NAG and activating CPS1, Carglumic acid restores ammonia detoxification capacity in patients whose NAGS enzyme is deficient or dysfunctional, thereby reducing toxic hyperammonemia.

Cystic teratoma is a benign germ cell tumor arising from aberrant differentiation of embryonic remnant cells. Its underlying pathogenesis involves ectopic embryonic tissue rather than metabolic dysregulation of the urea cycle, and there is no established biological connection between CPS1 activation, ammonia clearance, and teratoma formation or progression.

The TxGNN prediction for this pairing most likely reflects graph topology similarity within the biomedical knowledge graph — for example, shared nodes in metabolic disease clusters or rare-disease linkages — rather than any genuine mechanistic rationale. The Evidence Pack's repurposing rationale explicitly identifies this as a probable artifact of graph structure rather than a biologically meaningful signal. No supporting clinical, preclinical, or mechanistic evidence exists for this pairing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Carglumic acid is currently **not marketed in Taiwan** (未上市). No marketing authorizations are on record. This drug is approved in the EU (as Carbaglu, Recordati Rare Diseases) and the US (FDA orphan drug designation) for NAGS deficiency, but has not received TFDA authorization.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Carglumic acid carry L5 evidence (AI model prediction only; zero clinical trials, zero literature), and none of the predicted indications — ranging from benign developmental cysts (cystic teratoma, dermoid cysts) to orbital diseases and glaucoma — share a coherent biological pathway with the drug's known urea cycle/CPS1-activation mechanism. The mechanistic disconnect is severe enough that proceeding to any formal evaluation would not be scientifically justified at this stage.

**To proceed, the following is needed:**
- Formal MOA documentation from DrugBank or published literature to enable proper mechanism-to-indication matching
- Preclinical hypothesis generation: identification of any disease on this list where ammonia metabolism or the CPS1/NAG axis plays a documented pathophysiological role
- If prioritization is needed, the open-angle glaucoma prediction (Rank 7) warrants a dedicated literature review — glutamate excitotoxicity in retinal ganglion cells involves the glutamate/glutamine/ammonia axis, which is the most theoretically adjacent mechanistic pathway in this batch, though it remains speculative with no supporting data
- TFDA SmPC or equivalent safety documentation to complete the DG001 blocking data gap before any regulatory pathway analysis
- Consideration of whether the TxGNN model's graph topology (rather than biochemical similarity) is driving these predictions, which may warrant re-ranking candidates using mechanism-filtered scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

