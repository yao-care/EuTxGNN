---
layout: default
title: Diroximel Fumarate
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
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

# Diroximel Fumarate: From Multiple Sclerosis to Diabetic Cataract

## One-Sentence Summary

Diroximel fumarate (brand name: Vumerity) is a prodrug approved for the treatment of relapsing forms of multiple sclerosis (MS), acting through its active metabolite monomethyl fumarate (MMF) to activate the Nrf2 antioxidant pathway.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, based on a theoretical mechanistic link between Nrf2-mediated antioxidant protection and oxidative lens damage in diabetes.
Currently, **no clinical trials** and **no publications** exist to support this repurposing direction — evidence rests entirely on AI model prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsing forms of multiple sclerosis |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.9993% |
| Evidence Level | L5 |
| EU Market Status | Not authorized (0 licenses on record) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Diroximel fumarate is rapidly hydrolyzed in the gastrointestinal tract to its active metabolite, monomethyl fumarate (MMF). MMF activates the Nrf2 (Nuclear Factor Erythroid 2-Related Factor 2) transcription factor, which in turn upregulates a suite of cytoprotective and antioxidant enzymes — including heme oxygenase-1 (HO-1), NAD(P)H quinone dehydrogenase 1 (NQO1), and superoxide dismutase (SOD). This is the same mechanism responsible for its neuroprotective and anti-inflammatory effects in relapsing MS.

Diabetic cataract arises from chronic hyperglycemia activating the polyol pathway, leading to sorbitol accumulation, osmotic swelling, advanced glycation end-product (AGE) deposition, and ultimately oxidative damage to lens crystallin proteins. Because Nrf2 activation upregulates the same antioxidant enzymes that counteract these processes, a theoretical pathway exists for diroximel fumarate to protect against lens protein oxidation and cataract progression.

However, this entire rationale remains at the level of mechanistic hypothesis. No published animal studies, in vitro lens cell experiments, or clinical trials have examined diroximel fumarate — or even MMF directly — in any ocular indication. Critical unknowns include whether systemic oral dosing achieves therapeutically relevant MMF concentrations in the avascular lens, and whether the polyol-pathway component of diabetic cataract is sufficiently Nrf2-amenable to be modified pharmacologically. The TxGNN model's near-perfect score (99.9993%) reflects knowledge-graph pathway proximity, not empirical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the Nrf2–oxidative stress mechanistic bridge between diroximel fumarate and diabetic cataract is intellectually coherent, there is a complete absence of empirical evidence at every level — no preclinical models, no translational data, and no clinical signal — making any advancement premature.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept**: In vitro lens epithelial cell studies under high-glucose conditions + streptozotocin-induced diabetic rodent cataract models, measuring Nrf2 activation, HO-1/NQO1 induction, and lens opacity scoring after oral diroximel fumarate dosing
- **Ocular pharmacokinetics**: MMF concentration measurement in aqueous humor and lens tissue following systemic administration, to confirm adequate drug exposure at the target organ
- **MOA documentation**: Query DrugBank API to formally fill the DG002 data gap (mechanism of action) and confirm Nrf2 as the primary pathway
- **Safety review**: Retrieve and parse the approved SmPC to address DG001 (package insert warnings and contraindications), which is currently blocking S1 safety pre-screening
- **Comparative benchmark**: Assess other known Nrf2 activators (e.g., sulforaphane, bardoxolone methyl) with published ocular data to calibrate how realistic lens penetration and efficacy are as a drug class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

