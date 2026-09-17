---
layout: default
title: Pomalidomide
parent: High Evidence (L1-L2)
nav_order: 476
evidence_level: L2
indication_count: 10
---

# Pomalidomide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Pomalidomide: From Relapsed/Refractory Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

> Pomalidomide is a third-generation immunomodulatory drug (IMiD) already used for relapsed/refractory multiple myeloma.
> The TxGNN model predicts it may also be effective for **Indolent (Smoldering) Plasma Cell Myeloma**,
> with **1 completed Phase 2 clinical trial** and **2 supporting publications** currently available for this specific candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via marketing authorization data (data gap); mechanistic evidence references relapsed/refractory multiple myeloma |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 93.96% |
| Evidence Level | L2 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for pomalidomide is not available in the structured `original_moa` field of this Evidence Pack (data gap). However, the repurposing rationale attached to this candidate describes the mechanism directly: pomalidomide is a third-generation IMiD that binds cereblon (CRBN), an E3 ubiquitin ligase, driving degradation of the transcription factors IKZF1 and IKZF3. This suppresses plasma cell proliferation and enhances T-cell/NK-cell anti-tumour immunity — the basis for its established use in relapsed/refractory multiple myeloma.

Indolent (smoldering) plasma cell myeloma sits on the same disease continuum as active multiple myeloma, representing an earlier, lower tumour-burden stage of the same clonal plasma cell disorder. Because the pathogenic mechanism (clonal plasma cell proliferation) is shared, the CRBN/IKZF1/IKZF3 mechanism is directly applicable without requiring cross-disease extrapolation — this is the strongest category of TxGNN prediction, essentially a "same disease, earlier stage" extension rather than a novel mechanistic hypothesis.

This is supported by direct trial evidence: NCT02046915 tested pomalidomide + dexamethasone specifically in a relapsed myeloma population, matching both the drug and the underlying disease biology, though the single-arm design limits it to hypothesis-supporting rather than confirmatory evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02046915](https://clinicaltrials.gov/study/NCT02046915) | Phase 2 | Completed | 60 | Single-arm study of pomalidomide + dexamethasone, with response-adapted cyclophosphamide added, in relapsed myeloma; designed to balance efficacy against the substantial myelosuppression risk seen when IMiDs are combined with alkylating agents. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22180161](https://pubmed.ncbi.nlm.nih.gov/22180161/) | 2012 | Review | American Journal of Hematology | Updated diagnosis, risk-stratification, and management guidance for multiple myeloma, providing disease-context background for indolent/smoldering staging. |
| [21181954](https://pubmed.ncbi.nlm.nih.gov/21181954/) | 2011 | Review | American Journal of Hematology | Earlier version of the same myeloma diagnosis/management update, establishing the disease framework within which indolent myeloma is staged. |

---

## EU Market Information

No EU marketing authorization records are currently present in this dataset (0 authorizations, market status: not marketed). This should be verified independently, as the absence of records here may reflect a data collection gap rather than confirmed non-marketing status.

---

## Cytotoxicity

Pomalidomide is an antineoplastic agent (approved oncology indication: relapsed/refractory multiple myeloma) and is therefore evaluated for cytotoxicity risk.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/immunomodulatory therapy (Immunomodulatory Imide Drug, IMiD; thalidomide analog) — not a conventional cytotoxic agent |
| Myelosuppression Risk | High — trial evidence (NCT02046915) explicitly notes patients are at "substantial risk of critical myelosuppression," particularly when combined with alkylating agents |
| Emetogenicity Classification | Please refer to the SmPC — no emetogenicity data provided in this Evidence Pack |
| Monitoring Items | Complete blood count (CBC) with differential, given the documented myelosuppression risk; renal function (IMiDs are renally handled); consider thromboembolism monitoring given class-wide VTE risk |
| Handling Protection | As a thalidomide-class IMiD with known teratogenic potential, handling should follow pregnancy-prevention/REMS-equivalent controls in addition to standard antineoplastic handling precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this Evidence Pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is direct rather than extrapolated — indolent plasma cell myeloma and the approved indication share the same underlying clonal biology — and is supported by a completed Phase 2 trial in a closely related patient population, justifying advancement with guardrails rather than a full "Go."

**To proceed, the following is needed:**
- **Blocking gap**: TFDA/regulatory label warnings and contraindications must be obtained (currently unavailable), as this is required before any S1 safety pre-assessment can proceed.
- Confirmed drug-level mechanism of action (MOA) from DrugBank, to replace the current data gap and validate the mechanistic rationale independently of trial free-text.
- A confirmatory (ideally randomized) trial specifically in the indolent/smoldering myeloma population, since the current supporting trial (NCT02046915) enrolled relapsed/active myeloma patients, not the indolent subgroup itself.
- Drug interaction data, given none is currently available for this candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

