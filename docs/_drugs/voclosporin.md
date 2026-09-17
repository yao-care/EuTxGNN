---
layout: default
title: Voclosporin
parent: AI Predictions (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Voclosporin
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

# Voclosporin: From Lupus Nephritis to Primary Release Disorder of Platelets

## One-Sentence Summary

Voclosporin is a next-generation calcineurin inhibitor whose established immunosuppressive use is in lupus nephritis, though it currently holds no marketing authorization in the EU. The TxGNN model's top prediction is **Primary Release Disorder of Platelets**, a congenital platelet granule secretion defect — but this association is currently supported by **zero clinical trials** and **zero publications**, and even the model's own mechanistic rationale flags it as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lupus Nephritis (established from pivotal trial evidence in the pack; not covered by any EU marketing authorization) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 95.42% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Voclosporin is a next-generation calcineurin inhibitor. It blocks the calcineurin–NFAT signaling pathway, preventing dephosphorylation of Nuclear Factor of Activated T-cells and subsequent transcription of IL-2, which in turn suppresses T-cell activation. This mechanism underlies its established immunosuppressive role in autoimmune disease, most notably lupus nephritis, where it has been evaluated in large randomized controlled trials (see AURORA and AURA-LV data referenced elsewhere in this evidence pack).

Primary release disorder of platelets, however, is a structural/biochemical platelet defect — an inherited impairment of platelet granule secretion — rather than an immune-mediated disease. There is no established biological pathway connecting calcineurin–NFAT-driven T-cell suppression to platelet granule release mechanisms, so the pharmacological rationale linking voclosporin's known mode of action to this new indication is weak.

The evidence pack's own mechanistic assessment is explicit on this point: while cyclosporine-class agents have occasionally been reported to affect platelet function, this is not a mainstream or well-characterized pharmacological effect, and the TxGNN association appears to reflect a statistical pattern in the knowledge graph rather than a mechanistically grounded hypothesis. This prediction should be treated as exploratory only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Voclosporin currently holds no marketing authorization in the EU (0 licenses on record), so no EU product/dosage-form information is available.

## Safety Considerations

Structured safety data (key warnings, contraindications, and drug–drug interactions) are not currently available in this evidence pack, and this gap is flagged as **Blocking severity** — meaning a formal safety pre-assessment (S1) cannot proceed until label-level information (e.g., warnings and contraindications from an approved product label such as the US FDA Lupkynis label, since no EU SmPC exists) is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (primary release disorder of platelets) has no supporting clinical trials or literature and evidence level L5, and the model's own rationale states there is no established mechanistic link between calcineurin inhibition and platelet granule secretion disorders. Combined with the absence of any EU marketing authorization and a Blocking-severity safety data gap, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: obtain full label-level safety data (warnings, contraindications) from a jurisdiction where voclosporin is approved, since no EU SmPC exists
- Obtain formal, sourced mechanism-of-action documentation (e.g., via DrugBank API) rather than relying on narrative rationale text
- Preclinical or mechanistic studies specifically testing calcineurin inhibition in platelet granule secretion disorders, if this indication is to be pursued at all
- Consider re-ranking candidates: within this same evidence pack, "dermatitis" (rank 4) reached a higher evidence tier (L4/S1, "Research Question") on the strength of two literature reviews discussing off-label systemic calcineurin inhibitor use in dermatologic disease, and may be a more tractable candidate for further evaluation
- Audit the underlying KG disease-node mapping — the pack itself notes that trial evidence attached to another candidate ("exanthem," rank 6) actually corresponds to lupus nephritis trials, indicating a labeling/mapping quality issue that may also affect other entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

