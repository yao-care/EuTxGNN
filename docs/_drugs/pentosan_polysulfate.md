---
layout: default
title: Pentosan Polysulfate
parent: AI Predictions (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pentosan Polysulfate: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Bladder pain syndrome characterised by glomerulations or Hunner's les…"
monitor_inn: "Pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "fetal and neonatal alloimmune thrombocytopenia", "autosomal dominant macrothrombocytopenia", "hemoglobinopathy", "autoimmune hemolytic anemia", "autoimmune thrombocytopenic", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
---

# Pentosan Polysulfate
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

## Pentosan polysulfate: From Bladder Pain Syndrome to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Pentosan polysulfate is a heparin-like sulfated polysaccharide, originally authorised in the EU for bladder pain syndrome (Elmiron).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this prediction, and the drug's anticoagulant properties raise a bleeding-risk concern in this setting.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bladder pain syndrome characterised by glomerulations or Hunner's lesions in adults with moderate to severe pain, urgency and frequency of micturition |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pentosan polysulfate is a heparin-like sulfated polysaccharide with weak anticoagulant and antiplatelet-related activity. Its efficacy in bladder pain syndrome was the basis of its EU authorisation.

The prediction is not mechanistically convincing. Primary release disorder of platelets involves a defect in platelet granule release, and there is no evidence that pentosan polysulfate corrects it. Its anticoagulant effect could instead worsen bleeding in a platelet function disorder. The high TxGNN score (99.71%) therefore reflects a pattern in the knowledge graph, not supporting biological or clinical evidence.

The other top-ranked predictions are also platelet or bleeding disorders (Glanzmann thrombasthenia, pseudo-von Willebrand disease, fetal and neonatal alloimmune thrombocytopenia, and others). All are also supported by model prediction only. The one candidate with indirect supporting literature is hemoglobinopathy (sickle cell disease), where P-selectin blockade has been discussed as a way to improve microcirculatory blood flow. That evidence is preliminary and sits outside the primary prediction evaluated here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the primary predicted indication.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004246 (cancelled) | Elmiron | Not specified | Treatment of bladder pain syndrome characterised by either glomerulations or Hunner's lesions in adults with moderate to severe pain, urgency and frequency of micturition. |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from drug-disease relationships in the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, thrombocytopenia, blood coagulation disease, hemophilia, and heparin-induced thrombocytopenia.
- **Drug Interactions**: 58 interactions were identified, and the 20 listed in the data are all rated Moderate. They are mainly antithrombotic, anticoagulant or antiplatelet agents, which carry additive bleeding risk. Examples include acetylsalicylic acid, warfarin, apixaban, edoxaban, clopidogrel, dalteparin, alteplase, abciximab, cilostazol and dipyridamole.
- **Bleeding and immune thrombocytopenia**: Pentosan polysulfate has been reported to trigger a heparin-induced-thrombocytopenia-like immune reaction. The knowledge graph also lists thrombocytopenia and coagulation disorders as contraindications. This is a direct concern for a platelet or bleeding disorder indication.

Official label warnings and contraindications were not available. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials and no supporting literature, and no plausible mechanism. The drug's anticoagulant activity and its association with HIT-like thrombocytopenia argue against use in platelet or bleeding disorders. In addition, the only EU authorisation is cancelled.

**To proceed, the following is needed:**
- Label warnings and contraindications from the EMA package insert, which are currently missing and block safety screening
- Detailed mechanism of action data
- Preclinical data showing any effect on platelet granule release
- A bleeding-risk assessment for patients with platelet function disorders
- Consideration of hemoglobinopathy (sickle cell disease) as a better-supported alternative, with confirmation of the study design behind the P-selectin findings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

