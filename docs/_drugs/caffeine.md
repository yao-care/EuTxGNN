---
layout: default
title: Caffeine
parent: AI Predictions (L5)
nav_order: 120
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Caffeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Treatment of primary apnoea of premature newborns"
monitor_inn: "Caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Caffeine: From Primary Apnoea of Premature Newborns to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Caffeine was originally authorised in the EU to treat primary apnoea of premature newborns.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this rests mainly on the model score:
there are **no registered clinical trials** and only **3 publications**, none of which show that caffeine treats nasal disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of primary apnoea of premature newborns |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Caffeine is known as an adenosine receptor antagonist and a non-selective phosphodiesterase inhibitor, and its efficacy in apnoea of prematurity has been established through its EU authorisations. Whether this mechanism applies to nasal cavity disease is unclear.

The available literature offers only indirect links. A review describes bitter taste receptors (TAS2Rs) in human airway tissue, including the nasal cavity, which may influence innate defence and ciliary function (PMID 26272040). Caffeine is a bitter-taste-receptor ligand, but the review does not show a therapeutic effect in nasal disease. A nasal caffeine gel was studied for cognition after sleep deprivation (PMID 35579146); this concerns a delivery route, not treatment of a nasal condition. An animal study of black tea and caffeine in lung carcinogenesis (PMID 9751618) is not relevant to this indication.

The relationship between neonatal apnoea and nasal cavity disease is therefore weak, and the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in human airways, including the nasal cavity; their pharmacology and role in airway defence are discussed |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preclinical formulation study | Current Drug Delivery | Nasal thermo-sensitive caffeine in situ gel for cognition after sleep deprivation (not a nasal disease treatment) |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine reduced NNK-induced lung tumours in rats (not relevant to nasal disease) |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001014 | Peyona (previously Nymusa) | Not specified | Treatment of primary apnoea of premature newborns. (valid) |
| EMEA/H/C/005435 | Gencebok | Not specified | Treatment of primary apnoea of premature newborns. (valid) |

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links caffeine to contraindications in the following conditions:
  - Cardiovascular: hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, long QT syndrome (including familial form)
  - Neurological and psychiatric: epilepsy, insomnia, anxiety disorder, neurotic disorder, dysthymic disorder
  - Respiratory: chronic obstructive pulmonary disease
  - Gastrointestinal, hepatic and pancreatic: gastric ulcer, peptic ulcer disease, inflammatory bowel disease, liver failure, liver disease, gallbladder disease, pancreatitis
  - Renal and urinary: kidney disease, pyoureter
  - Haematological and metabolic: thrombocytopenia, inherited porphyria (porphyria, porphyrin metabolism disease), hypothyroidism (myxedema, congenital hypothyroidism)

  These come from graph edges and should be verified against the product label.
- **Drug Interactions**: 75 interactions were recorded. Major-level interactions include **cocaine (nasal)** and **cocaine (topical)**. Moderate-level interactions include alosetron, obeticholic acid, adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole and duloxetine. Minor-level interactions include acetylsalicylic acid, cimetidine, atazanavir and disulfiram.

Label-based warnings and contraindications were not available; please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (L5). There are no clinical trials, and the literature does not show a therapeutic effect in nasal cavity disease. In addition, all EU authorisations for caffeine in this dataset are cancelled, and label safety data were not available.

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale linking caffeine to nasal cavity disease
- Label warnings and contraindications from the SmPC
- Preclinical or early clinical evidence in a defined nasal condition (for example, allergic or inflammatory rhinitis)
- Assessment of route and formulation, since the cancelled products' dosage forms are not recorded
- Review of the cardiovascular, neurological and interaction risks, particularly with nasal cocaine

### Other Predicted Indications Reviewed (for reference)

Of the other predicted indications, **hypnic headache** has the most support: reviews describe caffeine as a first-line option, but there are no controlled trials (L4). **Neuralgia** and **trigeminal autonomic cephalalgia** are L4, with preclinical or indirect evidence only. The remaining indications (thrombotic disease, vein disease, acute laryngopharyngitis, papillary conjunctivitis, glossodynia, coccygodynia) have little or no supporting evidence and are best held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

