---
layout: default
title: Ranolazine
parent: AI Predictions (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Ranolazine
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

# Ranolazine: From Chronic Angina to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ranolazine is currently used as a second-line agent for chronic angina, acting through inhibition of the late/persistent cardiac sodium current (I_NaL). The TxGNN model's top-ranked prediction is **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this pairing currently has **zero clinical trials** and **zero publications**, and the model's own rationale states there is no known mechanistic link between the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic angina (per literature reference PMID 41293236; not yet confirmed via an official EU/Taiwan regulatory label — see Data Gaps below) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

A formal, sourced description of ranolazine's mechanism of action is not available in this evidence pack (`original_moa`: Data Gap). However, information embedded in the model's own rationale fields indicates ranolazine works by inhibiting the late cardiac sodium current (I_NaL), which reduces intracellular sodium/calcium overload in ischemic myocardium — the pharmacological basis for its established antianginal effect.

NSIAD, by contrast, is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), a renal water-handling pathway that is mechanistically unrelated to cardiac sodium channel modulation. The evidence pack's own repurposing rationale for this pairing is explicit: *"NSIAD is caused by AVPR2 gain-of-function mutations, with no known overlap with ranolazine's late cardiac sodium current inhibition mechanism; no reasonable biological connection."*

Given the complete absence of clinical trials, ICTRP registrations, or literature support, combined with this documented lack of mechanistic plausibility, the NSIAD prediction most likely reflects a knowledge-graph connectivity artifact rather than a genuine repurposing signal. Notably, of the 10 candidates in this evidence pack, **headache disorder (rank 9)** carries materially stronger support — three literature items, a plausible sodium-channel-related mechanism relevant to migraine, and evidence level L4 (decision stage S1, "Research Question") — and may be a more productive direction for further review, even though it is not the top-ranked TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Ranolazine currently holds **no EU marketing authorizations** on record in this evidence pack (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Supplementary note:* a real-world pharmacovigilance analysis of ranolazine using the FAERS database (PMID [41293236](https://pubmed.ncbi.nlm.nih.gov/41293236/), 2025) is available in the literature associated with a different candidate indication (headache disorder) in this pack, and may be a useful starting point once formal label data (warnings/contraindications) is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (NSIAD) has no supporting clinical or literature evidence, and its own documented mechanistic rationale confirms no plausible biological link to ranolazine's sodium-channel-based mode of action. Ranolazine also currently has no EU marketing authorization, adding a regulatory barrier on top of the scientific one.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Data Gap DG001, *Blocking* — required before any S1 safety review)
- Confirmed, sourced mechanism-of-action documentation (Data Gap DG002, *High*)
- If repurposing is still of interest, re-prioritize evaluation toward candidates with actual evidence, in particular **headache disorder** (L4, S1, three supporting literature items) rather than the top TxGNN-score pairing
- If NSIAD is to be pursued regardless, preclinical/mechanistic studies establishing a plausible pathway would be required before any clinical evidence search is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

