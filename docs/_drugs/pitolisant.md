---
layout: default
title: Pitolisant
parent: Medium Evidence (L3-L4)
nav_order: 489
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Pitolisant: predicted new indication Insomnia (evidence level L4). Approved use: Improving wakefulness and reducing excessive daytime sleepiness (EDS)…"
---

# Pitolisant
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

# Pitolisant: From Obstructive Sleep Apnoea Sleepiness to Insomnia

## One-Sentence Summary

Pitolisant is a wake-promoting drug, originally authorised in the EU for excessive daytime sleepiness in obstructive sleep apnoea (Ozawade) and for narcolepsy (Wakix).
The TxGNN model predicts it may be effective for **insomnia**, but there are **no registered clinical trials** and **none of the 10 publications retrieved** studies pitolisant as an insomnia treatment.
This prediction is most likely a model artefact, and the mechanism points the opposite way.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Improving wakefulness and reducing excessive daytime sleepiness (EDS) in adults with obstructive sleep apnoea (OSA) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| EU Market Status | ✗ Cancelled only (all authorisations cancelled) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pitolisant is a selective histamine H3 receptor antagonist/inverse agonist. It increases histamine release in the brain and promotes wakefulness. The data compiled for this report contain no formal mechanism-of-action entry, but the retrieved literature consistently describes this mechanism. Its efficacy in narcolepsy and in OSA-related sleepiness has been shown in randomised trials.

The prediction looks weak. Insomnia is a disorder of too little sleep, so treating it requires *reducing* arousal. Pitolisant does the opposite, and insomnia is a recognised adverse effect of the drug. The high TxGNN score is probably driven by how close the sleep-wake disorders sit to each other in the knowledge graph, not by a therapeutic direction. The retrieved papers concern narcolepsy and OSA, which are wakefulness-promoting indications. The only insomnia-related mention is in a review of the histaminergic system, which discusses doxepin (an H1 antagonist) for insomnia, a different mechanism.

By comparison, another prediction for this drug, **hypersomnia**, has far stronger support. It has a completed Phase 3 randomised-withdrawal study in idiopathic hypersomnia (NCT05156047, n=214) and a completed Phase 3 long-term open-label study (NCT05458128, n=119). This is a more credible repurposing direction than insomnia and merits separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications evaluates pitolisant for insomnia. They are listed as the closest available context (narcolepsy, OSA and histaminergic mechanism).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Pitolisant for residual excessive daytime sleepiness in OSA patients adhering to CPAP |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Pitolisant for daytime sleepiness in OSA patients who refuse CPAP |
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | Phase 3 double-blind placebo-controlled trial | Lancet Neurol | Safety and efficacy of pitolisant in children aged 6 years or older with narcolepsy |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Curr Neuropharmacol | Histaminergic changes in neuropsychiatric disorders; pitolisant for narcolepsy sleepiness, doxepin for insomnia |
| [42525367](https://pubmed.ncbi.nlm.nih.gov/42525367/) | 2026 | Review | Neurol Ther | Current and emerging therapies for paediatric sleep disorders |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Profile of pitolisant in narcolepsy: design, development and place in therapy |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handb Clin Neurol | Histamine receptors, agonists and antagonists in health and disease |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Clinical report | Clin Neuropharmacol | Pitolisant as an alternative stimulant in teenagers with refractory narcolepsy-cataplexy |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Rev Neurol | Real-life WAKE study of pitolisant in narcolepsy with cataplexy unresponsive to previous treatments |
| [41588264](https://pubmed.ncbi.nlm.nih.gov/41588264/) | 2026 | Cohort | Neurol Sci | Real-world study of pitolisant in Chinese paediatric narcolepsy (n=40) |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005117 | Ozawade | Not specified | Improve wakefulness and reduce excessive daytime sleepiness (EDS) in adult patients with obstructive sleep apnoea (OSA) |
| EMEA/H/C/002616 | Wakix | Not specified | Treatment of narcolepsy with or without cataplexy in adults, adolescents and children from 6 years of age... |

Both authorisations are currently recorded as cancelled.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded in the interaction databases, mostly of moderate severity. The two **major** interactions listed are:
  - Bupropion
  - Dolasetron

  Moderate interactions include famotidine, hydrocortisone, metformin, loperamide, morphine, acetylsalicylic acid, clarithromycin, dexamethasone and empagliflozin, among others.
- **Adverse effect relevant to this prediction**: insomnia is a recognised adverse effect of pitolisant, which argues against its use for this indication.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The H3 inverse agonist mechanism promotes wakefulness, which runs counter to insomnia treatment, and insomnia is a known adverse effect of pitolisant. There are no trials and no literature on pitolisant for insomnia, and the high score is likely a knowledge-graph artefact. All EU authorisations are also currently cancelled.

**To proceed, the following is needed:**
- Mechanistic reassessment that justifies a therapeutic direction for insomnia, or removal of this prediction as a false positive
- Formal mechanism-of-action data (MOA)
- The SmPC warnings and contraindications, which are missing from the compiled data
- Redirecting evaluation to the hypersomnia prediction, including:
  - Confirmation of the populations and indications of NCT05156047 and NCT05458128
  - Confirmation of regulatory and formulation status, given the "cancelled only" EU market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

