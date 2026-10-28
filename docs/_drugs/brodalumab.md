---
layout: default
title: Brodalumab
parent: AI Predictions (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Brodalumab: predicted new indication Strongyloidiasis (evidence level L5). Approved use: Moderate to severe plaque psoriasis in adult patients who are candida…"
monitor_inn: "Brodalumab"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "optic perineuritis", "isolated optic neuritis", "chronic relapsing inflammatory optic neuropathy", "recurrent idiopathic neuroretinitis", "episcleritis periodica fugax", "nodular episcleritis"]
---

# Brodalumab
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

## Brodalumab: From Plaque Psoriasis to Strongyloidiasis
{: .text-alpha }

## One-Sentence Summary

Brodalumab is an IL-17 receptor A (IL-17RA) blocking antibody, originally used to treat moderate to severe plaque psoriasis in adults who are candidates for systemic therapy.
The TxGNN model predicts it may be effective for **strongyloidiasis** with a very high score, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe plaque psoriasis in adult patients who are candidates for systemic therapy |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, brodalumab blocks IL-17RA signaling, which is why it is effective in psoriasis, a disease driven by IL-17-mediated inflammation.

The link to strongyloidiasis is weak. Host defense against helminths such as *Strongyloides* is driven mainly by type 2 immunity (IL-4, IL-5, IL-13), so blocking IL-17 has no obvious therapeutic rationale. The high TxGNN score appears to be a model output without biological support.

For context, the other top-ranked predictions (all also Hold) are mostly eye-related inflammatory conditions, such as optic neuritis variants, episcleritis, and a broad "eye disease" category. Among these:
- Immune-mediated optic and ocular inflammation may involve Th17 cells, giving a theoretical but unproven link.
- The "eye disease" literature does not show therapeutic benefit. It includes a case report of Behçet's disease arising after brodalumab initiation (a possible paradoxical reaction) and a pharmacovigilance analysis of drug-associated uveitis.
- Vitamin deficiency disorder and von Hippel anomaly have no identifiable mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for strongyloidiasis.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003959 (cancelled) | Kyntheum | Not specified | Moderate to severe plaque psoriasis in adult patients who are candidates for systemic therapy |

## Safety Considerations

- **Knowledge-graph contraindication signals**: Crohn disease, inflammatory bowel disease, and Crohn's colitis. These come from drug-disease edges in the TxGNN knowledge graph, not from label text, and should be verified against the SmPC.
- **Drug Interactions**: 68 interactions were identified. Examples include:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, BCG live vaccine (Tice substrain)
  - **Moderate**: roflumilast, alefacept, alemtuzumab, anakinra, canakinumab, tetanus toxoid, and several live or other vaccines (anthrax, adenovirus, cholera, and others)
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride)
- Overall, the combination with other immunosuppressants and with live vaccines deserves particular caution.

Please refer to the SmPC for warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongyloidiasis prediction has a high model score but no clinical or literature support and no plausible mechanism, since helminth defense depends on type 2 rather than IL-17 immunity. Blocking IL-17 could even be undesirable in an infectious setting. In addition, the only EU authorization has been cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) and a mechanistic assessment of IL-17RA blockade in helminth infection
- Warnings and contraindications from the SmPC, which are currently missing and block safety screening
- Preclinical or clinical evidence in strongyloidiasis; if none exists, consider prioritizing candidates with better support, such as immune-mediated ocular inflammation, after careful review of the paradoxical-reaction and uveitis signals
- Review of the Crohn disease and inflammatory bowel disease contraindication signal and the immunosuppressant and live-vaccine interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

