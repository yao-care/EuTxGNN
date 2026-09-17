---
layout: default
title: Fenofibrate
parent: Medium Evidence (L3-L4)
nav_order: 249
evidence_level: L3
indication_count: 10
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fenofibrate: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate-class lipid-regulating agent, originally used to manage hypertriglyceridemia and mixed dyslipidemia. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, with **1 clinical trial** and **11 publications** currently identified, though most of this evidence only partially supports the specific drug-disease pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (fenofibrate is a fibrate-class PPAR-α agonist, generally indicated for hypertriglyceridemia / mixed dyslipidemia) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DG002, severity: High). Based on known pharmacological information, fenofibrate is a fibric acid derivative and PPAR-α agonist that lowers plasma triglycerides and VLDL while modestly raising HDL-C; its efficacy in hypertriglyceridemia and mixed dyslipidemia is well established.

HoFH is a distinct, rare genetic disorder in which LDL receptors are almost completely absent or non-functional, causing markedly elevated LDL-C from birth. Because fenofibrate's PPAR-α mechanism acts largely independently of LDL receptor function, its ability to lower LDL-C in HoFH is inherently limited — a caveat explicitly noted in the underlying rationale data ("HoFH为LDL受体几乎完全缺失，fenofibrate的PPAR-α機轉對LDL受体依賴性降膽固醇效果極弱，理論效益有限，主要仍作為TG/VLDL輔助控制").

In practice, fenofibrate's plausible role in HoFH is as an **adjunct** to standard LDL-lowering therapies (statins, PCSK9 inhibitors, LDL apheresis) — helping control residual triglycerides and VLDL rather than serving as a primary LDL-lowering treatment. This is a mechanistically coherent but modest rationale, consistent with the model assigning this indication a moderate-confidence score without strong drug-specific clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated **alirocumab** (a PCSK9 inhibitor, not fenofibrate) in children/adolescents with hoFH, assessing LDL-C reduction at Weeks 12, 24, and 48. Relevance grade C — only the patient population overlaps; the study drug is not fenofibrate. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacological Research Communications | 22 patients with type II hyperlipoproteinemia treated with fenofibrate 300mg/day; one patient with HoFH showed the greatest fall in total and LDL cholesterol among the cohort. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | Reviews liver transplantation for HoFH when standard lipid-lowering drugs and LDL-apheresis are insufficient; contextualizes emerging drug therapies. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE clinical practice guideline for dyslipidemia management and cardiovascular disease prevention. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Notes fenofibrate's most definite indication is severe hypertriglyceridemia (>500 mg/dl); offers modest cardiovascular event reduction. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the NY Academy of Sciences | Surveys pharmacologic/surgical treatment of dyslipidemic children with familial hypercholesterolemia, listing fenofibrate among agents used with variable success. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews LDL-C lowering strategies including statins and PCSK9 inhibitors for severe hypercholesterolemia. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Reviews ezetimibe (a different cholesterol-lowering agent) as background context for combination lipid therapy. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Pharmacology and therapeutic potential review of atorvastatin in hyperlipidaemia management. |
| [9627539](https://pubmed.ncbi.nlm.nih.gov/9627539/) | 1998 | Review | The Canadian Journal of Cardiology | Reviews advances in dyslipidemia drug treatment with focus on atorvastatin. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK Study | Pharmacotherapy | Characterizes pharmacokinetic interactions of lomitapide (an HoFH-approved MTP inhibitor) with commonly used lipid-lowering drugs including fenofibrate. |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence linking fenofibrate specifically to HoFH is thin: the single identified clinical trial (NCT03510715) tested a different drug (alirocumab) in the relevant patient population rather than fenofibrate itself, and the literature is dominated by general dyslipidemia reviews and guidelines rather than fenofibrate-specific HoFH data. Mechanistically, fenofibrate's PPAR-α action is largely LDL-receptor-independent, limiting its expected benefit in a disease defined by LDL receptor deficiency — it would likely function only as adjunctive TG/VLDL control rather than a primary therapy.

**To proceed, the following is needed:**
- TFDA/EMA labeling data — warnings, contraindications (currently blocking; DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Fenofibrate-specific (not class-general) clinical evidence in confirmed HoFH populations
- Clarification of fenofibrate's role as monotherapy vs. adjunct to LDL receptor-targeted therapies (statins, PCSK9 inhibitors, apheresis) in HoFH
- Drug interaction data given likely co-administration with statins/PCSK9 inhibitors in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

