---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 10
---

# Olaparib
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Olaparib is an oral PARP1/2 inhibitor originally used as maintenance therapy for platinum-sensitive relapsed, BRCA-mutated high-grade serous ovarian, fallopian tube, or peritoneal cancer.
> The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**,
> with **50 clinical trials** and **20 publications** currently supporting this direction — including two completed Phase 3 RCTs (OlympiA, OlympiAD).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Maintenance treatment of platinum-sensitive relapsed, BRCA-mutated ovarian/fallopian tube/peritoneal cancer (derived from trial-level drug description in the evidence pack; not present in the regulatory license dataset) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| EU Market Status | Not marketed (per this dataset — see caveat below) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed MOA data is not populated in the drug record (`original_moa: [Data Gap]`), but the mechanism is well documented in the supporting literature within this evidence pack. Olaparib inhibits poly(ADP-ribose) polymerase (PARP1/2), blocking base-excision repair of single-strand DNA breaks. In cells with a dysfunctional homologous recombination pathway — most notably those carrying germline or somatic **BRCA1/2** mutations — this creates a state of "synthetic lethality," causing accumulation of unrepaired DNA damage and selective tumor cell death (PMID 26344419).

BRCA1/2 mutations are the shared genetic driver of hereditary breast-ovarian cancer syndrome, so the biological rationale for extending Olaparib from ovarian cancer into BRCA-mutated breast cancer is direct rather than speculative. This is reflected in the internal rationale note for this candidate: *"乳癌中 BRCA1/2 生殖系突變族群機轉明確，已為監管機關核准適應症"* — i.e., olaparib's use in germline BRCA-mutated breast cancer is mechanistically well established and already regulator-approved in multiple markets internationally (via OlympiA for adjuvant early breast cancer and OlympiAD for metastatic breast cancer).

**Regulatory caveat:** the same rationale note flags that this dataset's "Not marketed / 0 authorizations" status for this jurisdiction may reflect a **regional data gap rather than a true absence of approval** ("此資料集標記未上市可能為地區性差異"). This discrepancy should be verified against the primary regulatory source before any downstream decision is finalized.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Olaparib (AZD2281) + carboplatin in BRCA1/2-mutated breast/ovarian cancer and sporadic TNBC/ovarian cancer; dose-finding |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | Recruiting | 176 | Randomized: elacestrant + olaparib vs. olaparib alone in HR+/HER2− BRCA1/2-mutated advanced breast cancer |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib monotherapy vs. olaparib + durvalumab in BRCA-mutated, early-stage HER2− breast cancer |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | Non-randomized study of AZD2281 in known BRCA or recurrent breast/ovarian cancer; objective response rate |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | Active, not recruiting | 200 | PETREMAC — personalized primary medical treatment for high-risk mammary cancer, incl. PARP-inhibitor arm |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin-olaparib vs. capecitabine as first-line treatment in BRCA1/2-mutated, HER2− advanced breast cancer |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib + radiation therapy in inflammatory/locoregionally advanced/metastatic TNBC |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | Active, not recruiting | 36 | Olaparib + navitoclax (Bcl-2/Bcl-XL inhibitor) in BRCA1/2/PALB2-mutated TNBC and recurrent HGSC |
| [NCT05209529](https://clinicaltrials.gov/study/NCT05209529) | Phase 2 | Withdrawn | 0 | Neoadjuvant olaparib ± durvalumab in BRCA-associated TNBC (pathological complete response endpoint) |
| [NCT04417192](https://clinicaltrials.gov/study/NCT04417192) | Phase 2 | Completed | 30 | Preoperative olaparib monotherapy vs. olaparib + pembrolizumab in HRD-positive gynecologic/breast malignancy setting |

*(50 trials total were retrieved for this indication; the 10 most directly relevant to breast cancer are shown above.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib significantly improves invasive disease-free survival in germline BRCA1/2-mutated, HER2− early breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA overall survival analysis confirms sustained benefit of adjuvant olaparib in high-risk early breast cancer |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib monotherapy shows antitumor activity in germline BRCA-mutated metastatic breast cancer |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final OS results: olaparib vs. chemotherapy of physician's choice in gBRCA/HER2− metastatic breast cancer |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD extended follow-up confirms OS and safety profile of olaparib in gBRCA metastatic breast cancer |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT | J Clin Oncol | TBCRC 048: olaparib activity in metastatic breast cancer with somatic BRCA or non-BRCA HRR gene mutations |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT | Nature | PARTNER trial: neoadjuvant olaparib + chemotherapy in germline BRCA wild-type triple-negative breast cancer |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel increases pathologic complete response in HER2− stage II/III breast cancer |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors (olaparib, talazoparib) approved for gBRCA-mutated, HER2− breast cancer |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | Phase 1 | J Clin Oncol | Olaparib monotherapy activity across the spectrum of BRCA1/2-associated cancers, including breast cancer |

*(20 publications total were retrieved for this indication; the 10 highest-tier items are shown above.)*

---

## EU Market Information

No marketing authorization records are present for Olaparib in this dataset (0 licenses on file). Given that Olaparib (Lynparza®) is a globally established PARP inhibitor with two completed Phase 3 RCTs supporting breast cancer use (OlympiA, OlympiAD), **this is very likely a data completeness gap in the regulatory dataset rather than a true absence of market authorization** — as also flagged in the model's own rationale text. This should be independently verified against the primary regulator/SmPC source before finalizing any decision.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — PARP1/2 inhibitor acting via synthetic lethality in homologous-recombination-deficient (e.g., BRCA1/2-mutated) tumor cells; not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (no drug-specific hematologic toxicity data provided in this evidence pack) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: this evidence pack flags a **Blocking**-severity data gap (DG001) for TFDA-equivalent label warnings/contraindications, and a **High**-severity gap (DG002) for mechanism-of-action documentation. Neither can currently be sourced from DrugBank/regulatory data in this pack.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (OlympiA for adjuvant early breast cancer, OlympiAD for metastatic breast cancer) plus a broad supporting body of Phase 1–2 trials and reviews give this candidate L1-level evidence — the mechanistic link (BRCA1/2-driven synthetic lethality) is strong and well precedented. However, the regulatory record in this dataset (0 authorizations, "not marketed") and the missing safety/MOA fields are unresolved and must be closed before this indication can move past guardrailed review.

**To proceed, the following is needed:**
- TFDA/EU label warnings and contraindications (DG001 — Blocking; currently prevents S1 safety screening)
- Confirmed DrugBank mechanism-of-action record (DG002 — High)
- Reconciliation of the "Not marketed / 0 licenses" status against actual EU marketing authorization records for Lynparza®/olaparib
- A jurisdiction-specific safety monitoring plan (hematologic toxicity, renal function) informed by the SmPC once retrieved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

