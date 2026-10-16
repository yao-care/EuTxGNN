---
layout: default
title: Trastuzumab
parent: High Evidence (L1-L2)
nav_order: 635
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Trastuzumab: predicted new indication Progesterone-receptor positive breast cancer (evidence level L1). Approved use: HER2-positive metastatic breast cancer (MBC)…"
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Trastuzumab: From HER2-Positive Breast and Gastric Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab is a HER2-targeted monoclonal antibody, originally used for HER2-positive metastatic and early breast cancer and HER2-positive metastatic gastric cancer.
The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**,
with **14 clinical trials** and **20 publications** currently linked to this prediction. This is largely an on-label use in HER2-positive disease rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive metastatic breast cancer (MBC), early breast cancer (EBC), and HER2-positive metastatic gastric cancer |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| EU Market Status | Cancelled only (no currently valid authorizations in the data compiled) |
| Number of Authorizations | 10 (all cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Trastuzumab binds the extracellular domain of HER2, blocks HER2 signalling and mediates antibody-dependent cellular cytotoxicity. Detailed mechanism-of-action data were not available in the drug record, but this mechanism is well established.

HER2-positive tumours are frequently also progesterone-receptor (PR) positive (the HER2+/HR+ subtype). These patients are already covered by the approved breast cancer indications, including trastuzumab combined with an aromatase inhibitor for postmenopausal patients with hormone-receptor-positive metastatic disease. Benefit depends on HER2 status, not PR status. The high TxGNN score therefore reflects a real biological and clinical link, but the prediction describes existing use in a HER2-positive subgroup.

Other predicted indications in the same output differ in strength. Predictions for PR-negative breast cancer and luminal A/B breast tumours are similarly on-label when HER2 is confirmed. Predictions for rare tumours (for example ectomesenchymoma, HHV-8-related tumours and middle ear neuroendocrine tumour) rest on the knowledge-graph score only, with no supporting trials or literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy with or without trastuzumab in node-positive or high-risk node-negative breast cancer |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Pertuzumab biosimilar QL1209 plus trastuzumab and docetaxel in HER2-positive, ER/PR-negative early or locally advanced breast cancer |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | Completed | 92 | Neoadjuvant chemotherapy with or without trastuzumab |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Phase 2 | Completed | 50 | Dose-dense neoadjuvant chemotherapy in HER2-positive breast cancer, hormone receptor negative or positive |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Phase 2 | Completed | 36 | Cabozantinib alone or with trastuzumab in breast cancer brain metastases |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | Unknown | 34 | Palbociclib, trastuzumab, pyrotinib and fulvestrant in ER/PR-positive, HER2-positive brain metastases |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole plus trastuzumab in ErbB2-positive, ER and/or PR-positive metastatic breast cancer |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib, aromatase inhibitor and trastuzumab in ER-positive, HER2-positive cancers |
| [NCT02774681](https://clinicaltrials.gov/study/NCT02774681) | Phase 2 | Terminated | 12 | Palbociclib in HER2-positive metastatic breast cancer with brain metastasis; stopped early |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Completed | 37 | Everolimus, letrozole and trastuzumab in hormone receptor-positive, HER2-positive advanced breast cancer |

Other linked records (withdrawn trials with no enrolment, a non-interventional brain-function study, and an early-phase platform trial) provide no efficacy evidence. One Phase 3 trial (NCT00053339, trastuzumab with or without tamoxifen) was withdrawn with no participants enrolled.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncol | monarcHER: abemaciclib plus trastuzumab with or without fulvestrant versus trastuzumab plus chemotherapy in HR-positive, HER2-positive advanced breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | Lancet Oncol | NeoSphere 5-year analysis: neoadjuvant pertuzumab and trastuzumab in HER2-positive breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT HER2+/HR-: de-escalation with trastuzumab and pertuzumab ± paclitaxel |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | Meta-analysis | N Engl J Med | Risk of recurrence after stopping endocrine therapy at 5 years in ER-positive early breast cancer |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-analysis | Lancet | Overview of randomised trials of chemotherapy and hormonal therapy in early breast cancer |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Multi-cohort analysis | Theranostics | Molecular portraits and trastuzumab responsiveness of ER-positive, PR-positive, HER2-positive (triple-positive) breast cancer |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Review | Nat Rev Clin Oncol | HER2 and hormone receptor-positive breast cancer: combining anti-HER2 therapy with aromatase inhibitors |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncol | Current trends in the treatment of HR+/HER2+ breast cancer, including chemotherapy-free options |
| [26321480](https://pubmed.ncbi.nlm.nih.gov/26321480/) | 2015 | Review | Breast | Biology of luminal HER2 versus HER2-enriched subtypes and therapeutic implications |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Targeted and cytotoxic inhibitors in breast cancer, organised by HER2/HR/ER/PR status |

The pivotal adjuvant trial of trastuzumab with chemotherapy in HER2-positive breast cancer ([16236738](https://pubmed.ncbi.nlm.nih.gov/16236738/), N Engl J Med, 2005) was linked to the luminal A/B prediction rather than this one.

---

## EU Market Information

All 10 EU authorizations in the data compiled are cancelled; none is currently valid.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000278 | Herceptin | Not specified | HER2-positive metastatic breast cancer, early breast cancer, and metastatic gastric cancer... |
| EMEA/H/C/004323 | Ontruzant | Not specified | Breast cancer, metastatic breast cancer: HER2 positive metastatic breast cancer (MBC) as monotherapy... |
| EMEA/H/C/004361 | Kanjinti | Not specified | Metastatic breast cancer Kanjinti is indicated for the treatment of adult patients with HER2 positive... |
| EMEA/H/C/004463 | Trazimera | Not specified | Breast cancer Metastatic breast cancer Trazimera is indicated for the treatment of adult patients with... |
| EMEA/H/C/002575 | Herzuma | Not specified | Breast cancer Metastatic breast cancer Herzuma is indicated for the treatment of adult patients with... |

Five further cancelled authorizations are on record: Tuznue, Herwenda, Zercepac, Ogivri and Dazublys.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (risk is mainly from the chemotherapy it is combined with) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Cardiac function (cardiotoxicity is a documented concern, PMID 17687157); haematological parameters when combined with chemotherapy |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 94 interactions were identified. Major-level examples include deferiprone, samarium (153Sm) lexidronam, adalimumab and baricitinib. Moderate-level examples include paclitaxel, warfarin, alemtuzumab, azathioprine and palifermin.
- **Cardiotoxicity**: The linked literature describes trastuzumab-related cardiotoxicity and questions the assumption that it is fully reversible.

For label warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A large completed Phase 3 randomized trial (3270 patients) and multiple RCTs support trastuzumab in HER2-positive breast cancer, including HR-positive disease, and the use is already within approved indications. The prediction is clinically valid only when HER2 overexpression or amplification is confirmed; PR status alone does not predict benefit.

**To proceed, the following is needed:**
- Mandatory HER2 testing with an accurate, validated assay before treatment
- Confirmation of current EU marketing status, since all 10 authorizations in the data are cancelled
- Retrieval of the SmPC warnings and contraindications, which were not available in the data compiled
- Detailed mechanism-of-action data from DrugBank
- A cardiac monitoring plan, particularly with anthracycline-containing regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

