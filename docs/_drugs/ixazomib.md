---
layout: default
title: Ixazomib
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Ixazomib
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

# Ixazomib: From Relapsed/Refractory Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Ixazomib (Ninlaro®) is the first oral proteasome inhibitor, approved internationally for relapsed/refractory multiple myeloma (RRMM) in combination with lenalidomide and dexamethasone, based on the TOURMALINE-MM1 Phase 3 trial.
The TxGNN model predicts it may be effective for **Indolent Plasma Cell Myeloma** (smoldering myeloma),
with **0 clinical trials** and **2 real-world observational publications** currently providing indirect mechanistic support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/Refractory Multiple Myeloma (RRMM) |
| Predicted New Indication | Indolent Plasma Cell Myeloma (Smoldering Myeloma) |
| TxGNN Prediction Score | 96.17% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Ixazomib is a second-generation oral proteasome inhibitor that selectively and reversibly inhibits the chymotrypsin-like activity of the **20S proteasome β5 subunit**. By blocking this activity, it disrupts the ubiquitin-proteasome system (UPS) — the central protein quality-control machinery that plasma cells depend upon for high-volume immunoglobulin synthesis. Accumulated misfolded proteins overwhelm the endoplasmic reticulum, triggering the unfolded protein response (UPR) and ultimately driving plasma cell apoptosis.

Indolent (smoldering) plasma cell myeloma shares the same fundamental pathobiology as active multiple myeloma: both originate from clonal plasma cells that are equally dependent on UPS integrity. The distinction between the two lies primarily in disease burden and progression tempo, not in underlying molecular machinery. This makes proteasome inhibition a biologically rational strategy for the indolent form, and the TxGNN model's high confidence score (96.17%) reflects this mechanistic proximity.

However, the current standard of care for smoldering myeloma (SMM) in most guidelines remains watchful waiting — particularly for standard-risk patients. The clinical rationale for early intervention requires evidence that therapy-related benefits (delayed progression to active MM) outweigh toxicity risks in an asymptomatic population. The available literature addresses RRMM only and does not directly validate early-stage use. Further dedicated trials are needed before this prediction can progress to clinical evaluation.

---

## Clinical Trial Evidence

Currently no clinical trials registered for Ixazomib specifically in indolent plasma cell myeloma (smoldering myeloma).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38558233](https://pubmed.ncbi.nlm.nih.gov/38558233/) | 2024 | Real-world Cohort (Retrospective-Prospective) | Cancer Medicine | Northern Italy real-world analysis of IRd (ixazomib + lenalidomide + dexamethasone) in RRMM; demonstrates real-world efficacy and tolerability consistent with the TOURMALINE-MM1 pivotal trial |
| [32193630](https://pubmed.ncbi.nlm.nih.gov/32193630/) | 2020 | Real-world Observational | Annals of Hematology | Multi-site Israeli registry study of ixazomib-based regimens in RRMM; evaluates whether Phase 3 trial outcomes translate to real-world practice across heterogeneous patient populations |

> **Important caveat:** Both publications address relapsed/refractory multiple myeloma (active disease), not indolent/smoldering myeloma. The evidence is therefore **indirect** — it supports the drug's efficacy in plasma cell malignancies broadly, but does not demonstrate benefit in the asymptomatic, early-stage population predicted by TxGNN.

---

## Taiwan Market Information

Ixazomib is **not currently approved or marketed in Taiwan** (0 TFDA regulatory authorizations). No Taiwan-approved indication text is available. Prescribers would need to reference international SmPCs (e.g., FDA label for Ninlaro®) for full product information.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation oral proteasome inhibitor (boronate class) |
| Myelosuppression Risk | Moderate — Thrombocytopenia is the primary dose-limiting toxicity (nadirs typically around Day 14–21 of each cycle); neutropenia also reported; dose reductions may be required |
| Emetogenicity Classification | Low to moderate — Nausea is common but generally manageable with standard supportive antiemetics; oral route reduces infusion-related risks |
| Monitoring Items | CBC with differential (prior to each cycle and as clinically indicated), platelet count closely, hepatic function (AST/ALT/bilirubin), renal function (SCr, eGFR), peripheral neuropathy assessment at each visit |
| Handling Protection | Standard oral antineoplastic precautions apply; capsule contents should not be crushed or opened; caregivers and healthcare workers should avoid direct contact with capsule contents |

---

## Safety Considerations

Detailed safety warnings, contraindications, and drug-drug interaction profiles for Ixazomib are not available in this Evidence Pack (Taiwan SmPC not retrieved; DDI database returned no results). **Please refer to the international SmPC (Ninlaro® FDA or EMA label) for full safety information** prior to any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Ixazomib's proteasome inhibitory activity and indolent plasma cell myeloma is scientifically coherent and earns a high TxGNN score (96.17%). However, the only available supporting literature addresses RRMM — a clinically distinct population from smoldering myeloma — making the evidence indirect (L3, observational, non-specific). The risk-benefit ratio in an asymptomatic population cannot be established without dedicated prospective data, and the drug is not currently available in Taiwan.

**To proceed, the following is needed:**

- **Dedicated clinical trial evidence:** Identify ongoing or planned Phase 2/3 trials of proteasome inhibitors in high-risk smoldering myeloma (e.g., searches on ClinicalTrials.gov for SMM + ixazomib/bortezomib/carfilzomib)
- **Risk stratification:** Define the target sub-population using validated high-risk SMM criteria (e.g., Mayo 2018: ≥20% bone marrow plasma cells + serum M-protein ≥2 g/dL + involved/uninvolved FLC ratio ≥20) to optimize risk-benefit calculation
- **Safety data retrieval:** Download and parse Taiwan TFDA SmPC PDF (if available via international compassionate use records) and retrieve full Ninlaro® FDA/EMA label for complete warnings and contraindications
- **MOA documentation:** Obtain full DrugBank mechanistic data (MOA data gap DG002) to complete mechanistic pathway mapping
- **Market access pathway:** Given off-market status in Taiwan, evaluate regulatory pathway options (e.g., special approval, clinical trial IND) before any clinical exploration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

