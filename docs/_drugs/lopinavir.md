---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Lopinavir
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

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Lopinavir (co-formulated with ritonavir as Lopinavir/Ritonavir, brand name Kaletra) is an HIV-1 protease inhibitor originally used for HIV-1 infection.
> The TxGNN model's top-ranked prediction suggests it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
> but this is currently supported by **0 clinical trials** and only **3 publications** (all animal-model studies), placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection (established antiretroviral use, as part of Lopinavir/Ritonavir combination therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this evidence pack. Based on well-established pharmacology, Lopinavir is a HIV-1 protease inhibitor, boosted by ritonavir (Lopinavir/Ritonavir, Kaletra), and its efficacy in HIV-1 infection has been extensively proven in clinical practice.

The predicted new indication, SIV infection, is a lentivirus disease affecting non-human primates. SIV protease shares high structural homology with HIV-1 protease, which is why SIV-infected macaque models have long served as a preclinical platform to test antiretroviral regimens intended for human HIV-1 treatment.

However, this prediction is essentially a veterinary/animal-model application rather than a genuine human clinical indication. The high TxGNN score (99.90%) likely reflects tight embedding-space proximity between "SIV" and "HIV" nodes in the knowledge graph, rather than an unmet human therapeutic need. It should be read as a technical extension of the existing HIV-1 indication, not a novel repurposing opportunity for human patients.

**Note:** Within the same evidence pack, two other predicted indications — *congenital human immunodeficiency virus* (rank 4) and *AIDS related complex* (rank 5) — carry **L1 evidence** (multiple completed Phase 3 RCTs, "Proceed with Guardrails"). These are stronger, clinically meaningful signals but represent extensions of the already-approved HIV-1 indication rather than the model's top-ranked (rank 1) prediction reported above.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal Study (Macaque) | Journal of Virology | Quadruple antiretroviral therapy produced rapid viral decay in SIV-infected cynomolgus macaques |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal Study (SHIV construct) | Microbes and Infection | Novel SHIV bearing an HIV-1-derived protease gene, used as an in vivo platform for testing protease inhibitors |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal Study (Macaque) | Journal of Virological Methods | Oral HAART including Lopinavir/Ritonavir affected CD8 subset in SHIV-infected monkeys |

---

## EU Market Information

Lopinavir currently holds no EU marketing authorizations on record (market status: **not marketed**, 0 licenses).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA/EMA label warnings and contraindications are flagged as a Blocking data gap — DG001 — pending SmPC PDF retrieval and parsing.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) has no clinical trial support and is backed only by three Tier-3 animal-model publications. It represents a veterinary/preclinical model condition rather than a human therapeutic need, and the high TxGNN score is best explained by knowledge-graph node proximity (SIV↔HIV) rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Confirm this candidate should not advance as a human indication; redirect evaluation focus to the higher-evidence candidates in this same evidence pack (congenital HIV infection and AIDS related complex, both L1 / Proceed with Guardrails)
- Resolve DG001 (TFDA/EMA label warnings and contraindications — Blocking)
- Resolve DG002 (detailed mechanism of action from DrugBank)
- Verify EU marketing authorization status, since current data shows 0 licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

