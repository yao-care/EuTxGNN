---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Long-acting Basal Insulin to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir (Levemir®) is a long-acting basal insulin analogue with globally established use in both type 1 and type 2 diabetes mellitus, though it is not currently authorised in this market.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus (T1DM)** — a finding consistent with its established global clinical role —
with **over 50 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in this market (0 EU authorisations on record) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed (commercial withdrawal, 2023) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin detemir is a soluble, long-acting human insulin analogue created by acylating human insulin with a 14-carbon fatty acid chain. Following subcutaneous injection, this fatty acid modification allows the molecule to reversibly bind albumin — both at the injection site and in the systemic circulation — dramatically slowing absorption and extending the duration of glucose-lowering action to approximately 24 hours. Compared to NPH (Neutral Protamine Hagedorn) insulin, insulin detemir produces a flatter, more predictable pharmacokinetic profile with substantially less within-patient variability, translating into lower rates of nocturnal hypoglycaemia in clinical practice. Although detailed MOA documentation is not yet retrieved from DrugBank, the drug's mechanism is well characterised in the published literature cited below.

Type 1 diabetes mellitus is defined by autoimmune destruction of pancreatic β-cells, resulting in an absolute deficiency of endogenous insulin secretion. This creates a direct, mechanistically unambiguous therapeutic need: exogenous basal insulin supplementation must replace the physiological tonic insulin secretion that β-cells can no longer provide. Insulin detemir addresses precisely this deficit. Without adequate basal insulin coverage, T1DM patients rapidly develop life-threatening diabetic ketoacidosis. There is therefore no "mechanistic gap" to bridge — the drug is the physiological solution to the disease's core deficit.

