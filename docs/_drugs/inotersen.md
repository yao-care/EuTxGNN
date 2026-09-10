---
layout: default
title: Inotersen
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Inotersen
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

# Inotersen: From Hereditary Transthyretin Amyloidosis (hATTR) to Acute Intermittent Porphyria

## One-Sentence Summary

Inotersen is a liver-directed antisense oligonucleotide originally developed to treat hereditary transthyretin amyloidosis (hATTR) polyneuropathy by suppressing TTR protein production.
The TxGNN model predicts it may be relevant to **Acute Intermittent Porphyria (AIP)**, a mechanistically distant hepatic disease,
but currently only **1 review-level publication** supports this direction, with **no clinical trials** registered for this pairing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Transthyretin Amyloidosis (hATTR) Polyneuropathy (drug not currently licensed in Taiwan; indication inferred from mechanism-of-action evidence) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Inotersen is a liver-directed 2'-MOE antisense oligonucleotide that degrades transthyretin (TTR) mRNA, thereby reducing circulating TTR protein. This mechanism underlies its approved use in hATTR polyneuropathy, a hereditary hepatic-metabolic disease that also manifests as peripheral neuropathy.

Acute intermittent porphyria (AIP) shares structural similarities with hATTR at the disease-category level: both are hereditary, liver-driven metabolic disorders that can present with peripheral neuropathy. This "liver-directed oligonucleotide therapy + neuropathy phenotype" pattern has precedent — givosiran, an RNAi therapeutic targeting ALAS1, is an approved treatment for AIP.

However, this analogy is indirect rather than mechanistic. Inotersen has no known activity on ALAS1 or the heme biosynthesis pathway that drives AIP pathophysiology; its TTR-suppression mechanism does not intersect with AIP's underlying biology. The prediction should therefore be interpreted as a class-level pattern match rather than a validated pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Review | Neurological Sciences | Reviews therapeutic advances in genetic neuromuscular/peripheral neuropathy disorders, covering hATTR treatments (including TTR-lowering agents); does not directly study inotersen in AIP |

## Safety Considerations

Please refer to the drug's package insert (仿單) for safety information; TFDA labeling data for this product is not currently available (blocking data gap).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between inotersen and AIP is an indirect class-level analogy, not a validated pathway connection, and is supported only by one review article with no disease-specific data on inotersen in AIP and no clinical trials. The drug is also not marketed in Taiwan (0 licenses) and TFDA safety/labeling data is unavailable, blocking any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert / label data (warnings, contraindications) — currently a blocking gap
- Confirmed mechanism-of-action documentation from DrugBank or primary literature
- Preclinical or pharmacodynamic evidence directly linking TTR mRNA suppression to AIP pathophysiology or symptom relief
- Any exploratory clinical or case-level evidence specific to inotersen in porphyria patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

