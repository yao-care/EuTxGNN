---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Insulin Degludec
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

# Insulin Degludec: From Diabetes Management to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec (Tresiba®) is an ultra-long-acting basal insulin analog approved globally for the management of diabetes mellitus in adults and children, though it is currently not registered in Taiwan.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus**,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 (Taiwan) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin degludec is a second-generation ultra-long-acting basal insulin analog. Although formal mechanism of action data was not retrieved in this Evidence Pack, based on its well-established pharmacological profile, insulin degludec works by binding to insulin receptors in peripheral target tissues—primarily skeletal muscle and adipose tissue—promoting glucose uptake and suppressing hepatic glucose production. After subcutaneous injection, it forms soluble multi-hexamers that slowly dissociate into monomers, producing a flat and stable absorption curve with a duration of action exceeding 42 hours. Compared to first-generation analogs such as insulin glargine and insulin detemir, insulin degludec demonstrates approximately 20% lower pharmacodynamic variability (coefficient of variation), translating to more predictable glycemic control and a significantly reduced risk of nocturnal hypoglycemia.

Type 1 Diabetes Mellitus is caused by autoimmune destruction of pancreatic β-cells, resulting in absolute insulin deficiency. Insulin replacement is not merely a treatment option—it is a survival necessity for T1DM patients. Insulin degludec directly addresses this core pathophysiology by providing stable, long-duration basal insulin coverage. Its ultra-flat action profile is particularly advantageous in T1DM, where day-to-day glycemic variability is inherently high and hypoglycemia risk is a major concern.

