---
layout: default
title: Mogamulizumab
parent: AI Predictions (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Mogamulizumab
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

> Mogamulizumab is an anti-CCR4 monoclonal antibody used for cutaneous T-cell lymphoma (CTCL) and Sézary syndrome.
> The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**,
> but currently **0 clinical trials** and **0 publications** support this direction — this is a pure model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in local regulatory data; based on known drug class information — Cutaneous T-cell lymphoma (CTCL) / Sézary syndrome |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Mogamulizumab is an anti-CCR4 monoclonal antibody that depletes CCR4-expressing regulatory T cells (Tregs) and malignant T cells; its efficacy in CTCL/Sézary syndrome is well established.

Urothelial carcinoma of the prostatic urethra has no known biological connection to CCR4 expression or T-cell lymphoma biology. According to the evidence pack's own rationale, the high TxGNN score most likely reflects indirect clustering of urinary-tract tumor nodes within the knowledge graph, rather than genuine pharmacological plausibility.

No clinical trial or literature evidence currently supports extending Mogamulizumab to this indication. This prediction should be treated as a hypothesis-generation signal only, not as a basis for clinical or regulatory action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Market Information

No marketing authorizations are currently registered for this drug in this market (market status: Not Marketed; 0 licenses on file).

---

## Cytotoxicity (Antineoplastic Drugs Only)

Mogamulizumab is an antineoplastic monoclonal antibody (approved for CTCL/Sézary syndrome, a lymphoid malignancy).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CCR4 monoclonal antibody; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Data not available in this evidence pack — mAbs targeting CCR4⁺ T cells typically carry lower classic myelosuppression risk than cytotoxic chemotherapy, but immune-related adverse events (infusion reactions, dermatologic toxicity, autoimmune effects) are class-relevant concerns |
| Emetogenicity Classification | Low (typical for monoclonal antibody therapy) |
| Monitoring Items | CBC, skin examination, infusion-reaction monitoring, signs of autoimmune/immune-related toxicity |
| Handling Protection | Standard IV biologic handling; special cytotoxic drug handling precautions are not typically required for this drug class |

Please refer to the SmPC warnings and precautions for confirmed toxicity data.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this is unsupported by any clinical trial or literature evidence, and the mechanistic link between anti-CCR4 activity and urothelial carcinoma is weak per the model's own rationale. Critical safety data (TFDA warnings/contraindications) and mechanism-of-action confirmation are also missing, blocking any safety pre-assessment (S1).

**To proceed, the following is needed:**
- TFDA/regulatory label data — warnings, contraindications (blocking gap, DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Prospective or at least preclinical/mechanistic evidence specifically linking CCR4 biology to urothelial carcinoma
- Continued literature monitoring is reasonable for two comparatively higher-plausibility candidates flagged in the evidence pack — **HHV8-related tumor** (rank 5, immune-evasion mechanism rationale) and **Richter syndrome** (rank 10, shared lymphoid malignancy class) — though both remain L5/Hold pending actual data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

