---
layout: default
title: Degarelix
parent: AI Predictions (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Degarelix: predicted new indication Hypertrichosis (evidence level L5). Approved use: Treatment of adult male patients with advanced hormone-dependent pros…"
monitor_inn: "Degarelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
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

# Degarelix: From Advanced Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix is a gonadotrophin releasing hormone (GnRH) antagonist, originally used to treat advanced hormone-dependent prostate cancer.
The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** currently support this direction. The prediction rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of adult male patients with advanced hormone-dependent prostate cancer |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Degarelix is known as a GnRH receptor antagonist. It suppresses luteinising hormone (LH) and follicle-stimulating hormone (FSH), which lowers testicular androgen production. This is the basis for its use in hormone-dependent prostate cancer.

The link to the predicted indication is weak. Hypertrichosis is generally not androgen-driven, unlike hirsutism, which is a different condition. Any plausible mechanism would be indirect, such as reducing androgen-sensitive hair growth in a hirsutism-like presentation. The very high TxGNN score appears to be a graph-based prediction without clinical or literature support.

The other top predictions look similarly unsupported. Several are congenital or genetic hair and malformation conditions (Ambras syndrome, Dandy-Walker-related syndromes, isolated hair shaft abnormalities, familial trichomegaly). Others are urticaria types, where degarelix's own hypersensitivity reactions raise a safety concern rather than supporting benefit. Familial male-limited precocious puberty is driven downstream of the GnRH-LH axis, so a GnRH antagonist is not expected to work.

The one prediction with a coherent mechanism is **central precocious puberty** (rank 9, evidence level L4). GnRH suppression is the established principle there, though treatment normally uses GnRH agonists. It remains a research question, because no paediatric data, trials or literature were found for degarelix.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000986 | Firmagon (cancelled) | Not specified | GnRH antagonist for adult male patients with advanced hormone-dependent prostate cancer; high-risk localised and locally advanced hormone-dependent prostate cancer in combination with radiotherapy; neo-adjuvant tre... |
| EMEA/H/C/006048 | Degarelix Accord (cancelled) | Not specified | GnRH antagonist for adult male patients with advanced hormone-dependent prostate cancer; high-risk localised and locally advanced hormone-dependent prostate cancer in combination with radiotherapy; neo-adjuvant tre... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (GnRH antagonist), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease, potassium deficiency disease.
- **Drug Interactions**: 100 interactions were found in the interaction screen. Examples of the **Major** ones are cisapride and dolasetron, consistent with QT-prolongation concerns. Many **Moderate** interactions include clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, famotidine and loperamide. Bowel-preparation and laxative products (bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, magnesium citrate and others) also appear at Moderate level. Metronidazole is **Minor**.
- Degarelix has been associated with injection-site and hypersensitivity reactions, which matters for the urticaria predictions.

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of hypertrichosis has no clinical trials, no literature and only a weak mechanistic link, so the evidence level is L5. No currently valid EU marketing authorization exists for degarelix, and the safety profile includes QT-related signals and many drug interactions.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) to support a mechanistic-link analysis
- EMA SmPC warnings and contraindications, which block safety screening
- Any preclinical or clinical evidence for hypertrichosis, or a refocus on central precocious puberty as a research question, including paediatric safety data and a comparison with GnRH agonists
- Clarification of the cancelled EU authorization status and of the available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

