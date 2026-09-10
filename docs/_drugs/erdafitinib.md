---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Erdafitinib
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

# Erdafitinib: From Urothelial Carcinoma to Pulmonary Hypertension

## One-Sentence Summary

> Erdafitinib is a pan-FGFR1-4 tyrosine kinase inhibitor internationally approved for FGFR-altered urothelial carcinoma (this drug is **not currently marketed in Taiwan**, so this original-indication context comes from general drug knowledge, not from the Taiwan regulatory dataset in this evidence pack).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a prediction score of **99.38%**,
> but currently **no clinical trials and no literature** support this specific prediction — it is a pure AI/knowledge-graph inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial carcinoma, FGFR3/2-altered (international label; not covered by Taiwan regulatory data in this pack) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for erdafitinib is not available in this evidence pack (flagged as a data gap, DG002 – High severity). Based on the knowledge-graph rationale attached to this candidate, erdafitinib is understood to be a **pan-FGFR1-4 tyrosine kinase inhibitor**, and this is partially corroborated by the one literature record retrieved for this drug (Roskoski 2020, PMID 31862477), which classifies it among small-molecule protein kinase inhibitors approved by the FDA in 2019.

The proposed link to pulmonary hypertension rests on the general biology of FGF/FGFR signaling in pulmonary vascular smooth muscle cell proliferation and vascular remodeling — a pathway implicated in pulmonary arterial hypertension pathophysiology, with some exploratory animal-model work on FGFR inhibition reversing vascular remodeling.

However, this connection is **indirect and inferential**. There is no clinical trial, no case report, and no mechanistic study directly linking erdafitinib to pulmonary hypertension in the evidence collected. The prediction should be treated as a knowledge-graph-generated hypothesis rather than an evidence-backed candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Erdafitinib is not marketed in Taiwan — 0 authorizations on record, no license entries available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (pan-FGFR1-4 small-molecule tyrosine kinase inhibitor, per Roskoski 2020 review of FDA-approved kinase inhibitors) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pulmonary hypertension) has no clinical trial or literature support — only an inferential knowledge-graph mechanistic link — placing it at evidence level L5. This is compounded by a Blocking data gap on TFDA label warnings/contraindications (DG001), which alone prevents any S1 safety pre-screening, and a High-severity gap on confirmed MOA (DG002).

Across all 10 predicted indications for this candidate, only rheumatoid arthritis (rank 4) has any literature hit, and that single reference (PMID 31862477) is a general kinase-inhibitor review with no RA-specific data, giving it evidence level L4 — still not sufficient for progression. No other candidate has any clinical or literature evidence.

**To proceed, the following is needed:**
- TFDA label/PDF (warnings, contraindications) to clear the Blocking data gap (DG001)
- Confirmed MOA via DrugBank API to resolve DG002
- Direct preclinical or clinical evidence of FGFR inhibition in pulmonary hypertension models
- Confirmation of Taiwan market-entry status before any further regulatory pathway assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

