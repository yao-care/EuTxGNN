---
layout: default
title: Mirvetuximab Soravtansine
parent: AI Predictions (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Mirvetuximab Soravtansine
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

# Mirvetuximab Soravtansine: From Platinum-Resistant Ovarian Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Mirvetuximab Soravtansine is an antibody-drug conjugate (ADC) referenced in the literature as a treatment for FRα-positive, platinum-resistant ovarian cancer; however, official regulatory and mechanism-of-action data for this drug are currently unavailable (data gaps). The TxGNN model predicts potential efficacy for **Antithrombin Deficiency Type 2**, but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale text explicitly states there is no known biological mechanism linking the two.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Platinum-resistant, FRα-positive ovarian cancer (inferred from literature evidence only; not confirmed by official regulatory/DrugBank data) |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 97.95% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Mirvetuximab Soravtansine is currently a data gap. Based on information embedded in the evidence pack's rationale text, this drug is a cytotoxic antibody-drug conjugate (ADC) that targets folate receptor alpha (FRα) on tumor cells and delivers DM4, a maytansinoid microtubule inhibitor, as its payload. It is referenced in the literature as a treatment for platinum-resistant, FRα-positive ovarian cancer.

Antithrombin deficiency type 2 is a hereditary coagulation disorder caused by dysfunction of the antithrombin protein, leading to a predisposition toward spontaneous thrombosis. There is no established physiological pathway connecting FRα-targeted tumor cytotoxicity to antithrombin regulation or coagulation control.

The evidence pack's own mechanistic assessment for this pairing states explicitly: **"無合理機轉... 僅為 TxGNN 模型高分預測，無任何臨床或文獻支持"** ("no plausible mechanism... this is purely a high-scoring TxGNN model prediction, with no clinical or literature support"). In other words, despite the high statistical score, the model itself (via its accompanying rationale) flags this prediction as mechanistically implausible. This should be treated as a strong caution against over-interpreting the raw TxGNN score.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Cytotoxicity

Mirvetuximab Soravtansine is an antibody-drug conjugate with a cytotoxic microtubule-inhibitor payload, used in oncology — it qualifies as an antineoplastic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Antibody-drug conjugate (ADC) with a cytotoxic maytansinoid payload (DM4, a microtubule inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | As an ADC with a cytotoxic payload, handling should follow standard cytotoxic drug handling protocols pending SmPC confirmation |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (97.95%), but the drug's own documented rationale states there is no plausible mechanistic link between this cytotoxic FRα-targeted ADC and a hereditary coagulation disorder, and there is zero clinical trial or literature support. Combined with a blocking data gap on TFDA/SmPC safety information (warnings, contraindications) and a high-severity gap on confirmed MOA, this candidate cannot proceed past initial safety screening (S1).

**To proceed, the following is needed:**
- Official label/SmPC safety data (warnings, contraindications, DDI) — currently a blocking data gap (DG001)
- Confirmed mechanism of action via DrugBank or primary literature — currently a high-severity data gap (DG002)
- Preclinical or mechanistic evidence establishing a biological rationale between FRα-ADC cytotoxicity and coagulation/thrombophilia pathways before any further evaluation

**Note:** Among the 10 TxGNN-predicted candidates in this evidence pack, all carry a "Hold" recommendation. Rank 5 (plasma cell myeloma) has a comparatively higher evidence level (L4, 4 review-level publications) than the top-ranked candidate, though those publications discuss ADCs in gynecologic oncology generally rather than this drug in myeloma specifically, and the FRα target is not a recognized myeloma biomarker. If pursuing further repurposing evaluation for this drug, rank 5 would warrant review ahead of rank 1.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

