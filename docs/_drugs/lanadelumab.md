---
layout: default
title: Lanadelumab
parent: High Evidence (L1-L2)
nav_order: 350
evidence_level: L1
indication_count: 10
---

# Lanadelumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Lanadelumab: From Hereditary Angioedema Prevention to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab (Takhzyro) is a monoclonal antibody originally used for routine prevention of recurrent attacks of hereditary angioedema (HAE) in patients aged 2 years and older.
The TxGNN model predicts it may be effective for **C1 inhibitor deficiency**, which is closely tied to the approved HAE indication rather than a true new use.
Currently, **5 clinical trials** and **20 publications** support this direction, including one placebo-controlled randomized trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Routine prevention of recurrent attacks of hereditary angioedema (HAE) in patients aged 2 years and older |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L1 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on the literature, lanadelumab is a fully human monoclonal antibody that inhibits plasma kallikrein (target: KLKB1).

In C1 inhibitor deficiency (HAE types I/II), the loss of C1-INH control allows plasma kallikrein to act unchecked. This produces excess bradykinin, a vasodilator that drives angioedema attacks. Inhibiting kallikrein directly addresses this pathway.

The predicted indication is essentially the same disease as the approved one, since HAE types I/II is caused by C1 inhibitor deficiency. This is therefore not a true repurposing case. It is better read as a validation that the model correctly recovers a known drug-disease relationship.

Other predictions on the list (for example pancreatitis, platelet disorders and inflammatory myopathies) have no trials or literature. They appear to be computational artifacts and are not evaluated further here.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Open-label study of safety, PK and efficacy in Chinese HAE patients over 26 weeks |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING study: safety, PK and attack prevention in children aged 2 to under 12 years |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Open-label efficacy and safety study in Japanese patients with HAE type I or II |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | N/A | Active, not recruiting | 155 | Japanese post-marketing survey of long-term safety and symptom improvement |
| [NCT04583007](https://clinicaltrials.gov/study/NCT04583007) | N/A | No longer available | N/A | Expanded access program for paediatric HAE and non-histaminergic angioedema with normal C1-INH |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab versus placebo for prevention of HAE attacks |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label extension | Allergy | HELP OLE: long-term effectiveness and safety in patients aged 12 years and older |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network meta-analysis | Drugs in R&D | Indirect comparison of long-term prophylaxis options, including lanadelumab |
| [40504359](https://pubmed.ncbi.nlm.nih.gov/40504359/) | 2025 | Real-world cohort | Advances in Therapy | EMPOWER: sustained effectiveness and safety over up to 36 months |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirect comparison | J Comp Eff Res | Lanadelumab versus a C1-esterase inhibitor in children under 12 |
| [40769455](https://pubmed.ncbi.nlm.nih.gov/40769455/) | 2025 | Real-world study | Ann Allergy Asthma Immunol | Disease control and quality of life across disease activity subgroups |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | First global approval; reduced HAE attacks versus placebo |
| [31560114](https://pubmed.ncbi.nlm.nih.gov/31560114/) | 2019 | Review | Drugs | Review of lanadelumab in HAE, including the pivotal HELP trial |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case report | J Allergy Clin Immunol Pract | Efficacy in acquired angioedema with C1-inhibitor deficiency |
| [39399485](https://pubmed.ncbi.nlm.nih.gov/39399485/) | 2024 | Case report | Front Immunol | Use in a kidney transplant patient with HAE and high cardiovascular risk |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004806 | Takhzyro | Not specified | Routine prevention of recurrent attacks of hereditary angioedema (HAE) in patients aged 2 years and older. |

This authorization is recorded as cancelled in the compiled data, so there is currently no valid EU marketing authorization.

## Safety Considerations

- **Drug Interactions**: The only recorded interaction is pharmacological: lanadelumab's own target, plasma kallikrein (KLKB1). This reflects its intended mechanism rather than a clinical drug-drug interaction.
- **Coagulation tests**: Lanadelumab may prolong aPTT through effects on the intrinsic pathway. This warrants caution in patients with bleeding disorders and when interpreting coagulation assays.

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials and a placebo-controlled randomized trial support lanadelumab in HAE caused by C1 inhibitor deficiency. However, this is the same condition as the approved indication, so it does not represent new-indication evidence. The EU authorization is also recorded as cancelled.

**To proceed, the following is needed:**
- Confirmation of the current EU regulatory status, since the only authorization is recorded as cancelled
- Warnings and contraindications from the SmPC, which are not available in the compiled data
- Detailed mechanism of action data from DrugBank
- A monitoring plan for coagulation parameters, particularly in patients with bleeding disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

