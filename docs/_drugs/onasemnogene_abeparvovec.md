---
layout: default
title: Onasemnogene Abeparvovec
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
---

# Onasemnogene Abeparvovec
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

# Onasemnogene Abeparvovec: From Spinal Muscular Atrophy to Bronchitis

## One-Sentence Summary

> Onasemnogene abeparvovec is an AAV9-vector gene therapy originally developed to treat **spinal muscular atrophy (SMA)** by delivering a functional *SMN1* gene to motor neurons.
> The TxGNN model predicts a possible association with **Bronchitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it should be treated as an unvalidated model signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal Muscular Atrophy (SMA) — not formally captured in structured regulatory data; drug is not EU/TW-licensed |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 86.13% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the information available in this evidence pack, onasemnogene abeparvovec is an AAV9 (adeno-associated virus serotype 9) vector-based gene therapy that delivers a functional copy of the *SMN1* gene to motor neurons, replacing the survival motor neuron protein deficient in SMA patients. Its efficacy in SMA is well established, but this mechanism is specific to motor neuron protein replacement and has no known pharmacological pathway relevant to airway inflammation or infection.

The TxGNN model assigned bronchitis a relatively high similarity score (86.13%), but the underlying evidence pack explicitly flags this as likely reflecting a **secondary clinical association** rather than a direct treatment effect — SMA patients frequently develop respiratory complications (including bronchitis) as a disease sequela, which may create a spurious knowledge-graph link between the drug and this comorbid condition rather than indicating a true therapeutic effect.

Given the absence of any supporting clinical trials or literature, and the lack of a plausible direct mechanistic link, this prediction should be interpreted as **low-confidence model noise** rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorizations were found for onasemnogene abeparvovec in this evidence pack (market status: **not marketed**, total authorizations: **0**). No approved product/indication text is available for comparison.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction (Bronchitis, TxGNN score 86.13%) is supported by zero clinical trials and zero publications, and the drug's known mechanism (AAV9-mediated *SMN1* gene delivery to motor neurons) has no established biological pathway relevant to bronchitis. The evidence pack itself assesses this as a likely knowledge-graph artifact reflecting SMA-associated respiratory comorbidity rather than a direct treatment effect. All 10 TxGNN-predicted indications for this drug (including diabetic retinopathy, bronchial neoplasm, and testicular tumor) are similarly rated L5/Hold with no supporting clinical or literature evidence — none currently warrant further investment.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) documentation from DrugBank/manufacturer (Data Gap DG002)
- TFDA/EMA label warnings and contraindications (Data Gap DG001 — currently blocking safety pre-screening)
- A biologically plausible mechanistic hypothesis linking AAV9/*SMN1* gene therapy to airway/bronchial pathology before any evidence-collection effort is justified
- If pursued, targeted literature and clinical trial searches specifically for "onasemnogene abeparvovec" AND respiratory outcomes in SMA populations (to distinguish true signal from comorbidity confounding)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

