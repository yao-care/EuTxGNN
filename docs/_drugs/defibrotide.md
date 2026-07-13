---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease to Pseudo-von Willebrand Disease

## One-Sentence Summary

Defibrotide is a polydeoxyribonucleotide sodium compound with established use in the treatment and prevention of hepatic veno-occlusive disease (VOD/SOS) in patients undergoing hematopoietic stem cell transplantation (HSCT).
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**,
with **no clinical trials** and **no publications** currently supporting this direction.
This is the highest-ranked prediction (score 99.91%), though analysis suggests it likely reflects a knowledge graph generalization signal rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatic veno-occlusive disease / sinusoidal obstruction syndrome (VOD/SOS) in HSCT patients (inferred from clinical trial context; no formal license data available) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (0 authorizations on record) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Defibrotide is a polydeoxyribonucleotide sodium compound whose efficacy in hepatic VOD/SOS has been established through clinical trials, including a completed Phase 3 study (NCT02851407, n=372). Its pharmacological profile encompasses anti-thrombotic, profibrinolytic, anti-inflammatory, and endothelial-protective effects — including inhibition of platelet-activating factor (PAF), promotion of prostacyclin (PGI₂) and tissue plasminogen activator (t-PA) production, and downregulation of endothelial adhesion molecules.

Pseudo-von Willebrand disease (Pseudo-vWD, also called platelet-type vWD) is caused by gain-of-function mutations in platelet glycoprotein GPIbα. These mutations cause spontaneous binding of ultra-large von Willebrand factor (vWF) multimers to platelets, leading to platelet consumption and a bleeding phenotype paradoxically resembling vWD. In theory, Defibrotide's anti-platelet aggregation and profibrinolytic activities could interfere with pathological vWF-platelet interactions at the GPIbα binding site. However, this mechanistic connection is highly indirect — there is no known direct pharmacological action of Defibrotide on GPIbα or vWF multimer dynamics.

The TxGNN model's high score (99.91%) for this prediction most likely reflects shared nodes within the hemostasis and vWF pathway in the underlying knowledge graph, rather than disease-specific biological relevance. No clinical or preclinical studies have examined Defibrotide in Pseudo-vWD. This prediction should be treated as a **knowledge graph generalization artifact (false positive signal)** and does not currently warrant clinical investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Defibrotide in pseudo-von Willebrand disease.

> **Note:** A completed Phase 3 trial of Defibrotide exists for its established indication (NCT02851407, VOD/SOS prevention, n=372), which provides a robust safety profile for cross-indication reference but is not directly relevant to this predicted indication.

---

## Literature Evidence

Currently no related literature available for Defibrotide in pseudo-von Willebrand disease.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> No key warnings, contraindications, or drug interaction data were available in this evidence pack. TFDA prescribing information (仿單) has not yet been retrieved and should be consulted before any clinical evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting Defibrotide's use in pseudo-von Willebrand disease, and the mechanistic link between Defibrotide's endothelial/anti-thrombotic pharmacology and the GPIbα gain-of-function pathology underlying Pseudo-vWD is indirect and biologically unvalidated. The TxGNN high score is attributed to non-specific knowledge graph connectivity within the hemostasis pathway rather than disease-specific relevance.

**To proceed, the following is needed:**
- Retrieve Defibrotide MOA data from DrugBank API (Data Gap DG002) to confirm or refute mechanistic relevance
- Retrieve TFDA prescribing information / SmPC (Data Gap DG001) for baseline safety characterization before any S1 evaluation
- Confirm EU/Taiwan market authorization status for Defibrotide (Defitelio®) — formal regulatory data was absent in this evidence pack
- Consider deprioritizing Pseudo-vWD and instead directing resources toward **thrombotic thrombocytopenic purpura (TTP, rank 4, L3 evidence)** or **thrombocytopenic purpura (rank 10, L3 evidence)**, both of which have multiple published case series and mechanistic studies linking Defibrotide's endothelial-protective profile to the microvascular pathology involved — though a bidirectional safety signal (one case report of TTP onset *following* Defibrotide therapy, PMID 7896218) requires careful S1 evaluation before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

