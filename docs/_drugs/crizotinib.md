---
layout: default
title: Crizotinib
parent: AI Predictions (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is a targeted kinase inhibitor, originally used to treat ALK-positive and ROS1-positive advanced non-small cell lung cancer (NSCLC), as well as certain ALK-positive paediatric lymphomas and tumours.
The TxGNN model predicts it may be effective for **gingival fibromatosis** with a very high score, but **no clinical trials and no publications** currently support this prediction.
It is a model-only signal and should be treated as a hypothesis, not as an evidence-backed new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive advanced NSCLC (first-line and previously treated), ROS1-positive advanced NSCLC, and paediatric ALK-positive ALCL and IMT |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Crizotinib inhibits the receptor tyrosine kinases ALK, ROS1 and MET. Detailed mechanism of action data are not available in the data compiled for this report, so this description draws on the general literature in the compiled data (for example, drug monographs describing it as an ATP-competitive inhibitor of c-MET, ALK and ROS1).

For gingival fibromatosis, no mechanistic link has been identified. This condition is not known to be driven by ALK, ROS1 or MET. The high TxGNN score (0.998) is a model prediction only and is not supported by any trial or publication. The rank of the prediction (2501) also shows it is not a standout among the model's outputs.

Other lower-ranked predictions in the data are mostly either (a) restatements of the existing NSCLC indication (for example lung hilum carcinoma, pulmonary sulcus neoplasm), or (b) results of disease-term mapping with no real disease-specific signal (for example benign lung neoplasm, lung hamartoma). The top prediction should therefore be read with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002489 | Xalkori | Not specified | Monotherapy for first-line and previously treated ALK-positive advanced NSCLC, ROS1-positive advanced NSCLC, paediatric ALK-positive ALCL and IMT... |

The only authorization in the data is recorded as cancelled, so there is no currently valid EU authorization for crizotinib.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions. Case reports in the compiled literature also describe liver injury, QT prolongation and bradycardia, so liver function and ECG monitoring are reasonable considerations |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. Examples from the retrieved list:
  - **Major**: clarithromycin, cisapride, dolasetron, eliglustat, granisetron
  - **Moderate**: famotidine, metformin, loperamide, bupropion, aprepitant, dexamethasone, budesonide, bisacodyl, clotrimazole

- **Reports from the literature** (case reports, not label data): fatal fulminant liver failure, multiple cardiac toxicities (bradycardia, QT prolongation, ventricular arrhythmia, pericarditis), sick sinus syndrome, erythema multiforme and erosive esophagitis. These matter if use were considered in a non-oncology condition such as gingival fibromatosis, where the benefit-risk balance would be much less favourable.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible ALK, ROS1 or MET mechanism in gingival fibromatosis. The drug also carries notable toxicity, and its only EU authorization is cancelled.

**To proceed, the following is needed:**
- A mechanistic rationale showing a kinase-driven pathway in gingival fibromatosis, or preclinical data
- Mechanism of action data and the SmPC warnings and contraindications (the label safety review could not be completed)
- A benefit-risk assessment for a benign, non-oncology condition, given the toxicity signals
- Clarification of the cancelled EU status and current availability

**Other predictions of note (for context only):**
- **Lung hilum carcinoma** (score 99.73%, L4, Research Question): biologically plausible for ALK- or ROS1-driven NSCLC, but largely restates the existing indication, so it is not true repurposing.
- **Lung germ cell tumour** (score 99.73%, L3, Research Question): no direct evidence. Only tumour-agnostic, biomarker-driven trials (NCT01121588, NCT02465060) offer a route, and only for tumours carrying ALK, ROS1 or MET alterations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

