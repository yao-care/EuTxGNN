---
layout: default
title: Tafasitamab
parent: AI Predictions (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
---

# Tafasitamab
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

# Tafasitamab: From Diffuse Large B-Cell Lymphoma to Drug-Induced Osteoporosis

## One-Sentence Summary

Tafasitamab is an Fc-enhanced anti-CD19 monoclonal antibody, used in combination with lenalidomide for relapsed/refractory diffuse large B-cell lymphoma (DLBCL). The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**, but currently there are **no clinical trials** and **no supporting literature**, and the evidence pack itself notes no known biological link between CD19+ B-cell depletion and bone metabolism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diffuse Large B-Cell Lymphoma (DLBCL), in combination with lenalidomide |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for tafasitamab is not available in the current evidence pack (data gap, severity: High). Based on information embedded in the prediction rationale, tafasitamab is an Fc-enhanced monoclonal antibody targeting CD19, which depletes CD19+ B cells through antibody-dependent cellular cytotoxicity (ADCC) and phagocytosis (ADCP). It is approved for use in combination with lenalidomide for relapsed or refractory DLBCL.

For the top-ranked prediction, drug-induced osteoporosis, the evidence pack explicitly states that there is no known direct mechanistic relationship between CD19+ B-cell depletion and bone metabolism regulation. The pairing arises purely from TxGNN's network-topology-based inference and is described in the pack as lacking biological plausibility.

Because no mechanistic rationale, clinical trial, or published literature supports this specific pairing, it should be treated as a low-confidence AI hypothesis only, not a candidate ready for further pharmacological reasoning.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Tafasitamab is not currently authorized for marketing in the European Union (0 marketing authorizations on record).

---

## Cytotoxicity

Tafasitamab targets DLBCL, a hematologic malignancy, and is therefore evaluated as an antineoplastic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (Fc-enhanced anti-CD19 monoclonal antibody; ADCC/ADCP-mediated B-cell depletion, not a conventional cytotoxic agent) |
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
The top-ranked prediction (drug-induced osteoporosis) is evidence level L5 — a pure AI network-topology prediction with no clinical trials, no literature, and no biological plausibility per the evidence pack's own analysis. Tafasitamab is also not marketed in the EU, and critical safety data (TFDA/SmPC warnings, contraindications, DDI) and confirmed MOA data are missing, blocking entry into the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data via DrugBank API query
- TFDA/EU SmPC warnings, contraindications, and drug interaction data (currently blocking S1 safety evaluation)
- Independent preclinical or mechanistic studies linking B-cell depletion/immune modulation to bone metabolism, if this specific hypothesis is to be pursued
- Note: rank-10 candidate (pityriasis lichenoides) in the same evidence pack reflects an adverse drug reaction case report during tafasitamab+lenalidomide therapy, not a treatment signal — flagged here to avoid misinterpretation in future evaluation rounds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

