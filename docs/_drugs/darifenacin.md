---
layout: default
title: Darifenacin
parent: AI Predictions (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Darifenacin: predicted new indication Polycystic kidney disease 3 with or without polycystic liver disease (evidence level L5). Approved use: Symptomatic treatment of urge incontinence and/or increas…"
monitor_inn: "Darifenacin"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "thoracic malformation", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "low compliance bladder", "adult familial nephronophthisis-spastic quadriparesia syndrome", "karyomegalic interstitial nephritis", "polycystic kidney disease", "primary hereditary glaucoma", "respiratory failure"]
---

# Darifenacin
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

## Darifenacin: From Overactive Bladder to Polycystic Kidney Disease 3 (With or Without Polycystic Liver Disease)
{: .text-alpha }

## One-Sentence Summary

Darifenacin is a selective muscarinic antagonist originally used for the symptomatic treatment of urge incontinence, urinary frequency and urgency in adults with overactive bladder syndrome.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.
Among the other predicted indications, only "low compliance bladder" has indirect literature support (4 publications on antimuscarinic therapy and overactive bladder).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of urge incontinence and/or increased urinary frequency and urgency as may occur in adult patients with overactive bladder syndrome |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 96.93% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Darifenacin is known as a selective M3 muscarinic receptor antagonist. Its efficacy in overactive bladder comes from reducing detrusor muscle contraction.

For polycystic kidney disease 3, no mechanistic link is established. Cyst formation and growth involve pathways such as cAMP signalling and genetic defects in cyst-related proteins, and nothing in the compiled data connects M3 antagonism to them. The high TxGNN score (96.93%) reflects a knowledge-graph association only. Other top-ranked predictions (thoracic malformation, renal-hepatic-pancreatic dysplasia, Joubert syndrome with renal defect, nephronophthisis-related syndromes, karyomegalic interstitial nephritis) are developmental or genetic ciliopathy-type conditions with the same lack of plausible mechanism.

By contrast, **low compliance bladder** (rank 5, score 95.69%) is biologically plausible. It is closely related to the original indication, since M3 receptors mediate detrusor contraction. However, the available literature is general antimuscarinic and overactive bladder pharmacology, so the evidence is indirect (Evidence Level L4, flagged as a research question).

The prediction for **primary hereditary glaucoma** (rank 9) points to a potential safety concern rather than a benefit, because antimuscarinics can precipitate angle-closure glaucoma.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction (polycystic kidney disease 3). The table below lists the indirect literature found for the related prediction, low compliance bladder.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24140548](https://pubmed.ncbi.nlm.nih.gov/24140548/) | 2014 | Systematic Review | The Journal of Urology | Long-term adherence to antimuscarinic therapy in everyday practice; side effects contribute to poor adherence and persistence |
| [16465186](https://pubmed.ncbi.nlm.nih.gov/16465186/) | 2006 | Review | British Journal of Pharmacology | Antimuscarinics are the cornerstone of overactive bladder management, acting mainly through M2/M3 receptors in the detrusor |
| [17594185](https://pubmed.ncbi.nlm.nih.gov/17594185/) | 2007 | Review | Expert Opinion on Investigational Drugs | Overview of overactive bladder and treatments in early phase clinical trials |
| [37604331](https://pubmed.ncbi.nlm.nih.gov/37604331/) | 2024 | Preclinical (multi-omics) | Journal of Ethnopharmacology | Therapeutic mechanisms of a traditional Chinese prescription (Suo-Quan-Wan) for overactive bladder in rats; not about darifenacin |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000554 (cancelled) | Emselex | Not specified | Symptomatic treatment of urge incontinence and/or increased urinary frequency and urgency as may occur in adult patients with overactive bladder syndrome. |

## Safety Considerations

**Contraindication-related diseases (from knowledge-graph drug-disease edges, not label text):** liver failure, liver disease, gallbladder disease, angioedema (including acquired, hereditary, and RAAS-blocker-induced forms), angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, ulcerative colitis and inflammatory bowel disease, and bladder neck obstruction.

**Drug Interactions:** 100 interactions were identified in total. Examples from the first 20 reviewed:
- **Major:** potassium citrate, eliglustat
- **Moderate:** other anticholinergics and antimuscarinics (hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine), CNS or opioid-related drugs (morphine, loperamide, eluxadoline), CYP-related interactors (bupropion, cimetidine, clarithromycin, clotrimazole, aprepitant), and others (dexamethasone, lorcaserin, fenfluramine, dexfenfluramine, glycerol phenylbutyrate)

Please also refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (polycystic kidney disease 3) is based on a graph model score alone, with no clinical trials, no literature, and no plausible mechanistic link. Darifenacin's EU authorization is also cancelled, and several knowledge-graph contraindications (e.g., liver disease) overlap with organ systems affected in the predicted disease.

**To proceed, the following is needed:**
- Mechanism of action data for darifenacin, and an evaluation of any link to cyst-related pathways
- Preclinical evidence in polycystic kidney disease models
- The EMA label warnings and contraindications (blocking gap for safety screening)
- If a bladder-related direction is preferred, a targeted evaluation of **low compliance bladder**, which has the most plausible rationale but only indirect evidence
- Clarification of regulatory status, since the EU authorization is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

