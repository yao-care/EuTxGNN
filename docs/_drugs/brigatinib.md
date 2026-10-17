---
layout: default
title: Brigatinib
parent: AI Predictions (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Brigatinib: predicted new indication Gingival fibromatosis (evidence level L5). Approved use: ALK-positive advanced NSCLC (first-line, and after prior crizotinib)"
monitor_inn: "Brigatinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Brigatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Brigatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib is a kinase inhibitor originally used to treat ALK-positive advanced non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** support this prediction, which is purely computational.
The most relevant repurposing signal in the data compiled for this report is for **NF2-related schwannomatosis**, which surfaced under a different predicted term (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive advanced NSCLC (first-line, and after prior crizotinib) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Brigatinib is known to be a multi-target tyrosine kinase inhibitor acting on ALK, EGFR and ROS1. Its efficacy in ALK-positive NSCLC is well established through the Phase 3 ALTA-1L trial.

For gingival fibromatosis, no mechanistic link could be identified. No established kinase-driven pathway connects brigatinib's targets to this condition. The high TxGNN score (0.999) is therefore a statistical output of the model and is not backed by biological or clinical evidence. Other top-ranked predictions (fibroma of lung, lung hamartoma, junctional epidermolysis bullosa, and others) show the same pattern: no trials, no literature, and no plausible mechanism.

Two other predictions are worth noting:
- **Lung hilum carcinoma and pulmonary sulcus neoplasm** are lung cancers. ALK-positive cases could theoretically respond, but this is an extrapolation from the approved indication, not repurposing evidence.
- **NF2-related schwannomatosis** is the strongest repurposing signal. It appeared in the literature mapped to the rank-10 predicted term (a syndrome with an unrelated name, which appears to be a mapping artifact). Preclinical work shows brigatinib shrinks NF2-deficient meningioma and schwannoma through inhibition of multiple tyrosine kinases, but not ALK. A clinical report in *The New England Journal of Medicine* (2024) describes its use in patients with progressive tumors. This evidence is small and non-randomized (L3) and applies to NF2-related schwannomatosis, not to the named syndrome.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

For reference, the literature that surfaced under other predicted terms is summarized below. It is **not** evidence for the headline prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/) | 2024 | Cohort/Case series | N Engl J Med | Brigatinib in NF2-related schwannomatosis with progressive tumors |
| [34264955](https://pubmed.ncbi.nlm.nih.gov/34264955/) | 2021 | Preclinical | PLoS One | Tumor shrinkage in NF2-deficient meningioma and schwannoma via multiple tyrosine kinases, not ALK |
| [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) | 2018 | RCT | N Engl J Med | ALTA-1L: brigatinib vs crizotinib in ALK-positive NSCLC (original indication) |
| [34537440](https://pubmed.ncbi.nlm.nih.gov/34537440/) | 2021 | RCT | J Thorac Oncol | Final ALTA-1L results, superior progression-free survival vs crizotinib (original indication) |
| [34371380](https://pubmed.ncbi.nlm.nih.gov/34371380/) | 2021 | Case report | ESMO Open | Sustained response in metastatic pheochromocytoma with ALK mutation |
| [39395329](https://pubmed.ncbi.nlm.nih.gov/39395329/) | 2024 | Case report | Respir Investig | Response in lung large cell neuroendocrine carcinoma with EML4-ALK fusion |
| [27049722](https://pubmed.ncbi.nlm.nih.gov/27049722/) | 2016 | Preclinical | Oncotarget | Activity in ALK-positive neuroblastoma cells, Drosophila and mice |
| [34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/) | 2021 | Case report | Front Pharmacol | Fatal tumour lysis syndrome induced by brigatinib in lung adenocarcinoma |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004248 | Alunbrig | Not specified | Monotherapy for adults with ALK-positive advanced NSCLC not previously treated with an ALK inhibitor, or previously treated with crizotinib. |

The authorization status is **cancelled**.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Key Warnings**: A published case report describes fatal tumour lysis syndrome with brigatinib in a patient with lung adenocarcinoma treated with sequential ALK inhibitors (PMID 34987411). A pharmacovigilance analysis of cardiac toxicities with targeted NSCLC therapies has also been published (PMID 34418561).
- **Drug Interactions**: 100 interactions were found in the interaction database. Major-level interactions include:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin

  Moderate-level interactions include acid-suppressing drugs (famotidine, ranitidine, rabeprazole, cimetidine), antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin), loperamide, morphine, cisapride and clotrimazole.

Please refer to the SmPC for the full safety information, including contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for gingival fibromatosis rests only on a model score, with no trials, no literature and no plausible mechanism. The EU authorization is also cancelled.
- The NF2-related schwannomatosis signal is more promising but is small, non-randomized, and tied to a mismatched disease label.

**To proceed, the following is needed:**
- Remap the disease label to NF2-related schwannomatosis and reassess the evidence level for that indication.
- Obtain detailed mechanism of action data (MOA).
- Retrieve warnings and contraindications from the SmPC, which is currently missing and blocks safety screening.
- Clarify the reason for the cancelled EU authorization and the availability of the drug in the EU.
- Define a safety monitoring plan, including tumour lysis syndrome and cardiac risks.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

