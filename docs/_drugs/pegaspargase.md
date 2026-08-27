---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase (DrugBank DB00059) is a PEGylated *E. coli*-derived L-asparaginase that is an established backbone component of multi-agent chemotherapy for acute lymphoblastic leukemia (ALL)/lymphoblastic lymphoma. The TxGNN model's top-ranked prediction, **precursor lymphoblastic lymphoma/leukemia** (score **99.96%**), is supported by **50 clinical trials** (multiple large, completed Phase 3 studies) and **20 publications** — but this "predicted" indication is, in substance, the drug's own pre-existing core indication rather than a genuinely novel repurposing target. Every other candidate in this evidence pack that would represent true repurposing (CLL/SLL, follicular lymphoma, methylcobalamin deficiency, etc.) currently has weak or no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in the regulatory license dataset (0 licenses on file). Based on the evidence pack's own mechanistic rationale and cited literature, Pegaspargase's established use is acute lymphoblastic leukemia (ALL) / lymphoblastic lymphoma as part of multi-agent chemotherapy. |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukemia (rank 1) — **note: this substantially overlaps with the drug's existing core indication; see caveat below** |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails *(applies to confirming the existing indication only — see Conclusion for the true repurposing candidates)* |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap (`original_moa: [Data Gap]`) in the structured drug record. However, the model's own repurposing rationale, corroborated by the cited literature (e.g., PMID 31030380, PMID 17696798), reconstructs the mechanism: **Pegaspargase depletes circulating asparagine.** Precursor (lymphoblastic) leukemic cells lack asparagine synthetase and cannot synthesize their own asparagine, making them highly sensitive to asparagine deprivation — this triggers inhibition of protein synthesis and apoptosis in the leukemic blasts. This is the well-established, clinically validated mechanism underpinning Pegaspargase's role as a core backbone agent in ALL/lymphoblastic lymphoma induction and consolidation regimens.

Importantly, this mechanistic sensitivity is specific to **precursor (lymphoblastic) cells**. Mature lymphoid malignancies (e.g., CLL/SLL, follicular lymphoma — ranks 2, 3, 4, 9 in this pack) typically retain higher asparagine synthetase expression and are mechanistically less plausible targets, which is exactly why those candidates carry no clinical trial or literature support in this dataset (see Conclusion).

**Critical caveat:** because "precursor lymphoblastic lymphoma/leukemia" (rank 1) and "acute lymphoblastic leukemia" (rank 5, also L1/99.89%) are essentially the disease area Pegaspargase is already used to treat, this top prediction should be read as the model **correctly recovering a known, established indication** rather than surfacing a novel repurposing opportunity. The evidence pack's own rationale text explicitly flags both as "本質上屬既有適應症而非探索性再利用" (essentially an existing indication, not exploratory repurposing).

---

## Clinical Trial Evidence

