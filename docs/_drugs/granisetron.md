---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Granisetron
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

# Granisetron: From Chemotherapy-Induced Nausea and Vomiting to Manic Bipolar Affective Disorder

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist established for preventing chemotherapy- and radiotherapy-induced nausea and vomiting. The TxGNN model predicts it may also be effective for **Manic Bipolar Affective Disorder**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the signal rests entirely on a mechanistic hypothesis, not on observed clinical data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-/radiotherapy-induced nausea and vomiting (general pharmacological knowledge for granisetron; no jurisdiction-specific license text is available because the drug is not marketed in the evaluated jurisdiction) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, sourced mechanism-of-action data for granisetron is not available in this evidence pack (flagged as a High-severity data gap). What is available comes from the model's own repurposing rationale, which identifies granisetron as a 5-HT3 (serotonin) receptor antagonist. The rationale proposes that 5-HT3 blockade could theoretically modulate central serotonin–dopamine crosstalk implicated in mood circuitry, drawing an analogy to exploratory adjunctive use of a related 5-HT3 antagonist (ondansetron) in mania. Critically, the evidence pack itself flags this as an extrapolation: granisetron has **no direct data** in bipolar disorder, and the link is described as a "mechanistic extension, lacking direct evidence."

This same 5-HT3-antagonism mechanism appears repeatedly across the ten TxGNN predictions in this pack, but the model's own scoring treats it very differently depending on plausibility. For **manic bipolar affective disorder**, **Tourette syndrome**, and **trichotillomania**, the recommendation is "Research Question" — these are conditions with known serotonergic/dopaminergic involvement, so a central 5-HT3 mechanism is at least biologically conceivable. For **conjunctivitis, allergic/cold urticaria, angioedema, bronchitis, and nephrogenic SIAD**, the recommendation is "Hold" — these conditions have no plausible connection to 5-HT3 antagonism, and several (urticaria, angioedema) are actually **known adverse effects of granisetron**, suggesting the model may be picking up an adverse-event co-occurrence signal in the knowledge graph rather than a genuine therapeutic association.

In short, the mania prediction is the most mechanistically defensible of the ten candidates, but it remains a hypothesis generated purely from graph-based inference, with no supporting trial or literature evidence to date.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Granisetron currently has **no marketing authorization on record** in the evaluated jurisdiction (market status: Not Marketed; 0 licenses). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Warnings, contraindications, and drug–drug interaction data for granisetron were not retrievable in this evidence pack — this is logged as a Blocking data gap that must be resolved before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (manic bipolar affective disorder) is supported only by a model score and an unvalidated mechanistic hypothesis — there are zero clinical trials and zero publications, placing this at the lowest evidence tier (L5). Compounding this, a **Blocking** data gap on TFDA warning/contraindication information means a basic safety assessment (S1) cannot even be initiated, and granisetron holds no marketing authorization in the evaluated jurisdiction.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings and contraindications) to resolve the Blocking data gap and enable a safety pre-screen
- Verified mechanism-of-action data via DrugBank API to properly assess the biological plausibility of the serotonin–mania link
- Preclinical or mechanistic studies specifically examining 5-HT3 antagonism in mood/impulse-control disorders (bipolar mania, Tourette syndrome, trichotillomania), since current support is inferred by analogy to other 5-HT3 antagonists rather than granisetron-specific data
- Confirmation of current market/authorization status for granisetron in the target jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

