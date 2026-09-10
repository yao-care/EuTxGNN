---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
---

# Nintedanib
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

# Nintedanib: From Idiopathic Pulmonary Fibrosis to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

> Nintedanib is a triple angiokinase inhibitor whose established use is in fibrotic and certain oncology indications (idiopathic pulmonary fibrosis, and combination oncology use elsewhere).
> The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
> with **0 clinical trials** and **1 supporting publication** currently available in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (referenced within evidence pack's mechanistic rationale; not formally documented via TW license data) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 |
| Market Status (Taiwan) | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The drug's formal `original_moa` field is marked as a data gap in this evidence pack. However, the repurposing rationale documented alongside the top prediction describes Nintedanib as a **triple angiokinase inhibitor targeting VEGFR, FGFR, and PDGFRα/β**. This mechanistic detail, while not captured in the structured MOA field, is directly sourced from the evidence pack and can be used to assess biological plausibility.

DFSP is a tumor with a well-characterized molecular driver: the **COL1A1-PDGFB fusion gene**, which causes constitutive activation of PDGFRB. This makes DFSP a textbook example of a PDGFR-addicted tumor — a fact already validated in clinical practice, since **imatinib (a PDGFR inhibitor) is the established standard-of-care systemic therapy for DFSP**. Nintedanib's inhibitory activity against PDGFRα/β therefore provides a mechanistically coherent rationale for testing it in this same molecular context, even though direct clinical evidence in DFSP is currently absent.

That said, the connection to Nintedanib's own approved use (a fibrotic lung disease) is indirect — the shared thread is pathway biology (PDGFR/FGFR signaling in fibroblast/pericyte proliferation), not disease similarity. This is a mechanism-driven hypothesis rather than an indication-adjacency hypothesis, which is consistent with the L4 evidence classification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors in oncology; supports PDGFR as a druggable target in PDGFR-driven neoplasms, providing indirect mechanistic support rather than direct evidence for Nintedanib in DFSP. |

---

## EU Market Information

No marketing authorizations currently on file for Nintedanib in this jurisdiction (0 licenses; market status: **Not Marketed**). Regulatory/label data must be sourced separately (see Data Gap DG001 below) before any safety review can proceed.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> ⚠️ Note: This evidence pack flags the absence of TFDA label warnings/contraindications as a **Blocking** data gap (DG001) — this must be resolved before Stage 1 (S1) safety screening can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (PDGFR inhibition in a COL1A1-PDGFB fusion-driven tumor, with imatinib as clinical precedent) is biologically plausible, but evidence is currently limited to a single review article with no direct clinical trials in DFSP. Combined with a **Blocking** safety data gap (no TFDA label/contraindication data available), the candidate cannot yet advance past the research-question stage.

**To proceed, the following is needed:**
- TFDA-equivalent label data (warnings, contraindications) to complete S1 safety screening (DG001)
- Confirmed DrugBank MOA record to formally validate the mechanistic linkage (DG002)
- Preclinical or case-level evidence of Nintedanib activity in PDGFR-driven sarcomas (e.g., DFSP, fibrosarcoma) before considering translational/clinical follow-up
- Continued literature/trial monitoring, as current evidence level (L4) reflects mechanism-only support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

