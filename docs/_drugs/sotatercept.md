---
layout: default
title: Sotatercept
parent: AI Predictions (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Pulmonary Arterial Hypertension to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Sotatercept is an activin signaling inhibitor originally approved for pulmonary arterial hypertension (PAH) in adults.
The TxGNN model predicts it may be effective for **acute lymphoblastic leukemia**, but **no clinical trials and no publications** currently support this direction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | PAH in adult patients with WHO Functional Class II to III, in combination with other PAH therapies, to improve exercise capacity |
| Predicted New Indication | Acute lymphoblastic leukemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization in the data compiled for this report) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Sotatercept is an activin receptor type IIA-Fc fusion protein. It acts as a ligand trap for activin and related TGF-beta superfamily members. Currently, detailed mechanism of action data is not available in the data compiled for this report, so this description is based on general knowledge of the drug class.

Activin signaling has been implicated in the regulation of blood cell formation, so a biological connection to a leukemia is conceivable. However, no data link activin trapping to leukemic cell survival in acute lymphoblastic leukemia. The relationship between PAH, a vascular disease, and a blood cancer is weak. The high TxGNN score (0.998) is a computational output and cannot be verified from the supplied data.

**Other predicted indications (all L5, all Hold):** The model also ranked the following diseases highly, and none has trials or literature in the data compiled:
- Severe nonproliferative diabetic retinopathy and diabetic retinopathy (TGF-beta/activin involvement in retinal vessel remodeling is plausible but unsupported; sotatercept may increase telangiectasia and bleeding risk, a potential concern for fragile retinal vessels)
- Drug-induced osteoporosis (activin A suppresses osteoblast activity, and related ActRIIA-Fc molecules have shown bone-building signals in early research, so this is comparatively more plausible, but still unverified here)
- Diabetic cataract
- HER2-positive breast carcinoma
- Urothelial carcinoma variants (transitional cell carcinoma, prostatic urethra urothelial carcinoma, kidney pelvis sarcomatoid transitional cell carcinoma, infiltrating bladder urothelial carcinoma sarcomatoid variant). These scores likely reflect disease-ontology clustering rather than specific biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005647 | Winrevair | Not specified | PAH in adult patients with WHO FC II to III, in combination with other PAH therapies, to improve exercise capacity (see section 5.1). |

The only authorization is recorded with a status of cancelled.

## Safety Considerations

Please refer to the SmPC for safety information.

The one drug-specific concern noted in the rationale for the retinopathy predictions is a possible increase in telangiectasia and bleeding risk. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acute lymphoblastic leukemia rests solely on a model score. There are no trials, no literature, and no verified mechanism. The EU authorization is recorded as cancelled, which also needs clarification. Safety data for the label are missing.

**To proceed, the following is needed:**
- Safety data (warnings and contraindications) from the EMA product information, which is currently blocking safety screening
- Confirmation of the current EU authorization status of Winrevair
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic studies linking activin/ActRIIA trapping to leukemic cell biology
- A literature and trial search for the predicted indications, with the bone-related prediction (drug-induced osteoporosis) as the most plausible one to review first
- Route-of-administration and dosage-form compatibility assessment for any new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

