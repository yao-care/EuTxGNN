---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Denosumab
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab (Prolia®/Xgeva®) is a fully human monoclonal antibody targeting RANKL, globally approved for osteoporosis, bone metastases from solid tumors, and giant cell tumor of bone; it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, achieving a prediction score of **99.63%**.
Currently, **no clinical trials or published literature** directly support this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for osteoporosis, bone metastases, and giant cell tumor of bone |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known information, Denosumab is a fully human monoclonal antibody that binds and neutralizes RANKL (receptor activator of nuclear factor kappa-B ligand), a key cytokine regulating osteoclast formation, activation, and survival. By blocking RANKL from engaging its receptor RANK, Denosumab suppresses osteoclast-mediated bone resorption — the basis for its efficacy in osteoporosis and bone-related oncologic conditions.

The theoretical mechanistic bridge proposed by TxGNN connects the RANKL/OPG axis to diabetic retinopathy: RANKL signaling may theoretically regulate pericyte apoptosis and inflammatory responses within retinal microvasculature, processes that are central to the progression of diabetic retinopathy. Blocking RANKL could, in principle, attenuate retinal vascular inflammation and protect pericyte integrity.

However, this mechanistic link is explicitly characterized as **highly speculative** in the evidence pack. There is no published preclinical animal research or human clinical data validating RANKL blockade as a strategy for severe nonproliferative diabetic retinopathy. The biological plausibility exists at a conceptual level only and has not been subjected to any experimental testing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

---

## Cytotoxicity

Denosumab (as Xgeva®) is approved for oncologic indications including prevention of skeletal-related events from bone metastases and treatment of unresectable giant cell tumor of bone; literature in this evidence pack further references its use in prostate cancer-related bone loss. It is therefore classified as an antineoplastic targeted therapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (Anti-RANKL human monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (not a myelosuppressive agent; principal bone marrow risk is via hypocalcaemia, not direct marrow toxicity) |
| Emetogenicity Classification | Minimal (biologic injection; emetogenicity not a primary concern) |
| Monitoring Items | Serum calcium and vitamin D (hypocalcaemia), renal function, dental health assessment (osteonecrosis of the jaw), CBC if concurrent chemotherapy |
| Handling Protection | Standard biologic/injectable handling precautions; not classified as a conventional cytotoxic requiring cytotoxic handling protocols |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Taiwan regulatory safety data (TFDA SmPC warnings and contraindications) are unavailable for this drug, as it is not registered in Taiwan. DDI database query returned no results. For clinical decision-making, consult the EMA SmPC for Prolia® or Xgeva®, which documents known risks including hypocalcaemia, osteonecrosis of the jaw, atypical femoral fractures, and serious skin reactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score of 99.63% for severe nonproliferative diabetic retinopathy, the proposed RANKL/OPG–retinal microvascular mechanistic link is entirely speculative, with zero supporting preclinical or clinical evidence at the time of this assessment (Evidence Level L5).

**To proceed, the following is needed:**

- **Basic science validation:** Preclinical studies (in vitro retinal pericyte models or rodent diabetic retinopathy models) to determine whether RANKL/OPG signaling plays a functional role in retinal vascular disease
- **Mechanistic data:** Retrieve complete MOA and DrugBank pharmacology data (Data Gap DG002) to assess pathway plausibility more rigorously
- **Regulatory safety review:** Obtain Taiwan TFDA SmPC or EMA SmPC full text to complete S1 safety screening (Data Gap DG001)
- **Literature expansion:** Conduct a broader search for basic science papers linking RANKL signaling to retinal pericyte biology, diabetic microangiopathy, or neovascularization — any preclinical signal would upgrade this from L5 to L4 and warrant hypothesis-driven study design
- **Indirect evidence review:** PMID 38899553 (Cohort/RWE, 2024) reports that Denosumab reduces microvascular complications including retinopathy in T2DM patients compared to bisphosphonates — this indirect signal from the rank-2 indication (diabetic retinopathy) should be reviewed as supporting context before completely dismissing the hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

