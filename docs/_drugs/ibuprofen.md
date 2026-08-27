---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the provided Evidence Pack, here is the drug repurposing evaluation report.

---

# Ibuprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), globally established for pain, fever, and inflammation, though this Evidence Pack contains no Taiwan-specific licensing or original-indication record (the drug is currently **not marketed in Taiwan**). The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare monogenic skeletal disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the rationale text itself flags the mechanistic link as unclear.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (no Taiwan license record); Ibuprofen is generally known as an analgesic/antipyretic/anti-inflammatory NSAID |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mechanism of action data for Ibuprofen is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, Ibuprofen is a propionic-acid-derivative NSAID that non-selectively inhibits COX-1/COX-2, reducing prostaglandin synthesis and thereby producing analgesic, antipyretic, and anti-inflammatory effects. No original indication record was found in the Taiwan regulatory data (0 licenses on file), so it is not possible to compare the original indication against the predicted one using local licensing data.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare autosomal recessive skeletal disorder caused by *NPR2* gene defects, resulting in structural cartilage growth-pathway abnormalities. The evidence pack's own `repurposing_rationale` explicitly states that this pathology has **no known association** with Ibuprofen's COX-inhibition/anti-inflammatory mechanism, and specifically raises the possibility that the high TxGNN score reflects **sparse knowledge-graph data around rare skeletal disease nodes** rather than a genuine biological signal (a form of score collapse).

Notably, 6 of the top 10 predictions for this drug (ranks 1, 2, 4, 5, 6, 7) are rare monogenic skeletal/craniofacial dysplasias with no plausible anti-inflammatory mechanism, and 2 more (ranks 8, 10) are hair-follicle/keratinization disorders similarly unrelated to NSAID pharmacology. Only rank 9 (WHIM syndrome) offers even a weak symptomatic rationale (possible relief of secondary inflammatory symptoms from recurrent infections, not disease modification). This clustering pattern across the top 10 predictions further supports the hypothesis that the ranking may be an artifact of graph sparsity for rare-disease nodes rather than a mechanistically grounded signal, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Ibuprofen currently holds **no marketing authorizations** in Taiwan (`total_licenses: 0`); market status is recorded as **未上市 (Not Marketed)**. No license, product name, dosage form, or approved indication text is available in this Evidence Pack.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and drug interaction data are all recorded as data gaps in this Evidence Pack. In particular, TFDA label warnings/contraindications (DG001) are flagged as a **Blocking** data gap, meaning this candidate cannot yet proceed to the S1 safety pre-screen stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by an L5 model prediction (score 99.74%) with zero clinical trials and zero publications, and the evidence pack's own rationale text questions whether the mechanistic link is real or an artifact of sparse rare-disease data in the knowledge graph. Combined with a Blocking gap in TFDA safety labeling data, there is currently insufficient basis to advance this candidate past initial screening.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) retrieval and parsing — currently a Blocking gap (DG001)
- Ibuprofen mechanism of action (MOA) data via DrugBank API — currently a High-severity gap (DG002)
- Independent review of whether the NPR2/cartilage-growth pathway has any plausible link to COX inhibition, or whether this ranking reflects a systematic embedding artifact for rare skeletal-disease nodes (given the clustering pattern across ranks 1–10)
- Broader literature/trial search (including rare-disease registries and case reports) before any further evidence-level upgrade is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

