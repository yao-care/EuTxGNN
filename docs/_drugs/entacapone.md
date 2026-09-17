---
layout: default
title: Entacapone
parent: Medium Evidence (L3-L4)
nav_order: 221
evidence_level: L4
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to Lewy Body Dementia

**Note on candidate selection:** Among the 10 TxGNN-ranked candidates in this evidence pack, ranks 1–6, 8, and 9 (highest raw prediction scores, e.g. *PLA2G6-associated neurodegeneration*, *Rasmussen subacute encephalitis*, *transaldolase deficiency*) have **zero supporting trials or literature**, and their own rationale text flags them as likely knowledge-graph clustering artifacts rather than genuine signals. This report instead focuses on **Lewy Body Dementia (rank 7)**, the highest-ranked candidate that is actually backed by real clinical trial and literature evidence.

## One-Sentence Summary

Entacapone is a peripheral COMT inhibitor used as adjunctive therapy with levodopa in Parkinson's disease.
The TxGNN model's evidence-supported candidate points to **Lewy Body Dementia**,
with **1 clinical trial** and **3 publications** providing indirect, mechanism-level support — no direct interventional trial of entacapone in LBD currently exists.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunctive COMT-inhibitor therapy)* |
| Predicted New Indication | Lewy Body Dementia |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L4 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*\*Not present in the regulatory data pack (original_indications is empty); stated based on entacapone's established pharmacological class.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on established pharmacology, entacapone is a peripheral catechol-O-methyltransferase (COMT) inhibitor co-administered with levodopa/DDCI regimens; by blocking peripheral levodopa breakdown it increases CNS levodopa bioavailability and prolongs its motor benefit in Parkinson's disease.

Lewy Body Dementia (LBD) and Parkinson's disease belong to the same synucleinopathy spectrum — both feature α-synuclein aggregation and progressive dopaminergic neuron loss, and LBD patients frequently develop parkinsonian motor symptoms that are managed with levodopa. This shared pathology and shared symptomatic treatment approach is the biological basis for the TxGNN link.

However, the existing evidence is indirect: the one registered trial studies dopaminergic imaging in autonomic-failure patients rather than entacapone's therapeutic effect in LBD, and the literature covers α-synuclein pathology mechanisms and general antiparkinsonian pharmacology rather than entacapone-specific outcomes in LBD. The mechanistic rationale is sound, but it remains a research hypothesis, not a demonstrated treatment effect.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA dopaminergic imaging study in patients with autonomic failure / α-synucleinopathies (including DLB); evaluates dopamine system function, not entacapone treatment efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Review | Science Advances | iPSC-derived cortical organoid model of SNCA-triplication Lewy body disease used to identify candidate therapeutic drugs targeting α-synuclein pathology. |
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | Cohort | J Neurosci Res | In vitro study of antiparkinsonian agents (including levodopa-related therapy) on β-amyloid and α-synuclein oligomer formation, relevant to both AD and LBD pathology. |
| [11268898](https://pubmed.ncbi.nlm.nih.gov/11268898/) | 2001 | Review | Presse Médicale | General review of Parkinson's disease (abstract not available). |

## EU Market Information

No marketing authorizations are recorded for entacapone in the current evidence pack (market status: not marketed, 0 authorizations).

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-interaction data are marked as data gaps in this pack — notably DG001, a **Blocking**-severity gap on TFDA label warnings/contraindications that must be resolved before any S1 safety review can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between entacapone and Lewy Body Dementia is biologically plausible (shared synucleinopathy and dopaminergic pathway), but current evidence is entirely indirect — no interventional trial has tested entacapone specifically in LBD, and the one registered trial is an imaging study, not a treatment trial.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) — currently blocking any safety evaluation
- Confirmed mechanism of action data (DG002)
- A proof-of-concept interventional trial or observational cohort evaluating entacapone specifically in LBD patients with parkinsonism
- EU/local marketing authorization and regulatory status confirmation, since entacapone is currently unmarketed in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

