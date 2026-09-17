---
layout: default
title: Selpercatinib
parent: AI Predictions (L5)
nav_order: 534
evidence_level: L5
indication_count: 10
---

# Selpercatinib
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

# Selpercatinib: From RET-Altered Cancer to Pulmonary Hypertension

## One-Sentence Summary

Selpercatinib is a highly selective RET kinase inhibitor whose established use, per the cited literature, is in RET fusion-positive non-small-cell lung cancer (formal EU regulatory indication text is not available in this evidence pack). The TxGNN model's top prediction is **Pulmonary Hypertension** (score 99.18%), but this candidate is currently supported only by an AI knowledge-graph score — the two associated publications discuss selpercatinib's real-world oncology safety profile, not pulmonary hypertension, and are flagged in the evidence pack itself as likely graph noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | RET fusion-positive NSCLC (inferred from literature; no formal EU indication text on file — drug not yet authorized) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, Selpercatinib is described as a highly selective RET kinase inhibitor, and its use in RET fusion-positive/mutated cancers (NSCLC and related RET-driven tumours) is supported by the real-world literature cited here.

There is no established mechanistic link between RET kinase signaling and pulmonary vascular remodeling — the pathophysiology of pulmonary hypertension is more commonly associated with BMPR2/TGF-β signaling. The evidence pack's own rationale explicitly characterizes this prediction as likely knowledge-graph co-occurrence noise rather than a genuine drug–disease relationship: the two cited papers concern selpercatinib's adverse-event profile in oncology patients (PMID 39372206) and its real-world efficacy in RET fusion-positive NSCLC (PMID 34178121) — neither addresses pulmonary hypertension as a treatment target. The same pattern (score-driven ranking with no supporting mechanism or clinical data) is seen across all ten TxGNN-ranked candidates in this pack, several of which are rare/obsolete disease entries with no plausible RET connection.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world safety cohort | Frontiers in Pharmacology | Compared adverse event profiles of pralsetinib vs. selpercatinib using FDA FAERS data; addresses oncology-setting safety, not pulmonary hypertension. |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective cohort (SIREN) | Therapeutic Advances in Medical Oncology | Real-world efficacy/safety of selpercatinib in RET fusion-positive NSCLC treated through an access program; does not evaluate pulmonary hypertension. |

Neither publication provides direct or indirect support for a pulmonary hypertension indication; both concern selpercatinib's established oncology use.

## Cytotoxicity

Selpercatinib is a targeted oncology agent (RET fusion-positive NSCLC per literature), so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-ranked candidates for selpercatinib, including the top-ranked pulmonary hypertension prediction, are Evidence Level L5 — model-score-only with no supporting clinical trials, and the associated literature is explicitly identified in the evidence pack as knowledge-graph noise rather than genuine mechanistic or clinical support. Two blocking/high-severity data gaps (missing TFDA/EU safety labeling and missing MOA data) also prevent even a preliminary safety review (S1).

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (DG002)
- Official safety labeling (warnings, contraindications, DDI) from a regulatory source (DG001)
- Independent mechanistic or preclinical evidence linking RET signaling to pulmonary vascular remodeling before any further investment in this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

