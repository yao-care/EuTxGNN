---
layout: default
title: Lusutrombopag
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

Using no additional skill invocation — this is a direct content-generation task fully specified by the provided report template; I'll apply it directly to the evidence pack.

# Lusutrombopag: Original Indication Unconfirmed → Predicted Application in Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

> Lusutrombopag's original approved indication and detailed mechanism of action are not yet documented in this evidence pack (both flagged as data gaps, one of them **Blocking**). The TxGNN model's top prediction is **Hereditary Thrombocytopenia with Normal Platelets** (score 99.995%), but this is supported by **zero clinical trials** and **zero publications** — the prediction currently rests entirely on the AI model's knowledge-graph score.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | **Not available** — no regulatory license or approved indication text on file (Blocking data gap, DG001) |
| Predicted New Indication | Hereditary Thrombocytopenia with Normal Platelets *(see caveat below — disease name is internally contradictory)* |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | **L5** (model prediction only, no clinical/literature support) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Lusutrombopag is not available in the structured drug record (data gap DG002, High severity), and no original approved indication is on file for this evidence pack. However, the TxGNN rationale text generated alongside each prediction independently identifies Lusutrombopag as a **thrombopoietin receptor agonist (TPO‑RA)** — a drug class that stimulates megakaryocyte maturation and raises platelet counts. This class-level mechanism is the implicit basis for the model linking Lusutrombopag to a cluster of platelet-related phenotypes.

Looking across all 10 ranked predictions, three distinct mechanistic tiers emerge, and the evidence pack's own rationale text is candid about which ones hold up:

- **Quantitatively plausible (ranks 1–3):** hereditary thrombocytopenia with normal platelets, macrothrombocytopenia with mitral valve insufficiency, and transient neonatal thrombocytopenia are all disorders of *low platelet count*, which is mechanistically consistent with a TPO‑RA's known pharmacology.
- **Mechanistically mismatched (ranks 4–5):** dense granule disease and platelet storage pool deficiency are disorders of platelet *function* (granule content), not platelet *number*. The rationale explicitly states that increasing platelet production cannot correct a storage/secretion defect — these are flagged as poor mechanistic fits despite high model scores.
- **Likely graph noise (ranks 6–10):** amyotrophic lateral sclerosis and related neuromuscular/neurodevelopmental/skeletal conditions have no known TPO/MPL receptor pathway involvement. The rationale itself describes these as probable knowledge-graph artifacts (indirect node connections) rather than genuine pharmacological hypotheses.

**Important caveat on the top-ranked prediction:** the rationale for rank 1 explicitly flags that "hereditary thrombocytopenia with **normal platelets**" is a self-contradictory disease label, most likely an ontology/naming error in the underlying disease vocabulary rather than a real, distinct clinical entity. This should be resolved before any further evaluation of this specific candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorizations are on file. `market_status = "未上市" (Not Marketed)`, `total_licenses = 0`. Lusutrombopag currently has no recorded EU regulatory presence in this evidence pack.

---

## Other Predicted Indications (Ranks 2–10, Supplementary)

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------|-----------------|-----------------|------|
| 2 | Macrothrombocytopenia with mitral valve insufficiency | 99.995% | pending | pending | Scoring not yet completed in this evidence pack |
| 3 | Transient neonatal thrombocytopenia | 99.995% | L5 | Hold | Self-limiting condition; no neonatal safety/PK data for TPO‑RA class |
| 4 | Dense granule disease | 99.995% | L5 | Hold | Functional (not quantitative) platelet disorder — mechanism mismatch |
| 5 | Platelet storage pool deficiency | 99.958% | L5 | Hold | Same mechanism mismatch as rank 4 |
| 6 | Amyotrophic lateral sclerosis | 99.948% | L5 | Hold | No known TPO/MPL pathway link; likely graph noise |
| 7 | Lower motor neuron syndrome, late-adult onset | 99.948% | L5 | Hold | Likely graph noise |
| 8 | ALS, susceptibility to | 99.946% | L5 | Hold | Genetic susceptibility category, not a treatable disease entity |
| 9 | Bilateral parasagittal parieto-occipital polymicrogyria | 99.945% | L5 | Hold | Cortical malformation; no mechanistic link |
| 10 | Axial spondylometaphyseal dysplasia | 99.943% | L5 | Hold | Skeletal dysplasia; no mechanistic link |

---

## Safety Considerations

⚠️ **Blocking data gap (DG001):** TFDA/SmPC-level warnings and contraindications for Lusutrombopag are not yet available in this evidence pack. This is classified as **Blocking severity** — it directly prevents entry into Stage 1 (S1) safety pre-screening. Drug interaction (DDI) query also returned no results (`query_status = not_found`).

Please refer to the SmPC for safety information once obtained; do not proceed with clinical or regulatory evaluation until this gap is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are supported solely by TxGNN model scores with zero clinical trials and zero literature (L5 across the board). The single highest-ranked candidate carries a likely ontology-naming error, and half of the remaining candidates are flagged by the evidence pack's own mechanistic rationale as either mismatched (functional vs. quantitative platelet disorders) or probable knowledge-graph noise (ALS/neurodevelopmental/skeletal conditions). Combined with a **Blocking** safety data gap, this candidate cannot advance past S0.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/SmPC warnings and contraindications
- Resolve DG002: confirm Lusutrombopag's MOA via DrugBank API
- Obtain the confirmed, regulator-sourced original approved indication(s) for Lusutrombopag
- Clarify whether "hereditary thrombocytopenia with normal platelets" is a valid distinct ontology entry or a labeling/data error before further evaluating rank 1
- If pursuing rank 3 (transient neonatal thrombocytopenia), commission a dedicated neonatal safety/PK literature search before any advancement beyond S0
- Deprioritize ranks 4–10 from further research resource allocation given mechanistic mismatch or likely graph-noise status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

