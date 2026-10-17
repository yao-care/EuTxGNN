---
layout: default
title: Emicizumab
parent: AI Predictions (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Emicizumab: predicted new indication Pseudo-von Willebrand disease (evidence level L5). Approved use: Routine prophylaxis of bleeding episodes in patients with haemophilia…"
monitor_inn: "Emicizumab"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
---

# Emicizumab
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

# Emicizumab: From Haemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Emicizumab (Hemlibra) is a bispecific antibody originally used for routine prevention of bleeding in patients with haemophilia A.
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease**, but this rests on a graph-based prediction alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Routine prophylaxis of bleeding episodes in patients with haemophilia A (congenital factor VIII deficiency), with or without factor VIII inhibitors |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Emicizumab is a bispecific antibody that bridges activated factor IX and factor X. In this way it mimics the cofactor function of factor VIII in the coagulation cascade. Its original use is preventing bleeds in haemophilia A, where factor VIII is missing or neutralised. The data compiled for this report did not include a formal mechanism-of-action entry. This description comes from the pharmacology and mechanistic annotations available.

Pseudo-von Willebrand disease is a platelet-type disorder. A gain-of-function change in the platelet receptor GP1BA increases platelet binding to von Willebrand factor. The defect is in primary haemostasis, the platelet-based first step of clotting, and not in factor VIII cofactor activity. This means the mechanistic rationale for emicizumab is **weak**. The very high TxGNN score reflects a network-based association and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004406 | Hemlibra | — | Hemlibra is indicated for routine prophylaxis of bleeding episodes in patients with haemophilia A (congenital factor VIII deficiency): with factor VIII inh... |

This authorization is recorded as cancelled, and no valid authorizations were found.

## Safety Considerations

- **Drug Interactions** (5 interaction records were found; the three below carry a severity rating):
  - **Anti-inhibitor coagulant complex (aPCC): Major.** Combining it with emicizumab is associated with a risk of thrombotic events and thrombotic microangiopathy.
  - Antihemophilic factor, human recombinant: Moderate.
  - Coagulation factor VIIa, recombinant human: Moderate.
- **Additional concern for this prediction**: Emicizumab is a procoagulant. Thrombotic microangiopathy is a known risk, so any use in thrombosis-prone conditions needs particular caution.

For warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for pseudo-von Willebrand disease has no clinical trials or publications behind it, and the mechanism does not fit: the disease is a platelet defect, not a factor VIII deficiency. It should not advance on the strength of the model score alone.

Among the other candidates predicted for emicizumab, **acquired coagulation factor deficiency** (mainly acquired haemophilia A) is the only one with substantial supporting evidence.
- It has L1-level evidence, including prospective phase 2 (GTH-AHA-EMI) and phase 3 (AGEHA) studies and consensus recommendations.
- It would merit a separate evaluation under "Proceed with Guardrails".
- The guardrails would be thrombosis and thrombotic microangiopathy monitoring, caution with bypassing agents, and specialist-led immunosuppression decisions.

**To proceed, the following is needed:**
- A mechanistic or preclinical study showing that emicizumab-mediated tenase activity could plausibly benefit pseudo-von Willebrand disease.
- Any case reports or clinical data in platelet-type disorders.
- Safety information from the SmPC, covering warnings and contraindications.
- Clarification of the cancelled EU authorization status.
- A separate evaluation of the acquired coagulation factor deficiency indication, if the goal is a candidate with real evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

