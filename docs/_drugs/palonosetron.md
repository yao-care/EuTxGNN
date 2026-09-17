---
layout: default
title: Palonosetron
parent: Medium Evidence (L3-L4)
nav_order: 448
evidence_level: L4
indication_count: 10
---

# Palonosetron
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

# Palonosetron: From Antiemetic Use (CINV/PONV) to Migraine Disorder

## One-Sentence Summary

Palonosetron is a selective 5-HT3 receptor antagonist established for preventing chemotherapy- and postoperative-induced nausea and vomiting (CINV/PONV).
The TxGNN model predicts it may be effective for **Migraine Disorder**, but this direction is supported by **0 clinical trials** and only **1 case report** — and that case report actually describes Palonosetron *causing* migraine-type headache as an adverse reaction, not treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in marketing licenses (drug not currently marketed in this jurisdiction). Literature evidence in this pack confirms established use as an antiemetic for chemotherapy-induced and postoperative nausea/vomiting (CINV/PONV) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`[Data Gap]`). Based on the literature contained in this evidence pack, Palonosetron is a second-generation 5-HT3 receptor antagonist whose efficacy in CINV/PONV prevention is well established, and there is no known pharmacological pathway connecting 5-HT3 antagonism to migraine pathophysiology.

More importantly, the only literature evidence directly tied to this prediction is a 2011 case report titled *"Palonosetron-induced migraine-type headache"* — i.e., the drug is reported as a **cause** of migraine-type headache, not a treatment for it. This is the opposite direction from what the TxGNN score implies. The three clinical trials found under the related "headache disorder" node are also all PONV/CINV prophylaxis studies (existing indications), not migraine treatment trials, so they do not add supporting evidence either.

Given the missing MOA data, the absence of any efficacy trial, and evidence pointing toward an adverse effect rather than a therapeutic one, this prediction should be treated as a candidate signal requiring mechanistic clarification, not a repurposing lead ready for evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report | Canadian Journal of Anaesthesia | Reports Palonosetron **inducing** migraine-type headache as an adverse reaction — evidence direction opposes the predicted therapeutic use |

---

## EU Market Information

This drug is not currently marketed in this jurisdiction (`market_status: Not marketed`, 0 total authorizations). No marketing authorization records are available to extract indication text from.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug interaction data are not available in the current evidence pack — flagged as `DG001: EMA package insert warnings/contraindications`, severity Blocking.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence for Palonosetron in migraine, and the sole relevant publication describes migraine-type headache as an adverse effect of the drug rather than a therapeutic benefit — directly contradicting the predicted indication. Combined with missing MOA and safety labeling data, the evidence base is insufficient to proceed.

**To proceed, the following is needed:**
- Mechanism of action data (DG002) to assess biological plausibility for migraine
- TFDA/EMA product labeling — warnings and contraindications (DG001, Blocking)
- Primary efficacy studies (not adverse-event reports) evaluating Palonosetron specifically for migraine treatment
- Review of lower-ranked co-predicted indications (e.g., migraine with brainstem aura, epilepsy-susceptibility literature under rank 3) for possible knowledge-graph node cross-contamination, since none show a credible therapeutic mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

