---
layout: default
title: Concizumab
parent: AI Predictions (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Concizumab
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

# Concizumab: From Haemophilia A/B Bleeding Prophylaxis to Diabetic Cataract

## One-Sentence Summary

Concizumab is an anti-TFPI monoclonal antibody, originally used for routine prophylaxis of bleeding in haemophilia A and B.
The TxGNN model predicts it may be effective for **diabetic cataract**, but this is a model-only prediction with **0 clinical trials** and **0 publications** supporting it, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Routine prophylaxis of bleeding in patients 12 years or older with haemophilia A (with or without FVIII inhibitors) and haemophilia B (with or without FIX inhibitors) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.27% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, concizumab is an anti-TFPI (tissue factor pathway inhibitor) monoclonal antibody. By blocking TFPI, it removes inhibition of the extrinsic coagulation pathway and enhances thrombin generation, which is why it is used to prevent bleeding in haemophilia.

The link to the predicted indication is weak. Diabetic cataract is driven by polyol pathway activation, osmotic stress and oxidative damage to the lens, none of which involve the coagulation pathway. The high TxGNN score most likely reflects proximity in the underlying knowledge graph rather than real biology. Other top-ranked predictions are almost all cataract subtypes (craniostenosis, immature, tetanic, type 2 diabetes-associated, mature, cortical, nuclear senile and senile cataract) with near-identical scores, which suggests a graph-level artifact shared across this disease cluster.

The one prediction with some biological proximity to coagulation is antithrombin deficiency type 2 (rank 9). However, the direction is opposite: that condition is prothrombotic, and concizumab promotes thrombin generation, which would likely increase thrombotic risk.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005938 | Alhemo | Not specified | Routine prophylaxis of bleeding in patients 12 years of age or more with haemophilia A (with FVIII inhibitors; or severe without inhibitors) and haemophilia B (with FIX inhibitors; or moderate/severe without inhibitors)... |

The only EU authorization is listed as cancelled in the compiled data.

---

## Safety Considerations

Please refer to the SmPC for safety information.

The rationale for the antithrombin deficiency prediction also notes that concizumab carries thromboembolic warnings, which would argue against use in prothrombotic conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. There are no clinical trials or publications, and no plausible mechanism links TFPI inhibition to lens opacity. The only EU authorization is cancelled, and the safety review could not be completed.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a credible mechanistic hypothesis linking TFPI inhibition to cataract biology
- Safety information from the SmPC (warnings and contraindications), which is required before any safety screening
- Clarification of the cancelled EU market status
- Preclinical evidence in lens or diabetic cataract models before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

