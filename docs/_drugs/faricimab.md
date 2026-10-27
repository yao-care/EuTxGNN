---
layout: default
title: Faricimab
parent: AI Predictions (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Faricimab: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Neovascular (wet) age-related macular degeneration (nAMD)…"
monitor_inn: "Faricimab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "drug-induced osteoporosis", "esotropia", "severe nonproliferative diabetic retinopathy", "HER2 positive breast carcinoma", "diabetic retinopathy", "respiratory syncytial virus infectious disease", "fetal and neonatal alloimmune thrombocytopenia"]
---

# Faricimab
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

## Faricimab: From Neovascular Age-Related Macular Degeneration to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Faricimab (Vabysmo) is an intravitreal bispecific antibody originally used to treat retinal diseases: wet age-related macular degeneration, diabetic macular oedema and macular oedema after retinal vein occlusion.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **0 clinical trials** and **0 publications** support this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular (wet) age-related macular degeneration (nAMD), visual impairment due to diabetic macular oedema (DME), and visual impairment due to macular oedema secondary to retinal vein occlusion (RVO) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.88% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Faricimab is a bispecific antibody given by intravitreal injection. It neutralizes two targets, vascular endothelial growth factor A (VEGF-A) and angiopoietin-2 (Ang-2). Together these drive vascular leakage, inflammation and abnormal new vessel growth in the retina, which is why the drug works in the retinal conditions listed above.

On current information, **this prediction is not mechanistically reasonable**. Primary release disorder of platelets is a systemic platelet function disorder. Nothing links it to the VEGF-A/Ang-2 pathways that faricimab blocks in the eye. Faricimab is also dosed into the eye with minimal systemic exposure, which makes a systemic effect on platelet function even less likely. The high score looks like a graph-based prediction artifact rather than a pharmacological signal.

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
| EMEA/H/C/005642 | Vabysmo | Not specified | Vabysmo is indicated for the treatment of adult patients with: neovascular (wet) age-related macular degeneratio... |

The only authorization on record is listed as cancelled, so the EU market status is "Cancelled only".

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications, and no plausible mechanistic link between VEGF-A/Ang-2 blockade in the eye and platelet function disorders. The only EU authorization is also recorded as cancelled.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting VEGF-A/Ang-2 inhibition to platelet release function, with supporting preclinical data
- Any clinical or literature evidence in platelet function disorders (currently none)
- Review of the SmPC for safety information, including thromboembolic and bleeding considerations
- Clarification of the cancelled authorization status

**Note on other predictions:** Among the other top-ranked predictions, **diabetic retinopathy** (TxGNN score 96.75%) has the strongest support. It has Phase 3 evidence in the related condition DME (YOSEMITE/RHINE) and several faricimab trials in diabetic retinopathy, including the completed Phase 2 MAGIC trial (NCT05681884) and the recruiting Phase 3 trial NCT06790784. It is rated L1 with a "Proceed with Guardrails" recommendation, and it is a more practical candidate to evaluate first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

