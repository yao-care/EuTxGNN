---
layout: default
title: Bortezomib
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Bortezomib
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

# Bortezomib: From Multiple Myeloma to Vertebral Anomalies and Variable Endocrine and T-cell Dysfunction

## One-Sentence Summary

Bortezomib (Velcade) is a first-in-class proteasome inhibitor, globally approved for the treatment of multiple myeloma and mantle cell lymphoma, but not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Vertebral Anomalies and Variable Endocrine and T-cell Dysfunction**, with a prediction score of 96.10%; however, **no clinical trials or published literature** currently support this specific indication.
It is worth noting that the model simultaneously predicts strong activity across several other haematological and paediatric cancers — including neuroblastoma (4 clinical trials, 20 publications), Hodgkin's lymphoma, and myeloid leukemia — where substantially more evidence exists.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma; mantle cell lymphoma (globally approved; not registered in Taiwan) |
| Predicted New Indication | Vertebral Anomalies and Variable Endocrine and T-cell Dysfunction |
| TxGNN Prediction Score | 96.10% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, the formal mechanism of action data (MOA) was not retrieved in this evidence pack. Based on extensive descriptions in the retrieved literature, however, bortezomib is a highly selective and reversible inhibitor of the 26S proteasome — the principal intracellular machinery for targeted protein degradation. By blocking proteasomal activity, bortezomib causes accumulation of pro-apoptotic proteins (such as Bik, Bim, NOXA, and PUMA), suppresses the constitutively active NF-κB pathway, and induces endoplasmic reticulum stress, collectively driving tumour cell death. Its approved indications — plasma cell myeloma and B-cell lymphoma — are both highly dependent on proteasome function for proliferation and survival.

The predicted indication, vertebral anomalies and variable endocrine and T-cell dysfunction, is a rare, complex multi-system disorder affecting bone structure, endocrine organs, and T-lymphocyte function. The TxGNN model generates this prediction through network-level graph relationships within the biological knowledge graph, potentially linking proteasome regulation to immune cell homeostasis or skeletal morphogenesis pathways. The NF-κB signalling axis — a primary target of bortezomib — is known to participate in both T-cell development and bone remodelling (via RANK/RANKL regulation), which may provide an indirect mechanistic rationale.

That said, no direct preclinical or clinical evidence supports this specific repurposing. The prediction should be interpreted as a hypothesis-generating signal rather than a clinically actionable finding. In contrast, for paediatric neuroblastoma and haematological malignancies (Hodgkin's lymphoma, AML, NHL), the same evidence pack contains multiple completed clinical trials and extensive mechanistic literature, representing far stronger repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bortezomib in Vertebral Anomalies and Variable Endocrine and T-cell Dysfunction.

---

## Literature Evidence

Currently no related literature available for Bortezomib in Vertebral Anomalies and Variable Endocrine and T-cell Dysfunction.

---

## Taiwan Market Information

Bortezomib is currently not registered in Taiwan (未上市). No marketing authorizations are on file in the Taiwan FDA database. The drug is, however, approved internationally — including by the US FDA and EMA — for multiple myeloma and mantle cell lymphoma under the brand name Velcade.

---

## Cytotoxicity

Bortezomib is an antineoplastic agent (proteasome inhibitor) used in the treatment of haematological malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Proteasome inhibitor (first-in-class boronic acid dipeptide; not conventional cytotoxic) |
| Myelosuppression Risk | Moderate — thrombocytopenia is dose-limiting and frequently observed; neutropenia and anaemia also reported in combination regimens |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (particularly platelet count before each cycle), peripheral neuropathy grading (NCI CTCAE), liver function tests, renal function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations; subcutaneous administration preferred to reduce systemic exposure on administration staff |

---

## Safety Considerations

Formal warning and contraindication data from the Taiwan package insert were not retrieved in this evidence pack (Data Gap — see DG001). Based on the international SmPC and literature:

- **Key Warning**: Peripheral neuropathy is a significant and cumulative toxicity; subcutaneous administration substantially reduces incidence compared to intravenous infusion
- **Key Warning**: Thrombocytopenia is common and nadir typically occurs on Day 11 of each cycle; platelet count must be monitored before each dose

For comprehensive safety guidance, please refer to the international SmPC (EMA or US FDA label) until the Taiwan TFDA package insert can be retrieved and reviewed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (96.10%) for bortezomib in vertebral anomalies and variable endocrine and T-cell dysfunction, zero clinical trials and zero publications support this specific indication. The mechanistic link between proteasome inhibition and this rare multi-system disorder remains entirely speculative, and pursuing a development programme without even preclinical evidence would not be justifiable at this stage.

**To proceed, the following is needed:**

- Preclinical mechanistic study confirming that proteasome inhibition modulates the pathological pathway(s) underlying this condition (e.g., NF-κB in T-cell homeostasis; RANK/RANKL in vertebral development)
- At least one published case report or preclinical in vitro/in vivo study demonstrating bortezomib activity in this disease model
- Retrieval of the Taiwan TFDA package insert (DG001 remediation) to complete the safety review before any clinical translation
- Formal MOA documentation from DrugBank (DG002 remediation)
- Drug-drug interaction assessment for the relevant patient population
- Consultation with rare disease specialists to clarify disease pathophysiology and patient population size

> **Alternative recommendation**: Consider prioritising the neuroblastoma indication (TxGNN rank 4, score 95.11%) for deeper evaluation. Four clinical trials — including two completed Phase 1/2 studies specifically testing bortezomib in relapsed/refractory neuroblastoma — and 20 publications, including multiple mechanistic in vitro and in vivo studies, provide an L3–L4 evidence base that is far more actionable.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

