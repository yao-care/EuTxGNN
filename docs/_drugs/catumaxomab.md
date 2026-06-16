---
layout: default
title: Catumaxomab
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Catumaxomab
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

# Catumaxomab: From Malignant Ascites to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Catumaxomab (Removab) is a trifunctional bispecific antibody that simultaneously binds EpCAM on epithelial tumor cells and CD3ε on T cells, previously approved in Europe for the treatment of malignant ascites in EpCAM-positive carcinomas, though withdrawn from the EU market in 2017 for commercial (not safety) reasons.

The TxGNN model ranks **Severe Nonproliferative Diabetic Retinopathy** as the top predicted new indication (score: 99.64%), but mechanistic analysis strongly suggests this is a knowledge graph false positive with no biological plausibility — the more scientifically credible predictions are urothelial carcinomas (ranks 5–9) and HER2-positive breast carcinoma (rank 10).

**No supporting clinical trials or literature have been identified for any of the 10 predicted indications.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malignant ascites in adult patients with EpCAM-positive carcinomas (EMA approved 2009; withdrawn 2017) |
| Predicted New Indication (Rank 1) | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed (authorization withdrawn May 2017) |
| Number of Authorizations | 0 (currently active) |
| Recommended Decision | Hold (Ranks 1–4) / Research Question (Ranks 5–10) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacological literature, Catumaxomab is a rat/mouse hybrid trifunctional bispecific antibody that simultaneously engages three immune targets: EpCAM (Epithelial Cell Adhesion Molecule) on tumor cells, CD3ε on cytotoxic T lymphocytes, and Fcγ receptors on accessory immune cells (NK cells, macrophages, dendritic cells). This triple engagement creates an immunological synapse at the tumor surface, triggering T cell-mediated cytotoxicity against EpCAM-positive epithelial cancers — the mechanism that justified its original approval for malignant ascites.

The top-ranked TxGNN prediction — severe nonproliferative diabetic retinopathy — has essentially no mechanistic overlap with this mode of action. Diabetic retinopathy is a microvascular disease driven by hyperglycemia-induced pericyte loss, basement membrane thickening, and VEGF-mediated neovascularization. EpCAM is a cell adhesion molecule expressed on epithelial tissues and epithelial-origin tumors, not on retinal microvasculature or pericytes. More importantly, Catumaxomab is a large protein (~150 kDa) that cannot cross the blood-retinal barrier under physiological conditions, making ocular delivery essentially impossible without specialized formulation strategies that do not currently exist for this molecule.

The high TxGNN scores for diabetic eye conditions (ranks 1, 3) and drug-induced osteoporosis (rank 2) most likely reflect structural bias in the knowledge graph, where "diabetic complication" and "bone metabolism" disease nodes are densely connected to many drug nodes due to co-occurrence in biomedical literature — generating spurious high scores with no pharmacological meaning. By contrast, the urothelial carcinoma predictions (ranks 5–9) and HER2-positive breast carcinoma (rank 10) are biologically plausible because these are EpCAM-expressing epithelial tumors that could theoretically be targeted by Catumaxomab's core mechanism.

---

## Prediction Landscape — All 10 Indications

| Rank | Disease | TxGNN Score | Mechanistic Plausibility | Recommendation |
|------|---------|-------------|--------------------------|----------------|
| 1 | Severe Nonproliferative Diabetic Retinopathy | 99.64% | ❌ None — blood-retinal barrier; no EpCAM relevance | Hold |
| 2 | Drug-Induced Osteoporosis | 99.58% | ❌ None — OPG/RANKL axis; no EpCAM link | Hold |
| 3 | Diabetic Retinopathy | 99.47% | ❌ None — same as Rank 1 | Hold |
| 4 | Diabetic Cataract | 98.45% | ❌ Very Low — non-inflammatory; lens EpCAM not tumor-level | Hold |
| 5 | Kidney Pelvis Sarcomatoid TCC | 98.29% | ⚠️ Low–Moderate — EMT may reduce EpCAM expression | Research Question |
| 6 | Prostatic Urethra Urothelial Carcinoma | 98.27% | ⚠️ Moderate — EpCAM-positive epithelial; rare anatomical site | Research Question |
| 7 | Infiltrating Bladder Urothelial Carcinoma, Sarcomatoid Variant | 98.25% | ⚠️ Moderate — MIBC EpCAM 50–80%; EMT concern in sarcomatoid | Research Question |
| 8 | Renal Pelvis Papillary Urothelial Carcinoma | 98.18% | ✅ Moderate–High — preserves epithelial phenotype; EpCAM relatively high | Research Question |
| 9 | Transitional Cell Carcinoma (general) | 98.07% | ✅ High — broad EpCAM-positive class; peritoneal cases can parallel original indication | Research Question |
| 10 | HER2-Positive Breast Carcinoma | 97.47% | ✅ Highest — EpCAM co-expression >80%; historical preclinical interest; synergy with trastuzumab possible | Research Question |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## EU Market Information

