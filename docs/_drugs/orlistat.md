---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
---

# Orlistat
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

Using the drug-repurposing-report skill implicitly (following the v5 template structure as instructed) to produce the report below.

# Orlistat: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

> Orlistat is a gastrointestinal lipase inhibitor best known as an anti-obesity/weight-management agent (formal original-indication text was not available in this evidence pack).
> The TxGNN model's top-ranked prediction suggests possible relevance to **Hypervitaminosis** (fat-soluble vitamin excess),
> but this candidate currently has **0 clinical trials** and **0 publications** supporting it — the prediction is model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not reported in evidence pack (regulatory license data unavailable; orlistat is pharmacologically known as an anti-obesity/weight-loss agent per the rationale narrative) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation is not available in this evidence pack (flagged as data gap DG002, severity High). Based on known pharmacology referenced in the model's rationale, orlistat inhibits gastric and pancreatic lipase, blocking roughly one-third of dietary triglyceride hydrolysis and absorption — the basis for its established use as an anti-obesity/weight-management agent.

The link to the predicted indication is indirect: by reducing dietary fat absorption, orlistat also reduces absorption of fat-soluble vitamins (A, D, E, K). This is normally documented as an **adverse effect** (vitamin deficiency) of orlistat therapy. The TxGNN prediction essentially inverts this relationship, proposing that the same mechanism could theoretically be leveraged to *lower* excess fat-soluble vitamin concentrations in hypervitaminosis.

This is a plausible direction mechanistically, but it is a speculative extrapolation of a known side effect rather than a validated therapeutic pathway — there are no clinical trials, case reports, or preclinical studies in the evidence pack examining orlistat for this purpose. The prediction should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations recorded for orlistat in this evidence pack (market status: **Not Marketed**, total authorizations: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: key warnings, contraindications, and drug-interaction data were not available in this evidence pack. This is flagged as a **Blocking** data gap (DG001 — TFDA label warnings/contraindications), meaning safety review (S1 stage) cannot proceed until this is resolved.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Hypervitaminosis) is an L5, model-only prediction with zero supporting clinical trials or literature. Its mechanistic rationale inverts a known adverse effect of orlistat (vitamin malabsorption) rather than resting on a validated therapeutic pathway, and no original-indication or MOA documentation is available to anchor the comparison. A Blocking data gap on TFDA safety labeling (DG001) also prevents this candidate from advancing to S1 safety review.

**To proceed, the following is needed:**
- Formal MOA documentation from DrugBank (DG002, High severity)
- TFDA label warnings/contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Preclinical or case-based evidence specifically evaluating orlistat in fat-soluble vitamin excess states
- **Separate consideration recommended**: the evidence pack's rank-8 candidate, *fatty liver disease / NAFLD*, has substantially stronger support (7 clinical trials including 2 completed Phase 4 trials, and 20+ publications including RCTs and a 2024 systematic review/meta-analysis of RCTs). This candidate was not the top-ranked prediction but appears far better evidenced and may warrant its own dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

