---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: From Ovarian Cancer to Epiglottis Neoplasm

## One-Sentence Summary

> Niraparib is a PARP1/2 inhibitor, referenced in trial records as FDA-approved for maintenance treatment of recurrent epithelial ovarian, fallopian tube, and primary peritoneal cancer.
> The TxGNN model predicts it may be effective for **Epiglottis Neoplasm**,
> but currently **no clinical trials** and **no publications** support this specific direction — the prediction is based solely on knowledge-graph embedding similarity.

> ⚠️ Note: The drug is not yet marketed in Taiwan (0 licenses on file), and official Taiwan label data (warnings/contraindications) and DrugBank MOA data are flagged as data gaps in this evidence pack (DG001, DG002).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (maintenance therapy, recurrent epithelial ovarian/fallopian tube/peritoneal cancer) — derived from trial-record context; official Taiwan label text not yet available |
| Predicted New Indication | Epiglottis Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as data gap DG002). Based on information embedded in the accompanying evidence records, niraparib is a **PARP1/2 inhibitor** that exploits synthetic lethality in tumors with homologous recombination deficiency (HRD), most notably BRCA-mutated or HRD-positive gynecologic cancers (ovarian, endometrial serous carcinoma).

The predicted new indication — epiglottis neoplasm, a head and neck tumor — has no established connection to HRD/BRCA biology in the literature or trials reviewed here. The rationale text accompanying this prediction itself states that this is a pure knowledge-graph embedding signal, "without any clinical or mechanistic data supporting a specific link" to head and neck (epiglottic) tumors.

For context, a related prediction in this same evidence pack (**cystic neoplasm**, rank 2, score 99.99%) is far better supported — it maps largely onto ovarian and endometrial serous carcinoma, where niraparib already has Phase 2 trial and literature support. This suggests the model's embedding space is picking up genuine oncology-adjacent signal in some outputs, but for epiglottis neoplasm specifically, no such supporting evidence currently exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No marketing authorization records are currently on file for niraparib in Taiwan (0 licenses; market status: 未上市 / Not Marketed).

---

## Cytotoxicity

Niraparib is an antineoplastic agent (PARP1/2 inhibitor; oncology use referenced throughout the trial evidence in this pack), so cytotoxicity information is included below.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP1/2 inhibitor; synthetic lethality mechanism) |
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
The prediction score is high, but there is zero clinical trial or literature evidence directly supporting niraparib's use in epiglottis neoplasm — a tumor type with no established HRD/PARP-inhibitor biology. Combined with the drug's unmarketed status in Taiwan and outstanding blocking data gaps (label warnings, MOA), this candidate is not ready to advance.

**To proceed, the following is needed:**
- TFDA label/仿單 data (warnings and contraindications) — currently a Blocking gap (DG001)
- Confirmed DrugBank mechanism of action data — currently a High-severity gap (DG002)
- Preclinical or mechanistic studies establishing a rationale for PARP inhibition in epiglottic/laryngeal tumors specifically
- Consider re-scoping the review toward **cystic neoplasm** (rank 2 in this pack), which has substantially stronger evidence (L2, Phase 2 RCT enrolling, 9 supporting publications) and maps onto niraparib's known gynecologic-oncology profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

