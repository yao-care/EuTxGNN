---
layout: default
title: Alogliptin
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Alogliptin
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

# Alogliptin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Alogliptin is a selective DPP-4 (dipeptidyl peptidase-4) inhibitor, approved internationally for the treatment of type 2 diabetes mellitus (T2DM) by enhancing incretin-mediated insulin secretion.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome (SPS)** — a rare autoimmune neurological disorder — based on DPP-4's immunomodulatory role in T-cell regulation.
However, this prediction is currently supported by **0 clinical trials** and **0 publications** specifically addressing this indication, making it a purely model-driven hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (based on international pharmacological data; no Taiwan (TFDA) approval record available) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Alogliptin belongs to the DPP-4 inhibitor class (gliptins). Its therapeutic mechanism in T2DM involves selective inhibition of dipeptidyl peptidase-4, thereby prolonging the activity of incretin hormones GLP-1 and GIP — stimulating glucose-dependent insulin secretion and suppressing inappropriate glucagon release. Critically, DPP-4 is also known as the surface marker CD26, which is highly expressed on activated T lymphocytes.

Classic stiff person syndrome (SPS) is a rare, debilitating autoimmune neurological disease primarily driven by antibodies against glutamic acid decarboxylase 65 (anti-GAD65). The anti-GAD65 autoimmune attack impairs GABA synthesis in inhibitory interneurons of the spinal cord, leading to progressive muscle rigidity and spasms. Since DPP-4/CD26 plays a functional role in T-cell activation and the Th1/Th2 immune balance, DPP-4 inhibition theoretically carries immunomodulatory potential that could dampen autoimmune activity underlying SPS.

However, this mechanistic link is highly indirect. The pathway from systemic DPP-4 inhibition to meaningful attenuation of anti-GAD65-mediated neurological autoimmunity has not been demonstrated in any preclinical model or clinical observation. The TxGNN score reflects a graph-based structural relationship in the knowledge graph rather than experimentally validated biology. At present, this prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the Classic Stiff Person Syndrome indication specifically.

> **Note:** 3 publications were retrieved for the separately ranked **Pancreatic Agenesis** indication (Rank #6). These are not directly relevant to the top-ranked SPS indication but are listed below for reference, as they describe Alogliptin's β-cell protective mechanisms.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20859539](https://pubmed.ncbi.nlm.nih.gov/20859539/) | 2010 | Review/Commentary | Vascular Health and Risk Management | Discusses pioglitazone + alogliptin combination rationale in T2DM; highlights alogliptin's role in addressing GLP-1 deficiency and β-cell dysfunction |
| [21205126](https://pubmed.ncbi.nlm.nih.gov/21205126/) | 2011 | Animal Study / Preclinical | Diabetes, Obesity & Metabolism | Chronic alogliptin administration improved glucose control and preserved pancreatic islet function in a high-fat diet / streptozotocin mouse T2DM model |
| [22071236](https://pubmed.ncbi.nlm.nih.gov/22071236/) | 2011 | Review | Clinical Therapeutics | Review of DPP-4 inhibitor tolerability in T2DM; covers monotherapy and combination therapy safety profiles across the gliptin class |

---

## Taiwan Market Information

Alogliptin currently holds **no TFDA marketing authorization** in Taiwan. No approved indications, dosage forms, or license records are available in the Taiwan regulatory database.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) or the official prescribing information for safety details. Taiwan-specific label warnings and contraindications were not available in this Evidence Pack (Data Gap: TFDA 仿單 not retrieved). No drug-drug interaction data was returned from the DDI query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this Evidence Pack are classified at Evidence Level L5 — meaning the predictions are generated solely by the TxGNN model with no supporting clinical trials or disease-specific literature. The top-ranked indication (Classic Stiff Person Syndrome) has a plausible but highly indirect mechanistic hypothesis and zero empirical support; proceeding to any translational or regulatory activity is premature.

**To proceed, the following is needed:**

- **Retrieve MOA data:** Query DrugBank API for Alogliptin (DB06203) to formally document the mechanism of action and enable rigorous mechanistic-link analysis
- **Retrieve TFDA prescribing information:** Download and parse the TFDA SmPC PDF to populate key warnings, contraindications, and special population data (Data Gap DG001 — currently Blocking)
- **Preclinical evidence scan:** Conduct a broader PubMed search using MeSH terms combining "DPP-4 inhibitor" OR "gliptin" with "stiff person syndrome" OR "autoimmune neurological disease" to determine if any class-level (non-alogliptin) evidence exists
- **Class-level evidence review:** Evaluate whether sitagliptin or other DPP-4 inhibitors have published data in autoimmune disease models, as class effects may partially inform the plausibility of this prediction
- **Indication prioritisation review:** Given that 9 of 10 predicted indications are orphan/rare diseases with no evidence, consider whether mechanistically better-supported indications (e.g., Thiamine-Responsive Dysfunction Syndrome, which shares β-cell biology) warrant higher priority for evidence collection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

