---
layout: default
title: Ravulizumab
parent: AI Predictions (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Complement-Mediated Hemolytic Disorders to Congenital Neutropenia (G6PC3 Deficiency)

## One-Sentence Summary

> Ravulizumab is a long-acting anti-C5 monoclonal antibody whose established clinical role, per the repurposing rationale on file, is treating complement-mediated hemolytic and thrombotic microangiopathic disorders such as PNH and aHUS.
> The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**,
> but currently **0 clinical trials** and **0 publications** support this direction — the model itself flags the mechanistic link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in structured regulatory data (0 EU authorizations on file); rationale text indicates established use in complement-mediated hemolysis/TMA (e.g., PNH, aHUS) |
| Predicted New Indication | Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in the evidence pack (DG002). However, the repurposing rationale field describes Ravulizumab as a long-acting anti-C5 monoclonal antibody that blocks formation of the terminal complement complex (membrane attack complex, MAC), with clinical relevance concentrated in complement-mediated hemolysis and thrombotic microangiopathy — conditions such as paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS).

The predicted new indication, G6PC3-deficient severe congenital neutropenia, is driven by endoplasmic-reticulum stress that increases neutrophil apoptosis — a glucose-metabolism and ER-function disorder. This pathway does not overlap with terminal complement activation.

The rationale supplied with this candidate explicitly states the mechanistic link is **weak**, and suggests the prediction may reflect the knowledge graph clustering rare hematologic diseases together rather than a genuine shared biological pathway. This is a case where a high TxGNN score is not corroborated by any independent mechanistic or clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorizations are on file for Ravulizumab in this dataset (market status: Not Marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: Safety warnings, contraindications, and DDI data are marked as a blocking data gap (DG001) in this evidence pack and could not be evaluated.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, no clinical trials or literature), and the rationale itself identifies the drug-disease mechanistic link as weak/likely noise. Combined with a blocking data gap on safety labeling, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Ravulizumab (resolve DG002)
- TFDA/SmPC-equivalent safety labeling — warnings, contraindications, DDI (resolve DG001, blocking)
- Independent mechanistic or preclinical evidence linking terminal complement inhibition to G6PC3-deficient neutropenia
- Confirmation of current EU regulatory/marketing status, since this dataset shows 0 authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

