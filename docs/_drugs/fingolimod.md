---
layout: default
title: Fingolimod
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Fingolimod
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

# Fingolimod: From Multiple Sclerosis to Borderline Ovarian Serous Tumor

## One-Sentence Summary

Fingolimod (marketed originally as Gilenya) is a sphingosine-1-phosphate (S1P) receptor modulator used for relapsing multiple sclerosis. The TxGNN model's top-ranked prediction for this drug is **Borderline Ovarian Serous Tumor**, but this specific candidate is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph score with no direct clinical or literature backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (relapsing forms) — not found in the supplied regulatory license data |
| Predicted New Indication | Borderline Ovarian Serous Tumor |
| TxGNN Prediction Score | 94.94% |
| Evidence Level | L5 |
| Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on publicly known pharmacology, fingolimod is a sphingosine-1-phosphate receptor 1 (S1P1) modulator that causes internalization of S1P1 on lymphocytes, sequestering them in lymph nodes — its approved mechanism for multiple sclerosis is immunomodulatory, not antineoplastic.

The TxGNN score for borderline ovarian serous tumor derives purely from knowledge-graph embedding similarity — this node shares graph neighborhood structure with other ovarian tumor nodes rather than reflecting any direct trial or literature signal. Separately, the fingolimod analogue FTY720 has documented preclinical anti-tumor activity in **malignant** ovarian cancer cell lines and xenografts (via SphK1/S1P pathway inhibition), but that evidence pool attaches to other nodes in this same prediction set (ranks 5 and 8: "serous neoplasm" and "ovarian benign neoplasm"), not to the top-ranked borderline serous tumor entity itself. Borderline (low malignant potential) serous tumors have a distinct biology from the malignant epithelial ovarian cancer cell lines studied in the existing FTY720 literature, so mechanistic extrapolation to this specific entity is currently unsupported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

*Note: within this same prediction batch, related ovarian-tumor nodes have some preclinical support — "serous neoplasm" (1 paper, PMID 30120964) and "ovarian benign neoplasm" (8 papers, evidence level L4) — but none of that literature is attached to the top-ranked borderline serous tumor candidate reported here, and the "ovarian benign neoplasm" literature set actually studies malignant epithelial ovarian cancer models, suggesting a possible TxGNN node-labeling mismatch worth clarifying before further action.*

## Market Information

Fingolimod has no marketing authorization on record in this jurisdiction (market status: not marketed; 0 authorizations), so no license table is available.

## Safety Considerations

Please refer to the SmPC for safety information. (TFDA label warnings/contraindications are an unresolved Blocking data gap — DG001 — and must be obtained before any safety evaluation can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (borderline ovarian serous tumor) is supported only by knowledge-graph similarity, with zero clinical trials or publications; combined with an unresolved Blocking safety data gap (TFDA warnings/contraindications), this candidate does not meet the bar to proceed to safety screening (S1).

**To proceed, the following is needed:**
- TFDA label PDF (warnings, contraindications) — resolves DG001, currently Blocking
- Confirmed mechanism-of-action data from DrugBank — resolves DG002
- Direct preclinical or clinical evidence specific to borderline (low malignant potential) serous tumors, rather than extrapolation from malignant epithelial ovarian cancer models
- Clarification of the TxGNN node mapping for "ovarian benign neoplasm" (rank 8), since its attached literature describes malignant cell lines/xenografts — if that node is more accurately "ovarian cancer," it is a stronger candidate (L4, Research Question) than the current top-ranked, evidence-free node
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

