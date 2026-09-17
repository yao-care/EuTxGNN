---
layout: default
title: Tasonermin
parent: AI Predictions (L5)
nav_order: 568
evidence_level: L5
indication_count: 10
---

# Tasonermin
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

# Tasonermin: From Soft Tissue Sarcoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Tasonermin (recombinant human TNF-alpha) is currently approved only for regional treatment of soft tissue sarcoma via isolated limb perfusion (ILP), due to severe systemic toxicity that precludes systemic administration.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure AI-generated hypothesis with no experimental or clinical validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft Tissue Sarcoma, treated via Isolated Limb Perfusion (ILP) — not captured in EU authorization records because the drug is not currently marketed in the EU |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available in this Evidence Pack (marked as a data gap). Based on the rationale accompanying the prediction, Tasonermin is a recombinant human TNF-alpha that exerts local antitumor activity by inducing apoptosis in tumor vascular endothelial cells and disrupting tumor microvasculature. Its only approved use is isolated limb perfusion (ILP) for soft tissue sarcoma of the limb — a delivery method specifically designed to confine the drug to the affected limb, because systemic TNF-alpha exposure causes severe toxicity, including shock and hepatotoxicity.

The relationship between the original indication (regionally-perfused limb sarcoma) and the predicted new indication (systemic urothelial carcinoma of the prostatic urethra) is mechanistically distant. Urothelial carcinoma is not a vascularized soft-tissue sarcoma amenable to limb perfusion, and there is no established precedent for systemic or intravesical TNF-alpha use in this tumor type. The knowledge-graph association likely reflects shared molecular features (e.g., angiogenesis pathways, TNF-alpha receptor expression) rather than a validated therapeutic mechanism.

Because Tasonermin's clinical utility is fundamentally constrained by its route of administration (ILP only, due to systemic toxicity), any proposed application to a non-perfusable, non-limb malignancy such as urothelial carcinoma would require an entirely different delivery strategy (e.g., intravesical instillation) that has not been evaluated. This is explicitly acknowledged in the Evidence Pack as a "speculative mechanistic link... lacking any supporting evidence."

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Cytotoxicity

Tasonermin is an antineoplastic biologic (recombinant human TNF-alpha) whose only approved indication — soft tissue sarcoma — is a malignancy, meeting the criteria for inclusion of this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy / cytokine-based antineoplastic (recombinant TNF-alpha), not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Not the primary dose-limiting toxicity; the dominant risk is systemic inflammatory/vascular toxicity (shock, capillary leak, hepatotoxicity) when TNF-alpha reaches systemic circulation, which is why administration is restricted to isolated limb perfusion |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Hepatic function, hemodynamic status (blood pressure, signs of shock), signs of cytokine release/systemic inflammatory response during and after perfusion |
| Handling Protection | Administration requires a specialized isolated limb perfusion circuit under hyperthermic conditions in an experienced surgical/oncology center; strict containment is required to prevent systemic leakage given the drug's narrow safety margin |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Tasonermin, including this top-ranked candidate, are Evidence Level L5 — pure model predictions with zero supporting clinical trials or literature. Combined with a **blocking data gap** (missing TFDA/EMA label warnings and contraindications, which prevents even an initial safety screen), and the drug's known systemic toxicity profile that restricts it to regional limb perfusion only, there is currently no basis to advance this candidate beyond the hypothesis stage.

**To proceed, the following is needed:**
- TFDA/EMA-equivalent labeling data (warnings, contraindications) to complete the S1 safety screen (Blocking gap DG001)
- Confirmed mechanism-of-action detail via DrugBank API query (High-priority gap DG002)
- Preclinical or mechanistic studies specifically evaluating TNF-alpha activity in urothelial carcinoma
- A defined route-of-administration strategy (e.g., intravesical) since the drug's only validated delivery method (isolated limb perfusion) is not applicable to this tumor type
- At minimum, in vitro or animal model evidence before any clinical exploration is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

