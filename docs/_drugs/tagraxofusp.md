---
layout: default
title: Tagraxofusp
parent: AI Predictions (L5)
nav_order: 585
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tagraxofusp: predicted new indication Esotropia (evidence level L5). Approved use: First-line monotherapy for adult patients with blastic plasmacytoid d…"
monitor_inn: "Tagraxofusp"
predicted_indications: ["esotropia", "pre-malignant neoplasm", "inner ear neoplasm", "benign neoplasm of tongue", "bronchial adenomas/carcinoids childhood", "chondroid hamartoma", "non-seminomatous lesion", "ductal or ductular proliferation", "cystic neoplasm", "thyroglossal duct cyst"]
---

# Tagraxofusp
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Tagraxofusp: From Blastic Plasmacytoid Dendritic Cell Neoplasm to Esotropia

## One-Sentence Summary

Tagraxofusp was originally authorised in the EU as a monotherapy for the first-line treatment of adult patients with blastic plasmacytoid dendritic cell neoplasm (BPDCN).
The TxGNN model predicts it may be effective for **esotropia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The high score appears to be a graph-based artefact rather than a biologically grounded signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | First-line monotherapy for adult patients with blastic plasmacytoid dendritic cell neoplasm (BPDCN) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorisation is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, tagraxofusp is a CD123-directed cytotoxin (interleukin-3 fused to a truncated diphtheria toxin). It targets CD123-expressing malignant cells, which is why it was developed for BPDCN.

Esotropia is an ocular motor alignment disorder with no known CD123-driven pathology. No credible mechanistic link between the original and the predicted indication could be identified. The high TxGNN score (0.997) most likely reflects proximity in the knowledge graph rather than real biology, so the prediction should be treated as unsupported.

The other top-ranked predictions show the same pattern. They are mostly benign or non-CD123-driven conditions such as pre-malignant neoplasm, inner ear neoplasm, benign tongue neoplasm, chondroid hamartoma and thyroglossal duct cyst. Their scores are all between 99.71% and 99.73%, and none has any trial or literature support. Together they suggest a general "neoplasm" association in the graph rather than target-specific rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005031 (cancelled) | Elzonris | Not specified | Monotherapy for the first-line treatment of adult patients with blastic plasmacytoid dendritic cell neoplasm (BPDCN). |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted cytotoxic fusion protein (CD123-directed; IL-3 linked to diphtheria toxin fragment) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Liver function and signs of capillary leak syndrome are of particular relevance; please refer to the SmPC warnings and precautions for the full list |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 66 interactions were identified in the interaction screening. All of the 20 listed in the data compiled for this report are rated Moderate and mostly involve glucose-lowering agents. Examples include:
  - Metformin, pioglitazone, glimepiride and chlorpropamide
  - Acarbose
  - Canagliflozin, dapagliflozin and empagliflozin
  - Alogliptin, saxagliptin and linagliptin
  - Albiglutide, dulaglutide and semaglutide
  - Several insulins (aspart, degludec, detemir, glargine, glulisine, human isophane)
- **Other safety considerations**: Based on the compiled rationale, the known capillary leak syndrome and hepatotoxicity risks of this cytotoxic fusion protein would be hard to justify in a benign or non-CD123-driven condition.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanistic link between a CD123-directed cytotoxin and esotropia. The only EU authorisation is cancelled, and the drug carries serious toxicity risks.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) to allow a proper mechanistic-link analysis
- Warnings and contraindications from the EMA product information, which are required for safety screening
- Any preclinical or clinical evidence of CD123 involvement in esotropia (none is currently known)
- A review of whether the CD123-positive haematologic malignancy predictions are more promising than the current top-ranked results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

