---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
---

# Avatrombopag
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Avatrombopag: From Immune Thrombocytopenia to Marcothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag is a second-generation thrombopoietin receptor agonist (TPO-RA) approved in multiple countries (including the US and EU) for chronic immune thrombocytopenia (ITP) and procedure-related thrombocytopenia in chronic liver disease, but not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **marcothrombocytopenia with mitral valve insufficiency**, with **0 clinical trials** and **0 publications** currently supporting this specific direction.
This remains a model-only prediction (Level L5) requiring dedicated mechanistic and clinical investigation before any development decision can be made.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic immune thrombocytopenia (ITP); thrombocytopenia in adults with chronic liver disease undergoing procedures (globally approved; not registered in Taiwan) |
| Predicted New Indication | Marcothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, avatrombopag is a small-molecule TPO receptor agonist that binds to the transmembrane domain of c-Mpl (the thrombopoietin receptor), activating the JAK2/STAT5 downstream signaling cascade to stimulate megakaryocyte proliferation, differentiation, and platelet release from bone marrow. Unlike first-generation TPO mimetics (e.g., romiplostim), avatrombopag does not compete with endogenous TPO for receptor binding, which may reduce the risk of neutralizing antibody formation.

Marcothrombocytopenia with mitral valve insufficiency (likely referring to macrothrombocytopenia — enlarged, morphologically abnormal platelets with reduced count — co-existing with mitral valve regurgitation) is a rare and heterogeneous condition. The valvular component may drive platelet consumption through turbulent shear-mediated destruction or von Willebrand factor degradation analogous to Heyde's syndrome, creating a consumption-driven thrombocytopenia superimposed on a possible production deficit. In theory, TPO-RA stimulation could compensate for accelerated platelet loss by boosting megakaryopoiesis upstream.

The mechanistic plausibility is limited but not zero. Avatrombopag addresses the quantitative dimension of thrombocytopenia regardless of underlying etiology — a property that has made TPO-RAs useful across diverse thrombocytopenic conditions. However, the "macro-" morphology component and any associated platelet function defects (which frequently accompany hereditary macrothrombocytopenias) would not be corrected by increasing platelet number alone. More critically, the concurrent mitral valve insufficiency introduces significant thrombosis risk in a patient population already susceptible to cardiovascular events, making the risk-benefit ratio highly uncertain without dedicated safety data. The TxGNN high score likely reflects broad knowledge-graph proximity between c-Mpl signaling nodes and thrombocytopenic phenotypes rather than a disease-specific mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN score of 99.995%, there is zero clinical or preclinical published evidence linking avatrombopag to marcothrombocytopenia with mitral valve insufficiency; the mechanistic connection is indirect, and the concurrent cardiovascular pathology introduces unquantified thrombotic risk that prevents responsible advancement at this stage.

**To proceed, the following is needed:**
- Establish the pathophysiological mechanism of thrombocytopenia in this syndrome (production deficit vs. accelerated consumption vs. structural platelet abnormality)
- Confirm whether the TPO-R (c-Mpl) signaling pathway is intact in affected patients — macrothrombocytopenias caused by mutations in GPIbα (Bernard-Soulier), MYH9, or GATA1 may not respond to TPO-RA
- Obtain TFDA prescribing information / SmPC to assess warnings, contraindications, and cardiovascular safety (Data Gap DG001, classified Blocking)
- Retrieve avatrombopag MOA data from DrugBank to complete mechanistic plausibility analysis (Data Gap DG002)
- Conduct a systematic literature review on platelet kinetics and TPO levels in macrothrombocytopenia associated with valvular heart disease
- Perform a dedicated cardiovascular thrombosis risk assessment before designing any clinical investigation in patients with mitral valve insufficiency
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

