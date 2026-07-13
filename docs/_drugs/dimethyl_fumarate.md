---
layout: default
title: Dimethyl Fumarate
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Dimethyl Fumarate
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

# Dimethyl Fumarate: From Relapsing-Remitting Multiple Sclerosis to Progressive Multiple Sclerosis

## One-Sentence Summary

Dimethyl fumarate (DMF, brand name Tecfidera) is an oral immunomodulator with established approval in the EU and US for relapsing-remitting multiple sclerosis (RRMS), acting through antioxidant and anti-inflammatory pathways. The TxGNN model predicts it may be effective for **Progressive Multiple Sclerosis**, with **2 directly relevant clinical trials** (including a completed Phase 2 RCT specifically in primary progressive MS) and **19 publications** currently supporting this direction. While the key RCT did not meet its primary endpoint, the mechanistic rationale and accumulating real-world data make this a worthwhile candidate for further evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsing-Remitting Multiple Sclerosis (RRMS) |
| Predicted New Indication | Progressive Multiple Sclerosis |
| TxGNN Prediction Score | 90.67% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note**: DMF (Tecfidera) holds EU approval (EMA, January 2014) and US FDA approval (2013) for RRMS. It is not currently registered in Taiwan.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on published literature and the repurposing rationale, DMF activates the Nrf2 (Nuclear factor erythroid 2–related factor 2) transcription pathway, enhancing cellular antioxidant defenses, while simultaneously downregulating Th1/Th17 pro-inflammatory cytokine production and upregulating the anti-inflammatory Th2 response. This dual immunomodulatory and neuroprotective profile is what drives its established efficacy in RRMS.

Progressive MS — both primary progressive (PPMS) and secondary progressive (SPMS) — differs fundamentally from RRMS in that neurodegeneration and oxidative stress, rather than acute demyelinating attacks, become the dominant drivers of disability accumulation. This pathological shift is precisely where DMF's Nrf2-mediated neuroprotection may offer unique value: by reducing reactive oxygen species burden and shielding oligodendrocytes from damage, DMF targets mechanisms that are largely untouched by conventional anti-inflammatory DMTs. Most existing immunotherapies have minimal impact once the progressive phase has begun, creating significant unmet need.

