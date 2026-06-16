---
layout: default
title: Cerliponase Alfa
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase alfa: From CLN2 Disease to Scheie Syndrome

## One-Sentence Summary

Cerliponase alfa is a recombinant human tripeptidyl peptidase-1 (TPP1) enzyme replacement therapy delivered by intracerebroventricular infusion, indicated for CLN2 disease (Neuronal Ceroid Lipofuscinosis Type 2 / Batten disease).
The TxGNN model predicts it may be effective for **Scheie Syndrome** as its top-ranked candidate (score 99.98%), with 9 additional rare disease predictions also identified.
All 10 predicted indications carry **L5 evidence** (model prediction only, no clinical trials or supporting publications) and a uniform **Hold** recommendation due to fundamental mechanistic incompatibilities between TPP1 enzyme replacement and each predicted disease target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CLN2 Disease (Neuronal Ceroid Lipofuscinosis Type 2 / Batten Disease) |
| Predicted New Indication | Scheie Syndrome (MPS I-S, top prediction) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why This Prediction Requires Caution

Cerliponase alfa's mechanism of action data was not available in this evidence pack. Based on established pharmacological knowledge: cerliponase alfa is a recombinant human TPP1 (tripeptidyl peptidase-1), a serine protease that resides in lysosomes and degrades peptide fragments from ceroid lipofuscin. In CLN2 disease, loss-of-function mutations in the *CLN2* gene result in TPP1 deficiency, leading to pathological accumulation of ceroid lipofuscin in CNS neurons. Cerliponase alfa compensates for this deficiency by direct intracerebroventricular (ICV) infusion, bypassing the blood-brain barrier to deliver the enzyme to brain lysosomes.

Scheie syndrome (MPS I-S) is caused by a partial deficiency of **α-L-iduronidase (IDUA)**, a completely distinct lysosomal enzyme that degrades dermatan sulfate and heparan sulfate glycosaminoglycans. TPP1 and IDUA share no substrate, no structural homology, and no functional overlap. Furthermore, MPS I-S is a systemic disease requiring body-wide enzyme delivery — cerliponase alfa's ICV route restricts distribution to CNS tissue and cannot address the visceral, skeletal, or corneal manifestations that characterize MPS I. An approved ERT for MPS I (laronidase / Aldurazyme®) already exists.

The uniformly high TxGNN prediction scores across all 10 predicted indications (ranging from 99.90% to 99.98%) strongly suggest the model is detecting shared **"lysosomal storage disease" ontology nodes** in the knowledge graph rather than genuine enzyme-substrate relationships. Across every candidate — from Gaucher disease (glucocerebrosidase deficiency) to juvenile myoclonic epilepsy (ion channel disorder) to ichthyosis (skin barrier defect) — the mechanistic analysis reveals no biologically plausible connection to TPP1 replacement therapy. This pattern is consistent with a systematic knowledge graph artifact in the LSD disease cluster.

---

## All Predicted Indications — Mechanistic Assessment

