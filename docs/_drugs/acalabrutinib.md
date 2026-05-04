---
layout: default
title: Acalabrutinib
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Acalabrutinib
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

# Acalabrutinib: From Mantle Cell Lymphoma/CLL to Non-Hodgkin Lymphoma (Familial)

## One-Sentence Summary

Acalabrutinib (Calquence®) is a second-generation, highly selective Bruton's tyrosine kinase (BTK) inhibitor approved by the US FDA for mantle cell lymphoma (MCL) and chronic lymphocytic leukemia (CLL), but currently not marketed in Taiwan.
The TxGNN model predicts it may be effective for **lymphoma, non-Hodgkin, familial** — a category encompassing B-cell NHL subtypes such as DLBCL, follicular lymphoma, and marginal zone lymphoma —
with **20 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mantle cell lymphoma (MCL) and chronic lymphocytic leukemia (CLL) — US FDA approved; not registered in Taiwan |
| Predicted New Indication | Lymphoma, Non-Hodgkin, Familial |
| TxGNN Prediction Score | 97.64% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acalabrutinib is a second-generation, covalent BTK inhibitor that irreversibly binds to the Cys481 residue of Bruton's tyrosine kinase, blocking downstream B-cell receptor (BCR) signaling through the NF-κB and MAPK pathways. This mechanism selectively eliminates the survival and proliferation signals that malignant B cells depend upon. Compared to first-generation ibrutinib, acalabrutinib demonstrates substantially improved kinase selectivity, reducing off-target inhibition of TEC-family and EGFR kinases — a property that translates to a more favorable cardiovascular and bleeding safety profile.

B-cell non-Hodgkin lymphomas (NHL) — including MCL, diffuse large B-cell lymphoma (DLBCL), follicular lymphoma (FL), and marginal zone lymphoma (MZL) — share constitutive activation of the BCR/BTK signaling axis as a common molecular vulnerability. The step from acalabrutinib's established indications (MCL, CLL) to the predicted indication of familial NHL is therefore one of scope rather than mechanism: all mature B-cell malignancies listed under the NHL umbrella express BTK and depend on the same BCR-driven survival pathways that acalabrutinib targets.

