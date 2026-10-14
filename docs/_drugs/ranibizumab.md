---
layout: default
title: Ranibizumab
parent: High Evidence (L1-L2)
nav_order: 507
evidence_level: L1
indication_count: 10
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Ranibizumab: From Neovascular Age-Related Macular Degeneration to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Ranibizumab is an anti-VEGF antibody fragment, originally used to treat neovascular (wet) age-related macular degeneration (AMD) and other retinal diseases.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
with **no registered clinical trials** but **20 publications** (including post hoc analyses of the Phase 3 RIDE/RISE trials and a randomized trial of a ranibizumab port delivery system) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular (wet) age-related macular degeneration (AMD), visual impairment due to diabetic macular oedema (DME), proliferative diabetic retinopathy (PDR), macular oedema secondary to retinal vein occlusion, and choroidal neovascularisation (CNV) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| EU Market Status | Cancelled only (all licenses cancelled) |
| Number of Authorizations | 7 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ranibizumab is an anti-VEGF antibody fragment. VEGF drives retinal vascular permeability and neovascularisation in diabetic retinopathy, so blocking it plausibly slows disease progression and promotes regression of retinopathy severity.

Ranibizumab is already approved in the EU for DME and PDR, so severe nonproliferative diabetic retinopathy sits on the same disease continuum, between earlier disease and the proliferative stage. Post hoc analyses of the Phase 3 RIDE/RISE trials showed regression of retinopathy severity, and a randomized trial tested a ranibizumab port delivery system in nonproliferative diabetic retinopathy.

No registered trials were supplied, so the evidence grade rests on the literature alone. The PMIDs have not been independently verified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | PAVILION: ranibizumab port delivery system vs monitoring in nonproliferative diabetic retinopathy without macular oedema |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT (post hoc) | Clin Ophthalmol | Predictors of early diabetic retinopathy regression with ranibizumab in RIDE/RISE |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | RCT (post hoc meta-analysis) | Ophthalmol Retina | Baseline DR severity and time to DME resolution with ranibizumab in Phase 3 trials |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Systematic review/meta-analysis | Eur J Pharmacol | Sustained ranibizumab port delivery for disease modification in DR and DME |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Ranibizumab has been proven effective in diabetic retinopathy, including DME |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Systematic review/meta-analysis | Health Technol Assess | Anti-VEGF drugs vs laser photocoagulation for diabetic retinopathy |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | Cohort | Front Endocrinol | Nomogram predicting response to anti-VEGF plus laser in severe NPDR |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Open-label extension analysis | BMJ Open Ophthalmol | Effect of less frequent ranibizumab on DRSS scores in RIDE/RISE extension |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Trial follow-up | Retina | Five-year changes in DR severity with ranibizumab in DRCR.net Protocol I |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Simulation | BMJ Open Ophthalmol | Long-term impact of proactive anti-VEGF therapy in severe NPDR |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000715 | Lucentis | Not specified | Neovascular (wet) AMD, CNV, DME, macular oedema secondary to RVO |
| EMEA/H/C/005019 | Ranivisio | Not specified | Neovascular (wet) AMD, DME, PDR, macular oedema secondary to RVO, CNV |
| EMEA/H/C/005545 | Byooviz | Not specified | Neovascular (wet) AMD, DME, PDR, macular oedema secondary to RVO, CNV |
| EMEA/H/C/005617 | Ximluci | Not specified | Neovascular (wet) AMD, DME, PDR, macular oedema secondary to RVO, CNV |
| EMEA/H/C/006055 | Rimmyrah | Not specified | Neovascular (wet) AMD, DME, PDR, macular oedema secondary to RVO, CNV |

All 7 authorizations (the two others are Ranluspec, EMEA/H/C/006502, and Epruvy, EMEA/H/C/006528) are listed as cancelled.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): eye infectious disease and conjunctivitis.
- **Drug Interactions**: No interaction records were found.
- A case report describes capsular block syndrome after an intravitreal ranibizumab injection in a patient with AMD, which is an isolated adverse event.

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Randomized evidence and post hoc analyses of Phase 3 trials (RIDE/RISE, DRCR.net Protocol I, PAVILION) support ranibizumab for diabetic retinopathy, and the drug is already approved for DME and PDR. However, no trials are registered for this exact indication in the data compiled, and all EU licenses are currently cancelled.

**To proceed, the following is needed:**
- Safety information from the SmPC (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Verification of the cited PMIDs and a registered trial search for severe NPDR
- Clarification of EU regulatory status and available formulations or routes (including the port delivery system)
- Screening for active ocular or periocular infection before use, given the knowledge-graph contraindication signals

**Other predicted indications:** The remaining predictions (immature, tetanic, craniostenosis, mature, nuclear senile, cortical and senile cataract, type 2 diabetes-associated cataract, and hemorrhagic disease of the newborn) have no mechanistic rationale and no direct supporting evidence. They are most likely graph artifacts, and the recommendation for each is **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

