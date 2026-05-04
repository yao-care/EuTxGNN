---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Prandial Glycemic Control to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine (Apidra®) is a rapid-acting human insulin analogue engineered for mealtime glucose control in patients with diabetes, with global regulatory approvals (FDA 2004, EMA) that are not yet reflected in the current local market registry.
The TxGNN model ranks **Type 1 Diabetes Mellitus (T1DM)** as the top predicted indication with a score of 99.55% — confirming its strongest mechanistic and clinical alignment —
supported by **50 clinical trials** and **19 publications** currently available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No local registration data available |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| EU Market Status | Not Registered (0 authorizations in database) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in the current local database. Based on published pharmacology, insulin glulisine is a rapid-acting human insulin analogue with amino acid substitutions at positions B3 (asparagine → lysine) and B29 (lysine → glutamic acid). These changes reduce self-aggregation and accelerate subcutaneous absorption, producing onset of action within 10–15 minutes and a duration of approximately 3–4 hours — closely mimicking the physiological first-phase insulin secretion that occurs in response to meals.

Type 1 diabetes mellitus is defined by the autoimmune destruction of pancreatic β-cells, leading to absolute insulin deficiency. Without exogenous insulin, patients cannot regulate postprandial glucose or suppress hepatic glucose output. Insulin glulisine addresses this directly: it binds the insulin receptor (IR), activates the PI3K/AKT signalling cascade, stimulates GLUT4 translocation for glucose uptake in muscle and adipose tissue, promotes glycogen synthesis, and suppresses gluconeogenesis. There is no indirect or extrapolated mechanism here — glulisine *is* the insulin replacement therapy that T1DM patients require.

