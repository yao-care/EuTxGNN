---
layout: default
title: Glycopyrronium
parent: AI Predictions (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Glycopyrronium: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Symptomatic treatment of severe sialorrhoea (chronic pathological dro…"
monitor_inn: "Glycopyrronium"
predicted_indications: ["irritable bowel syndrome", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "neurocirculatory asthenia", "migraine disorder", "migraine with brainstem aura", "open-angle glaucoma", "autonomic nervous system disease", "primary hereditary glaucoma", "dysthymic disorder"]
---

# Glycopyrronium
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

## Glycopyrronium: From Severe Sialorrhoea and COPD to Irritable Bowel Syndrome
{: .text-alpha }

## One-Sentence Summary

Glycopyrronium is a peripherally acting antimuscarinic, originally authorised in the EU for severe chronic drooling (sialorrhoea) in children and for maintenance bronchodilator treatment in adults with COPD.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of severe sialorrhoea (chronic pathological drooling) in children and adolescents aged 3 years and older with chronic neurological disorders |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 4 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Glycopyrronium is known as a peripherally acting antimuscarinic. Its efficacy has been shown in sialorrhoea and COPD, both conditions where blocking muscarinic receptors reduces secretions or relaxes airway smooth muscle.

For irritable bowel syndrome, the plausible link is blockade of M3 receptors in gut smooth muscle. This could reduce spasm and hypermotility, in line with other antimuscarinic antispasmodics used in IBS. This link comes only from the TxGNN prediction. No trial or publication was provided to confirm it.

The other top predictions are weaker. Several (migraine, dysthymic disorder, neurocirculatory asthenia) have no credible mechanism, as glycopyrronium crosses the blood-brain barrier poorly. Cauda equina syndrome and obsolete neurogenic bladder are plausible only for symptomatic bladder or bowel control. Open-angle and primary hereditary glaucoma are mechanistically concerning, because antimuscarinics can raise intraocular pressure or precipitate angle closure.

## Clinical Trial Evidence

Currently no related clinical trials registered for irritable bowel syndrome.

## Literature Evidence

Currently no related literature available for irritable bowel syndrome.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003883 | Sialanar (cancelled) | Not specified | Symptomatic treatment of severe sialorrhoea (chronic pathological drooling) in children and adolescents aged 3 years and older with chronic neurological disorders. |
| EMEA/H/C/002691 | Enurev Breezhaler (cancelled) | Not specified | Maintenance bronchodilator treatment to relieve symptoms in adult patients with chronic obstructive pulmonary disease (COPD). |
| EMEA/H/C/002690 | Tovanor Breezhaler (cancelled) | Not specified | Maintenance bronchodilator treatment to relieve symptoms in adult patients with chronic obstructive pulmonary disease (COPD). |
| EMEA/H/C/002430 | Seebri Breezhaler (cancelled) | Not specified | Maintenance bronchodilator treatment to relieve symptoms in adult patients with chronic obstructive pulmonary disease (COPD). |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries. Most listed are of Moderate level, with a few Minor. Examples:
  - Other anticholinergics and antimuscarinics (additive effects): aclidinium, hyoscyamine, homatropine, amitriptyline
  - Sedating antihistamines: chlorpheniramine, acrivastine, phenyltoloxamine
  - Opioids and CNS depressants: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol, loperamide
  - Others: botulinum toxin type A, acetylcholine, amantadine, acebutolol
  - Minor: acetaminophen, hydrochlorothiazide
- **Class-related concern**: Antimuscarinics can cause mydriasis and raise intraocular pressure, so glaucoma is a caution for this class. Two of the ten model predictions are glaucoma types, which should be treated as a safety signal rather than a therapeutic opportunity.

Warnings and contraindications from the product label were not available. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The IBS prediction scores high (98.84%) and has a biologically plausible antimuscarinic mechanism. However, it is supported by no clinical trials or literature (Evidence Level L5). All four EU authorisations are cancelled, which further limits near-term development.

**To proceed, the following is needed:**
- A systematic search for trials and literature on glycopyrronium or related antimuscarinics in IBS
- Retrieval of the product label (SmPC) warnings and contraindications, which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Assessment of route and formulation compatibility (oral vs. inhaled vs. other) for a gastrointestinal indication
- Clarification of why the EU authorisations were cancelled (commercial or safety reasons)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

