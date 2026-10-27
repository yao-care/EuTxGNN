---
layout: default
title: Nepafenac
parent: High Evidence (L1-L2)
nav_order: 424
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Nepafenac: predicted new indication Eye disease (evidence level L1). Approved use: Prevention and treatment of postoperative pain and inflammation assoc…"
monitor_inn: "Nepafenac"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
---

# Nepafenac
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

## Nepafenac: From Postoperative Ocular Pain and Inflammation to Eye Disease
{: .text-alpha }

## One-Sentence Summary

Nepafenac is a topical NSAID eye drop, originally used to prevent and treat pain and inflammation after cataract surgery and to reduce the risk of macular oedema after cataract surgery in diabetic patients.
The TxGNN model predicts it may be effective for **eye disease** (a broad category that largely overlaps with its approved use).
The data compiled for this report include **43 clinical trials** and **20 publications**, though the registered EU product is now cancelled.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention and treatment of postoperative pain and inflammation associated with cataract surgery; reduction in the risk of postoperative macular oedema associated with cataract surgery in diabetic patients |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the drug record. From the published literature, nepafenac is a prodrug. Eye tissue enzymes convert it to amfenac, which inhibits COX-1 and COX-2. This lowers prostaglandin production, which in turn reduces ocular inflammation, pain, and breakdown of the blood-retinal barrier.

The predicted "eye disease" is very broad and mostly covers what the drug is already approved for. It is therefore closer to an extension of the approved use than true repurposing. Evidence for the more distinct retinal uses is smaller and less certain. These include epiretinal membrane surgery, diabetic macular oedema, retinal detachment surgery, and central serous chorioretinopathy. Studies show topical nepafenac and amfenac reach the back of the eye, which makes these uses plausible.

Other lower-ranked predictions in the model output are not supported by evidence:
- **Optic papillitis** (score 99.84%): Only a preclinical rabbit study of retinal oedema and one cataract trial are linked, and that trial does not study papillitis. The link looks like a mapping artefact. Evidence level L4, decision Hold.
- **Vitreous detachment** (score 99.81%): One Phase 4 biomarker trial (NCT07162818) in retinal detachment and proliferative vitreoretinopathy gives mechanistic but not clinical evidence. Evidence level L4, treated as a research question.
- **Hypotrichosis simplex of the scalp, seborrheic keratosis, von Hippel anomaly, congenital hypotrichosis milia, McPherson-Robertson-Cammarano syndrome, lagophthalmos, vulvar inverted follicular keratosis** (scores 99.80–99.84%): No trials or literature and no plausible mechanism. Evidence level L5, decision Hold.

## Clinical Trial Evidence

The table lists the 10 most relevant of the 43 trials linked to the top prediction, prioritising large, controlled studies of the labelled and retinal uses.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Nepafenac 0.3% for prevention and treatment of ocular inflammation and pain after cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Vehicle-controlled study of nepafenac 0.3% once daily in diabetic patients after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Same design as above, a parallel diabetic cataract-surgery study |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for inflammation and pain after cataract surgery |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Prevention of pseudophakic cystoid macular oedema with nepafenac 0.3% vs placebo |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Clinical equivalence of generic nepafenac 0.3% to Ilevro for pain and inflammation after cataract surgery |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | Nevanac 0.1% vs vehicle for reducing macular oedema after cataract surgery in diabetic retinopathy |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | Completed | 267 | Nevanac 0.1% vs Acular LS for ocular inflammation after cataract surgery |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | Completed | 227 | European study of nepafenac 0.1% vs ketorolac and placebo for inflammation and pain after cataract surgery |
| [NCT00900887](https://clinicaltrials.gov/study/NCT00900887) | Phase 2 | Completed | 84 | Topical nepafenac or ketorolac for central thickness after photocoagulation in diabetic macular oedema |

Other registered trials explore off-label retinal uses, for example epiretinal membrane surgery ([NCT07736690](https://clinicaltrials.gov/study/NCT07736690), n=60) and retinal detachment ([NCT07162818](https://clinicaltrials.gov/study/NCT07162818), n=61). These are small, and their results were not available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Systematic review / network meta-analysis | Eye (London) | Compared topical NSAIDs for macular oedema and visual outcome after phacoemulsification |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Systematic review | Cochrane Database Syst Rev | Topical NSAIDs for diabetic cystoid macular oedema |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | Nepafenac 0.1% vs prednisolone 1% for inflammation control after micro-incisional cataract surgery |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Nepafenac in cataract surgery: reduces inflammation, pain, and macular oedema risk, with high ocular penetration |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAIDs in the treatment of retinal diseases |
| [41039316](https://pubmed.ncbi.nlm.nih.gov/41039316/) | 2025 | Comparative study | BMC Ophthalmol | Analgesic efficacy of 7 topical NSAIDs for pain from panretinal photocoagulation |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Preclinical / PK | Exp Eye Res | Nepafenac and amfenac distribute to the posterior segment of the eye |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclinical | Diabetes | Topical nepafenac inhibited early diabetic retinal disease in rats |
| [12506103](https://pubmed.ncbi.nlm.nih.gov/12506103/) | 2003 | Preclinical | Invest Ophthalmol Vis Sci | Topical nepafenac inhibited ocular neovascularisation in mouse models |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | Case report | J Cataract Refract Surg | Corneal melt associated with nepafenac after cataract surgery |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000818 (cancelled) | Nevanac | Not stated | Prevention and treatment of postoperative pain and inflammation associated with cataract surgery; reduction in the risk of postoperative macular oedema associated with cataract su... |

## Safety Considerations

- **Disease associations flagged by the knowledge graph** (from a drug-disease contraindication network, not from label text): rheumatoid arthritis, diabetes mellitus, diabetic ketoacidosis, blood coagulation disease, keratitis, keratoconjunctivitis, dry eye syndrome, xerophthalmia, and corneal ulcer. These should be checked against the SmPC, as the diabetes flag sits alongside an approved use in diabetic patients.
- **Corneal safety**: A published case report describes corneal melt with nepafenac after cataract surgery in a patient with graft-versus-host disease. This is consistent with the known risk of corneal healing problems with topical NSAIDs, and it matters for ocular surface disease.

Please refer to the SmPC for the full warnings, contraindications, and drug interactions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials support nepafenac in postoperative ocular inflammation, pain, and macular oedema in diabetic patients. However, this evidence mainly covers the already approved use rather than a new indication. The EU authorization is cancelled, and evidence for broader retinal uses is small and exploratory. The other predicted indications lack evidence and should stay on Hold.

**To proceed, the following is needed:**
- Confirm current market availability in the EU, since the only registered authorization is cancelled
- Obtain and review the SmPC warnings and contraindications
- Obtain detailed mechanism-of-action data from DrugBank
- Review results from the trials in retinal surgery and diabetic macular oedema before pursuing those uses
- Define a corneal safety monitoring plan, especially for patients with ocular surface disease, diabetes, or rheumatoid arthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

