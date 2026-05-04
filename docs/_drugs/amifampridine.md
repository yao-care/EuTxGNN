---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine (3,4-diaminopyridine) is a voltage-gated potassium channel (VGKC) blocker approved in the US and EU for Lambert-Eaton Myasthenic Syndrome (LEMS), a rare neuromuscular junction disorder — though it is not currently registered in Taiwan.
The TxGNN model ranks **Glaucoma** as its top predicted new indication with a score of **99.71%**,
however **no clinical trials and no supporting publications** have been identified for this specific repurposing direction, placing it at evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lambert-Eaton Myasthenic Syndrome (LEMS) — not registered in Taiwan |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Amifampridine is a voltage-gated potassium channel (VGKC) blocker. By prolonging action potential duration at presynaptic nerve terminals, it increases calcium influx and enhances acetylcholine release at the neuromuscular junction — the established mechanism underlying its efficacy in LEMS.

In the context of glaucoma, Kv channels expressed in ciliary body epithelial cells are theoretically involved in regulating aqueous humor secretion, the primary determinant of intraocular pressure. This provides a distant mechanistic rationale: Amifampridine-mediated Kv channel blockade could in principle influence aqueous humor production and thereby modulate intraocular pressure.

In practice, however, this mechanistic link is extremely tenuous. No ocular pharmacology or glaucoma-focused research on Amifampridine has been identified. The high TxGNN score likely reflects a non-specific association between potassium channel-related disease nodes in the knowledge graph, rather than a genuine therapeutic relationship. This prediction is most appropriately classified as a potential knowledge graph artifact pending any preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Amifampridine is not registered or marketed in Taiwan. No marketing authorizations were found in TFDA records.

> **Note:** Amifampridine is approved in the United States (Firdapse®, Jacobus Pharmaceutical) and the European Union for the symptomatic treatment of Lambert-Eaton Myasthenic Syndrome in adults. Any future Taiwan registration application would need to reference these international approvals.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Full safety data (key warnings, contraindications) are not available in this evidence pack due to the absence of a TFDA package insert. Clinicians should consult the EMA-approved Summary of Product Characteristics (SmPC) for Firdapse® before any investigational use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN score of 99.71%, the glaucoma prediction carries no supporting clinical trials, no relevant literature, and only a speculative mechanistic connection to VGKC biology in the eye. It does not meet the minimum threshold for further development under current evidence.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank (currently marked as Data Gap) to formally characterize VGKC selectivity and off-target ocular effects
- Commission a targeted literature search for any preclinical studies of 3,4-DAP on intraocular pressure or ciliary body ion transport
- Evaluate whether this TxGNN prediction reflects a true biological signal or a knowledge graph false positive (e.g., non-specific K⁺-channel disease node proximity)

---

> **Prioritization Note:** Among the 10 TxGNN predictions in this evidence pack, the glaucoma prediction has the highest model score but the weakest mechanistic basis. The following predictions warrant closer attention based on mechanistic plausibility:
>
> | Rank | Indication | Score | Evidence Level | Recommendation | Rationale |
> |------|-----------|-------|---------------|----------------|-----------|
> | 7 | Paraneoplastic Limbic Encephalitis | 98.31% | L5 | Research Question | VGKC-complex antibodies (LGI1, CASPR2) overlap with LEMS pathway |
> | 8 | Paraneoplastic Polyneuropathy | 98.26% | L5 | Research Question | Some subtypes share ACh transmission deficits analogous to LEMS |
> | 10 | Paraneoplastic Cerebellar Degeneration | 97.99% | **L4** | Research Question | Two LEMS-focused publications (PMID [15034474](https://pubmed.ncbi.nlm.nih.gov/15034474/), [29386498](https://pubmed.ncbi.nlm.nih.gov/29386498/)) document shared paraneoplastic co-morbidity and VGCC antibody overlap with SCLC-triggered PCD |
>
> Of these, **Paraneoplastic Cerebellar Degeneration (rank 10)** currently represents the strongest repurposing hypothesis: PCD frequently co-occurs with LEMS (both triggered by small cell lung cancer, both associated with VGCC antibodies), and the two existing publications provide indirect mechanistic grounding even though no PCD-directed trials exist yet.

---

*This report is generated for research reference only and does not constitute medical advice. All repurposing candidates require prospective clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

