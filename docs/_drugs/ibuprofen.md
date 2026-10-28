---
layout: default
title: Ibuprofen
parent: AI Predictions (L5)
nav_order: 305
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Treatment of a haemodynamically significant patent ductus arteriosus…"
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
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

## Ibuprofen: From Patent Ductus Arteriosus to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen was originally authorised in the EU to treat a haemodynamically significant patent ductus arteriosus in preterm newborn infants.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare skeletal dysplasia.
However, **no clinical trials and no publications** currently support this prediction, so it rests on the model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of a haemodynamically significant patent ductus arteriosus in preterm newborn infants less than 34 weeks of gestational age |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ibuprofen is generally known as a non-selective COX inhibitor with anti-inflammatory and analgesic action. In the EU it was authorised for closing a patent ductus arteriosus in preterm infants.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5, which disrupt cartilage and bone formation. COX inhibition does not address this GDF5/BMP signalling defect, so **no credible mechanistic link was identified**.

The very high TxGNN score is a TxGNN model (deep learning) prediction. It is most likely driven by network proximity rather than biology. The same applies to the other top-ranked predictions, which include brachyolmia, pseudoachondroplasia, myosclerosis, and WHIM syndrome. None has supporting clinical or literature evidence. At most, pseudoachondroplasia has a weak, purely symptomatic rationale (NSAIDs for joint pain), which would not be disease-modifying.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| EMEA/H/C/006129 | Ibuprofen Gen.Orph | Not specified | Treatment of a haemodynamically significant patent ductus arteriosus in preterm newborn infants less than 34 weeks of gestational age | Valid |
| EMEA/H/C/000549 | Pedea | Not specified | Treatment of a haemodynamically significant patent ductus arteriosus in preterm newborn infants less than 34 weeks of gestational age. | Valid |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links, not label text): hypertension and hypotensive disorders, liver failure and liver disease, kidney disease, peptic ulcer disease, inflammatory bowel disease, thrombocytopenia, blood coagulation disease, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, diabetes mellitus and diabetic ketoacidosis, hypothyroidism, epilepsy, COPD, systemic lupus erythematosus, and others.
- **Drug Interactions**: 100 interactions were recorded; the first 20 are listed in the compiled data.
  - **Major**: acetylsalicylic acid.
  - **Moderate**: corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), aprepitant, balsalazide, dexfenfluramine, fenfluramine, exenatide, kanamycin, levofloxacin.
  - **Minor**: famotidine, ranitidine, cimetidine.

Please refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials or publications, no plausible mechanistic link to a GDF5-related skeletal disorder, and both EU authorisations have been cancelled.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting COX inhibition to the GDF5/BMP signalling defect, tested in preclinical models
- Mechanism of action data for ibuprofen
- EU label warnings and contraindications from the SmPC
- A safety assessment for the target population, taking into account the contraindication signals and interactions above
- Re-evaluation of other predicted indications only if supporting evidence appears
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

