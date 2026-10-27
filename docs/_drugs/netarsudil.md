---
layout: default
title: Netarsudil
parent: AI Predictions (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Netarsudil: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Reduction of elevated intraocular pressure (IOP) in adult patients wi…"
monitor_inn: "Netarsudil"
predicted_indications: ["hypoglycemia", "Axenfeld anomaly", "hydrophthalmos", "hereditary thrombocytopenia with normal platelets", "dense granule disease", "marcothrombocytopenia with mitral valve insufficiency"]
---

# Netarsudil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Netarsudil: From Glaucoma and Ocular Hypertension to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Netarsudil is an eye-drop medicine originally used to lower raised eye pressure in adults with primary open-angle glaucoma or ocular hypertension.
The TxGNN model's top prediction is **primary hereditary glaucoma**, but this prediction has **no clinical trials and no publications** specific to it.
The strongest evidence applies to the closely related, already approved glaucoma indication (**26 clinical trials** and **19 publications** mapped to "glaucoma"), which largely confirms the existing label rather than representing true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reduction of elevated intraocular pressure (IOP) in adult patients with primary open-angle glaucoma or ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 for the top prediction (model prediction only); L1 for the related indications "glaucoma", "glaucoma 1, open angle" and "open angle glaucoma" |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold for primary hereditary glaucoma; Proceed with Guardrails for the glaucoma-related indications |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the drug database record compiled for this report. Pharmacology data do show that netarsudil acts on Rho-associated kinases (ROCK1 and ROCK2). It also inhibits the norepinephrine transporter. Together these actions are thought to lower eye pressure by increasing fluid drainage through the trabecular meshwork, reducing pressure in the episcleral veins, and decreasing fluid production in the eye.

Primary hereditary glaucoma involves impaired drainage of fluid from the eye, so a drug that improves outflow is mechanistically plausible. However, the high model score (0.995) is a computational prediction only. The prediction may also overlap with the approved indication (open-angle glaucoma) rather than describing a distinct hereditary population.

Several other predicted indications are of low credibility. Hypoglycemia, hereditary thrombocytopenia, dense granule disease and macrothrombocytopenia with mitral valve insufficiency have no plausible link to a topical eye drop, and are likely artifacts of the knowledge graph. Axenfeld anomaly and hydrophthalmos (congenital glaucoma) are theoretically plausible through eye pressure lowering, but have no supporting evidence, and safety in infants is not established.

---

## Clinical Trial Evidence

The table below shows the most relevant trials mapped to the broader "glaucoma" prediction (rank 2). No trials are mapped to primary hereditary glaucoma itself.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02558374](https://clinicaltrials.gov/study/NCT02558374) | Phase 3 | Completed | 708 | Netarsudil 0.02% once daily vs timolol 0.5% twice daily, 6-month IOP-lowering efficacy and safety |
| [NCT02674854](https://clinicaltrials.gov/study/NCT02674854) | Phase 3 | Completed | 750 | Netarsudil/latanoprost combination vs each component alone, 3 months |
| [NCT02207621](https://clinicaltrials.gov/study/NCT02207621) | Phase 3 | Completed | 756 | Netarsudil once or twice daily vs timolol, 12-month efficacy and safety |
| [NCT02558400](https://clinicaltrials.gov/study/NCT02558400) | Phase 3 | Completed | 718 | Netarsudil/latanoprost combination vs components, 12 months |
| [NCT07082816](https://clinicaltrials.gov/study/NCT07082816) | Phase 3 | Completed | 489 | Reformulated netarsudil/latanoprost vs active control in open-angle glaucoma or ocular hypertension |
| [NCT03284853](https://clinicaltrials.gov/study/NCT03284853) | Phase 3 | Completed | 436 | Netarsudil/latanoprost vs bimatoprost/timolol (MERCURY 3), 6 months |
| [NCT02207491](https://clinicaltrials.gov/study/NCT02207491) | Phase 3 | Completed | 411 | Netarsudil vs timolol, 3-month efficacy and safety |
| [NCT04620135](https://clinicaltrials.gov/study/NCT04620135) | Phase 3 | Completed | 245 | Netarsudil once daily vs ripasudil twice daily in Japanese patients, 4 weeks |
| [NCT02246764](https://clinicaltrials.gov/study/NCT02246764) | Phase 3 | Completed | 93 | 12-month ocular and systemic safety of netarsudil vs timolol |
| [NCT04981886](https://clinicaltrials.gov/study/NCT04981886) | Phase 4 | Unknown | 115 | Netarsudil vs bimatoprost (Lumigan) in normal tension glaucoma; results not confirmed |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37615697](https://pubmed.ncbi.nlm.nih.gov/37615697/) | 2024 | RCT | Graefes Arch Clin Exp Ophthalmol | MERCURY-3: netarsudil/latanoprost compared with bimatoprost/timolol in open-angle glaucoma and ocular hypertension |
| [37603205](https://pubmed.ncbi.nlm.nih.gov/37603205/) | 2023 | RCT | Adv Ther | J-ROCKET: netarsudil vs ripasudil in Japanese patients |
| [41915113](https://pubmed.ncbi.nlm.nih.gov/41915113/) | 2026 | RCT | Adv Ther | J-ROCKET-2: netarsudil added to latanoprost in Japanese patients with inadequate IOP control |
| [35979215](https://pubmed.ncbi.nlm.nih.gov/35979215/) | 2022 | Meta-analysis | Front Med | Netarsudil/latanoprost combination vs monotherapy in open-angle glaucoma or ocular hypertension |
| [35686679](https://pubmed.ncbi.nlm.nih.gov/35686679/) | 2022 | Systematic review | Cochrane Database Syst Rev | Rho kinase inhibitors for primary open-angle glaucoma and ocular hypertension |
| [32826769](https://pubmed.ncbi.nlm.nih.gov/32826769/) | 2020 | Pooled RCT analysis | J Glaucoma | Pooled phase 3 data: netarsudil non-inferior to timolol, with few serious or systemic adverse events |
| [32166538](https://pubmed.ncbi.nlm.nih.gov/32166538/) | 2020 | Pooled analysis | Adv Ther | Pooled MERCURY-1 and -2 results for the netarsudil/latanoprost combination |
| [31695162](https://pubmed.ncbi.nlm.nih.gov/31695162/) | 2020 | Review | Eye (Lond) | Review of new glaucoma medications, including netarsudil |
| [32637736](https://pubmed.ncbi.nlm.nih.gov/32637736/) | 2020 | Case report | Am J Ophthalmol Case Rep | Netarsudil-associated epithelial keratopathy |
| [41675443](https://pubmed.ncbi.nlm.nih.gov/41675443/) | 2026 | Case series | Am J Ophthalmol Case Rep | Netarsudil-associated conjunctival fragility |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004583 (cancelled) | Rhokiinsa | Not specified | Reduction of elevated intraocular pressure (IOP) in adult patients with primary open-angle glaucoma or ocular hypertension. |

The only EU authorization for the single-agent product is cancelled. A fixed-dose combination of netarsudil with latanoprost has a separate EU authorization (approved January 2021), but it is not part of the data compiled for this report.

---

## Safety Considerations

Package-insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for formal safety information.

Published reports and trial-based assessments point to the following ocular effects to monitor:
- Conjunctival hyperemia (the most common side effect)
- Corneal verticillata and epithelial keratopathy
- Corneal edema, including reticular epithelial edema
- Conjunctival fragility, relevant before glaucoma surgery
- Punctal stenosis or closure
- Corneal honeycombing in children with glaucoma (56% of 16 children in one series)

**Drug interactions:** The pharmacology data show interaction with the targets ROCK1 and ROCK2. No drug-drug interactions are listed.

---

## Conclusion and Next Steps

**Decision: Hold (primary hereditary glaucoma); Proceed with Guardrails (glaucoma, open-angle glaucoma)**

**Rationale:**
- For the top-ranked prediction, primary hereditary glaucoma, there are no trials or publications. The high score is a model prediction only, so evidence is at L5.
- The strong evidence (multiple completed Phase 3 RCTs, evidence level L1) supports the already approved open-angle glaucoma/ocular hypertension use. This confirms the existing label rather than showing new repurposing value.

**To proceed, the following is needed:**
- Clinical or observational data in genetically defined or hereditary glaucoma populations (for example MYOC-linked), including whether these patients were separate from general open-angle glaucoma
- Safety data in children and infants before considering congenital forms (hydrophthalmos, Axenfeld anomaly)
- Verification of the cancelled EU authorization, supply and current regulatory availability, including the status of the netarsudil/latanoprost combination
- SmPC warnings and contraindications to complete safety screening
- Detailed mechanism of action data from the drug database
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

