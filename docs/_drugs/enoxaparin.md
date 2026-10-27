---
layout: default
title: Enoxaparin
parent: AI Predictions (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Enoxaparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Prophylaxis of venous thromboembolism (VTE)…"
monitor_inn: "Enoxaparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "pseudo-von Willebrand disease", "neuropathy, painful", "thrombotic thrombocytopenic purpura", "retinal telangiectasia", "arteriosclerotic retinopathy", "retinal microaneurysm", "vertebral artery occlusion"]
---

# Enoxaparin
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

## Enoxaparin: From Venous Thromboembolism Prophylaxis and Treatment to Thrombophilia Due to Protein C Deficiency
{: .text-alpha }

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin, originally used to prevent and treat venous thromboembolism and to treat acute coronary syndromes.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**,
but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of venous thromboembolism (VTE), treatment of deep vein thrombosis, unstable angina/non-Q-wave myocardial infarction, STEMI, and prevention of clotting in the haemodialysis circuit |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, enoxaparin is a low-molecular-weight heparin that enhances antithrombin III activity and inhibits factor Xa. This reduces thrombin generation and clot formation.

Protein C deficiency removes a natural anticoagulant brake, leaving patients prone to clotting. The original indications (preventing and treating venous thrombosis) address the same clotting problem, and heparins are used in clinical practice as anticoagulant cover in this condition. That makes the prediction biologically plausible.

However, the very high score is a computational prediction only. No trials or publications are linked to this indication. Evidence is therefore at the model-prediction level (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004264 (cancelled) | Inhixa | Not specified | Inhixa is indicated for adults for: Prophylaxis of venous thromboembolism, particularly in patients undergoing orthopaedic, gen... |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from drug-disease relationship edges, not from label text): liver failure, thrombocytopenia, heparin-induced thrombocytopenia, blood coagulation disease, hemophilia, antithrombin III deficiency, Glanzmann thrombasthenia, qualitative platelet defect, intracranial or intracerebral haemorrhage, placental abruption, active peptic ulcer disease, infective/subacute bacterial endocarditis, inflammatory bowel disease/ulcerative colitis, biliary tract disease, obstructive jaundice, osteoporosis, and retinal conditions (retinitis, diabetic and hypertensive retinopathy, diabetic cataract).
- **Drug Interactions**: 100 interactions were recorded. The main **Major** ones are:
  - Antiplatelet and thrombolytic agents: acetylsalicylic acid, abciximab, alteplase
  - NSAIDs: ketorolac, ibuprofen
  - Others: deferasirox, acalabrutinib, trastuzumab emtansine, and the radiopharmaceuticals ibritumomab tiuxetan and tositumomab (including I-131)
  - Moderate interactions include fenfluramine, dexfenfluramine, sibutramine, sugammadex, and aliskiren.

Please refer to the SmPC for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high and the mechanism is plausible, but there are no trials or literature for protein C deficiency. In the EU, the only authorization in the data (Inhixa) is cancelled.

**To proceed, the following is needed:**
- Literature review of heparin/LMWH use in congenital protein C deficiency (for example, case series and guidelines)
- Mechanism of action data and SmPC warnings and contraindications
- Confirmation of the current EU market status of enoxaparin products, since only a cancelled authorization appears in the data
- Safety assessment for this rare population, including bleeding risk and the knowledge-graph contraindications listed above

**Other predictions in the ranked list:**
Evidence is weak for all of them, with no trials and no direct enoxaparin literature.
- **Vertebral artery occlusion** (score 89.40%, L4) is the only one flagged as a research question. Anticoagulation is plausible, but the two linked papers (a May-Thurner syndrome case and a Bow Hunter's syndrome review) are indirect.
- **Thrombotic thrombocytopenic purpura** (score 96.73%, L4) has only indirect literature. Heparin is not standard therapy, apart from thromboprophylaxis during recovery.
- **Primary release disorder of platelets** and **pseudo-von Willebrand disease** are bleeding-tendency conditions, so an anticoagulant would be expected to add risk rather than benefit.
- **Atypical haemolytic-uraemic syndrome with thrombomodulin anomaly** is mainly complement-driven.
- **Painful neuropathy** and the **retinal conditions** (retinal telangiectasia, arteriosclerotic retinopathy, retinal microaneurysm) have no clear rationale. Anticoagulation may even raise haemorrhage risk in the retina.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

