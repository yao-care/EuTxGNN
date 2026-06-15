---
layout: default
title: Apalutamide
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Apalutamide
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

# Apalutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Apalutamide (Erleada®) is a second-generation androgen receptor (AR) inhibitor approved in the US and EU for metastatic castration-sensitive prostate cancer (mCSPC) and non-metastatic castration-resistant prostate cancer (nmCRPC), though not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Male Reproductive Organ Cancer** broadly — a category spanning multiple prostate cancer stages and subtypes — with **50+ clinical trials** and **18 publications** supporting this direction.
Evidence is anchored by the landmark Phase 3 TITAN and SPARTAN trials, placing this prediction at the highest evidence level (L1).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (mCSPC; nmCRPC) |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 97.41% |
| Evidence Level | L1 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on prediction selection**: TxGNN's highest-ranked prediction (Rank 1: "prostate cancer/brain cancer susceptibility", score 98.43%) represents a genetic susceptibility category rather than a treatment target — the repurposing rationale in the evidence pack explicitly flags this as a likely knowledge-graph proximity artifact with no direct mechanistic link. This report therefore focuses on **Male Reproductive Organ Cancer** (Rank 8, score 97.41%) as the most evidence-supported and clinically actionable prediction.

---

## Why is This Prediction Reasonable?

Apalutamide is a potent, selective second-generation nonsteroidal androgen receptor inhibitor. It binds directly to the ligand-binding domain of the AR, blocking AR nuclear translocation and DNA binding, thereby preventing transcriptional activation of androgen-responsive genes that drive tumor cell proliferation and survival. Unlike first-generation antiandrogens such as bicalutamide, apalutamide remains fully antagonistic even under conditions of AR overexpression — a key feature underlying its superior clinical efficacy.

Prostate cancer is the dominant malignancy within the "male reproductive organ cancer" disease category, and it is fundamentally an AR-dependent disease across all stages: hormone-sensitive (castration-naïve), castration-resistant, non-metastatic, and metastatic. Because Apalutamide's mechanism directly targets the core growth driver of prostate cancer, the TxGNN prediction captures a well-grounded mechanistic and biological overlap. The TxGNN score reflects the high node-proximity between Apalutamide's pharmacological targets and the disease nodes within the knowledge graph — not simply a spurious correlation.

