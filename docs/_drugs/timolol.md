---
layout: default
title: Timolol
parent: Medium Evidence (L3-L4)
nav_order: 593
evidence_level: L4
indication_count: 10
---

# Timolol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Timolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Timolol is a non-selective beta-adrenergic receptor blocker classically used to lower intraocular pressure in glaucoma; however, this evidence pack does not contain a formal original-indication text, which is flagged as a data gap.
The TxGNN model's top-ranked prediction suggests potential effectiveness for **Primary Hereditary Glaucoma**,
but currently only **1 clinical trial** and **0 publications** are linked to this specific pairing — and even that single trial does not actually study this disease, making the supporting evidence weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — this dataset records 0 EU marketing authorizations for Timolol and no `original_indications` entries (data gap); classic clinical use is intraocular-pressure lowering in glaucoma |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L4 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Timolol is marked as a data gap in this evidence pack. Based on well-established pharmacology reconstructed from the evidence context, Timolol is a non-selective β-adrenergic receptor antagonist that blocks β receptors on the ciliary body epithelium, reducing aqueous humor production and lowering intraocular pressure — the classic mechanism underlying its long-standing use in glaucoma management.

"Primary hereditary glaucoma" typically refers to congenital/developmental glaucoma (e.g., due to *CYP1B1* mutations causing trabecular meshwork dysgenesis), a pathophysiologically distinct entity from typical adult open-angle glaucoma. While a reduction in aqueous humor production via β-blockade could theoretically be applicable to any glaucoma subtype regardless of etiology, the mechanistic link here is inferred by analogy rather than demonstrated directly.

Critically, the only clinical trial linked to this prediction (NCT02484716) does **not** study hereditary glaucoma at all — it investigates topical nasal timolol for epistaxis in Hereditary Hemorrhagic Telangiectasia (HHT), an unrelated vascular disorder. It appears to have been matched to this candidate purely through the shared keyword "hereditary." This substantially weakens confidence in the current evidence level and suggests the true evidentiary support is closer to a pure mechanistic hypothesis (L5) than the L4 rating implies. Separately, three other candidates in this same evidence pack — closed-angle glaucoma, open-angle glaucoma, and angle-closure glaucoma — carry much stronger Phase 3/4 RCT and meta-analysis support, but their rationale texts flag that these are very likely already-approved uses of ophthalmic Timolol rather than genuine new indications, reflecting a probable gap in the `original_indications` field rather than a true repurposing signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02484716](https://clinicaltrials.gov/study/NCT02484716) | Phase 2 | Completed | 58 | Evaluated timolol nasal spray for epistaxis in Hereditary Hemorrhagic Telangiectasia (HHT) — **not** a study of hereditary glaucoma; likely a keyword-matching false positive and does not constitute direct evidence for this indication |

## Literature Evidence

Currently no related literature available

## EU Market Information

Timolol currently has no EMA marketing authorization on record in this dataset (market status: **Not Marketed**; 0 licenses).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial associated with this top-ranked prediction does not actually study the predicted indication, and no supporting literature exists at all. Combined with the absence of an EU marketing authorization and blocking gaps in core safety data, this candidate does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- Resolve the blocking data gap on TFDA/EMA product-label warnings and contraindications (source: official regulatory label PDF)
- Resolve the mechanism-of-action data gap via DrugBank API query
- Identify clinical trials or literature that specifically study Timolol in congenital/hereditary (as opposed to adult acquired) glaucoma
- Clarify Timolol's actual approved indication set, since `original_indications` is empty in this dataset
- Cross-check this candidate against the other glaucoma-related predictions in the same evidence pack (closed-angle, open-angle, angle-closure glaucoma), which carry much stronger clinical evidence but likely represent existing approved uses rather than new repurposing opportunities — deduplication against known indications is recommended before further prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

