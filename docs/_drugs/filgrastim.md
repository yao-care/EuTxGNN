---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim (recombinant human G-CSF) is originally used to treat neutropenia and to mobilize peripheral blood stem cells prior to transplantation. TxGNN predicts a possible effect on **Primary Release Disorder of Platelets** with a very high model score (99.998%), but the supporting evidence — **14 clinical trials** and **1 publication** — consists almost entirely of transplant-support studies in which filgrastim was used incidentally for stem cell mobilization, not as a treatment targeting platelet release function.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neutropenia / peripheral blood stem cell mobilization (drug's known pharmacological use; no formal TFDA label text is available in this evidence pack) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Market Status (Taiwan) | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, filgrastim is a recombinant G-CSF that stimulates proliferation and differentiation of granulocyte precursors and mobilizes hematopoietic stem cells — it is not known to act on platelet dense-granule or alpha-granule secretion pathways, which are the defective mechanisms in primary platelet release disorders.

The evidence pack's own mechanistic assessment is explicit on this point: there is no known direct pharmacological link between G-CSF signaling and platelet granule release. The reviewers hypothesize that TxGNN's very high score (rank 48 of all candidate diseases) likely reflects an indirect knowledge-graph connection through "stem cell transplantation" nodes rather than a genuine pharmacological relationship.

Consistent with this, none of the 14 retrieved clinical trials or the single retrieved publication studied filgrastim as a treatment for platelet release disorders — they are transplant, GVHD-prophylaxis, or unrelated-condition studies in which filgrastim appears only as a supportive stem-cell-mobilization agent. This pattern supports treating the prediction as model-driven rather than mechanism-driven.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for hematologic malignancies; filgrastim used for stem cell mobilization/support, not targeted at a platelet disorder (graded low relevance) |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | RCT of ganciclovir/valganciclovir for CMV reactivation prevention in respiratory failure; filgrastim not the study drug (graded low relevance) |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | AHSCT vs. best available therapy for treatment-resistant relapsing MS; general transplant context, no link to platelet release function (graded low relevance) |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic stem cell transplant for high-risk pediatric sarcomas; filgrastim as supportive care only |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Autologous HSCT for severe systemic lupus erythematosus; filgrastim used for stem cell mobilization |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT for patients with GATA2 mutations; filgrastim as supportive agent |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplant with NK cells for myeloid leukemia; filgrastim as supportive agent |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial of post-transplant cyclophosphamide-based GVHD prophylaxis after mismatched unrelated donor PBSCT; filgrastim as supportive agent |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose-finding for post-transplant cyclophosphamide GVHD prophylaxis after reduced-intensity PBSCT; filgrastim as supportive agent |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs. unselected autologous SCT in advanced mantle cell/DLBCL lymphoma; filgrastim as supportive agent |

*(4 additional lower-relevance trials in the evidence pack are omitted here; none directly studied platelet release function.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Review/Observational | Frontiers in Immunology | G-CSF mobilization in healthy donors preferentially mobilizes lymphocyte subsets during peripheral blood stem cell collection; describes G-CSF immunomodulatory effects in donors, not disease-specific evidence for a platelet release disorder |

## Safety Considerations

A Blocking-severity data gap exists: TFDA label warnings and contraindications for filgrastim have not been retrieved, which prevents this candidate from entering the S1 safety pre-assessment stage. No drug interaction data was found (query returned no results). Please refer to the SmPC/TFDA label for safety information once retrieved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (mechanism/preclinical-adjacent at best), no trial or publication directly studied filgrastim for this indication, and the evidence pack's own mechanistic review concludes there is no plausible pharmacological link — the high TxGNN score likely reflects an indirect knowledge-graph artifact. A Blocking safety data gap also prevents progression to the S1 safety stage.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications for filgrastim (Blocking gap, DG001)
- Confirmed mechanism of action via DrugBank API (High-severity gap, DG002)
- Direct pharmacological or preclinical evidence linking G-CSF signaling to platelet granule release
- Clinical studies specifically enrolling patients with primary platelet release disorders, rather than incidental filgrastim use in transplant-support settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

