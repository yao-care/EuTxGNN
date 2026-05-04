---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Aliskiren
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

# Aliskiren: From Hypertension to Pulmonary Hypertension owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Aliskiren is the first orally active direct renin inhibitor, used clinically for the treatment of arterial hypertension by blocking the rate-limiting step of the renin-angiotensin-aldosterone system (RAAS).
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
with **no clinical trials** and **20 publications** retrieved — however, none of the publications directly investigate Aliskiren in this indication, leaving the prediction without specific clinical or preclinical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (direct renin inhibitor; not registered in Taiwan) |
| Predicted New Indication | Pulmonary Hypertension owing to Lung Disease and/or Hypoxia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on pharmacological class, Aliskiren is a direct renin inhibitor — the first in its class to receive clinical approval. It acts at the most upstream point of the RAAS by binding directly to renin and blocking its catalytic activity, thereby suppressing the generation of angiotensin I, and consequently angiotensin II (Ang II) and aldosterone. Ang II is known to induce pulmonary vasoconstriction via AT1 receptors, which provides the theoretical basis for the TxGNN model's prediction.

Pulmonary hypertension owing to lung disease and/or hypoxia (WHO Group 3 PH) develops primarily through hypoxic pulmonary vasoconstriction (HPV) and hypoxia-driven vascular remodeling mediated by the HIF-1α/endothelin-1 axis. Unlike renovascular or essential hypertension — where RAAS is the dominant driver — Group 3 PH is governed by oxygen-sensing pathways. RAAS plays only a secondary, modulatory role in this disease context. While Ang II contributes to pulmonary vascular tone, renin inhibition alone is unlikely to adequately address the underlying HIF-1α-driven remodeling and right ventricular pressure overload that characterize this condition.

The 20 retrieved publications address general hypoxia biology — neurological effects, tumor microenvironment, immunity — without any paper examining Aliskiren in pulmonary hypertension or lung disease models. The mechanistic link therefore remains theoretical and extremely weak, insufficient to support advancement beyond AI model prediction at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Aliskiren in pulmonary hypertension owing to lung disease and/or hypoxia.

---

## Literature Evidence

All 20 retrieved publications address general hypoxia biology and are not specific to Aliskiren or pulmonary hypertension from lung disease. The 10 most contextually relevant entries are listed below for background reference.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics | Reviews four mechanisms of hypoxemia (hypoventilation, V/Q mismatch, right-to-left shunt, diffusion impairment) directly relevant to Group 3 PH pathophysiology; does not address Aliskiren |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Oxygen sensing governs angiogenesis, vascular disease, and pH homeostasis; overview of HIF pathway and hypoxia-related disease mechanisms; does not address Aliskiren |
| [28972206](https://pubmed.ncbi.nlm.nih.gov/28972206/) | 2017 | Review | Nature Reviews Immunology | Hypoxia regulates innate and adaptive immunity in physiological and pathological niches; relevant to vascular remodeling context; does not address Aliskiren |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell and Tissue Research | HIF-1-mediated adaptation drives tissue repair; chronic hypoxia shifts balance toward pathological fibrosis and vascular remodeling; does not address Aliskiren |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Tumor hypoxia induces resistance to radiation and immunotherapy; discusses strategies to therapeutically modify hypoxia; does not address Aliskiren |
| [39841808](https://pubmed.ncbi.nlm.nih.gov/39841808/) | 2025 | Review | Science Translational Medicine | Chronic continuous hypoxia shows preclinical benefits in mitochondrial disease and ischemia models; translation to patients faces major safety barriers; does not address Aliskiren |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia is pivotal in Alzheimer's and other neurodegenerative diseases; reduced ambient oxygen may exert protective effects in aging; does not address Aliskiren |
| [40963621](https://pubmed.ncbi.nlm.nih.gov/40963621/) | 2025 | Review | Frontiers in Immunology | HIF-1α mediates shared molecular mechanisms across tumor progression and autoimmune disease; does not address Aliskiren |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Acute and chronic hypoxia cause neurological deficits including cognitive dysfunction; reviews clinical and molecular evidence; does not address Aliskiren |
| [37915135](https://pubmed.ncbi.nlm.nih.gov/37915135/) | 2023 | Review | BMB Reports | CMGC kinases regulate HIF abundance in tumor hypoxia, with implications for angiogenesis and therapy resistance; does not address Aliskiren |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.98%), the mechanistic link between renin inhibition and Group 3 pulmonary hypertension is weak — the core pathophysiology (hypoxic pulmonary vasoconstriction and HIF-1α/ET-1-driven vascular remodeling) is not primarily RAAS-dependent, no clinical trials or Aliskiren-specific literature support this indication, and known safety signals from the ALTITUDE trial (increased renal and cardiovascular events with RAAS blockade in high-risk patients) counsel caution before pursuing new indications.

**To proceed, the following is needed:**
- Preclinical studies in hypoxia-exposed animal models of pulmonary hypertension to test whether renin inhibition reduces right ventricular pressure or pulmonary vascular remodeling
- Mechanistic research quantifying the contribution of RAAS/renin to Group 3 PH relative to HIF-1α and ET-1 pathways
- TFDA SmPC review (warnings, contraindications, drug interactions) to complete the safety profile
- MOA data from DrugBank API to confirm pharmacological target, receptor selectivity, and off-target activity relevant to pulmonary vasculature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

