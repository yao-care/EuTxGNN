---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Bupivacaine
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

# Bupivacaine: From Local/Regional Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is a long-acting amino-amide local anesthetic widely used for nerve blocks, epidural anesthesia, spinal anesthesia, and perioperative pain management.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans**,
however, with **0 clinical trials** and **0 publications** currently supporting this specific direction, the evidence base rests entirely on AI model prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local and regional anesthesia (nerve block, epidural, spinal anesthesia, pain management) |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bupivacaine is an amino-amide local anesthetic that acts by blocking voltage-gated sodium channels (Nav1.x), preventing depolarization and nerve impulse propagation. Beyond this primary mechanism, laboratory evidence shows that bupivacaine and related local anesthetics can inhibit NF-κB signaling — a central regulator of inflammatory cytokine expression — at clinically relevant concentrations. This anti-inflammatory property is the most plausible mechanistic hook that the TxGNN model may have leveraged.

Acrodermatitis chronica atrophicans (ACA) is a late-stage cutaneous manifestation of Lyme borreliosis (*Borrelia burgdorferi sensu lato* infection), characterized by progressive atrophic skin changes and persistent low-grade dermal inflammation. The theoretical rationale is that bupivacaine's NF-κB inhibition could dampen the chronic inflammatory cascade seen in ACA, particularly in the post-antibiotic residual inflammation phase.

In practice, however, this mechanistic link is extremely indirect. ACA is fundamentally an infectious disease requiring systemic antibiotic therapy; its inflammation is secondary to persistent or post-infectious immune dysregulation involving pathways (Toll-like receptor activation, complement cascades) not directly targeted by sodium channel blockade. There is no published preclinical or clinical evidence supporting any local anesthetic as a therapeutic agent for Borrelia-associated skin conditions. This prediction requires in vitro validation before it can be considered a credible repurposing candidate.

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
Despite a high TxGNN prediction score (99.23%), there is zero clinical or preclinical evidence supporting bupivacaine for acrodermatitis chronica atrophicans, and the proposed mechanistic link — NF-κB inhibition modulating Borrelia-driven chronic skin inflammation — remains highly speculative without any experimental grounding.

**To proceed, the following is needed:**
- Retrieve detailed MOA data from DrugBank (DG002) and TFDA SmPC warnings/contraindications (DG001)
- Conduct in vitro studies examining bupivacaine's effect on Borrelia-infected dermal fibroblasts or keratinocytes
- Assess whether anti-inflammatory concentrations achievable in skin tissue are consistent with safe local delivery
- Review whether any existing ACA animal models could serve as a feasibility screen
- Evaluate route-of-administration compatibility: topical or intradermal delivery of bupivacaine for a chronic skin indication differs substantially from its established procedural anesthetic uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