Clinical translation of this mechanistic rationale is already well underway. Randomized Phase 2 trials in DLBCL (STELLAR trial, NCT03899337; HARMONIA-UK, NCT04546620) and Phase 2 studies in follicular lymphoma (NCT04883437) directly evaluate acalabrutinib in NHL subtypes beyond its approved indications. The landmark ACE-LY-004 trial (Lancet, 2018) demonstrated an 81% overall response rate in R/R MCL — a disease that is itself classified within NHL — providing the foundation for the FDA's 2017 accelerated approval and validating the strong mechanistic case for the broader NHL prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03899337](https://clinicaltrials.gov/study/NCT03899337) | Phase 2 | Recruiting | 105 | STELLAR trial: Randomized comparison of acalabrutinib + CHOP-R vs CHOP-R alone in newly diagnosed Richter's Syndrome (CLL-transformed DLBCL); highest-relevance direct acalabrutinib RCT in NHL |
| [NCT04546620](https://clinicaltrials.gov/study/NCT04546620) | Phase 2 | Active, not recruiting | 453 | Molecularly guided randomized Phase 2: acalabrutinib added to R-CHOP in untreated CD20+ DLBCL; large-scale 453-patient trial, completion expected May 2028 |
| [NCT04094142](https://clinicaltrials.gov/study/NCT04094142) | Phase 2 | Completed | 66 | R²A (acalabrutinib + rituximab + lenalidomide) in R/R B-cell NHL; 66-patient completed trial with published efficacy results (Park et al., Nature Commun 2024) |
| [NCT04002947](https://clinicaltrials.gov/study/NCT04002947) | Phase 2 | Recruiting | 132 | NCI-sponsored study of acalabrutinib + DA-EPOCH-R or R-CHOP in untreated aggressive B-cell lymphoma (primarily DLBCL); ongoing, completion expected March 2030 |
| [NCT04883437](https://clinicaltrials.gov/study/NCT04883437) | Phase 2 | Recruiting | 49 | Acalabrutinib + obinutuzumab in previously untreated low-tumor-burden follicular lymphoma and other indolent NHL; chemotherapy-free frontline approach |
| [NCT04257578](https://clinicaltrials.gov/study/NCT04257578) | Phase 1/2 | Active, not recruiting | 23 | Acalabrutinib + anti-CD19 CAR-T (axicabtagene ciloleucel) in B-cell lymphoma; exploring BTK inhibition as a strategy to enhance CAR-T cell efficacy |
| [NCT03623373](https://clinicaltrials.gov/study/NCT03623373) | Phase 2 | Completed | 13 | Pilot study of acalabrutinib + bendamustine-rituximab → cytarabine-rituximab in treatment-naïve MCL; completed April 2025, informs cooperative group design |
| [NCT02362035](https://clinicaltrials.gov/study/NCT02362035) | Phase 1/2 | Completed | 161 | Acalabrutinib + pembrolizumab across hematologic malignancies; 161-patient PK/PD/safety study across multiple NHL subtypes, completed October 2025 |
| [NCT02180711](https://clinicaltrials.gov/study/NCT02180711) | Phase 1/2 | Active, not recruiting | 113 | Acalabrutinib alone or with rituximab in R/R follicular lymphoma and marginal zone lymphoma; long-term follow-up ongoing through December 2028 |
| [NCT04502394](https://clinicaltrials.gov/study/NCT04502394) | Phase 1/2 | Unknown | 84 | KRT-232 (MDM2 inhibitor) + acalabrutinib in R/R DLBCL and CLL; 84-patient combination study evaluating dual apoptotic pathway blockade |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | Phase 1b/2 Trial | J Clin Oncol | Acalabrutinib + bendamustine-rituximab (ABR) in untreated MCL: demonstrated superior PFS over historical BR with a more favorable toxicity profile than ibrutinib-BR |
| [38555311](https://pubmed.ncbi.nlm.nih.gov/38555311/) | 2024 | Phase 2 Trial | Nature Commun | R²A regimen (acalabrutinib + lenalidomide + rituximab) in R/R aggressive B-cell NHL: single-arm Phase 2 reporting ORR and CR endpoints; supports triplet efficacy |
| [38781315](https://pubmed.ncbi.nlm.nih.gov/38781315/) | 2024 | Phase 1b/2 Trial (2-year follow-up) | Blood Advances | AVR (acalabrutinib + venetoclax + rituximab) in treatment-naïve MCL: 95.2% induction completion rate, 2-year follow-up confirms durable responses |
| [37470152](https://pubmed.ncbi.nlm.nih.gov/37470152/) | 2024 | Phase 2 Trial (Final Report) | Haematologica | Final OS data from ACE-LY-004 Phase 2: acalabrutinib monotherapy in R/R MCL including poor-prognostic subgroups; long-term survival outcomes |
| [40775236](https://pubmed.ncbi.nlm.nih.gov/40775236/) | 2025 | Phase 2 Trial | Nature Commun | Frontline acalabrutinib + lenalidomide + rituximab for advanced-stage follicular lymphoma with high tumor burden; 24-patient trial reporting best CR rate as primary endpoint |
| [41289154](https://pubmed.ncbi.nlm.nih.gov/41289154/) | 2026 | Phase 2 Trial | Blood Advances | MRD-guided acalabrutinib + lenalidomide ± rituximab/obinutuzumab in frontline MCL: molecular CR (uMRD6 by clonoSEQ) as primary endpoint, novel MRD-adaptive strategy |
| [29241979](https://pubmed.ncbi.nlm.nih.gov/29241979/) | 2018 | Phase 2 Single-arm Trial | Lancet | ACE-LY-004 pivotal trial: acalabrutinib monotherapy in R/R MCL; 81% ORR, 40% CR — the basis for FDA accelerated approval in MCL |
| [29209955](https://pubmed.ncbi.nlm.nih.gov/29209955/) | 2018 | Regulatory Review | Drugs | First global approval summary for acalabrutinib (Calquence®): clinical development milestones, Phase 1/2 dose-finding, and regulatory pathway for MCL |
| [36029036](https://pubmed.ncbi.nlm.nih.gov/36029036/) | 2023 | Review | Br J Haematol | Updated review of primary and acquired resistance to BTK inhibitors in CLL and NHL: covers C481S mutation, bypass signaling via PLCG2/RAS, and microenvironmental mechanisms |
| [38578606](https://pubmed.ncbi.nlm.nih.gov/38578606/) | 2024 | Review | Clin Cancer Res | New strategies for BTK targeting: next-generation covalent/non-covalent inhibitors and BTK degraders; addresses acquired resistance challenges across CLL and NHL |

---

## Taiwan Market Information

Acalabrutinib currently has **no marketing authorization in Taiwan** (total licenses: 0). No approved product records are available from TFDA. The drug is marketed as Calquence® in the United States (FDA-approved for R/R MCL since October 2017; first-line and R/R CLL since November 2019) and holds EMA approval in Europe. No Taiwan regulatory filing has been identified in the current dataset.

> **Note:** The absence of Taiwan TFDA package insert data is flagged as a **Blocking data gap** (DG001), meaning Taiwan-specific warnings, contraindications, and dosing guidance cannot be assessed from local sources. The US FDA label and EMA SmPC should be used as interim references.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation selective covalent BTK inhibitor; not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — Neutropenia and thrombocytopenia reported in clinical trials; significantly less myelosuppressive than chemotherapy, but haematological monitoring is required |
| Emetogenicity Classification | Low — Oral targeted agent; classified as minimal-to-low emetogenic risk per MASCC/ESMO guidelines |
| Monitoring Items | CBC with differential (at baseline and during treatment), liver function tests (ALT/AST), renal function, platelet function and bleeding assessment, cardiac monitoring (atrial fibrillation risk) |
| Handling Protection | Follow institutional hazardous drug handling protocols for oral targeted therapies; standard precautions for preparation and dispensing |

---

## Safety Considerations

Please refer to the SmPC (or US FDA prescribing information for Calquence®) for safety information, as Taiwan TFDA package insert data is not currently available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 clinical trials directly studying acalabrutinib in B-cell NHL subtypes (DLBCL, follicular lymphoma, MCL) demonstrate a clear translational pathway, and the shared BTK/BCR molecular dependency across all mature B-cell malignancies provides a mechanistically coherent basis for the TxGNN prediction of 97.64%. The existing FDA approval for MCL and CLL establishes a well-characterized safety and efficacy foundation that substantially de-risks further NHL investigation.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain Taiwan TFDA package insert for acalabrutinib via TFDA official website to assess Taiwan-specific warnings, contraindications, and black box warnings — this is required before any local safety evaluation
- **Resolve DG002 (High):** Retrieve complete MOA and drug interaction data from DrugBank (DB11703), specifically CYP3A4 substrate profile and interaction with strong CYP3A4 inhibitors/inducers
- **Subtype stratification:** Define the specific NHL subtype(s) of highest unmet need in Taiwan (DLBCL vs. follicular lymphoma vs. MZL) to prioritize the most actionable repurposing target
- **Monitor key trials:** Await primary results from NCT04546620 (HARMONIA-UK, n=453, DLBCL) and NCT03899337 (STELLAR, n=105, Richter's Syndrome/DLBCL) before any Phase 3 escalation decision
- **Taiwan regulatory pathway:** Assess feasibility of TFDA registration for an NHL indication, including data package requirements and local bridging study needs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

