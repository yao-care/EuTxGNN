---
layout: default
title: Ospemifene
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Ospemifene
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

# Ospemifene: From Menopausal Vulvovaginal Atrophy to Leprosy

## One-Sentence Summary

Ospemifene is a selective estrogen receptor modulator (SERM); the evidence pack itself does not confirm an original indication (publicly known use is dyspareunia due to menopausal vulvovaginal atrophy, but this is not documented in the current dataset). The TxGNN model's top prediction is **Leprosy**, but this direction is currently supported by **zero clinical trials and zero relevant literature** — it is a pure model-score prediction with no mechanistic rationale identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (publicly known: dyspareunia due to menopausal vulvovaginal atrophy — unconfirmed here) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the limited information in this evidence pack, Ospemifene is characterized as a **SERM (Selective Estrogen Receptor Modulator)** — this classification is echoed consistently across the rationale text for every predicted indication in this pack, but no further mechanistic detail is provided.

The relationship between the (unconfirmed) original indication and the predicted new indication cannot be meaningfully assessed without MOA data. For leprosy specifically, the evidence pack explicitly states: *"no known mechanistic link — Ospemifene as a SERM has no known intersection with M. leprae infection or immune pathways; under the MOA data gap, no plausible hypothesis can be constructed."*

In short, this prediction is a pure network/model-score output (TxGNN rank 9682 out of the full candidate space) with **no biological hypothesis currently supporting it**. It should be treated as exploratory only, not as a mechanistically grounded repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

This drug is currently **not marketed** in the region covered by this evidence pack (0 authorizations on record), so no license table is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA/regulatory label warnings and contraindications are recorded as a Blocking data gap (DG001) — this drug cannot yet proceed to a formal S1 safety screening stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Leprosy) has no supporting clinical trials, no relevant literature, and no identifiable mechanistic link — the evidence pack's own scoring explicitly assigns L5/S0/Hold. Combined with the Blocking-severity gap in regulatory safety data (DG001) and the High-severity gap in MOA data (DG002), this candidate does not meet the minimum evidence bar to advance.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (resolve DG001 — currently blocking any safety screening)
- Confirmed mechanism of action data via DrugBank or primary literature (resolve DG002)
- Confirmation of the drug's actual original approved indication(s), since `original_indications` is currently empty
- If pursuing repurposing further, prioritize re-screening against indications with at least preliminary mechanistic plausibility (e.g., rheumatoid arthritis or migraine, where an estrogen-pathway hypothesis is at least theoretically stated) rather than leprosy, and independently verify that any retrieved literature is drug-specific rather than keyword-matched noise (as seen in the migraine literature set, which is entirely epilepsy-genetics content unrelated to Ospemifene)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

