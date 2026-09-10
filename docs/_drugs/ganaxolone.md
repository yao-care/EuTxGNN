---
layout: default
title: Ganaxolone
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Ganaxolone
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

# Ganaxolone: From Epilepsy (Neurodevelopmental Seizure Disorders) to Alcohol Withdrawal Delirium

## One-Sentence Summary

Ganaxolone is a synthetic neuroactive steroid whose confirmed original indication is not present in this evidence pack (Taiwan market status: not marketed, 0 authorizations). The TxGNN model's top-ranked prediction is **Alcohol Withdrawal Delirium**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure mechanism-based extrapolation with no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan marketing authorization on record (evidence pack references epilepsy/neurodevelopmental seizure disorders in related rationale text, but this is not a confirmed regulatory indication) |
| Predicted New Indication | Alcohol Withdrawal Delirium |
| TxGNN Prediction Score | 94.85% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status (Taiwan) | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Ganaxolone is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information that is available, Ganaxolone is described in the evidence rationale as a synthetic neuroactive steroid acting as a **positive allosteric modulator (PAM) at the GABA-A receptor** — the same general receptor target used by benzodiazepines and barbiturates, the current standard-of-care drug classes for alcohol withdrawal management.

This shared receptor mechanism is the entire basis of the prediction: theoretically, GABA-A potentiation could suppress the central nervous system hyperexcitability that drives alcohol withdrawal delirium, in a manner analogous to benzodiazepine therapy. However, this rationale is explicitly described in the source data as **"pure mechanistic extrapolation"** — no clinical trial, case report, or preclinical study specific to alcohol withdrawal delirium exists to support it. The TxGNN score reflects the strength of the knowledge-graph relationship, not clinical validation.

It is worth noting that other, lower-ranked predictions in this same evidence pack for closely related conditions have meaningfully stronger support: **"alcohol withdrawal"** (rank 6) has L4 evidence including an animal pharmacogenetic study directly involving ganaxolone in ethanol withdrawal, and **"autism spectrum disorder"** (rank 7) has L3 evidence with 13 literature hits, including a direct ganaxolone behavioral study in an autism mouse model and clinical linkage through CDKL5-related epilepsy syndromes. These may be more productive candidates for further evaluation than the top-ranked but evidence-free prediction discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations on record. Ganaxolone's market status in Taiwan is "Not Marketed" with 0 total licenses/authorizations, so no product/dosage-form/indication table can be generated.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data were queried but not found in the available sources; the TFDA package insert data gap is classified as **Blocking** and must be resolved before any safety assessment can proceed — see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction (Alcohol Withdrawal Delirium) carries a high TxGNN score but zero clinical or literature evidence, and Ganaxolone has no marketing authorization or safety labeling on file in Taiwan. There is currently no basis to move this specific candidate past a mechanism-only hypothesis.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap
- Confirmed mechanism of action documentation for Ganaxolone — currently a High-severity data gap
- Any clinical or preclinical study specifically evaluating Ganaxolone in alcohol withdrawal delirium
- Consider redirecting evaluation effort to the higher-evidence candidates identified in the same evidence pack ("alcohol withdrawal," L4/S1; "autism spectrum disorder," L3/S1), which already carry a "Research Question" recommendation rather than "Hold"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

