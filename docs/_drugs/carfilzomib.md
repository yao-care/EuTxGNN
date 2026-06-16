---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Carfilzomib
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

# Carfilzomib: From Multiple Myeloma to CMM7

## One-Sentence Summary

Carfilzomib is a selective, irreversible proteasome inhibitor approved internationally as a second-line or later treatment for relapsed/refractory multiple myeloma (RRMM).
The TxGNN model predicts it may be effective for **CMM7** (Cutaneous Malignant Melanoma 7),
with **0 clinical trials** and **0 publications** currently supporting this specific direction.
Among the top 10 predicted indications, myeloid leukemia (Phase 1 trial completed) and melanoma (preclinical evidence) carry higher levels of supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory multiple myeloma (globally approved; not registered in Taiwan) |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma 7) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on information consistently referenced across the repurposing rationales provided, Carfilzomib is a **selective, irreversible inhibitor of the chymotrypsin-like (CT-L) catalytic subunit** of the 20S proteasome. Blocking this activity causes misfolded and damaged proteins to accumulate inside the cell, saturating the unfolded protein response (UPR) and triggering endoplasmic reticulum (ER) stress-driven apoptosis. Cancer cells that rely heavily on high-throughput protein synthesis or rapid proliferation — such as immunoglobulin-secreting plasma cells — are particularly dependent on an intact proteasome for survival and therefore especially vulnerable to this class of drug.

CMM7 (Cutaneous Malignant Melanoma 7) is a genetically defined melanoma susceptibility locus associated with CDK4 gene amplification or activating mutation, which drives aberrant, unrestrained cell cycle progression. Melanoma cells in general maintain elevated proteasome activity to manage the proteotoxic burden arising from oncogene-driven metabolic demands, rapid proliferation, and stress in the tumor microenvironment. The TxGNN knowledge graph likely identified network-level connectivity between proteasome-dependent degradation of CDK4-related regulatory proteins and Carfilzomib's mechanism, generating this high-scoring prediction (99.37%).

It is important to note, however, that no direct clinical or preclinical evidence exists for Carfilzomib specifically in CMM7. The biological rationale is indirect: at the broader melanoma level (ranked 5th in this assessment), cell line studies confirm that proteasome inhibitors including Carfilzomib can induce apoptosis in B16-F1 melanoma cells, providing some mechanistic plausibility. Nevertheless, CDK4-specific CMM7 biology has not been separately studied in this context, and Carfilzomib's large molecular weight (~720 Da) combined with its P-glycoprotein substrate status significantly limits tissue penetration in solid tumors — a relevant pharmacokinetic barrier for any non-hematologic application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carfilzomib in CMM7.

---

## Literature Evidence

Currently no related literature available for Carfilzomib in CMM7.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Second-generation irreversible proteasome inhibitor (epoxyketone class) |
| Myelosuppression Risk | High — anemia, thrombocytopenia, and neutropenia are commonly reported in RRMM clinical trials; mandatory haematological monitoring is required throughout treatment |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, renal function (serum creatinine, eGFR), cardiac function (ECG, left ventricular ejection fraction), blood pressure, pulmonary status (dyspnoea surveillance) |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system transfer devices are recommended during preparation and administration |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
CMM7 is a genetically defined melanoma subtype with no published clinical or preclinical evidence for Carfilzomib. At the current L5 evidence level, this prediction remains a computational hypothesis; no actionable data exists to support progression to drug development activities.

**To proceed, the following is needed:**
- MOA documentation from DrugBank to formally characterize the mechanistic link between proteasome inhibition and CDK4-amplified melanoma biology
- Preclinical validation studies in CDK4-mutant or CMM7-relevant melanoma cell line and animal models
- Taiwan TFDA drug label (仿單) review to establish the complete safety profile and contraindication list
- Drug-drug interaction (DDI) profile assessment
- Solid tumor tissue penetration data for Carfilzomib to assess pharmacokinetic feasibility in non-hematologic malignancies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