*(from predicted_indications[0] — "precursor lymphoblastic lymphoma/leukemia")*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | Completed | 5,377 | Randomized comparison of combination chemotherapy regimens in newly diagnosed standard-risk B-precursor ALL; large, directly relevant confirmatory evidence. |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Completed | 6,136 | International collaborative treatment protocol comparing combination chemotherapy regimens in children/adolescents with ALL. |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Active, not recruiting | 9,350 | Risk-adapted chemotherapy regimens for newly diagnosed standard-risk B-ALL / localized B-lineage lymphoblastic lymphoma. |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Active, not recruiting | 6,720 | Blinatumomab added to chemotherapy backbone (including pegaspargase) for newly diagnosed standard-risk/Down-syndrome B-ALL and localized B-LLy. |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | Recruiting | 5,000 | AIEOP-BFM ALL 2017 — international collaborative treatment protocol for children/adolescents with ALL, MRD-directed risk stratification. |
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | Completed | 470 | ALLR3 — international collaborative trial in relapsed/refractory ALL comparing combination chemotherapy regimens. |
| [NCT00222612](https://clinicaltrials.gov/study/NCT00222612) | Phase 4 | Unknown | 2,100 | UKALL 2003 — UK national trial in childhood ALL using MRD to define risk groups; large post-marketing validation. |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | Completed | 650 | NOPHO protocol comparing intermittent vs. continuous PEG-asparaginase dosing for asparagine depletion in children/young adults with ALL. |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Completed | 166 | Randomized comparison of calaspargase pegol vs. pegaspargase (both with combination chemotherapy) in newly diagnosed high-risk ALL. |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Recruiting | 440 | Randomized trial of levocarnitine prophylaxis to prevent asparaginase-associated hepatotoxicity in AYA patients with ALL/LL. |

---

## Literature Evidence

*(from predicted_indications[0] — "precursor lymphoblastic lymphoma/leukemia")*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232: dexamethasone and high-dose methotrexate improve outcomes in high-risk B-ALL in children/young adults. |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434: nelarabine added to pegaspargase-containing chemotherapy in newly diagnosed T-ALL. |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | Phase 3 trial | J Clin Oncol | COG AALL1231: bortezomib added to chemotherapy backbone in newly diagnosed T-ALL/T-LL, with reduced prophylactic cranial radiation. |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001: efficacy and toxicity of calaspargase pegol vs. standard pegaspargase in childhood ALL. |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Advances | GIMEMA LAL1913: pegaspargase-modified, risk-oriented pediatric-inspired regimen in adult Ph-negative ALL/LL. |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Review | Blood | "How I treat" review on managing pegaspargase toxicities in adults with ALL. |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Comprehensive review of pegaspargase (Oncaspar®) in ALL — pharmacology, efficacy, and safety profile. |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Expert consensus | Haematologica | Expert panel consensus on recognition, prevention, and management of asparaginase/pegaspargase-associated adverse events in adults. |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Phase 2 study | Int J Hematol | Multicenter study of pegaspargase efficacy, safety, and PK in previously untreated Japanese ALL patients. |
| [35987855](https://pubmed.ncbi.nlm.nih.gov/35987855/) | 2022 | Consensus recommendations | Bull Cancer | French Society of Children and Adolescent Cancers recommendations on managing pegaspargase-associated toxicities. |

---

## EU Market Information

No marketing authorizations are on file for Pegaspargase in this dataset (`market_status`: Not Marketed; `total_licenses`: 0). No product name, dosage form, or approved indication text is available to summarize.

---

## Cytotoxicity

Pegaspargase is an antineoplastic biologic (asparagine-depleting enzyme) used as a core component of ALL combination chemotherapy, meeting the criteria for inclusion of this section (original indication is a leukemia; the drug is a standard chemotherapy-regimen component).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — metabolic/enzyme-based antineoplastic agent (asparagine-depleting biologic, distinct from DNA-damaging cytotoxics) |
| Myelosuppression Risk | Not directly quantified in the safety dataset (`safety.key_warnings`/`contraindications` are data gaps). Literature evidence (PMID 40109190, PMID 31977001) indicates the dominant toxicities are hepatotoxicity, pancreatitis, coagulopathy/thrombosis, hypertriglyceridemia, and hypersensitivity reactions rather than classic direct myelosuppression — though it is typically given within myelosuppressive multi-agent regimens. |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions (no data provided) |
| Monitoring Items | Liver function (ALT/AST/bilirubin), pancreatic enzymes (amylase/lipase), coagulation parameters (fibrinogen, antithrombin), triglycerides, and hypersensitivity/infusion reaction monitoring, per the cited toxicity-management literature |
| Handling Protection | As a component of combination cytotoxic chemotherapy regimens, standard cytotoxic drug handling precautions apply |

---

## Safety Considerations

Please refer to the SmPC for safety information. (`key_warnings`, `contraindications`, and `ddi` are all marked as data gaps or not found in this evidence pack — DDI query status: not found, 0 interactions on file.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails — but only as confirmation of the existing indication, not as a novel repurposing candidate**

**Rationale:**
- The top-ranked TxGNN prediction (precursor lymphoblastic lymphoma/leukemia, L1, 50 trials/20 publications) and the closely related rank-5 prediction (acute lymphoblastic leukemia, also L1) both correspond to Pegaspargase's already-established core indication, as explicitly noted in the model's own repurposing rationale. This is a valuable sanity check on the model but does **not** constitute new therapeutic ground.
- All genuinely exploratory candidates in this pack are weak: CLL/SLL, its pregerminal-center subtype, follicular lymphoma, and CLL/SLL (again, rank 9) are all L5/Hold with zero trials or literature and mechanistically implausible (mature B-cell neoplasms generally retain asparagine synthetase). The methylcobalamin-deficiency (cblE) prediction (rank 6) is very likely a spurious knowledge-graph embedding artifact with no plausible biological link.
- "Lymphoid neoplasm" (rank 7, L2) and "Hodgkin's lymphoma" (rank 8, L2) warrant a **Research Question** stage only: the underlying trial/literature evidence largely concerns extranodal NK/T-cell lymphoma (NKTCL), not classic Hodgkin lymphoma — a likely disease-label mismatch that needs manual curation before any further action.
- "Blast phase CML, BCR-ABL1 positive" (rank 10, L4) has only indirect, non-specific evidence (general Ph+ ALL/leukemia induction trials) and remains a Hold.

**To proceed, the following is needed:**
- TFDA/EMA label data (SmPC or 仿单) to establish the actual original indication and safety/contraindication text — currently a Blocking data gap (DG001)
- Formal DrugBank MOA confirmation to replace the reconstructed mechanism used in this report (High-severity data gap, DG002)
- Manual disease-label verification for the "Hodgkin's lymphoma" and "lymphoid neoplasm" predictions, given the apparent NKTCL/Hodgkin mismatch in the underlying trial and literature evidence
- If genuine repurposing signal is the goal, deprioritize ranks 1 and 5 (duplicate of known indication) and instead commission targeted literature/trial searches for the lower-ranked, mechanistically distinct candidates before advancing any to S1+
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

