---
layout: default
title: Isavuconazole
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Isavuconazole
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

# Isavuconazole: From Invasive Fungal Infections to Migraine Disorder

## One-Sentence Summary

Isavuconazole is a triazole antifungal agent used to treat invasive aspergillosis and mucormycosis in immunocompromised patients.
The TxGNN model predicts it may be effective for **migraine disorder**,
however, there are currently **no clinical trials** and **no relevant publications** supporting this direction — all 10 top predictions remain at evidence level L5 (AI prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive fungal infections (aspergillosis, mucormycosis) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Isavuconazole belongs to the triazole class of antifungals. Triazoles work by inhibiting CYP51 (lanosterol 14α-demethylase), a fungal enzyme essential for ergosterol biosynthesis. Without ergosterol, fungal cell membranes lose structural integrity, leading to cell death. Detailed mechanism of action data from DrugBank was not available in this evidence pack, but the drug's antifungal pharmacology is well-established.

Migraine is a neurovascular disorder driven by trigeminal nerve sensitization and cortical spreading depression, with no known connection to ergosterol pathways or fungal CYP51 biology. The antifungal mechanism of Isavuconazole does not map onto any established migraine pathway. One indirect consideration is that Isavuconazole is a potent inhibitor of human CYP3A4 and CYP2C19, which could alter plasma concentrations of certain co-administered drugs — but this is a drug–drug interaction (DDI) concern, not a therapeutic mechanism relevant to migraine.

The high TxGNN score (98.99%) likely reflects indirect structural associations in the knowledge graph — for example, shared CYP metabolic nodes connecting both antifungals and migraine-related pharmacology — rather than a genuine biological signal. No preclinical or clinical data currently support Isavuconazole as a migraine treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

---

## Literature Evidence

Currently no related literature available for migraine disorder.

> **Note on evidence quality:** A PubMed query for the overlapping indication "migraine with or without aura, susceptibility to" (rank 3) returned 20 publications; however, all articles on review concern epilepsy/migraine shared genetics and neurobiology (e.g., CACNA1A, ATP1A2 channelopathies, neuroinflammation). None address Isavuconazole or any antifungal agent. These results are classified as keyword co-mention false positives and do not constitute drug–disease evidence.

---

## Taiwan Market Information

Isavuconazole is currently **not marketed in Taiwan**. No marketing authorizations are on record with the TFDA.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Taiwan-specific package insert warnings and contraindications (TFDA) were not available in this evidence pack. This is a blocking data gap that must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are at evidence level L5 with no supporting clinical or mechanistic evidence; the antifungal mechanism of action (CYP51 inhibition / ergosterol disruption) has no known intersection with migraine pathophysiology, and the high prediction scores are likely computational artifacts from CYP metabolic node clustering in the knowledge graph.

**To proceed, the following is needed:**

- **MOA data**: Query DrugBank API for full mechanism of action, target binding profile, and known human off-target effects
- **TFDA package insert**: Download and parse the TFDA SmPC PDF to obtain Taiwan-specific warnings, contraindications, and DDI information (currently a blocking data gap)
- **Hypothesis re-evaluation**: Determine whether any indirect biological pathway (e.g., CYP3A4-mediated effects on vasoactive mediators, ergosterol-related lipid signaling, or immunomodulation) could plausibly relate to migraine susceptibility — if not, de-prioritize all migraine-related predictions
- **Broader indication scan**: Isavuconazole's known CYP3A4/2C19 inhibitory profile may be more relevant for repurposing targets that involve those metabolic pathways; a hypothesis-driven search beyond the top 10 TxGNN predictions may be warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

