---
layout: default
title: Mirabegron
parent: AI Predictions (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Mirabegron
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

# Mirabegron: From Overactive Bladder (mechanism-inferred) to Thoracic Malformation

## One-Sentence Summary

Mirabegron is a β3-adrenergic receptor agonist that mechanistically acts on bladder detrusor muscle and brown adipose tissue; no confirmed original indication or EU marketing authorization is recorded in this evidence pack. The TxGNN model's top prediction is **Thoracic Malformation** (score 83.06%), but this is supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph co-occurrence artifact rather than a genuine drug–disease relationship.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in regulatory data (mechanistic notes indicate action on bladder detrusor muscle, consistent with β3-agonist class use in overactive bladder) |
| Predicted New Indication | Thoracic Malformation |
| TxGNN Prediction Score | 83.06% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (Not currently marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Mirabegron's original indication is not available in the evidence pack (flagged as a Data Gap, DG002, High severity). Based on the limited information present, Mirabegron is known as a β3-adrenergic receptor agonist acting primarily on bladder detrusor muscle and brown adipose tissue — consistent with the drug class typically used for overactive bladder, though this is not confirmed by any regulatory license text in this pack.

For the top-ranked prediction, thoracic malformation, the evidence pack's own mechanistic analysis explicitly concludes there is **no known receptor expression or signaling pathway link** between β3-adrenergic agonism and thoracic skeletal developmental abnormality. It classifies this association as a statistical artifact arising from knowledge-graph embedding proximity rather than a genuine mechanism-derived hypothesis.

Notably, several other candidates in the top-10 list (rank 3: polycystic kidney/liver disease; ranks 6–7: esophageal varices) show similarly weak or even **mechanistically contradictory** rationale — e.g., β3-agonism activates cAMP signaling, which runs counter to the cAMP-lowering strategy used therapeutically in polycystic kidney disease (tolvaptan), and is pharmacologically opposite to the non-selective β-blockade used in esophageal varices management. No candidate in this evidence pack currently has a mechanistically well-supported rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the SmPC for safety information.

**Note:** A Blocking-severity data gap (DG001) has been identified — TFDA/regulatory-equivalent warnings and contraindications for Mirabegron are not available, which prevents this candidate from entering the S1 safety pre-screening stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (thoracic malformation) is an L5, model-only association with no clinical trial or literature support, and the evidence pack's own mechanistic review identifies it as a likely spurious knowledge-graph correlation rather than a biologically plausible signal. Combined with a Blocking-severity safety data gap and the absence of confirmed EU marketing status, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/EMA-equivalent SmPC warnings and contraindications (resolves DG001, Blocking)
- Confirmed original indication and mechanism of action data (resolves DG002, High)
- Independent preclinical or mechanistic evidence linking β3-adrenergic agonism to thoracic malformation before this candidate can move beyond S0
- If pursuing alternative candidates from this pack (e.g., rank 3, polycystic kidney/liver disease), a pharmacological reassessment is needed given the cAMP-pathway directionality conflict noted in the rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

