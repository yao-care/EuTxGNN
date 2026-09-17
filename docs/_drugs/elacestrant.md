---
layout: default
title: Elacestrant
parent: AI Predictions (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Elacestrant
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

# Elacestrant: From ER+/HER2- Breast Cancer to Amenorrhea

## One-Sentence Summary

Elacestrant is a selective estrogen receptor degrader (SERD) known clinically for treating ER+/HER2- breast cancer, though the evidence pack does not carry a formal original-indication record for this drug. The TxGNN model's top prediction points to **Amenorrhea**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic annotation flags the prediction as pharmacologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (known clinical use: ER+/HER2- breast cancer, SERD class) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 92.50% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information gathered from the evidence pack's own rationale annotations, elacestrant is an estrogen receptor (ER) degrader used in ER+/HER2- breast cancer, where it antagonizes and degrades ER signaling to suppress tumor growth.

The model's rank-1 prediction, however, links elacestrant to **Amenorrhea** — and the evidence pack's own mechanistic assessment explicitly states this direction is biologically backwards: an ER-degrading drug is pharmacologically more likely to *induce* a menopausal-like hormonal state (including amenorrhea-related side effects) than to *treat* primary or secondary amenorrhea. The annotation describes this as "opposite to known pharmacology, mechanism not reasonable, purely a TxGNN embedding-similarity artifact."

In other words, this top-ranked candidate should be read as a model-similarity signal rather than a biologically grounded hypothesis. None of the lower-ranked candidates in this pack fare better: rank 3 (multiple endocrine neoplasia) only pulled in breast-cancer trials unrelated to MEN (Grade C relevance), and rank 9 (hypogonadotropic hypogonadism) only pulled in COVID-19 anosmia literature that matched on the keyword "anosmia" rather than on the actual endocrine disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Elacestrant is not currently authorized in this market (0 licenses on record; market status: Not Marketed). No authorization records are available to list.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Selective Estrogen Receptor Degrader, SERD) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Amenorrhea) has no clinical trial or literature support and is flagged by the evidence pack's own mechanistic analysis as pharmacologically implausible (opposite direction to elacestrant's known ER-degrading action). None of the other nine candidates in this pack are backed by disease-relevant evidence either — matched trials and literature are all off-target (breast cancer trials, COVID-19 anosmia papers). This is an L5, model-prediction-only case with no path to S1 safety screening.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap — required before any S1 safety pre-screening)
- Confirmed mechanism of action data from DrugBank
- A re-ranked or re-queried TxGNN output, since the current top candidates show weak or contradictory mechanistic links
- If pursuing further, disease-specific (not drug-name-only) clinical trial and literature searches for any retained candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

