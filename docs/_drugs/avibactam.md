---
layout: default
title: Avibactam
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Avibactam
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

# Avibactam: From Gram-Negative Bacterial Infections to Streptococcal Pneumonia

## One-Sentence Summary

Avibactam is a novel non-β-lactam β-lactamase inhibitor used in combination with ceftazidime to treat serious Gram-negative bacterial infections, including those caused by carbapenem-resistant organisms — though it is not currently approved in Taiwan.
The TxGNN model predicts it may be effective for **Streptococcal Pneumonia** (TxGNN score 99.70%), with **0 clinical trials** and **0 publications** currently supporting this direction.
The mechanistic rationale is assessed as implausible; this prediction is likely a knowledge graph false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (ceftazidime-avibactam combination; not approved in Taiwan) |
| Predicted New Indication | Streptococcal Pneumonia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, avibactam is a diazabicyclooctane (DBO) class β-lactamase inhibitor. It works by covalently and reversibly binding to serine-based β-lactamases, inhibiting Class A enzymes (including KPCs and ESBLs), Class C enzymes (AmpC), and select Class D OXA-type carbapenemases. When combined with ceftazidime, it restores β-lactam activity against otherwise resistant Gram-negative pathogens such as carbapenem-resistant Enterobacterales (CRE) and certain strains of *Pseudomonas aeruginosa*.

The prediction target — *Streptococcus pneumoniae* — is, however, a Gram-positive bacterium. Its primary mechanism of β-lactam resistance is mutations in penicillin-binding proteins (PBPs), which is completely independent of β-lactamase production. Because avibactam does not interact with PBPs and has no known intrinsic antibacterial activity on its own, it provides no benefit against PBP-mediated resistance. The biological rationale for this prediction is therefore absent.

This is most likely a false positive arising from indirect topological connections in the TxGNN knowledge graph rather than a meaningful biological signal. Among all 10 predicted indications reviewed in this report, only Staphylococcus aureus infection (Rank 7) carries any supporting evidence (2 clinical trials, 20 publications, evidence level L4), and even that prediction carries important mechanistic caveats.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Streptococcal Pneumonia.

> **Note:** For reference, the highest-evidence prediction in this pack is **Staphylococcus aureus infection** (Rank 7, L4), which has 2 associated clinical trials. Neither trial directly tests avibactam for S. aureus treatment efficacy — one is an AMR surveillance study in cirrhosis (NCT06634940) and the other is an antibiotic stewardship intervention study (NCT03941951).

---

## Literature Evidence

Currently no related literature available for Streptococcal Pneumonia.

> **Note:** For reference, the Staphylococcus aureus infection prediction has 20 associated publications. The most mechanistically relevant is PMID [22733066](https://pubmed.ncbi.nlm.nih.gov/22733066/) (2012, *Antimicrobial Agents and Chemotherapy*), which evaluated ceftaroline-avibactam in vitro against MRSA — but this tests avibactam as part of a ceftaroline combination, not standalone, and the primary focus was Gram-negative organisms.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Avibactam's β-lactamase inhibition mechanism is entirely ineffective against *Streptococcus pneumoniae*, whose β-lactam resistance is driven by PBP mutations rather than β-lactamase activity. With zero clinical trials and zero supporting literature, this top-ranked TxGNN prediction lacks both mechanistic plausibility and empirical support, and should not be advanced.

**To proceed with any further evaluation of Avibactam repurposing, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain Taiwan TFDA prescribing information (仿單) for complete safety profile, including warnings and contraindications, before any clinical evaluation can begin
- **Resolve DG002 (High):** Retrieve full MOA data via DrugBank API (DB09060) to enable proper mechanistic analysis across all predicted indications
- **Reassess the full prediction list:** Of the 10 predictions reviewed, only **Staphylococcus aureus infection (Rank 7, L4)** has any supporting evidence — but mechanistic plausibility remains limited to the theoretical ceftaroline-avibactam combination context; a focused mechanistic and in vitro feasibility review is recommended before advancing
- **Flag ranks 1–6, 8–10 as likely false positives:** Predictions for influenza, tuberculosis, schistosomiasis, polyclonal hyperviscosity syndrome, hyperamylasemia, squamous cell lung carcinoma, and congenital analbuminemia all have zero evidence and no credible mechanistic link; these should be deprioritized in any repurposing strategy

---

*This report is for research reference only. Drug repurposing candidates require clinical validation before any therapeutic application. Results generated by the TxGNN model are AI predictions and do not constitute medical advice.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

