---
layout: default
title: Duvelisib
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Duvelisib
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

# Duvelisib: From Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma to Hodgkin's Lymphoma

## One-Sentence Summary

Duvelisib (DrugBank DB11952) is a dual PI3Kδ/γ inhibitor whose original approved indication (per published FDA approval literature) was relapsed/refractory chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) and follicular lymphoma; it is currently **not marketed in the EU** (0 authorizations on file). The TxGNN model's top-ranked new indication is **Hodgkin's Lymphoma**, with a **99.94% prediction score**, supported by **11 clinical trials** and **15 publications** — however, essentially all of this evidence actually enrolls non-Hodgkin lymphoma (NHL), CLL, or T-cell lymphoma patients, not classical Hodgkin lymphoma, suggesting a possible knowledge-graph disease-label mismatch that must be resolved before this specific prediction can be trusted.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (CLL/SLL), per FDA approval literature (no EU/TW license record on file) |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (evidence-pack stage: "Research Question" / S1 — see rationale) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the structured drug record for duvelisib. Based on the supporting literature retrieved for this candidate, duvelisib is a first-in-class oral dual inhibitor of phosphoinositide-3-kinase delta and gamma (PI3K-δ/γ), which sit downstream of the B-cell receptor (BCR) signaling pathway and are essential for the growth, survival, and migration of neoplastic lymphoid cells (PMID 30430368, 28388280). This mechanism underpinned its original approval for CLL/SLL and follicular lymphoma.

Hodgkin lymphoma and non-Hodgkin lymphoma are both malignancies of lymphoid origin, and PI3K/BCR-pathway signaling is broadly implicated across B- and T-cell lymphoid neoplasms, which is the mechanistic basis for the TxGNN model's prediction. However, a close read of the evidence retrieved specifically for "Hodgkin's lymphoma" shows an important caveat: **none of the 11 clinical trials or 15 publications actually enroll or discuss classical Hodgkin lymphoma** — instead they consistently describe indolent NHL, peripheral T-cell lymphoma, CLL/SLL, or mantle cell lymphoma. This pattern strongly suggests the TxGNN knowledge graph may have mapped "Hodgkin's lymphoma" as a proxy/adjacent node for the broader lymphoma space rather than reflecting a validated, disease-specific signal. As a result, this indication should currently be treated as a **research hypothesis requiring disease-mapping verification**, not as an evidence-backed repurposing candidate.

By contrast, other TxGNN-predicted indications for duvelisib in this same evidence pack — most notably "B-cell neoplasm" (rank 9, L1 evidence, driven by the pivotal Phase 3 DUO trial, NCT02004522) — are directly and robustly supported. This lends indirect plausibility to the PI3K-inhibitor mechanism in lymphoid malignancies generally, even while the Hodgkin-lymphoma-specific claim remains unconfirmed.

---

## Clinical Trial Evidence

