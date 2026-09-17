---
layout: default
title: Rufinamide
parent: AI Predictions (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
---

# Rufinamide
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

Using the drug-repurposing evidence pack as the sole source, per top-ranked prediction (`predicted_indications[0]`).

---

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome (FIRES)

## One-Sentence Summary

> Rufinamide is a triazole-derivative sodium-channel blocking anticonvulsant, historically used as adjunctive therapy for **Lennox-Gastaut syndrome (LGS)**.
> The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**,
> but currently **no clinical trials** and **no literature** in this evidence pack support this specific direction — the prediction is model-generated only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no EU marketing authorization on file); historically approved as adjunctive treatment for Lennox-Gastaut syndrome (LGS), per background literature cited elsewhere in this pack |
| Predicted New Indication | Febrile Infection-Related Epilepsy Syndrome (FIRES) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form for this evidence pack (flagged as a High-severity data gap, DG002). Based on the literature retrieved elsewhere in this pack, rufinamide is understood to prolong the inactive state of voltage-gated Na⁺ channels, producing a membrane-stabilizing, broad-spectrum antiseizure effect. It is not chemically related to other marketed antiepileptics and is best known as an adjunctive therapy for Lennox-Gastaut syndrome (LGS), a severe childhood-onset developmental and epileptic encephalopathy.

FIRES is an extremely refractory epileptic encephalopathy that follows a febrile illness and is thought to be driven substantially by neuroinflammatory mechanisms rather than a classical channelopathy. The evidence pack's own mechanistic rationale for this pairing is explicit that the link is theoretical: rufinamide's Na⁺-channel mechanism is extrapolated by class analogy (broad-spectrum antiepileptic drug) rather than by any FIRES-specific pharmacology, and no clinical or preclinical data currently exist to confirm or refute it.

Because this is a pure knowledge-graph association with no corroborating trial or publication evidence, it should be treated as a research hypothesis only, not as a basis for clinical action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (FIRES) is evidence level L5 (model prediction only, decision stage S0) — there is no clinical trial or literature evidence in this pack to support the drug-disease pairing, and the drug's own regulatory/safety profile is undocumented here (0 EU authorizations on file).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): TFDA/SmPC warnings and contraindications must be sourced before any S1 safety screening can begin
- Resolve DG002 (High): Structured mechanism of action data from DrugBank, to validate or refute the Na⁺-channel rationale for FIRES
- Preclinical or case-level evidence specifically in FIRES (not general LGS/refractory-epilepsy data) before advancing past S0
- Confirmation of current EU marketing/licensing status, since this pack shows 0 active authorizations

**Note for reviewers:** This pack contains 10 ranked candidates for rufinamide. Rank 8, *childhood onset epileptic encephalopathy*, is functionally continuous with the drug's already-established LGS indication and carries **L1 evidence** (systematic reviews, meta-analyses, and Phase III trial data) with a **Proceed with Guardrails** recommendation — it is a label-adjacent reconfirmation rather than a novel repurposing signal, but is worth separate evaluation if the goal includes indication-expansion documentation rather than genuinely new use cases.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

