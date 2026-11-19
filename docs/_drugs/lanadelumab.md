---
layout: default
title: Lanadelumab
parent: AI Predictions (L5)
nav_order: 350
evidence_level: L5
indication_count: 9
monitor_inn: "Lanadelumab"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
last_modified_at: 2026-11-12
description: "Lanadelumab: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). Approved use: Takhzyro is indicated for routine prevention of recurrent attacks of…"
---

# Lanadelumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Lanadelumab: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Lanadelumab is a monoclonal antibody that inhibits plasma kallikrein, and it is authorised in the EU for routine prevention of recurrent hereditary angioedema attacks.
The TxGNN model predicts it may be relevant to **serpinopathy with toxic serpin polymerization**, but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Takhzyro is indicated for routine prevention of recurrent attacks of hereditary angioedema (HAE) in patients aged 2 years and older. |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lanadelumab: "Lanadelumab-flyo is a fully human monoclonal antibody (IgG1/κ-light chain) that binds plasma kallikrein and inhibits its proteolytic activity. Plasma kallikrein is a protease that cleaves high-molecular-weight-kininogen (HMWK) to generate cleaved HMWK (cHMWK) and bradykinin, a potent vasodilator that increases vascular permeability resulting in swelling and pain associated with HAE." ([DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8), label version 2026-09-18; accessed 2026-11-19.) From the target information that is available, lanadelumab binds plasma kallikrein (KLKB1) and inhibits the kallikrein-bradykinin axis. The antibody is reported not to bind prekallikrein.

The high TxGNN score probably reflects network proximity between the serpin pathway (SERPING1/C1 inhibitor) and the serpinopathy disease class, rather than an independent mechanistic rationale. Toxic serpin polymerization is a gain-of-function intracellular process, and inhibiting plasma kallikrein would not be expected to address it. The prediction should therefore be treated as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/004806 | Takhzyro | lanadelumab | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: One pharmacology-based entry is recorded, describing the drug's own target, plasma kallikrein (KLKB1). It is not a drug-drug interaction in the clinical sense.
- **Coagulation considerations**: Lanadelumab may prolong aPTT through effects on the intrinsic pathway. This is a theoretical concern in patients with bleeding disorders.

For full warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only, with no clinical trials or publications addressing this disease. The mechanism of lanadelumab (plasma kallikrein inhibition) does not plausibly address toxic serpin polymerization, so the evidence level is L5.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- A clear mechanistic hypothesis showing how plasma kallikrein inhibition could affect toxic serpin polymerization
- Preclinical studies in relevant disease models
- Review of EMA label warnings and contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

