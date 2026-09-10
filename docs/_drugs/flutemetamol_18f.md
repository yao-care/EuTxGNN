---
layout: default
title: Flutemetamol 18F
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
---

# Flutemetamol 18F
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

# Flutemetamol (18F): From Alzheimer's Disease Diagnostic Imaging to Anaphylaxis

## One-Sentence Summary

Flutemetamol (18F) is a fluorine-18 labeled PET radiotracer used to visualize amyloid plaques in patients being evaluated for Alzheimer's disease — it is a **diagnostic imaging agent, not a therapeutic drug**. The TxGNN model predicts it may be "effective" for **Anaphylaxis**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic link as absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally licensed in this dataset; known use is amyloid-β PET imaging for suspected Alzheimer's disease (diagnostic, not therapeutic) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 98.79% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Flutemetamol (18F) (marked as a data gap in this evidence pack). Based on known information, Flutemetamol (18F) is a PET radiodiagnostic agent that binds amyloid-β plaques in the brain, used solely to support the visual assessment of amyloid pathology in patients undergoing Alzheimer's disease workup. It has no established pharmacodynamic role in immune or allergic pathways.

Amyloid-PET imaging and anaphylaxis belong to entirely different domains — one is a passive imaging biomarker tool, the other is an acute IgE-mediated (or non-IgE) hypersensitivity reaction. There is no structural, receptor-binding, or pathway-based rationale connecting the two. The evidence pack's own rationale field is explicit on this point: *"Flutemetamol (18F) is an amyloid PET imaging agent used for Alzheimer's disease diagnostic imaging, a non-therapeutic drug, with no known pharmacological MOA supporting a therapeutic mechanism related to anaphylaxis. The high TxGNN score reflects only knowledge-graph topological association, not mechanistic evidence."*

The most plausible real-world connection is the inverse of a repurposing signal: radiocontrast/PET tracer agents can occasionally *cause* hypersensitivity-type reactions as an adverse event, rather than treat them. This makes the prediction a likely artifact of knowledge-graph embedding proximity (e.g., shared nodes such as "IV administration," "PET imaging setting," or diagnostic co-occurrence with allergy-related conditions) rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Flutemetamol (18F) is currently **not marketed** in Taiwan under this dataset (0 licenses on record), so no product/dosage-form/indication table is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: This evidence pack flags TFDA label/warning data as a Blocking gap — DG001 — meaning a formal safety pre-screen (S1) cannot proceed until the package insert is retrieved and parsed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Flutemetamol (18F) is a non-therapeutic diagnostic radiotracer with no plausible mechanistic link to anaphylaxis (or to any of the other 9 predicted indications in this pack, which include dermatitis, dermatomyositis subtypes, and other unrelated conditions). All ten predictions are L5/S0 — model output only, with zero clinical trials and zero literature — and the evidence pack's own scoring already recommends "Hold" for every ranked candidate.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (currently a Blocking data gap, DG001)
- Verified mechanism of action data (currently a data gap, DG002)
- A domain-appropriate repurposing framework — since Flutemetamol (18F) is a diagnostic agent rather than a treatment, standard "old drug, new indication" repurposing logic may not apply, and this candidate should be reassessed for whether it belongs in this pipeline at all
- Independent mechanistic or preclinical rationale before any further investment in this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

