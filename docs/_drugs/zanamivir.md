---
layout: default
title: Zanamivir
parent: AI Predictions (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

> Zanamivir is a neuraminidase inhibitor originally developed for the treatment of influenza A and B infection.
> The TxGNN model predicts it may be effective for **Pyelonephritis**, but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the Evidence Pack's own mechanistic review finds no credible biological rationale for this connection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (inferred from clinical trial titles and mechanism-of-action description in the Evidence Pack; no EU-approved indication text is on file) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field is marked as a data gap, but the Evidence Pack's rationale text consistently describes Zanamivir as a viral neuraminidase inhibitor: it blocks the neuraminidase enzyme on the surface of influenza A and B viruses, preventing newly formed virions from being released from infected respiratory epithelial cells. This mechanism is strictly dependent on the virus expressing a sialic-acid-cleaving neuraminidase — a target found in orthomyxoviruses (influenza) but not in most other pathogens.

Pyelonephritis, the top-ranked predicted indication, is a bacterial infection of the renal parenchyma, most commonly caused by ascending gram-negative organisms such as *Escherichia coli*. Its pathogenesis involves bacterial adhesion, ascent through the urinary tract, and host inflammatory response — none of which involve a neuraminidase-dependent viral replication cycle. There is no shared drug target, tissue tropism, or pathophysiological pathway between influenza and pyelonephritis that would support repurposing on mechanistic grounds.

The Evidence Pack itself flags this explicitly: the `repurposing_rationale.mechanistic_link` for this candidate states that pyelonephritis has "no neuraminidase-dependent mechanism and no credible mechanistic link" to Zanamivir. The same pattern repeats across the other nine ranked candidates in this pack (inborn errors of tyrosine/phenylalanine metabolism, Pierre Robin syndrome, dengue, aspergillosis, HIV, Legionnaires' disease, schistosomiasis) — each is annotated as mechanistically implausible or, in the case of "susceptibility to HIV infection," associated with clinical trials and literature that actually describe influenza studies mislabeled under the wrong disease tag. This suggests the ranked list reflects knowledge-graph proximity artifacts in TxGNN rather than genuine biological signal, and it should be weighed accordingly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorization is on record for Zanamivir in this Evidence Pack (market status: Not Marketed; 0 authorizations listed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (pyelonephritis) has no supporting clinical trials or literature, no plausible shared mechanism with Zanamivir's known neuraminidase-inhibitor activity, and the drug currently has no EU marketing authorization. The Evidence Pack's own mechanistic review independently reaches the same "no credible link" conclusion, and this pattern of implausibility extends across the rest of the ranked candidate list for this drug, further undermining confidence in the prediction set as a whole.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data (original_moa is currently a data gap)
- TFDA/EMA label warnings and contraindications (currently a blocking data gap)
- Independent mechanistic or preclinical evidence specifically linking neuraminidase inhibition to renal/urinary tract infection pathophysiology
- Correction of the disease-evidence mapping error observed in the "susceptibility to HIV infection" candidate (rank 8), where attached trials/literature describe influenza, not HIV
- Regulatory status confirmation (EU authorization data currently absent)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

