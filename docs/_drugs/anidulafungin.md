---
layout: default
title: Anidulafungin
parent: AI Predictions (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Anidulafungin: predicted new indication Impetigo (evidence level L5). Approved use: Treatment of invasive candidiasis in adults and paediatric patients a…"
---

# Anidulafungin
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

# Anidulafungin: From Invasive Candidiasis to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal, originally used to treat invasive candidiasis in adults and children aged 1 month to under 18 years.
The TxGNN model predicts it may be effective for **impetigo**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
It is a model-only prediction without a plausible mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of invasive candidiasis in adults and paediatric patients aged 1 month to < 18 years |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, anidulafungin is an echinocandin that inhibits fungal 1,3-beta-D-glucan synthase, and its efficacy in invasive candidiasis is established.

That target does not explain the prediction. Impetigo is caused mainly by *Staphylococcus aureus* and *Streptococcus pyogenes*. These bacteria lack 1,3-beta-D-glucan synthase, and anidulafungin has no antibacterial activity. The high score (0.989) therefore reflects a computational association only, and it is not backed by any trial or publication.

The other top-ranked predictions show the same pattern. Bullous impetigo, staphylococcal scalded skin syndrome, hordeolum and Clostridium infections are bacterial diseases. The mesothelioma and pleural tumour predictions have no known link to the antifungal target. The one partial exception is pleural empyema, which has a pharmacokinetic study showing that the drug reaches pleural fluid. That study does not show efficacy, and any Candida-related use is already covered by the existing indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for impetigo.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000788 (cancelled) | Ecalta | Not specified | Treatment of invasive candidiasis in adults and paediatric patients aged 1 month to < 18 years. |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): liver disease and gallbladder disease.
- **Drug Interactions**: One interaction was found, with cyclosporine (Minor, DDInter).

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The impetigo prediction rests only on a model score. The drug has no antibacterial activity, and no trials or literature exist. The product's only EU authorization is also cancelled.

**To proceed, the following is needed:**
- A plausible mechanistic rationale, or in vitro evidence of activity against the causative organisms. Without this, impetigo is unlikely to justify further work.
- Mechanism of action data and SmPC warnings and contraindications, to allow safety screening.
- Clarification of the regulatory situation, given the cancelled authorization.
- If any follow-up is warranted, consider the pleural empyema signal (Candida-associated cases only). This would need clinical efficacy data, not just pharmacokinetics.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

