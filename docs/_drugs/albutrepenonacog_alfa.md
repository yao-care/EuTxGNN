---
layout: default
title: Albutrepenonacog Alfa
parent: AI Predictions (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Albutrepenonacog Alfa: predicted new indication Pseudo-von Willebrand disease (evidence level L5). Approved use: Treatment and prophylaxis of bleeding in patients with haemophilia B…"
monitor_inn: "Albutrepenonacog alfa"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "acquired coagulation factor deficiency", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "inherited thrombophilia"]
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog alfa: From Haemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Albutrepenonacog alfa is a recombinant factor IX fused to albumin, originally used to treat and prevent bleeding in patients with haemophilia B.
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment and prophylaxis of bleeding in patients with haemophilia B (congenital factor IX deficiency) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on known information, albutrepenonacog alfa is a recombinant factor IX fused to albumin. It replaces the deficient factor IX in the intrinsic coagulation pathway, and its efficacy in haemophilia B is established.

Mechanistically, however, the link to the new indication is weak. Pseudo-von Willebrand disease is a platelet-type disorder caused by a gain-of-function defect in GPIbα, which leads to excess binding of von Willebrand factor. The defect lies in the interaction between platelets and von Willebrand factor, not in a lack of factor IX. The high score (0.9994) most likely reflects shared bleeding-disorder annotations in the knowledge graph rather than a shared biological mechanism, and it should not be read as evidence of benefit.

Among the other top-ranked predictions, most are platelet disorders (primary release disorder of platelets, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defect, constitutional thrombocytopenia) and share the same weakness. Two predictions, thrombotic thrombocytopenic purpura and inherited thrombophilia, raise a theoretical safety concern because a pro-coagulant could worsen thrombosis. The most plausible candidate is **acquired coagulation factor deficiency** (rank 7, score 98.58%), where factor IX replacement could in theory offset an acquired deficit. Established therapies exist there (prothrombin complex concentrate, fresh frozen plasma, vitamin K), so it merits only a hypothesis-level research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003955 (cancelled) | Idelvion | Not specified | Treatment and prophylaxis of bleeding in patients with haemophilia B (congenital factor IX deficiency). |

---

## Safety Considerations

Please refer to the SmPC for safety information.

Pro-coagulant activity is a theoretical concern in prothrombotic conditions such as thrombotic thrombocytopenic purpura and inherited thrombophilia, both of which appear among the model's predictions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for pseudo-von Willebrand disease has no clinical or literature support (L5, model prediction only) and no clear mechanistic basis, since the disease is driven by a platelet-VWF defect rather than factor IX deficiency. In addition, the only EU authorization is cancelled.

**To proceed, the following is needed:**
- Safety information from the EMA product information (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic analysis
- Preclinical or mechanistic evidence showing a plausible role for factor IX in the predicted disease
- Optionally, a hypothesis-level research question on acquired coagulation factor deficiency, the most mechanistically plausible of the predicted indications
- Clarification of the reason for the cancelled marketing authorization and the current availability of the product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

