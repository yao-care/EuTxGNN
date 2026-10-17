---
layout: default
title: Rasburicase
parent: AI Predictions (L5)
nav_order: 510
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Rasburicase: predicted new indication Hypouricemia, renal (evidence level L5). Approved use: Treatment and prophylaxis of acute hyperuricaemia…"
monitor_inn: "Rasburicase"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Rasburicase: From Tumour Lysis-Related Hyperuricaemia to Renal Hypouricaemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase, originally used to treat and prevent acute hyperuricaemia in patients with haematological malignancies at risk of tumour lysis.
The TxGNN model predicts it may be effective for **renal hypouricaemia**, but **no clinical trials and no publications** currently support this prediction.
The mechanistic review also suggests that the prediction is biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment and prophylaxis of acute hyperuricaemia, to prevent acute renal failure, in adults, children and adolescents (0–17 years) with haematological malignancy with a high tumour burden at risk of rapid tumour lysis or shrinkage at the start of chemotherapy |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Rasburicase is known to be a recombinant urate oxidase. It converts uric acid to allantoin, which is more soluble and easily excreted, and so it lowers serum uric acid quickly.

Renal hypouricaemia is already a condition of abnormally low serum uric acid, caused by defects in urate transporters such as URAT1 and GLUT9. Further urate lowering would be mechanistically counterproductive and could worsen the phenotype. The high TxGNN score (rank 296) therefore appears to reflect proximity in the knowledge graph (the uric acid pathway) rather than a true therapeutic link.

Other top-ranked predictions are also weakly supported. Partial HPRT deficiency has a conceptual link to urate lowering, but rasburicase is immunogenic, which limits repeated dosing, and it does not address purine overproduction. Chronic management is already served by xanthine oxidase inhibitors. Most of the other predictions (hepatic porphyria, hepatopulmonary syndrome, portal vein and portal hypertension disorders, copper-associated cirrhosis, renal tubular acidosis, phenylalanine metabolism disorders) have no identifiable mechanistic link. Several share identical scores, which suggests a non-specific graph artifact.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000331 (cancelled) | Fasturtec | Not specified | Treatment and prophylaxis of acute hyperuricaemia, in order to prevent acute renal failure, in adults, children and adolescents (aged 0 to 17 years) with haem... |

## Safety Considerations

- **Drug Interactions**: 13 interactions were identified in the DDI database. Two are rated **Major**: prilocaine and nitrous acid. Most of the others are rated Moderate and involve topical or ophthalmic local anaesthetics (tetracaine, lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine, cinchocaine). Idelalisib is also rated Moderate.
- **Other considerations from the mechanistic review**: Rasburicase is contraindicated in G6PD deficiency. It is immunogenic, which limits repeated dosing. It also generates hydrogen peroxide, which adds oxidative stress and is undesirable in porphyria.

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by a model score only (L5), with no clinical trials or literature. The mechanism argues against benefit, since lowering uric acid in a condition of already low uric acid could be harmful. The product's only EU authorization is also cancelled.

**To proceed, the following is needed:**
- A biological rationale that justifies the prediction, or a decision to deprioritize it as a graph artifact
- Mechanism of action data from DrugBank
- Warnings and contraindications from the SmPC
- Review of lower-ranked or alternative predictions, such as partial HPRT deficiency, for acute severe hyperuricaemia use only
- Clarification of the regulatory status, given that the only EU authorization is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

