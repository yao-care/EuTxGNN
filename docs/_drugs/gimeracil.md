---
layout: default
title: Gimeracil
parent: AI Predictions (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Gimeracil: predicted new indication Colonic neoplasm (evidence level L5). Approved use: Advanced gastric cancer (with cisplatin)"
monitor_inn: "Gimeracil"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "lipoma of colon", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "colonic lymphangioma", "colon leiomyoma"]
---

# Gimeracil
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

# Gimeracil: From Gastric and Metastatic Colorectal Cancer to Colonic Neoplasm

## One-Sentence Summary

Gimeracil is a component of the S-1 combination (tegafur/gimeracil/oteracil), originally used for advanced gastric cancer and, in specific settings, metastatic colorectal cancer.
The TxGNN model predicts it may be effective for **colonic neoplasm**, with **6 clinical trials** and **12 publications** currently supporting this direction. Note that the trial evidence concerns the S-1 combination, not gimeracil alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced gastric cancer (with cisplatin); metastatic colorectal cancer in patients who cannot continue another fluoropyrimidine because of hand-foot syndrome or cardiovascular toxicity |
| Predicted New Indication | Colonic neoplasm |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 (see note below) |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Only one Phase 3 trial (NCT00660894) is completed. Another Phase 3 trial (NCT03448549) has an unknown status. Strictly applying the rule (≥2 completed Phase 3 RCTs), the evidence is closer to L2. The L1 label is retained from the compiled scoring, but it should be interpreted cautiously.

## Why is This Prediction Reasonable?

Gimeracil is a potent inhibitor of dihydropyrimidine dehydrogenase (DPD), the enzyme that breaks down 5-fluorouracil (5-FU). In S-1, tegafur is the 5-FU prodrug, and gimeracil blocks 5-FU breakdown, so 5-FU levels stay high and sustained, strengthening the antitumour effect. Oteracil reduces gastrointestinal toxicity. Detailed mechanism data were not available in the compiled drug record, so this description is based on the known pharmacology of S-1.

Gastric cancer and colonic neoplasm are both gastrointestinal tumours that respond to fluoropyrimidines. The EU label for Teysuno already covers metastatic colorectal cancer in a restricted setting, so this prediction is largely an on-label or near-label use rather than true repurposing. Gimeracil has no independent antitumour role, so any benefit comes from the S-1 combination.

Among the other predictions, rectosigmoid junction neoplasm and cardia cancer have only indirect support (anatomical or histological extrapolation from colorectal and gastric adenocarcinoma, and a single case report for cardia cancer). The remaining predictions, mostly benign or biologically distinct conditions, have no supporting evidence and should be held.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+leucovorin vs S-1 as adjuvant treatment for stage III colon cancer; strongest direct evidence for S-1 in colon cancer |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (oxaliplatin + S-1) vs XELOX as adjuvant chemotherapy for stage III colorectal cancer; motivated by capecitabine hand-foot syndrome |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable or recurrent colorectal cancer after failure of irinotecan and oxaliplatin regimens |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic colorectal cancer after standard chemotherapy failure; primary endpoint is progression-free survival |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fruquintinib + tegafur/gimeracil/oteracil as third-line treatment of advanced metastatic colorectal cancer; single-arm |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | Coronary artery blood flow effects of S-1 vs capecitabine with oxaliplatin in metastatic GI adenocarcinoma; a cardiovascular safety study |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinical (xenograft) | Oncol Rep | Irinotecan combined with S-1 overcame 5-FU resistance in colon cancer xenografts by down-regulating thymidylate synthase |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Pharmacokinetic study | Gan To Kagaku Ryoho | S-1 pharmacokinetics in a mouse model of colon cancer peritoneal metastasis |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Retrospective analysis | Gan To Kagaku Ryoho | Risk factors for grade 3-4 haematological toxicity with S-1 + irinotecan in 87 patients with unresectable or recurrent colonic cancer (rate 16.1%) |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case report | Anticancer Res | Complete response maintained with S-1 + irinotecan in hepatic metastases of colon cancer |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case report | Gan To Kagaku Ryoho | SOX plus panitumumab as downstaging chemotherapy enabling two-stage hepatectomy for colorectal liver metastases |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case report | J Oncol Pharm Pract | Hypertriglyceridaemia induced by S-1, with literature review |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Case report | Eur J Dermatol | TS-1-induced erythroderma with extensive mucosal involvement and hand-foot syndrome |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Case report | Gan To Kagaku Ryoho | Urinary retention linked to oxaliplatin-induced acute peripheral neuropathy after tegafur/gimeracil/oteracil and CAPOX+BEV |

No randomised controlled trial publications were identified; the literature is mainly preclinical work and case reports.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001242 (cancelled) | Teysuno | Not specified | Adults: advanced gastric cancer in combination with cisplatin; metastatic colorectal cancer as monotherapy or combined with oxaliplatin or irinotecan, with or without bevacizumab, when another fluoropyrimidine cannot be continued... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class, as part of S-1) |
| Myelosuppression Risk | Medium; one retrospective study reported grade 3-4 haematological toxicity in 16.1% of patients receiving S-1 + irinotecan |
| Emetogenicity Classification | Low to medium |
| Monitoring Items | Complete blood count with differential, liver and renal function, electrolytes |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the SmPC warnings and precautions for authoritative details.

## Safety Considerations

- **Reported adverse events (from the literature):** hand-foot syndrome and erythroderma with mucosal involvement, hypertriglyceridaemia, and haematological toxicity when combined with irinotecan. These come from case reports and a retrospective study, not label text.
- **Cardiovascular safety:** the terminated trial NCT02216149 specifically examined coronary blood flow effects of S-1 versus capecitabine.

Please refer to the SmPC for full warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 trial (n=1535) and several Phase 2 studies support S-1 in colon and colorectal cancer, and the EU label already covers a restricted colorectal setting. However, the evidence is for the S-1 combination rather than gimeracil alone, several trials have unknown status, and the EU authorization is cancelled.

**To proceed, the following is needed:**
- Published results of NCT00660894 and NCT03448549 to confirm efficacy and safety
- Clarification of the cancelled EU authorization status and the availability of any S-1 product
- Detailed mechanism of action data and SmPC safety information (warnings, contraindications, drug interactions)
- A safety monitoring plan, including DPD status, haematological and cardiovascular monitoring
- Hold the other nine predicted indications until supporting evidence appears; rectosigmoid junction neoplasm and cardia cancer could be considered research questions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

