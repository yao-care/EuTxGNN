---
layout: default
title: Artenimol
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Artenimol
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

# Artenimol: From Malaria to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Artenimol (dihydroartemisinin, DHA) is the primary active metabolite of all artemisinin-class prodrugs, serving as the pharmacological core of antimalarial combination therapies such as Eurartesim® (artenimol + piperaquine). The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis (SSM)**, with **0 clinical trials** and **0 publications** directly supporting this direction. Notably, a separate TxGNN prediction at rank 4 — Plasmodium vivax malaria — carries robust **L1 evidence** with 6 clinical trials and 20 publications, confirming the drug's established antimalarial profile and underscoring the stark contrast with the SSM prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (antimalarial active metabolite; no standalone TW or EU registration) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Artenimol (DHA) is the bioactive core shared by all artemisinin prodrugs. Its canonical antimalarial mechanism involves iron-catalyzed decomposition of the endoperoxide bridge, generating reactive carbon radicals that alkylate parasite proteins (including PfATP6 and PfCRT) and disrupt mitochondrial electron transport. Beyond antiparasitic activity, extensive in vitro evidence shows DHA also inhibits NF-κB transcriptional activity and suppresses the PI3K/Akt/mTOR signaling axis — two pathways broadly implicated in tumor cell survival and proliferation.

Smouldering Systemic Mastocytosis (SSM) is characterized by pathological accumulation of mast cells driven predominantly by the KIT D816V activating mutation, which constitutively signals through PI3K/Akt/mTOR and NF-κB to sustain cell survival. In vitro studies with artemisinin-class compounds have demonstrated inhibition of KIT receptor downstream signaling and induction of apoptosis in mast cell lines, providing at least a mechanistic basis for the TxGNN prediction. The overlap between DHA's established anti-proliferative targets and the oncogenic circuitry in SSM makes this a biologically plausible — if highly speculative — hypothesis.

That said, the TxGNN score of 98.67% should be interpreted with caution. In the context of zero clinical evidence, high graph-propagation scores more likely reflect structural similarity between SSM's disease node and other mast cell or inflammatory nodes that are well-connected to artemisinin-class compounds in the knowledge graph, rather than any SSM-specific experimental signal. Before this can advance beyond a computational hypothesis, in vitro validation in KIT D816V-mutant cell models is the essential first step.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data are not available in this Evidence Pack. Retrieval of the TFDA/EMA SmPC (DG001) is a blocking prerequisite before any clinical translation discussion.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (98.67%), zero clinical trials and zero supporting publications mean this remains a purely computational hypothesis. The mechanistic link through KIT D816V / NF-κB / mTOR inhibition is biologically plausible but entirely unvalidated at the bench or bedside; no investment in clinical development can be justified without preclinical confirmation.

**To proceed, the following is needed:**

- **In vitro validation (highest priority):** Test artenimol against KIT D816V-mutant mast cell lines (e.g., HMC-1.2, ROSA) to confirm anti-proliferative activity, determine IC₅₀, and characterize apoptosis induction
- **MOA data retrieval (DG002):** Query DrugBank API to obtain the complete pharmacological profile of artenimol, including known molecular targets beyond antimalarial mechanisms
- **Safety data retrieval (DG001 — Blocking):** Download and parse TFDA/EMA SmPC PDF to populate key warnings and contraindications before any clinical rationale can be completed
- **Regulatory pathway assessment:** Artenimol has no standalone EU or TW marketing authorization; any SSM indication would require a full new drug application rather than a label extension — a materially higher development barrier
- **Consider broader entry point:** Systemic mastocytosis (rank 3, TxGNN 98.28%) represents the same disease spectrum with a wider patient population and may be a more tractable proof-of-concept study design than the narrower SSM subtype; evaluating both together in a single preclinical package would be more efficient

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

