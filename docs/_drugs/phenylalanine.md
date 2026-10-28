---
layout: default
title: Phenylalanine
parent: AI Predictions (L5)
nav_order: 484
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Phenylalanine: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Maple syrup urine disease (MSUD) presenting with an acute decompensat…"
monitor_inn: "phenylalanine"
predicted_indications: ["sclerosing cholangitis", "congenital prothrombin deficiency"]
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Phenylalanine: From Maple Syrup Urine Disease to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Phenylalanine (as the product Maapliv) was originally authorised in the EU for acute decompensation episodes of maple syrup urine disease (MSUD).
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are **0 clinical trials** and only **3 tangential publications**, none of which tests phenylalanine as a treatment.
This prediction is currently a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Maple syrup urine disease (MSUD) presenting with an acute decompensation episode, in patients from birth who are not eligible for an oral or enteral BCAA-free formulation |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenylalanine is an essential aromatic amino acid and a precursor of tyrosine and catecholamines. In Maapliv it is part of an amino acid formulation used for MSUD, a metabolic disorder of branched-chain amino acids.

The data compiled for this report do not establish a mechanistic link between phenylalanine and sclerosing cholangitis. The only related literature reports an association between plasma tyrosine (a phenylalanine metabolite) and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. That is an observation about a symptom, not evidence of a therapeutic effect. No plausible disease-modifying mechanism in cholestatic or fibrosing biliary disease is supported. The high TxGNN score (0.9943) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis.

A second prediction, congenital prothrombin deficiency (score 0.9926), has no trials or literature and no identifiable mechanism. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Relation between plasma tyrosine and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis; an association with a symptom, not a treatment effect |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort | J Clin Exp Hepatol | Serum metabolic signature of cholangiocarcinoma in a UK cohort; biomarker study, does not test phenylalanine as a treatment |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Other | J Gastroenterol Hepatol | Radioimmunoassay for a formylated chemotactic peptide (fMLP) showing enterohepatic circulation; unrelated to phenylalanine therapy |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005557 (cancelled) | Maapliv | Not specified | Maapliv is indicated for the treatment of maple syrup urine disease (MSUD) presenting with an acute decompensation episode in patients from birth who are not eligible for an oral and enteral branched-chain amino acids free (BCAA- free)... |

## Safety Considerations

Safety information from the product label was not available for this report; please refer to the SmPC.

- **Disease associations flagged in the knowledge graph (not label text)**: The TxGNN knowledge graph lists contraindication edges for phenylalanine with several conditions:
  - Phenylketonuria and other disorders of phenylalanine metabolism
  - Kidney disease, including chronic kidney disease, chronic renal failure and end-stage renal failure
  - Nephrolithiasis, nephrocalcinosis and acute urate nephropathy
  - Hypercalcaemia-related conditions, including sarcoidosis and humoral hypercalcaemia of malignancy
  - Phosphorus metabolism disease
  - Heart and cardiovascular disease, including ventricular fibrillation and digitalis poisoning
  - Pyoureter

These are computational associations and need verification against authoritative labelling.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no clinical trials, and the retrieved literature is tangential and does not test phenylalanine as a treatment. No mechanistic link is established, and the EU authorisation is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) and a plausible rationale for biliary disease
- Safety information from the SmPC, including the warnings and contraindications
- Preclinical or mechanistic studies of phenylalanine or its metabolites in cholestatic or fibrosing biliary disease
- Assessment of route and formulation compatibility, since the original product was an intravenous amino acid formulation for acute use
- Review of the knowledge-graph contraindication signals, especially for renal and cardiovascular patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

