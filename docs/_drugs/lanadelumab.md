---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From Hereditary Angioedema to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab (Takhzyro®) is a fully human monoclonal antibody that inhibits plasma kallikrein, approved in the United States and Europe since 2018 for long-term prophylaxis of Hereditary Angioedema (HAE) with C1-inhibitor deficiency, but not yet marketed in Taiwan. The TxGNN model predicts it may be highly effective for **C1 Inhibitor Deficiency**, with **22 clinical trials** and **20 publications** currently supporting this direction. The near-perfect prediction score reflects a mechanistically direct drug-disease match — lanadelumab targets the causative enzyme of the disease — making this a strong candidate for Taiwan market entry.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan registration; globally approved for HAE prophylaxis (Type I/II, ≥12 years) in US and EU |
| Predicted New Indication | C1 Inhibitor Deficiency |
| TxGNN Prediction Score | 99.9955% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lanadelumab is a fully human IgG1/κ monoclonal antibody that selectively binds and inhibits plasma kallikrein, a serine protease at the core of the kallikrein-kinin system (KKS). In patients with HAE Types I and II, mutations in the *SERPING1* gene produce insufficient or dysfunctional C1-inhibitor (C1-INH) protein. Without adequate C1-INH, the contact activation pathway becomes dysregulated: plasma kallikrein escapes inhibition, continuously cleaves high-molecular-weight kininogen (HMWK), and generates excess bradykinin. Bradykinin acting on vascular B2 receptors dramatically increases vascular permeability, producing the recurrent, potentially life-threatening swelling attacks — in skin, gastrointestinal tract, and upper airway — that define C1-INH-HAE. Lanadelumab directly neutralizes this causative enzyme, establishing a first-order mechanistic connection between drug target and disease pathophysiology.

The TxGNN predicted indication of "C1 inhibitor deficiency" maps precisely onto the established clinical indication for which lanadelumab already holds global approvals. The FDA approved Takhzyro® in August 2018, followed by the EMA in November 2018, both for long-term prophylaxis of HAE with C1-INH deficiency in patients aged 12 years and older. Subsequent Phase 3 data from the SPRING study (NCT04070326) extended the evidence base to children aged 2–11 years. The TxGNN model's near-perfect score (99.9955%) reflects the deep knowledge graph integration of kallikrein pathway biology, serpin family protein topology, and contact system relationships — all strongly converging on this drug-disease pair.

