---
layout: default
title: Tegafur
parent: High Evidence (L1-L2)
nav_order: 594
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Tegafur: predicted new indication Colonic neoplasm (evidence level L1). Approved use: Advanced gastric cancer (with cisplatin)"
monitor_inn: "Tegafur"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "rectosigmoid junction neoplasm", "colonic lymphangioma", "cavernous hemangioma of colon"]
---

# Tegafur
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Tegafur: From Gastric Cancer and Metastatic Colorectal Cancer to Colonic Neoplasm

## One-Sentence Summary

Tegafur is an oral prodrug of 5-fluorouracil (5-FU), originally authorised in the EU (as Teysuno) for advanced gastric cancer and for metastatic colorectal cancer in patients who cannot continue another fluoropyrimidine.
The TxGNN model predicts it may be effective for **Colonic Neoplasm**, with **16 clinical trials** and **20 publications** currently supporting this direction.
The indication lies very close to its existing use, so this is closer to an extension of current use than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced gastric cancer (with cisplatin); metastatic colorectal cancer in patients who cannot continue another fluoropyrimidine due to hand-foot syndrome or cardiovascular toxicity |
| Predicted New Indication | Colonic neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tegafur is an oral prodrug of 5-FU, converted mainly by hepatic CYP2A6. 5-FU inhibits thymidylate synthase and is incorporated into RNA and DNA, which is the established cytotoxic mechanism in colorectal cancer.

The predicted indication is therefore mechanistically consistent with the drug's existing oncology use. Colonic neoplasm is closely related to the labelled indication of metastatic colorectal cancer. The very high TxGNN score agrees with the clinical evidence, which includes several large, completed Phase 3 trials of tegafur-based therapy (mostly UFT, tegafur-uracil) in colon and colorectal cancer.

Other lower-ranked predictions (for example cecum villous adenoma, lipoma of colon, colonic lymphangioma and cavernous hemangioma of colon) are benign lesions without clinical evidence. They are most likely artefacts of anatomical proximity in the knowledge graph and are not supported.

---

## Clinical Trial Evidence

Up to 10 of the most relevant trials are shown. Note that most trials test tegafur combinations (UFT or S-1) rather than tegafur alone.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1608 | Oral UFT + leucovorin vs 5-FU/LV in resected stage II/III colon cancer |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | Postoperative adjuvant UFT vs surgery alone in Dukes C colorectal cancer (NSAS-CC) |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2025 | Adjuvant UFT vs observation in curatively resected stage II colon cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT + leucovorin vs S-1 as adjuvant treatment for stage III colon cancer |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (S-1 + oxaliplatin) vs XELOX as adjuvant chemotherapy in stage III colorectal cancer |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Phase 3 | Unknown | 380 | UFT + PSK vs UFT + leucovorin in stage IIB/III colorectal cancer |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | Unknown | 340 | Postoperative UFT+LV regimens, with or without PSK, in stage III colorectal cancer |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | Completed | 89 | Patient-preference cross-over of capecitabine vs UFT + folinic acid in advanced colorectal cancer |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable or recurrent colorectal cancer after prior chemotherapy |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | Completed | 47 | Cetuximab, irinotecan, oxaliplatin and UFT as first-line therapy in metastatic colorectal cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT (Phase 3) | Clin Colorectal Cancer | ACTS-CC 02: S-1 + oxaliplatin vs UFT/LV as adjuvant therapy in high-risk stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT follow-up | ESMO Open | Updated 5-year survival of ACTS-CC 02; SOX was not superior to UFT/LV for disease-free survival |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Cohort study and meta-analysis | Medicine | UFT vs 5-FU as adjuvant therapy in stage II/III colon cancer (Taiwan national database) |
| [10089948](https://pubmed.ncbi.nlm.nih.gov/10089948/) | 1999 | Meta-analysis | Jpn J Clin Oncol | Individual patient data meta-analysis of randomized trials of oral fluoropyrimidines as adjuvant therapy after curative resection |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT as postoperative adjuvant chemotherapy: clinical evidence and mechanism of action |
| [16111469](https://pubmed.ncbi.nlm.nih.gov/16111469/) | 2005 | Review | Expert Rev Anticancer Ther | Stage-specific chemotherapy options in colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Guideline/Consensus | Clin Colorectal Cancer | Asian consensus on adaptation of international guidelines for metastatic colorectal cancer |
| [36676634](https://pubmed.ncbi.nlm.nih.gov/36676634/) | 2022 | Cohort study | Medicina (Kaunas) | Benefit of UFT as postoperative adjuvant chemotherapy in stage IIA colon cancer |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | Adjuvant immunochemotherapy (OK-432) vs chemotherapy with oral pyrimidines (HCFU, UFT) in colorectal cancer |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Case report (adverse event) | Cancer Chemother Pharmacol | UFT-induced haemolytic anaemia in a patient with metastatic colon cancer |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001242 (cancelled) | Teysuno | Not specified | Teysuno is indicated in adults: - for the treatment of advanced gastric cancer when given in combination with cisplatin... |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class; 5-FU prodrug) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (fluoropyrimidines generally carry a risk of neutropenia and thrombocytopenia) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function, electrolytes |
| Handling Protection | Follow standard cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the SmPC for safety information. No drug-interaction records were found in the data compiled for this report, and no contraindication edges were recorded in the knowledge graph.

Safety signals from the published literature include a case of UFT-induced haemolytic anaemia. A small terminated Phase 2 trial (NCT02216149) examined fluoropyrimidine-related coronary microvascular toxicity, a known concern for this drug class.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple large, completed Phase 3 randomized trials (NCT00378716, NCT00152230, NCT00392899, NCT00660894) support tegafur-based therapy in colon and colorectal cancer, and the mechanism is consistent with the existing oncology use. Guardrails are needed because the EU authorisation is cancelled, most evidence is for UFT or S-1 combinations rather than tegafur alone, and safety label data are missing.

**To proceed, the following is needed:**
- Safety information from the SmPC (warnings and contraindications), which is currently missing and is a blocking gap for safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Clarification of which tegafur formulation and regimen (UFT, S-1, or single agent) applies in the EU, given the cancelled authorisation
- A safety monitoring plan, including cardiovascular and haematological toxicity and DPD deficiency screening
- Predictions for benign lesions (villous adenoma, lipoma, lymphangioma, hemangioma) should be kept on Hold, as there is no supporting rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

