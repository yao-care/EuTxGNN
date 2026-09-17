---
layout: default
title: Oseltamivir
parent: AI Predictions (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Oseltamivir
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

# Oseltamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

> Oseltamivir is a neuraminidase inhibitor established for the **treatment and prophylaxis of influenza**.
> The TxGNN model predicts it may be effective for **Pyelonephritis**, but this candidate is currently supported by **0 clinical trials** and only **1 loosely related publication**, which the evidence review judges to be search noise rather than a genuine mechanistic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (treatment/prophylaxis) — based on the drug's established pharmacological class (neuraminidase inhibitor); no jurisdiction-specific approved label text is available in this evidence pack (see Data Gap DG001) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on information embedded in the surrounding evidence (e.g., mechanistic notes on related candidates in this batch), oseltamivir is known to act as a **neuraminidase inhibitor** that blocks influenza viral replication — this is its established, well-documented pharmacology, not a data-gap item for the drug class itself.

Pyelonephritis is a bacterial urinary tract/renal infection with no established pathophysiological link to viral neuraminidase inhibition. The only literature item attached to this prediction (PMID 26033556) is a 2015 review on **influenza during pregnancy**, which discusses obstetric complications of seasonal flu — it does not address renal or urinary tract infection, oseltamivir's antibacterial activity, or any mechanism connecting the two conditions.

Given the absence of clinical trials, absence of any pyelonephritis-specific literature, and the review's own assessment that this is likely an embedding-similarity artifact rather than a real biological hypothesis, the mechanistic rationale for this prediction is **not supported**. The high TxGNN score reflects graph-based similarity in the knowledge graph, not verified pharmacological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26033556](https://pubmed.ncbi.nlm.nih.gov/26033556/) | 2015 | Review | Presse médicale (Paris, France : 1983) | Reviews influenza risk and management during pregnancy (increased pneumonia/hospitalization risk); does not address pyelonephritis, renal infection, or an antibacterial mechanism for oseltamivir — judged as off-topic to this indication pairing |

---

## EU Market Information

No marketing authorizations are currently recorded for oseltamivir in this jurisdiction (market status: Not Marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (pyelonephritis) has no clinical trial support and its single attached publication is unrelated to the proposed indication. The evidence review classifies this pairing as likely knowledge-graph noise rather than a testable pharmacological hypothesis, so it does not meet the bar for further evaluation at this time.

**To proceed, the following is needed:**
- A validated mechanistic rationale connecting neuraminidase inhibition (or any other oseltamivir target) to bacterial pyelonephritis/UTI pathophysiology
- Targeted literature search specifically on oseltamivir and urinary tract/renal infection outcomes (the current hit was retrieved on general "influenza" text overlap)
- TFDA/EMA label data — safety warnings and contraindications (Data Gap DG001, Blocking) and formal MOA documentation (Data Gap DG002, High) before any S1 safety screening can begin

**Note for decision-makers:** Within this same evidence pack, a lower-ranked TxGNN candidate — **pneumonia** (rank 8, score 92.1%) — shows substantially stronger support (L1 evidence, multiple completed Phase 3 RCTs, "Proceed with Guardrails" recommendation) and may warrant prioritization over this top-ranked but poorly supported pyelonephritis candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