*(from `predicted_indications[0]` — "Hodgkin's Lymphoma"; note: no trial in this list specifically enrolls classical Hodgkin lymphoma patients — all target NHL, PTCL, or related lymphoid malignancies)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Completed | 103 | Compared two intermittent dosing schedules of duvelisib in indolent NHL (iNHL); studied 2-week dose-holiday effects on tumor response and tolerability. |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Suspended | 170 | Randomized comparison of CHO(E)P vs CC-486-CHO(E)P vs Duvelisib-CHO(E)P in previously untreated CD30-negative peripheral T-cell lymphoma. |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1 | Completed | 48 | Assessed MTD and preliminary efficacy of duvelisib + rituximab (± bendamustine) in relapsed/refractory lymphoma or CLL. |
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unknown | 140 | Evaluated related PI3K inhibitor YY-20394 monotherapy in relapsed/refractory follicular NHL after ≥2 prior therapies. |
| [NCT05923502](https://clinicaltrials.gov/study/NCT05923502) | N/A | Not yet recruiting | 200 | Planned multicenter real-world observational study of duvelisib capsules in NHL. |
| [NCT02576275](https://clinicaltrials.gov/study/NCT02576275) | Phase 3 | Withdrawn | 0 | Planned pivotal RCT of duvelisib + bendamustine/rituximab vs placebo in previously-treated indolent NHL; withdrawn before enrollment. |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Completed | 14 | Dose-finding study of duvelisib in combination with BMS-986345 in lymphoid malignancies. |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) (DUAL) | Phase 1 | Withdrawn | 0 | Planned duvelisib + acalabrutinib combination in relapsed/refractory indolent NHL; withdrawn. |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Active, not recruiting | 42 | Dose escalation/expansion of duvelisib following CAR T-cell therapy, aiming to enhance CAR-T persistence via PI3K inhibition. |
| [NCT01882803](https://clinicaltrials.gov/study/NCT01882803) | Phase 2 | Completed | 129 | Pivotal monotherapy trial in refractory iNHL (follicular/marginal zone/small lymphocytic lymphoma) — basis for duvelisib's follicular lymphoma indication, not Hodgkin lymphoma. |

*(1 additional lower-relevance trial, NCT02640833, omitted for brevity — also unrelated to classical HL.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematic Review/Meta-analysis | Frontiers in Immunology | Meta-analysis of prospective trials evaluating safety/efficacy of dual PI3K-δ,γ inhibition (duvelisib) across relapsed/refractory lymphoid neoplasm subtypes. |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Review | The Lancet Oncology | Discusses duvelisib's role specifically in indolent non-Hodgkin lymphoma. |
| [29191916](https://pubmed.ncbi.nlm.nih.gov/29191916/) | 2018 | Phase 1 Clinical Trial | Blood | Foundational Phase 1 study (n=210) establishing MTD (75 mg BID) and clinical activity of duvelisib across advanced hematologic malignancies. |
| [31490009](https://pubmed.ncbi.nlm.nih.gov/31490009/) | 2019 | Phase 1 Clinical Trial | American Journal of Hematology | Phase 1 combination trial of duvelisib with rituximab ± bendamustine in NHL and CLL patients. |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Review | Am J Health-Syst Pharm | Summarizes FDA-approved targeted therapies, including duvelisib, for B- and T-cell lymphomas. |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Review | Current Treatment Options in Oncology | Reviews the PI3K-inhibitor drug class, including duvelisib's mechanism and role in lymphoma treatment. |
| [33132100](https://pubmed.ncbi.nlm.nih.gov/33132100/) | 2021 | Review | Clin Lymphoma Myeloma Leuk | Discusses next-generation PI3K inhibitors and unmet needs in relapsed/refractory B-cell lymphoma. |
| [26413907](https://pubmed.ncbi.nlm.nih.gov/26413907/) | 2015 | Review | Expert Review of Hematology | Reviews BCR-signaling inhibitors (including early PI3K inhibitors) in B-cell lymphoproliferative disorders. |
| [27872741](https://pubmed.ncbi.nlm.nih.gov/27872741/) | 2016 | Review | Mediterr J Hematol Infect Dis | Reviews novel agents, including PI3K inhibitors, for follicular lymphoma. |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Review | Drugs | Reviews novel therapeutic approaches, including PI3K inhibitors, for follicular lymphoma. |

*(5 additional lower-priority items — an analytical/pharmacokinetic method paper, a T-cell lymphoma target-discovery paper, and papers on a different PI3K agent (copanlisib) — omitted as they do not add disease-specific evidence for this indication.)*

---

## EU Market Information

Duvelisib currently has **no EU marketing authorization on file** (`total_licenses: 0`, `market_status: 未上市`). No product/authorization table can be produced from the available data.

---

## Cytotoxicity

Duvelisib is an antineoplastic agent (its literature-documented original indication, CLL/SLL, is a hematologic malignancy), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral dual PI3K-δ/γ small-molecule kinase inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (no quantified hematologic toxicity data available in this evidence pack) |
| Emetogenicity Classification | Low (typical of oral small-molecule kinase inhibitors as a class; not separately confirmed in this evidence pack) |
| Monitoring Items | CBC, liver function tests, and renal function; literature in this pack references historical FDA boxed warnings for hepatotoxicity, severe diarrhea/colitis, and pneumonitis/infections — clinical monitoring should cover these organ systems |
| Handling Protection | Despite oral administration, duvelisib is a hazardous antineoplastic agent and should be handled per institutional cytotoxic/hazardous-drug handling protocols |

---

## Safety Considerations

Please refer to the SmPC for safety information — the structured safety fields in this evidence pack (`key_warnings`, `contraindications`, `ddi`) are all data gaps, and DDI query status is `not_found`.

For context only: literature within this evidence pack notes that duvelisib carried FDA boxed warnings (hepatotoxicity, severe colitis, pneumonitis, and infections) and was **voluntarily withdrawn from the market in 2021** for commercial and safety-related reasons — this should be independently verified against the official SmPC/USPI before any further use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence pack's own scoring for this specific indication (Hodgkin's Lymphoma) is L4 / decision stage S1 ("Research Question") — an early, mechanism-level stage, not a clinically actionable one.
- Critically, all 11 trials and 15 publications retrieved for "Hodgkin's Lymphoma" actually describe NHL, PTCL, CLL/SLL, or MCL populations — there is **no direct clinical evidence in classical Hodgkin lymphoma**, raising concern about a disease-label/knowledge-graph mapping error that must be resolved before this candidate can advance.
- A **Blocking** data gap (DG001: TFDA/SmPC warnings and contraindications) independently prevents entry into the S1 safety pre-assessment stage regardless of efficacy evidence.

**To proceed, the following is needed:**
- Verify whether the TxGNN "Hodgkin's lymphoma" node is correctly mapped, or whether it is an artifact of the model associating duvelisib with the broader lymphoma disease cluster (given all supporting evidence is NHL/PTCL/CLL-specific).
- Obtain official product labeling / SmPC warnings and contraindications (DG001, Blocking) via the regulatory agency's official product label, as this currently blocks any safety pre-assessment.
- Obtain a formal DrugBank/pharmacology MOA record (DG002, High) to support a rigorous mechanistic-link analysis rather than relying on secondary literature.
- If disease-mapping is confirmed correct, consider redirecting the primary repurposing focus toward "B-cell neoplasm" (rank 9), which already has L1-level Phase 3 evidence (DUO trial, NCT02004522) and a "Proceed with Guardrails" recommendation — a substantially stronger evidence base than the top-ranked Hodgkin's lymphoma prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

