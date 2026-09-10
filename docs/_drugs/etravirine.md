---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Etravirine is a second-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) known from the evidence pack to be used against HIV-1 infection, though its formal original-indication and MOA fields are not yet populated in this dataset. The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary indication — but this pairing is explicitly flagged in the pack itself as a topological artifact, with **0 clinical trials** and **0 publications** supporting it. Overall evidence for this specific candidate is essentially absent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in regulatory licenses (drug not marketed); known class indication per evidence pack: HIV-1 infection (NNRTI) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded elsewhere in the pack — clinical trial titles and literature discussing etravirine alongside darunavir, raltegravir, and rilpivirine in HIV-1 regimens — etravirine is known to act as an NNRTI that directly inhibits HIV-1 reverse transcriptase.

The top-ranked prediction in this pack, Feline Acquired Immunodeficiency Syndrome (FIV), is a lentiviral infection in cats that is structurally analogous to HIV only at a coarse level. The pack's own rationale states this directly: *"FIV reverse transcriptase structure differs significantly from HIV-1, and cross-reactivity of NNRTI-class drugs against FIV RT is not supported by literature — this is purely a TxGNN topological similarity prediction."* In other words, the model appears to be scoring this pairing highly because of graph proximity between HIV and FIV nodes, not because of any demonstrated pharmacological activity. It is also a veterinary indication, which is outside the scope of a human drug repurposing evaluation.

Within the same pack, two lower-ranked predictions — "AIDS related complex" (rank 4, L2) and "congenital human immunodeficiency virus" (rank 5, L3) — do carry real clinical trial and literature support. However, both are explicitly characterized in their own rationale text as extensions of etravirine's already-known HIV-1 mechanism (pre-AIDS disease stages and vertical transmission prophylaxis) rather than genuinely novel indications. They are noted here for context but are not the subject of this report's headline pairing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

No marketing authorizations are on record for this product (`market_status`: Not Marketed, `total_licenses`: 0). No dosage form or approved indication data is available to tabulate.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The headline prediction (FIV) has no clinical trial or literature support, is explicitly identified in the source data as a topological artifact rather than a mechanistically grounded hypothesis, and targets a veterinary rather than human population — it does not meet the bar for further evaluation. Within the broader candidate pack, the only predictions with meaningful evidence (AIDS related complex, congenital HIV) are not novel indications but extensions of etravirine's existing HIV-1 mechanism.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001) preventing any S1 safety assessment
- Confirmed mechanism of action data from DrugBank (DG002)
- A mechanistically credible, human-relevant novel indication hypothesis, since the current top-ranked candidate does not qualify
- If HIV-adjacent indications (e.g., perinatal HIV prophylaxis) are of interest, these should be scoped as label-extension questions rather than repurposing candidates, given the mechanistic overlap already noted in the source rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

