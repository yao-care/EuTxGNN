---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Galcanezumab is a humanized anti-CGRP monoclonal antibody already used internationally to prevent episodic/chronic migraine and episodic cluster headache. The TxGNN model additionally flags **Migraine with Brainstem Aura** (a rare migraine subtype) as a plausible indication, and unlike nine other high-scoring but mechanistically implausible candidates in this batch, this one is backed by **20 publications**, including Phase 3 RCT data on the parent compound and several aura/hemiplegic-migraine-specific studies — though no dedicated clinical trial exists yet for this exact subtype.

> **Note on other candidates:** This evidence pack ranked 10 predicted indications for galcanezumab. Nine of them (e.g., heparin cofactor 2 deficiency, antithrombin deficiency, thrombophilia, atrophoderma vermiculata) have **zero clinical trials or literature support** and no biologically plausible link to the CGRP pathway; they are flagged internally as likely knowledge-graph embedding artifacts and scored "Hold." Only **migraine with brainstem aura** clears the bar for further evaluation, so this report focuses on that candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this regulatory dataset (0 EU/Taiwan authorizations on file); internationally, galcanezumab is indicated for migraine prevention and episodic cluster headache per published literature |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 98.33% |
| Evidence Level | L2 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured drug record (marked as a data gap). Based on the literature evidence collected for this candidate, galcanezumab is a humanized monoclonal antibody that binds and neutralizes calcitonin gene-related peptide (CGRP), a neuropeptide central to the pathophysiology of migraine and other trigeminovascular headache disorders. This mechanism is already validated by three pivotal Phase 3 RCTs (EVOLVE-1, EVOLVE-2, REGAIN) supporting its efficacy in general episodic and chronic migraine.

Migraine with brainstem aura (formerly "basilar-type migraine") is a subtype of migraine with aura, sharing the same underlying trigeminovascular/CGRP-mediated pathophysiology as typical migraine, but with additional brainstem-origin aura symptoms. Because CGRP signaling is implicated broadly across migraine subtypes — not only the non-aura form studied in the pivotal trials — extending anti-CGRP therapy to aura-predominant and even genetically-driven aura subtypes (e.g., familial/sporadic hemiplegic migraine) is mechanistically coherent, and is exactly the direction several of the collected publications explore.

The key caveat is that none of the identified literature is a trial specifically enrolling patients with brainstem aura; the supporting evidence instead comes from (a) general Phase 3 efficacy/mechanism data for CGRP blockade in migraine, and (b) smaller case series/observational studies in adjacent aura subtypes (hemiplegic migraine, aura in general). This subtype has historically been excluded from RCTs due to safety concerns around vasoactive drugs and brainstem/vascular symptoms, so applicability should be confirmed with caution rather than assumed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura specifically.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29813147](https://pubmed.ncbi.nlm.nih.gov/29813147/) | 2018 | RCT | JAMA Neurology | EVOLVE-1: pivotal Phase 3 trial establishing galcanezumab's efficacy for episodic migraine prevention vs. placebo |
| [33549036](https://pubmed.ncbi.nlm.nih.gov/33549036/) | 2021 | RCT (post-hoc/Phase 3 subanalysis) | J Headache Pain | Pooled analysis of EVOLVE-1, EVOLVE-2, REGAIN showing galcanezumab reduces migraine severity and associated symptoms |
| [32504377](https://pubmed.ncbi.nlm.nih.gov/32504377/) | 2020 | Review | Drugs | Comprehensive review confirming anti-CGRP mechanism and efficacy across episodic/chronic migraine and cluster headache |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Review (case reports) | J Clin Medicine | Reviews anti-CGRP mAbs (including galcanezumab) specifically for migraine **aura**; notes limited but promising data on aura prevention |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Review/Genetic | Headache | Genetic migraine disorders with aura/brainstem-type features responding to CGRP antagonist therapy |
| [37366160](https://pubmed.ncbi.nlm.nih.gov/37366160/) | 2023 | Case series | Headache | Anti-CGRP mAbs used in hemiplegic migraine (an aura-predominant subtype), a tertiary headache center series |
| [39345003](https://pubmed.ncbi.nlm.nih.gov/39345003/) | 2025 | Case series | Headache | Galcanezumab efficacy specifically reported in PRRT2-associated familial hemiplegic migraine |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual patient analysis | J Headache Pain | Effectiveness/safety of anti-CGRP mAbs in hemiplegic migraine, a rare aura subtype systematically excluded from RCTs |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review (mechanism) | Handb Exp Pharmacol | Foundational review of CGRP's role in migraine pathophysiology, underpinning rationale for aura-subtype extension |
| [36266558](https://pubmed.ncbi.nlm.nih.gov/36266558/) | 2023 | Cohort/Post-hoc analysis | Neurology and Therapy | Phase 2 secondary analysis in Japanese patients on migraine severity/symptom reduction |

---

## EU Market Information

No marketing authorization records are available in this evidence pack (0 licenses on file; market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CGRP-blockade mechanism is well-validated for migraine broadly (multiple Phase 3 RCTs), and multiple case series/reviews support extending this to aura-predominant subtypes, giving this candidate L2 evidence — clearly stronger than the nine other TxGNN-ranked candidates in this batch, which have no clinical or mechanistic support. However, no trial has directly tested galcanezumab in migraine with brainstem aura, a subtype historically excluded from RCTs on safety grounds (vasoactive drug in a vascular-symptom-driven condition).

**To proceed, the following is needed:**
- Official drug label / SmPC data (TFDA warnings and contraindications) — currently a **blocking** data gap preventing safety (S1) evaluation
- Confirmed mechanism-of-action documentation from DrugBank or manufacturer labeling
- A dedicated pilot study or case series specifically enrolling migraine-with-brainstem-aura patients, given their systematic exclusion from pivotal trials
- EU/Taiwan marketing authorization status confirmation, since this drug currently shows zero licenses on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

