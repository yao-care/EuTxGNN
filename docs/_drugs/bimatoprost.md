---
layout: default
title: Bimatoprost
parent: AI Predictions (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Bimatoprost: predicted new indication Malformation syndrome with odontal and/or periodontal component (evidence level L5). Approved use: Reduction of elevated intraocular pressure in chronic open-ang…"
monitor_inn: "Bimatoprost"
predicted_indications: ["malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "genetic alopecia", "pulmonary arteriovenous malformation (disease)"]
---

# Bimatoprost
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

## Bimatoprost: From Glaucoma and Ocular Hypertension to Malformation Syndrome with Odontal and/or Periodontal Component
{: .text-alpha }

## One-Sentence Summary

Bimatoprost is a prostamide (prostaglandin F2-alpha analog) eye drop, originally used to lower raised eye pressure in chronic open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **malformation syndrome with odontal and/or periodontal component**, but **0 clinical trials** and **0 publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reduction of elevated intraocular pressure in chronic open-angle glaucoma and ocular hypertension (as monotherapy or as adjunctive therapy to beta-blockers) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 1.0000 (model rank 52) |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for bimatoprost: "Bimatoprost, a prostaglandin analog, is a synthetic structural analog of prostaglandin with ocular hypotensive activity. Bimatoprost is believed to lower IOP in humans by increasing outflow of aqueous humor through both the trabecular meshwork (conventional) and uveoscleral routes (unconventional)." ([DailyMed: Durysta (bimatoprost) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3f59da84-0bcc-4c84-b3e2-e215681ef341), label version 2024-10-16; accessed 2026-11-19.) Bimatoprost is known as a prostamide/prostaglandin F2-alpha analog. Its established actions are increasing fluid outflow from the eye, which lowers eye pressure, and stimulating the growth phase of hair follicles.

Neither action maps to a developmental dental or periodontal malformation. These conditions are structural, usually genetic problems of tooth and gum formation, and no plausible mechanistic link was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Without supporting trials or publications, this prediction should be treated as a model output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000391 | Lumigan | bimatoprost | Valid |
| EMEA/H/C/000668 | Ganfort | bimatoprost; timolol | Valid |

<!-- licenses:end -->

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links in the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, and iritis.
- **Drug interactions**: 66 potential interactions were identified, none with a graded severity level. Examples include calcitriol, phentermine, pantoprazole, morphine, metformin, omeprazole, prednisone, simvastatin, and ondansetron.

Please refer to the SmPC for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support, and the drug's known pharmacology has no plausible connection to dental or periodontal malformation.

<!-- review:begin eu-lic-20261106-bimatoprost-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The prediction has no clinical or literature support, and the drug's known pharmacology has no plausible connection to dental or periodontal malformation. The marketing authorization has also been cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 2 EU marketing authorisations for this drug, 2 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-bimatoprost-1 -->

**To proceed, the following is needed:**
- A credible biological rationale linking prostamide signaling to dental or periodontal development
- Any preclinical or clinical evidence specific to this condition
- Detailed mechanism of action data and SmPC safety information

**Note on other predictions:** Among the other predictions compiled for bimatoprost, **alopecia** (model rank 120, score 1.0000) has by far the strongest support. It has 11 registered trials, including three completed Phase 2 studies in androgenetic alopecia (NCT01325337, NCT01904721, NCT01325350), and 20 publications. It is rated L2 with a "Proceed with Guardrails" recommendation. No Phase 3 evidence for scalp alopecia was provided, and efficacy outcomes need expert review. If a repurposing direction is pursued for this drug, alopecia is the more evidence-supported candidate.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The marketing authorization has also been cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Durysta (bimatoprost) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3f59da84-0bcc-4c84-b3e2-e215681ef341) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

