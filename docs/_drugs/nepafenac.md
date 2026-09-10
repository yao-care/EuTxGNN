---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Post-Cataract Surgery Ocular Inflammation to Eye Disease

## One-Sentence Summary

> Nepafenac is a topical ophthalmic NSAID whose established use, based on the clinical trial evidence in this dataset, is the prevention and treatment of ocular inflammation and pain after cataract surgery.
> The TxGNN model predicts it may be effective more broadly for **Eye Disease**,
> with **41 clinical trials** and **20 publications** currently supporting this direction — though this predicted indication substantially overlaps with the drug's already-known ophthalmic profile rather than representing a clearly novel therapeutic area.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in regulatory data (per trial evidence: prevention/treatment of ocular inflammation and pain after cataract surgery) |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not available for this evaluation. Based on the supporting literature, nepafenac is a prodrug NSAID that, after topical ocular administration, is converted intraocularly to its active metabolite **amfenac**, which inhibits COX-1/COX-2 and reduces prostaglandin-mediated inflammation (PMID 26474497). Its efficacy in reducing post-cataract-surgery ocular inflammation and pain — and in reducing the risk of postoperative macular edema in diabetic patients — is well established across dozens of completed Phase 3 trials.

The predicted indication "eye disease" is a broad category, and the supporting clinical trial portfolio shows the drug already being tested well beyond its narrow post-surgical label: diabetic macular edema and diabetic retinopathy (NCT01853072, NCT01872611, NCT00939276, NCT00782717, NCT01331005), uveitis-associated macular edema (NCT01939691), glaucoma-related laser iridotomy inflammation (NCT02955641), corneal endothelial dystrophy (NCT04843839), and epiretinal membrane surgery (NCT00818844).

Mechanistically this is plausible because amfenac reaches therapeutic concentrations not just in the anterior segment but also in the posterior segment (retina/choroid) of the eye (PMID 26474497), and animal studies show nepafenac inhibits diabetes-induced retinal microvascular disease and retinal angiogenesis (PMID 17259381, PMID 19897019). However, because "eye disease" is essentially the organ-system category nepafenac already operates in, this prediction has limited discriminative value as a *novel* repurposing signal — it largely confirms known pharmacology rather than pointing to an unexpected new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% QD superior to vehicle for clinical outcomes in diabetic subjects after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Replicate Phase 3 study confirming superiority in diabetic subjects post-cataract surgery |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | Terminated | 175 | Evaluated nepafenac in diabetic retinopathy patients with macular edema post-cataract surgery |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | Nepafenac vs vehicle for reducing macular edema incidence in diabetic retinopathy patients |
| [NCT01331005](https://clinicaltrials.gov/study/NCT01331005) | Phase 2 | Completed | 125 | Topical NSAIDs (incl. nepafenac) effect on macular volume in non-central diabetic macular edema |
| [NCT00801905](https://clinicaltrials.gov/study/NCT00801905) | Phase 2 | Terminated | 50 | Topical nepafenac for macular thickening related to pan-retinal photocoagulation in diabetic retinopathy |
| [NCT01939691](https://clinicaltrials.gov/study/NCT01939691) | Phase 4 | Terminated | 9 | Nepafenac vs difluprednate for uveitis-associated macular edema |
| [NCT02955641](https://clinicaltrials.gov/study/NCT02955641) | N/A | Unknown | 100 | Efficacy/necessity of anti-inflammatory drops (incl. nepafenac) after laser peripheral iridotomy |
| [NCT04843839](https://clinicaltrials.gov/study/NCT04843839) | Phase 2 | Unknown | 30 | Topical NSAID eye drops for corneal cloudiness in congenital endothelial dystrophy (SLC4A11 mutation) |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | Completed | 40 | Nepafenac vs placebo for reducing macular volume after epiretinal membrane surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review/Meta-analysis | Eur J Ophthalmol | Nepafenac's effect on macular swelling prevention and visual outcome after cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology. Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% for inflammation control after laser peripheral iridotomy |
| [35196591](https://pubmed.ncbi.nlm.nih.gov/35196591/) | 2022 | RCT | Ophthalmology. Glaucoma | Nepafenac 0.1% vs bromfenac 0.09% for inflammation after laser peripheral iridotomy |
| [24345317](https://pubmed.ncbi.nlm.nih.gov/24345317/) | 2014 | RCT | Am J Ophthalmol | Randomized study of nepafenac's effect on intraocular pressure in cataract eyes |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | RCT | J Cataract Refract Surg | Prophylactic nepafenac vs ketorolac vs placebo for postoperative macular edema prevention |
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | Phase 3 Study | J Cataract Refract Surg | Once-daily nepafenac 0.3% for prevention/treatment of ocular inflammation and pain post-cataract surgery |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of diagnostic and therapeutic agents (incl. NSAIDs) for non-infectious corneal injury |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Role of nepafenac in routine cataract surgery |
| [16466612](https://pubmed.ncbi.nlm.nih.gov/16466612/) | 2006 | Review | Curr Med Res Opin | Ocular permeation and inhibition of retinal inflammation — clinical utility of nepafenac |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | PK/Distribution Study | Exp Eye Res | Nepafenac and active metabolite amfenac distribute to the posterior segment of the eye |

---

## EU Market Information

Nepafenac is currently **not marketed** in the EU per this dataset — no marketing authorization records are available (`total_licenses: 0`). Note that nepafenac ophthalmic suspensions are known internationally under brand names such as NEVANAC and ILEVRO (referenced in the clinical trial evidence above), but no corresponding EU authorization entry exists in the current data pack.

---

## Safety Considerations

Safety information (key warnings, contraindications, and drug interactions) has not yet been collected for this candidate. This is flagged as a **blocking data gap** in the source evidence pack — TFDA/EU product label (SmPC) warnings and contraindications must be obtained before this candidate can proceed to a preliminary safety assessment (S1). Please refer to the SmPC once available for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap on core safety information (warnings, contraindications, DDI) prevents any preliminary safety review (S1), and MOA confirmation from DrugBank is still missing.
- The predicted indication "eye disease" is non-specific and largely overlaps with nepafenac's already-established ophthalmic anti-inflammatory profile, limiting its value as a genuinely novel repurposing signal despite the strong (L1) evidence base.

**To proceed, the following is needed:**
- TFDA/EU SmPC warnings, contraindications, and drug interaction data (blocking)
- Confirmed DrugBank mechanism-of-action record
- Refinement of the target indication to a specific, clinically meaningful subtype (e.g., diabetic macular edema or uveitic macular edema) rather than the generic "eye disease" category
- Clarification of EU marketing authorization status and regulatory pathway, since the drug is not currently marketed in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

