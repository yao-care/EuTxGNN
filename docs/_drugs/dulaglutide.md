---
layout: default
title: Dulaglutide
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Dulaglutide
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

# Dulaglutide: From Glycemic Control (Type 2 Diabetes) to Opsismodysplasia

## One-Sentence Summary

Dulaglutide is a GLP-1 receptor agonist used clinically for glycemic control (original indication data and formal MOA are currently gaps in this dataset). The TxGNN model's top-ranked prediction suggests possible activity in **Opsismodysplasia**, a rare skeletal dysplasia, but this candidate has **0 clinical trials** and **0 publications** — and the evidence pack's own mechanistic analysis flags the biological link as implausible. This is one of **10 AI-only (L5) predictions** in the pack, none of which currently have any supporting real-world evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (drug not marketed under the reviewed jurisdiction). Rationale text across all 10 candidates consistently references glycemic control / incretin effect, consistent with Dulaglutide's known use in Type 2 Diabetes — but no formal indication record exists here |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this candidate (flagged as a High-severity data gap, DG002). Based on the information embedded in this evidence pack's own rationale text, Dulaglutide is understood to act as a GLP-1 receptor agonist that regulates blood glucose through incretin effects — consistent with its known real-world use in glycemic control.

Unlike a typical repurposing candidate, however, the mechanistic case here is weak rather than reasonable. Opsismodysplasia is a congenital skeletal dysplasia caused by *INPPL1* mutations — a structural developmental disorder with no known relationship to GLP-1 receptor signaling, glucose regulation, or incretin biology. The evidence pack's own rationale explicitly states this link "lacks mechanistic plausibility" and attributes the high TxGNN score to indirect graph proximity between "rare disease" and "metabolic drug" nodes rather than genuine biological reasoning.

This pattern repeats across the other 9 top-ranked candidates in this pack: several (focal stiff limb syndrome, classic stiff person syndrome, thiamine-responsive dysfunction syndrome, pancreatic agenesis, and four distinct lipodystrophy syndromes) show similarly high scores with rationale text that self-flags weak or absent mechanistic grounding, no clinical trials, and no literature. Only the lowest-ranked candidate (autoimmune oophoritis, score 69.6%) shows a materially lower model confidence, but it too lacks any supporting evidence. Taken together, this evidence pack should be read as a screening-stage output requiring substantial follow-up before any of the 10 candidates can be considered credible repurposing leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Dulaglutide currently has no market authorization records in this dataset (market status: **Not Marketed**, 0 authorizations on file). No license table can be generated.

---

## Other AI-Predicted Candidates in This Evidence Pack

For completeness, all 10 candidates supplied in this evidence pack are AI-prediction-only (L5) with no clinical trial or literature support, and all carry a "Hold" recommendation at decision stage S0:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Plausibility (per rationale) |
|------|----------------------|-------------|-------------------------------------------|
| 1 | Opsismodysplasia | 97.05% | Implausible — no known GLP-1 pathway link |
| 2 | Focal stiff limb syndrome | 97.05% | Implausible — GAD65 autoimmune mechanism unrelated |
| 3 | Classic stiff person syndrome | 97.05% | Weak — theoretical anti-inflammatory link only |
| 4 | Thiamine-responsive dysfunction syndrome | 96.81% | Implausible — distinct metabolic/genetic pathway |
| 5 | Drug-induced localized lipodystrophy | 95.62% | Weak — GLP-1 agents are associated with this as an adverse effect, not a treatment |
| 6 | Pancreatic agenesis | 95.55% | Implausible — structural/developmental defect, not reversible pharmacologically |
| 7 | Centrifugal lipodystrophy | 95.37% | Implausible — no mechanistic evidence |
| 8 | Pressure-induced localized lipoatrophy | 95.29% | Implausible — likely graph clustering artifact across lipodystrophy nodes |
| 9 | Idiopathic localized lipodystrophy | 94.99% | Implausible — same clustering pattern as above |
| 10 | Autoimmune oophoritis | 69.57% | Weakest of the set — no mechanistic link, notably lower model confidence |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this evidence pack are Evidence Level L5 (AI prediction only), with zero supporting clinical trials or literature across every candidate. The pack's own mechanistic rationale text explicitly rates most of these links as biologically implausible or graph-artifact-driven rather than genuinely mechanistic, and the top candidate (Opsismodysplasia) is a congenital structural disorder with no plausible connection to GLP-1 receptor biology.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (DG001, Blocking — currently prevents any S1 safety screening)
- Confirmed mechanism of action from DrugBank or primary literature (DG002, High)
- Independent preclinical or mechanistic studies for any candidate before further evaluation, particularly to explain the apparent graph-clustering effect across the multiple lipodystrophy-related predictions
- Formal original indication and regulatory licensing data, currently absent from this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

