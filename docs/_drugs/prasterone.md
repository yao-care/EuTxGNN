---
layout: default
title: Prasterone
parent: AI Predictions (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From No Approved Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Prasterone (DHEA) has no recorded original indication in this evidence pack and is not currently marketed in this jurisdiction. The TxGNN model predicts a possible link to **Heparin Cofactor 2 Deficiency**, but this is a Level 5 (L5) prediction with **zero clinical trials** and **zero supporting publications**, and the model's own generated rationale explicitly flags the score as a graph-embedding artifact rather than a validated biological mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file; drug is not currently marketed in this jurisdiction |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the limited information present in this evidence pack, Prasterone (DHEA) is described as a gonadal steroid hormone precursor. No approved original indication or licensing history is on file, so it is not possible to compare this candidate against an established clinical use case, and no independent MOA source could be verified.

More importantly, the evidence pack's own analysis of the top-ranked prediction states directly that there is **no known mechanistic pathway** connecting DHEA's endocrine metabolism to Heparin Cofactor II (a serine protease inhibitor) gene deficiency. The high TxGNN score is attributed to knowledge-graph proximity between nodes, not to any documented pharmacological or physiological relationship — the rationale text itself describes this as "非生物學依據" (not a biological basis).

A further caution emerges from a lower-ranked but evidence-backed prediction in the same pack: for "thrombophilia" (rank 4, L4), the associated literature describes hyperandrogenic states (e.g., PCOS, Leydig cell tumors) as being **associated with increased thrombotic risk**, not reduced risk. Since DHEA is an androgen precursor, this is a directionally concerning signal — it suggests androgen exposure may exacerbate, rather than treat, disorders of coagulation and clotting-factor regulation. Given that three of the top five predictions in this pack (ranks 1, 2, 3) are inherited clotting-factor deficiencies, this pattern should be treated as a safety caution rather than supportive evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations are on file for Prasterone in this jurisdiction (0 total licenses). The drug is currently listed as not marketed.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Heparin cofactor 2 deficiency) is an L5, AI-only signal with no supporting clinical trials or literature, and the model's own rationale explicitly disclaims a biological basis. Related evidence elsewhere in the pack (thrombophilia, rank 4) points toward androgen excess *increasing* thrombotic risk, which runs counter to using this drug for clotting-factor–related indications.

**To proceed, the following is needed:**
- TFDA/regulatory label data — warnings and contraindications (currently a Blocking gap, DG001)
- Verified mechanism of action (MOA) for Prasterone (DG002)
- Original approved indication and licensing history, since the drug is not currently marketed in this jurisdiction
- Independent preclinical or mechanistic evidence directly linking DHEA/androgen pathways to hemostasis or coagulation-factor regulation before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

