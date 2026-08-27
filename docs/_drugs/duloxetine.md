---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

Using superpowers checked — this is a self-contained content-generation task (populate the given evidence-pack-to-report template with the provided JSON), not a coding/debugging/design task, so no additional skill applies. I'll flag one honesty issue up front: `predicted_indications[0]` (top TxGNN score) is "benign paroxysmal torticollis of infancy," which has **zero** trials/literature and an L5/Hold status — I followed the spec's extraction rule literally rather than substituting a better-evidenced candidate from the same pack, and noted the discrepancy in the Conclusion so it isn't silently misleading.

Also note: `drug.original_indications` and `taiwan_regulatory.licenses` are both empty, so "Original Indication" cannot be sourced from Taiwan regulatory data as instructed — I did not guess it. Instead I cited the one place original indications actually appear in this evidence pack (the PMID 31749717 abstract, itself provided data, not external knowledge), and labeled it clearly as such rather than presenting it as a confirmed local label indication.

---

# Duloxetine: From Major Depressive Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

> Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI), globally known for treating major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, and fibromyalgia (per literature cited in this evidence pack).
> The TxGNN model's top-ranked prediction for this drug is **Benign Paroxysmal Torticollis of Infancy**, with a prediction score of 99.85%,
> but **0 clinical trials** and **0 publications** currently support this specific direction — it is a pure model prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Taiwan/EU regulatory dataset (drug currently not marketed, 0 licenses on record). Per literature context within this evidence pack (PMID 31749717), Duloxetine is known to be approved elsewhere for major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, and fibromyalgia. |
| Predicted New Indication | Benign Paroxysmal Torticollis of Infancy |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Duloxetine is currently unavailable and is flagged as a blocking-adjacent data gap in this evidence pack (DG002). Based on known pharmacological class information, Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI), a class whose efficacy has been proven in mood and anxiety disorders and certain chronic pain states; mechanistically it acts on monoamine reuptake rather than on developmental or vestibular pathways.

Benign paroxysmal torticollis of infancy is a self-limiting condition occurring in infancy, thought to be related to immature vestibular system development or to sit within the migraine spectrum. There is no established pharmacological or mechanistic link between SNRI activity and this condition, and no safety data exist for Duloxetine in this age group.

The TxGNN model assigned this pairing a very high similarity score, but that score reflects graph-embedding proximity rather than a validated biological rationale. Given the absence of any supporting mechanistic literature, trial data, or age-appropriate safety data, this specific prediction should be treated as a low-confidence, hypothesis-generating signal only, not as clinically actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations are on record for Duloxetine (DB00476) in this jurisdiction — the drug is currently listed as not marketed (0 licenses).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps or "not found" in this evidence pack; TFDA label warnings/contraindications retrieval is tracked as a blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has evidence level L5 — a model prediction with no supporting clinical trials, no literature, and no plausible mechanistic link to the drug's known SNRI pharmacology. Combined with the absence of any regulatory safety data (DG001, blocking) and MOA confirmation (DG002), there is currently no basis to advance this specific indication beyond exploratory research.

**To proceed, the following is needed:**
- TFDA/SmPC label data (warnings, contraindications) — required before any safety screening (blocking gap DG001)
- Confirmed mechanism of action from DrugBank or equivalent source (DG002)
- Preclinical or mechanistic rationale connecting SNRI activity to vestibular/migraine-spectrum pathophysiology, if this candidate is to be pursued further
- Note: within this same prediction batch, other candidates for Duloxetine show substantially stronger evidence and may warrant priority review instead — notably **obsessive-compulsive disorder** (L2, includes a completed Phase 4 trial [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) and a double-blind RCT, PMID 27811556) and **agoraphobia** (L4, supported by open-label and cohort literature on panic disorder). These were not the top-ranked TxGNN score but have meaningfully more clinical grounding than the rank-1 candidate covered above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

