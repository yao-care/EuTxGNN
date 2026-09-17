---
layout: default
title: Idursulfase
parent: AI Predictions (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Idursulfase
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

# Idursulfase: From Hunter Syndrome (MPS II) to Ptosis-Strabismus-Ectopic Pupils Syndrome

## One-Sentence Summary

Idursulfase is a recombinant enzyme replacement therapy used for Hunter syndrome (Mucopolysaccharidosis II, MPS II). The TxGNN model predicts it may be effective for **ptosis-strabismus-ectopic pupils syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hunter syndrome (Mucopolysaccharidosis II, MPS II) |
| Predicted New Indication | Ptosis-strabismus-ectopic pupils syndrome |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Idursulfase is flagged as a data gap in the evidence pack. However, the pack's own rationale notes indicate Idursulfase is a recombinant form of iduronate-2-sulfatase (IDS), used as enzyme replacement therapy for Hunter syndrome (MPS II) — a lysosomal storage disorder caused by IDS gene deficiency that leads to glycosaminoglycan (GAG) accumulation.

Ptosis-strabismus-ectopic pupils syndrome is a congenital craniofacial/extraocular muscle developmental disorder. The evidence pack explicitly states there is **no known mechanistic connection** between this syndrome and GAG metabolism or lysosomal storage — the pathology is structural/developmental, not a substrate-accumulation disease that IDS enzyme replacement would address. This top-ranked prediction is therefore flagged by the source data itself as lacking mechanistic basis, and no supporting trials or literature were found.

Notably, among all 10 predicted indications in this pack, only rank 10 (Scheie syndrome, TxGNN score 94.79%, lower than the top prediction) has any literature evidence (7 publications). Even there, the evidence pack raises an explicit mechanism-mismatch warning: Scheie syndrome is a subtype of MPS **I** (alpha-L-iduronidase/IDUA gene deficiency, treated with laronidase), not MPS II (IDS gene deficiency, treated with Idursulfase). The apparent TxGNN signal likely reflects knowledge-graph clustering by the shared "mucopolysaccharidosis" disease category rather than a true enzyme-substrate match.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Idursulfase is currently **not marketed** in the target region, with 0 authorizations on record.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no supporting clinical trial or literature evidence, and the evidence pack itself states there is no plausible mechanistic basis. The only candidate in this set with literature support (Scheie syndrome) carries an explicit enzyme/gene-target mismatch warning, so overall evidentiary support for repurposing is currently absent.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (DG001, currently blocking S1 safety review)
- Confirmed original mechanism-of-action documentation via DrugBank API (DG002)
- A mechanistically grounded candidate indication (e.g., one tied to GAG/lysosomal storage pathology) before advancing past S0
- If the Scheie syndrome direction is pursued, clarification of the IDUA vs. IDS enzyme-target discrepancy before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

