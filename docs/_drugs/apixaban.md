---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Apixaban
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

# Apixaban: From Venous Thromboembolism to Migraine Disorder

## One-Sentence Summary

Apixaban is a selective, direct Factor Xa inhibitor used globally as an oral anticoagulant for stroke prevention in atrial fibrillation and treatment of venous thromboembolism, though it is not currently registered in Taiwan.
The TxGNN model ranks **Migraine Disorder** as its top predicted new indication with a score of **99.02%**,
supported by **1 Phase 3 clinical trial** (indirect relevance) and **4 publications** — however, existing clinical evidence raises a critical contradictory signal: apixaban appears ineffective or potentially harmful for migraine, while warfarin is beneficial, suggesting a fundamental mechanistic mismatch.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for AF stroke prevention and VTE treatment/prevention |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the local data pack. Based on known pharmacology, Apixaban is a highly selective, reversible inhibitor of Factor Xa (FXa) — a central enzyme in the coagulation cascade. By blocking FXa, it prevents conversion of prothrombin to thrombin, thereby reducing clot formation. Its well-established clinical roles include stroke prevention in non-valvular atrial fibrillation and treatment/secondary prevention of deep vein thrombosis and pulmonary embolism.

The TxGNN model likely generates this migraine prediction through the known epidemiological and pathophysiological overlap between migraine, patent foramen ovale (PFO), and antiphospholipid antibody (aPL) syndrome. The working hypothesis is that microthrombi formed in hypercoagulable states can trigger cortical spreading depression (CSD) — the neurophysiological substrate of migraine aura — and that anticoagulation might interrupt this cascade. This rationale has driven some investigators to explore anticoagulant therapy in highly selected migraine subpopulations (e.g., refractory migraine with aPL antibodies or cryptogenic stroke with PFO).

However, the clinical evidence introduces a critical contradictory signal that undermines this prediction for apixaban specifically. Case reports demonstrate consistently that **warfarin** (which broadly inhibits multiple coagulation factors including prothrombin, and also modulates protein C and S pathways) produces sustained migraine remission — but **apixaban** (selective FXa inhibition only) does not replicate this benefit and may in fact worsen migraine symptoms. This pharmacological specificity gap suggests the anti-migraine mechanism of warfarin depends on thrombin suppression or non-anticoagulant effects (e.g., vitamin K-dependent protein signaling), rather than FXa inhibition per se. Selective FXa inhibition by apixaban may be insufficient to interrupt the CSD-triggering chain.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | CLOSE trial: randomized comparison of PFO transcatheter closure, chronic oral anticoagulation, and antiplatelet therapy for secondary stroke prevention in cryptogenic stroke with PFO. The PFO population has high migraine comorbidity, and the anticoagulation arm provides indirect context. However, migraine is not a primary or secondary endpoint, the anticoagulant used is not specified as apixaban, and the primary focus is stroke recurrence rather than migraine treatment — relevance is indirect (Grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Pilot Trial | *Lupus* | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies (aPL); antithrombotic therapy (anticoagulants and/or antiplatelet agents) produced symptomatic improvement in a subset of patients. Supports the aPL-migraine hypothesis as a biological framework, but does not distinguish between anticoagulant agents — apixaban not specifically evaluated. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report | *The Neurologist* | Migraine with aura **worsened** after initiating apixaban. Accompanying literature review concludes that the effect of DOACs on migraine frequency and severity is unclear and controversial — a direct negative signal against apixaban in this indication. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | 55-year-old female with 12-year complete migraine with aura remission on warfarin; symptoms returned within 3 weeks of switching to apixaban, then resolved again within days of resuming warfarin. The most direct evidence of a warfarin-specific, apixaban-ineffective anti-migraine effect — a key negative signal for this repurposing direction. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolution on warfarin and topiramate. Consistent with a warfarin-class-specific (not general anticoagulant class) effect on migraine; apixaban not mentioned. |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite apixaban receiving the highest TxGNN prediction score in this dataset (99.02%), the available clinical literature presents a consistent and reproducible negative signal: selective FXa inhibition by apixaban does not reproduce the anti-migraine benefit of warfarin and may actively worsen symptoms. This is not a data gap — it is a mechanistic disconfirmation signal that must be resolved before any further clinical development of apixaban for migraine can be justified.

**To proceed on migraine, the following is needed:**
- Mechanistic studies to determine whether warfarin's anti-migraine effect is mediated by thrombin suppression, protein C/S pathway modulation, or off-target (non-coagulation) vitamin K-related effects
- Clarification of why selective FXa inhibition fails where broad vitamin K antagonism succeeds — this distinction may represent a fundamental molecular barrier for the entire DOAC class
- If a specific subpopulation rationale (e.g., aPL+ refractory migraine) is pursued, antithrombotic agents with broader coagulation coverage should be prioritized over apixaban

**Higher-priority alternative — Pulmonary Hypertension (Rank 8, L2):**
Investigators should consider redirecting resources to the **pulmonary hypertension** repurposing hypothesis, which carries substantially stronger evidence. Two RCTs support apixaban in this setting:
- PMID 36335915 (AXADIA-AFNET 8): Direct RCT comparison of apixaban vs. VKA in a PH-overlapping population
- PMID 27932335 (SPHInX protocol): Multicentre placebo-controlled RCT specifically in SSc-related pulmonary arterial hypertension

The mechanistic rationale is coherent with apixaban's pharmacology — FXa-PAR2-mediated pulmonary arterial smooth muscle cell proliferation and in-situ thrombosis in small pulmonary vessels provide direct targets for FXa inhibition. This candidate warrants a **Proceed with Guardrails** designation and should be elevated to the primary repurposing focus for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

