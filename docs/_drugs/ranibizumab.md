---
layout: default
title: Ranibizumab
parent: AI Predictions (L5)
nav_order: 507
evidence_level: L5
indication_count: 9
monitor_inn: "Ranibizumab"
predicted_indications: ["mature cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "tetanic cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "hemorrhagic disease of newborn"]
last_modified_at: 2026-10-28
description: "Ranibizumab: predicted new indication Mature cataract (evidence level L5). Approved use: Neovascular (wet) age-related macular degeneration (AMD)…"
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ranibizumab: From Neovascular Age-Related Macular Degeneration to Mature Cataract
{: .text-alpha }

## One-Sentence Summary

Ranibizumab is an anti-VEGF eye injection, originally used for neovascular (wet) age-related macular degeneration and other retinal vascular conditions.
The TxGNN model predicts it may be effective for **mature cataract**, but **no clinical trials** and only **2 publications** were found, and neither tests ranibizumab as a treatment for cataract.
The prediction is best treated as a model artefact rather than a real therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular (wet) age-related macular degeneration (AMD), plus diabetic macular oedema, proliferative diabetic retinopathy, retinal vein occlusion macular oedema and choroidal neovascularisation |
| Predicted New Indication | Mature cataract |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 7 of 7) |
| Number of Authorizations | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ranibizumab is known as an anti-VEGF (vascular endothelial growth factor) antibody fragment given by intravitreal injection. Its efficacy in retinal neovascular and oedema conditions is established, which is why it is authorised for these uses.

The link to mature cataract is weak. Cataract is an opacity of the lens, and no known VEGF-driven mechanism would be reversed by ranibizumab. The only publication on mature cataract describes combined cataract surgery and ranibizumab injection in eyes with diabetic macular oedema. There, ranibizumab treats the retinal disease, not the cataract. The second paper reports cataract progression after a dexamethasone implant, which does not involve ranibizumab.

The high TxGNN score most likely reflects similarities the model (deep learning) learned between related ocular diseases, not biological evidence of a genuine therapeutic relationship. The other cataract subtypes also scored in the same range (about 0.9999), which supports this reading. Because no cited study directly examines ranibizumab as a treatment for mature cataract, the evidence level is capped at L5.

## Clinical Trial Evidence

Currently no related clinical trials are registered for mature cataract.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40790176](https://pubmed.ncbi.nlm.nih.gov/40790176/) | 2025 | Cohort (eyes randomly assigned to groups) | BMC Ophthalmology | Compared combined cataract surgery with or without intravitreal ranibizumab in 39 eyes with diabetic macular oedema and advanced cataract. It addresses macular oedema outcomes, not treatment of the cataract. |
| [30606142](https://pubmed.ncbi.nlm.nih.gov/30606142/) | 2019 | Case report | BMC Ophthalmology | Rapid progression of cataract to the mature stage after a dexamethasone implant for macular oedema. Ranibizumab was not involved. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000715 | Lucentis | Not specified | Adults: neovascular (wet) AMD, visual impairment due to choroidal neovascularisation (CNV), diabetic macular oedema (DME), macular oedema secondary to retinal vein occlusion... |
| EMEA/H/C/005019 | Ranivisio | Not specified | Adults: neovascular (wet) AMD, DME, proliferative diabetic retinopathy (PDR), macular oedema secondary to retinal vein occlusion... |
| EMEA/H/C/005617 | Ximluci | Not specified | Adults: neovascular (wet) AMD, DME, PDR, macular oedema secondary to retinal vein occlusion... |
| EMEA/H/C/005545 | Byooviz | Not specified | Adults: neovascular (wet) AMD, DME, PDR, macular oedema secondary to retinal vein occlusion... |
| EMEA/H/C/006055 | Rimmyrah | Not specified | Adults: neovascular (wet) AMD, DME, PDR, macular oedema secondary to retinal vein occlusion... |

The list shows 5 of 7 authorizations. The other two are Ranluspec (EMEA/H/C/006502) and Epruvy, previously Ranibizumab Midas (EMEA/H/C/006528), with the same retinal indications. None of the authorizations covers cataract.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: The knowledge graph records contraindication relations with eye infectious disease and conjunctivitis. These are not taken from product label text and should be checked against the SmPC.
- **Reported adverse event in the literature**: One 2024 case report describes capsular block syndrome after an intravitreal ranibizumab injection in a patient with AMD.

For other safety information, including warnings, contraindications and drug interactions, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no study showing that ranibizumab treats cataract. There is also no plausible biological mechanism linking VEGF inhibition to lens opacity. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related ocular diseases, not biological evidence.

**To proceed, the following is needed:**
- A plausible mechanistic rationale for anti-VEGF activity in lens opacity, supported by preclinical data
- Mechanism of action data for ranibizumab
- Any clinical or controlled study that directly tests ranibizumab on cataract itself
- Safety information from the SmPC (warnings and contraindications), including the knowledge-graph contraindication relations with eye infection and conjunctivitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

