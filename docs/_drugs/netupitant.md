---
layout: default
title: Netupitant
parent: AI Predictions (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Netupitant
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

# Netupitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Netupitant is a highly selective NK1 (Substance P) receptor antagonist, used clinically as part of a fixed-dose combination for the prevention of chemotherapy-induced nausea and vomiting.
> The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
> but this prediction is currently supported by **no clinical trials** and **no published literature** — it is a pure model output with no identifiable mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (netupitant is clinically an NK1 antagonist antiemetic, used in combination therapy) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.35% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the supporting rationale text that accompanies the predictions, netupitant is a highly selective NK1 (Substance P) receptor antagonist. Its established pharmacology relates to blocking Substance P signaling in the central nervous system's vomiting reflex pathway, which is why it is used as an antiemetic.

For the top-ranked predicted indication, nephrogenic syndrome of inappropriate antidiuresis (NSIAD), the model itself flags an important caveat: NSIAD is driven by aberrant vasopressin (AVP) receptor signaling, and there is no known pharmacological interaction between NK1 antagonism and the AVP receptor pathway. In other words, the high TxGNN score (98.35%) appears to reflect a statistical/embedding-space association within the knowledge graph rather than a biologically plausible mechanism.

Given the absence of any mechanistic rationale, clinical trial, or literature evidence for this specific pairing, this candidate should be treated as a hypothesis-generating signal only, not a basis for further clinical investigation at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Netupitant is currently **not marketed** in this region and has no recorded marketing authorizations, so no authorization table can be produced.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA-equivalent label warnings/contraindications and detailed MOA data are flagged as outstanding data gaps — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (NSIAD) has an evidence level of L5 — a model score with no clinical trials, no literature, and, per the model's own rationale, no identifiable mechanistic link to netupitant's known pharmacology. There is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank (currently a Blocking/High-severity data gap — DG002)
- Official label warnings/contraindications (currently a Blocking data gap — DG001), required before any S1 safety pre-screen
- Independent mechanistic or preclinical evidence linking NK1 antagonism to AVP-pathway disorders before considering this indication further
- If pursuing repurposing at all, migraine disorder (rank 3, score 97.5%) has a biologically plausible rationale via Substance P/NK1 involvement in trigeminovascular activation — however, prior NK1 antagonists (lanepitant, aprepitant) failed in migraine trials, so this should be treated as a research question rather than a development candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

