---
layout: default
title: Florbetaben 18F
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Florbetaben 18F
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Florbetaben (18F): From Beta-Amyloid PET Imaging to Migraine Disorder

## One-Sentence Summary

Florbetaben (18F) (DrugBank DB09148) is an F-18–labeled PET radiotracer used diagnostically to visualize beta-amyloid plaques in the brain; it has no recorded therapeutic indication and no EU marketing authorization on file. The TxGNN model's top prediction is **Migraine Disorder** (score 99.41%), but this candidate currently has **zero supporting clinical trials and zero literature**, and is classified as a pure AI-graph association (L5) with no mechanistic rationale. Across all 10 ranked candidates, the only trial/literature "hits" found were subsequently verified as database mismatches unrelated to Florbetaben.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — per evidence notes, used as a diagnostic F-18 PET beta-amyloid imaging agent (no therapeutic indication recorded) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (Data Gap DG002). Based on the information available in the evidence pack, Florbetaben (18F) is a microdose F-18–labeled PET diagnostic imaging agent that binds beta-amyloid plaques for visualization purposes; it has no systemic pharmacological activity at the doses used and no established therapeutic mechanism.

The repurposing rationale explicitly states there is no known connection between Florbetaben's imaging mechanism and migraine pathophysiology (vascular/trigeminovascular system, CGRP signaling) — the prediction is described as a pure knowledge-graph embedding association without mechanistic support. The same "no mechanistic basis" pattern holds across the other nine candidates (rheumatoid arthritis, pulmonary hypertension, Raynaud disease, etc.), none of which have any plausible pharmacological link to a diagnostic imaging tracer.

Notably, apparent supporting evidence found for lower-ranked candidates was investigated and found to be spurious: the one clinical trial linked to "headache disorder" (NCT03443973) is actually a Phase 3 trial of **Gantenerumab** (a different amyloid-targeting monoclonal antibody) for Alzheimer's disease, unrelated to Florbetaben or headache treatment. Similarly, the 20 literature hits linked to "migraine with or without aura, susceptibility to" are reviews on epilepsy/migraine comorbidity genetics that never mention Florbetaben — a keyword false-match. This substantially weakens confidence in the overall prediction set.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication (Migraine Disorder).

## Literature Evidence

Currently no related literature available for the top-ranked indication (Migraine Disorder).

## EU Market Information

No EU marketing authorizations are on file for Florbetaben (18F) — market status is "Not Marketed" with 0 recorded licenses.

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (DDI query status: not_found).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (Migraine Disorder) has no supporting clinical trials or literature and no mechanistic rationale — it is an L5, AI-graph-only association. Across the full candidate list, the only apparent trial/literature evidence was verified to be mismatched data (wrong drug or unrelated topic), and a blocking safety data gap (TFDA label unavailable) prevents even an initial S1 safety screen.

**To proceed, the following is needed:**
- TFDA product label (warnings/contraindications) — download and parse from TFDA official site (DG001, Blocking; required before any S1 safety evaluation)
- Confirmed mechanism of action from DrugBank API (DG002)
- Independent mechanistic or preclinical rationale connecting a beta-amyloid PET tracer to migraine pathophysiology before further evidence collection is warranted
- Real DDI/safety interaction data (current query returned no results)
- Re-verification of database linkage quality, given confirmed false-positive matches (e.g., Gantenerumab trial, unrelated epilepsy literature) elsewhere in this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

