---
layout: default
title: Tecovirimat
parent: AI Predictions (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# Tecovirimat
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

# Tecovirimat: From Orthopoxvirus Infection to Hordeolum

## One-Sentence Summary

Tecovirimat is an antiviral agent whose known mechanism specifically targets the VP37 envelope-wrapping protein of orthopoxviruses (variola/smallpox, mpox, vaccinia), and it has established clinical use in the treatment of these infections. The TxGNN model predicts a possible new indication for **Hordeolum** (an acute bacterial infection of the eyelid), but this candidate is supported only by a computational score (**score-based ranking only, no confirming trials or publications**), and the drug's own mechanism of action provides no plausible pathway to a bacterial eyelid infection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smallpox / Mpox (orthopoxvirus infections) — not confirmed in the EU regulatory dataset provided (no EU marketing authorization on record) |
| Predicted New Indication | Hordeolum |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is marked as a data gap in this Evidence Pack. However, the repurposing rationale accompanying the prediction independently describes Tecovirimat's known mechanism: it selectively inhibits the VP37 envelope-wrapping protein of orthopoxviruses, blocking viral envelopment and cell-to-cell/extracellular spread. This mechanism is active only against poxviruses (smallpox, mpox, vaccinia) and has no known activity against bacteria.

Hordeolum, however, is an acute bacterial infection of the meibomian or Zeis/Moll glands of the eyelid, most commonly caused by *Staphylococcus* species. There is no overlap between an antiviral, poxvirus-specific mechanism and the pathophysiology of a bacterial eyelid abscess. The relationship between the original indication (orthopoxvirus infection) and the predicted new indication (hordeolum) is therefore not mechanistically supported.

This appears to be a case where the TxGNN knowledge-graph embedding produced a high similarity score without an underlying biological rationale — a known limitation of purely graph-based repurposing predictions in the absence of confirmatory clinical or literature evidence. The Evidence Pack's own scoring explicitly reflects this: Evidence Level L5, decision stage S0, and a recommendation of Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Tecovirimat currently has no marketing authorization on record in the EU dataset provided (`total_licenses: 0`, market status: **Not marketed**). No authorization table can be generated.

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are marked as blocking data gaps in this Evidence Pack — specifically, TFDA/EU label warnings and contraindications have not yet been retrieved, which is flagged as a blocking issue for any safety pre-assessment.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (hordeolum) has no supporting clinical trials or literature (Evidence Level L5), and the drug's known antiviral, poxvirus-specific mechanism provides no plausible biological pathway to a bacterial eyelid infection. In addition, this drug is not currently marketed in the EU dataset, and safety labelling data (warnings/contraindications) remains an unresolved blocking data gap.

**To proceed, the following is needed:**
- Retrieval of the TFDA/EU product label (SmPC) to resolve the blocking safety data gap (warnings, contraindications)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source
- Independent mechanistic or preclinical evidence linking VP37 inhibition (or any other Tecovirimat activity) to bacterial eyelid infection, before this candidate can advance past S0
- Given that all top-10 TxGNN predictions for this drug (hordeolum, vibrio infection, Klebsiella infection, noma, E. coli infection, Newcastle disease, herpes, equine infectious anemia, Astroviridae infection, Arterivirus infection) show the same pattern — high score, no mechanistic plausibility, no confirmatory evidence — this candidate bundle should be treated as a low-priority screening artifact rather than a near-term repurposing opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

