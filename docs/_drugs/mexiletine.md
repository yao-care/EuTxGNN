---
layout: default
title: Mexiletine
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Mexiletine
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

# Mexiletine: From Ventricular Arrhythmia to Headache Disorder

## One-Sentence Summary

Mexiletine is a Class IB sodium-channel blocker with an established history as an oral antiarrhythmic and as an off-label agent for neuropathic pain and myotonia. Among the ten TxGNN-predicted indications in this evidence pack, **Headache Disorder** is the one with actual, drug-specific supporting literature — **0 clinical trials but 7 publications** (including several case series naming mexiletine directly), whereas the model's top-ranked candidates (e.g., hypertrichosis, nephrogenic SIAD) have no supporting evidence at all and are flagged internally as likely noise.

> **Note on indication selection:** TxGNN's #1-ranked prediction by raw score is "hypertrichosis," which has zero clinical trials, zero literature, and an explicit rationale stating no known mechanistic link. This report instead profiles **Headache Disorder** (TxGNN rank 10, score 99.48%), the candidate with the strongest actual evidence base and the highest internal decision stage (S2) in the pack, consistent with standard practice of prioritizing evidence over raw model score alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally recorded in regulatory data (drug not marketed in this region). Literature in this pack confirms established use as an oral Class IB antiarrhythmic for ventricular arrhythmia, with off-label use in neuropathic pain and myotonia |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L3 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in our database for mexiletine (data gap). Based on the literature retrieved in this evidence pack, mexiletine is described as "a Class 1B antiarrhythmic drug that acts on sodium channels," and is already used clinically for neuropathic pain and myotonia — both conditions involving abnormal neuronal/muscular excitability driven by sodium channel dysfunction.

Headache disorders — particularly trigeminal autonomic cephalalgias such as SUNCT/SUNA and refractory chronic daily headache — are increasingly understood to involve abnormal, sodium-channel-dependent firing within the trigeminal-vascular system. Intravenous **lidocaine**, a close pharmacological relative of mexiletine (both Class IB agents), is an established treatment for these conditions, and this evidence pack directly links the two: one publication (PMID 20425204) explicitly reviews "intravenous lidocaine and mexiletine in the management of trigeminal autonomic cephalalgias."

This creates a plausible mechanistic bridge — sodium channel blockade suppressing pathological neuronal firing — from mexiletine's established antiarrhythmic/neuropathic pain use to headache disorders. The evidence, however, consists entirely of small case series and one open-label prospective study spanning 1981–2021, with no randomized controlled trials, which limits certainty despite the biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------------|
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective Open-label + Meta-analysis | J Neurol Neurosurg Psychiatry | Prospective study of medical treatments (including sodium channel blockers) for SUNCT/SUNA, a trigeminal autonomic headache subtype; single-arm meta-analysis of treatment efficacy |
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Case Series/Observational | Curr Pain Headache Rep | Reviews IV lidocaine and mexiletine (both Class 1B sodium channel blockers) for trigeminal autonomic cephalalgias; notes mexiletine's established use in neuropathic pain and myotonia supports a role in headache syndromes |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case Series (n=9) | Headache | Nine patients with refractory chronic daily headache treated with mexiletine |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Case Series | N Z Med J | Early report describing mexiletine use for vascular headaches |
| [40197813](https://pubmed.ncbi.nlm.nih.gov/40197813/) | 2025 | Cochrane Review | Cochrane Database Syst Rev | Review of drug treatments for myotonia (sodium channelopathy); background mechanistic evidence for mexiletine's channel-blocking activity, not headache-specific |
| [24820732](https://pubmed.ncbi.nlm.nih.gov/24820732/) | 2014 | Review | Curr Pain Headache Rep | General review of new daily persistent headache; no mexiletine-specific data, included as disease background |
| [91699](https://pubmed.ncbi.nlm.nih.gov/91699/) | 1979 | Clinical Study | Kardiologiia | Original antiarrhythmic efficacy study of mexiletine (Mexityl) in ventricular arrhythmia; unrelated to headache, included as background pharmacology only |

---

## EU Market Information

Mexiletine currently has **no marketing authorization on record** in this region (0 authorizations; market status: Not Marketed). No product/dosage-form information is available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: This candidate has a blocking internal data gap — label warnings and contraindications for mexiletine could not be sourced, which prevents formal safety pre-screening (S1) for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While mexiletine's sodium-channel mechanism plausibly links to headache disorders — and is supported by a multi-decade, mexiletine-specific case series literature (1981–2021) plus one prospective open-label study — the evidence remains Level L3 (no RCTs, no clinical trials registered), and a **blocking data gap on safety warnings/contraindications** means the candidate cannot yet complete initial safety screening.

**To proceed, the following is needed:**
- Source mexiletine's label warnings and contraindications (e.g., via DrugBank or an SmPC from a market where it is authorized) to clear the blocking safety data gap
- Obtain formal mechanism of action (MOA) documentation to strengthen the mechanistic rationale
- Design a small controlled/pilot trial in refractory headache disorder (e.g., trigeminal autonomic cephalalgia) to validate the existing case-series signal, given QT-prolongation and cardiac risk considerations typical of Class IB antiarrhythmics
- Clarify regulatory pathway, since mexiletine currently holds no marketing authorization in this region
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

