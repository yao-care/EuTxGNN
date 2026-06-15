---
layout: default
title: Apremilast
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Apremilast
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

# Apremilast: From Psoriatic Arthritis to Rheumatoid Arthritis

## One-Sentence Summary

Apremilast (Otezla) is an oral small-molecule PDE4 inhibitor approved in the US and EU for psoriatic arthritis and plaque psoriasis, but not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis (RA)**, with **6 clinical trials** and **19 publications** supporting this direction — though a key Phase 2 trial (n=237) was terminated early, indicating limited efficacy in the MTX-refractory population and no Phase 3 follow-up.

> **Note on prediction ranking:** The top TxGNN-scored prediction for Apremilast is migraine disorder (score 98.66%, L5 — no clinical evidence). This report focuses on **Rheumatoid Arthritis (TxGNN rank 3, score 98.09%, L2)**, which carries the strongest clinical evidence and the most actionable decision recommendation among all predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriatic arthritis, plaque psoriasis (globally approved; not marketed in Taiwan) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Apremilast selectively inhibits phosphodiesterase type 4 (PDE4), the enzyme responsible for degrading intracellular cyclic AMP (cAMP). By blocking PDE4, apremilast elevates cAMP, activates protein kinase A (PKA), and prevents NF-κB nuclear translocation — thereby suppressing downstream production of TNF-α, IL-17, IL-23, and IL-1β. In vitro data from human RA synovial cells directly confirmed that apremilast inhibits spontaneous TNF-α secretion (PMID 20525198), and a collagen-induced arthritis mouse model demonstrated suppression of Th1/Th17 cells alongside enhanced Treg differentiation (PMID 30072998).

Rheumatoid arthritis shares the same core inflammatory axis as psoriatic arthritis — the condition for which apremilast is approved. Both diseases involve Th1/Th17 skewing, synovial macrophage overactivation, and excess cytokine production. This mechanistic overlap has already been tested in humans: a completed Phase 2 RCT (NCT01250548; PMID 25779750) evaluated apremilast directly in active RA, providing controlled efficacy and safety data.

