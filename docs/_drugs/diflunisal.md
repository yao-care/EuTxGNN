---
layout: default
title: Diflunisal
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: From Pain and Arthritis to Acromesomelic Dysplasia (Hunter-Thompson Type)

## One-Sentence Summary

Diflunisal is a salicylate-derived NSAID (non-steroidal anti-inflammatory drug) known for its analgesic and anti-inflammatory effects in musculoskeletal conditions such as pain and arthritis.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type** — a rare genetic skeletal dysplasia caused by GDF5/CDMP1 mutations —
however **no clinical trials** and **no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain relief and inflammatory musculoskeletal conditions (arthritis, mild-to-moderate pain) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on established pharmacology, Diflunisal is a difluorophenyl derivative of salicylic acid that acts as a dual COX-1/COX-2 inhibitor, suppressing prostaglandin synthesis to produce analgesic and anti-inflammatory effects. It is structurally related to aspirin but has a longer half-life (~8–12 hours) and improved gastrointestinal tolerability relative to conventional salicylates.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the *GDF5/CDMP1* gene. This disrupts BMP (bone morphogenetic protein) signaling during embryonic skeletal development, resulting in characteristic shortening of the forearms and lower legs (acromesomelia). The condition is a structural developmental defect, not an inflammatory disease.

The mechanistic rationale for this TxGNN prediction is weak. COX-1/COX-2 inhibition has no known intersection with GDF5/BMP signaling pathways, and prostaglandin suppression cannot correct or modify the underlying gene-level skeletal defect. Diflunisal could theoretically provide symptomatic pain relief in affected individuals, but this represents a general NSAID property rather than a disease-specific repurposing opportunity. The model's high prediction score likely reflects structural proximity in the drug-disease knowledge graph rather than genuine therapeutic biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Acromesomelic dysplasia, Hunter-Thompson type is a genetic structural bone defect driven by *GDF5/CDMP1* mutations; Diflunisal's COX inhibition mechanism has no pathway-level connection to BMP signaling and cannot modify the underlying disease, making this a non-viable repurposing candidate.

**To proceed, the following is needed:**
- MOA data from DrugBank to confirm or refute any novel mechanistic link (e.g., off-target BMP pathway interactions)
- TFDA/SmPC documentation for complete safety profile assessment
- Preclinical evidence demonstrating any GDF5/BMP pathway modulation before any clinical hypothesis generation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

