---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Pibrentasvir is the NS5A-inhibitor component of the glecaprevir/pibrentasvir combination (marketed as Maviret/Mavyret), approved for chronic hepatitis C virus (HCV) infection.
> The TxGNN model assigns a **99.84%** score to **Hepatitis B Virus (HBV) infection** as a possible new indication,
> but a closer review of the **14 clinical trials** and **20 publications** cited as "evidence" shows they are almost entirely HCV efficacy trials in which HBV appears only as a co-infection screening/exclusion criterion — not as a treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C virus (HCV) infection (Pibrentasvir is the NS5A-inhibitor component of glecaprevir/pibrentasvir) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (per source scoring; see caveat below — evidence base is largely mismatched) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

The structured DrugBank MOA field for this candidate is currently a data gap. However, the evidence pack's own analysis confirms Pibrentasvir's mechanism: it is a **HCV NS5A inhibitor**, active against the Flaviviridae family virus that causes hepatitis C, and is co-formulated with glecaprevir (an NS3/4A protease inhibitor) as Mavyret/Maviret.

HBV, by contrast, is a Hepadnaviridae (a DNA reverse-transcribing virus), with a replication cycle (via an RNA pregenome and reverse transcriptase) that is fundamentally different from HCV's RNA-dependent RNA polymerase replication machinery. **NS5A has no known homologous target in HBV**, so there is no established mechanistic bridge between Pibrentasvir's mode of action and HBV suppression.

Critically, when the cited clinical trials were checked against their actual protocols, they are not HBV treatment trials at all — they are HCV registration trials (e.g., ENDURANCE-3, SURVEYOR-I/II, CERTAIN-1/2) in which HBV co-infection was typically an **exclusion criterion** or a baseline screening variable, not a study endpoint. The evidence pack's own reviewer notes this explicitly: *"the listed trials are, after verification of titles against known indications, entirely HCV treatment trials... HBV was only a co-infection screening/exclusion criterion for enrolled subjects, not the primary efficacy target — this is a data-matching artifact, not genuine repurposing evidence."* This same pattern repeats across nearly every other predicted indication in this candidate's list (HIV, HAV, HEV, Omsk hemorrhagic fever, Kyasanur forest disease, SIV, feline AIDS, and even an unrelated rare pediatric neurodevelopmental disorder), suggesting the high TxGNN score reflects **disease-embedding proximity within a broad "viral hepatitis / immunodeficiency virus" cluster**, rather than a genuine biological signal.

---

## Clinical Trial Evidence

*Note: All trials below are registered studies of glecaprevir/pibrentasvir (ABT-493/ABT-530) for **hepatitis C**, not hepatitis B. They are listed here for transparency, but none constitutes direct efficacy evidence for the predicted HBV indication.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ENDURANCE-3: ABT-493/ABT-530 vs. sofosbuvir+daclatasvir in HCV genotype 3. HBV not a study endpoint (Grade C: HBV only a co-infection screening criterion). |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Completed | 141 | Efficacy/safety of ABT-493/ABT-530 ± ribavirin in HCV patients who failed prior DAA therapy. HCV-only endpoint (Grade C). |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV co-infected patients — not an HBV study (Grade C). |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | G/P ± ribavirin in HCV genotype 1 patients previously treated with NS5A inhibitor + sofosbuvir. |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Completed | 694 | SURVEYOR-II: ABT-493/ABT-530 ± ribavirin in HCV genotypes 2–6. |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | SURVEYOR-I: ABT-493/ABT-530 ± ribavirin in HCV genotypes 1, 4–6. |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Completed | 295 | CERTAIN-1: ABT-493/ABT-530 in Japanese adults with chronic HCV. |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Completed | 384 | Long-term follow-up of DAA resistance durability in prior HCV trial participants. |
| [NCT02296905](https://clinicaltrials.gov/study/NCT02296905) | Phase 1 | Completed | 24 | PK/safety of ABT-493/ABT-530 in subjects with hepatic impairment (not HBV-specific). |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | Completed | 136 | CERTAIN-2: ABT-493/ABT-530 vs. sofosbuvir+ribavirin in Japanese HCV genotype 2 patients. |

---

## Literature Evidence

*Note: The 20 publications retrieved for this candidate discuss hepatitis C treatment, HCV/HBV epidemiology comparisons, or co-infection management context — none reports direct antiviral activity or clinical efficacy of Pibrentasvir against HBV.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | The Lancet Infectious Diseases | Discusses HBV **vaccination** after HCV treatment cure — not Pibrentasvir efficacy against HBV. |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review (pending) | Lancet Gastroenterol Hepatol | Overview of HCV infection in children/adolescents; DAA regimens discussed only for HCV. |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review (pending) | World J Gastroenterol | Notes that HBV treatment "is currently far from being curative," contrasted with HCV DAA success — not evidence of Pibrentasvir activity on HBV. |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report (pending) | AIDS Reviews | Global HBV/HCV burden estimates and WHO elimination roadmap; no drug-specific HBV data. |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective (pending) | Klin Mikrobiol Infekc Lek | Retrospective review of antiviral treatment for chronic HBV **and** HCV in children (Ostrava) — separate cohorts/regimens, not Pibrentasvir-for-HBV data. |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional (pending) | Annals of Hepatology | Compares HBV/HCV drug **pricing** across countries; not an efficacy study. |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Case report | BMJ Case Reports | G/P-associated liver injury in HCV patient explicitly **without** HBV co-infection. |
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case report (pending) | J Infect Chemother | Case of HCV exacerbation (not HBV) during chemotherapy for multiple myeloma. |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | Real-world (pending) | World J Gastroenterol | Real-world DAA effectiveness in HIV/HCV genotype 6 co-infection; no HBV endpoint. |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review (pending) | Clin Pharmacokinet | PK/PD review of HCV DAA regimens including glecaprevir/pibrentasvir; HCV only. |

---

## EU Market Information

Pibrentasvir has **no independent EU marketing authorization** recorded in this evidence pack (0 licenses; market status: Not Marketed). As a single moiety it is only available as part of the fixed-dose combination glecaprevir/pibrentasvir (Maviret/Mavyret), which is not captured under this drug-level regulatory record.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and DDI data are all recorded as data gaps in this evidence pack; DG001 flags TFDA/EMA label warnings as a **blocking** gap for any safety pre-screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score is very high (99.84%), the underlying "evidence" for HBV is a data-matching artifact — the cited trials and literature are HCV efficacy studies in which HBV was only a co-infection screening/exclusion variable, not a treatment endpoint. There is no established mechanistic link between the HCV-specific NS5A target and HBV replication, and this pattern of mismatched evidence recurs across **all ten** of this candidate's top predicted indications (HIV, HAV, HEV, Omsk hemorrhagic fever, Kyasanur forest disease, SIV, feline AIDS, and an unrelated rare neurodevelopmental disorder), consistent with a broad disease-embedding clustering artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Confirmed DrugBank/SmPC mechanism-of-action data (DG002) to formally assess target biology
- TFDA/EMA label warnings and contraindications (DG001) — currently blocking any S1 safety pre-screening
- Independent virology screening data showing direct antiviral activity of Pibrentasvir against HBV in vitro, since no such data currently exists in the trial or literature record
- Given the systemic evidence-mismatch pattern across this candidate's entire prediction list, recommend deprioritizing further manual review unless new primary HBV-specific data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

