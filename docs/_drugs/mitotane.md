---
layout: default
title: Mitotane
parent: Medium Evidence (L3-L4)
nav_order: 413
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Mitotane: predicted new indication Multiple endocrine neoplasia (evidence level L4). Approved use: Symptomatic treatment of advanced (unresectable…"
monitor_inn: "Mitotane"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "seborrheic keratosis", "vulvar inverted follicular keratosis", "apocrine adenosis of breast", "blunt duct adenosis of breast", "fat necrosis of breast", "breast abscess"]
---

# Mitotane
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Mitotane: From Adrenal Cortical Carcinoma to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Mitotane is an adrenolytic anticancer drug, originally used for symptomatic treatment of advanced adrenal cortical carcinoma.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**,
but only **1 clinical trial** (which did not test mitotane alone for MEN) and a small body of mostly indirect literature currently relate to this direction, so the prediction is **largely unsupported by direct evidence**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of advanced (unresectable, metastatic or relapsed) adrenal cortical carcinoma. The effect on non-functional adrenal cortical carcinoma is not established. |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 98.05% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mitotane is an adrenolytic agent that inhibits steroidogenic enzymes (such as CYP11A1 and CYP11B1) and is toxic to adrenocortical cells. Its efficacy in advanced adrenal cortical carcinoma is the basis of its approval.

The link to multiple endocrine neoplasia is limited to adrenal involvement. Adrenocortical tumours or hypercortisolism can occur in MEN type 1, and a few case reports describe mitotane controlling hypercortisolism in Carney complex, a related multiple endocrine neoplasia syndrome. There is no direct evidence that mitotane treats MEN itself. The high TxGNN score most likely reflects network proximity to adrenal cortical carcinoma, the approved indication, rather than independent MEN-specific evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00778817](https://clinicaltrials.gov/study/NCT00778817) | Phase 2 | Terminated | 20 | Randomized trial of IMC-A12 (cixutumumab, anti-IGF-1R antibody) plus mitotane vs mitotane alone in adrenocortical carcinoma. Mitotane served as the comparator backbone, so the trial gives no direct evidence for MEN. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38608694](https://pubmed.ncbi.nlm.nih.gov/38608694/) | 2024 | Phase 2 single-arm trial | The Lancet. Oncology | Cabozantinib in advanced adrenocortical carcinoma. Notes mitotane is the only approved therapy for this cancer. |
| [25402388](https://pubmed.ncbi.nlm.nih.gov/25402388/) | 2015 | Case series/report | Hormones (Athens) | Ten-year follow-up of a low-dose mitotane regimen with sustained correction of hypercortisolism in Carney complex (a multiple endocrine neoplasia syndrome). |
| [15816372](https://pubmed.ncbi.nlm.nih.gov/15816372/) | 2005 | Case report | J Endocrinol Invest | Six-month mitotane course produced sustained correction of hypercortisolism in a young woman with PPNAD and Carney complex. |
| [33875173](https://pubmed.ncbi.nlm.nih.gov/33875173/) | 2020 | Clinical review | Endocr Pract | AACE practical approach to evaluation and management of adult adrenocortical carcinoma. |
| [32098326](https://pubmed.ncbi.nlm.nih.gov/32098326/) | 2020 | Review | Cancers | Adjuvant therapy in adrenocortical carcinoma. Mitotane is the mainstay, but the evidence is retrospective and sometimes conflicting. |
| [37435451](https://pubmed.ncbi.nlm.nih.gov/37435451/) | 2022 | Review | Endocr Oncol | Prognostic factors and adjuvant treatment options in adrenocortical carcinoma. |
| [30798468](https://pubmed.ncbi.nlm.nih.gov/30798468/) | 2019 | Review | Curr Oncol Rep | Summary of clinical management of adrenocortical carcinoma. |
| [31118348](https://pubmed.ncbi.nlm.nih.gov/31118348/) | 2019 | Case report | Endocr J | Myxoid variant adrenocortical carcinoma in a patient with MEN1. Describes the disease association, not mitotane efficacy. |
| [30863550](https://pubmed.ncbi.nlm.nih.gov/30863550/) | 2019 | Case report | Oxf Med Case Reports | Metastatic adrenocortical carcinoma. Notes its occurrence in familial syndromes including MEN1. |
| [25639313](https://pubmed.ncbi.nlm.nih.gov/25639313/) | 2015 | Systematic review | Neurosurg Focus | Medical therapies for Cushing's disease. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000521 (cancelled) | Lysodren | Not specified | Symptomatic treatment of advanced (unresectable, metastatic or relapsed) adrenal cortical carcinoma. The effect of Lysodren on non-functional adrenal cort... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Adrenolytic cytotoxic agent (acts on adrenocortical cells) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions (gastrointestinal toxicity is commonly reported) |
| Monitoring Items | Adrenal function and cortisol replacement status, liver function, plasma mitotane levels |
| Handling Protection | Follow local cytotoxic drug handling regulations |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease, gallbladder disease, adrenocortical insufficiency, Addison disease, injury.
- **Drug Interactions**: 100 interactions were identified in the interaction database. Major-level examples include eliglustat, naldemedine, naloxegol, rolapitant and cobicistat. Moderate-level examples include aprepitant, saxagliptin, linagliptin, repaglinide, nitisinone, macimorelin, apixaban, avatrombopag and warfarin. Several others (e.g. morphine, omeprazole, hydrocortisone, ondansetron) have an unclassified severity level.
- Official label warnings and contraindications are not available in the compiled data. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for multiple endocrine neoplasia is a high model score plus indirect case reports on hypercortisolism in Carney complex. The single registered trial does not test mitotane for MEN. The EU authorization is cancelled, and mitotane's toxicity profile is substantial.

**To proceed, the following is needed:**
- Official SmPC warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Prospective clinical data on mitotane in MEN-related adrenal disease or hypercortisolism
- Clarification of the cancelled EU authorization status and available dosage forms
- Evaluation of the benefit-risk balance against existing standard therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

