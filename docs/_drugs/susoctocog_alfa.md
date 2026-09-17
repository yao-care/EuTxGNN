---
layout: default
title: Susoctocog Alfa
parent: AI Predictions (L5)
nav_order: 559
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog Alfa: From Acquired Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Susoctocog alfa (marketed elsewhere as Obizur) is a recombinant, B-domain-deleted porcine-sequence antihemophilic factor VIII (FVIII) product used to control bleeding episodes in adults with Acquired Hemophilia A (AHA). The TxGNN model's top-ranked prediction suggests potential efficacy in **Primary Release Disorder of Platelets**, but this candidate is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review finds no pharmacological basis linking platelet granule release defects to FVIII replacement therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acquired Hemophilia A (AHA) — inferred from the collected literature/trial evidence, since the formal indication field and EU licensing data are currently empty |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap. Based on information extracted from the collected literature (e.g. PMID 27098420), susoctocog alfa is a recombinant, B-domain-deleted, porcine-sequence antihemophilic factor VIII product with low cross-reactivity to anti-human FVIII antibodies, which restores functional FVIII activity in patients whose endogenous FVIII is neutralized by autoantibodies — this is the pharmacological basis for its approved use in AHA.

Primary Release Disorder of Platelets, by contrast, is a platelet dense/alpha-granule secretion defect: platelets are present in normal numbers and can adhere and aggregate, but fail to release their granule contents properly during activation. This is mechanistically unrelated to plasma FVIII levels, which act downstream in the coagulation cascade rather than at the platelet-granule level.

The evidence pack's own mechanistic rationale for this candidate states explicitly that there is no direct mechanistic link between platelet granule release dysfunction and FVIII deficiency, and that FVIII supplementation does not affect platelet granule release function. No clinical trial or literature evidence currently supports this candidate — the high TxGNN score most likely reflects semantic clustering of "bleeding/coagulation" concepts within the knowledge graph rather than genuine pharmacological relevance. Notably, among the 10 TxGNN-predicted indications for this drug, only ranks #4 ("hemophilia") and #5 ("acquired coagulation factor deficiency") have any supporting literature — and the evidence pack itself notes these substantially overlap with the drug's already-known AHA indication rather than representing a genuinely new repurposing opportunity. The remaining candidates (ranks 1–3 and 6–10, including Glanzmann thrombasthenia, pseudo-von Willebrand disease, Scott syndrome, congenital FXIII deficiency, and adenosine deaminase deficiency) are all flagged in the rationale as mechanistically implausible and unsupported by any trial or publication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN assigns a very high prediction score (99.94%) to Primary Release Disorder of Platelets, but there is no mechanistic rationale, no clinical trial, and no published literature connecting FVIII replacement therapy to platelet granule release disorders — consistent with a knowledge-graph embedding artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications for susoctocog alfa (blocking data gap — required before any S1 safety pre-assessment)
- Detailed mechanism-of-action data from DrugBank (High-severity data gap affecting mechanistic-link analysis)
- Preclinical or in vitro evidence establishing any relationship between FVIII activity and platelet granule release, before any further investment in this specific candidate
- If repurposing interest persists, re-examine rank #5 ("acquired coagulation factor deficiency", L3 evidence) — though note this largely overlaps with the drug's already-recognized AHA indication rather than representing a distinct new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