Beyond already-approved indications, Phase 3 trials are actively evaluating Apalutamide in additional clinical settings within this disease category: neoadjuvant and adjuvant therapy for high-risk localized prostate cancer (NCT03767244, n=2,517), adjuvant post-prostatectomy therapy (NCT04295447), and combination with radiotherapy for locally advanced disease (NCT04557059). The prediction therefore aligns closely with Apalutamide's established and emerging clinical development trajectory, identifying a label-broadening opportunity that extends well-characterised AR-inhibition benefits across the full spectrum of male reproductive organ cancers.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03767244](https://clinicaltrials.gov/study/NCT03767244) | Phase 3 | Active, Not Recruiting | 2,517 | Apalutamide + ADT vs placebo + ADT before and after radical prostatectomy in high-risk localized/locally advanced prostate cancer; co-primary endpoints: pathological complete response rate and metastasis-free survival |
| [NCT02489318](https://clinicaltrials.gov/study/NCT02489318) | Phase 3 | Active, Not Recruiting | 1,052 | TITAN: Apalutamide + ADT vs ADT alone in metastatic hormone-sensitive prostate cancer; demonstrated superior radiographic progression-free survival and overall survival |
| [NCT04557059](https://clinicaltrials.gov/study/NCT04557059) | Phase 3 | Active, Not Recruiting | 694 | Apalutamide added to radiotherapy + LHRHa in high-risk hormone-sensitive prostate cancer; progressive disease defined by PSMA-PET imaging |
| [NCT06592924](https://clinicaltrials.gov/study/NCT06592924) | Phase 3 | Recruiting | 830 | Addition of docetaxel to androgen receptor pathway inhibitor therapy in mCSPC patients with suboptimal PSA response |
| [NCT03124433](https://clinicaltrials.gov/study/NCT03124433) | Phase 2 | Completed | 30 | NEAR trial: Neoadjuvant apalutamide monotherapy before radical prostatectomy in D'Amico intermediate-to-high-risk prostate cancer; evaluated tumor downstaging and oncologic efficacy |
| [NCT01171898](https://clinicaltrials.gov/study/NCT01171898) | Phase 1/2 | Completed | 127 | First-in-human study of ARN-509 in advanced castration-resistant prostate cancer; established the tolerable dose range, pharmacokinetics, and proof-of-concept activity |
| [NCT02903368](https://clinicaltrials.gov/study/NCT02903368) | Phase 2 | Completed | 118 | Neoadjuvant + adjuvant abiraterone + apalutamide for intermediate-to-high-risk prostate cancer undergoing prostatectomy; assessed pathological response and tissue/radiographic biomarkers |
| [NCT03899077](https://clinicaltrials.gov/study/NCT03899077) | Phase 2 | Unknown | 202 | Salvage radiotherapy + 6-month ADT vs salvage radiotherapy + apalutamide in hormone-naïve patients with biochemical progression after radical prostatectomy |
| [NCT04295447](https://clinicaltrials.gov/study/NCT04295447) | Phase 2 | Active, Not Recruiting | 190 | Adjuvant apalutamide vs standard of care in high-risk prostate cancer post-prostatectomy; primary endpoint: biochemical recurrence-free survival |
| [NCT02867020](https://clinicaltrials.gov/study/NCT02867020) | Phase 2 | Completed | 128 | Head-to-head comparison of abiraterone + ADT vs apalutamide monotherapy vs abiraterone + apalutamide in hormone-naïve locally advanced or metastatic prostate cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33914595](https://pubmed.ncbi.nlm.nih.gov/33914595/) | 2021 | Phase 3 RCT | J Clin Oncol | TITAN final survival analysis: Apalutamide + ADT significantly improved OS and rPFS in mCSPC after unblinding and placebo-to-apalutamide crossover |
| [29420164](https://pubmed.ncbi.nlm.nih.gov/29420164/) | 2018 | Phase 3 RCT | N Engl J Med | SPARTAN: Apalutamide significantly extended metastasis-free survival vs placebo in high-risk non-metastatic CRPC |
| [31150574](https://pubmed.ncbi.nlm.nih.gov/31150574/) | 2019 | Phase 3 RCT | N Engl J Med | TITAN first analysis: Apalutamide + ADT prolonged radiographic PFS and overall survival in metastatic castration-sensitive prostate cancer |
| [32907777](https://pubmed.ncbi.nlm.nih.gov/32907777/) | 2021 | Phase 3 RCT Follow-up | Eur Urol | SPARTAN final OS analysis: Apalutamide confirmed overall survival benefit in nmCRPC with PSA doubling time ≤10 months |
| [38261983](https://pubmed.ncbi.nlm.nih.gov/38261983/) | 2024 | Phase 3 RCT | J Clin Oncol | PRESTO: Intensification of androgen blockade with apalutamide + abiraterone in high-risk biochemically relapsed castration-sensitive prostate cancer after radical prostatectomy |
| [36167599](https://pubmed.ncbi.nlm.nih.gov/36167599/) | 2023 | Phase 2 RCT | Eur Urol | ARNEO: Neoadjuvant degarelix with or without apalutamide before radical prostatectomy in high-risk prostate cancer; evaluated androgen deprivation response |
| [35091711](https://pubmed.ncbi.nlm.nih.gov/35091711/) | 2022 | Phase 2 Trial | Prostate Cancer Prostatic Dis | NEAR trial: Neoadjuvant apalutamide monotherapy with radical prostatectomy in intermediate-to-high-risk prostate cancer; efficacy and tumor downstaging outcomes |
| [39417629](https://pubmed.ncbi.nlm.nih.gov/39417629/) | 2025 | Comparative Study | The Prostate | Real-world multicenter comparison of abiraterone, enzalutamide, and apalutamide in mHSPC; assessed differential efficacy and safety across ARPI agents |
| [33480983](https://pubmed.ncbi.nlm.nih.gov/33480983/) | 2021 | Review | Endocr Rev | Comprehensive review of hormonal therapy evolution in prostate cancer from gonadal testosterone deprivation to direct AR inhibition; covers resistance mechanisms |
| [32930958](https://pubmed.ncbi.nlm.nih.gov/32930958/) | 2020 | Drug Review | Drugs | Apalutamide (Erleada®) clinical pharmacology review in mCSPC; summarises Phase 3 TITAN data, dosing, tolerability, and regulatory status |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation nonsteroidal androgen receptor (AR) inhibitor |
| Myelosuppression Risk | Low — not a conventional cytotoxic agent; clinically significant myelosuppression is not an expected adverse effect |
| Emetogenicity Classification | Low |
| Monitoring Items | Thyroid function (TSH; hypothyroidism risk), liver function (ALT/AST), PSA (treatment response), bone density (fracture risk with prolonged androgen deprivation), neurological assessment (falls/seizure risk) |
| Handling Protection | Standard handling; dedicated cytotoxic drug handling protocols not required |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3 RCTs — including TITAN (mCSPC, n=1,052) and SPARTAN (nmCRPC) — have firmly established Apalutamide's efficacy and safety across the prostate cancer spectrum, constituting L1-level evidence for the male reproductive organ cancer category. The drug's AR-inhibition mechanism is well-characterised and directly aligned with disease biology. However, Apalutamide is currently not marketed in Taiwan, and complete local safety data are not yet available for this evidence pack.

**To proceed, the following is needed:**
- Taiwan TFDA market authorisation application and regulatory pathway analysis
- Full SmPC safety review, with particular attention to drug-drug interactions (Apalutamide is a strong CYP3A4 and CYP2C19 inducer with clinically significant interaction potential)
- Taiwan-specific pharmacoeconomic analysis and National Health Insurance reimbursement strategy
- Definition of priority patient population for initial Taiwan market entry (nmCRPC vs mCSPC vs neoadjuvant/adjuvant settings)
- Long-term safety monitoring plan addressing fractures, falls, cardiovascular events, and hypothyroidism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

