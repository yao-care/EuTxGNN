---
layout: default
title: Tecovirimat
parent: AI Predictions (L5)
nav_order: 591
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tecovirimat: predicted new indication Hordeolum (evidence level L5). Approved use: Smallpox…"
monitor_inn: "Tecovirimat"
predicted_indications: ["hordeolum", "vibrio infectious disease", "Klebsiella infectious disease", "noma", "escherichia coli infection", "Newcastle disease", "idiopathic recurrent and disabling cutaneous herpes", "equine infectious anemia", "Astroviridae infectious disease", "Arterivirus infectious disease"]
---

# Tecovirimat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tecovirimat: From Smallpox, Monkeypox and Cowpox to Hordeolum
{: .text-alpha }

## One-Sentence Summary

Tecovirimat is an antiviral originally used to treat smallpox, monkeypox (mpox) and cowpox, and to treat complications of vaccinia virus replication after smallpox vaccination.
The TxGNN model predicts it may be effective for **hordeolum** (a stye of the eyelid), but there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone and is likely a network-prediction artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smallpox, monkeypox and cowpox in adults and children weighing at least 13 kg; complications of vaccinia virus replication after smallpox vaccination |
| Predicted New Indication | Hordeolum |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Tecovirimat is known to be a narrow-spectrum antiviral that inhibits the orthopoxvirus VP37 envelope-wrapping protein. Its efficacy has been established against orthopoxvirus infections, not against other pathogen groups.

The predicted indication does not fit this mechanism. Hordeolum is typically a bacterial infection (usually *Staphylococcus aureus*) of an eyelid gland. Bacteria have no VP37 homolog, and tecovirimat has no known antibacterial activity. The high TxGNN score (99.66%) is therefore most likely a network-prediction artifact rather than a true repurposing signal.

The same pattern holds for the other top-ranked predictions: bacterial infections (Vibrio, Klebsiella, *E. coli*, noma) and unrelated viruses (herpes, Newcastle disease, equine infectious anemia, astroviruses, arteriviruses). None has a plausible mechanistic link to tecovirimat.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for hordeolum.

Among the other ranked predictions, a few papers were retrieved, but all concern tecovirimat in mpox, which is the original indication, and none supports the predicted indication.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005248 (cancelled) | Tecovirimat SIGA | Not specified | Smallpox, monkeypox and cowpox in adults and children weighing at least 13 kg; complications of vaccinia virus replication after smallpox vaccination... |

## Safety Considerations

Please refer to the SmPC for safety information. No interaction data were found for this drug in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hordeolum has no clinical, literature or mechanistic support. A bacterial eyelid infection cannot plausibly be treated by a narrow-spectrum orthopoxvirus inhibitor. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Warnings and contraindications from the EMA package insert, which are required before any safety screening
- Any experimental evidence of activity in the predicted indication; without it, this candidate should not advance
- Confirmation of the reason for the authorization cancellation and the current EU availability of tecovirimat
- If repurposing is still of interest, a review of lower-ranked predictions that are viral and closer to orthopoxviruses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

