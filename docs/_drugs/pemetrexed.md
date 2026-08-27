---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Established Oncology Indications to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate chemotherapy agent, with globally recognized use in non-small cell lung cancer and malignant pleural mesothelioma. The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, a rare and histologically related tumour, with **11 clinical trials** and **20 publications** currently supporting this direction — though no completed Phase 3 trial exists yet for this specific anatomical subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer / Malignant pleural mesothelioma (established chemotherapy indications; no EU marketing-license record found in this dataset) |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed (no license record in this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pemetrexed is not available in this dataset (data gap DG002). Based on well-established pharmacological knowledge, pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase, dihydrofolate reductase, and glycinamide ribonucleotide formyltransferase — key folate-dependent enzymes required for de novo purine and pyrimidine synthesis. This mechanism underlies its proven efficacy, in combination with a platinum agent, in mesothelioma of pleural origin.

Malignant peritoneal mesothelioma and malignant pleural mesothelioma arise from the same mesothelial cell lineage and share nearly identical histological and molecular pathological features; they differ mainly in anatomical site of origin (pleura vs. peritoneum) rather than underlying tumour biology. Because pemetrexed's antifolate mechanism is not organ-specific, its antiproliferative activity is expected to translate across mesothelial-derived tumours regardless of cavity of origin.

This mechanistic rationale is reinforced by direct clinical practice: cisplatin plus pemetrexed is already used as a de facto first-line regimen for peritoneal mesothelioma in oncology practice, extrapolated from the pleural mesothelioma evidence base (see rank-3 prediction in this same evidence pack, "Pleural Mesothelioma," which carries an L1 evidence level with multiple completed Phase 3 RCTs). This existing extrapolation pattern supports the biological plausibility of the TxGNN prediction, even though peritoneal-specific trials remain at the Phase 1/2 stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Randomized trial comparing intraperitoneal vs. intravenous chemotherapy (incl. pemetrexed-based regimens) after cytoreductive surgery + HIPEC in malignant peritoneal mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed + gemcitabine as front-line chemotherapy in pleural or peritoneal mesothelioma; assessed safety, survival, and tumour response |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial of carboplatin/pemetrexed/bevacizumab ± atezolizumab as neoadjuvant/palliative therapy for peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | PIPAC + systemic chemotherapy (cisplatin + pemetrexed) vs. systemic chemotherapy alone as 1st-line treatment; primary endpoint overall survival |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab combined with pemetrexed and cisplatin in unresectable disease; exploring efficacy, safety, and biomarkers |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Maintenance talazoparib following first-line platinum-based chemotherapy (incl. pemetrexed) in pleural or peritoneal mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | Methoxyamine (TRC102) combined with cisplatin and pemetrexed in advanced solid tumours/mesothelioma, including patients refractory to pemetrexed-cisplatin |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed, and imatinib in unresectable/metastatic mesothelioma; determined maximum tolerated dose |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 with pemetrexed and cisplatin in arginine-dependent tumours, including advanced peritoneal mesothelioma |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat with pemetrexed-cisplatin in mesothelioma (pleural/peritoneal); trial withdrawn before enrollment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | Journal of gastrointestinal oncology | Overview of diagnosis and management of malignant peritoneal mesothelioma, including systemic chemotherapy role |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Translational lung cancer research | Comprehensive review of peritoneal mesothelioma epidemiology, pathology, and treatment approaches |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | Journal of clinical medicine | Review of treatment strategies for malignant peritoneal mesothelioma, including systemic chemotherapy |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert review of anticancer therapy | Evaluates efficacy of first-line pemetrexed + cisplatin specifically in malignant peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Japanese journal of clinical oncology | Assesses efficacy and safety of pemetrexed + cisplatin as first-line therapy in advanced peritoneal mesothelioma |
| [41710652](https://pubmed.ncbi.nlm.nih.gov/41710652/) | 2026 | Retrospective cohort | Frontiers in oncology | Single-center study of pemetrexed/platinum ± bevacizumab after CRS+HIPEC in peritoneal mesothelioma |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-center cohort | Annals of surgical oncology | Analysis of treatment strategies and outcomes across a multi-center peritoneal mesothelioma population |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case series | Journal of immunotherapy | Combination chemoimmunotherapy in platinum-nonresponsive metastatic peritoneal mesothelioma |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort/Case series | Pleura and peritoneum | Bidirectional chemotherapy enabling surgery and HIPEC in initially unresectable peritoneal mesothelioma |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ case reports | Patient with peritoneal mesothelioma responding to rechallenge with cisplatin and pemetrexed, with literature review |

---

## EU Market Information

No EU marketing authorizations for pemetrexed are recorded in this dataset (market status: Not Marketed; total licenses: 0). This appears to be a data-collection gap for this specific dataset rather than a confirmed absence from the EU market, since pemetrexed is a long-established oncology agent internationally. Regulatory license data should be verified directly against the EMA product database before any go/no-go decision is finalized.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (multitargeted antifolate class — inhibits thymidylate synthase, dihydrofolate reductase, and GARFT) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (no structured toxicity dataset available; antifolate/platinum combination regimens are generally associated with clinically significant myelosuppression) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count with differential, renal function (pemetrexed is renally cleared), folate/vitamin B12 status prior to and during treatment |
| Handling Protection | Standard cytotoxic drug handling precautions apply, consistent with antineoplastic antifolate agents |

---

## Safety Considerations

Please refer to the SmPC for safety information. No structured key warnings, contraindications, or drug-drug interaction data are available in this evidence pack (DDI query status: not found); this is flagged as a **Blocking** data gap (DG001) that must be resolved before any Stage 1 safety review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 1/2 trials (several actively recruiting) and a growing body of retrospective/cohort literature directly support pemetrexed + platinum-based regimens in malignant peritoneal mesothelioma, and this extrapolation is already reinforced by the much stronger, Phase 3-validated evidence base for pemetrexed in the closely related pleural mesothelioma indication. However, no completed Phase 3 RCT exists specifically for the peritoneal subtype, capping the evidence level at L2.

**To proceed, the following is needed:**
- TFDA/EMA product label warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism of action documentation from DrugBank (currently a High-severity data gap, DG002)
- Verification of actual EU marketing authorization status (dataset shows 0 licenses, which is inconsistent with pemetrexed's known international approval history and should be re-queried)
- Monitoring of ongoing Phase 2 trials (e.g., NCT06057935, NCT05001880) for maturing efficacy and safety data specific to peritoneal mesothelioma
- A dedicated drug-drug interaction review, since the current DDI query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

