---
layout: default
title: Lumacaftor
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Lumacaftor
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

# Lumacaftor: From Cystic Fibrosis to Leprosy

## One-Sentence Summary

> Lumacaftor is a CFTR corrector approved (in combination with ivacaftor, as Orkambi) for the treatment of cystic fibrosis caused by the F508del-CFTR mutation.
> The TxGNN model predicts it may be effective for **Leprosy**, but currently **no clinical trials** and **no literature** support this direction, and the model's own mechanistic assessment finds no pharmacological plausibility for this link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (inferred from mechanistic description; official TFDA label indication text not available) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is not available from DrugBank in this evidence pack. Based on the mechanistic notes accompanying the predicted-indication entries, Lumacaftor is a CFTR corrector that repairs the misfolding of the F508del-CFTR protein and facilitates its trafficking to the cell membrane. It is approved, in combination with ivacaftor (Orkambi), for cystic fibrosis.

There is no established or biologically plausible link between CFTR-mediated chloride channel correction and the immune/dermatologic pathology of leprosy (Mycobacterium leprae infection). No shared pathway, drug target, or clinical rationale connects the two conditions. The evidence pack itself flags this prediction as likely arising from an indirect knowledge-graph association (e.g., comorbidity or tissue-expression overlap) rather than from any genuine pharmacological mechanism.

Given the absence of both mechanistic rationale and supporting evidence, this specific prediction should be treated as exploratory only. Among the other candidates in this pack, **pulmonary hypertension** (rank 5, L4) has a comparatively more plausible—though still indirect—rationale, since CF patients can develop secondary pulmonary hypertension from chronic lung disease; this may warrant closer attention than leprosy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Lumacaftor currently holds no marketing authorizations in Taiwan (0 licenses; market status: Not marketed). No product, dosage form, or approved indication information is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

Note: TFDA label warnings/contraindications data are marked as a **blocking data gap** in this evidence pack (DG001), meaning a formal safety pre-assessment (S1 stage) cannot proceed until this information is obtained from the TFDA product label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (leprosy) has zero supporting clinical trials or literature, and the model's own mechanistic review explicitly finds no pharmacological plausibility connecting CFTR correction to leprosy pathophysiology. In addition, a blocking data gap in TFDA safety labeling prevents any safety pre-assessment, so this candidate cannot move forward at this time.

**To proceed, the following is needed:**
- TFDA product label (warnings/contraindications) to resolve the blocking safety data gap (DG001)
- Detailed mechanism of action (MOA) data from DrugBank (DG002)
- Re-evaluation of whether a higher-evidence candidate from this batch (e.g., pulmonary hypertension, L4) should be prioritized over leprosy for further investigation
- If leprosy is to be pursued further, dedicated mechanistic or preclinical studies establishing a biological rationale, since none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

