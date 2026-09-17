---
layout: default
title: Vestronidase Alfa
parent: AI Predictions (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
---

# Vestronidase Alfa
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

# Vestronidase Alfa: From Mucopolysaccharidosis VII (Sly Syndrome) to Scheie Syndrome

## One-Sentence Summary

> Vestronidase alfa is a recombinant human β-glucuronidase (rhGUS) enzyme replacement therapy, originally developed for Mucopolysaccharidosis type VII (MPS VII, Sly syndrome).
> The TxGNN model predicts it may be effective for **Scheie syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags a likely enzyme-target mismatch rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis VII (Sly Syndrome) — derived from supporting literature, not from a formal Taiwan/EU label record |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action (MOA) record is not available in this Evidence Pack (flagged as a High-severity data gap). However, the supporting literature consistently describes vestronidase alfa as a recombinant human β-glucuronidase (rhGUS) enzyme replacement therapy, approved in the US and EU for MPS VII, where deficiency of the GUS enzyme leads to accumulation of glycosaminoglycans (GAGs) in lysosomes.

Scheie syndrome, however, is classified as MPS I — a distinct mucopolysaccharidosis subtype caused by deficiency of α-L-iduronidase (IDUA), a different enzyme entirely from GUS. Because the two diseases require replacement of different enzymes, there is no established biological pathway by which vestronidase alfa's mechanism would translate to Scheie syndrome.

The evidence pack's own rationale explicitly notes that this prediction likely reflects a knowledge-graph embedding artifact: Scheie syndrome and MPS VII cluster together in the "MPS / lysosomal storage disease" disease family, which can generate high similarity scores without a true shared mechanism. In short, this appears to be a case where TxGNN's disease-similarity signal is not backed by pharmacological plausibility, and the associated evidence level (L5, no supporting trials or literature) is consistent with that assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Vestronidase alfa is currently not marketed in the EU (0 marketing authorizations on record in this Evidence Pack), so no authorization table is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Scheie syndrome, MPS I / IDUA deficiency) does not match vestronidase alfa's known mechanism (GUS enzyme replacement for MPS VII), and there is no clinical trial or literature evidence to support this specific pairing. The evidence pack's own mechanistic review assesses this as a likely knowledge-graph clustering artifact rather than a genuine repurposing hypothesis.

**To proceed, the following is needed:**
- Resolution of the Blocking data gap: TFDA/EU label warnings and contraindications (DG001), required before any safety pre-screening (S1) can begin
- Resolution of the High-severity data gap: formal MOA documentation (DG002), to confirm or rule out any indirect enzymatic/pathway overlap between GUS and IDUA-related disease biology
- Independent biological/genetic validation confirming any shared pathway between MPS VII and MPS I (Scheie syndrome) before further investment
- Given the mechanistic mismatch, deprioritize this candidate in favor of higher-ranked signals in the same disease cluster (e.g., rank 2, "lysosomal storage disease with skeletal involvement," which may simply be an on-label MPS VII restatement and warrants label clarification rather than new-indication validation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

