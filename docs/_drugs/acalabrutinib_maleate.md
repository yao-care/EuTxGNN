---
layout: default
title: Acalabrutinib Maleate
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 0
---

# Acalabrutinib Maleate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Acalabrutinib Maleate: Drug Repurposing Evaluation Report

---

## One-Sentence Summary

Acalabrutinib maleate is a second-generation BTK (Bruton's Tyrosine Kinase) inhibitor, currently not marketed in Taiwan, with no recorded approvals in the local regulatory database.
This Evidence Pack contains **no TxGNN-predicted indications** and is missing critical baseline data including mechanism of action details and safety information.
As a result, a full repurposing evaluation **cannot be completed** with the current data — this report serves as a gap assessment and readiness checklist.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack |
| Predicted New Indication | None — TxGNN predictions not available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no predictions generated) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Predictions Are Unavailable

The Evidence Pack returned an empty `predicted_indications` array, which indicates the TxGNN prediction pipeline was not completed for this candidate. Two likely causes:

1. **Missing DrugBank ID**: The `drugbank_id` field is null, which means the drug could not be matched to a node in the TxGNN knowledge graph. Without a valid DrugBank entry, neither the Knowledge Graph (KG) method nor the Deep Learning (DL) method can generate repurposing candidates.

2. **Incomplete data inputs**: The `inputs_received` field in the metadata is empty (`[]`), confirming that the pipeline did not receive the necessary input files to run predictions.

Acalabrutinib maleate is the maleate salt form of acalabrutinib (brand name: Calquence, AstraZeneca). The free base form may already exist in DrugBank under a separate entry. Resolving the DrugBank mapping is the single most critical step to unlock TxGNN predictions for this drug.

---

## Taiwan Market Information

| Item | Content |
|------|---------|
| Market Status | Not marketed in Taiwan |
| Total Licenses | 0 |
| Dosage Forms | No records |

No TFDA marketing authorizations were found for acalabrutinib maleate. The drug may be available through compassionate use or clinical trial access in Taiwan, but this is not reflected in the current Evidence Pack.

---

## Safety Considerations

No safety data is available in this Evidence Pack. Please refer to the prescribing information (SmPC or USPI for Calquence) for:

- Haemorrhage risk (major bleeding events)
- Atrial fibrillation / atrial flutter
- Infections (including opportunistic infections)
- Cytopenias
- Second primary malignancies
- Drug interactions via CYP3A pathway

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective BTK inhibitor (kinase inhibitor class) |
| Myelosuppression Risk | Moderate (neutropenia, anaemia, and thrombocytopenia reported) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, hepatic function, cardiac monitoring (ECG for AF), bleeding assessment |
| Handling Protection | Handle per institutional cytotoxic drug handling protocols for oral targeted agents |

*Note: Classification is based on drug class knowledge. Formal toxicity data was not available in the Evidence Pack.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is critically incomplete — no DrugBank ID, no TxGNN predictions, no safety records, and no regulatory authorizations. A repurposing evaluation cannot be responsibly conducted without resolving these foundational data gaps.

**To proceed, the following is needed:**

- [ ] **Resolve DrugBank ID**: Search DrugBank for "acalabrutinib" (free base, DB12493) and confirm whether the maleate salt maps to the same node; update `drugbank_id` in the candidate record
- [ ] **Re-run TxGNN pipeline**: With a valid DrugBank ID, re-execute both the KG and DL prediction modules to generate repurposing candidates
- [ ] **Retrieve TFDA prescribing information**: Download and parse the SmPC/仿單 PDF from the TFDA website to populate safety warnings and contraindications (Data Gap DG001 — Blocking)
- [ ] **Retrieve mechanism of action**: Query the DrugBank API for MOA, pharmacodynamics, and pharmacokinetics data (Data Gap DG002 — High)
- [ ] **Check EU / FDA approvals**: Acalabrutinib holds FDA approval for CLL/SLL and MCL; confirm whether EMA authorization exists and populate regulatory context accordingly
- [ ] **Re-generate Evidence Pack**: Once the above inputs are resolved, re-run the full evidence collection pipeline (ClinicalTrials.gov + PubMed) against the top TxGNN-predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

