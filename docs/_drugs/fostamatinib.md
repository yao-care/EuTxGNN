---
layout: default
title: Fostamatinib
parent: AI Predictions (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Fostamatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fostamatinib: From Chronic Immune Thrombocytopenia to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib is a SYK (spleen tyrosine kinase) inhibitor originally used to treat chronic immune thrombocytopenia (ITP) in adults who are refractory to other treatments.
The TxGNN model predicts it may be effective for **autosomal thrombocytopenia with normal platelets**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic immune thrombocytopenia (ITP) in adult patients who are refractory to other treatments |
| Predicted New Indication | Autosomal thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fostamatinib is a SYK inhibitor; its active metabolite is R406. In chronic ITP, it reduces antibody-mediated destruction of platelets by macrophages. Detailed mechanism-of-action data was not available in the data compiled for this report, so this description relies on the known pharmacology of the drug.

The new indication is a thrombocytopenia, so the model's high score probably reflects how close the disease sits to ITP in the knowledge graph. However, inherited thrombocytopenias are caused by genetic defects in platelet production, not by immune-mediated platelet destruction. SYK inhibition therefore has no clear mechanistic rationale here, and the prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern. Syndromic constitutional thrombocytopenia (score 98.97%) is linked only through the shared low-platelet phenotype. Several others have no plausible mechanistic link and look like knowledge-graph artifacts: non-syndromic esophageal malformation, biotin metabolic disease, vitamin deficiency disorder, filariasis, and primary hereditary glaucoma. Glaucoma, open-angle glaucoma, and esophageal disease have only speculative or indirect links. None of these has trials, and the few publications retrieved are general kinase-inhibitor reviews or preclinical esophageal cancer studies, not studies of fostamatinib.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (autosomal thrombocytopenia with normal platelets), currently no related literature is available.

Publications retrieved for lower-ranked predictions are only indirectly relevant:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30877063](https://pubmed.ncbi.nlm.nih.gov/30877063/) | 2019 | Review | Pharmacological Research | Properties of FDA-approved small-molecule protein kinase inhibitors (glaucoma prediction); does not study fostamatinib in glaucoma |
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Review | Pharmacological Research | 2020 update on FDA-approved kinase inhibitors (glaucoma prediction); no fostamatinib-specific glaucoma data |
| [38096958](https://pubmed.ncbi.nlm.nih.gov/38096958/) | 2024 | Review | Pharmacological Research | US cost of FDA-approved kinase inhibitors (glaucoma prediction); no clinical evidence for this indication |
| [37734435](https://pubmed.ncbi.nlm.nih.gov/37734435/) | 2023 | Preclinical proteomics study | Life Sciences | Proteomics and phosphoproteomics of esophageal cancer cells with different invasive abilities (esophageal disease prediction) |
| [29930979](https://pubmed.ncbi.nlm.nih.gov/29930979/) | 2018 | Preclinical siRNA screen | Cellular and Molecular Gastroenterology and Hepatology | siRNA screen identifying a druggable immune signature driving esophageal adenocarcinoma cell growth (esophageal disease prediction) |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005012 (cancelled) | Tavlesse | Not specified | Tavlesse is indicated for the treatment of chronic immune thrombocytopenia (ITP) in adult patients who are refractory to other treatments. |

## Safety Considerations

- **Drug Interactions**: The interaction screening completed and returned 100 interacting drugs; the 20 listed in the compiled data are mostly Moderate severity.
  - **Major**: Clarithromycin.
  - **Moderate (examples)**: proton pump inhibitors and acid reducers (rabeprazole, omeprazole, dexlansoprazole, cimetidine); corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone); antiemetics (aprepitant, dolasetron); antidiabetic drugs (empagliflozin, pioglitazone); and others (alosetron, alvimopan, dronabinol, eliglustat, loperamide, morphine).

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or relevant literature (Evidence Level L5). Inherited thrombocytopenia is not driven by the immune-mediated platelet destruction that SYK inhibition addresses, so there is no clear mechanistic support. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data and a plausible biological rationale linking SYK inhibition to the genetic defects in platelet production
- Preclinical or clinical evidence in this indication
- Warnings and contraindications from the EU product information, which are required before any safety screening
- Clarification of why the EU authorization was cancelled and what that means for availability
- A review of the interaction profile, especially the Major interaction with clarithromycin, for the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

