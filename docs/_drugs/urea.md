---
layout: default
title: Urea
parent: High Evidence (L1-L2)
nav_order: 628
evidence_level: L2
indication_count: 10
---

# Urea
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Urea: From No EU-Approved Indication to Dermatitis

## One-Sentence Summary

Urea (carbamide, DrugBank DB03904) currently holds no EU marketing authorization and has no recorded approved indication in this Evidence Pack.
The TxGNN model predicts it may be effective for **Dermatitis**, and while a broader search returned 50 registered trials under this disease term, only **6 trials specifically study urea-based creams** (mainly for radiodermatitis and chemotherapy-induced hand-foot skin reactions); **no dedicated literature** was identified for this specific drug-indication pair.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — Urea has no EU marketing authorization as a standalone medicinal product in this Evidence Pack |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 98.21% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for urea in this Evidence Pack. Based on general pharmacological knowledge, urea is a small-molecule keratolytic and humectant that hydrates the stratum corneum and reduces hyperkeratosis when applied topically — properties widely exploited in dermatological creams. This established topical activity offers a plausible mechanistic basis for a knowledge-graph association with dermatitis, even though urea does not carry a formal EU-wide marketing authorization as a standalone product.

Because no original indication is on record for this compound, the TxGNN prediction here is not an extrapolation from a known approved use, but a direct knowledge-graph inference. Independent support comes from real-world clinical practice: several completed and ongoing trials use urea-based creams specifically to prevent or treat radiodermatitis (skin inflammation from radiotherapy) and capecitabine-induced hand-foot skin reaction/palmar-plantar erythrodysesthesia — both of which are dermatitis-spectrum conditions. This convergence between the model's prediction and existing off-label/adjunctive clinical use lends independent plausibility to the prediction, though it falls short of confirming a formal therapeutic indication.

## Clinical Trial Evidence

*Note: the disease-level search returned 50 trials, but most investigate unrelated compounds (e.g., hydroxyurea, biologics, vaccines) captured only by keyword overlap. The table below lists the 6 trials that actually study urea-based formulations.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02247830](https://clinicaltrials.gov/study/NCT02247830) | Phase 3 | Completed | 48 | Compared chamomile recutita gel vs. urea-based cream for **prevention** of radiodermatitis in breast/head-and-neck cancer patients undergoing radiotherapy. |
| [NCT02251392](https://clinicaltrials.gov/study/NCT02251392) | Phase 3 | Unknown | 100 | Evaluated chamomile gel, chamomile infusion, and urea cream for **treatment** of established radiodermatitis in breast/head-and-neck cancer patients. |
| [NCT02249884](https://clinicaltrials.gov/study/NCT02249884) | Phase 2 | Completed | 30 | Dose-response study establishing the safe/tolerable dose of chamomile gel and urea cream for radiodermatitis prevention and treatment. |
| [NCT05641246](https://clinicaltrials.gov/study/NCT05641246) | Phase 2 | Completed | 86 | Urea-based cream (Carbamide) combined with topical diclofenac reduced hand-foot syndrome incidence and improved quality of life in capecitabine-treated breast cancer patients. |
| [NCT05348278](https://clinicaltrials.gov/study/NCT05348278) | Phase 2/3 | Unknown | 214 | RCT testing urea-based cream to prevent capecitabine-associated hand-foot skin reactions, following prior positive data with sorafenib. |
| [NCT05939726](https://clinicaltrials.gov/study/NCT05939726) | N/A | Completed | 145 | Three-arm trial comparing moisturizing cream with/without vitamin E concentrate added to urea-based cream, versus urea-based cream alone, for capecitabine-associated palmar-plantar erythrodysesthesia. |

## Literature Evidence

Currently no related literature available.

## Safety Considerations

No detailed safety warnings, contraindications, or drug interaction data were available in the evidence pack for urea in this indication (all queries returned empty or "not found"). This is flagged as a **blocking data gap** (DG001: TFDA/EU label warnings and contraindications not yet obtained) that must be resolved before any safety review can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Six completed or ongoing trials specifically testing urea-based creams for radiodermatitis and chemotherapy-induced hand-foot skin reactions, together with a high TxGNN score, support L2-level plausibility for a dermatitis association. However, urea has no EU marketing authorization, no confirmed mechanism-of-action record, and a blocking gap in safety/label data — so a Go decision cannot be justified yet.

**To proceed, the following is needed:**
- TFDA/EU label warnings and contraindications for urea (blocking gap DG001)
- Mechanism of action confirmation via DrugBank (gap DG002)
- Clarification of intended route/formulation (topical vs. systemic) and whether it matches available dosage forms
- Re-screening of the 50 dermatitis-tagged trials to remove unrelated compounds (e.g., hydroxyurea, biologics) from future evidence updates
- A dedicated literature search specific to "urea cream dermatitis" rather than relying on the broader disease-term query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

