---
layout: default
title: Polatuzumab Vedotin
parent: AI Predictions (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: From Diffuse Large B-Cell Lymphoma to HER2 Positive Breast Carcinoma

## One-Sentence Summary

> Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate (ADC) originally developed for relapsed/refractory Diffuse Large B-Cell Lymphoma (DLBCL).
> The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as mechanistically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diffuse Large B-Cell Lymphoma (DLBCL) — per known drug class (no structured license data on file; drug is not marketed in this jurisdiction) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no verified structured mechanism-of-action (MOA) record is available for Polatuzumab vedotin in this evidence pack — this is flagged internally as a High-severity data gap requiring a DrugBank API lookup. Based on the drug-class context noted in the model's own rationale, Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate (ADC) that delivers the microtubule-disrupting cytotoxic payload MMAE specifically to CD79b-expressing B cells, and it is approved for relapsed/refractory DLBCL in combination regimens.

CD79b is a surface marker restricted to the B-cell lineage; it is not expressed on breast epithelial or breast tumor cells. This means the antibody targeting component of the ADC has no biological mechanism to engage HER2-positive, PR-positive, PR-negative, luminal A/B, or normal breast-like breast tumors — the mechanistic rationale linking the original indication to any of the predicted breast cancer subtypes is weak to absent.

The TxGNN knowledge-graph score for this pairing is high (99.34%), but it is not corroborated by any registered clinical trial or relevant literature. This pattern — a high embedding score with zero real-world evidence and no plausible target biology — is consistent with a knowledge-graph false positive rather than a genuine repurposing signal, as explicitly noted in the evidence pack's own repurposing rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

This drug currently holds no EU marketing authorizations (0 licenses on file; market status: Not marketed／not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Antibody-drug conjugate) with cytotoxic microtubule-inhibitor payload (MMAE) |
| Myelosuppression Risk | Medium–High (class effect of MMAE-based ADCs; neutropenia commonly reported — please refer to the SmPC for drug-specific data, as detailed toxicity data is not on file) |
| Emetogenicity Classification | Low to moderate (typical of ADC-class agents; not confirmed for this specific product) |
| Monitoring Items | CBC with differential (neutropenia), liver function tests, peripheral neuropathy assessment (MMAE-related) |
| Handling Protection | Yes — must follow institutional hazardous/cytotoxic drug handling protocols given the MMAE payload |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but zero corroborating clinical trials or literature (Evidence Level L5), and the mechanistic rationale itself indicates CD79b — the drug's only known target — is not expressed in breast tumor tissue, making the biological plausibility of this repurposing candidate weak. The same pattern (high score, no evidence, no target expression) also applies to the other 9 predicted indications in this candidate set, several of which (e.g., antithrombin deficiency, heparin cofactor 2 deficiency) appear to be unrelated coagulation disorders with no conceivable mechanistic link, and one (luminal A/B breast cancer) shows literature counts that on inspection are likely a text-mining artifact from the letter "B" rather than genuine relevance.

**To proceed, the following is needed:**
- Resolve the Blocking-severity data gap (DG001): obtain TFDA/regional label warnings and contraindications before any safety-stage (S1) review
- Resolve the High-severity data gap (DG002): obtain verified MOA data from DrugBank API
- Independent confirmation of CD79b (or any alternative target) expression status in HER2-positive breast carcinoma tissue
- Do not advance beyond S0 unless genuine clinical trial or peer-reviewed evidence emerges for this specific drug-indication pairing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

