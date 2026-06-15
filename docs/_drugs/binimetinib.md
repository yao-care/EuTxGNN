---
layout: default
title: Binimetinib
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Binimetinib
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

# Binimetinib: From BRAF V600E/K Mutant Melanoma to Choroideremia

## One-Sentence Summary

Binimetinib is a MEK1/2 kinase inhibitor approved for use in combination with encorafenib for the treatment of adult patients with unresectable or metastatic melanoma harboring BRAF V600E/K mutations.
The TxGNN model predicts it may be effective for **Choroideremia** with a prediction score of **98.63%**,
however, there are currently **no clinical trials** and **no publications** supporting this direction, placing the evidence at Level 5 (AI model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BRAF V600E/K mutation-positive unresectable or metastatic melanoma (in combination with encorafenib) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known clinical information, Binimetinib is a selective inhibitor of MEK1 and MEK2 kinases — components of the RAS/MAPK (Rapidly Accelerated Fibrosarcoma/Mitogen-Activated Protein Kinase) signaling cascade. It is used in combination with the BRAF inhibitor encorafenib to suppress downstream ERK phosphorylation, thereby halting tumor cell proliferation in BRAF V600-mutant melanoma.

Choroideremia is an X-linked recessive hereditary retinal dystrophy caused by loss-of-function mutations in the CHM gene, which encodes Rab Escort Protein 1 (REP1). The disease mechanism centers on impaired Rab geranylgeranyl transferase (Rab-GGTase) activity, leading to failure of intracellular vesicular transport in retinal pigment epithelium and photoreceptors, and their subsequent progressive degeneration. This pathophysiology does not have a direct, established connection to the MEK-ERK signaling axis.

The high TxGNN prediction score likely reflects a distant, indirect association in the knowledge graph — possibly through shared retinal cell survival nodes — rather than a specific mechanistic link. Without preclinical experimental evidence demonstrating MEK-ERK pathway involvement in choroideremia pathophysiology, this prediction cannot be mechanistically justified at this time, and the biological rationale requires foundational research before any clinical translation is considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Binimetinib currently holds no marketing authorization in Taiwan. The drug is not marketed domestically.

---

## Cytotoxicity

Binimetinib's original approved indication is unresectable or metastatic melanoma — a malignancy — and it belongs to the kinase inhibitor class of anticancer agents.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — MEK1/2 inhibitor (non-conventional cytotoxic; not a classical alkylating or antimetabolite agent) |
| Myelosuppression Risk | Low (MEK inhibitors carry substantially lower myelosuppression risk than conventional chemotherapy; anaemia and neutropenia reported at low frequency) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (baseline and periodic), liver function tests (ALT/AST/bilirubin), cardiac function (LVEF by echocardiography), serum creatine kinase (CK), ophthalmological examination (retinal vein occlusion, uveitis, serous retinopathy), blood pressure |
| Handling Protection | Please refer to the SmPC warnings and precautions; standard oral anticancer drug handling precautions apply per institutional protocol |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (98.63%), the mechanistic rationale for applying a MEK inhibitor to choroideremia — a disease driven by CHM gene mutation and Rab-GGTase pathway dysfunction — is absent, and no supporting clinical trials or published literature exist. There is no basis to advance this candidate without primary mechanistic evidence.

**To proceed, the following is needed:**
- Basic mechanistic research to determine whether MEK-ERK pathway activity contributes to choroideremia pathophysiology or photoreceptor survival
- Preclinical validation using CHM-knockout animal models or patient-derived retinal organoids treated with binimetinib
- TFDA prescribing information (SmPC equivalent) to fully characterize the safety profile for potential new patient populations, including ophthalmic considerations
- Detailed MOA data from DrugBank or peer-reviewed sources to enable formal mechanistic linkage analysis
- Landscape review of the choroideremia treatment pipeline (note: CHM gene replacement therapy via AAV vector is the leading clinical approach and represents a fundamentally different mechanism; the competitive and scientific context must be assessed before committing resources to a small-molecule repurposing strategy)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

