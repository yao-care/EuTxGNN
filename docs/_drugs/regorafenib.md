---
layout: default
title: Regorafenib
parent: AI Predictions (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Regorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Metastatic colorectal cancer (previously treated)"
---

# Regorafenib
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

# Regorafenib: From Metastatic Colorectal Cancer to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multi-kinase inhibitor originally authorised in the EU for metastatic colorectal cancer, gastrointestinal stromal tumours (GIST) and hepatocellular carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** and **9 publications** compiled for this report. However, the best randomised evidence in liposarcoma (the SARC024 liposarcoma cohort) did **not** support routine use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (previously treated); unresectable or metastatic GIST after imatinib and sunitinib; hepatocellular carcinoma after sorafenib |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L1 (as assigned in the compiled data; see caveat below) |
| EU Market Status | Cancelled only (the single centralised authorisation is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Proceed with Guardrails (see the caution in the Conclusion) |

---

## Why is This Prediction Reasonable?

Regorafenib is a multi-kinase inhibitor targeting angiogenic kinases (VEGFR1-3, TIE2), stromal kinases (PDGFR, FGFR) and oncogenic kinases (KIT, RET, RAF). Structured mechanism-of-action data were not available in the compiled drug record, but this target profile is described in the literature reviewed for this report.

Regorafenib is already used in cancers driven by angiogenic and kinase signalling (colorectal cancer, GIST, hepatocellular carcinoma). Soft tissue sarcomas, including liposarcoma, also depend in part on PDGFR and VEGFR signalling. Related kinase inhibitors such as pazopanib have shown activity in soft tissue sarcomas. This is the mechanistic basis for the model's prediction.

The evidence is subtype-dependent, however. The placebo-controlled REGOSARC phase 2 trial showed benefit in non-adipocytic sarcomas (e.g. leiomyosarcoma, synovial sarcoma) but **not in liposarcoma**. The SARC024 liposarcoma cohort confirmed this. The model's high score therefore should not be read as evidence of clinical benefit in liposarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: blanket protocol of oral regorafenib in selected sarcoma subtypes, including liposarcoma. The liposarcoma stratum is only part of the enrollment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort (randomised, placebo-controlled phase 2): results do not support routine use of regorafenib in this population |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC: randomised phase 2 of regorafenib vs placebo in anthracycline-pretreated advanced soft tissue sarcoma |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | European Journal of Cancer | Updated REGOSARC analysis including cross-over: benefit in non-adipocytic sarcoma, but not in liposarcoma |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Review of the growing role of regorafenib in sarcoma |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Quality-adjusted analysis | Cancer | REGOSARC Q-TWiST analysis of clinical benefit in doxorubicin-refractory sarcoma |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Study protocol | BMC Cancer | REGOSARC trial design |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Maintenance therapy after first-line treatment for advanced soft tissue sarcoma |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study (different drug: anlotinib) | Anti-Cancer Drugs | Anlotinib in well-/dedifferentiated liposarcoma; indirect evidence |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case report (different drug: pazopanib) | Rare Tumors | Pazopanib in Ewing sarcoma; provided rationale for adding arms to SARC024 |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002573 (status: cancelled) | Stivarga | Not specified | Monotherapy for adults with previously treated metastatic colorectal cancer, unresectable or metastatic GIST after imatinib and sunitinib, and hepatocellular carcinoma previously treated with sorafenib... |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC; literature reviewed for this report highlights hepatic toxicity, hand-foot skin reaction, hypertension and proteinuria as class-related adverse effects, so liver function, blood pressure and urinalysis are reasonable to monitor |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: A drug-interaction query returned 100 records. Major-level interactions in the listed results include acetylsalicylic acid, deferasirox, ibritumomab tiuxetan, tositumomab, abciximab, alteplase, antithrombin III and apixaban (largely antithrombotic or bleeding-risk agents). Moderate interactions include dexamethasone, clarithromycin, naltrexone, rosuvastatin, cobicistat, fenfluramine, dexfenfluramine and sibutramine.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (leaning toward Hold for liposarcoma specifically)**

**Rationale:**
- The compiled data label this candidate L1 and "Proceed with Guardrails". However, the key randomised evidence in liposarcoma (SARC024 and REGOSARC) is negative, and the authors state it does not support routine use. A high model score and a rich evidence base do not equal a positive signal. Any further work should be limited to hypothesis-driven studies, such as combination approaches or specific liposarcoma subtypes, rather than regorafenib monotherapy as a general liposarcoma treatment.
- The EU authorisation for Stivarga is cancelled, so no currently valid EU marketed product exists in the compiled data.

**To proceed, the following is needed:**
- Subtype-level results from SARC024 (e.g. well-differentiated, dedifferentiated, myxoid and pleomorphic liposarcoma) to check for any responsive subgroup
- Clarification of the EU market status (reasons for and date of cancellation)
- Warnings, contraindications and mechanism-of-action data from the SmPC and DrugBank
- A safety monitoring plan for the known class toxicities (hepatic, dermatological, hypertension) and for the major interactions with anticoagulants and antiplatelet agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

