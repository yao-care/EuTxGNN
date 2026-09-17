---
layout: default
title: Pasireotide
parent: AI Predictions (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Pasireotide
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

# Pasireotide: From Cushing's Disease/Acromegaly to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Pasireotide is a somatostatin analog with known clinical use in Cushing's disease and acromegaly (general drug class knowledge; not present in this evidence pack).
> The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
> but currently **no clinical trials** and **no published literature** support this direction — this is a model-prediction-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (drug class: somatostatin analog) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 96.12% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack — it is explicitly flagged as a High-severity data gap (DG002) requiring a DrugBank API query. Likewise, the drug's original indication is not recorded (`original_indications: []`). No pharmacological or clinical rationale can currently be constructed from the supplied data alone.

For context, pasireotide is generally known as a cyclohexapeptide somatostatin analog with broad affinity across somatostatin receptor subtypes (predominantly SSTR5), used in conditions such as Cushing's disease and acromegaly. NSIAD, in contrast, is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2) gene, a pathway mechanistically distinct from somatostatin receptor signaling. No direct or indirect molecular link between the two has been identified in the evidence pack.

The remaining nine predicted indications in this pack (ranks 2–10) reinforce this picture: where rationale text is available, it explicitly describes the predictions as **knowledge-graph noise** with no plausible mechanistic link (e.g., a congenital chromosomal rearrangement syndrome, and a periodontitis-related prediction where the only literature theme — diabetes/inflammation — is unrelated to pasireotide, and where pasireotide's known hyperglycemic side effect could theoretically worsen rather than treat the condition). This pattern across the candidate list lowers overall confidence in the top-ranked prediction as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Pasireotide is currently **not marketed** in this jurisdiction (0 authorizations on record), so no marketing authorization table is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Note: TFDA/label-level warnings and contraindications for this drug are recorded as a **Blocking** data gap (DG001) — this prevents formal S1 safety screening and must be resolved before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (NSIAD) has zero supporting clinical trials or literature — it is an unvalidated model output (L5), and no plausible mechanistic link to somatostatin receptor pharmacology is apparent (NSIAD is an AVPR2-driven condition).
- A Blocking-severity safety data gap (missing TFDA warnings/contraindications) currently prevents even a baseline safety assessment.
- Other candidate indications in this pack were independently annotated as low-confidence knowledge-graph noise, further reducing confidence in this drug's repurposing pipeline output at this time.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — required to clear the Blocking gap (DG001)
- Formal mechanism of action data via DrugBank API (DG002)
- Confirmed original indication(s) for this drug in the regulatory dataset
- Any preclinical or mechanistic evidence specifically connecting somatostatin signaling to AVPR2-mediated antidiuresis, if it exists, before further investment in this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

