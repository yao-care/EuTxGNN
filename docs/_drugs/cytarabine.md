---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Cytarabine
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

# Cytarabine: From Acute Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is a nucleoside antimetabolite with established clinical use in hematologic malignancies, particularly acute myeloid leukemia (AML).
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma (SCLC)**, with a prediction score of 99.78%.
This direction is supported by **3 registered clinical trials** (indirect relevance) and **20 publications**, including several historical Phase I/II studies that directly incorporated cytarabine into SCLC regimens between 1979 and 1988.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute myeloid leukemia (AML) and hematologic malignancies |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| EU Market Status | Not marketed (no registered authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from formal database sources. Based on established pharmacological knowledge, cytarabine is a pyrimidine nucleoside antimetabolite — after intracellular phosphorylation to its active form ara-CTP, it competitively inhibits DNA polymerase-α and becomes incorporated into elongating DNA strands, causing chain termination. This cytotoxic mechanism is strictly S-phase specific, making cytarabine most active against cells with high proliferation indices.

Small cell lung carcinoma is one of the most aggressively proliferating solid tumors, with Ki-67 indices typically exceeding 50%. This biological characteristic theoretically creates susceptibility to S-phase-specific cytotoxic agents. Historical clinical evidence confirms this hypothesis was actively explored: a 1979 study (PMID 232239) directly incorporated cytosine arabinoside into a combination regimen for 20 previously untreated SCLC patients alongside cyclophosphamide and Adriamycin. A 1984 study (PMID 6095640) tested intensive Ara-C infusion in SCLC both as monotherapy in refractory patients and as an addition to the CAV combination in extensive-stage disease. VP-16 plus infusional Ara-C was further evaluated as salvage therapy in relapsed SCLC in 1988 (PMID 2841844).

However, the landscape of SCLC treatment has fundamentally transformed since these historical studies. The current standard of care combines etoposide/platinum-based chemotherapy with PD-L1 checkpoint inhibitors (atezolizumab or durvalumab), achieving substantially improved outcomes compared to older alkylating agent combinations. Cytarabine has not been re-evaluated in modern SCLC clinical trials, and its modest response rates in historical NSCLC Phase II studies (14–18%) underscore the limitation of straightforward extrapolation. The TxGNN high prediction score likely reflects cytarabine's broad cytotoxic profile captured in the knowledge graph topology rather than SCLC-specific contemporary mechanistic validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Tested intrathecal pemetrexed for recurrent NSCLC leptomeningeal metastases; cytarabine is referenced as the existing standard for intrathecal chemotherapy, providing context for its established role in the CNS compartment |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed combined with involved-field radiotherapy for solid tumor leptomeningeal metastases; indirectly contextualizes cytarabine's position as a benchmark intrathecal agent |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy for early-stage NSCLC (vinorelbine, cisplatin, docetaxel, gemcitabine, pemetrexed); terminated early due to slow accrual; cytarabine not an investigational agent |

> No contemporary clinical trials evaluating cytarabine specifically in SCLC were identified. All retrieved trials are of low direct relevance (grade C).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Clinical Trial | Med Pediatr Oncol | 20 previously untreated SCLC patients; cyclophosphamide + Adriamycin + cytosine arabinoside (20 mg/m² q12h SC, days 5–9) combined with 3,000 rads radiotherapy; foundational direct evidence of Ara-C use in SCLC |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical Trial | Am J Clin Oncol | Intensive Ara-C (100 mg/m²/d continuous infusion) in SCLC: no responses in 10 heavily pretreated monotherapy patients; separately added to CAV backbone in 25 extensive-stage SCLC patients |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Clinical Trial | Am J Clin Oncol | 17 chemotherapy-refractory SCLC patients; VP-16 (three daily bolus doses) + infusional Ara-C (45 mg/m²/d ×72h); evaluates salvage strategy in relapsed disease |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | J Clin Oncol | CALGB randomized trial of chemotherapy + radiotherapy ± warfarin in limited-stage SCLC; cytarabine-containing backbone regimen; assesses anticoagulation benefit on response and survival |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II | Tumori | 32 advanced NSCLC patients; cisplatin (40 mg/m² days 1–3) + vindesine + cytarabine (15 mg/m² q12h days 1–3); 18% objective response rate; provides dose-finding context |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II | Cancer | 37 chemo-naive advanced NSCLC patients; high-dose cytarabine (3 g/m² IV) + cisplatin (100 mg/m²); 14% overall response rate; Grade IV myelosuppression in 32%, four treatment-related deaths |
| [2820740](https://pubmed.ncbi.nlm.nih.gov/2820740/) | 1987 | Pilot Study | Eur J Cancer Clin Oncol | Cisplatin + cytarabine combination chemotherapy in advanced NSCLC; pilot feasibility and early efficacy data |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case Series | Am J Med | 60 SCLC patients with cerebral and meningeal metastases receiving intensive chemotherapy; 78% CR + PR rate; documents cytarabine-containing regimen utility in CNS compartment SCLC |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case Report | Gan Kagaku Ryoho | Stage IV SCLC with meningeal carcinomatosis; multidisciplinary treatment including cytarabine-containing intrathecal therapy after systemic progression; illustrates current clinical practice context |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics Chemother | Comprehensive overview of Ara-C analogs developed to overcome rapid deactivation by cytidine deaminase; mechanistic foundation for understanding cytarabine's pharmacological limitations in solid tumors |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Nucleoside antimetabolite / Pyrimidine analog) |
| Myelosuppression Risk | High — bone marrow suppression is the primary dose-limiting toxicity; severe leukopenia, thrombocytopenia, and anemia are expected dose-dependent effects; Grade IV myelosuppression reported in 32% of patients at high-dose regimens (3 g/m²) (PMID 2156598) |
| Emetogenicity Classification | Low to moderate (dose-dependent; high-dose regimens ≥3 g/m² may cause more pronounced nausea and vomiting) |
| Monitoring Items | CBC with differential (nadir at days 7–14), platelet count, liver function tests (AST, ALT, bilirubin), renal function (creatinine, BUN), neurological assessment (cerebellar toxicity risk at high doses ≥1 g/m²) |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system drug transfer devices recommended; special precautions required for high-dose preparation and administration |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While historical clinical data (1979–1997) demonstrates that cytarabine was directly incorporated into SCLC regimens and provides a mechanistic basis through S-phase-specific cytotoxicity against high-proliferation tumors, the evidence is entirely from the pre-immunotherapy era and no contemporary clinical trials have re-evaluated cytarabine in SCLC. The combination of dated L3 evidence, significant toxicity at effective doses, and displacement by superior modern regimens is insufficient to support current clinical development without fresh validation.

**To proceed, the following is needed:**
- Contemporary in vitro and in vivo efficacy data in SCLC cell lines and xenograft models, benchmarked against current etoposide/platinum/immunotherapy standards
- Pharmacokinetic assessment of cytarabine tumor penetration in solid tumor (lung) settings, where rapid deamination by cytidine deaminase significantly limits systemic exposure compared to hematologic disease
- Formal mechanism of action verification via DrugBank API to document DNA polymerase inhibition relevance in SCLC context
- Evaluation of a potential niche role in SCLC CNS disease (leptomeningeal metastases) where intrathecal cytarabine delivery may bypass the pharmacokinetic limitations of systemic administration
- EU regulatory landscape survey for existing cytarabine-containing products (EMA authorization database query required)
- Exploration of potential synergy or sensitization strategies combining cytarabine with checkpoint inhibitors or targeted agents in SCLC preclinical models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