The TxGNN prediction score of 99.44% reflects this direct and mechanistically unambiguous link. Importantly, this prediction is not a speculative repurposing signal: insulin degludec is already approved for T1DM in the European Union, United States, and Japan. The high confidence score is consistent with the model correctly identifying an established yet Taiwan-unregistered therapeutic application. Proceeding with this prediction is therefore less about de novo drug development and more about addressing a regulatory gap in the Taiwan market.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Once-weekly insulin efsitora alfa (LY3209590) compared with once-daily insulin degludec in T1DM patients on MDI therapy; insulin degludec served as the gold-standard active comparator, confirming its benchmark efficacy and safety role in T1DM |
| [NCT02034513](https://clinicaltrials.gov/study/NCT02034513) | Phase 3 | Completed | 501 | SWITCH 1: double-blind crossover RCT comparing insulin degludec vs. insulin glargine, both combined with mealtime insulin aspart, in T1DM adults; demonstrated non-inferior HbA1c reduction with significantly lower hypoglycemia rates favouring degludec |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1,392 | PRONTO-T1D: randomized double-blind RCT of LY900014 vs. insulin lispro in T1DM, both administered in combination with either insulin glargine or insulin degludec as basal insulin; confirmed degludec's efficacy as a basal component in T1DM regimens |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Phase 3 trial investigating insulin degludec/insulin aspart (IDegAsp, once daily + aspart for remaining meals) vs. insulin detemir in children and adolescents with T1DM; demonstrated comparable glycemic control with a favourable safety profile in paediatric populations |
| [NCT03328845](https://clinicaltrials.gov/study/NCT03328845) | Phase 4 | Completed | 300 | INEOX study: evaluated oxidative stress parameters across different current insulin analogs in T1DM patients; provided mechanistic safety data on degludec's metabolic footprint beyond glycemic endpoints |
| [NCT02192450](https://clinicaltrials.gov/study/NCT02192450) | Phase 4 | Completed | 149 | Assessed whether insulin degludec reduces the risk of symptomatic nocturnal hypoglycemia compared to insulin glargine in T1DM patients at high risk of severe nocturnal hypoglycemia; confirmed clinically meaningful benefit in this high-risk subgroup |
| [NCT00612040](https://clinicaltrials.gov/study/NCT00612040) | Phase 2 | Completed | 178 | Early foundational treat-to-target trial comparing two insulin degludec (NN1250) formulations vs. insulin glargine in a basal-bolus regimen in T1DM adults; established dose-finding and initial efficacy/safety basis for degludec in T1DM |
| [NCT00841087](https://clinicaltrials.gov/study/NCT00841087) | Phase 2 | Completed | 65 | Japanese exploratory Phase 2 study assessing safety (with emphasis on hypoglycemia) of insulin degludec + NovoRapid in T1DM patients switching from long-acting insulin in a basal-bolus regimen; provided early Asian-specific safety data |
| [NCT04409587](https://clinicaltrials.gov/study/NCT04409587) | Phase 4 | Completed | 59 | BIGLEAP: investigator-initiated crossover trial comparing once-daily insulin degludec injection vs. CSII basal delivery in T1DM, both with bolus aspart via pump; assessed glycemic variability, overall control, and hypoglycemia incidence via CGM |
| [NCT03463564](https://clinicaltrials.gov/study/NCT03463564) | Phase 4 | Recruiting | 150 | METRO study: comparing insulin pump vs. multiple daily injections (including degludec as basal insulin) in T1DM adolescents transitioning to adult care; evaluating glycemic and metabolic outcomes in this high-risk transition period |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | *Lancet* | ONWARDS 6: Phase 3a RCT comparing once-weekly insulin icodec vs. once-daily insulin degludec in T1DM adults on basal-bolus regimen; degludec as active comparator confirmed its standard-of-care status in T1DM |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | *Lancet* | QWINT-5: Phase 3 non-inferiority RCT of once-weekly insulin efsitora alfa vs. insulin degludec in T1DM adults; insulin degludec again served as the benchmark comparator, validating its established role |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | *Lancet Diabetes & Endocrinology* | EXPECT trial: first dedicated RCT comparing degludec vs. insulin detemir (both with insulin aspart) in pregnant women with T1DM; demonstrated non-inferiority with comparable maternal and neonatal safety profiles |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review / Meta-analysis | *Clinical Therapeutics* | Meta-analysis comparing degludec vs. insulin glargine and detemir in T1DM and T2DM; confirmed comparable HbA1c reduction with statistically significant reductions in overall and nocturnal hypoglycemia favouring degludec |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review | *Value in Health* | Network meta-analysis of basal insulin regimens in T1DM adults; positioned insulin degludec favourably relative to other long-acting analogs for hypoglycemia risk reduction and glycemic stability |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Evidence-based Review | *Diabetes & Metabolism* | Comprehensive review of randomized controlled and observational studies; documented superior fasting plasma glucose control and consistent nocturnal hypoglycemia reductions with degludec across both T1DM and T2DM real-world settings |
| [25081590](https://pubmed.ncbi.nlm.nih.gov/25081590/) | 2014 | Meta-analysis | *Diabetes Therapy* | Patient-level meta-analysis across seven Phase 3a trials comparing degludec vs. insulin glargine in T1DM and T2DM; established the consistent advantage in nocturnal hypoglycemia with non-inferior overall glycemic control |
| [35476308](https://pubmed.ncbi.nlm.nih.gov/35476308/) | 2022 | Systematic Review | *International Journal of Clinical Pharmacy* | Indirect treatment comparison of degludec U100 vs. insulin glargine U300 in T1DM; evaluated safety, efficacy, and cost-effectiveness differences to support formulary decision-making |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Narrative Review | *Endocrinología y Nutrición* | Early clinical review summarizing the pharmacological rationale for degludec (soluble multi-hexamer formation, ultra-long flat action profile) and key clinical outcomes from T1DM and T2DM development trials |
| [40098468](https://pubmed.ncbi.nlm.nih.gov/40098468/) | 2025 | RCT Extension | *Diabetes Technology & Therapeutics* | INHALE-3 extension: 30-week study of inhaled technosphere insulin combined with insulin degludec in T1DM adults; confirmed sustained HbA1c and time-in-range benefits with degludec as the basal component in a novel combination regimen |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin degludec has robust Phase 3 RCT evidence—including multiple completed head-to-head trials directly in T1DM populations—and is approved by the EMA, FDA, and PMDA. The Taiwan non-registration represents a regulatory gap, not an evidence gap, and the clinical evidence fully supports a market authorization application with TFDA.

**To proceed, the following is needed:**
- **Taiwan safety documentation**: Obtain and parse the full prescribing information (global SmPC / package insert) to document key warnings, contraindications, and clinically relevant drug interactions required for local regulatory submission
- **Mechanism of action dossier**: Retrieve the complete DrugBank entry (DB09564) to formally document pharmacodynamic and pharmacokinetic properties for the TFDA regulatory file
- **TFDA market access pathway assessment**: Evaluate the applicable submission route (e.g., abbreviated NDA based on existing EMA/FDA approvals), estimate timeline, and assess National Health Insurance reimbursement positioning against currently listed basal insulin analogs
- **Local clinical needs assessment**: Review whether any Taiwan-specific population data (e.g., East Asian PK differences, local hypoglycemia risk profiles) would be requested by TFDA reviewers
- **Pharmacovigilance plan**: Design a post-marketing surveillance framework aligned with TFDA requirements to monitor hypoglycemia events and injection-site reactions in the local population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