Globally, insulin detemir has been granted marketing authorisation by the EMA, FDA, and multiple other regulatory agencies for use in T1DM across all age groups, including children from age 2 and pregnant women. The current EU status of "not marketed" reflects Novo Nordisk's voluntary commercial withdrawal of Levemir® from the EU in 2023 as part of a portfolio rationalisation strategy — a decision unrelated to safety or efficacy. The TxGNN prediction score of 99.77% therefore captures an established, evidence-rich clinical relationship rather than a speculative repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Multinational parallel-group RCT comparing insulin detemir vs NPH insulin (each combined with insulin aspart) in pregnant women with T1DM across Africa, Europe, the Americas, and Oceania; directly evaluated blood glucose control and safety in a high-risk T1DM subpopulation |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | Completed | 447 | Europe/USA RCT establishing that insulin detemir is a safe and at least as effective alternative to insulin glargine in T1DM basal-bolus therapy combined with insulin aspart |
| [NCT01074268](https://clinicaltrials.gov/study/NCT01074268) | Phase 3 | Completed | 456 | Multinational BEGIN BB T1 trial comparing next-generation insulin degludec against insulin detemir (both with aspart) in T1DM; provides head-to-head comparative data with detemir as the active reference standard |
| [NCT00435019](https://clinicaltrials.gov/study/NCT00435019) | Phase 3 | Completed | 348 | European RCT comparing insulin detemir vs NPH insulin in children and adolescents with T1DM on a once- or twice-daily basal-bolus regimen using insulin aspart |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Phase 3 | Completed | 88 | Multicentre crossover non-inferiority RCT comparing fasting blood glucose variability between insulin detemir and insulin glargine (each combined with insulin glulisine) in T1DM patients |
| [NCT00773279](https://clinicaltrials.gov/study/NCT00773279) | Phase 3 | Completed | 242 | USA multicenter crossover RCT comparing insulin detemir ± insulin aspart administered via a new disposable pen (PDS290/FlexTouch®) vs the established FlexPen® in T1DM and T2DM; assessed glycaemic control and patient device preference |
| [NCT00604344](https://clinicaltrials.gov/study/NCT00604344) | Phase 3 | Completed | 401 | Japanese 48-week parallel-group RCT comparing insulin detemir vs NPH insulin in patients with insulin-requiring diabetes on a basal-bolus regimen; the pivotal trial supporting the Japanese regulatory approval |
| [NCT00623194](https://clinicaltrials.gov/study/NCT00623194) | Phase 3 | Completed | 146 | European 52-week multinational open-label extension trial assessing long-term safety of insulin detemir (with insulin aspart) in children and adolescents aged 3–17 years with T1DM; specifically evaluated antibody development |
| [NCT00700765](https://clinicaltrials.gov/study/NCT00700765) | N/A | Completed | 1,531 | Large Asian observational safety study (Korea, other Asian sites) evaluating the incidence of adverse events with Levemir® under routine clinical practice conditions in T1DM and T2DM patients |
| [NCT00626080](https://clinicaltrials.gov/study/NCT00626080) | N/A | Completed | 40 | Mechanistic study comparing the effect of subcutaneous insulin detemir vs NPH insulin on cerebral glucose metabolism and blood flow in appetite-regulating brain regions in T1DM patients, investigating the pharmacological basis of detemir's observed weight-neutral profile |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review / Network Meta-analysis | Value in Health | Assessed relative efficacy and safety of all basal insulin regimens (detemir, glargine, degludec, NPH) in adults with T1DM; provides the most comprehensive indirect comparative evidence base |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review / Meta-analysis | Clinical Therapeutics | Compared efficacy and tolerability of insulin degludec vs insulin glargine and insulin detemir in T1DM and T2DM; quantified HbA1c differences and hypoglycaemia event rates across long-acting analogues |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | The Lancet Diabetes & Endocrinology | EXPECT trial: open-label multinational non-inferiority RCT of insulin degludec vs insulin detemir in pregnant women with T1DM; the most recent head-to-head trial placing detemir as the established comparator |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Clinical Practice Review | The Lancet Diabetes & Endocrinology | Comprehensive update on lifestyle, pharmacological options (including basal insulin analogues), and diabetes technology for achieving glycaemic targets in T1DM pregnancy; contextualises detemir's role in current guidelines |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Meta-analysis | Polskie Archiwum Medycyny Wewnetrznej | Systematic review and meta-analysis directly comparing long-acting insulin detemir vs NPH insulin in T1DM; pooled analysis of glycaemic control improvement and hypoglycaemia reduction |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Drug Review | Drugs | Definitive pharmacological review of insulin detemir covering its self-association and albumin-binding mechanism, glucose-clamp evidence for reduced within-patient variability vs NPH, and consolidated clinical safety data in T1DM and T2DM |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Narrative Review | Vascular Health and Risk Management | Update on T1DM and T2DM treatment focusing on insulin detemir; compares HbA1c outcomes, hypoglycaemia rates, and weight effects vs NPH insulin across pivotal trials |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Drug Review | Drugs | Foundational review establishing insulin detemir's albumin-binding mechanism of action, pharmacokinetic profile, and early Phase 2/3 clinical evidence in T1DM and T2DM at the time of regulatory submission |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Narrative Review | Vascular Health and Risk Management | Review of insulin detemir's less variable pharmacokinetic profile vs NPH/ultralente insulins and its clinical evidence supporting reduced hypoglycaemia risk in T1DM and T2DM |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Clinical Review | Paediatric Drugs | Review of insulin analogue preparations including insulin detemir for children and adolescents with T1DM; addresses the pharmacokinetic limitations of traditional insulins and the rationale for switching to long-acting analogues |

---

## EU Market Information

Insulin detemir (Levemir®) is not currently authorised in the EU. The product had previously received EMA marketing authorisation for the treatment of diabetes mellitus in adults, adolescents, and children aged 2 years and above (both T1DM and T2DM), but Novo Nordisk voluntarily withdrew the marketing authorisation in 2023. This withdrawal was a commercial portfolio decision and was explicitly not related to any safety signal or change in the benefit–risk profile of the medicine.

No active EU authorisation records are present in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Formal safety data (TFDA package insert warnings, contraindications, and drug-drug interaction records) were not available in this evidence pack (Data Gaps DG001 and DG002). Clinicians should consult the Levemir® SmPC or the equivalent prescribing information from EMA prior to clinical use. Key safety considerations known from published literature include: hypoglycaemia risk (including severe and nocturnal events), injection-site lipohypertrophy, weight changes, and adjustments required in renal or hepatic impairment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin detemir has an exceptionally strong evidence base for T1DM — multiple large Phase 3 RCTs, systematic reviews, and decades of post-marketing safety data globally — and the TxGNN prediction of 99.77% reflects this established clinical reality. The primary barrier to EU market access is regulatory-commercial (withdrawal of the prior authorisation) rather than any scientific uncertainty about efficacy or safety. A re-entry strategy requires navigating the regulatory pathway, not generating new clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway assessment:** Clarify whether re-submission of a marketing authorisation application to EMA is commercially viable, or whether the T1DM patient need in the EU is already adequately met by insulin glargine (Lantus®/Toujeo®) and insulin degludec (Tresiba®), which remain authorised
- **SmPC and safety data retrieval (DG001 — Blocking):** Download and parse the Levemir® SmPC to extract contraindications, boxed warnings, and special population guidance; this is required before any formal S1 safety evaluation can proceed
- **MOA documentation (DG002 — High):** Retrieve complete DrugBank entry for DB01307 to formally document the acylated insulin / albumin-binding mechanism of action; currently available from published sources but not yet in structured format for the evidence pack
- **Competitive landscape review:** Assess whether insulin detemir's commercial withdrawal from the EU creates a patient access gap specifically in T1DM populations where it had a differentiated profile (e.g., pregnancy, paediatrics, weight-neutral use), as this would strengthen the re-authorisation rationale
- **Biosimilar strategy:** Consider whether a biosimilar development pathway for insulin detemir in the EU is preferable to re-authorising the originator, given the existing global data package
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

