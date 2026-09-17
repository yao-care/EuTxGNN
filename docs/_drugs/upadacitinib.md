---
layout: default
title: Upadacitinib
parent: AI Predictions (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
---

# Upadacitinib
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

# Upadacitinib: From Immune-Mediated Inflammatory Disease to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Upadacitinib is a selective JAK1 inhibitor that acts through immunomodulatory and anti-inflammatory pathways; its specific approved indication is not recorded in the current dataset. The TxGNN model's top-ranked prediction links it to **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, a rare congenital developmental disorder, but this pairing is supported by **no clinical trials** and **no published literature**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph noise signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in current dataset (Upadacitinib is a selective JAK1 inhibitor used for immune-mediated inflammatory conditions) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Upadacitinib is not available in this evidence pack (flagged as a High-severity data gap, DG002, pending a DrugBank API lookup). Based on information embedded in the prediction rationale itself, Upadacitinib is described as a selective JAK1 inhibitor whose therapeutic effect operates through immunomodulatory and anti-inflammatory signaling pathways.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare congenital malformation syndrome affecting eye and skeletal development. It is a structural developmental disorder rather than an immune- or inflammation-driven condition, so there is no established disease-mechanism overlap with JAK1 inhibition.

The pack's own rationale explicitly characterizes this pairing as a probable knowledge-graph noise association: TxGNN assigned it the highest raw prediction score (99.61%) among the ten candidates evaluated, yet the accompanying biological review found no reasonable link between JAK1-mediated immune modulation and a congenital structural defect. For context, other candidates further down the ranked list — plasma cell myeloma (ranks 3 and 7) and amyotrophic lateral sclerosis (rank 9) — carry more plausible mechanistic hypotheses (IL-6/JAK/STAT3 signaling in myeloma progression; JAK-STAT-driven neuroinflammation in ALS) and were classified as "Research Question" rather than "Hold," although they too currently lack any clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorizations are currently recorded for Upadacitinib in this dataset (0 authorizations; market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN assigns a high raw score to this pairing, but there is no clinical trial or literature evidence, and the accompanying mechanistic review concludes the association is likely a knowledge-graph noise signal with no biological plausibility linking JAK1 inhibition to a congenital structural malformation syndrome.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/EMA label warnings and contraindications) and DG002 (confirmed mechanism of action via DrugBank API) before any safety evaluation (S1) can begin
- Confirmed original indication and EU marketing authorization data for Upadacitinib
- If further repurposing research is pursued, prioritize the mechanistically more plausible "Research Question" candidates in this pack (plasma cell myeloma, amyotrophic lateral sclerosis) over this top-ranked but biologically implausible pairing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

