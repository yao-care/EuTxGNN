---
layout: default
title: Evinacumab
parent: AI Predictions (L5)
nav_order: 249
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Evinacumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Adjunct to diet and other LDL-C lowering therapies for adults and ado…"
monitor_inn: "Evinacumab"
predicted_indications: ["diabetic cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "immature cataract", "craniostenosis cataract", "tetanic cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic retinopathy"]
---

# Evinacumab
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

# Evinacumab: From Homozygous Familial Hypercholesterolaemia to Diabetic Cataract

## One-Sentence Summary

Evinacumab (brand name Evkeeza) is a monoclonal antibody originally authorised in the EU as an add-on treatment for homozygous familial hypercholesterolaemia (HoFH).
The TxGNN model predicts it may be effective for **diabetic cataract**, with a score of 98.5%, but **no clinical trials and no publications** currently support this direction.
The only related signal in the data is one 2026 preclinical study linking the drug's target to **diabetic retinopathy**, a different eye condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunct to diet and other LDL-C lowering therapies for adults and adolescents aged 12 years and older with homozygous familial hypercholesterolaemia (HoFH) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Evinacumab is a monoclonal antibody that is generally known to neutralise ANGPTL3 (angiopoietin-like protein 3), a regulator of lipid metabolism. Its efficacy in HoFH is the basis of its original authorisation.

For diabetic cataract, the link rests only on the TxGNN prediction score. No trials or publications connect ANGPTL3 inhibition to lens opacity, polyol-pathway damage or oxidative lens injury. The same high score (about 98.4%) appears across many cataract subtypes (type 2 diabetes-associated, mature, immature, nuclear senile, cortical and senile cataract, among others). This suggests a shared signal in the knowledge graph rather than independent support for each condition. The only plausible indirect connection is through diabetes-related metabolic and lipid dysregulation, and it is unproven.

A more biologically grounded lead exists in a neighbouring eye condition, **diabetic retinopathy** (predicted rank 10, score 98.2%). One 2026 study describes an ANGPTL3-integrin α5 axis driving retinal vascular leakage. This is direct biological support for targeting ANGPTL3, although it is probably preclinical work. It does not support the cataract prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered for diabetic cataract.

## Literature Evidence

Currently no related literature available for diabetic cataract.

For reference, the nearby diabetic retinopathy prediction has one publication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41555340](https://pubmed.ncbi.nlm.nih.gov/41555340/) | 2026 | Preclinical/mechanistic study (inferred from title, not verified) | Journal of Translational Medicine | ANGPTL3 is a clinical predictor of diabetic retinopathy. The study examines an ANGPTL3-integrin α5 axis that drives retinal vascular leakage and blood-retinal barrier breakdown. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005449 (status: cancelled) | Evkeeza | Not specified | Adjunct to diet and other LDL-C lowering therapies for adult and adolescent patients aged 12 years and older with homozygous familial hypercholesterolaemia (HoFH). |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The diabetic cataract prediction is based only on a model score, with no trials, no literature and no mechanistic rationale in the data. The EU authorisation is also listed as cancelled, and safety information could not be retrieved. Diabetic retinopathy is a more promising research question than cataract, but it is still at an early, preclinical stage.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking ANGPTL3 inhibition to lens pathology in diabetic cataract
- Confirmed mechanism of action data for evinacumab
- Warnings, contraindications and interaction data from the SmPC
- Clarification of why the EU authorisation was cancelled and the current regulatory status
- Assessment of route and exposure questions, such as whether systemic dosing can reach the eye or local delivery is needed
- If pursuing the eye indications, consider prioritising diabetic retinopathy: verify the design of PMID 41555340 and compare against established anti-VEGF therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

