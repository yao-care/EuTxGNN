---
layout: default
title: Corifollitropin Alfa
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Corifollitropin Alfa
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

# Corifollitropin Alfa: From Ovarian Stimulation to Gastroduodenitis

## One-Sentence Summary

Corifollitropin alfa is a long-acting recombinant FSH (follicle-stimulating hormone) analogue used for controlled ovarian stimulation in assisted reproductive technology (ART), designed to replace daily FSH injections during the early follicular phase.
The TxGNN model predicts it may be effective for **Gastroduodenitis**, yet **no clinical trials** and **no publications** currently support this direction.
Across all 10 predicted indications in this batch, Evidence Level L5 applies uniformly — representing model-only predictions with no clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Controlled ovarian stimulation (ART) — no Taiwan regulatory approval on file |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Market Status (Taiwan) | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the current database query. Based on published pharmacology, Corifollitropin alfa is a long-acting FSH analogue — a fusion protein combining recombinant FSH-β with the C-terminal peptide of hCG-β — that acts as an FSH receptor (FSHR) agonist. It sustains supraphysiological FSH levels for approximately one week per single subcutaneous injection, driving multi-follicular development during controlled ovarian stimulation. Its primary pharmacological target, FSHR, is expressed almost exclusively in ovarian granulosa cells and testicular Sertoli cells.

Gastroduodenitis is an inflammatory condition of the stomach and duodenum, driven predominantly by *Helicobacter pylori* infection, NSAID use, or acid hypersecretion. FSH receptors are essentially absent from gastroduodenal mucosal tissue, and the FSH/FSHR/cAMP signalling cascade has no established intersection with the mechanisms underlying gastroduodenal inflammation.

The high TxGNN score (99.65%) most likely reflects multi-step indirect edges in the knowledge graph — for example, pathways connecting inflammation → cytokines → hormonal regulation → FSH axis — rather than a direct mechanistic relationship. This pattern is consistent with graph noise in sparsely connected regions of the knowledge graph and does not translate into a biologically plausible repurposing hypothesis. This same assessment applies broadly to the other nine indications in this batch: migraine (ranks 2, 4, 8), peptic ulcer disease (rank 3), Raynaud disease (rank 5), pulmonary hypertension (rank 6), kyphoscoliotic heart disease (rank 7), atrophoderma vermiculata (rank 9), and peptic esophagitis (rank 10) — all conditions where FSH receptor biology has no established therapeutic role.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications for Corifollitropin alfa in this batch are classified at Evidence Level L5 — model prediction only — with zero supporting clinical trials or directly relevant literature across the entire candidate set. The top-ranked prediction (gastroduodenitis) has no plausible mechanistic basis: FSH receptor expression is confined to reproductive tissues and does not intersect with the pathophysiology of any of the 10 predicted diseases.

**To proceed, the following is needed:**
- Retrieve full MOA and safety data from DrugBank API (DB09066) and TFDA SmPC to complete the baseline drug profile before any further evaluation
- Conduct a mechanistic plausibility pre-screen for all 10 predicted indications prior to committing additional evidence collection resources
- Flag and filter 20 PubMed records retrieved for the "migraine with or without aura susceptibility" indication (rank 8): all articles address epilepsy genetics and neuropharmacology and are unrelated to Corifollitropin alfa — these are false positives from the current evidence collection system
- Consider deprioritising this candidate in the current repurposing pipeline; resources would be better directed toward candidates with L3 or higher evidence levels and demonstrable mechanistic links to their predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

