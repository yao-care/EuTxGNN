---
layout: default
title: Neratinib
parent: Medium Evidence (L3-L4)
nav_order: 411
evidence_level: L3
indication_count: 10
---

# Neratinib
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

# Neratinib: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

> Neratinib is an irreversible pan-HER tyrosine kinase inhibitor whose efficacy in HER2-positive breast cancer is established in the literature evidence provided (e.g., the ExteNET trial).
> The TxGNN model predicts it may be effective for **Normal Breast-Like Subtype of Breast Carcinoma**,
> with only **1 clinical trial** and **no dedicated publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (inferred from literature evidence; no EU marketing authorization record found in this dataset) |
| Predicted New Indication | Normal Breast-Like Subtype of Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L3 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, pending DrugBank API lookup). Based on known information, Neratinib belongs to the irreversible pan-HER (HER1/EGFR, HER2, HER4) tyrosine kinase inhibitor class. Its efficacy in HER2-positive breast cancer has been demonstrated in supporting literature (e.g., the ExteNET Phase 3 trial for extended adjuvant therapy), which is consistent with public knowledge of this drug class.

The predicted new indication, "normal breast-like subtype of breast carcinoma," refers to one of the intrinsic molecular subtypes of breast cancer (alongside Luminal A/B, HER2-enriched, and Basal-like). This subtype is typically characterized as HER2-negative/low, which creates a mechanistic tension with neratinib's HER2-driven mode of action. The only supporting trial in this evidence pack (NCT01670877) actually enrolled patients with **HER2 non-amplified but HER2-mutant** metastatic breast cancer — a genomically defined population that is related to, but not identical with, the transcriptomically defined "normal-like" subtype.

Given this mismatch between the trial population and the predicted disease label, the mechanistic rationale should be considered **provisional**: it plausibly reflects a subset of HER2-negative tumors carrying activating HER2/HER-family mutations that remain sensitive to pan-HER inhibition, rather than a validated efficacy signal in the "normal-like" subtype as a whole.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Evaluated neratinib alone and in combination with fulvestrant in metastatic breast cancer that is HER2 non-amplified but harbors an activating HER2 mutation — a population mechanistically adjacent to, but not synonymous with, the "normal-like" subtype. |

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Neratinib currently has no EU marketing authorization record in this evidence pack (0 licenses, market status: Not Marketed). Regulatory status should be independently verified against the EMA product database before any decision advances beyond Hold.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (pan-HER tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> ⚠ Note: Safety data collection (TFDA/EMA label warnings and contraindications) is flagged as a **Blocking** data gap (DG001) — this must be resolved before the candidate can enter the S1 safety initial evaluation stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported by only one completed, non-randomized Phase 2 trial whose enrolled population (HER2-mutant, HER2 non-amplified metastatic breast cancer) does not precisely match the predicted disease label ("normal breast-like subtype"), and there is no supporting literature. Combined with a Blocking safety data gap and the absence of any EU marketing authorization, the evidence is insufficient to proceed past Hold at this time.

**To proceed, the following is needed:**
- TFDA/EMA SmPC safety data (warnings, contraindications, DDI) — required to clear the Blocking data gap (DG001)
- Confirmed mechanism of action via DrugBank API (DG002)
- Clarification of disease ontology mapping between "normal-like breast carcinoma" (transcriptomic subtype) and the HER2-mutant trial population (genomic subtype)
- Additional trials or literature specific to HER2-negative/normal-like breast cancer to validate the mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

