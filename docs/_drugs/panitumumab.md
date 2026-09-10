---
layout: default
title: Panitumumab
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Panitumumab
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

# Panitumumab: From Metastatic Colorectal Cancer to Drug-induced Osteoporosis

## One-Sentence Summary

Panitumumab is a fully human anti-EGFR monoclonal antibody originally used to treat metastatic colorectal cancer.
The TxGNN model predicts it may be effective for **Drug-induced Osteoporosis**,
but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a purely AI-driven association with no direct experimental or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (per DrugBank general knowledge; no EU marketing authorization record found for this jurisdiction) |
| Predicted New Indication | Drug-induced Osteoporosis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known information, Panitumumab is a fully human IgG2 monoclonal antibody that targets EGFR (epidermal growth factor receptor), and its efficacy in metastatic colorectal cancer is well established. EGFR signaling has some documented role in bone remodeling (osteoclast/osteoblast regulation), which is likely the basis for the knowledge-graph connection TxGNN identified between this drug and osteoporosis.

However, per the model's own rationale, this link is indirect: it appears to reflect gene-level EGFR–bone pathway associations in the knowledge graph rather than a validated pharmacological mechanism for drug-induced bone loss. There is no clinical or literature evidence currently supporting this specific indication, and the same caveat applies to the other nine predictions in this pack (all EGFR-related eye/lens or bone conditions with similarly weak, gene-level-only rationale).

Given the absence of mechanistic specificity, clinical trials, or published literature, this prediction should be treated as a hypothesis-generating signal only, not a basis for clinical or regulatory action at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations were found for Panitumumab in this jurisdiction — the drug is currently listed as **not marketed** (0 licenses on record).

---

## Cytotoxicity

Panitumumab is an antineoplastic agent (anti-EGFR monoclonal antibody used in metastatic colorectal cancer), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Anti-EGFR monoclonal antibody; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — typical of anti-EGFR monoclonal antibodies; please refer to the SmPC for detailed haematological data |
| Emetogenicity Classification | Low (minimal emetogenic potential typical of monoclonal antibody therapy) |
| Monitoring Items | Skin/dermatologic toxicity, serum electrolytes (magnesium, calcium), infusion-related reactions; CBC and renal/hepatic function per SmPC |
| Handling Protection | Standard biologic infusion precautions; not classified as a cytotoxic hazardous drug requiring special cytotoxic handling procedures |

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and drug-interaction data are currently unavailable — this is flagged as a Blocking data gap (DG001), preventing safety pre-screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are Evidence Level L5 (AI prediction only, decision stage S0) with zero supporting clinical trials or publications, and the mechanistic rationale for the top-ranked indication (drug-induced osteoporosis) is explicitly described as an indirect, gene-level knowledge-graph association rather than a validated pharmacological link. Combined with the Blocking safety data gap and the drug's non-marketed status in this jurisdiction, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (resolve DG001, Blocking)
- Confirmed mechanism of action data from DrugBank or primary literature (resolve DG002, High)
- Generation of preclinical or clinical evidence specifically linking EGFR inhibition to bone metabolism/osteoporosis
- Regulatory status confirmation, since no marketing authorization currently exists in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