Beyond the canonical HAE Type I/II indication, emerging case series (PMID 33556593, 36379410, 39357560) suggest that acquired angioedema with C1-INH deficiency (AAE-C1-INH) — a non-hereditary condition sharing the same downstream bradykinin excess mechanism — may also respond to lanadelumab. This broadens the potential clinical population and strengthens the biological rationale for comprehensive evaluation of this drug in the Taiwanese clinical context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | HELP Study — pivotal multicenter double-blind RCT; lanadelumab 150 mg Q4W, 300 mg Q4W, and 300 mg Q2W vs. placebo all significantly reduced HAE attack rates; primary regulatory approval basis for FDA and EMA |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP OLE — open-label long-term extension of HELP Study; confirmed sustained attack reduction over more than 2 years, supporting durable prophylactic efficacy |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term open-label extension for non-histaminergic angioedema with normal C1-INH; evaluated safety and efficacy over up to 2.5 years of continuous dosing |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING Study — pediatric PK/PD and safety study in children aged 2–<12 years; PK bridging data supported label expansion to younger age groups |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Japanese open-label Phase 3; evaluated safety and efficacy of lanadelumab in Japanese HAE Type I/II patients — directly relevant for Asia-Pacific regulatory submissions |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Chinese open-label Phase 3; evaluated safety, PK, and efficacy over 26 weeks in Chinese HAE patients — supports ethnic bridging data for Taiwan |
| [NCT04955964](https://clinicaltrials.gov/study/NCT04955964) | N/A (PAS) | Completed | 48 | Argentina post-authorization surveillance study; real-world safety and effectiveness of lanadelumab in routine clinical practice in teenagers and adults |
| [NCT06346899](https://clinicaltrials.gov/study/NCT06346899) | N/A | Completed | 115 | Chinese real-world observational study comparing lanadelumab (prophylaxis) vs. icatibant (on-demand); provides relative effectiveness benchmarking in the Chinese population |
| [NCT04861090](https://clinicaltrials.gov/study/NCT04861090) | N/A | Completed | 207 | Largest real-world retrospective chart review; quantified attack-free rates and treatment patterns with lanadelumab dosed Q2W and Q4W across multiple centers |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completed | 140 | ENABLE — 3-year prospective non-interventional multicenter study; longitudinal real-world effectiveness assessment and disease burden quantification through patient-reported smartphone diaries |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | HELP pivotal trial publication: all three lanadelumab dosing regimens statistically significantly reduced HAE attack rates vs. placebo; 300 mg Q2W achieved the greatest reduction |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | RCT (Open-Label Extension) | Allergy | HELP OLE: long-term effectiveness and safety in patients ≥12 years with HAE Type I/II; durable attack reduction maintained with low adverse event burden |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clin Rev Allergy Immunol | Systematic review of breakthrough HAE attack characteristics during long-term prophylaxis across multiple agents; benchmarks lanadelumab's real-world performance |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network Meta-Analysis | Drugs in R&D | NMA comparing garadacimab, lanadelumab, subcutaneous C1INH, and berotralstat for HAE long-term prophylaxis; provides indirect comparative efficacy and safety estimates in the absence of head-to-head trials |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirect Treatment Comparison | J Comp Effectiveness Res | ITC comparing lanadelumab vs. C1-esterase inhibitor in pediatric HAE patients aged <12 years; supports dosing and positioning decisions for younger patients |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | N Engl J Med | Comprehensive NEJM review of hereditary angioedema: pathophysiology, diagnosis, and management landscape including the role of plasma kallikrein inhibitors |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Pharmacological Review | BioDrugs | Detailed review of lanadelumab preclinical and Phase 1 data; characterizes the mechanism of plasma kallikrein inhibition, PK/PD modeling, and dose selection rationale |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Drug Approval Review | Drugs | First global approval summary for lanadelumab; covers pharmacology, Phase 1–3 clinical efficacy, safety profile, and regulatory history in HAE |
| [37328263](https://pubmed.ncbi.nlm.nih.gov/37328263/) | 2023 | Real-World Database Study | Allergy Asthma Proc | US real-world healthcare utilization comparing new users of lanadelumab vs. subcutaneous C1-INH; describes resource use, costs, and treatment patterns |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case Series | JACI Pract | Three cases of acquired angioedema with C1-INH deficiency (AAE-C1-INH) treated with lanadelumab; demonstrates potential off-label benefit beyond HAE Type I/II through shared bradykinin pathomechanism |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lanadelumab holds Level 1 evidence from multiple completed Phase 3 RCTs — including the pivotal HELP Study published in JAMA — and has received regulatory approvals in the US, EU, Japan, China, South Korea, and Argentina. The TxGNN prediction is fully consistent with the established pharmacological mechanism: direct plasma kallikrein inhibition addresses the molecular root cause of C1-INH deficiency, not merely its symptoms. Taiwan currently has no approved long-term prophylactic option for HAE with C1-INH deficiency, representing a clear unmet need for this rare but potentially life-threatening disease. The availability of Asian-population Phase 3 data (Japanese and Chinese cohorts) substantially lowers the bridging data burden for TFDA submission.

**To proceed, the following is needed:**

- **TFDA regulatory submission**: prepare a Taiwan-specific dossier leveraging existing FDA/EMA approvals; the Japanese (NCT04180163) and Chinese (NCT05460325, NCT06346899) datasets provide ethnic bridging evidence relevant to the Taiwanese population
- **TFDA SmPC / package insert**: download and parse the Taiwan-specific prescribing information for complete warnings, contraindications, and special population guidance (currently a blocking data gap)
- **Rare disease designation assessment**: evaluate eligibility for Taiwan's orphan drug designation pathway, which may expedite review timelines and reduce regulatory burden
- **DrugBank API query**: formally document the mechanism of action and complete drug classification in the evidence pack (current data gap; mechanism is well-characterized in published literature but needs structured data entry)
- **Safety monitoring plan**: develop protocols for pediatric patients, renally or hepatically impaired populations, and pregnant/nursing women in the context of routine Taiwan clinical practice
- **Health technology assessment (HTA)**: conduct pharmacoeconomic analysis to support National Health Insurance reimbursement consideration, including budget impact modelling for the HAE patient population in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

