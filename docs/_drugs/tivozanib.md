---
layout: default
title: Tivozanib
parent: AI Predictions (L5)
nav_order: 600
evidence_level: L5
indication_count: 10
---

# Tivozanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tivozanib: From Renal Cell Carcinoma to Endocervical Carcinoma

## One-Sentence Summary

Tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor, established as an anti-angiogenic therapy for renal cell carcinoma. The TxGNN model predicts it may be effective for **Endocervical Carcinoma**, but this prediction is currently supported by **no registered clinical trials** and **no published literature** — it rests entirely on a class-effect mechanistic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (based on general pharmacological knowledge; not recorded in the current evidence pack) |
| Predicted New Indication | Endocervical Carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (`original_moa: [Data Gap]`). Based on the mechanistic annotation attached to the top prediction, tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor with anti-angiogenic activity, a mechanism class well established in oncology.

Cervical (endocervical) carcinoma is a tumour type with known dependence on tumour angiogenesis, and anti-angiogenic agents such as bevacizumab already have demonstrated clinical benefit in cervical cancer. This creates a plausible class-effect rationale: if VEGF-pathway inhibition benefits cervical cancer as a class, a potent VEGFR TKI like tivozanib could theoretically extend to this setting.

However, this rationale is explicitly described in the evidence pack itself as a class-level hypothesis rather than drug-specific evidence — "tivozanib itself has no direct evidence in this indication." The same TxGNN run also surfaced nine additional, extremely rare cervical/uterine adenocarcinoma subtypes (ranks 2–10, scores 99.76–99.80%) using similarly indirect class-analogy reasoning (e.g., comparison to ovarian serous carcinoma or endometrial carcinoma response to other anti-angiogenic TKIs). None of these tumour types have any tivozanib-specific clinical or literature data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations are recorded in the current evidence pack. Tivozanib is listed as **not marketed** in the EU dataset used to generate this report, with zero authorizations on file.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR-1/2/3 tyrosine kinase inhibitor, anti-angiogenic) |
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
This prediction is supported only by a TxGNN computational score (L5, no clinical trials, no literature) and a class-effect mechanistic hypothesis that is explicitly not drug-specific. Combined with the missing safety data (marked as a Blocking data gap for TFDA-equivalent warnings/contraindications) and the drug's "not marketed" EU status, there is currently no basis to advance this indication beyond hypothesis stage.

**To proceed, the following is needed:**
- Official SmPC/labeling data (warnings, contraindications, DDI) to clear the Blocking safety data gap
- Confirmed mechanism of action documentation from DrugBank or equivalent source
- At minimum, preclinical or case-level evidence directly linking tivozanib to cervical/endocervical carcinoma before considering trial design
- Clarification of tivozanib's actual EU regulatory status, since "not marketed" in this dataset should be cross-checked against known authorizations (e.g., Fotivda)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

