---
layout: default
title: Gefitinib
parent: AI Predictions (L5)
nav_order: 280
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Gefitinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Locally advanced or metastatic NSCLC with activating EGFR tyrosine ki…"
monitor_inn: "Gefitinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Gefitinib: From EGFR-Mutant Non-Small-Cell Lung Cancer to fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor, originally used for locally advanced or metastatic non-small-cell lung cancer (NSCLC) with activating EGFR mutations.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Locally advanced or metastatic NSCLC with activating EGFR tyrosine kinase mutations |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Gefitinib is known as an EGFR tyrosine kinase inhibitor, and its efficacy in EGFR-mutant NSCLC is established. Whether this extends to gingival fibromatosis is unproven.

One possible link is that EGFR/ErbB signalling drives fibroblast proliferation, which could be relevant to a fibroproliferative gum condition. This is speculative and not supported by any trial or publication in the data. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions are similarly unsupported, and several have no plausible EGFR mechanism. For example, the VCP-related inclusion body myopathy with Paget disease looks like a network artifact. Predictions that involve lung tumours (such as lung hilum carcinoma and pulmonary sulcus neoplasm) mainly reflect the already-approved lung cancer setting rather than a genuinely new indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001016 (cancelled) | Iressa | Not specified | Treatment of adult patients with locally advanced or metastatic non-small-cell lung cancer with activating mutations of epidermal-growth-factor-receptor tyrosine kinase. |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC; liver function and respiratory symptoms are relevant given the associations below |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: liver disease, gallbladder disease, interstitial lung disease, pulmonary fibrosis and postinflammatory pulmonary fibrosis are linked to gefitinib as contraindication-type edges. Published case reports in the compiled literature also describe gefitinib-induced pneumonitis and interstitial lung disease.
- **Drug Interactions**: 100 interactions were found. Most of those listed are Moderate severity. Main ones include:
  - Acid-suppressing agents: famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole
  - CYP-related agents: clarithromycin, miconazole, clotrimazole, aprepitant, dexamethasone
  - Others: naltrexone, troglitazone
  - Unknown severity: calcitriol, glimepiride

Official warnings and contraindications from the product information were not available. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature for gingival fibromatosis. The mechanistic link is speculative. The only EU authorization is cancelled, and the safety data compiled are incomplete.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence on EGFR inhibition in gingival fibromatosis or related fibroproliferative conditions
- Mechanism of action data for gefitinib and a review of how it would apply to this disease
- Official SmPC warnings and contraindications, including the interstitial lung disease and liver risks
- A benefit-risk assessment for a non-oncology population, since gefitinib is a cancer drug with notable skin and lung toxicity
- Clarification of the regulatory status, given the cancelled EU authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

