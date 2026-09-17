---
layout: default
title: Rasburicase
parent: AI Predictions (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Tumor Lysis Syndrome–Associated Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

> Rasburicase is a recombinant urate-oxidase enzyme conventionally used to manage hyperuricemia in tumor lysis syndrome (TLS); this specific use is not captured in the current dataset, which contains no `original_moa` or `original_indications` entries.
> The TxGNN model's top prediction is **Renal Hypouricemia**, but expert review of the pack's own rationale flags this as **directionally contradictory** — the drug lowers uric acid, while renal hypouricemia is a *low*-uric-acid disorder — suggesting a likely false-positive from graph-embedding proximity rather than genuine pharmacological plausibility.
> **Zero clinical trials and zero publications** currently support any of the top 10 predicted indications; all are pure model output (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in this dataset (`original_indications` empty, `original_moa` = Data Gap). Known clinical use: hyperuricemia prophylaxis/treatment in tumor lysis syndrome (TLS). |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% (0.999872) |
| Evidence Level | L5 — model prediction only, no clinical trials or literature |
| EU Market Status | ✗ Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset (`original_moa`: Data Gap). Based on known clinical information, rasburicase is a recombinant urate-oxidase enzyme that converts uric acid to allantoin, and is used to **lower** serum uric acid in patients at risk of tumor lysis syndrome.

Critically, the evidence pack's own mechanistic analysis flags the top prediction — **renal hypouricemia** — as biologically implausible in the wrong direction: renal hypouricemia is caused by a *deficiency* of urate reabsorption (URAT1/GLUT9 transporter defects) and results in **abnormally low**, not high, serum uric acid. Administering a uric-acid-lowering enzyme to a patient who already has pathologically low uric acid would be expected to worsen rather than treat the condition. The evidence pack explicitly attributes this to a suspected artifact of the TxGNN knowledge-graph embedding space — proximity clustering around "uric acid"-related nodes — rather than a genuine pharmacological signal.

By contrast, rank 2 (**HGPRT partial deficiency**, e.g., Kelley-Seegmiller syndrome) shows the mechanistically *correct* direction: this purine salvage pathway defect causes chronic hyperuricemia/gout, which a uric-acid-lowering enzyme could plausibly address. However, this candidate also has zero supporting clinical trials or literature. Ranks 3–8 (hepatic/portal vascular diseases) and ranks 9–10 (renal tubular acidosis, phenylalanine metabolism disorders) are all assessed in the pack as having no credible mechanistic link to urate-oxidase activity, and likely reflect disease-node clustering noise in the graph rather than true repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Rasburicase has **no EU marketing authorizations** recorded in this dataset (`market_status`: Not marketed, `total_licenses`: 0, `licenses`: empty). No product/dosage-form table can be generated.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: `key_warnings`, `contraindications`, and drug interaction data are all flagged as Data Gaps in this pack. DG001 (TFDA label warnings/contraindications) is classified as a **Blocking** gap — it prevents this candidate from entering the S1 safety pre-screening stage.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (renal hypouricemia) is mechanistically contradictory — the drug's known pharmacology (lowering uric acid) runs opposite to the disease's pathophysiology (already-low uric acid) — and is assessed as a likely false positive from knowledge-graph artifact rather than a real signal. No clinical trials, no literature, no EU marketing authorization, and a **Blocking** data gap on safety labeling (DG001) mean this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/EMA label warnings and contraindications) before any S1 safety pre-screening
- Resolve DG002 (confirmed MOA from DrugBank) to properly assess mechanistic plausibility
- If pursuing a repurposing hypothesis for this drug, **re-evaluate rank 2 (HGPRT partial deficiency / Kelley-Seegmiller syndrome)** instead of rank 1 — it is the only top-10 candidate with a mechanistically coherent (correct-direction) rationale, though it still requires primary clinical/literature evidence generation
- Independent review of whether ranks 1, 3–8 represent a systematic false-positive pattern (uric-acid node / hepatic-disease node clustering) in this TxGNN model version, to avoid similar misleading high-score predictions for other drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

