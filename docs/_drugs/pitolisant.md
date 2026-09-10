---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Pitolisant
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

# Pitolisant: From Narcolepsy to Insomnia

## One-Sentence Summary

> Pitolisant is a selective histamine H3 receptor antagonist/inverse agonist, developed and used clinically for narcolepsy with excessive daytime sleepiness.
> The TxGNN model's top-ranked prediction suggests possible efficacy for **Insomnia**,
> but this is currently supported by only **1 clinical trial (withdrawn before enrollment)** and **8 publications**, none of which directly test pitolisant in insomnia — and the drug's known pharmacology points in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy with/without cataplexy (per literature evidence; not captured as a formal license record in this dataset — see Data Gap DG001) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| EU Market Status | Not Marketed (0 authorizations on record in this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (Data Gap DG002). Based on the assembled literature, pitolisant is a selective histamine H3 receptor antagonist/inverse agonist. By blocking presynaptic H3 autoreceptors, it increases release of histamine and other monoamines in the brain, producing a **wake-promoting** effect. This is the basis of its established use in narcolepsy and, per the clinical trial evidence below, in excessive daytime sleepiness associated with idiopathic hypersomnia and obstructive sleep apnea (OSA).

Narcolepsy and insomnia are both classified as sleep disorders, and TxGNN's knowledge graph likely places them close together as neighboring "sleep disorder" nodes — which is probably what drove the high similarity score. However, the two conditions are pharmacologically opposite: narcolepsy is characterized by *excessive* sleepiness requiring a stimulant-like agent, whereas insomnia is characterized by *difficulty initiating or maintaining* sleep, which typically requires a sedating or sleep-promoting agent.

Mechanistically, applying a wake-promoting H3 inverse agonist to insomnia is not well supported. Reduced sleep duration and insomnia-type symptoms are, in fact, listed among pitolisant's known adverse effects in narcolepsy trials, rather than a therapeutic target. The evidence review for this candidate explicitly flags the prediction as a likely artifact of embedding proximity between sleep-disorder nodes rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Designed to evaluate pitolisant for Alcohol Use Disorder (primary endpoint: heavy drinking days), not insomnia specifically. Withdrawn before any participant was enrolled — no usable data generated. |

---

## Literature Evidence

*Note: none of the publications below directly study pitolisant for insomnia. They cover pitolisant's established use in narcolepsy/OSA and general H3-receptor pharmacology.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | Lancet Neurology | Phase 3 double-blind RCT of pitolisant in pediatric narcolepsy with/without cataplexy — safety and efficacy for excessive daytime sleepiness, not insomnia. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Randomized trial of pitolisant for residual excessive daytime sleepiness in OSA patients adherent to CPAP. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Randomized trial of pitolisant for daytime sleepiness in OSA patients refusing CPAP. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Real-world study | Revista de neurología | "WAKE" real-life study: pitolisant effectiveness/safety in type 1 narcolepsy patients unresponsive to prior treatments. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Overview of pitolisant's development and place in narcolepsy therapy. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | Overview of histamine receptors (H1–H4), including CNS roles of H3. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Histaminergic system changes in neuropsychiatric disorders; notes pitolisant's role is for excessive sleepiness, contrasted with H1-antagonist doxepin used for insomnia. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review (mechanism) | Clinical Neuropharmacology | Describes pitolisant as an H3 inverse agonist and stimulant alternative for narcolepsy-cataplexy in adolescents. |

---

## EU Market Information

No EU marketing authorization records are present in this dataset (0 of 0 licenses; see Data Gap DG001). Literature evidence (e.g. PMID 28087755, 30214155) indicates pitolisant (Wakix) has been marketed in Europe for narcolepsy since 2016, but this is not reflected in the structured regulatory data available for this report.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial linked to this candidate was withdrawn before enrollment, and no literature directly evaluates pitolisant for insomnia. More importantly, pitolisant's wake-promoting mechanism runs counter to the therapeutic goal of insomnia treatment, and insomnia-type symptoms are a known adverse effect rather than a treatment target — this prediction is most likely a knowledge-graph artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- A validated mechanistic or clinical rationale explaining how an H3 inverse agonist could be therapeutic in insomnia (none currently identified)
- Formal MOA and TFDA/EMA warning and contraindication data (Data Gaps DG001, DG002)
- If pursued at all, a dedicated preclinical or early Phase 2 study directly testing pitolisant in an insomnia population

**Note:** within this same evidence batch, *idiopathic hypersomnia* (rank 9, L1 evidence, decision stage S3, "Proceed with Guardrails") is a substantially stronger candidate — supported by three completed Phase 3 trials (NCT05156047, NCT05458128, NCT02800083-adjacent NCT01638403) — and warrants a separate evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

