---
layout: default
title: Velaglucerase Alfa
parent: AI Predictions (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Velaglucerase Alfa
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

# Velaglucerase alfa: From Gaucher Disease to Steel Syndrome

## One-Sentence Summary

> Velaglucerase alfa is an enzyme replacement therapy whose approved indication is Gaucher disease (type 1), where it substitutes for deficient glucocerebrosidase.
> The TxGNN model predicts it may be effective for **Steel syndrome**, a COL27A1-related skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a likely knowledge-graph artifact rather than a mechanistically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (type 1) — inferred from evidence-pack rationale text; not independently confirmed by regulatory data |
| Predicted New Indication | Steel syndrome |
| TxGNN Prediction Score | 96.99% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`[Data Gap]` in the evidence pack). Based on the information that is present, velaglucerase alfa is a recombinant human glucocerebrosidase used as enzyme replacement therapy, and its efficacy in Gaucher disease — a lysosomal storage disorder caused by glucocerebrosidase deficiency — is well established.

Steel syndrome, however, is a skeletal dysplasia caused by mutations in COL27A1, a collagen gene. It has no known overlap with the glycosphingolipid-metabolism pathway that glucocerebrosidase acts on. The evidence pack's own mechanistic assessment states this explicitly: the high TxGNN score is likely an artifact of "rare genetic disease" node clustering in the knowledge graph, rather than a reflection of shared biology.

This pattern repeats across the other nine ranked candidates in the evidence pack: several (hypophosphatasia, growth hormone insensitivity syndrome, proximal myopathy with extrapyramidal signs) are flagged as having no plausible pathway overlap; a few (Wolman disease, cholesteryl ester storage disease) share only a broad "lysosomal storage disease / enzyme replacement therapy" class-level similarity without substrate specificity for glucocerebrosidase; and two (esophageal varices, with and without bleeding) are actually downstream complications of Gaucher disease itself rather than independent new indications. None of the ten candidates is supported by a mechanistic rationale strong enough to justify progression without further validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Velaglucerase alfa currently has no EU marketing authorization on record in this evidence pack (0 authorizations, market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: Label warnings/contraindications data collection is flagged in the evidence pack as a blocking data gap and has not yet been retrieved from the regulatory source.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications are L5 (model-prediction-only, no supporting clinical trials or literature), and the evidence pack's own mechanistic analysis indicates most — including the top-ranked Steel syndrome — are likely knowledge-graph clustering artifacts without biological plausibility. Combined with a blocking gap in regulatory safety data, there is no basis to proceed at this time.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (DG002)
- Independent mechanistic review of the top candidates to distinguish genuine signal from graph-embedding artifact before any evidence-collection effort is invested
- If any candidate is prioritized, targeted literature/clinical-trial searches to establish at least L3–L4 evidence before further scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

