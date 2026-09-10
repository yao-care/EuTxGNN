---
layout: default
title: Ozanimod
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
---

# Ozanimod
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

# Ozanimod: From Relapsing Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

Ozanimod is a selective sphingosine-1-phosphate receptor (S1P1/S1P5) modulator originally developed and approved for relapsing forms of multiple sclerosis. The TxGNN model predicts it may also be effective for **Progressive Relapsing Multiple Sclerosis (PRMS)**, with **8 clinical trials** and **18 publications** currently associated with this signal — though none of them enroll PRMS patients specifically, and the evidence is largely extrapolated from broader relapsing-MS trial populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing forms of multiple sclerosis (established indication per literature, e.g. PMID 32385738; not extracted from a structured `original_indications` field — data gap) |
| Predicted New Indication | Progressive Relapsing Multiple Sclerosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L3 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data from DrugBank is not available for this record (data gap, DG002). However, based on the literature collected in this evidence pack, ozanimod is well characterized as a selective S1P1/S1P5 receptor modulator. It binds these receptors on lymphocytes, driving receptor internalization and sequestration of autoreactive T and B cells within secondary lymphoid organs, thereby limiting their trafficking into the central nervous system (PMID 32385738, 33287177). This mechanism underlies its established efficacy in relapsing multiple sclerosis.

Progressive Relapsing Multiple Sclerosis (PRMS) shares the "relapsing" inflammatory component with standard relapsing-remitting MS, but is additionally defined by steady disability accumulation from onset — a neurodegenerative process driven more by compartmentalized CNS inflammation (microglial activation, chronic axonal loss) than by peripheral lymphocyte trafficking. Because ozanimod's proven mechanism acts primarily on peripheral lymphocyte egress, its ability to control the progressive/neurodegenerative component of PRMS is mechanistically far less certain than its effect on acute relapses.

It is also important to note that **PRMS is a largely obsolete diagnostic category**: current MS phenotype classifications (post-2013 revisions) have folded this subtype into "active secondary progressive MS" or "primary progressive MS with activity." This substantially limits the practical, real-world applicability of this prediction, even though the TxGNN similarity score is high — the score likely reflects embedding proximity to relapsing-MS concepts rather than a clinically actionable, distinct indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: early intensive vs. escalation DMT strategy in relapsing MS; not PRMS-specific |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | Recruiting | 60 | Predicts disease activity/rebound risk in MS patients on S1P receptor modulators, including ozanimod |
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | Completed | 2494 | Pivotal RCT of ozanimod (RPC1063) vs. active comparator in relapsing MS (efficacy/safety) |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by invitation | 323 | STATURE: treatment burden and adherence across 6 oral DMTs including ozanimod |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | Active, not recruiting | 9000 | ORION: real-world post-authorization safety study of ozanimod in RRMS |
| [NCT05688436](https://clinicaltrials.gov/study/NCT05688436) | N/A | Recruiting | 1178 | Pregnancy outcomes registry for diroximel fumarate in MS (comparator DMT, not ozanimod-specific) |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, not recruiting | 900 | Pragmatic trial comparing early aggressive vs. escalation therapy in MS |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | Active, not recruiting | 84 | Effectiveness and safety of oral ozanimod in Chinese adults with relapsing MS |

**Note:** None of the above trials specifically enroll or analyze a PRMS subgroup; all evidence is indirect extrapolation from relapsing-MS populations.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network meta-analysis (progressive MS) | Cochrane Database Syst Rev | Compares immunomodulator/immunosuppressant efficacy and safety across progressive MS forms; relative benefit remains unclear |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Comprehensive drug review | Neurology International | Reviews ozanimod's efficacy/safety profile as an S1P modulator for relapsing MS |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | Discusses therapeutic developments and mechanistic targets for progressive MS |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Drug review ("First Approval") | Drugs | Confirms 2020 US FDA approval and EU CHMP positive opinion for relapsing forms of MS |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis (RRMS) | Cochrane Database Syst Rev | Compares immunomodulators/immunosuppressants in RRMS |
| [35805142](https://pubmed.ncbi.nlm.nih.gov/35805142/) | 2022 | Review | Cells | Overview of S1P/S1PR signaling and modulator development history |
| [30410033](https://pubmed.ncbi.nlm.nih.gov/30410033/) | 2018 | General review | Nat Rev Dis Primers | Comprehensive MS disease primer covering pathophysiology and phenotypes |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | Reviews S1P receptor modulator class for MS treatment |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opin Pharmacother | Update on S1PR modulators (fingolimod, siponimod, ozanimod, ponesimod) in relapsing MS |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | Review | Front Immunol | Discusses CNS-bioavailable DMTs and their limited efficacy in progressive MS forms |

---

## EU Market Information

Ozanimod is not currently marketed in this jurisdiction — the regulatory record shows **0 authorizations** and no license entries are available.

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug interactions) for this record are not available. This is flagged as a **Blocking** data gap (DG001): without the product label/SmPC, no preliminary safety (S1) assessment can be completed.

> Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for ozanimod in PRMS is entirely indirect — extrapolated from relapsing-MS trials with no PRMS-specific enrollment or subgroup data, and the mechanistic case for the neurodegenerative component of PRMS is weak. Additionally, PRMS is a largely obsolete diagnostic classification in current MS phenotyping, which limits the clinical actionability of this prediction. A blocking safety data gap (missing product label) also prevents any preliminary safety assessment (S1).

**To proceed, the following is needed:**
- Product label / SmPC with warnings and contraindications (DG001, Blocking)
- Structured DrugBank mechanism-of-action data (DG002, High)
- Clarification on how PRMS maps to current MS phenotype classifications in the target regulatory framework, or reformulation of the hypothesis toward "active SPMS"
- Dedicated trial or registry data stratified by progressive-relapsing phenotype, if such patients still exist within contemporary MS cohorts

**Analyst note:** This evidence pack also contains rank 6, "relapsing-remitting multiple sclerosis" (L1 evidence, decision stage S3, Proceed with Guardrails). That entry is **not a novel repurposing signal** — RRMS is ozanimod's already-approved, on-label indication (Zeposia). It is included here only because it surfaced in the same prediction batch; it should not be evaluated as a new indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

