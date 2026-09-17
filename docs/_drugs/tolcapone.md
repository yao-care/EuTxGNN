---
layout: default
title: Tolcapone
parent: AI Predictions (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Tolcapone is a COMT (catechol-O-methyltransferase) inhibitor originally developed as an adjunct therapy for Parkinson's disease, used to prolong the effect of levodopa. The TxGNN model's top-ranked prediction is **Rasmussen subacute encephalitis**, but this candidate is supported by **no clinical trials**, **no published literature**, and — critically — the model's own rationale states there is **no known pathophysiological connection** between the two conditions. This is a pure knowledge-graph embedding signal, not a mechanistically or clinically supported hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) — inferred from mechanistic rationale text; no formal EU marketing record exists since the drug is not marketed |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for tolcapone is not available in this Evidence Pack (flagged as a High-severity data gap). Based on contextual information embedded in the model's own rationale fields, tolcapone acts as a **COMT inhibitor**, which slows the peripheral and central breakdown of dopamine/catecholamines and is used to extend the therapeutic window of levodopa in Parkinson's disease.

For the top-ranked prediction, **Rasmussen subacute encephalitis**, the model's own rationale explicitly states that this is an autoimmune/inflammatory disease causing unilateral cortical destruction, with **no known pathophysiological link** to COMT inhibition or catecholamine metabolism. The prediction score is driven purely by knowledge-graph embedding similarity, not by any identifiable biological mechanism.

Notably, several **lower-ranked** candidates in this Evidence Pack show substantially stronger mechanistic plausibility than the top-ranked one — most importantly **"paralysis agitans, juvenile, of Hunt"** (rank 10), a historical term for early-onset/juvenile Parkinson's disease, whose pathophysiology overlaps almost completely with tolcapone's approved indication, and **Lewy body dementia** (rank 6), which shares α-synuclein/dopaminergic pathology with Parkinson's disease and is supported by two preclinical/mechanistic publications. These may warrant closer attention than the top TxGNN-ranked candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: literature evidence was found for a lower-ranked candidate, Lewy body dementia — PMID [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) and PMID [31744850](https://pubmed.ncbi.nlm.nih.gov/31744850/) — but none for the top-ranked prediction, Rasmussen subacute encephalitis.)*

---

## EU Market Information

Tolcapone is currently **not marketed** in the EU under this Evidence Pack's data (0 authorizations on file), so no EU product/license table is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA-equivalent warnings and contraindications data are flagged as a Blocking data gap in this Evidence Pack, meaning a formal Stage-1 safety screen cannot yet be completed for this drug.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Rasmussen subacute encephalitis) has no supporting clinical trials, no literature, and no plausible mechanistic link per the model's own rationale — it is a pure embedding-similarity artifact at decision stage S0. Combined with a Blocking gap in TFDA-equivalent safety data (warnings/contraindications) and a High-severity gap in mechanism-of-action data, this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Official safety labeling (warnings, contraindications, black-box hepatotoxicity information) sourced from a regulatory agency (e.g., TFDA or EMA SmPC)
- Structured mechanism-of-action data via DrugBank API query
- Re-evaluation of alternative, more mechanistically plausible candidates in this same prediction set — specifically **juvenile parkinsonism (Hunt)** and **Lewy body dementia**, which show stronger biological rationale and, in the case of Lewy body dementia, existing preclinical literature support
- If pursuing Rasmussen subacute encephalitis specifically, dedicated preclinical/mechanistic studies would be required before any clinical evaluation, given the absence of an identified biological pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

