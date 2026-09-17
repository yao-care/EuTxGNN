---
layout: default
title: Tipiracil
parent: AI Predictions (L5)
nav_order: 594
evidence_level: L5
indication_count: 10
---

# Tipiracil
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

# Tipiracil: From Metastatic Colorectal Cancer to Cecum Villous Adenoma

## One-Sentence Summary

Tipiracil is a pharmacokinetic-enhancing component of the trifluridine/tipiracil combination (TAS-102, Lonsurf), originally used for metastatic colorectal cancer.
The TxGNN model predicts it may be effective for **Cecum Villous Adenoma**,
but currently **0 clinical trials** and **0 publications** directly support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (as a component of the trifluridine/tipiracil combination, TAS-102/Lonsurf; not separately specified in the regulatory record) |
| Predicted New Indication | Cecum Villous Adenoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record. Based on available information, Tipiracil is not used as a standalone therapeutic agent — it is one of two active components in the trifluridine/tipiracil combination (TAS-102, brand name Lonsurf). Tipiracil acts as a thymidine phosphorylase inhibitor; its role is purely pharmacokinetic, preventing rapid degradation of trifluridine (the actual cytotoxic antimetabolite component) and thereby increasing trifluridine's systemic exposure and antitumour activity. This combination is approved for metastatic colorectal cancer.

The predicted new indication, cecum villous adenoma, is anatomically located in the same organ (colon/cecum) as the approved indication, which likely explains the very high similarity score assigned by the TxGNN knowledge-graph model. However, villous adenoma is a benign, pre-malignant colonic polyp, and the standard of care is endoscopic or surgical resection — not cytotoxic chemotherapy. There is no established biological rationale for using a cytotoxic-agent-potentiating drug to treat a benign lesion; the connection appears to be an artifact of anatomical co-location within the knowledge graph rather than a genuine pharmacological relationship. The Evidence Pack's own rationale explicitly flags this pairing as lacking treatment logic.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

Tipiracil (as a standalone entity) currently has no EU marketing authorizations on record; the trifluridine/tipiracil combination product is separately authorized under its own combination-product license, which is not captured in this dataset.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine-class antimetabolite combination; tipiracil itself is a pharmacokinetic enhancer, not directly cytotoxic) |
| Myelosuppression Risk | High — literature on the trifluridine/tipiracil combination reports leukopenia and neutropenia as common adverse effects |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (particularly for neutropenia), renal and hepatic function |
| Handling Protection | Must follow cytotoxic drug handling regulations, as this agent is administered only as part of a cytotoxic chemotherapy combination |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite an extremely high TxGNN prediction score, this candidate has zero supporting clinical trials or literature (Evidence Level L5), and the target indication — a benign colonic polyp typically managed by resection — is mechanistically inconsistent with a cytotoxic chemotherapy potentiator. The prediction likely reflects anatomical co-location in the knowledge graph rather than a genuine pharmacological signal.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for tipiracil (currently a Data Gap, DG002)
- TFDA/EMA-approved label warnings and contraindications (currently a Blocking Data Gap, DG001) before any safety evaluation can begin
- Preclinical or mechanistic evidence demonstrating a plausible rationale for chemotherapy use in a benign adenoma, if this candidate is to be pursued further
- Clarification of whether "villous adenoma" in the source ontology could represent a malignant-transformation subset, which would materially change the risk-benefit assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

