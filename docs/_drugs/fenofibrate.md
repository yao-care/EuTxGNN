---
layout: default
title: Fenofibrate
parent: Medium Evidence (L3-L4)
nav_order: 256
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Fenofibrate: predicted new indication Homozygous familial hypercholesterolemia (evidence level L4). Approved use: Adjunctive therapy to diet and exercise in high cardiovascular risk a…"
monitor_inn: "Fenofibrate"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "hypercholesterolemia, autosomal dominant", "hypolipoproteinemia (disease)", "hyperalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Fenofibrate: From Mixed Dyslipidaemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug, originally used (in fixed-dose combinations with a statin) to treat mixed dyslipidaemia in adults at high cardiovascular risk.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**, but the only linked clinical trial tests a different drug (alirocumab), so **no direct trial evidence** supports this prediction.
The more credible signals sit with hyperlipoproteinemia (many Phase 3 trials) and familial hypercholesterolemia (older small studies), as discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunctive therapy to diet and exercise in high cardiovascular risk adults with mixed dyslipidaemia, to reduce triglycerides and increase HDL-C when LDL-C is adequately controlled on simvastatin monotherapy (Cholib) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorizations in the data compiled) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fenofibrate activates PPARalpha, which lowers triglycerides and modestly raises HDL-C, with only a small direct LDL-lowering effect. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on the general pharmacology of the drug class.

In homozygous familial hypercholesterolemia (HoFH), the core defect is impaired LDL receptor function, so a PPARalpha agonist is mechanistically unlikely to work as monotherapy. At most it could serve as an add-on for associated hypertriglyceridemia. The high TxGNN score likely reflects network similarity between lipid disorders rather than a validated therapeutic link.

The only fenofibrate-specific item for this prediction is a 1984 cohort report in type II hyperlipoproteinemia, which included one HoFH patient with the greatest fall in cholesterol, but this is anecdotal.

For context, other predictions in the same analysis have stronger support:
- **Hyperlipoproteinemia** (L1, Proceed with Guardrails): multiple completed Phase 3 trials, but this largely overlaps with the existing labeled use and is not a novel repurposing finding.
- **Familial hypercholesterolemia** and **autosomal dominant hypercholesterolemia** (L3): small 1980s studies show lipid effects, including with colestipol, but modern LDL-lowering agents are superior.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in children and adolescents with HoFH. Does not involve fenofibrate, so it gives no direct evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | 22 patients with type II hyperlipoproteinemia on fenofibrate 300 mg/day; LDL-C fell about 24%. One HoFH patient showed the greatest fall in total and LDL cholesterol. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin lipid drugs. Fenofibrate monotherapy is mainly indicated for triglycerides above 500 mg/dl to reduce pancreatitis risk, with modest cardiovascular benefit. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Drug and surgical treatment of dyslipidemic children; fenofibrate among agents reported to reduce lipids, mostly in familial hypercholesterolemia. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia management and cardiovascular prevention. General context only. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Interactions of lomitapide (approved for HoFH) with lipid-lowering drugs including fenofibrate. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002559 | Cholib (cancelled) | Not specified | Adjunctive therapy to diet and exercise in high cardiovascular risk adults with mixed dyslipidaemia to reduce triglycerides and increase HDL C levels when... |
| EMEA/H/C/001243 | Pravafenix (cancelled) | Not specified | Adjunct to diet and other non-pharmacological treatment for mixed hyperlipidaemia in adults at high cardiovascular risk to reduce triglycerides and incr... |

## Safety Considerations

- **Contraindications (from a knowledge-graph source, not label text):** liver failure, liver disease, pancreatitis, gallbladder disease and gallstones (cholelithiasis), impaired renal function, myopathy, rhabdomyolysis and other muscle diseases, thrombocytopenia, anemia, and leukopenia/neutropenia-related conditions.
- **Drug Interactions (moderate level, 100 interactions recorded):** sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), many insulin products (human, aspart, degludec, detemir, glargine, glulisine, lispro), chenodeoxycholic acid, and esomeprazole. Blood glucose monitoring is advisable when combined with antidiabetic agents.

For authoritative warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for HoFH has no direct clinical evidence: the only linked trial tests alirocumab, and the mechanism (PPARalpha agonism) does not address the LDL receptor defect. Both EU authorizations are cancelled.

**To proceed, the following is needed:**
- Fenofibrate-specific clinical data in HoFH (even small mechanistic or add-on studies for associated hypertriglyceridemia)
- Detailed mechanism-of-action data and SmPC warnings/contraindications
- Clarification of current EU regulatory status and available formulations
- If pursuing a lipid-disorder repurposing direction, prioritize the hyperlipoproteinemia (mixed hyperlipidemia) and familial hypercholesterolemia add-on use cases, where more evidence exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

