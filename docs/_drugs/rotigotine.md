---
layout: default
title: Rotigotine
parent: AI Predictions (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Parkinson's Disease/Restless Legs Syndrome to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Rotigotine is a dopamine receptor agonist known from the literature for treating Parkinson's disease and restless legs syndrome.
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> but currently **no clinical trials** and only **3 indirect publications** support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's Disease / Restless Legs Syndrome (inferred from literature evidence; no formal EU regulatory record in this evidence pack) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently unavailable (flagged as a High-severity data gap). Based on the literature evidence collected, Rotigotine is described as a non-ergot dopamine receptor "pan-agonist" — a 2023 structural biology study (PMID 37221270) resolved cryo-EM structures of all five human dopamine receptor subtypes (D1R–D5R) in complex with Rotigotine, confirming broad D1–D5 receptor engagement. Clinically, it is used for Parkinson's disease and restless legs syndrome (RLS), both conditions rooted in dopaminergic system dysfunction.

The link to ADHD is indirect but biologically plausible. ADHD pathophysiology is strongly associated with reduced striatal and prefrontal dopamine transmission (the "dopamine hypothesis"), and RLS has a well-documented clinical comorbidity with ADHD, particularly in children (PMID 21476956). A 2021 receptor-pharmacology study (PMID 34182128) further implicates dopamine D4 receptor polymorphisms and α2A-adrenoceptor heteromerization in ADHD susceptibility, providing a plausible receptor-level rationale for why a broad dopamine agonist like Rotigotine could theoretically modulate ADHD-relevant circuits.

However, none of the available literature reports direct study of Rotigotine in ADHD populations. The supporting evidence is limited to (1) RLS/ADHD comorbidity reviews and (2) general dopamine-receptor pharmacology unrelated to any Rotigotine-specific intervention. This is a mechanism-level hypothesis extrapolated from TxGNN's knowledge graph embedding, not a validated pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclinical/Receptor pharmacology | Pharmacological Research | D4 receptor heteromerization with α2A-adrenoceptors implicated in ADHD susceptibility; provides receptor-level rationale relevant to dopamine agonist mechanisms, but does not study Rotigotine directly |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current Pharmaceutical Design | Review of RLS in children, noting overlap with ADHD symptomatology and treatment considerations |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General review of restless-legs syndrome pathophysiology; does not address ADHD or Rotigotine specifically |

---

## EU Market Information

Rotigotine is currently **not marketed** in the EU according to this evidence pack (0 marketing authorizations on record). No authorization details are available for review.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence Level is L5 (model prediction only) with a decision stage of S0 — there are no clinical trials, and the 3 supporting publications are indirect (comorbidity reviews and general dopamine-receptor pharmacology), none of which studies Rotigotine in ADHD directly. In addition, a **Blocking**-severity data gap (missing TFDA/regulatory label warnings and contraindications) currently prevents even entering the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product label warnings/contraindications to enable S1 safety pre-screening
- Resolve DG002 (High): confirm mechanism of action via DrugBank API query
- Rotigotine-specific preclinical or pilot clinical data in ADHD populations (current evidence is class-level/mechanistic only)
- Confirmation of EU marketing authorization status, given 0 licenses are currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

