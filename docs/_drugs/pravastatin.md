---
layout: default
title: Pravastatin
parent: Medium Evidence (L3-L4)
nav_order: 497
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Pravastatin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L4). Approved use: Adjunct to diet for mixed hyperlipidaemia in adults at high cardiovas…"
monitor_inn: "Pravastatin"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "hypoalphalipoproteinemia", "cholesterol-ester transfer protein deficiency"]
---

# Pravastatin
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

# Pravastatin: From Mixed Hyperlipidaemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a statin, originally authorised in the EU (as part of the fixed-dose product Pravafenix) for mixed hyperlipidaemia in adults at high cardiovascular risk.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**, but the data compiled for this report contain **1 clinical trial** (which tests a different drug) and **13 publications** (mostly reviews of other lipid-lowering agents), so there is no direct pravastatin evidence for this use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunct to diet for mixed hyperlipidaemia in adults at high cardiovascular risk, to reduce triglycerides and increase HDL-C when LDL-C is adequately controlled on pravastatin 40 mg or another moderate-intensity statin |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pravastatin belongs to the statin class, which inhibits HMG-CoA reductase and upregulates hepatic LDL receptors, and its lipid-lowering efficacy in hyperlipidaemia is well established. Mechanistically, it could be applicable to familial hypercholesterolemia, which is also a disorder of high LDL cholesterol.

However, the rationale is weak for the homozygous form. Homozygous familial hypercholesterolemia involves severely reduced or absent LDL receptor function, so a drug that works by raising LDL receptor expression is expected to have limited effect. One of the retrieved reviews also states that statins are not very effective in this condition. The prediction therefore appears to reflect network proximity in lipid metabolism rather than a demonstrated therapeutic link.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (a PCSK9 inhibitor) in children and adolescents aged 8–17 with homozygous familial hypercholesterolemia. Pravastatin is not the investigational agent, so it provides no direct evidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Updated review of statins for children with familial hypercholesterolemia |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidaemia management and cardiovascular disease prevention |
| [15532136](https://pubmed.ncbi.nlm.nih.gov/15532136/) | 2004 | Review | Prescrire Int | Notes statins are not very effective in familial homozygous hypercholesterolaemia |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin indicated for several hyperlipidaemias, including homozygous familial hypercholesterolemia |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review; reported superior lipid improvement vs pravastatin in hypercholesterolaemia |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe, a cholesterol absorption inhibitor |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Review | Cardiovasc Drug Rev | Ezetimibe as a first-in-class cholesterol absorption inhibitor |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology and therapeutic potential in hyperlipidaemias |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Atorvastatin in primary hypercholesterolemia and mixed dyslipidemias |

None of these papers provides direct evidence of pravastatin efficacy in homozygous familial hypercholesterolemia.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001243 (cancelled) | Pravafenix | Not specified | Adjunct to diet and other non-pharmacological treatment for mixed hyperlipidaemia in adult patients at high cardiovascular risk to reduce triglycerides and incr... |

## Safety Considerations

Package-insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for safety information.

- **Knowledge-graph contraindication signals** (from a drug-disease knowledge graph, not label text): kidney disease, liver disease, gallbladder disease, myopathy and other muscle disease, rhabdomyolysis, thrombocytopenia, peptic ulcer disease, gout, hemophilia, anaemia, nephrolithiasis, and others. These should be verified against the official label.
- **Drug Interactions**: 100 interactions were found. Moderate-level interactions include metronidazole, clarithromycin, eluxadoline, naltrexone, pectin, rosuvastatin, simvastatin and tinidazole. Others (for example calcitriol, acarbose, sucralfate, prednisone) have an unclassified severity level.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score. The one linked trial tests a different drug, the literature is largely about other lipid-lowering agents, and the biology of absent LDL receptor function argues against meaningful statin efficacy. The only EU authorisation for a pravastatin-containing product is cancelled.

**To proceed, the following is needed:**
- Direct pravastatin efficacy data in homozygous familial hypercholesterolemia (or a clear rationale for residual LDL receptor activity in the target patients)
- Mechanism of action data and SmPC warnings and contraindications
- Review of current EU authorisations of other pravastatin products to clarify the market situation
- Comparison against established therapies for this condition (such as PCSK9 inhibitors)

*Other predictions with more relevant evidence:* Heterozygous familial hypercholesterolemia and autosomal dominant hypercholesterolemia have substantial pediatric pravastatin data (evidence level L3), but they represent established statin uses rather than true repurposing. Dyslipidemia in HIV has the largest body of pravastatin-specific trials (evidence level L2) and is an indication for cardiovascular risk management in people with HIV, not treatment of HIV itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

