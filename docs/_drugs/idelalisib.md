---
layout: default
title: Idelalisib
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

Using report drafting directly — this is a structured content-generation task from a well-specified template, not a coding/debugging/design task that maps to an available skill.

# Idelalisib: From B-Cell Malignancies (CLL/Follicular Lymphoma/SLL) to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib (Zydelig®) is a PI3Kδ inhibitor originally approved for chronic lymphocytic leukemia (CLL), follicular lymphoma, and small lymphocytic lymphoma (SLL), but voluntarily withdrawn from the EU market in 2022 after post-marketing safety signals.
The TxGNN model predicts it may also be effective for **Mantle Cell Lymphoma (MCL)**, with **9 clinical trials** and **20 publications** currently associated with this direction — though most trials are early-phase (Phase 1/2) and none were designed specifically to confirm MCL efficacy in a randomized setting.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic lymphocytic leukemia (CLL), relapsed follicular lymphoma, small lymphocytic lymphoma (SLL) — per cited literature (PMID 25187123, 26933132) |
| Predicted New Indication | Mantle Cell Lymphoma |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| EU Market Status | ✗ Not Marketed (withdrawn) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (MOA field marked as a data gap). Based on information embedded in the evidence pack itself, idelalisib is a selective PI3Kδ (phosphatidylinositol 3-kinase delta) inhibitor. PI3Kδ is a key kinase in the B-cell receptor (BCR) signaling pathway, and its inhibition blocks proliferation and survival signals in malignant B cells — the mechanism underlying idelalisib's approval in CLL, follicular lymphoma, and SLL.

Mantle cell lymphoma is also a BCR-signaling-dependent B-cell malignancy, which provides a plausible mechanistic rationale for extending PI3Kδ inhibition to this indication. Early-phase clinical data support measurable single-agent activity: a dedicated Phase 1 study (NCT01088048/related, PMID 24615778) and a case-report-level activity signal (PMID 24795031, *Cancer Discovery*, 2014) both describe clinical responses to idelalisib in heavily pretreated MCL patients.

However, the evidence pack's own rationale flags an important caveat: several idelalisib combination trials in MCL and related B-cell malignancies (e.g., NCT01796470, NCT02457598) were **terminated**, and idelalisib as a monotherapy has shown **intrinsic resistance** in MCL according to preclinical work (PMID 33850273), which is why researchers have explored combination strategies (p300/CBP inhibitors, CDK4/6 inhibitors) to overcome resistance. No randomized Phase 2/3 trial has confirmed efficacy specifically in MCL.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib + idelalisib in relapsed/refractory hematologic malignancies including MCL, CLL, DLBCL, iNHL |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | BCL201 + idelalisib dose-escalation in follicular lymphoma and MCL; safety/tolerability primary endpoint |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Oral pirtobrutinib (LOXO-305) in CLL/SLL/NHL failing standard care; idelalisib relevant as prior/comparator therapy context |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib combined with other targeted anti-cancer therapies in B-cell lymphoproliferative malignancies |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Unknown | 464 | Quality-of-life assessment of oral lymphoma therapies (ibrutinib, acalabrutinib, idelalisib, venetoclax, lenalidomide) including MCL patients |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Idelalisib + chemotherapy/immunomodulatory agents/anti-CD20 mAb in relapsed/refractory indolent B-NHL, MCL, or CLL |
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 | Completed | 106 | Idelalisib + lenalidomide vs. lenalidomide alone in relapsed/refractory MCL |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Completed | 121 | Real-world assessment of side effects vs. plasma concentrations of ibrutinib and idelalisib in hematologic malignancies |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as post-allogeneic HSCT maintenance in B-cell derived malignancies; double-blind randomized placebo toxicity trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 clinical study | Blood | 48-week Phase 1 study of idelalisib (50–350 mg) in 40 patients with relapsed/refractory MCL; assessed safety, DLT, ORR, PFS |
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Clinical activity report | Cancer Discovery | PI3Kδ inhibitor idelalisib effective in heavily pretreated MCL patients |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical (mechanism) | Acta Pharmacologica Sinica | p300/CBP inhibitor A-485 overcomes intrinsic idelalisib resistance in MCL cells in vitro and in vivo |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical mechanistic | Clinical Cancer Research | Idelalisib disrupts translation-regulatory mechanisms driving MCL cell growth |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ inhibitor resistance in MCL; propolis restores sensitivity via ferroptosis |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Letters | Idelalisib enhances anti-tumor effects of palbociclib (CDK4/6 inhibitor) via PLK1 in B-cell lymphoma including MCL |
| [28775119](https://pubmed.ncbi.nlm.nih.gov/28775119/) | 2017 | Review | Haematologica | Practical approach to incidence and management of toxicity associated with ibrutinib and idelalisib in indolent B-cell malignancies including MCL |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | British Journal of Haematology | Current regimens and novel agents (including PI3K-pathway inhibitors) for mantle cell lymphoma |
| [26841011](https://pubmed.ncbi.nlm.nih.gov/26841011/) | 2016 | Review | Cancer Journal | Idelalisib targeting the PI3K pathway in non-Hodgkin lymphoma, including MCL rationale |
| [23512567](https://pubmed.ncbi.nlm.nih.gov/23512567/) | 2013 | Review | Current Treatment Options in Oncology | Current and emerging therapies in mantle cell lymphoma |

---

## Cytotoxicity

Idelalisib is an antineoplastic agent (oral targeted therapy for hematologic malignancies).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Moderate — literature cites neutropenia alongside immune-mediated toxicities (colitis, pneumonitis, hepatotoxicity) as key concerns (PMID 28775119, NCT02928510 idelalisib-associated colitis study) |
| Emetogenicity Classification | Low (oral small-molecule targeted therapy; not directly characterized in the evidence pack) |
| Monitoring Items | Liver function tests (transaminitis), CBC with differential (cytopenias), pulmonary symptoms (pneumonitis risk), GI symptoms (colitis/diarrhea) |
| Handling Protection | Standard oral oncolytic handling precautions; not subject to IV cytotoxic drug handling regulations, but institutional oral chemotherapy protocols should apply |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack — DG001 in the data gap log flags this as a blocking item for formal safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for idelalisib in MCL is limited to early-phase (Phase 1) and terminated combination trials, with no confirmatory randomized Phase 2/3 study — consistent with the L3 evidence level assigned. Compounding this, idelalisib carries a documented safety history (multiple front-line/combination trials across its approved indications were halted due to increased deaths and serious adverse events, per trial summaries in this pack) and was voluntarily withdrawn from the EU market in 2022. Formal safety review (S1) cannot proceed until the blocking data gap (TFDA/EMA label warnings and contraindications) is resolved.

**To proceed, the following is needed:**
- TFDA/EMA product label (SmPC) warnings, contraindications, and DDI data (currently a Blocking data gap — DG001)
- Confirmed mechanism of action documentation from DrugBank (High-priority data gap — DG002)
- A dedicated, non-terminated MCL-focused efficacy trial (ideally combination strategy addressing known intrinsic resistance) before advancing beyond a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

