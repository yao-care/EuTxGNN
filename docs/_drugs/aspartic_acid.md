---
layout: default
title: Aspartic Acid
parent: AI Predictions (L5)
nav_order: 65
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Aspartic Acid: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Treatment of maple syrup urine disease (MSUD) presenting with an acut…"
monitor_inn: "aspartic acid"
predicted_indications: ["renal tubular acidosis"]
---

# Aspartic Acid
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

## Aspartic Acid: From Maple Syrup Urine Disease to Renal Tubular Acidosis
{: .text-alpha }

## One-Sentence Summary

Aspartic acid (marketed as Maapliv) is an amino acid formulation originally authorised in the EU for acute decompensation episodes of maple syrup urine disease (MSUD) in patients who cannot take an oral or enteral BCAA-free formulation.
The TxGNN model predicts it may be effective for **renal tubular acidosis**, but there are **0 clinical trials** and only **4 loosely related publications** (none showing a treatment effect), so this remains a **model-only prediction**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of maple syrup urine disease (MSUD) presenting with an acute decompensation episode in patients from birth who are not eligible for an oral and enteral BCAA-free formulation |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Aspartic acid is a non-essential amino acid involved in the urea cycle, transamination, and renal ammoniagenesis. In its original use, it was part of an amino acid parenteral nutrition product for acute MSUD decompensation.

The only conceivable link to renal tubular acidosis (RTA) is theoretical: aspartate metabolism contributes to ammonia production and acid-base handling in the kidney. RTA, however, results from defective hydrogen ion secretion or bicarbonate reabsorption in the tubules, for example from SLC4A1 anion-exchanger mutations in distal RTA. There is no evidence that supplementing aspartic acid corrects these transport defects.

The link is therefore weak and indirect. The very high TxGNN score reflects a model-based association, not clinical proof. Because aspartic acid is itself an acidic amino acid, supplementation could in theory add to the acid load rather than relieve it. The original indication (MSUD) is also unrelated to RTA.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Case report | J Inherit Metab Dis | Neonate with pyruvate carboxylase deficiency, proximal RTA and cystinuria; the patient began to thrive when the diet was supplemented with aspartic acid, asparagine and other amino acids (the only item that mentions aspartic acid) |
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Genetic diagnostic study | J Pediatr (Rio J) | Whole-exome sequencing used to establish the genetic diagnosis of distal RTA in four children; no treatment data |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Genetic case series | Nephron Physiol | Distal RTA in Filipino children caused by SLC4A1 (AE1/Band 3) mutations; describes clinical and genetic features |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | Basic physiology | Am J Physiol | Relationship between tubular cell pNH3 and renal ammonia production; background physiology only |

None of these publications is a controlled study of aspartic acid in RTA.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005557 (cancelled) | Maapliv | Not specified | Maapliv is indicated for the treatment of maple syrup urine disease (MSUD) presenting with an acute decompensation episode in patients from birth who are not eligible for an oral and enteral branched-chain amino acids free (BCAA- free) formulation. |

---

## Safety Considerations

- **Disease associations flagged by the knowledge graph (not label text):** The TxGNN knowledge graph lists contraindication links with kidney disease, pyoureter, diarrheal disease, chronic diarrheal disease, atrioventricular block, hyperkalemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita and gastroparesis. These come from model data rather than product labelling and should be verified. The link with kidney disease is particularly relevant to a renal indication.
- **Acid load:** Aspartic acid is an acidic amino acid, so supplementation could theoretically worsen acid-base balance in patients with RTA.

No drug interaction data were found. For authoritative warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (Evidence Level L5). Knowledge-graph contraindication signals involving kidney disease add further caution.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to test whether any plausible pathway links aspartic acid to tubular acid-base handling
- Package insert warnings and contraindications from the EMA SmPC, which are required before any safety screening
- Preclinical or mechanistic studies showing an effect of aspartate on bicarbonate reabsorption or H+ secretion in RTA models
- Clarification of whether acid-load effects make aspartic acid unsuitable in RTA
- Review of the reasons for the cancellation of the marketing authorisation, and assessment of route and formulation compatibility with the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

