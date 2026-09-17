---
layout: default
title: Trastuzumab Deruxtecan
parent: AI Predictions (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Trastuzumab Deruxtecan
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

# Trastuzumab Deruxtecan: From Undocumented Indication to Drug-induced Osteoporosis

## One-Sentence Summary

The original indication and mechanism of action for trastuzumab deruxtecan are not documented in the current Evidence Pack (flagged as a Blocking/High-severity data gap). TxGNN's top prediction is **Drug-induced Osteoporosis**, but this candidate has **0 clinical trials** and **0 supporting publications**, and the model's own rationale explicitly flags it as a likely graph-noise artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/label data in this Evidence Pack (Data Gap DG002) |
| Predicted New Indication | Drug-induced Osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset (Data Gap DG002, High severity). Based on the rationale annotations accompanying the predictions, trastuzumab deruxtecan (T-DXd) is understood to be a HER2-targeted antibody-drug conjugate (ADC), delivering a cytotoxic payload (deruxtecan, a topoisomerase I inhibitor) selectively to HER2-expressing cells.

For the top-ranked prediction, **drug-induced osteoporosis**, the evidence pack's own mechanistic assessment concludes there is **no known pathway** linking a HER2-targeted ADC/topoisomerase I inhibitor to bone metabolism or osteoclast regulation, and characterizes this association as a statistical artefact of the knowledge graph rather than a biologically plausible repurposing hypothesis. The same conclusion — "no mechanistic link, no supporting evidence" — is echoed across the remaining nine predictions in this batch (severe nonproliferative diabetic retinopathy, diabetic retinopathy, bronchitis, diabetic cataract, bronchial adenomas/carcinoids in children, non-seminomatous lesion, ductal/ductular proliferation, chondroid hamartoma, and testicular/paratesticular tumor). Several of these predictions are additionally flagged as **contradicting known ADC safety signals** (e.g., diabetic retinopathy vs. known T-DXd ocular toxicity; bronchitis vs. known interstitial lung disease risk).

Given the absence of both original-indication documentation and a plausible mechanistic rationale for any of the top 10 predictions, this candidate does not currently meet the bar for further pharmacological evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: the top-ranked prediction, drug-induced osteoporosis, has no associated literature. For context, rank 8 — "ductal or ductular proliferation," evidence level L4 — did return 20 publications, but 19 are unrelated hepatic ductular-reaction basic science and the single drug-relevant hit, [PMID 37492824](https://pubmed.ncbi.nlm.nih.gov/37492824/) (Cureus, 2023), is a case report of **deruxtecan-induced reversible Fanconi syndrome** — an adverse-event signal, not efficacy evidence.)*

---

## EU Market Information

Trastuzumab deruxtecan currently has **no EU marketing authorizations** on record in this Evidence Pack (`total_licenses: 0`, `market_status: Not marketed`).

---

## Cytotoxicity

Trastuzumab deruxtecan is an antibody-drug conjugate delivering a cytotoxic payload, and is therefore classified as an antineoplastic agent for the purposes of this assessment.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (ADC) carrying a cytotoxic topoisomerase I inhibitor payload (deruxtecan) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Should be handled per cytotoxic/hazardous drug handling protocols, consistent with its cytotoxic payload |

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug interactions) is not available in the current dataset — please refer to the SmPC for safety information.

**Additional signals noted in the evidence pack's prediction rationale** (not sourced from structured SmPC data, provided for context only):
- Reported class-associated risks referenced during mechanistic screening include interstitial lung disease/pneumonitis and ocular toxicity (keratopathy).
- One published case report, [PMID 37492824](https://pubmed.ncbi.nlm.nih.gov/37492824/), describes deruxtecan-induced reversible Fanconi syndrome (renal tubular toxicity) in a patient treated for HER2+ breast cancer.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top-ranked TxGNN predictions for this drug lack a plausible mechanistic link per the model's own rationale, and none has clinical trial support. The single drug-relevant literature hit found across all predictions is an adverse-event case report, not efficacy evidence. Combined with the absence of EU marketing authorization and missing original-indication/MOA/safety documentation, there is insufficient basis to advance any of these candidates.

**To proceed, the following is needed:**
- Resolve Data Gap DG001 (Blocking): obtain the drug's label/SmPC warnings and contraindications, since safety review cannot proceed without it.
- Resolve Data Gap DG002 (High): obtain confirmed mechanism of action and original indication documentation from DrugBank to enable a proper mechanistic relevance assessment.
- Given the consistently low evidence quality (L5 across 9/10 candidates, and a negative L4 signal for the 10th), consider excluding this candidate from further repurposing evaluation unless new clinical trial or literature evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

