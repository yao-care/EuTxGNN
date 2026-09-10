---
layout: default
title: Gimeracil
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil: From Gastric Cancer (S-1 Component) to Colonic Neoplasm

## One-Sentence Summary

Gimeracil is the dihydropyrimidine dehydrogenase (DPD)-inhibiting component of the S-1 combination (tegafur + gimeracil + oteracil), which was developed to boost 5-FU-based chemotherapy against gastric cancer. The TxGNN model predicts it may also be effective for **Colonic Neoplasm**, with **8 clinical trials** (including 2 completed Phase 3 RCTs) and **14 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not individually licensed — Gimeracil is a component of the S-1 combination (tegafur/gimeracil/oteracil), historically used for gastric cancer |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Gimeracil as a standalone entity (DrugBank MOA field: data gap). Based on known information from the evidence pack, Gimeracil is part of the S-1 combination (tegafur + gimeracil + oteracil); its efficacy — via this combination — in gastric cancer has been established, and mechanistically it may be applicable to colonic neoplasm as well.

Within S-1, gimeracil inhibits DPD, the enzyme that degrades 5-fluorouracil (5-FU), thereby prolonging and enhancing the antitumour activity of tegafur (a 5-FU prodrug) without requiring continuous infusion. Gastric cancer and colorectal cancer are both gastrointestinal adenocarcinomas that respond to fluoropyrimidine-based chemotherapy, so a mechanism validated in gastric cancer is pharmacologically plausible in colonic neoplasm.

This plausibility is corroborated by the evidence itself: S-1 (the tegafur/gimeracil/oteracil combination) already has an extensive clinical trial record in colorectal cancer, including large completed Phase 3 trials comparing it against standard regimens such as capecitabine and UFT/leucovorin, which supports the reasonableness of the TxGNN prediction rather than treating it as a purely novel hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (oxaliplatin+S-1) vs XELOX as adjuvant chemotherapy for Stage III colorectal cancer |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | S-1 vs capecitabine as first-line treatment for metastatic colorectal cancer (SALTO study) |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+leucovorin vs S-1 (TS-1) as adjuvant treatment for Stage III colon cancer |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL) in untreated metastatic colorectal cancer |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1/capecitabine + oxaliplatin effects on coronary microvascular function in metastatic GI adenocarcinoma |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after prior chemotherapy failure |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic colorectal cancer after standard chemotherapy failure |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib + tegafur/gimeracil/oteracil as third-line treatment in advanced metastatic CRC |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Clinical study | Zhonghua Zhong Liu Za Zhi | Efficacy and side effects of oxaliplatin + S-1 in postoperative colorectal cancer patients |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Retrospective/observational | Gan To Kagaku Ryoho | Risk factors for grade 3–4 haematological toxicity with S-1 + irinotecan in colonic cancer (n=87; 16.1% incidence) |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinical/mechanism | Oncology Reports | Irinotecan overcomes 5-FU resistance via thymidylate synthase down-regulation in colon cancer xenografts treated with S-1 components |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Preclinical | Gan To Kagaku Ryoho | Pharmacokinetic study of S-1 for peritoneal metastasis from colon cancer in a mouse model |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case report | Anticancer Research | Complete response maintained with S-1 + CPT-11 in hepatic metastases of colon cancer |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Case report | Gan To Kagaku Ryoho | Repeated laparoscopic resection for peritoneal recurrence after UFT/leucovorin adjuvant chemotherapy in colon cancer |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case report | Gan To Kagaku Ryoho | Two-stage hepatectomy for irresectable colorectal liver metastases after SOX (S-1+oxaliplatin) + panitumumab |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Case report | Gan To Kagaku Ryoho | Transverse colon cancer with liver metastasis and portal vein tumour thrombosis managed with chemotherapy |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case report | J Oncol Pharm Pract | Hypertriglyceridaemia induced by S-1 in a colorectal cancer patient |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Case report | Eur J Dermatol | TS-1 (tegafur/gimeracil/oteracil)-induced erythroderma with extensive mucosal involvement and hand-foot syndrome |

## EU Market Information

No EU marketing authorization is currently on file for Gimeracil. `taiwan_regulatory` reports market status as "Not Marketed" with 0 authorizations — consistent with Gimeracil being a formulation component of the S-1 combination rather than a standalone marketed product in this dataset.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — fluoropyrimidine-modulating agent (DPD inhibitor component of the S-1 combination) |
| Myelosuppression Risk | Medium — grade 3–4 haematological toxicity reported at 16.1% with S-1 + irinotecan combination (PMID 21084813) |
| Emetogenicity Classification | Low to Medium (consistent with fluoropyrimidine-based regimens) |
| Monitoring Items | CBC with differential, liver and renal function, serum triglycerides (per PMID 32936722), skin/mucosal reactions (erythroderma, hand-foot syndrome per PMID 28414195) |
| Handling Protection | Yes — must follow cytotoxic drug handling precautions as part of the S-1 combination regimen |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (NCT01918852, NCT00660894) plus multiple Phase 1/2 trials support the efficacy of S-1 (containing gimeracil) in colorectal cancer, and the underlying DPD-inhibition mechanism plausibly extends from gastric to colonic neoplasms. However, Gimeracil itself carries no independent EU marketing authorization, and both mechanism-of-action and TFDA label/safety data are flagged as blocking data gaps.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001, blocking — required before any S1 safety assessment)
- Detailed mechanism-of-action documentation from DrugBank (DG002, high priority)
- Confirmation of the regulatory/marketing status of the full S-1 combination product (not Gimeracil alone) in the EU
- Drug-drug interaction data (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

