---
layout: default
title: Eculizumab
parent: AI Predictions (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Paroxysmal Nocturnal Haemoglobinuria to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor, originally used to treat paroxysmal nocturnal haemoglobinuria (PNH) and atypical haemolytic uremic syndrome (aHUS).
The TxGNN model predicts it may be effective for **cyclic hematopoiesis** (cyclic neutropenia), but **no clinical trials** and **no publications** specific to this disease are currently available, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal haemoglobinuria (PNH) and atypical haemolytic uremic syndrome (aHUS) in adults and children |
| Predicted New Indication | Cyclic hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (all marketing authorizations cancelled) |
| Number of Authorizations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Eculizumab is known as a C5 complement inhibitor, and its efficacy in complement-mediated diseases (PNH, aHUS, refractory generalized myasthenia gravis, NMOSD) is established.

Cyclic hematopoiesis (cyclic neutropenia) is typically caused by ELANE mutations and is not primarily a complement-mediated disease. No plausible complement-related mechanism is supported by the available data. The very high TxGNN score (99.97%, model rank 595) reflects a graph-based association only and should not be read as evidence of efficacy.

The other top-ranked predictions (various congenital neutropenias, adult idiopathic neutropenia, primary immunodeficiency due to p14 deficiency, primary release disorder of platelets) share the same weakness: they involve defects in myeloid maturation, chemokine/G-CSF signalling or platelet function rather than terminal complement activity. Blocking C5 also increases the risk of serious meningococcal infection, which is a particular concern in neutropenic or immunodeficient patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications specific to cyclic hematopoiesis were found. The literature retrieved for the lower-ranked predictions is mostly general eculizumab-indication material (PNH, aHUS/thrombotic microangiopathy, myasthenia gravis, CD59 deficiency) and does not address the predicted new indications. It is therefore not listed here.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/006036 (cancelled) | Epysqli | Not specified | PNH and aHUS in adults and children |
| EMEA/H/C/000791 (cancelled) | Soliris | Not specified | PNH, aHUS, refractory generalized myasthenia gravis (anti-AChR positive), NMOSD (anti-AQP4 positive)... |
| EMEA/H/C/005652 (cancelled) | Bekemv | Not specified | PNH in adults and children |

## Cytotoxicity

Eculizumab is a monoclonal antibody against complement C5, not a cytotoxic antineoplastic drug, so this section does not apply.

## Safety Considerations

- **Drug Interactions**: Four minor interactions were identified, all with human immunoglobulin G preparations (intravenous, subcutaneous, intramuscular, and combined intravenous/subcutaneous).
- **Infection risk (from the mechanism of C5 inhibition)**: Terminal complement blockade raises the risk of serious meningococcal infection, which would be a particular concern in neutropenic or immunodeficient patients.

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or targeted literature, and there is no plausible complement-driven mechanism for cyclic hematopoiesis. The evidence level is L5. In addition, all three EU marketing authorizations are currently cancelled.

**To proceed, the following is needed:**
- Mechanistic evidence for complement involvement in cyclic hematopoiesis (ELANE-related neutropenia)
- Mechanism of action data for the drug
- Warnings and contraindications from the SmPC, followed by a safety review that addresses meningococcal infection risk in neutropenic patients
- Clarification of the cancelled EU authorization status and the current availability of the product
- Preclinical or early clinical data before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

