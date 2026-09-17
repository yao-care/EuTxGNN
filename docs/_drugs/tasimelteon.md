---
layout: default
title: Tasimelteon
parent: High Evidence (L1-L2)
nav_order: 567
evidence_level: L1
indication_count: 10
---

# Tasimelteon
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Tasimelteon: From Non-24-Hour Sleep-Wake Disorder to Insomnia

## One-Sentence Summary

Tasimelteon is a melatonin MT1/MT2 receptor agonist most widely known for treating Non-24-Hour Sleep-Wake Disorder. Among the ten TxGNN-predicted indications reviewed, the only one supported by real-world evidence is **Insomnia**, backed by **4 clinical trials** (including one completed Phase 3 RCT) and **6 publications**. Because insomnia shares the drug's core circadian-regulation mechanism, this is best understood as a label-extension opportunity rather than a mechanistically novel repurposing candidate; the remaining nine top-ranked predictions (e.g., polymicrogyria, ALS-cluster diseases) have no supporting evidence and are flagged in the source data as likely knowledge-graph noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-24-Hour Sleep-Wake Disorder (drug's known approved use, referenced in the evidence pack's mechanistic rationale; no EU marketing-authorization text is available to confirm this independently) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not provided directly for this drug (flagged as a data gap), but the evidence pack's own rationale confirms tasimelteon is a non-selective **MT1/MT2 melatonin receptor agonist** that acts on the suprachiasmatic nucleus (SCN), the brain's master circadian pacemaker, to promote sleep onset and re-entrain the sleep-wake cycle.

Insomnia and Non-24-Hour Sleep-Wake Disorder are both circadian/sleep-initiation disorders governed by the same MT1/MT2–SCN signaling pathway. The evidence pack explicitly notes that this prediction should be viewed as a **label extension rather than a novel cross-mechanism repurposing**, since tasimelteon's core pharmacology already targets sleep-onset regulation.

This mechanistic continuity is why insomnia — despite not being the numerically highest-scoring TxGNN prediction — is the only candidate among the top 10 with meaningful clinical support. By contrast, rank 1 (bilateral parasagittal parieto-occipital polymicrogyria, a structural/genetic cortical malformation) and the cluster of ALS-related predictions (ranks 3, 6–10) have **no supporting trials or literature** and are explicitly described in the source rationale as likely knowledge-graph adjacency noise, since neither condition has a known pathophysiological link to melatonergic signaling.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00548340](https://clinicaltrials.gov/study/NCT00548340) | Phase 3 | Completed | 322 | Pivotal RCT evaluating tasimelteon (VEC-162) 20 mg and 50 mg/day vs. placebo over a 5-week double-blind period in primary insomnia |
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Recruiting | 420 | Ongoing confirmatory multicenter RCT of daily oral tasimelteon vs. placebo in pediatric insomnia disorder |
| [NCT03291041](https://clinicaltrials.gov/study/NCT03291041) | Phase 2 | Completed | 25 | Proof-of-concept study of tasimelteon vs. placebo in travelers with jet lag disorder (a circadian sleep-disruption phenotype related to insomnia) |
| [NCT05922995](https://clinicaltrials.gov/study/NCT05922995) | Early Phase 1 | Terminated | 20 | Open-label pilot assessing tasimelteon 20 mg on REM Behavior Disorder and co-occurring insomnia symptoms (ISI, PSQI, ESS); stopped early, small sample |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Review | Int J Mol Sci | Reviews efficacy/safety of marketed melatonin receptor agonists (ramelteon, prolonged-release melatonin, agomelatine, tasimelteon) for insomnia, depression, and circadian rhythm disorders |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | J Med Chem | Reviews MT1/MT2 receptor pharmacology, identifying tasimelteon as a high-affinity, non-selective MT1/MT2 agonist |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatr Dis Treat | Reviews prolonged-release melatonin and synthetic melatoninergic agonists as emerging approaches for insomnia management |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Ther Adv Neurol Disord | Reviews melatonin/analogs for sleep disturbance and REM Behavior Disorder in Parkinson's disease |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinol Lett | Reviews disrupted sleep chronobiology and the therapeutic potential of melatonin in circadian/metabolic disruption |
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Unclassified | Curr Drug Saf | Discusses melatonin and tasimelteon in relation to insomnia and circadian disruption in Alzheimer's disease |

## EU Market Information

Tasimelteon currently holds **no EU marketing authorization** (0 authorizations on record; market status: Not Marketed). No product/dosage-form table can be generated from the evidence pack.

## Safety Considerations

Please refer to the SmPC for safety information. (No EU-authorized product exists, so no SmPC is currently available; key warnings, contraindications, and drug-interaction data were not supplied in this evidence pack.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The insomnia prediction is mechanistically coherent with tasimelteon's established MT1/MT2 pharmacology and is supported by one completed Phase 3 RCT (n=322) plus an ongoing confirmatory Phase 3 pediatric trial, giving it L1-level evidence. However, this evidence largely reflects an overlap with the drug's known approved use rather than a genuinely novel indication, and critical safety data are missing.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (flagged as a **Blocking** data gap — required before any safety pre-assessment can proceed)
- Confirmed mechanism-of-action documentation via DrugBank (High-severity data gap)
- Clarification of whether insomnia should be classified as a true repurposing candidate or as a label/dosage-form extension of the existing Non-24-Hour Sleep-Wake Disorder indication
- EU regulatory pathway assessment, since the drug currently holds no EU marketing authorization
- Deprioritize (Hold) the remaining low-confidence predictions (polymicrogyria, ALS-cluster diseases, endogenous depression) pending mechanistic or clinical evidence beyond review-level literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

