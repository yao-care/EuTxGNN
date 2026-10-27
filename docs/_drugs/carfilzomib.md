---
layout: default
title: Carfilzomib
parent: AI Predictions (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Carfilzomib: predicted new indication CMM7 (evidence level L5). Approved use: Multiple myeloma in adults who have received at least one prior thera…"
monitor_inn: "Carfilzomib"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma", "intellectual disability, autosomal dominant 55, with seizures", "myeloid leukemia", "neutrophil immunodeficiency syndrome", "central nervous system melanocytic neoplasm"]
---

# Carfilzomib
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

## Carfilzomib: From Multiple Myeloma to CMM7 (Melanoma-Related Predictions)
{: .text-alpha }

## One-Sentence Summary

Carfilzomib is a proteasome inhibitor, originally used to treat adult patients with relapsed or refractory multiple myeloma.
The TxGNN model's top prediction is **CMM7**, with a score of 99.37%, but **no clinical trials and no publications** currently support it.
This is a model prediction only. The nearest indication with some evidence is **melanoma** (preclinical studies only), and **myeloid leukemia** has the strongest clinical signal (one Phase 1 trial of carfilzomib itself).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma in adults who have received at least one prior therapy (in combination with daratumumab and dexamethasone, lenalidomide and dexamethasone, or dexamethasone alone) |
| Predicted New Indication | CMM7 (top-ranked prediction) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, carfilzomib is a proteasome inhibitor. Its efficacy in relapsed multiple myeloma is established, and mechanistically it may be applicable to melanocyte-derived tumours through proteotoxic stress and apoptosis.

For the top prediction (CMM7) there is no direct mechanistic evidence. The high score is a model output only. The same applies to the other melanoma-related predictions: pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, vulvar melanoma and central nervous system melanocytic neoplasm. For the two central nervous system indications, carfilzomib's limited blood-brain barrier penetration is an additional pharmacological obstacle.

Several other predictions have more support:
- **Melanoma (rank 5, L4):** a preclinical study found that carfilzomib combined with bortezomib increased apoptosis in B16-F1 melanoma cells. The other literature is computational docking and cell-survival studies, so the evidence is indirect.
- **Myeloid leukemia (rank 8, L3):** the literature supports proteasome dependence in AML, and a Phase 1 trial tested carfilzomib directly in relapsed AML and ALL.
- **Indolent plasma cell myeloma (rank 6):** this is closely related to the approved disease, so it is not a true repurposing case.
- **Neutrophil immunodeficiency syndrome and the neurodevelopmental disorder (intellectual disability, autosomal dominant 55, with seizures):** these have no plausible mechanistic rationale. Proteasome inhibition causes immunosuppression and cytopenias, and the scores likely reflect network artefacts.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (CMM7). The only predicted indication with trials is myeloid leukemia (rank 8):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01137747](https://clinicaltrials.gov/study/NCT01137747) | Phase 1 | Completed | 18 | Dose escalation of carfilzomib in adults with relapsed acute myeloid and acute lymphoblastic leukemia. Directly relevant, but small and early phase. Results are not described in the data. |
| [NCT01204164](https://clinicaltrials.gov/study/NCT01204164) | Phase 1 | Completed | 120 | TG02 citrate in advanced hematologic malignancies. Does not evaluate carfilzomib. |
| [NCT03530683](https://clinicaltrials.gov/study/NCT03530683) | Phase 1 | Terminated | 189 | TTI-622 (maplirpacept) in lymphoma, leukemia and multiple myeloma. Does not involve carfilzomib. |

---

## Literature Evidence

No literature is available for the top-ranked prediction (CMM7). Selected publications for the better-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro | Biology | Carfilzomib plus bortezomib enhanced apoptosis in B16-F1 melanoma cells (melanoma) |
| [27911437](https://pubmed.ncbi.nlm.nih.gov/27911437/) | 2016 | Review | Blood Cancer J | The role of the proteasome in AML and the rationale for proteasome inhibition |
| [26674111](https://pubmed.ncbi.nlm.nih.gov/26674111/) | 2016 | Phase 1 study | Leuk Lymphoma | Phase I study of carfilzomib in relapsed or refractory AML and ALL (no abstract available) |
| [28340282](https://pubmed.ncbi.nlm.nih.gov/28340282/) | 2017 | Preclinical | Br J Haematol | Carfilzomib induced leukaemia cell apoptosis via ELK1/CIP2A inhibition and PP2A activation, independent of proteasome inhibition |
| [24590311](https://pubmed.ncbi.nlm.nih.gov/24590311/) | 2014 | Preclinical | Oncogenesis | Synergy of carfilzomib with tyrosine kinase inhibitors in imatinib-sensitive and -resistant CML models |
| [39285441](https://pubmed.ncbi.nlm.nih.gov/39285441/) | 2024 | Preclinical | J Hematol Oncol | Proteasome inhibition enhanced the anti-leukemic efficacy of CAR-NK cells against AML |
| [27291302](https://pubmed.ncbi.nlm.nih.gov/27291302/) | 2016 | Review | Am J Hematol | Multiple myeloma update on diagnosis, risk stratification and management (indolent plasma cell myeloma) |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003790 | Kyprolis | Not specified | Kyprolis in combination with daratumumab and dexamethasone, with lenalidomide and dexamethasone, or with dexa... |

This authorization is recorded as cancelled, and no currently valid authorization was identified.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions. Haematological parameters (CBC) are generally monitored with antineoplastic therapy. |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

**Drug Interactions:** The interaction screening returned 100 potential interactions. Among the 20 listed, the following are rated **Major**:
- Anabolic steroids: oxandrolone, oxymetholone, stanozolol
- Deferiprone
- Samarium (153Sm) lexidronam
- Haemostatic and coagulation products: recombinant antihemophilic factor, aminocaproic acid, von Willebrand factor, human C1-esterase inhibitor, recombinant coagulation factor VIIa, coagulation factor X, conestat alfa
- Avatrombopag

Moderate interactions include metronidazole, tinidazole, naltrexone, rosuvastatin, simvastatin, palifermin and strontium chloride Sr-89.

For warnings and contraindications, please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions (CMM7 and the other melanoma subtypes) rest only on a model score, with no trials or publications. The strongest signals are preclinical melanoma data and an early-phase AML/ALL trial with no reported results. The EU authorization is also recorded as cancelled.

**To proceed, the following is needed:**
- Mechanism of action data for carfilzomib
- Warnings and contraindications from the EMA product information
- Clarification of the cancelled EU authorization status
- For melanoma: in vivo preclinical validation and a rationale for CNS penetration in the CNS and leptomeningeal subtypes
- For myeloid leukemia: published results of the Phase 1 trial (NCT01137747) and data from Phase 2 or later
- Review of whether the neutrophil immunodeficiency and neurodevelopmental predictions are network artefacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

