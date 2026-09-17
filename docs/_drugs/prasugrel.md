---
layout: default
title: Prasugrel
parent: AI Predictions (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Acute Coronary Syndrome (Post-PCI Antiplatelet Therapy) to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a P2Y12 platelet ADP receptor antagonist historically used alongside aspirin in acute coronary syndrome patients undergoing PCI. The TxGNN model's top prediction suggests possible efficacy for **Pulmonary Hypertension**, but the **2 clinical trials** and **2 publications** currently attached to this pairing are not mechanistically relevant — the evidence pack itself flags this as a likely coincidental keyword match rather than genuine supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome, post-PCI antiplatelet therapy (inferred from literature evidence; no structured EU regulatory record on file) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, structured mechanism-of-action data is not available for Prasugrel in this evidence pack (`original_moa` is a data gap). Based on the repurposing rationale text provided, Prasugrel is a thienopyridine prodrug that acts as an irreversible antagonist of the platelet P2Y12 ADP receptor, inhibiting platelet aggregation — the same mechanistic class as clopidogrel and ticagrelor.

The theoretical link to pulmonary hypertension rests on the idea that certain PH subtypes (notably CTEPH) involve chronic microthrombus formation, where antiplatelet therapy could plausibly play an adjunctive role. However, current PAH/CTEPH treatment guidelines do not support antiplatelet monotherapy, and there is no established efficacy signal — bleeding risk is not offset by demonstrated benefit in this context.

Critically, the clinical trials and literature actually attached to this prediction (NOAC management in atrial fibrillation, cancer-associated thrombosis trial eligibility, clopidogrel adherence in ACS, and COVID-19 comorbidity registries) **do not address prasugrel treatment or pulmonary hypertension outcomes at all**. The evidence pack's own annotation concludes this is most likely a knowledge-graph keyword coincidence rather than a genuine mechanistic signal — this should be treated as an unverified AI prediction, not an evidence-supported hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational, cross-sectional study describing NOAC management in elderly patients with non-valvular atrial fibrillation in Spain — no direct relevance to prasugrel or pulmonary hypertension |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on eligibility for cancer-associated thrombosis trials (e.g., CARAVAGGIO) — does not involve prasugrel treatment or PH endpoints |

Both trials were graded "C" (low relevance) in the underlying evidence review.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | Examines clopidogrel use, adherence, and persistence in ACS patients post-PCI; notes prasugrel as an alternative per guidelines, but does not address pulmonary hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | Analyzes background chronic-disease therapy prior to COVID-19 infection and its effect on mortality outcomes; no direct link to prasugrel efficacy or PH |

Neither publication provides direct or indirect evidence for prasugrel's use in pulmonary hypertension.

## EU Market Information

Prasugrel currently has **no EU marketing authorization on file** in this dataset (`market_status: Not marketed` / Not Marketed, `total_licenses: 0`). No product listings are available to summarize.

## Safety Considerations

Please refer to the SmPC for safety information. No structured warnings, contraindications, or drug-drug interaction data were available in this evidence pack (TFDA label data is flagged as a **Blocking** data gap — DG001).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pulmonary hypertension) has only L5 evidence — a TxGNN score alone, with all attached clinical trials and literature judged clinically irrelevant by the evidence review itself. Combined with the absence of EU marketing status, MOA data, and safety/label information, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) — currently blocking safety pre-screening (S1)
- Resolve DG002 (confirmed mechanism of action via DrugBank) to properly assess mechanistic plausibility
- Identify clinical trials or literature that specifically evaluate prasugrel (or class-level P2Y12 inhibitors) in pulmonary hypertension/CTEPH populations
- Consider re-evaluating **rank 2 (migraine disorder, L3 evidence, decision stage S1, "Research Question")** instead — it is supported by class-relevant thienopyridine/PFO literature (PMID 30478067, PMID 30478066) and represents a materially stronger evidentiary basis than the top-ranked pulmonary hypertension candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

