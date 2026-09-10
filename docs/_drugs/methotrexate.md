---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Antimetabolite Chemotherapy to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate (DrugBank DB00563) is a folate-antagonist antimetabolite long used across oncology (leukemia, lymphoma, sarcoma), transplant-related immunosuppression, and rheumatologic disease, though a formally documented original indication is not available in this dataset. The TxGNN model's top-ranked prediction for this drug is **Pulmonary Blastoma**, with a prediction score of **99.45%**, but currently **0 clinical trials** and **0 publications** directly support this specific indication — the prediction rests on algorithmic inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory data (drug not marketed in this jurisdiction; no license records) |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information from the broader evidence collected across this drug's other predicted-indication branches, methotrexate is a dihydrofolate reductase (DHFR) inhibitor that blocks purine/pyrimidine synthesis, exerting cytotoxic effects on rapidly dividing cells — a mechanism that underlies its established roles in hematologic malignancy, sarcoma chemotherapy, GVHD prophylaxis, and rheumatologic immunosuppression.

Pulmonary blastoma is a rare, aggressive biphasic lung tumor containing both epithelial and rapidly dividing mesenchymal/sarcomatous elements. The model's rationale is that methotrexate's broad-spectrum cytotoxicity against rapidly dividing sarcoma- or blastoma-like tissue components could theoretically extend to this tumor type. However, this remains a purely mechanistic hypothesis — no direct clinical trial or published case evidence for methotrexate in pulmonary blastoma exists in the current evidence base.

It is worth noting that other lower-ranked predictions for this drug (e.g., small cell lung carcinoma, rhabdomyosarcoma, Hodgkin lymphoma) are supported by substantially stronger evidence (L2, Phase II trial data), which stands in contrast to the top-ranked but evidence-poor prediction discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Methotrexate is currently **not marketed** in this jurisdiction (market status: 未上市), and no marketing authorization records are available in this dataset (0 total licenses).

---

## Cytotoxicity

Methotrexate is a classical antimetabolite chemotherapy agent and is evaluated here as an antineoplastic drug.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite / antifolate — DHFR inhibitor) |
| Myelosuppression Risk | High — bone marrow suppression is a well-recognized, dose-dependent toxicity, particularly with high-dose regimens |
| Emetogenicity Classification | Low to Moderate (dose-dependent; high-dose IV regimens carry moderate emetogenic risk) |
| Monitoring Items | CBC with differential, renal function (critical for MTX clearance), liver function, serum MTX levels for high-dose regimens, folate/leucovorin rescue status |
| Handling Protection | Yes — must follow cytotoxic drug handling regulations as an antineoplastic agent |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug interaction data are not currently available for this drug in this dataset — flagged as a Blocking-severity data gap requiring TFDA/regulatory label retrieval before any safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pulmonary blastoma, TxGNN score 99.45%) has no supporting clinical trials or literature — it is evidence level L5, model prediction only. Combined with the absence of MOA data and safety/label data, this candidate does not meet the threshold to advance beyond a research hypothesis stage.

**To proceed, the following is needed:**
- Resolve blocking data gap: retrieve TFDA/regional product label (warnings, contraindications) before any safety pre-assessment (S1)
- Resolve MOA data gap via DrugBank API query to support mechanistic-relevance analysis
- Generate or identify preclinical/case-level evidence specific to methotrexate in pulmonary blastoma before considering research-question status
- Given the sparse evidence for this top-ranked indication, consider directing further evaluation toward this drug's other predicted indications with stronger existing evidence (e.g., small cell lung carcinoma, rhabdomyosarcoma, Hodgkin lymphoma — all L2, Proceed with Guardrails), which may represent more actionable repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

