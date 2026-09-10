---
layout: default
title: Galsulfase
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Galsulfase
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

# Galsulfase: From Mucopolysaccharidosis VI (Maroteaux-Lamy Syndrome) to Ptosis-Strabismus-Ectopic Pupils Syndrome

*Note: The evidence pack's `taiwan_regulatory.licenses` and `drug.original_indications` are empty, and `original_moa` is flagged as a data gap (DG002). The original indication/MOA above is reconstructed from the mechanistic annotation embedded in this same evidence pack (rank-10 rationale, which identifies galsulfase as N‑acetylgalactosamine‑4‑sulfatase used for MPS VI), not from an independent source.*

## One-Sentence Summary

Galsulfase (DrugBank DB01279) is an enzyme replacement therapy whose target enzyme, per this evidence pack, is used in Mucopolysaccharidosis VI (Maroteaux-Lamy syndrome); the drug is currently **not marketed in Taiwan**. The TxGNN model's top-ranked prediction is **Ptosis-Strabismus-Ectopic Pupils Syndrome**, but this pairing has **0 clinical trials and 0 publications**, and the model's own rationale states there is no known mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Ptosis-Strabismus-Ectopic Pupils Syndrome |
| TxGNN Prediction Score | 97.89% (model rank 17,520) |
| Evidence Level | L5 (model prediction only) |
| Market Status (Taiwan) | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The evidence pack does not provide a confirmed `original_moa` field for galsulfase (flagged as data gap DG002, severity High). However, the rationale attached to this drug's own predictions (specifically the rank-10 candidate) identifies galsulfase as N-acetylgalactosamine-4-sulfatase, an enzyme-replacement therapy for Mucopolysaccharidosis VI (Maroteaux-Lamy syndrome), acting via chondroitin/dermatan sulfate metabolism.

For the top-ranked candidate, **Ptosis-Strabismus-Ectopic Pupils Syndrome**, the evidence pack's own mechanistic assessment is explicit and negative: this is a rare congenital ocular structural/neurodevelopmental syndrome with no known connection to galsulfase's sulfate-metabolizing enzyme-replacement mechanism. The pack states this pairing reflects "TxGNN embedding similarity only, with no mechanistic plausibility support" — i.e., the prediction is driven by graph-embedding proximity rather than any biological rationale.

By contrast, the same evidence pack's rank-10 candidate, Scheie syndrome, is at least in the correct disease family (a mucopolysaccharidosis), though it targets a different enzyme deficiency (MPS I / α-L-iduronidase, treated with laronidase) than galsulfase's actual target (MPS VI). That candidate has some literature support (see below) but is not the top-ranked prediction and was not selected as this report's primary subject.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Detailed safety information (key warnings, contraindications, drug interactions) is not currently available in this evidence pack. TFDA labeling data was queried but is a blocking data gap (DG001). Please refer to the manufacturer's official product labeling once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ptosis-Strabismus-Ectopic Pupils Syndrome) has no clinical trials, no literature, and the model's own rationale explicitly disclaims any mechanistic link — this is a pure embedding-similarity artifact (L5), not a biologically grounded repurposing hypothesis.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (DG001, Blocking) — required before any S1 safety screening
- Confirmed mechanism of action for galsulfase from DrugBank (DG002, High)
- A biologically plausible rationale connecting galsulfase's sulfatase-replacement mechanism to this specific ocular/neurodevelopmental syndrome, or reprioritization toward a mechanistically closer candidate (e.g., rank-10 Scheie syndrome, which at least sits within the mucopolysaccharidosis disease family, despite targeting a different enzyme deficiency than galsulfase)
- Confirmation of Taiwan market status before any regulatory pathway planning, since the drug currently holds zero local authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

