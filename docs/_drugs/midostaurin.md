---
layout: default
title: Midostaurin
parent: AI Predictions (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Midostaurin
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

# Midostaurin: From Undocumented Original Indication to Familial Thrombocytosis

## One-Sentence Summary

> Midostaurin's original approved indication and mechanism of action are not documented in the current evidence pack (drug status: **Not marketed** in this jurisdiction, 0 authorizations on record).
> The TxGNN model predicts it may be effective for **Familial Thrombocytosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic assessment explicitly flags the biological link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap) |
| Predicted New Indication | Familial Thrombocytosis |
| TxGNN Prediction Score | 98.92% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for midostaurin is not available in the structured evidence (`original_moa`: Data Gap), and no original indication record was found for this jurisdiction. Contextual information embedded in the evidence pack (drawn from literature retrieved for other candidate indications) describes midostaurin as a multikinase inhibitor targeting PKCα, VEGFR2, KIT, PDGFR, and FLT3, and notes it is used clinically in FLT3-mutated AML and aggressive systemic mastocytosis — but this is background context surfaced through literature abstracts, not a confirmed field in this drug's regulatory record, and should be treated accordingly.

For the top-ranked prediction, **familial thrombocytosis**, the evidence pack's own mechanistic assessment is unfavorable: this condition is typically driven by germline mutations in *THPO*, *MPL*, or *JAK2*, rather than the FLT3/KIT/PKC pathways that midostaurin targets. The rationale explicitly states that the high TxGNN score is not backed by substantive mechanistic support — this appears to be a model-only signal rather than a biologically grounded hypothesis.

It is worth noting that other candidates in this same evidence pack show comparatively stronger rationale — for example, rank 5 ("thrombocythemia," a myeloproliferative neoplasm with FLT3-ITD/JAK2 pathway involvement) reaches evidence level L4 with a "Research Question" recommendation, and rank 3 ("metastatic melanoma") has direct Phase IIA clinical trial evidence (negative result). These may warrant separate, dedicated evaluation outside the scope of this specific report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorizations are recorded for this drug. Market status: **Not marketed** (total licenses: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: Key warnings, contraindications, and drug-drug interaction data are all currently unavailable (data gap DG001, flagged as Blocking — this prevents the candidate from entering the S1 safety pre-assessment stage).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for familial thrombocytosis is supported only by the TxGNN model score (L5), with no clinical trials or literature evidence, and the evidence pack's own mechanistic analysis concludes the pathway link is weak (THPO/MPL/JAK2-driven disease vs. a FLT3/KIT/PKC-targeted drug). A Blocking data gap in TFDA/SmPC safety information further prevents this candidate from proceeding to formal safety review.

**To proceed, the following is needed:**
- TFDA/SmPC label data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action data via DrugBank API — currently High severity gap (DG002)
- Disease-specific preclinical or clinical evidence for familial thrombocytosis (none currently exists)
- Consider evaluating rank 5 (thrombocythemia, L4) and rank 3 (metastatic melanoma, L2 with negative trial data) as separate, better-evidenced candidates from this same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

