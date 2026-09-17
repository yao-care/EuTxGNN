---
layout: default
title: Evinacumab
parent: AI Predictions (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Evinacumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Evinacumab: From Unspecified Original Indication to Diabetic Cataract

## One-Sentence Summary

> Evinacumab (DrugBank ID: DB15354) is an ANGPTL3-targeting monoclonal antibody; its original approved indication is not recorded in this evidence pack, and the drug currently has **no EU marketing authorization** on file.
> The TxGNN model's top prediction is **Diabetic Cataract**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a likely false positive.
> A lower-ranked candidate in the same pack — **Diabetic Retinopathy** — has a 2026 mechanistic publication linking ANGPTL3 to retinal vascular leakage, making it a more credible research lead than the top-ranked prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (original_indications and original_moa are unrecorded) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Evinacumab and its original approved indication were not available in this evidence pack. Based on information present elsewhere in the pack (the rationale for the diabetic retinopathy candidate), Evinacumab is an **ANGPTL3 (Angiopoietin-like protein 3) monoclonal antibody**, a class of drug that primarily modulates lipoprotein metabolism.

For the top-ranked prediction, **diabetic cataract**, the model's own repurposing rationale explicitly states there is **no known direct mechanistic link** between ANGPTL3 inhibition and the lens osmotic/glycation pathology underlying diabetic cataract. It further notes that ranks 1–9 in this candidate set are all cataract subtypes clustered at nearly identical scores (0.984–0.985), which is characteristic of a **knowledge-graph node-clustering artifact** rather than a genuine biological signal — i.e., a suspected model false positive.

By contrast, rank 10 in the same pack, **diabetic retinopathy**, is supported by a 2026 mechanistic publication showing an ANGPTL3–integrin α5 axis drives retinal vascular leakage in diabetic retinopathy — a biologically plausible link to ANGPTL3 inhibition, though still preclinical/mechanistic (L4) with no clinical trial or case evidence yet. This candidate warrants more attention than the nominal top-ranked cataract prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: the pack does contain one relevant publication, but it supports the rank-10 candidate, diabetic retinopathy, not the top-ranked diabetic cataract prediction: [41555340](https://pubmed.ncbi.nlm.nih.gov/41555340/), 2026, Mechanistic/Preclinical, *Journal of Translational Medicine* — "The ANGPTL3–integrin α5 axis drives retinal vascular leakage in diabetic retinopathy.")*

---

## EU Market Information

Evinacumab currently has no EU marketing authorization on record (total_licenses = 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (diabetic cataract) has no clinical trial or literature support, and the evidence pack itself flags it as a likely knowledge-graph clustering artifact rather than a genuine mechanistic signal. There is insufficient basis to advance this specific candidate.

**To proceed, the following is needed:**
- Basic drug-level data currently missing: original approved indication, mechanism of action, and TFDA/EMA label warnings and contraindications (flagged as Blocking in this pack's data gaps)
- If pursuing an ophthalmic angle, redirect attention to the mechanistically-supported **diabetic retinopathy** candidate (rank 10, L4, decision stage S1) rather than the top-ranked cataract prediction, and monitor for follow-up preclinical or clinical studies on the ANGPTL3–integrin α5 axis
- DDI and contraindication data (currently not_found) before any safety-related (S1) evaluation can proceed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

