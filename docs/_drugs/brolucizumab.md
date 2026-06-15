---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Brolucizumab
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

# Brolucizumab: From Neovascular Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Brolucizumab (Beovu®) is an anti-VEGF-A single-chain antibody fragment (scFv), approved internationally for neovascular (wet) age-related macular degeneration (AMD) via intravitreal injection; it is not currently marketed in Taiwan.
The TxGNN model's top-ranked prediction is **Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies** (score: 99.67%),
yet **zero clinical trials or literature** exist to support this or any of the top 10 predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neovascular (wet) AMD (internationally approved; not marketed in Taiwan) |
| Predicted New Indication | Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, brolucizumab is an anti-VEGF-A single-chain antibody fragment (scFv) that binds and neutralizes all isoforms of VEGF-A, thereby suppressing pathological choroidal and retinal neovascularization. It is delivered exclusively via intravitreal injection, yielding systemic plasma concentrations below 5 ng/mL — far too low for meaningful systemic target engagement. Internationally, it is approved as Beovu® for neovascular (wet) AMD.

Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies involves mutations in nuclear-encoded genes required for respiratory chain complex assembly and function, leading to impaired cellular ATP production. There is no established connection between VEGF-A signaling and primary mitochondrial energy metabolism. While VEGF has been observed to have some cytoprotective roles in hypoxic environments, this is unrelated to the nuclear-encoded respiratory chain defects that define this disease.

The mechanistic link between brolucizumab and this condition is extremely weak. The high TxGNN score most likely reflects indirect graph node connections between VEGF-related pathways and energy metabolism nodes in the knowledge graph — a computational artifact rather than a clinically plausible repurposing hypothesis. Route incompatibility further disqualifies the prediction: intravitreal injection cannot deliver therapeutically relevant concentrations to systemic mitochondria.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## Taiwan Market Information

Brolucizumab is not currently marketed in Taiwan (0 authorizations). Internationally, it is approved as Beovu® in the United States (FDA, October 2019) and in the European Union (EMA) for neovascular AMD, and is under regulatory review or approved in multiple other markets.

---

## Predicted Indications — Full Landscape

All 10 TxGNN predictions are L5 with no clinical evidence. Given brolucizumab's highly specific intravitreal route, mechanistic plausibility varies considerably across the predictions. The table below provides a comparative view to guide prioritization:

| Rank | Disease | TxGNN Score | Mechanistic Relevance | Route Compatible |
|------|---------|-------------|----------------------|-----------------|
| 1 | Mitochondrial oxidative phosphorylation disorder (nuclear DNA) | 99.67% | Extremely low — no known VEGF role in mitochondrial respiratory chain | ✗ |
| 2 | Esophageal varices without bleeding | 99.12% | Low — systemic anti-VEGF rationale theoretically exists, but intravitreal route cannot reach portal vasculature | ✗ |
| 3 | Esophageal varices with bleeding | 99.12% | Low — same as above; acute hemorrhage context makes this additionally unsafe | ✗ |
| 4 | Exocrine pancreatic insufficiency | 99.07% | None — VEGF-A has no established role in exocrine enzyme secretion | ✗ |
| 5 | MRCS syndrome | 98.54% | Very low — retinal component present, but atrophic rather than neovascular; no VEGF driver | Partial |
| 6 | Pigmented paravenous retinochoroidal atrophy (PPRA) | 98.33% | Low-moderate — same ocular tissue and delivery route; VEGF overexpression not established in PPRA | ✓ |
| 7 | Familial flecked retinopathy | 97.90% | Low — genetic/degenerative photoreceptor disease (e.g., ABCA4 mutations), not neovascular | ✓ |
| 8 | Ectopia lentis-chorioretinal dystrophy-myopia syndrome | 97.82% | Moderate if choroidal neovascularization (CNV) is present — myopic CNV is an established anti-VEGF target | ✓ |
| 9 | Retinal dystrophy in systemic or cerebroretinal lipidoses | 97.73% | Very low — lysosomal storage disorder; retinal degeneration is secondary and VEGF-independent | ✓ |
| 10 | Senile reticular retinal degeneration | 97.71% | Moderate — AMD-related phenotype (reticular pseudodrusen); closest to the approved indication; however, if purely dry-form, anti-VEGF benefit is unproven | ✓ |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Taiwan TFDA package insert data is unavailable for brolucizumab (Data Gap DG001: Blocking). Based on international labeling (Beovu® FDA/EMA SmPC), key safety signals include intraocular inflammation, retinal vasculitis, retinal vascular occlusion, and endophthalmitis — all specific to the intravitreal route. These safety profiles would not directly apply to any hypothetical systemic repurposing attempts.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are L5 (AI model prediction only), supported by zero clinical trials and zero published literature. The highest-ranked prediction has essentially no mechanistic plausibility, and brolucizumab's intravitreal delivery route makes it fundamentally incompatible with the majority of predicted systemic indications.

**If further exploration is warranted, prioritize these three candidates in order:**

1. **Rank 10 — Senile reticular retinal degeneration**: This AMD-related phenotype (reticular pseudodrusen) is the closest condition to brolucizumab's approved indication. Should neovascular transformation occur, the existing clinical framework for wet AMD would directly apply.
2. **Rank 8 — Ectopia lentis-chorioretinal dystrophy-myopia syndrome**: Myopic choroidal neovascularization is an established anti-VEGF indication; if CNV is a component of this syndrome, the mechanistic case becomes substantive.
3. **Rank 6 — Pigmented paravenous retinochoroidal atrophy (PPRA)**: Same tissue target and delivery route as the approved indication; inflammatory microenvironment modulation by anti-VEGF scFv is biologically plausible, though unvalidated.

**To proceed, the following is needed:**

- Resolve Data Gap DG001 (Blocking): Obtain Taiwan TFDA package insert for safety screening — required before any S1 safety evaluation
- Resolve Data Gap DG002 (High): Retrieve MOA data from DrugBank API to enable formal mechanistic linkage analysis
- Conduct targeted literature search for anti-VEGF therapy in reticular retinal degeneration and PPRA
- Investigate whether VEGF overexpression is documented histologically in PPRA or ectopia lentis-associated CNV
- Assess orphan drug designation eligibility for the three prioritized rare ophthalmic indications, given their ultra-rare disease status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