This TxGNN prediction is therefore not a novel repurposing in the traditional sense. Rather, it represents a high-confidence confirmation: the model correctly identifies the drug's primary pharmacological target. The absence of local registration data is a regulatory record gap, not a gap in clinical evidence. With multiple completed Phase 3 and Phase 4 trials and over two decades of real-world use globally, the evidence base for this drug-disease pair is among the strongest possible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03328845](https://clinicaltrials.gov/study/NCT03328845) | Phase 4 | Completed | 300 | Prospective comparison of different insulin analogues including glulisine in T1DM patients; assessed impact on oxidative stress biomarkers over the treatment period |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Multicenter, open, non-randomised Phase 4 study directly evaluating the efficacy and safety of insulin glulisine in T1DM patients on insulin glargine; evaluated HbA1c, dosing, and patient satisfaction |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | Multicenter open Phase 3 study evaluating glulisine (HMR1964) efficacy (HbA1c change from baseline to week 26) and full safety profile in T1DM patients co-treated with insulin glargine |
| [NCT01204593](https://clinicaltrials.gov/study/NCT01204593) | Phase 4 | Completed | 206 | International, multicenter study of once-daily insulin glargine + three-times-daily insulin glulisine (basal-bolus) in T1DM patients previously uncontrolled on any insulin regimen; primary endpoint HbA1c change at week 24 |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Completed | 485 | Randomised, 12-week, multicenter trial comparing insulin glulisine (3:1) to insulin lispro in T1DM and T2DM; co-primary endpoints: HbA1c change and hypoglycemia frequency |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | Completed | 319 | INHALE-1: Open-label RCT comparing inhaled Afrezza to injectable rapid-acting analogues (aspart, lispro, or glulisine) combined with basal insulin in pediatric T1DM/T2DM over 26 weeks |
| [NCT00174642](https://clinicaltrials.gov/study/NCT00174642) | Phase 3 | Completed | 811 | Large multinational trial comparing stepwise introduction of glulisine boluses (1–3 injections) added to insulin glargine + metformin in T2DM patients poorly controlled on basal insulin |
| [NCT00135083](https://clinicaltrials.gov/study/NCT00135083) | Phase 3 | Completed | 347 | Non-inferiority study: 1 vs. 2 vs. 3 daily glulisine injections added to insulin glargine + oral sensitizer in T2DM; primary endpoint HbA1c at week 24 |
| [NCT04124302](https://clinicaltrials.gov/study/NCT04124302) | Phase 4 | Completed | 76 | Randomised study comparing two insulin dose-calculation methods on postprandial glycemia after mixed meals in children with T1DM; directly relevant to prandial glulisine dosing |
| [NCT02846831](https://clinicaltrials.gov/study/NCT02846831) | Phase 2 | Completed | 36 | Open-label, randomised, two-way crossover study comparing single-hormone closed-loop delivery (rapid-acting analogue including glulisine) vs. sensor-augmented pump in adults with T1DM over 12 outpatient days |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | RCT/Comparative | Acta Diabetologica | Real-world comparison of glulisine vs. lispro and aspart for continuous subcutaneous insulin infusion (CSII) in T1DM; evaluated HbA1c, fasting blood glucose, hyperglycemia, hypoglycemia, and DKA rates |
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Hormone and Metabolic Research | Multinational, randomised, parallel-group trial (n=683) comparing insulin glulisine to insulin lispro in adults with T1DM; demonstrated comparable glycemic control and safety profile |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technology & Therapeutics | Three-way randomised crossover trial comparing glulisine, aspart, and lispro delivered via CSII in T1DM; glulisine showed a trend toward fewer catheter occlusions |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technology & Therapeutics | 26-week RCT in pediatric T1DM comparing glulisine to lispro as part of a basal-bolus regimen; demonstrated comparable efficacy and safety in children and adolescents |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Clinical Study | Pediatrics International | Prospective study evaluating glulisine for CSII in 20 children with T1DM over 1 year; significant improvements in postprandial glucose at breakfast and dinner vs. baseline |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | PK/PD Study | Clinical Pharmacokinetics | Detailed pharmacokinetic and pharmacodynamic characterisation of insulin glulisine; confirms faster absorption, earlier peak action, and shorter duration than regular human insulin |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Comprehensive review of insulin glulisine (Apidra) in adults, adolescents, and children with diabetes; non-inferior to other rapid-acting insulins with a comparable glucose disposal profile |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Systematic Review | Drugs of Today | Systematic review of insulin analogues for T1DM in children and adolescents; glulisine is one of three approved rapid-acting analogues with distinct absorption characteristics |
| [17703632](https://pubmed.ncbi.nlm.nih.gov/17703632/) | 2007 | Review | Vascular Health and Risk Management | Reviews combining basal and prandial insulins for optimal glycemic control in T1DM and T2DM; discusses pharmacokinetic advantages of glulisine in reducing postprandial excursions |
| [19216625](https://pubmed.ncbi.nlm.nih.gov/19216625/) | 2009 | Review | Expert Opinion on Biological Therapy | Discusses basal/bolus therapy with insulin glulisine for optimised diabetes treatment; covers clinical evidence, physiological rationale, and early initiation of insulin strategy |

---

## EU Market Information

No marketing authorization records for insulin glulisine were found in the current database (0 entries). This is a known data gap: insulin glulisine (Apidra®, Sanofi) holds EMA approval and is commercialised across EU member states. Please verify the current authorization status and indication text directly via the [EMA EPAR database](https://www.ema.europa.eu/en/medicines/find-medicine/european-public-assessment-reports).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin glulisine has one of the strongest evidence profiles of any candidate in this pipeline: it is globally approved (FDA 2004, EMA) for T1DM with multiple completed Phase 3 and Phase 4 trials and over 19 peer-reviewed publications, including direct head-to-head RCTs in both adult and pediatric T1DM populations. The TxGNN L1 prediction score of 99.55% reflects this alignment. The primary constraint is not clinical but regulatory and administrative — the absence of local registration and safety data documentation.

**To proceed, the following is needed:**
- Retrieve and parse the official SmPC (Apidra® EU SmPC or equivalent) to document warnings, contraindications, special populations, and drug interaction profile
- Confirm current EMA authorization status and retrieve approved indication text from the EPAR database
- Assess local market registration requirements and determine whether existing EMA approval can support expedited local registration pathways
- Obtain DrugBank MOA data (DB01309) to formally complete the mechanistic section of the repurposing dossier
- Review pediatric-specific dosing and device compatibility data (CSII pump compatibility) for completeness of the evidence package
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

