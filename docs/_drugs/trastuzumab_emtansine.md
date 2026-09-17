---
layout: default
title: Trastuzumab Emtansine
parent: Medium Evidence (L3-L4)
nav_order: 615
evidence_level: L3
indication_count: 10
---

# Trastuzumab Emtansine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab emtansine (T-DM1) is a HER2-targeted antibody-drug conjugate whose approved use is built around HER2-positive breast cancer. The TxGNN model predicts it may also be effective for **Normal Breast-Like Subtype of Breast Carcinoma**, but this signal is currently supported by only **1 clinical trial** and **no dedicated literature**, and the mechanistic fit is uncertain because this molecular subtype typically shows low HER2 expression.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (inferred from the repurposing rationale; no EU authorization record is currently on file to independently confirm this — see EU Market Information below) |
| Predicted New Indication | Normal Breast-Like Subtype of Breast Carcinoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently missing for this candidate (flagged as a High-severity data gap). However, evidence assembled for this candidate consistently describes trastuzumab emtansine as an antibody-drug conjugate (ADC): the anti-HER2 monoclonal antibody trastuzumab chemically linked to the cytotoxic microtubule inhibitor DM1 (emtansine). The antibody component delivers the cytotoxic payload specifically to HER2-overexpressing tumor cells, which is why its established use is anchored to HER2-positive breast cancer.

"Normal breast-like subtype" is not a separate disease entity but one of the intrinsic molecular subtypes of breast carcinoma (alongside Luminal A/B, HER2-enriched, and Basal-like), and it can co-occur across different HER2 statuses. The repurposing rationale for this candidate explicitly notes that if a tumor of this subtype happens to be HER2-overexpressing, it would fit T-DM1's existing mechanism; however, the normal breast-like subtype is typically associated with lower HER2 expression, which weakens the mechanistic case unless HER2 status is separately confirmed in the target population.

In short, the prediction is mechanistically plausible only as a conditional subset (HER2-positive tumors that happen to be classified as normal breast-like), not as a broad extension of T-DM1's activity to this subtype as a whole. This conditionality, combined with thin clinical evidence, is the main reason the evidence level remains modest.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Evaluates optimal neoadjuvant-to-adjuvant anti-HER2-based therapy in Nigerian women with HER2-positive breast cancer; assesses efficacy and safety before/after surgery. T-DM1 is not explicitly named as the study drug, and no results are available yet. |

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Currently no EU marketing authorization records available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — HER2-directed antibody-drug conjugate (ADC) carrying the cytotoxic microtubule-inhibitor payload DM1 (emtansine) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting clinical trial is an ongoing, not-yet-reported Phase 2 study that does not specifically test T-DM1, and the mechanistic rationale depends on a HER2-positive subset within a molecular subtype that is typically HER2-low. Evidence is currently insufficient to move this candidate past a research-question stage.

**To proceed, the following is needed:**
- Mechanism-of-action confirmation via DrugBank API query (currently a High-severity data gap)
- Official product label / SmPC warnings and contraindications, sourced and parsed from the regulatory authority (currently a Blocking-severity data gap, required before any safety pre-assessment)
- Confirmation of HER2 expression status among "normal breast-like" tumors, to establish whether the mechanistic link applies broadly or only to a HER2-positive subset
- Results from NCT06348134 once available, and identification of any trial that directly tests T-DM1 in this specific subtype
- Verification of EU marketing authorization status, since the current record shows no active authorization for this well-established oncology agent — this should be re-checked against the source regulatory database for completeness
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