However, the development trajectory carries a significant warning signal. The largest Phase 2 RA trial (NCT01285310, n=237) was terminated early — most likely due to insufficient efficacy in the MTX-inadequate refractory population — and NCT01204138 was withdrawn with zero enrollment. Apremilast did not advance to Phase 3 for RA. This pattern suggests its utility may be limited to a specific subpopulation: patients with mild-to-moderate RA who are MTX-intolerant, biologic-naïve, or in whom biologics are contraindicated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | Completed | 34 | Controlled trial (apremilast vs placebo) directly in active RA; assessed safety, time to response, and durability of effect — the most directly relevant completed trial for this indication |
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | Terminated | 237 | Two apremilast doses vs placebo in RA patients with inadequate MTX response; terminated early — likely due to insufficient efficacy; no Phase 3 followed, a critical negative signal |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | Withdrawn | 0 | Crossover study of apremilast add-on to TNF inhibitor + MTX in active RA; withdrawn before any enrollment — further weakens the case for use in refractory RA |
| [NCT00521339](https://clinicaltrials.gov/study/NCT00521339) | Phase 2 | Completed | 31 | Safety, pharmacodynamics, and PK characterisation of apremilast in inflammatory disease; provides key dosing and tolerability data underpinning subsequent RA trials |
| [NCT01504113](https://clinicaltrials.gov/study/NCT01504113) | N/A | Unknown | 100 | Psoriasis targeted therapy and microorganism interactions; indirect background on apremilast's immunomodulatory breadth and infection-risk profile |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | Phase II RCT | Arthritis & Rheumatology | Apremilast vs placebo in active RA with inadequate MTX response; primary clinical efficacy and safety data — the pivotal published evidence for this repurposing direction |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | PK/PD Study | Clin Pharmacol Drug Dev | Co-administration PK of apremilast + methotrexate in RA and PsA patients; no clinically significant pharmacokinetic interaction identified, supporting safe co-use |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | Animal Model | Front Immunol | Apremilast suppressed Th1/Th17 cells and enhanced Treg differentiation in collagen-induced arthritis mouse model; direct mechanistic evidence for RA-relevant anti-inflammatory effect |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | In Vitro / Mechanism | Arthritis Res Ther | Apremilast inhibited spontaneous TNF-α production from human RA synovial cells and ameliorated two murine arthritis models; foundational mechanism study |
| [40283434](https://pubmed.ncbi.nlm.nih.gov/40283434/) | 2025 | Review | J Clin Med | Comparative review of rituximab, apremilast, and upadacitinib in inflammatory arthritis; most current overview of apremilast's therapeutic context in the RA landscape |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Drug Approval Review | Drugs | First global approval review of apremilast; confirms RA was an active development target alongside PsA and psoriasis, and summarises the regulatory history |
| [33403021](https://pubmed.ncbi.nlm.nih.gov/33403021/) | 2020 | Systematic Review | Ther Adv Musculoskelet Dis | Shared development of targeted therapies across autoimmune inflammatory diseases; supports the mechanistic plausibility and precedent for cross-indication repurposing |
| [32453211](https://pubmed.ncbi.nlm.nih.gov/32453211/) | 2021 | Case Report | J Clin Rheumatol | Successful use of apremilast for rituximab-associated palmoplantar pustulosis in a seropositive RA patient; documents real-world safety and utility in an RA context |
| [30917076](https://pubmed.ncbi.nlm.nih.gov/30917076/) | 2019 | Real-World Cohort | J Manag Care Spec Pharm | Adherence, persistence, and costs of high-cost anti-inflammatory drugs in RA; contextualises real-world patient behaviour with novel agents including apremilast |
| [38499181](https://pubmed.ncbi.nlm.nih.gov/38499181/) | 2024 | Clinical Guideline | J Am Acad Dermatol | Perioperative management of systemic immunomodulatory agents (including apremilast) in psoriasis and PsA; safety guidance with direct applicability to any RA development programme |

---

## Taiwan Market Information

Apremilast is **not currently marketed in Taiwan** (0 TFDA authorizations on record). Globally, it is approved by the US FDA (2014) and EMA under the brand name Otezla for psoriatic arthritis in adults and moderate-to-severe plaque psoriasis. Any repurposing development targeting the Taiwan market for RA would require a de novo TFDA regulatory submission. The Taiwan SmPC and formal warning/contraindication data are not yet available for this evaluation.

---

## Safety Considerations

- **MOA Data Gap:** Detailed mechanism of action data is listed as unavailable in this evidence pack. From the included literature, apremilast is consistently characterised as a PDE4 inhibitor (PMID 20525198, 30072998, 24797159), with class-associated risks including nausea, diarrhoea, headache, and — importantly — neuropsychiatric effects (depression, suicidal ideation) known from the PDE4 inhibitor class.
- **Pregnancy Considerations:** A 2025 scoping review (PMID 39895048) highlights incomplete data on tsDMARD pregnancy outcomes; apremilast's reproductive safety in RA has not been separately characterised.
- **No Drug-Drug Interaction Data Found:** The DDI query returned no results. CYP3A4 inducers (e.g. rifampicin) are known to reduce apremilast exposure based on global SmPC data; this should be confirmed before clinical use.

Please refer to the global Otezla SmPC for complete warnings, contraindications, and drug interaction information pending TFDA SmPC availability.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Apremilast has direct Phase 2 RCT evidence in RA (PMID 25779750; NCT01250548) with compelling mechanistic support from human synovial cell studies and animal models. However, development stalled after the larger NCT01285310 (n=237) was terminated — the drug did not reach Phase 3 for RA. The opportunity lies in a narrower, better-defined patient subgroup (MTX-intolerant, biologic-naïve, or mild-to-moderate RA) rather than in the refractory population where it has already shown insufficient effect.

**To proceed, the following is needed:**

- Obtain and review the full published or unpublished results from NCT01250548 and NCT01285310, including the specific reason for termination and subgroup efficacy data
- Define the target RA subpopulation where the benefit-risk profile is favourable (e.g. MTX-intolerant, early RA, or those with contraindications to biologics)
- Obtain the Taiwan TFDA SmPC or global Otezla SmPC to complete warning, contraindication, and DDI assessment (currently listed as data gaps)
- Confirm MOA data via DrugBank API (DB05676) to complete the mechanistic profile
- Conduct a focused systematic review on apremilast in early or mild RA before designing any new clinical study
- Review the 2025 pregnancy outcomes scoping review (PMID 39895048) to assess reproductive safety if the target population includes women of childbearing potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

