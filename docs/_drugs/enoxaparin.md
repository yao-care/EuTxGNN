---
layout: default
title: Enoxaparin
parent: AI Predictions (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Enoxaparin
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

# Enoxaparin: From Venous Thromboembolism Prevention to Thrombophilia due to Protein C Deficiency

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin (LMWH) anticoagulant, established for the prevention and treatment of venous thromboembolism. The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence rests entirely on the model's confidence score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Venous thromboembolism prophylaxis/treatment (established LMWH use); specific authorized indication text not available — no EU marketing authorization is on file for this dataset |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known information, Enoxaparin is a low-molecular-weight heparin (LMWH) that inhibits Factor Xa (and to a lesser extent thrombin), and its efficacy in preventing and treating venous thromboembolism is well established; mechanistically this antithrombotic action may be applicable to conditions of pathological hypercoagulability.

Protein C deficiency is an inherited thrombophilia: reduced Protein C activity impairs inactivation of Factors Va and VIIIa, producing a hypercoagulable state and elevated venous thrombosis risk. An anticoagulant such as enoxaparin is therefore mechanistically plausible as thromboprophylaxis in this population — the same rationale underlying LMWH use in other inherited and acquired thrombophilias.

However, this mechanistic plausibility is not yet corroborated by any registered trial or published study specific to this disease. The prediction currently rests solely on the TxGNN model's score, and the original mechanism-of-action data for enoxaparin itself is flagged as a data gap in this evidence pack (DG002), which limits how confidently the mechanistic link above can be verified against primary sources.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorization is currently on file for Enoxaparin in this dataset (market status: not marketed; 0 authorizations recorded).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: a blocking data gap (DG001) has been identified — TFDA label warnings/contraindications are not yet available, which prevents this candidate from entering the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high TxGNN confidence score, but is unsupported by any clinical trial or literature evidence (L5), and the drug's mechanism-of-action and label safety data are both currently missing — together these block progression past initial screening.

**To proceed, the following is needed:**
- Enoxaparin mechanism of action (MOA) data from DrugBank (DG002)
- TFDA/SmPC label warnings and contraindications, to enable the S1 safety pre-assessment (DG001, blocking)
- Targeted literature or preclinical search for LMWH use in inherited Protein C deficiency/thrombophilia to establish at least mechanistic (L4) support
- Confirmation of original approved indication(s) and any existing marketing authorization, since none are currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

