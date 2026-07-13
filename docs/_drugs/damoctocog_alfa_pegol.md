---
layout: default
title: Damoctocog Alfa Pegol
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Damoctocog Alfa Pegol
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

# Damoctocog alfa pegol: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Damoctocog alfa pegol (Jivi) is a site-specifically PEGylated recombinant Factor VIII (FVIII) replacement therapy, primarily indicated for the treatment and prophylaxis of bleeding episodes in patients with Hemophilia A (congenital FVIII deficiency).
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Mechanistic analysis strongly suggests this prediction reflects knowledge graph topological noise rather than a genuine biological repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hemophilia A (congenital Factor VIII deficiency; derived from known drug profile — no regulatory record found in dataset) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 97.67% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed MOA data is not currently available in the Evidence Pack. Based on established pharmacology, Damoctocog alfa pegol is a B-domain deleted recombinant FVIII with site-specific 20 kDa PEGylation, which extends plasma half-life by reducing receptor-mediated clearance. It functions within the intrinsic coagulation pathway as a cofactor of the intrinsic tenase complex (FVIIIa–FIXa), dramatically accelerating the conversion of Factor X to Factor Xa during secondary hemostasis. Its original approved use is prophylaxis and on-demand treatment of bleeding in patients with Hemophilia A.

Primary platelet release disorder is characterised by defective secretion of platelet dense granules (ADP, serotonin) or alpha granules (fibrinogen, vWF) upon platelet activation — a pathological process confined entirely to primary hemostasis at the platelet level. FVIII replacement has no known mechanism to correct platelet granule packaging or release defects. In clinical practice, recombinant Factor VIIa (rFVIIa; NovoSeven) serves as the bypass hemostatic agent for platelet function disorders, not FVIII concentrates.

The TxGNN score of 97.67% most likely reflects the topological proximity between Hemophilia A and platelet release disorder nodes within the knowledge graph's broader "bleeding disorder" cluster — both diseases belong to the same disease superclass — rather than any direct mechanistic correspondence. This is a classic example of disease-cluster noise in graph-based prediction models, and should not be interpreted as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorization records were found for Damoctocog alfa pegol in this dataset (0 authorizations; market status: not marketed).

> **Note for reviewers:** Damoctocog alfa pegol (Jivi®, Bayer AG) has received regulatory approvals in major markets including the United States (FDA, 2018) and the European Union (EMA, EU/1/18/1331) for Hemophilia A. The absence of records in this dataset likely reflects a data collection gap rather than true non-approval status. Please verify current EU authorization status via the EMA product database.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for primary platelet release disorder lacks biological plausibility — FVIII replacement therapy acts downstream in the coagulation cascade and cannot address the platelet granule secretion defect that underlies this condition. There is no supporting clinical trial evidence, no supporting literature, and the mechanistic rationale for repurposing is absent. The high prediction score is attributed to knowledge graph topology, not therapeutic potential.

**To proceed, the following would be needed:**
- Retrieve complete MOA data from DrugBank API (DB14700) to formally document the mechanism of action
- Obtain Taiwan/EU SmPC to complete the safety profile (warnings, contraindications, DDI)
- Identify any preclinical studies demonstrating a role of FVIII or the tenase complex in platelet granule biology — without such evidence, this indication cannot advance beyond L5
- Consider reviewing other predicted indications in the pack (e.g., Pseudo-von Willebrand Disease, Rank 3) where a weak but mechanistically traceable secondary FVIII connection exists, before revisiting this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

