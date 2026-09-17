---
layout: default
title: Evolocumab
parent: AI Predictions (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Evolocumab
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

# Evolocumab: From Hypercholesterolemia to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab is a PCSK9-inhibitor monoclonal antibody established for LDL-cholesterol lowering (its formal original-indication record is not populated in this Evidence Pack).
The TxGNN model's top prediction suggests possible relevance to **symptomatic hemophilia in female carriers**,
but this is currently supported by **0 clinical trials** and **0 publications** — the prediction is model-output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (`taiwan_regulatory.licenses` is empty; `original_indications` is empty) |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for evolocumab is not available in this Evidence Pack (`original_moa` = Data Gap). Based on the mechanistic notes attached to this prediction, evolocumab is a PCSK9 inhibitor that acts on the LDL-receptor (LDLR) recycling pathway to lower LDL-cholesterol — a pathway with no established, direct connection to coagulation factor synthesis or clearance.

The rationale for this specific prediction explicitly flags this as a weak link: while some LDLR-family members (e.g., LRP1) participate in aspects of coagulation-factor metabolism, there is no literature support for PCSK9 inhibition affecting the hemophilia phenotype, and the direction of any effect is unclear — it could plausibly be neutral or even increase bleeding risk rather than help.

This weakness is reinforced by the broader prediction list: ranks 2–10 include several mutually contradictory disease categories (e.g., bleeding disorders like "hemorrhagic disease of newborn" alongside a pro-thrombotic condition like "inherited thrombophilia"), plus non-specific ontology labels ("disease of catalytic activity," "disorder of other vitamins and cofactors metabolism and transport") that are not actionable disease entities. Taken together, this pattern indicates KG-embedding similarity noise rather than a coherent, mechanistically grounded repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Evolocumab currently has no EU marketing authorization recorded in this dataset (market status: Not marketed / Not Marketed; 0 authorizations on file).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: `taiwan_regulatory` marks TFDA label warnings/contraindications as a Blocking data gap (DG001) — this must be resolved via TFDA label lookup before any S1 safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (symptomatic hemophilia in female carriers) has no supporting clinical trials or literature (L5, model prediction only), and its own mechanistic rationale describes the drug-disease link as absent or directionally uncertain. Combined with contradictory signals across the rest of the top-10 list, there is currently no basis to advance this candidate beyond a research hypothesis.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap, DG001)
- Confirmed mechanism of action data via DrugBank API (DG002)
- Original indication and EU licensing records (currently empty in this pack)
- Preclinical or mechanistic studies specifically linking PCSK9/LDLR pathway activity to coagulation factor biology, if this hypothesis is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

