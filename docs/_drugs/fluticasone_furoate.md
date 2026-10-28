---
layout: default
title: Fluticasone Furoate
parent: AI Predictions (L5)
nav_order: 268
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Fluticasone Furoate: predicted new indication Atopic eczema (evidence level L5). Approved use: Treatment of the symptoms of allergic rhinitis in adults…"
monitor_inn: "Fluticasone furoate"
predicted_indications: ["atopic eczema", "bronchitis", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "contact dermatitis", "occupational dermatitis", "phototoxic dermatitis"]
---

# Fluticasone Furoate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Fluticasone Furoate: From Allergic Rhinitis to Atopic Eczema
{: .text-alpha }

## One-Sentence Summary

Fluticasone furoate is a corticosteroid originally used to treat the symptoms of allergic rhinitis (as the EU product Avamys).
The TxGNN model predicts it may be effective for **atopic eczema**, but **no clinical trials** and only **2 low-tier publications** (a review and a case report, neither with efficacy data) are linked to this prediction, so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of the symptoms of allergic rhinitis in adults, adolescents (12 years and over) and children (6-11 years) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluticasone furoate is a potent glucocorticoid with anti-inflammatory and immunosuppressive effects. Its efficacy in allergic rhinitis, a Th2-driven allergic condition, is established, and mechanistically it may be applicable to other allergic inflammatory diseases such as atopic eczema.

Allergic rhinitis frequently coexists with atopic dermatitis, and the two share an allergic inflammatory background. This is the plausible basis for the model's prediction.

There are important limits. Fluticasone furoate is formulated for intranasal and inhaled delivery, and the data compiled for this report show no topical or dermatologic development. The high TxGNN score is a prediction only. The same applies to the other skin-related predictions (contact dermatitis, occupational dermatitis, phototoxic dermatitis, 2-hydroxyethyl methacrylate sensitization), which rest on class-level corticosteroid reasoning without drug-specific evidence.

**Other predicted indications.** The only prediction with substantial evidence is **obstructive lung disease** (L1, Proceed with Guardrails). It is largely an extension of the drug's existing respiratory use rather than a truly new indication, and the evidence comes from combination products (see the final section).

## Clinical Trial Evidence

Currently no related clinical trials registered for atopic eczema.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews adrenal suppression (HPA-axis effects) from intranasal corticosteroids in allergic rhinitis, which often coexists with asthma and atopic dermatitis. It does not assess efficacy in atopic eczema. |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case report | Indian J Otolaryngol Head Neck Surg | Allergen immunotherapy in a patient with autoimmune disease. Atopic dermatitis is mentioned only as one application of immunotherapy. No efficacy evidence for fluticasone furoate. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000770 | Avamys (valid) | Not specified | Adults, adolescents (12 years and over) and children (6-11 years). Avamys is indicated for the treatment of the symptoms of allergic rhinitis. |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication edges, not label text): measles, herpes simplex virus keratitis, varicella zoster infection, fungal infectious disease, dermatophytosis, pulmonary tuberculosis, parasitic infection, infectious disease, adrenocortical insufficiency, Addison disease, adrenal gland hyperfunction, Cushing syndrome, ocular hypertension, glaucoma, and several upper and lower respiratory tract, nasal cavity and paranasal sinus diseases.
- **Systemic effects**: the literature compiled for this report highlights HPA-axis suppression with intranasal corticosteroids.
- **Respiratory use**: pneumonia risk with inhaled corticosteroids in COPD requires patient selection and monitoring.

Please refer to the SmPC for label warnings, contraindications and drug interaction information, as none were available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For atopic eczema, the prediction is supported only by a model score and a plausible class-level corticosteroid rationale. There are no trials, no efficacy literature, and no dermatologic formulation. The only EU authorization is cancelled.

For reference, the **obstructive lung disease** prediction (L1) is backed by several completed Phase 3 trials and RCTs such as FULFIL, IMPACT and CAPTAIN. Those studies tested fluticasone furoate in fixed-dose combinations (with vilanterol and umeclidinium), so the contribution of fluticasone furoate alone is not isolated. It could be considered **Proceed with Guardrails** in a separate evaluation.

**To proceed, the following is needed:**
- Mechanism of action data (MOA)
- Label warnings and contraindications from the SmPC
- A dermatologic formulation and route-compatibility assessment, followed by preclinical and early clinical studies in atopic eczema
- Verification of current product availability, since the only EU authorization is cancelled
- For the respiratory indication: a plan to isolate the contribution of fluticasone furoate from the combination products, plus pneumonia-risk monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

