---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Irbesartan is an Angiotensin II Type 1 Receptor Blocker (ARB) with established pharmacological use in hypertension and diabetic nephropathy, acting by inhibiting Angiotensin II-mediated renal vasoconstriction and fibrosis.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** (score: 99.31%),
with **no registered clinical trials** and **no disease-specific publications** currently identified for this indication — though mechanistic evidence from related ARB approvals provides biological plausibility at Level L4.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Diabetic Nephropathy (FDA-approved; not registered in Taiwan) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold — Pending S1 Safety Assessment |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Irbesartan selectively blocks the Angiotensin II Type 1 Receptor (AT1R), the primary effector receptor of the renin-angiotensin system (RAS). By blocking AT1R, Irbesartan inhibits Angiotensin II-driven renal afferent and efferent arteriolar constriction, reducing intraglomerular hypertension. It also suppresses aldosterone secretion, reduces proteinuria, and exerts direct antifibrotic effects on the renal parenchyma. Irbesartan has received FDA approval for nephropathy in type 2 diabetic patients, establishing its class-level renal-protective efficacy.

Malignant hypertensive renal disease (accelerated hypertensive nephropathy) shares its core pathophysiology with the conditions where ARBs are already proven effective: severe Angiotensin II-driven renal microvascular damage, fibrinoid necrosis of arterioles, and progressive glomerulosclerosis. The pathological axis — RAS overactivation → AT1R stimulation → glomerular hypertension → nephrosclerosis — is precisely the target of Irbesartan's mechanism. This mechanistic alignment explains why TxGNN assigns a high prediction score and why the scoring system classifies this as an L4 (mechanism-supported) rather than a purely model-speculative (L5) candidate.

One critical safety constraint must be acknowledged upfront: in patients with bilateral renal artery stenosis (or stenosis of a solitary functioning kidney), ARB-mediated efferent arteriolar dilation may precipitate acute kidney injury (AKI). This risk is particularly relevant in the malignant hypertension setting, where renovascular disease may coexist. Full S1 safety stratification — including bilateral renal artery stenosis exclusion — is a prerequisite before any clinical development can proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Taiwan Market Information

Irbesartan is currently **not marketed in Taiwan** with no authorizations on record. No product license data is available for review.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Critical mechanistic safety alert (from repurposing rationale):** Based on known ARB pharmacology and the proposed indication, use of Irbesartan in patients with bilateral renal artery stenosis carries a documented risk of acute kidney injury. This must be addressed as part of the S1 safety assessment before clinical development.

---

## Conclusion and Next Steps

**Decision: Hold — Pending S1 Safety Assessment**

**Rationale:**
Irbesartan's AT1R-blocking mechanism is directly aligned with the pathophysiology of malignant hypertensive renal disease, and its FDA-approved renal-protective precedent in diabetic nephropathy provides a credible mechanistic bridge. However, the complete absence of direct clinical trials and disease-specific literature, combined with an unresolved bilateral renal artery stenosis safety flag, prevents advancement beyond Hold until the S1 gate is cleared.

**To proceed, the following is needed:**
- **S1 Safety Stratification**: Define explicit exclusion criteria for bilateral renal artery stenosis (and single-kidney with ipsilateral stenosis) in any clinical protocol
- **MOA Data Retrieval**: Query DrugBank API for full Irbesartan mechanism of action, targets, and known off-target effects (Data Gap DG002)
- **Taiwan SmPC Review**: Download and parse the TFDA product insert PDF to extract warnings and contraindications (Data Gap DG001 — currently Blocking)
- **Targeted Literature Search**: Conduct a focused PubMed/Embase search specifically for "Irbesartan OR ARB AND malignant hypertensive nephropathy" to confirm the evidence gap and capture any case reports or mechanistic studies missed in the current query
- **Preclinical Evidence Gap**: Design or identify an animal model study of malignant hypertensive nephropathy with ARB treatment to upgrade evidence from L4 toward L3 before requesting investigator-initiated trial consideration
- **Regulatory Pathway Check**: Assess whether existing FDA diabetic nephropathy labeling can be leveraged as supportive bridging evidence for a Taiwan IND application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

