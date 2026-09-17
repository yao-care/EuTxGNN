---
layout: default
title: Ulipristal
parent: AI Predictions (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
---

# Ulipristal
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

# Ulipristal: From Undocumented Original Indication to Rheumatoid Arthritis

## One-Sentence Summary

The original approved indication for ulipristal is not documented in the current evidence pack, and detailed mechanism of action data is also unavailable. The TxGNN model's top-ranked prediction suggests possible activity in **Rheumatoid Arthritis**, but this signal is supported by only **1 clinical trial** (graded as low-relevance/likely false positive) and **no supporting literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current evidence pack |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 90.31% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for ulipristal in the current dataset. However, the model's own rationale text identifies ulipristal as a Selective Progesterone Receptor Modulator (SPRM) acting on progesterone and glucocorticoid receptor pathways — this class information comes from the repurposing rationale rather than a confirmed MOA record.

Because the original approved indication is not documented in this evidence pack, no direct comparison can be made between the drug's established use and the newly predicted indication. More importantly, the rationale explicitly states that there is **no known mechanistic connection** between SPRM-mediated progesterone/glucocorticoid receptor modulation and the immune pathogenesis of rheumatoid arthritis. The evidence pack itself flags this association as likely arising from TxGNN embedding co-occurrence rather than any biological or clinical basis.

This pattern is consistent across all ten top-ranked predictions in the dataset: every candidate is scored L5 (model prediction only), most have no clinical trial or literature evidence at all, and where a trial was retrieved (as with rheumatoid arthritis, rank 1), it was graded as clinically irrelevant to ulipristal. Overall, this prediction should be treated as a hypothesis-generating signal only, not as evidence of therapeutic potential.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04300465](https://clinicaltrials.gov/study/NCT04300465) | N/A | Unknown | 64 | Community-based lifestyle intervention program (MySláinte) targeting cardiovascular risk factors. Does not test ulipristal and is not a drug trial. Graded **C (low relevance)** — likely a false-positive co-occurrence from the knowledge graph rather than genuine supporting evidence. |

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Currently no EU marketing authorization found for this drug (market status: Not Marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information. Key safety fields (warnings, contraindications, drug interactions) are not currently available in this evidence pack; this is flagged as a **Blocking** data gap that must be resolved before any safety-based decision can be made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only retrieved clinical trial is unrelated to ulipristal and graded as a likely false positive, no supporting literature exists, and the rationale text itself states there is no known mechanistic link between the drug's proposed pharmacology and rheumatoid arthritis. Combined with the absence of EU marketing authorization and missing safety label data, the evidence base is insufficient to advance this candidate.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (currently a Blocking data gap)
- Confirmed original indication and mechanism of action (MOA) data for ulipristal
- Preclinical or literature evidence establishing a plausible biological link between SPRM activity and rheumatoid arthritis pathogenesis
- Additional, disease-specific clinical trials or case data actually testing ulipristal (or its pharmacological class) in autoimmune/inflammatory conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

