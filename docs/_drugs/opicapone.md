---
layout: default
title: Opicapone
parent: AI Predictions (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
---

# Opicapone
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

# Opicapone: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Opicapone is a peripheral COMT (catechol-O-methyltransferase) inhibitor, used as adjunctive therapy with levodopa in Parkinson's disease.
> The TxGNN model's top-ranked prediction is **Rasmussen Subacute Encephalitis**,
> but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as mechanistically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa/DOPA-decarboxylase inhibitor therapy) — inferred from mechanistic rationale text; not present as a structured field in this evidence pack |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 |
| EU/TW Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured `original_moa` field (flagged as a Blocking/High data gap). Based on information embedded in the model's own rationale text, Opicapone acts as a peripherally-restricted COMT inhibitor, reducing peripheral breakdown of levodopa to prolong central dopaminergic availability — its established role in Parkinson's disease motor fluctuation management.

For the top-ranked prediction, **this mechanistic link is explicitly weak**. Rasmussen subacute encephalitis is a T-cell mediated autoimmune/inflammatory cortical encephalitis in children, a pathology with no known connection to COMT enzyme activity or catecholamine metabolism. The rationale itself states that the high TxGNN score likely reflects **topological proximity of neurological-disease nodes in the knowledge graph, rather than genuine pharmacological plausibility** — there is no clinical or mechanistic support for this pairing.

Notably, several lower-ranked candidates in this evidence pack show stronger biological rationale — particularly **Lewy body dementia** (rank 7, synucleinopathy overlap with Parkinson's disease, flagged "Research Question") and **PLA2G6-associated neurodegeneration** (rank 3, parkinsonian phenotype overlap, flagged "Research Question"). These may be more productive directions than the top-scored candidate for further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA/EMA label warnings and contraindications are marked as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rasmussen subacute encephalitis) has no clinical or literature evidence, and the model's own mechanistic rationale explicitly disputes its pharmacological plausibility, attributing the high score to knowledge-graph topology rather than biology. This does not meet the bar to proceed.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/regulatory label — warnings, contraindications) — currently blocking any safety evaluation
- Resolve DG002 (confirmed mechanism of action from DrugBank or primary literature)
- Re-evaluate mechanistically stronger candidates from this same prediction set — particularly Lewy body dementia and PLA2G6-associated neurodegeneration — as alternative research questions
- If pursuing Rasmussen encephalitis specifically, obtain independent mechanistic or preclinical justification before any clinical consideration, given the model's own caveat about graph-topology bias
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