The TxGNN prediction is directly supported by a completed Phase 2 RCT (NCT02959658) that specifically enrolled PPMS patients, with results published in *Neurology: Neuroimmunology & Neuroinflammation* (PMID 34429340) and an open-label extension (PMID 36586351). Although the primary endpoint — reduction in CSF neurofilament light chain (NFL) concentration — was not met in the placebo-controlled phase, open-label extension data and a real-world cohort study in progressive MS (PMID 33996142) suggest residual signals worth pursuing. A terminated Phase 3 trial in SPMS (NCT02430532) further demonstrates that this hypothesis has previously attracted serious clinical investment from Biogen.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02959658](https://clinicaltrials.gov/study/NCT02959658) | Phase 2 | Completed | 54 | **Core RCT**: randomized, placebo-controlled trial of DMF in primary progressive MS (PPMS); 48-week treatment; primary endpoint (CSF NFL reduction) not met; open-label extension data published (PMID 36586351) |
| [NCT03092544](https://clinicaltrials.gov/study/NCT03092544) | Phase 4 | Unknown | 57 | Investigates indirect neuroprotective mechanism of DMF (Tecfidera) in both RRMS and progressive MS patients, including gut microbiome–immune axis analysis; directly evaluates DMF in progressive phenotype |
| [NCT02430532](https://clinicaltrials.gov/study/NCT02430532) | Phase 3 | Terminated | 58 | Randomized, double-blind, placebo-controlled study of DMF (BG00012) in secondary progressive MS (SPMS); primary objective was slowing disability accumulation independent of relapses; terminated early after limited enrollment |
| [NCT02683863](https://clinicaltrials.gov/study/NCT02683863) | Phase 4 | Completed | 20 | Open-label PK study exploring CNS penetration of DMF/MMF (its active metabolite) in SPMS via matched blood/CSF sampling; relevant to whether DMF reaches the progressive disease compartment |
| [NCT07138833](https://clinicaltrials.gov/study/NCT07138833) | Phase 4 | Not Yet Recruiting | 50 | Multicenter open-label trial of DMF enteric-coated capsules in relapsing MS including active SPMS; expected start 2025, completion 2028 |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, Not Recruiting | 800 | DELIVER-MS: pragmatic RCT comparing early intensive vs escalation DMT strategies in RRMS; DMF is one of available agents; informs long-term disability prevention strategy |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, Not Recruiting | 900 | TREAT-MS: early aggressive vs escalation therapy in MS; DMF is an available comparator; addresses whether preventing progressive conversion can be achieved via early treatment |
| [NCT03193866](https://clinicaltrials.gov/study/NCT03193866) | N/A | Completed | 3,526 | COMBAT-MS: large prospective observational cohort comparing rituximab vs all approved DMTs including DMF in RRMS; n=3,526; real-world comparative effectiveness data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34429340](https://pubmed.ncbi.nlm.nih.gov/34429340/) | 2021 | RCT | Neurology: Neuroimmunology & Neuroinflammation | Phase 2 RCT of DMF vs placebo in PPMS (n=54, 48 weeks); primary endpoint (CSF neurofilament light chain reduction) not met; key direct evidence for DMF in progressive MS |
| [36586351](https://pubmed.ncbi.nlm.nih.gov/36586351/) | 2023 | Open-label Extension | Multiple Sclerosis and Related Disorders | Open-label extension of the PPMS RCT; reports longer-term outcomes of DMF in PPMS beyond the controlled phase |
| [33996142](https://pubmed.ncbi.nlm.nih.gov/33996142/) | 2021 | Real-world Cohort | MS Journal – Experimental, Translational and Clinical | Real-world safety and effectiveness analysis of DMF in progressive MS populations; limited prior published data in this group |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network Meta-analysis | Cochrane Database of Systematic Reviews | Updated Cochrane network meta-analysis of immunomodulators and immunosuppressants for RRMS; contextualizes DMF's comparative efficacy across the DMT landscape |
| [29686116](https://pubmed.ncbi.nlm.nih.gov/29686116/) | 2018 | Clinical Practice Guideline | Neurology | AAN guideline recommendations for DMTs in MS; provides authoritative positioning of DMF across MS phenotypes |
| [25900414](https://pubmed.ncbi.nlm.nih.gov/25900414/) | 2015 | Systematic Review | Cochrane Database of Systematic Reviews | Cochrane review of DMF for MS; synthesizes DEFINE and CONFIRM Phase 3 RCT data establishing DMF's RRMS evidence base |
| [27433310](https://pubmed.ncbi.nlm.nih.gov/27433310/) | 2016 | Narrative Review | Therapeutic Advances in Chronic Disease | Review of DMF after >190,000 patients treated globally; covers real-world experience, neuroprotective mechanisms, and biomarker data relevant to progressive disease |
| [34465252](https://pubmed.ncbi.nlm.nih.gov/34465252/) | 2022 | Long-term Extension | Multiple Sclerosis | ENDORSE study: up to 13 years of DMF follow-up in RRMS; confirms sustained favorable benefit–risk profile informing safety expectations in a new indication |
| [32808554](https://pubmed.ncbi.nlm.nih.gov/32808554/) | 2022 | Safety Cohort | Multiple Sclerosis | Nine PML cases in DMF-treated MS patients reported; estimated PML incidence 0.02 per 1,000 patients; risk concentrated in those with severe or prolonged lymphopenia |
| [33091427](https://pubmed.ncbi.nlm.nih.gov/33091427/) | 2021 | Systematic Review | Pharmacology & Therapeutics | Comprehensive review of DMF-induced lymphopenia mechanisms and PML risk; critical reference for monitoring protocol design in a progressive MS population |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Key safety signal from evidence review**: Multiple publications in the evidence set (PMIDs 32808554, 36387034, 38321317) document an association between DMF treatment and **Progressive Multifocal Leukoencephalopathy (PML)**, a rare but potentially fatal opportunistic brain infection caused by JC virus. The estimated incidence is approximately **0.02 per 1,000 patients**, with risk concentrated in those with **severe or prolonged lymphopenia** (grade 3, <0.5 × 10⁹/L). Any repurposing protocol for progressive MS must include regular lymphocyte monitoring and a defined threshold for treatment interruption.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (NCT02959658) directly tested DMF in primary progressive MS and real-world cohort data for progressive MS are available — establishing an L2 evidence level and justifying continued investigation. However, the primary endpoint was not met and a Phase 3 SPMS trial was terminated early, meaning the efficacy signal requires targeted characterization (particularly by disease subtype and inflammatory activity) before broad adoption.

**To proceed, the following is needed:**
- Retrieve full DMF SmPC (EU) to complete safety profile: warnings, contraindications, and special population guidance
- Obtain DMF mechanism of action data from DrugBank (Nrf2/NF-κB pathway specifics and oligodendrocyte protection evidence)
- Define the target progressive MS population precisely — active SPMS (with ongoing relapses, where anti-inflammatory effects remain relevant) is likely more tractable than inactive PPMS
- Design a lymphocyte monitoring protocol with clear discontinuation thresholds to manage PML risk
- Conduct subgroup analysis of published PPMS RCT data (NCT02959658) to identify potential responder characteristics (e.g., age, disability level, baseline NFL)
- Monitor outcome of NCT07138833 (active SPMS arm) as emerging prospective evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

