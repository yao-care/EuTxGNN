---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Memantine
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

# Memantine: From Alzheimer's Disease to Migraine Disorder

## One-Sentence Summary

Memantine is an NMDA receptor antagonist originally developed for moderate-to-severe Alzheimer's disease. The TxGNN model's top-ranked prediction was pulmonary hypertension, but that signal is unsupported by any real-world evidence. The second-ranked prediction — **Migraine Disorder** — carries a near-identical TxGNN score and is backed by **2 clinical trials** and **20 publications**, including a completed Phase 3 RCT, a meta-analysis, and a systematic review, making it the far more actionable candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (moderate to severe) — based on established drug knowledge; not present in this evidence pack (no EU/TW licenses on file) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.52% (rank 5,318 of all predictions) |
| Evidence Level | L1 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** TxGNN's rank-1 prediction, pulmonary hypertension (score 99.54%), has no clinical trials and only tangential literature (one mechanistic paper on glutamate/NMDA signaling in metabolism, and one PK study of a different nitrate-derivative compound, MN-08, whose relevance to memantine itself is questionable). Migraine — rank 2 by a statistically negligible score difference — has substantially stronger, direct clinical evidence and is therefore the focus of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on established pharmacological knowledge, memantine is a non-competitive NMDA receptor antagonist, originally approved for moderate-to-severe Alzheimer's disease, where it works by reducing glutamate-mediated excitotoxicity in the CNS.

This same mechanism is directly relevant to migraine pathophysiology. Glutamatergic overactivity and NMDA receptor signaling are implicated in cortical spreading depression and central sensitization — two core processes in migraine generation. Multiple independent reviews (e.g., Hoffmann & Charles 2018; Podkowa et al. 2023) identify glutamate signaling as a validated therapeutic target for migraine, providing a coherent mechanistic bridge between memantine's known pharmacology and this new indication.

Clinically, this rationale has already been tested: case series and open-label studies date back to 2007–2009, a placebo-controlled RCT was published in 2016, and by 2021 two independent groups (a systematic review and a meta-analysis of RCTs) had synthesized the accumulated evidence. A completed Phase 3 RCT (NCT04698525) directly compared memantine to sodium valproate — an established first-line migraine prophylactic — for episodic migraine prevention. Together, this constitutes a plausible, mechanistically grounded, and clinically tested repurposing hypothesis, though the underlying trials remain small.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Head-to-head comparison of memantine vs. sodium valproate for prophylactic treatment of episodic migraine; direct efficacy comparison against an established Level A prophylactic agent, though limited by small sample size. |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by invitation | 3,300 | Broad EMR-based pragmatic registry across 10 common neurological disorders at NorthShore University HealthSystem; not designed specifically to evaluate memantine for migraine (low relevance). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-Analysis of RCTs | Clinical Neuropharmacology | Pooled analysis of randomized controlled studies evaluating memantine's efficacy in migraine; synthesizes prior RCT evidence base. |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic Review | Headache | Systematic assessment of efficacy and safety of memantine for prophylactic treatment of episodic migraine. |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network Meta-Analysis | Frontiers in Pharmacology | Compares oral preventive migraine medications, including memantine, across efficacy and safety in adults 18–65. |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (Double-Blind, Placebo-Controlled) | Headache | Randomized controlled trial testing memantine for prophylaxis of migraine without aura, building on earlier uncontrolled findings. |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective Study | Journal of Headache and Pain | Retrospective characterization of memantine's efficacy as preventive therapy in patients with frequent migraine. |
| [19031499](https://pubmed.ncbi.nlm.nih.gov/19031499/) | 2008 | Open-label Study | Headache | Assessed efficacy and tolerability of memantine in preventive treatment of refractory migraine. |
| [19280698](https://pubmed.ncbi.nlm.nih.gov/19280698/) | 2009 | Open-label/Pilot Study | Headache | Early pilot evidence for memantine in preventive treatment of migraine and refractory migraine. |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedeberg's Archives of Pharmacology | Reviews NMDA receptor antagonists memantine and ketamine as anti-migraine agents, summarizing published trial evidence. |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | Reviews glutamate and its receptors, including NMDA, as therapeutic targets for migraine, supporting the mechanistic rationale. |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary/Opinion | Headache | "Memantine for migraine—Big promise but little evidence" — cautionary expert commentary highlighting the gap between mechanistic promise and confirmatory trial data. |

---

## EU Market Information

No EU marketing authorizations are currently on record for memantine in this dataset (market status: **Not Marketed**, 0 licenses).

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this evidence pack — DG001, Blocking severity — and must be sourced from the official TFDA/EMA label before any clinical decision.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and consistently reinforced across nearly two decades of literature, culminating in a completed Phase 3 RCT, a systematic review, and a meta-analysis (L1 evidence). However, the largest controlled trial enrolled only 33 patients, and a 2021 expert commentary explicitly cautions that "promise" outpaces "evidence" — so this is not yet a Go, but the evidence base is too substantial to Hold.

**To proceed, the following is needed:**
- TFDA/EMA label data (key warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A larger, adequately powered confirmatory Phase 3 RCT for episodic/chronic migraine prophylaxis
- Regulatory pathway assessment, since memantine currently holds no marketing authorization in this jurisdiction
- Re-evaluation of the pulmonary hypertension signal (rank 1) once independent, drug-specific (not MN-08 analog) evidence becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

