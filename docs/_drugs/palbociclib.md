---
layout: default
title: Palbociclib
parent: AI Predictions (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Palbociclib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Palbociclib: From HR+/HER2- Breast Cancer to Hyperthyroidism

## One-Sentence Summary

Palbociclib is a CDK4/6 inhibitor originally used for hormone receptor-positive, HER2-negative locally advanced or metastatic breast cancer.
The TxGNN model's top-ranked prediction is **hyperthyroidism**, but there are **0 clinical trials** and **0 publications** supporting it, so the prediction rests on the graph model alone.
Other predictions have more support, notably **myeloid leukemia** (4 registered trials, 19 publications) and **rheumatoid arthritis** (4 publications, no trials). They are discussed below as better-supported alternatives.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR-positive, HER2-negative locally advanced or metastatic breast cancer (with an aromatase inhibitor, or with fulvestrant after prior endocrine therapy) |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization in the data compiled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, palbociclib belongs to the CDK4/6 inhibitor class. Its efficacy in HR+/HER2- breast cancer is established, and it works by controlling cell-cycle progression.

For hyperthyroidism, the data compiled for this report identified no plausible CDK4/6-dependent mechanism. The high score (0.994) is a graph-based prediction only, with no supporting trials or literature. The same is true of the other thyroid-related predictions (thyroid hormone resistance, hyperthyroxinemia), which are likely driven by shared neighbors in the knowledge graph.

Among the ten predictions, three are worth noting:
- **Myeloid leukemia (Level L3, rank 6):** CDK6 is a dependency in AML, especially MLL- and NUP98-rearranged forms. Preclinical studies show synergy with venetoclax/azacitidine, menin inhibitors and LSD1 inhibitors. Four early-phase trials are registered, with no randomized data.
- **Rheumatoid arthritis (Level L4, rank 2):** CDK4/6 drives synovial fibroblast proliferation. Evidence consists of animal and in vitro studies plus one case report. It is hypothesis-generating only.
- **Thrombotic disease (rank 3):** The literature shows CDK4/6 inhibitors are associated with an *increased* thromboembolism risk. The prediction conflicts with the safety evidence and should not be pursued.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperthyroidism.

For reference, the best-supported alternative prediction (myeloid leukemia) has these registered trials:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02310243](https://clinicaltrials.gov/study/NCT02310243) | Phase 1/2 | Unknown | 50 | Palbociclib in MLL-rearranged acute leukemias; no results provided |
| [NCT03132454](https://clinicaltrials.gov/study/NCT03132454) | Phase 1 | Active, not recruiting | 32 | Palbociclib alone and with sorafenib, decitabine or dexamethasone in relapsed/refractory leukemia |
| [NCT05627232](https://clinicaltrials.gov/study/NCT05627232) | Phase 1 | Recruiting | 24 | Tazemetostat + CPX-351 (Part 1); palbociclib pre-treatment then CPX-351 (Part 2) in relapsed/refractory AML |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | Precision-oncology platform trial; not informative for myeloid leukemia |

---

## Literature Evidence

Currently no related literature available for hyperthyroidism.

For reference, selected publications for the alternative predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case report | Mod Rheumatol Case Rep | Rheumatoid arthritis improved in a breast cancer patient treated with palbociclib |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical | Int J Mol Sci | CDK6-dependent, CDK4-independent synovial hyperplasia in arthritic mice |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical | Ann Rheum Dis | CDK inhibition plus cytokine blockade improved arthritis in animal models without added immune suppression |
| [41468895](https://pubmed.ncbi.nlm.nih.gov/41468895/) | 2026 | Preclinical | Cell Rep Med | Palbociclib plus venetoclax effective in AML samples and xenograft models |
| [36076608](https://pubmed.ncbi.nlm.nih.gov/36076608/) | 2022 | Preclinical | Biomed Pharmacother | Palbociclib enhanced venetoclax plus azacitidine activity in AML |
| [38430306](https://pubmed.ncbi.nlm.nih.gov/38430306/) | 2024 | Case report | Cancer Chemother Pharmacol | Palbociclib with venetoclax and azacitidine used in refractory/relapsed therapy-related AML |
| [36794339](https://pubmed.ncbi.nlm.nih.gov/36794339/) | 2023 | Pharmacovigilance / systematic review | Expert Opin Drug Saf | Thromboembolism signal associated with CDK4/6 inhibitors |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003853 | Ibrance | Not specified | Ibrance is indicated for the treatment of hormone receptor (HR) positive, human epidermal growth factor receptor 2 (HER2) negative locally advanced or metastatic breast cancer:  in comb... |

The authorization is recorded as cancelled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) |
| Myelosuppression Risk | Neutropenia and bone marrow suppression are recognized effects of this class; please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count; please refer to the SmPC for the full schedule |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were found in total. Major-level interactions in the data include **clarithromycin**, **cobicistat**, **deferiprone** and **samarium (153Sm) lexidronam**. Moderate-level interactions include aprepitant, dexamethasone, cimetidine, saxagliptin, simvastatin, miconazole and cilostazol.
- **Class safety signals from the literature:** Pharmacovigilance analyses report thromboembolic events and interstitial lung disease or pulmonary toxicity with CDK4/6 inhibitors. This is relevant to any cardiovascular or thrombotic indication (including Prinzmetal angina and thrombotic disease).

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hyperthyroidism prediction has no clinical, literature or mechanistic support. Its score is a computational artifact only (Level L5). The EU authorization is also recorded as cancelled, which limits near-term regulatory pathways.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic rationale linking CDK4/6 inhibition to thyroid hormone excess
- EU label warnings and contraindications (SmPC), currently missing
- Consider redirecting evaluation to better-supported candidates: **myeloid leukemia** (early-phase trial results, myelosuppression risk assessment) and **rheumatoid arthritis** (a proper clinical study beyond one case report and animal data)
- Deprioritize **thrombotic disease** and **Prinzmetal angina** because of the thromboembolic safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

