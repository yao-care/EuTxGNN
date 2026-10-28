---
layout: default
title: Rivastigmine
parent: AI Predictions (L5)
nav_order: 533
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Rivastigmine: predicted new indication Glaucoma (evidence level L4). Approved use: Symptomatic treatment of mild to moderately severe Alzheimer's dement…"
monitor_inn: "Rivastigmine"
predicted_indications: ["glaucoma"]
---

# Rivastigmine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Rivastigmine: From Alzheimer's Dementia to Glaucoma
{: .text-alpha }

## One-Sentence Summary

Rivastigmine is a cholinesterase inhibitor originally used for the symptomatic treatment of mild to moderately severe Alzheimer's dementia and Parkinson's disease dementia.
The TxGNN model predicts it may be effective for **glaucoma**, but there are currently **no registered clinical trials** for this use. Support comes from **3 publications**, only one of which is original preclinical work (a rabbit study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of mild to moderately severe Alzheimer's dementia; symptomatic treatment of mild to moderately severe dementia in patients with idiopathic Parkinson's disease |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 0.9927 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 6 of 6) |
| Number of Authorizations | 6 (valid: 6) |
| Recommended Decision | Hold (treated as a research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Rivastigmine is known to be a cholinesterase inhibitor: it slows the breakdown of acetylcholine, the neurotransmitter that is depleted in Alzheimer's disease.

The link to glaucoma runs through the eye's cholinergic system. Higher acetylcholine levels in the eye can strengthen ciliary muscle contraction and improve outflow through the trabecular meshwork. This lowers intraocular pressure (IOP), the main treatable risk factor in glaucoma. Miotic cholinergic agents such as pilocarpine work in a similar way. A 2000 rabbit study reported that topical rivastigmine lowered IOP in normotensive animals, and a 2024 review of cholinergic agents for IOP reduction supports the rationale.

This evidence is preclinical and indirect. No human data exist, and the ocular safety and tolerability of topical or systemic rivastigmine in glaucoma patients have not been established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical (animal study) | J Ocul Pharmacol Ther | Topical rivastigmine, a selective acetylcholinesterase inhibitor, lowered intraocular pressure in rabbits |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review | Front Mol Biosci | Systems genetics, molecular modeling and in vivo perspectives on cholinergic agents for IOP reduction; systemic cholinergic adverse effects limit current approved agonists |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review (patent literature) | Expert Opin Ther Pat | Update on acetylcholinesterase inhibitors and reactivators; mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis and glaucoma |

## EU Market Information

Rivastigmine is marketed in this country, with 6 valid licences out of 6. Dosage form is not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000169 | Exelon | Not available | Symptomatic treatment of mild to moderately severe Alzheimer's dementia. Symptomatic treatment of mild to moderately sev... |
| EMEA/H/C/000255 | Prometax | Not available | Symptomatic treatment of mild to moderately severe Alzheimer's dementia. Symptomatic treatment of mild to moderately sev... |
| EMEA/H/C/001029 | Nimvastid | Not available | Symptomatic treatment of mild to moderately severe Alzheimer's dementia. Symptomatic treatment of mild to moderately sev... |
| EMEA/H/C/001181 | Rivastigmine 1 A Pharma | Not available | Symptomatic treatment of mild to moderately severe Alzheimer's dementia. Symptomatic treatment of mild to moderately sev... |
| EMEA/H/C/001182 | Rivastigmine Hexal | Not available | Symptomatic treatment of mild to moderately severe Alzheimer's dementia. Symptomatic treatment of mild to moderately sev... |

(A sixth cancelled authorization, Rivastigmine Sandoz, EMEA/H/C/001183, carries the same indication.)

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** The TxGNN knowledge graph links rivastigmine to contraindications in several conditions. These include:
  - Cardiac: sick sinus syndrome, atrioventricular block, heart conduction disease, sudden cardiac arrest.
  - Respiratory: asthma and chronic obstructive pulmonary disease.
  - Gastrointestinal: active peptic ulcer disease and diarrheal disease.
  - Neurological: epilepsy, parkinsonian disorder and Parkinson disease, basal ganglia disease, focal hand dystonia and blepharospasm.
  - Other: urinary tract obstruction and anorexia nervosa.
- **Drug Interactions:** 100 interactions were recorded. The most notable is **bupropion (Major)**. Moderate interactions include:
  - Anticholinergics and antispasmodics: atropine, hyoscyamine, glycopyrronium, dicyclomine, clidinium, trospium, mepenzolate.
  - Acid suppressants: famotidine, ranitidine, cimetidine.
  - Antibiotics: clarithromycin, levofloxacin, metronidazole.
  - Antiemetics: dolasetron, palonosetron.
  - Bowel-cleansing agents and others: loperamide, picosulfuric acid, polyethylene glycol, sodium sulfate.

Please refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
The glaucoma prediction has a plausible mechanism and one animal study showing IOP reduction. However, there are no human trials, and the evidence level is L4. The drug is marketed in this country with 6 valid licences out of 6, and the knowledge graph flags several relevant contraindications, especially cardiac conduction and respiratory disease, which are common in older glaucoma patients.

**To proceed, the following is needed:**
- Mechanism of action data and the SmPC warnings and contraindications (currently missing)
- Confirmation of the pharmacology and efficacy in human or additional preclinical models, including dose-response
- A topical ophthalmic formulation and its local and systemic tolerability, including ocular safety
- A plan for managing the cardiac, respiratory and gastrointestinal risks and the interaction with bupropion
- Clarification of why the EU authorizations were cancelled, and of the regulatory pathway for any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

