---
layout: default
title: Lonoctocog Alfa
parent: AI Predictions (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Lonoctocog Alfa
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

# Lonoctocog Alfa: From Haemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Lonoctocog alfa is a recombinant Factor VIII (FVIII) replacement product, originally developed for Haemophilia A (FVIII deficiency). The TxGNN model's top prediction suggests possible efficacy in **pseudo-von Willebrand disease**, but this is supported by **0 clinical trials** and **0 publications** — and the evidence pack's own mechanistic analysis argues the biological link is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (Factor VIII deficiency) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed (Taiwan) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Lonoctocog alfa is not currently available in this evidence pack. Based on known drug-class information, Lonoctocog alfa is a B-domain-deleted recombinant Factor VIII, used to replace deficient or absent FVIII in Haemophilia A.

Pseudo-von Willebrand disease, however, is not a coagulation-factor deficiency — it is caused by a platelet GPIb receptor abnormality that produces excessive affinity for von Willebrand factor (vWF), leading to spontaneous vWF/platelet clearance. The pathology sits entirely on the platelet-receptor side, not the FVIII-synthesis side.

Because of this, the evidence pack's own mechanistic assessment concludes the link is **weak**: supplementing FVIII does not correct a platelet receptor defect, and the high TxGNN similarity score most likely reflects the model picking up on shared "bleeding disorder" graph neighborhoods rather than a real causal mechanism. This prediction should be treated as a hypothesis-generation signal only, not a mechanistically grounded candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SmPC for safety information.

**Data gap flagged as blocking**: TFDA label warnings/contraindications for Lonoctocog alfa are not yet available (DG001), which prevents any safety pre-screening for this candidate.

## Other Predicted Indications — Context

Nine additional candidates (rank 2–10) were generated with similarly high TxGNN scores (98.1%–99.8%), all at evidence level L5 with zero supporting trials or literature. The pack's rationale text flags each as mechanistically weak relative to FVIII replacement (e.g., Glanzmann thrombasthenia, Scott syndrome, and constitutional thrombocytopenia are platelet-defect diseases, not coagulation-factor deficiencies). One candidate — **thrombotic thrombocytopenic purpura (rank 10)** — deserves specific caution rather than pursuit: FVIII concentrates typically co-contain vWF, and increasing vWF activity could theoretically worsen microthrombus formation in TTP, which is the opposite of the therapeutic goal (ADAMTS13/vWF reduction). This should be tracked as a potential contraindication signal, not a repurposing opportunity.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pseudo-von Willebrand disease) lacks any clinical or literature support, and the evidence pack's own mechanistic review indicates the biological rationale is weak — FVIII replacement does not address the underlying platelet-receptor defect. Combined with a blocking data gap on TFDA safety labeling and the drug's unmarketed status in Taiwan, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA (or manufacturer SmPC) warnings and contraindications for Lonoctocog alfa (currently blocking)
- Confirmed detailed mechanism-of-action documentation from DrugBank/primary literature
- Any preclinical or case-level evidence specifically linking FVIII replacement to platelet-receptor disorders, before considering escalation beyond L5
- If pursuing further, explicit exclusion/caution review for TTP given the theoretical vWF-related risk noted above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

