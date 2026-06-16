---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Catridecacog
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

# Catridecacog: From Congenital Factor XIII Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

Catridecacog (NovoThirteen®/Tretten®) is a recombinant human Factor XIII A-subunit (rFXIII-A), designed as replacement therapy for patients with congenital Factor XIII deficiency.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, however there are currently **no clinical trials** and **no publications** directly supporting this direction.
Evidence is limited to model prediction only (L5), and the mechanistic link is biologically indirect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Factor XIII Deficiency |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Catridecacog is a recombinant human coagulation Factor XIII A-subunit that functions as a transglutaminase: once activated by thrombin and calcium, it catalyses the formation of isopeptide cross-links between fibrin α- and γ-chains, stabilising the fibrin clot network and making it resistant to fibrinolysis.

Primary release disorder of platelets — such as delta-storage pool deficiency — is characterised by impaired secretion of platelet granule contents (ADP, serotonin, calcium) upon activation. The disease pathology lies upstream in the platelet granule release machinery, not in downstream fibrin stabilisation. While FXIII is physiologically stored within platelets (accounting for approximately 50% of circulating FXIII), this reflects biological distribution rather than a therapeutic rationale for platelet granule secretion defects.

The TxGNN model's high prediction score likely reflects shared network proximity between haemostatic disorders within the knowledge graph, rather than a direct mechanistic relationship. FXIII replacement therapy cannot correct platelet granule release defects, and there is no clinical or preclinical evidence to support this repurposing direction at present.

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
There is no clinical or preclinical evidence supporting the use of catridecacog in primary release disorder of platelets, and the mechanistic link is biologically implausible — FXIII crosslinking activity does not address defects in platelet granule secretion.

**To proceed, the following is needed:**
- Preclinical studies demonstrating a biologically plausible connection between FXIII replacement and platelet granule release defects
- Identification of a patient subpopulation with concurrent FXIII deficiency and platelet release disorder that might benefit from combination management
- MOA data from DrugBank (DG002) to enable a rigorous mechanistic analysis
- TFDA/EMA SmPC review (DG001) to assess any contraindications relevant to platelet disorders

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

