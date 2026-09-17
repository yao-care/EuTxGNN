---
layout: default
title: Sparsentan
parent: AI Predictions (L5)
nav_order: 553
evidence_level: L5
indication_count: 10
---

# Sparsentan
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

# Sparsentan: From IgA Nephropathy to Predicted Alopecia

## One-Sentence Summary

Sparsentan is a dual endothelin type A (ETA) / angiotensin II type 1 (AT1) receptor antagonist (DEARA), known in clinical practice for reducing proteinuria in primary IgA nephropathy — though this original indication is not recorded in the current Evidence Pack.
The TxGNN model predicts it may be effective for **Alopecia**, but this is currently supported by **0 clinical trials** and **0 publications** — the signal comes purely from knowledge-graph embedding similarity, and the drug's own repurposing rationale describes the mechanistic link as "weak, with no known direct pathway."

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in this Evidence Pack (`original_indications` is empty; drug is not EU-marketed). Based on known pharmacology, Sparsentan is a DEARA developed for primary IgA nephropathy |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 94.52% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the Evidence Pack (flagged as data gap DG002). Based on known information, Sparsentan is a dual ETA/AT1 receptor antagonist (DEARA class); its ability to reduce proteinuria in primary IgA nephropathy is well established in clinical use, but this original-indication context is not captured in the structured data supplied here, and the drug currently holds no EU marketing authorization (0 licenses).

The relationship between the original indication (a proteinuric kidney disease driven by endothelin/angiotensin-mediated vascular and glomerular effects) and the predicted new indication (alopecia, a hair-follicle growth-cycle disorder) is not mechanistically obvious. The evidence pack's own rationale text states explicitly that there is "no known direct pathway between ETA/AT1 antagonism and hair follicle growth-cycle regulation," and that the signal is "inferred solely from knowledge-graph embedding similarity, with weak mechanistic support." In other words, the model has found a statistical association in the graph, not a biologically grounded hypothesis.

It is also worth noting that this candidate is one of ten AI-generated predictions for Sparsentan, and several of the lower-ranked ones (angioedema, potassium deficiency, fetal erythroblastosis) are flagged in the rationale text as likely **inverted signals** — i.e., the model may be capturing known *adverse effects* of AT1-antagonist pharmacology (angioedema risk, hyperkalemia, pregnancy contraindication/fetal toxicity) rather than genuine therapeutic opportunities. This pattern suggests the overall prediction set for this drug should be treated with added caution rather than as a curated shortlist of therapeutic hypotheses.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Sparsentan currently holds **0 EU marketing authorizations** (`total_licenses: 0`, `market_status: Not marketed/Not marketed`). No product records are available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information (`safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all unavailable in this Evidence Pack; DG001 flags TFDA label warnings/contraindications as a **Blocking** data gap for safety triage).

**Class-related signals noted in the prediction set (not sourced from a formal safety database, but embedded in the rationale text of other ranked predictions for this drug):**
- Rank 5 (angioedema) and rank 8 (potassium deficiency/hyperkalemia) rationales note that AT1-antagonist-class drugs are clinically known to *cause*, not treat, these conditions — a possible inverted graph signal.
- Rank 10 (fetal erythroblastosis) rationale flags that ARB-class agents are contraindicated in pregnancy due to fetal toxicity — a serious safety consideration if this drug class is evaluated further for any indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications for Sparsentan are Evidence Level L5 (model prediction only — zero clinical trials, zero literature), the top-ranked alopecia hypothesis has an explicitly weak mechanistic basis per the model's own rationale text, and the drug has no EU marketing authorization. Critical safety data (TFDA label warnings/contraindications) is flagged as a **Blocking** data gap, and several other predictions in the same set appear to represent inverted/contradictory pharmacological signals rather than genuine indications — this further lowers confidence in the overall prediction batch.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/FDA label warnings and contraindications) before any S1 safety triage
- Resolve DG002 (confirmed mechanism of action and original indication, e.g., via DrugBank/FDA label for Filspari/IgA nephropathy)
- Preclinical or mechanistic evidence directly linking ETA/AT1 antagonism to hair follicle biology before pursuing the alopecia hypothesis
- Independent pharmacovigilance review of ranks 5, 8, and 10 to confirm whether they represent inverted safety signals rather than viable indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

