---
layout: default
title: Perflutren
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Perflutren
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

Using no additional skill — this is a direct content-generation task fully specified by the provided template; proceeding straight to the report.

# Perflutren: From Ultrasound Contrast Agent to Acute Intermittent Porphyria

## One-Sentence Summary

Perflutren is an octafluoropropane-filled lipid microsphere used as an intravascular ultrasound contrast agent (no marketed therapeutic indication is on file in this dataset). The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria**, but currently **0 clinical trials** and **0 publications** support this direction — this is a pure knowledge-graph correlation with no clinical or mechanistic backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no marketing authorization exists in this jurisdiction. Based on the evidence pack's own descriptions, Perflutren is used as an inert-gas microbubble ultrasound contrast agent for echocardiographic imaging, not as a treatment for a specific disease |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 97.47% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Perflutren is not available in DrugBank (flagged as a High-severity data gap, DG002). Based on the descriptions embedded in the evidence pack itself, Perflutren is an octafluoropropane gas encapsulated in a lipid microsphere shell. It has no known pharmacological or metabolic activity — it works purely through differential acoustic reflectivity, enhancing ultrasound signal for diagnostic imaging (e.g., myocardial contrast echocardiography, left ventricular opacification, endocardial border delineation).

There is no known or plausible biological pathway connecting an inert imaging agent to porphyrin metabolism or heme biosynthesis, the pathway underlying acute intermittent porphyria. The evidence pack's own rationale is explicit on this point: "no clinical trials, literature, or known MOA support this association... Perflutren has no metabolic pharmacological activity and no known relationship to porphyrin metabolism pathways. This is purely a TxGNN graph-based correlation."

It is worth noting that other, lower-ranked candidates in this pack (myocardial ischemia, rank 4; coronary artery disease, rank 7) do carry substantial clinical trial and literature evidence (L4). However, that evidence entirely reflects Perflutren's established role as a diagnostic contrast agent for myocardial perfusion imaging and sonothrombolysis research — not a genuine therapeutic repurposing signal. None of the ten predicted indications in this pack, including the top-ranked Acute Intermittent Porphyria, have supporting evidence of an actual treatment effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Perflutren currently holds no marketing authorization in this jurisdiction (0 licenses on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this pack. TFDA/EMA label warnings and contraindications are a Blocking-severity gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Acute Intermittent Porphyria) has zero clinical trials, zero publications, and no known mechanistic pathway connecting it to Perflutren — it is a pure TxGNN graph correlation (L5, decision stage S0). In addition, a Blocking-severity data gap (missing TFDA/EMA label warnings and contraindications) prevents this candidate from even entering a basic safety review (S1).

**To proceed, the following is needed:**
- TFDA/EMA official label (SmPC) warnings and contraindications — required to clear the S1 safety gate (Blocking, DG001)
- Drug mechanism of action (MOA) data from DrugBank (High priority, DG002)
- Preclinical or mechanistic rationale establishing any biological link between Perflutren and porphyrin/heme metabolism before this candidate can advance beyond S0
- If pursuing other candidates in this pack (e.g., myocardial ischemia, coronary artery disease), clarify that existing evidence reflects diagnostic imaging use only, not a validated therapeutic repurposing signal, before treating them as viable candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

