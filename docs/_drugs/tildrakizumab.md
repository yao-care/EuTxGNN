---
layout: default
title: Tildrakizumab
parent: AI Predictions (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Tildrakizumab
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

# Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Tildrakizumab is an anti-IL-23 p19 monoclonal antibody, originally used to treat moderate to severe plaque psoriasis in adults who are candidates for systemic therapy.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe plaque psoriasis in adults who are candidates for systemic therapy |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tildrakizumab is an antibody that blocks the p19 subunit of IL-23. Its efficacy in plaque psoriasis, an IL-23/IL-17-driven inflammatory skin disease, has been established, and mechanistically it may be applicable to diabetic retinopathy.

The proposed link is that chronic low-grade inflammation, including IL-23/IL-17 signalling, may contribute to retinal microvascular damage in diabetic retinopathy. This is speculative. No data compiled for this report show that tildrakizumab acts on retinal disease.

The high TxGNN score (0.996) is a model output only. Practical questions would also need answering, such as whether a systemic or intravitreal antibody could reach the retina safely and effectively. The other top predictions (several cataract subtypes with near-identical scores) look like knowledge-graph proximity to diabetes-related nodes rather than true biological signals. Diabetic retinopathy itself (score 0.995) is the most biologically plausible of the predicted indications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004514 | Ilumetri (status: cancelled) | Not specified | Ilumetri is indicated for the treatment of adults with moderate to severe plaque psoriasis who are candidates for systemic therapy. |

## Safety Considerations

- **Drug Interactions**: 78 potential interactions were identified in total. The first 20 returned include:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, cladribine. These are mostly other immunosuppressive or immunomodulatory agents, so combined immunosuppression is the main concern.
  - **Moderate**: roflumilast, tacrolimus, azathioprine, cyclosporine, alefacept, alemtuzumab, anakinra, canakinumab, denosumab, and several vaccines (tetanus toxoid, anthrax, live cholera vaccine).
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride).

Other safety information (warnings and contraindications) is not available in the data compiled for this report. Please refer to the SmPC for it.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score. There are no registered clinical trials or publications, the mechanism of action data are missing, and the only EU authorization is cancelled. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to support a mechanistic-link analysis
- Warnings and contraindications from the SmPC or package insert, which are needed for safety screening
- A literature and trial search for IL-23 pathway involvement in diabetic retinopathy, and preclinical (L4) evidence in retinal models
- An assessment of route and delivery feasibility (systemic vs. intravitreal) for retinal disease
- Clarification of why the EU authorization was cancelled (e.g., commercial or safety reasons)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

