---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: From Cutaneous Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab (Libtayo) is an anti-PD-1 immune checkpoint inhibitor approved by the FDA and EMA for cutaneous squamous cell carcinoma (CSCC), basal cell carcinoma (BCC), non-small cell lung cancer (NSCLC), and cervical cancer; it currently has no marketing authorization in Taiwan.
The TxGNN model predicts it may be effective for **Gallbladder Adenosquamous Carcinoma**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous squamous cell carcinoma (FDA/EMA approved; no Taiwan authorization) |
| Predicted New Indication | Gallbladder Adenosquamous Carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Cemiplimab is not currently available from the DrugBank query (data gap). Based on clinical context available in the evidence pack, Cemiplimab is an anti-PD-1 (Programmed Death-1) monoclonal antibody. It works by blocking the PD-1 receptor on CD8+ cytotoxic T cells, preventing tumor cells from evading immune surveillance through the PD-1/PD-L1 checkpoint axis — thereby restoring the immune system's ability to identify and destroy malignant cells. This mechanism has been validated across multiple tumor types bearing squamous histology and high PD-L1 expression.

Gallbladder adenosquamous carcinoma is an extremely rare mixed-histology malignancy (< 1% of gallbladder cancers) containing both squamous and glandular tumor components. The presence of a squamous component creates a theoretical basis for PD-L1 upregulation in the mixed tumor microenvironment, drawing a mechanistic parallel to other squamous cell malignancies where anti-PD-1 therapy has demonstrated efficacy. Additionally, the parent disease category — biliary tract cancer broadly — carries exploratory checkpoint inhibitor evidence, which gives the prediction indirect biological plausibility.

However, gallbladder adenosquamous carcinoma is so rare that no dedicated clinical or preclinical studies exist for this subtype. The TxGNN model appears to be generalizing from squamous histology patterns and known PD-1 responsiveness across related tumor types — a reasonable computational hypothesis, but one that cannot be validated without direct evidence. The mechanistic rationale remains indirect and insufficient to support clinical progression at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cemiplimab in gallbladder adenosquamous carcinoma.

---

## Literature Evidence

Currently no related literature available for Cemiplimab in gallbladder adenosquamous carcinoma.

---

## Taiwan Market Information

Cemiplimab currently has no TFDA marketing authorization and is not marketed in Taiwan. No regulatory approval data or package insert is available for review. The absence of Taiwan approval is itself a blocking data gap for safety evaluation (see Safety Considerations).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (Anti-PD-1 monoclonal antibody) |
| Myelosuppression Risk | Low — direct bone marrow toxicity is uncommon; immune-mediated hematological adverse events (e.g., immune thrombocytopenia, hemolytic anemia) are possible but rare |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests (AST/ALT/total bilirubin), thyroid function (TSH, free T4), adrenal function (morning cortisol), fasting blood glucose, serum creatinine — all for immune-related adverse event (irAE) surveillance |
| Handling Protection | Standard monoclonal antibody handling procedures apply; cytotoxic drug handling precautions are generally not required for anti-PD-1 biologics |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** TFDA package insert data for Cemiplimab is currently unavailable (blocking data gap DG001). Safety review — including key warnings, contraindications, and drug interaction screening — cannot be completed until the SmPC or equivalent label is retrieved and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or published literature exist for Cemiplimab specifically in gallbladder adenosquamous carcinoma, an exceptionally rare tumor subtype (< 1% of gallbladder cancers). The current evidence is AI model prediction only (L5), which is insufficient to support any development decision without foundational research data.

**To proceed, the following is needed:**
- Characterization of PD-L1 expression (CPS/TPS scoring) and tumor mutational burden (TMB) in gallbladder adenosquamous carcinoma tissue samples — these biomarkers are the primary determinants of anti-PD-1 responsiveness
- Consideration of basket trial enrollment covering rare biliary tract or mixed-histology carcinomas (e.g., TMB-high or MSI-H enriched cohorts)
- TFDA package insert retrieval and parsing for full safety, warning, and contraindication review (currently a blocking data gap — DG001)
- Mechanism of action data from DrugBank API (high-priority gap — DG002)
- Taiwan regulatory pathway assessment: Cemiplimab is not currently authorized in Taiwan; an import or regulatory filing strategy would be required before any clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

