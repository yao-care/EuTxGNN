---
layout: default
title: Natalizumab
parent: AI Predictions (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Natalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

> Natalizumab (marketed elsewhere as Tysabri) is a monoclonal antibody used to treat relapsing-remitting multiple sclerosis by blocking VLA-4-mediated leukocyte migration across the blood-brain barrier.
> The TxGNN model's top prediction proposes **Bronchitis** as a new indication with a **99.46%** score,
> but this is a pure AI-generated prediction — **0 clinical trials** and **0 publications** currently support it, and no plausible mechanistic link to bronchitis exists.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no TFDA/EMA license records provided). Natalizumab's globally recognized indication — referenced throughout the literature evidence in this pack (e.g., AFFIRM trial, RRMS therapy) — is relapsing-remitting multiple sclerosis. |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

> Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information, Natalizumab is a monoclonal antibody that blocks VLA-4–mediated leukocyte adhesion and migration, and it is established for use in multiple sclerosis. Mechanistically, there is no known connection between this pathway and bronchitis, which is typically driven by infectious or irritant-triggered airway inflammation.

This candidate is not supported by clinical or literature evidence — it is a model-score-only ("S0 / L5") prediction. Notably, this pattern extends across nearly all of the top 10 TxGNN candidates for this drug: several (bronchitis, severe nonproliferative diabetic retinopathy, penile fibromatosis, neonatal dermatomyositis) have **zero** clinical trial or literature support of any kind. Where literature does exist for other ranked candidates (psoriasis, dermatitis, parapsoriasis, pityriasis lichenoides, pustulosis palmaris et plantaris), it consistently describes natalizumab **inducing or exacerbating** these skin conditions as adverse drug reactions — not treating them. This suggests the underlying knowledge-graph signal may be picking up drug-induced disease associations rather than genuine therapeutic potential, which is an important caveat for interpreting this candidate set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Natalizumab has no EU/EMA or Taiwan marketing authorizations recorded in this evidence pack (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, drug interactions) are not available in this evidence pack — this is flagged as a **Blocking** data gap (DG001: TFDA label/warnings not yet retrieved), which prevents this candidate from advancing past the S1 safety screening stage.

That said, the literature evidence collected for adjacent candidates in this pack repeatedly and independently documents natalizumab's association with **progressive multifocal leukoencephalopathy (PML)** — a rare but often fatal CNS infection caused by JC virus reactivation (e.g., PMID 20298966, 19647202, 24136456, 30324046, 20925435, 36283150, 20073129, 22082208, 36283150). This is a well-established, serious safety signal for natalizumab and must be factored into any repurposing risk-benefit assessment, regardless of target indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the top 10 TxGNN-predicted indications for natalizumab have credible supporting evidence. Most candidates, including the top-ranked bronchitis, have no clinical trials or literature at all. Where literature exists for other candidates, it exclusively describes drug-induced adverse skin reactions rather than therapeutic efficacy, and a blocking data gap prevents even a baseline safety review.

**To proceed, the following is needed:**
- TFDA/EMA official label (SmPC) with warnings, contraindications, and PML risk-management information (resolves DG001)
- Confirmed mechanism of action data from DrugBank (resolves DG002)
- Any prospective or mechanistic studies directly testing natalizumab in a respiratory indication, as opposed to adverse-event case reports
- Re-evaluation of this candidate set's ranking methodology, since several top-scored predictions appear to reflect known side-effect signals rather than therapeutic signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