| Rank | Disease | TxGNN Score | Evidence | Decision | Key Mechanistic Concern |
|------|---------|------------|----------|----------|-------------------------|
| 1 | Scheie syndrome | 99.98% | L5 | Hold | MPS I-S: IDUA deficiency — unrelated enzyme; laronidase already approved |
| 2 | Hurler syndrome | 99.97% | L5 | Hold | MPS I-H: IDUA deficiency (severe form) — same mismatch; laronidase approved |
| 3 | Lysosomal storage disease w/ skeletal involvement | 99.95% | L5 | Hold | Broad LSD category (GAG accumulation); TPP1 has no role in skeletal LSD subtypes |
| 4 | Cholesteryl ester storage disease | 99.93% | L5 | Hold | LAL/LIPA deficiency (lipase); sebelipase alfa already approved |
| 5 | Gaucher disease | 99.93% | L5 | Hold | GBA/GCase deficiency; retrieved publication is natural-history study, not a cerliponase trial |
| 6 | Familial encephalopathy w/ neuroserpin inclusion bodies | 99.93% | L5 | Hold | ER conformational disease (SERPINI1 misfolding) — not lysosomal; cerliponase alfa cannot clear ER aggregates |
| 7 | Wolman disease w/ hypolipoproteinemia & acanthocytosis | 99.92% | L5 | Hold | Complete LAL deficiency; same enzyme family mismatch as CESD |
| 8 | Myoclonic epilepsy, juvenile, susceptibility to | 99.92% | L5 | Hold | Polygenic GABA/ion channel epilepsy; no lysosomal enzyme deficiency; no mechanistic entry point for TPP1 |
| 9 | Proximal myopathy w/ extrapyramidal signs | 99.92% | L5 | Hold | Muscle/extrapyramidal syndrome; ICV route cannot deliver enzyme to skeletal muscle |
| 10 | Autosomal ichthyosis syndrome w/ fatal disease course | 99.90% | L5 | Hold | Skin barrier defect (ABCA12/SNAP29); no lysosomal link; ICV route anatomically unfeasible for skin disease |

---

## Clinical Trial Evidence

Currently no clinical trials are registered for cerliponase alfa in any of the 10 predicted indications.

---

## Literature Evidence

No relevant literature is available for the top predicted indication (Scheie Syndrome).

A single publication was retrieved for the Rank 5 prediction (Gaucher disease):

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41527340](https://pubmed.ncbi.nlm.nih.gov/41527340/) | 2026 | Natural History / Observational | Journal of Inherited Metabolic Disease | Natural history mapping framework using Gaucher disease as a precision medicine model for LSD drug development — not a cerliponase alfa intervention study |

> **Important**: This publication does not evaluate cerliponase alfa for Gaucher disease. It examines Gaucher disease natural history as a methodological model for rare disease research. Its retrieval reflects lysosomal storage disorder keyword overlap, not direct drug-disease relevance.

---

## Taiwan Market Information

Cerliponase alfa is not currently authorized in Taiwan (0 licenses registered).

> For reference: Cerliponase alfa (brand name **Brineura®**) is approved by the FDA (2017) and EMA for the treatment of CLN2 disease (Batten disease) in children aged ≥3 years. Taiwan registration status should be verified via the TFDA drug database.

---

## Safety Considerations

Please refer to the SmPC (Brineura® product monograph) for safety information. No drug-drug interaction data was identified in this evidence review, and TFDA label warnings and contraindications have not yet been retrieved (see Data Gaps below).

---

## Conclusion and Next Steps

**Decision: Hold (All 10 Predicted Indications)**

**Rationale:**
All ten TxGNN-predicted indications show fundamental mechanistic mismatches with cerliponase alfa's pharmacology: the drug replaces TPP1 serine protease specifically for CLN2 disease, while every predicted target involves a distinct lysosomal enzyme (IDUA, GBA, LAL), a non-lysosomal pathological mechanism (ER conformational disease, ion channelopathy), or an anatomically inaccessible tissue (skin, skeletal muscle) for ICV-delivered therapy. The uniformly high prediction scores across mechanistically unrelated diseases are a strong signal of a knowledge graph artifact — LSD ontology clustering — rather than genuine repurposing potential.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001**: Download and parse the Brineura® SmPC (TFDA or EMA) to complete safety pre-screening
- **Resolve Data Gap DG002**: Retrieve full MOA documentation from DrugBank (DB13173) to formally document TPP1 enzyme class and substrate specificity
- **KG artifact investigation**: Review TxGNN knowledge graph to determine whether "lysosomal storage disease" as a disease category node is causing systematic false-positive enzyme replacement therapy predictions — individual enzyme-substrate relationships (IDUA, GBA, GAA, LAL, TPP1) should be encoded as distinct nodes
- **No additional clinical evidence collection** is recommended for these 10 indications until the KG artifact question is resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

