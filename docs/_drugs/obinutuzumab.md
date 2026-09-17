---
layout: default
title: Obinutuzumab
parent: AI Predictions (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Obinutuzumab
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

# Obinutuzumab: From Chronic Lymphocytic Leukemia to Pregerminal Center CLL/SLL (Molecular Subtype)

## One-Sentence Summary

> Obinutuzumab is a glycoengineered, type II anti-CD20 monoclonal antibody already established in the treatment of chronic lymphocytic leukemia (CLL) and follicular lymphoma.
> The TxGNN model's top-ranked prediction, **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma**, is a molecular subgroup of CLL/SLL rather than an independent disease entity,
> and currently has **0 clinical trials** and **0 publications** specifically indexed against it — the model score of 99.21% likely reflects the drug's already-proven efficacy in CLL as a whole, not a genuinely new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via EMA licensing data (0 authorizations on record); contextual evidence in this pack references obinutuzumab's established use in chronic lymphocytic leukemia (CLL11 trial) |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L1 (pipeline-assigned; see caveat below — driven by existing CLL approval, not by direct trials/literature for this specific molecular subtype) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is not available in this evidence pack. Based on information embedded in the repurposing rationale, obinutuzumab is a third-generation, glycoengineered, type II anti-CD20 monoclonal antibody. Its mechanism combines enhanced direct B-cell killing with increased antibody-dependent cellular cytotoxicity (ADCC) and antibody-dependent cellular phagocytosis (ADCP) compared with first-generation anti-CD20 agents such as rituximab. It has been approved based on pivotal trials including CLL11 (chronic lymphocytic leukemia) and GALLIUM (follicular lymphoma).

"Pregerminal center CLL/SLL" and "CLL/SLL with IGHV somatic hypermutation" are not distinct diseases — they are biological subgroups of CLL/SLL defined by immunoglobulin heavy-chain variable-region (IGHV) mutation status and cell-of-origin. Because obinutuzumab's target, CD20, is expressed on malignant B cells regardless of IGHV mutation status, there is no mechanistic reason to expect differential efficacy between subgroups. This explains the very high TxGNN score: the model is essentially re-discovering an already-approved indication expressed at finer ontological granularity, rather than proposing a genuinely novel therapeutic hypothesis.

This also explains the absence of dedicated trials or literature for this exact label — evidence-collection pipelines typically filter out "known indications" (CLL as a whole) when searching for *new* uses, and the finer-grained subtype label falls into a gap between "already known" and "genuinely novel." As a result, this specific candidate should be treated as a taxonomy artifact rather than an actionable repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EMA marketing authorizations are on record for obinutuzumab in this evidence pack (0 licenses; market status: Not Marketed). This may reflect a genuine absence of EU marketing authorization, or a gap in the data source used to compile this pack — it should be confirmed against the EMA product database before any regulatory conclusion is drawn.

---

## Cytotoxicity (Antineoplastic Drug)

Obinutuzumab is an antineoplastic biologic (anti-CD20 monoclonal antibody used in CLL/lymphoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / immunotherapy — glycoengineered, type II anti-CD20 monoclonal antibody (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Moderate–High — neutropenia, including prolonged/late-onset neutropenia, is a well-documented effect of the anti-CD20 antibody class in CLL/lymphoma trials; please refer to the SmPC for graded incidence data |
| Emetogenicity Classification | Low — minimal direct emetogenic potential; the dominant acute toxicity is infusion-related reaction rather than nausea/vomiting |
| Monitoring Items | CBC with differential (neutropenia, thrombocytopenia), infusion-related reaction monitoring during and after infusion, hepatitis B screening (reactivation risk with B-cell depleting antibodies), serum immunoglobulin levels |
| Handling Protection | Monoclonal antibodies are generally not subject to cytotoxic hazardous-drug handling protocols, but standard biologic infusion precautions, premedication, and infusion-reaction management procedures are required |

Please refer to the SmPC warnings and precautions for full toxicity grading.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate, "pregerminal center CLL/SLL," has zero supporting clinical trials or literature (decision stage S0) and, per the underlying rationale, most likely represents a known-indication subgroup rather than a genuinely new therapeutic use. Pursuing this as a standalone repurposing candidate is not currently justified.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA/EMA label warnings and contraindications) before any safety-stage review can begin
- Resolve high-priority data gap DG002 (formal mechanism-of-action data from DrugBank)
- Clarify whether TxGNN's disease ontology should collapse CLL/SLL molecular subtypes into the parent "CLL/SLL" node to avoid inflating apparent "new indication" counts with known-indication artifacts
- Confirm actual EU/EMA marketing authorization status, since 0 licenses is currently unverified against the primary EMA source

**Note for portfolio prioritization:** among this drug's other predicted indications, **mantle cell lymphoma** (rank 4, evidence level L2, decision stage S2, "Proceed with Guardrails") is a substantially stronger candidate — it is not an approved indication, yet is supported by dozens of trials (including head-to-head studies) and recent high-quality literature (e.g., PMID 38669626, *Blood* 2024). It may warrant its own dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