Catumaxomab was granted EMA marketing authorization in 2009 under the brand name Removab. The authorization was withdrawn in May 2017 at the marketing authorization holder's (Neovii Biotech GmbH / Fresenius Biotech) request — explicitly for commercial reasons, not due to safety or efficacy concerns. The full EPAR (European Public Assessment Report) remains available from the EMA website and constitutes the primary public reference for historical safety and efficacy data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EU/1/09/512/001 | Removab | Concentrate for solution for infusion (intraperitoneal) | Malignant ascites in EpCAM-positive carcinomas where no standard therapy is available or feasible — **withdrawn May 2017** |

---

## Cytotoxicity

Catumaxomab is an antineoplastic agent (immunotherapy class). Original indication was treatment of malignant ascites in EpCAM-positive carcinomas.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Trifunctional bispecific antibody (EpCAM × CD3 × Fcγ receptor) |
| Myelosuppression Risk | Low–Moderate (cytokine release may cause transient lymphopenia; not a conventional myelosuppressive cytotoxic agent) |
| Emetogenicity Classification | Low (primary adverse effects are cytokine release syndrome and infusion reactions, not direct emetogenic activity) |
| Monitoring Items | Liver enzymes (ALT/AST), lymphocyte count, vital signs during and after infusion (cytokine release syndrome monitoring), abdominal pain and gastrointestinal symptoms (intraperitoneal route) |
| Handling Protection | Please refer to the SmPC warnings and precautions (EMA EPAR for Removab) |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> No safety data (key warnings, contraindications, or drug interactions) was retrievable from this Evidence Pack. The drug is currently not marketed in Taiwan or the EU. Historical safety data is available from the EMA's published EPAR for Removab, which includes pivotal Phase II/III trial data. Key historically documented adverse effects include cytokine release syndrome (pyrexia, nausea, vomiting), abdominal pain (intraperitoneal administration), and hepatotoxicity.

---

## Conclusion and Next Steps

**Decision: Hold (Ranks 1–4) / Research Question (Ranks 5–10)**

**Rationale:**
The top four TxGNN predictions relate to diabetic complications (retinopathy, cataract) and drug-induced osteoporosis — all of which have no biologically plausible connection to Catumaxomab's EpCAM × CD3 mechanism and should be dismissed as knowledge graph artifacts. Ranks 5–10 involve EpCAM-expressing epithelial malignancies (urothelial carcinomas and HER2-positive breast cancer) where the core mechanism is theoretically applicable, but no clinical or preclinical evidence currently exists to support development. The drug's EU market withdrawal and absence from Taiwan further constrains access.

**To proceed with Research Question indications (Ranks 5–10), the following is needed:**

- **EpCAM expression profiling**: Confirm EpCAM expression rates in target tumor subtypes — especially sarcomatoid variants (ranks 5, 7) where epithelial-to-mesenchymal transition may significantly reduce EpCAM surface density and diminish targeting efficiency
- **Drug access pathway**: Determine whether Catumaxomab can be obtained through the original manufacturer's compassionate use program, academic collaboration, or biosimilar development, given current EU and Taiwan non-marketing status
- **Preclinical studies**: Design in vitro EpCAM binding, T cell cytotoxicity, and 3D tumor model studies for urothelial carcinoma (TCC) and HER2-positive breast carcinoma cell lines
- **HER2+ breast carcinoma priority (Rank 10)**: This is the highest-priority Research Question candidate — evaluate preclinical synergy between Catumaxomab (EpCAM targeting) and trastuzumab (HER2 targeting) given >80% EpCAM/HER2 co-expression
- **Route of administration assessment**: Evaluate whether intraperitoneal delivery (original approved route) is feasible for any target indication with peritoneal metastasis; systemic IV dosing would require separate pharmacokinetic development
- **Safety data retrieval**: Obtain complete warnings, contraindications, and adverse event profile from the EMA Removab EPAR for current regulatory readiness assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

