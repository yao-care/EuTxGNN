---
layout: default
title: Travoprost
parent: AI Predictions (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Open-Angle Glaucoma / Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a topical prostaglandin F2α analogue used to lower intraocular pressure in patients with open-angle glaucoma and ocular hypertension. The TxGNN model's top prediction for this drug is efficacy in **Visceral Calciphylaxis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own analysis flags the underlying score as likely inflated rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / ocular hypertension (topical IOP-lowering therapy) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record for Travoprost is not available (flagged as a High-severity data gap). Based on information embedded in the clinical trial records in this evidence pack, Travoprost is known to act as a prostaglandin F2α receptor agonist administered as an eye drop; it lowers intraocular pressure by increasing uveoscleral outflow, and its systemic bioavailability is very low because the drug is rapidly metabolized locally at the cornea/ocular surface.

Visceral calciphylaxis is a systemic vascular calcification disorder, most commonly associated with chronic kidney disease, secondary hyperparathyroidism, and microvascular thrombosis affecting visceral organs. This is mechanistically and anatomically distant from a topical ocular hypotensive agent, and the evidence pack's own rationale for this candidate explicitly states that no known mechanistic pathway links PGF2α receptor stimulation at the eye to visceral vascular calcification.

It is also worth noting that this candidate sits within a cluster of near-identical top scores (0.999997–0.999998) spanning ranks 1–16 for this drug, several of which are anatomically/mechanistically implausible (e.g., thoracic outlet syndrome subtypes, idiopathic coronary artery dissection, lymphangiectasis) and have zero supporting trials or literature. Even the one candidate in this list with substantial trial and publication volume — "vascular disease" (rank 5, 15 trials, 20 publications) — was, on inspection, found to consist almost entirely of recycled evidence from Travoprost's already-approved glaucoma indication rather than genuine new mechanistic support. This pattern is consistent with score saturation in the model's embedding space rather than a disease-specific biological signal, and further lowers confidence in the visceral calciphylaxis prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations are recorded for Travoprost in this database (market status: Not marketed; total authorizations: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials or published literature supporting Travoprost's use in visceral calciphylaxis, no plausible pharmacological mechanism connects a topical ocular PGF2α agonist to systemic vascular calcification, and the prediction score itself shows signs of saturation shared with other implausible candidates for this drug.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (currently a Blocking data gap preventing entry into S1 safety pre-assessment)
- A confirmed, structured mechanism-of-action record for Travoprost (High-severity data gap)
- Preclinical or mechanistic studies establishing any biological rationale linking prostaglandin receptor signaling to vascular/visceral calcification
- If this candidate is still pursued despite the above, dedicated exploratory studies given the complete absence of existing trial or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

