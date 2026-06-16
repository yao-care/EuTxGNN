---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: From Thrombotic Thrombocytopenic Purpura to Primary Release Disorder of Platelets

## One-Sentence Summary

Caplacizumab is a humanized anti-von Willebrand factor (anti-vWF) nanobody approved globally for acquired thrombotic thrombocytopenic purpura (aTTP; EMA 2018, FDA 2019), acting by blocking the interaction between vWF multimers and platelet glycoprotein Ib (GPIb) to prevent microvascular thrombosis.
The TxGNN model ranks **Primary Release Disorder of Platelets** as its top new predicted indication with a score of **99.99%**, classifying it within the same broad family of platelet pathway disorders.
However, **no clinical trials or literature** currently exist to support this specific application, and the mechanistic rationale is not straightforward — this remains an early-stage hypothesis only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acquired Thrombotic Thrombocytopenic Purpura (aTTP) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Caplacizumab is a humanized, bivalent, variable-domain-only immunoglobulin fragment (nanobody) that binds with high specificity to the A1 domain of von Willebrand factor. By occupying this binding site, it physically prevents vWF multimers from docking onto platelet glycoprotein Ib (GPIb), thereby halting pathological platelet aggregation. This mechanism is directly relevant to aTTP, where severe ADAMTS13 deficiency causes ultra-large vWF multimers to accumulate in circulation and trigger widespread microthrombosis, leading to thrombocytopenia, hemolytic anemia, and end-organ ischemia.

Primary release disorder of platelets refers to a group of inherited platelet secretion defects in which dense granules (containing ADP and serotonin) or α-granules (containing fibrinogen and vWF) fail to release normally upon platelet activation. The result is impaired secondary aggregation and a bleeding phenotype. The underlying pathology involves granule biogenesis or exocytosis machinery — a distinct cellular axis from the vWF-GPIb adhesion step targeted by caplacizumab — and there is currently no published evidence suggesting that blocking vWF-GPIb interaction would restore or compensate for impaired granule secretion.

The mechanistic concern here runs deeper than a simple lack of data. Primary release disorder is a **hemorrhagic** condition caused by insufficient platelet function; caplacizumab further **reduces** platelet adhesion to vWF. Deploying an anti-platelet agent in an existing platelet secretion deficiency would be expected to worsen bleeding rather than provide therapeutic benefit. The high TxGNN score most likely reflects the model's recognition of shared platelet-pathway ontology terms (both diseases involve platelet dysfunction) rather than a biologically actionable link. Absent any preclinical or clinical data, this prediction warrants no further clinical development at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary release disorder of platelets.

---

## Literature Evidence

Currently no related literature available for primary release disorder of platelets.

---

## Taiwan Market Information

Caplacizumab (DrugBank: DB06081) has not received marketing authorization from the Taiwan Food and Drug Administration (TFDA). No product licenses, approved dosage forms, or registered indications are on record.

For international reference, caplacizumab is marketed as **Cablivi** (Sanofi/Ablynx) and holds approvals from the European Medicines Agency (2018) and the U.S. FDA (2019) for the treatment of adults with acquired aTTP in combination with plasma exchange and immunosuppression. It is also approved in Japan following a Phase 2/3 study in Japanese aTTP patients (NCT04074187, n=21, completed 2021).

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Mechanistic safety signal for this predicted indication:** Caplacizumab's core pharmacological action — blocking vWF-GPIb interaction — constitutes a recognized anti-platelet mechanism. In a hemorrhagic disease background such as primary release disorder of platelets, introduction of an additional anti-platelet agent carries a plausible risk of exacerbating bleeding. This concern is a primary driver of the Hold recommendation and should be formally evaluated before any exploratory study is contemplated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Primary release disorder of platelets is a bleeding disorder rooted in platelet granule secretion failure; caplacizumab's vWF-GPIb blockade mechanism has no established therapeutic relevance to this pathway and may worsen the hemorrhagic phenotype. Evidence level is L5 (model prediction only) with zero supporting clinical or preclinical data.

**To proceed, the following would be needed:**
- Preclinical data (in vitro platelet function assays or animal models) demonstrating any mechanistic benefit of vWF-GPIb blockade in granule release disorder subtypes
- Disease subtype clarification — if any primary release disorder variant involves pathological vWF-GPIb over-engagement, that subtype could be re-evaluated separately
- Formal safety assessment confirming that the anti-platelet effect of caplacizumab does not worsen bleeding in this hemorrhagic background
- Full mechanism-of-action documentation for caplacizumab (currently listed as data gap in this Evidence Pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

