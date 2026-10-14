---
layout: default
title: Fondaparinux
parent: AI Predictions (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Fondaparinux
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

# Fondaparinux: From Venous Thromboembolism Prevention to Primary Release Disorder of Platelets

## One-Sentence Summary

Fondaparinux is an anticoagulant originally used to prevent and treat venous thromboembolism and to treat acute coronary syndromes.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials** and only **1 loosely related publication** exist, and the mechanism points the opposite way (an anticoagulant would be expected to worsen bleeding).
This prediction is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of venous thromboembolic events (VTE) in adults undergoing major orthopaedic surgery of the lower limbs, abdominal surgery, or in high-risk medical patients; treatment of superficial-vein thrombosis, acute DVT, acute PE, and UA/NSTEMI/STEMI |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 93.06% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fondaparinux is an indirect factor Xa inhibitor that acts through antithrombin III. It is used to prevent and treat venous and coronary thrombosis.

Primary platelet release disorders are qualitative platelet function defects that cause a bleeding tendency. An anticoagulant would be expected to aggravate bleeding rather than treat the condition. The mechanism therefore offers no plausible support for this prediction, which is likely a knowledge-graph artifact.

Other top-ranked predictions show the same pattern. Several are bleeding disorders (pseudo-von Willebrand disease, Glanzmann thrombasthenia), where anticoagulation is contraindicated in principle. Others are fibroproliferative or retinal vascular conditions with no recognized link to factor Xa inhibition. The only prediction with indirect plausibility is vertebral artery occlusion (rank 5, evidence level L4), a thrombotic cerebrovascular condition. Even there, no specific trials or literature were found, and the hemorrhagic risk of anticoagulation in acute cerebrovascular events needs evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Case report | Journal of the Advanced Practitioner in Oncology | Case study of palliative chemotherapy and palliative care in a young patient with metastatic adenocarcinoma. It does not address fondaparinux or platelet release disorders and is not relevant evidence. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000403 (cancelled) | Arixtra | Not specified | 1.5-mg/0.3-ml and 2.5-mg/0.5-ml solution for injection Prevention of venous thromboembolic events (VTE) in adults undergoing major orthopaedic surgery of... |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): kidney disease, thrombocytopenia (including heparin-induced and immune thrombocytopenia), blood coagulation disease, anemia, diabetic retinopathy, diabetic cataract, endocarditis, subacute bacterial endocarditis, pyoureter.
- **Drug Interactions**: 100 interactions were identified. Major interactions include:
  - Antiplatelet and NSAID agents: acetylsalicylic acid, abciximab, ketorolac, ibuprofen, anagrelide
  - Anticoagulation-related and bleeding-risk agents: antithrombin alfa, antithrombin III human, acalabrutinib, trastuzumab emtansine
  - Others: deferasirox, ibritumomab tiuxetan, tositumomab
- Moderate interactions include fenfluramine, dexfenfluramine, sibutramine, sugammadex, and radioiodine products.

Please also refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no trials and no relevant literature. The mechanism is contrary to the disease biology, and the added bleeding risk is a safety concern. The product's only EU authorization is also cancelled.

**To proceed, the following is needed:**
- Label warnings and contraindications from the SmPC, which are currently missing
- Detailed mechanism of action data
- If any follow-up is pursued, redirect it to the mechanistically plausible candidate (vertebral artery occlusion) with a dedicated literature review and a hemorrhagic-risk assessment
- Confirmation that the model's association is not simply a knowledge-graph artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

