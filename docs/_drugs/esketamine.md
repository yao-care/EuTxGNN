---
layout: default
title: Esketamine
parent: Medium Evidence (L3-L4)
nav_order: 234
evidence_level: L4
indication_count: 10
---

# Esketamine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Esketamine: From Treatment-Resistant Depression to Agoraphobia

## One-Sentence Summary

Esketamine is the S-enantiomer of ketamine, marketed internationally (as Spravato) for treatment-resistant depression (TRD). The TxGNN model's top-ranked prediction for this compound is **Agoraphobia**, but this specific direction is currently supported by **0 clinical trials** and only **1 indirect literature reference**, placing it at the lowest tier of evidence maturity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment-resistant depression (per literature record; no formal local license on file) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information present elsewhere in the evidence collected, Esketamine is the active ingredient of the nasal spray Spravato, an NMDA-receptor antagonist that modulates glutamatergic neurotransmission and produces rapid-acting antidepressant effects; it has established efficacy in treatment-resistant depression and is approved for that use in the US and EU.

Treatment-resistant depression and agoraphobia both fall within the broader mood/anxiety-disorder spectrum, and glutamatergic (NMDA) signaling has been implicated in fear-extinction and panic-circuit neurobiology in general anxiety research. This provides a plausible, though unproven, mechanistic bridge.

However, the only supporting literature retrieved is a general review of anxiety-disorder pharmacotherapy (panic disorder, GAD, social anxiety disorder) that does not specifically address agoraphobia or provide esketamine-specific efficacy data. No clinical trials in agoraphobia patients have been identified. The prediction should therefore be treated as a knowledge-graph-driven hypothesis rather than an evidence-backed clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33424664](https://pubmed.ncbi.nlm.nih.gov/33424664/) | 2020 | Review | Frontiers in Psychiatry | General review of current and emerging pharmacotherapy for anxiety disorders (panic disorder, GAD, social anxiety disorder); does not focus specifically on agoraphobia and provides no esketamine-specific clinical data |

---

## EU Market Information

Esketamine is currently **not marketed** in this jurisdiction (0 marketing authorizations on record).

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps or not found in this evidence pack; TFDA label/warning retrieval is a Blocking-severity gap, DG001, required before any safety screening can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-ranked prediction (Agoraphobia) has no supporting clinical trials and only one indirect, non-specific literature review (L4 — mechanism/preclinical-tier evidence). Combined with the absence of local marketing authorization and two outstanding data gaps (TFDA label/warnings — Blocking; MOA — High), there is insufficient evidence to advance this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- Retrieve TFDA/SmPC label warnings and contraindications (DG001, blocking S1 safety screening)
- Confirm mechanism of action via DrugBank API (DG002)
- Identify or initiate clinical trials specifically evaluating esketamine in agoraphobia
- Obtain agoraphobia-specific literature beyond general anxiety-disorder reviews
- Drug-drug interaction (DDI) data, currently not found in queried sources

*Note: This candidate's evidence pack also contains other predicted indications (e.g., neurotic depression, rank 3) with substantially stronger clinical trial and literature support (L1, "Proceed with Guardrails") largely reflecting esketamine's already-approved TRD indication under a legacy diagnostic label — these may warrant separate review outside the scope of this agoraphobia-focused report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

