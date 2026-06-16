---
layout: default
title: Chenodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Chenodeoxycholic Acid
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

# Chenodeoxycholic Acid: From Cerebrotendinous Xanthomatosis to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Chenodeoxycholic acid (CDCA) is a primary bile acid and the most potent endogenous agonist of the Farnesoid X Receptor (FXR), clinically used as the standard bile acid replacement therapy for Cerebrotendinous Xanthomatosis (CTX), a rare inherited disorder of bile acid synthesis.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **0 clinical trials** and **1 publication** (addressing a related but distinct condition) currently supporting this direction — yielding the lowest possible evidence classification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cerebrotendinous Xanthomatosis (CTX) — bile acid replacement therapy |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Chenodeoxycholic acid (CDCA) is the most potent endogenous ligand for FXR (Farnesoid X Receptor), a nuclear receptor that orchestrates bile acid homeostasis, lipid metabolism, and inflammatory signaling. As an FXR agonist, CDCA suppresses PCSK9 transcription, which theoretically enhances LDL receptor recycling back to the hepatocyte surface — a mechanism that could, in principle, reduce circulating LDL cholesterol. The TxGNN model likely identified network-level metabolic similarity between bile acid metabolism disorders and severe lipid dysregulation, leading to the HoFH prediction.

The phenotypic overlap between CTX (CDCA's established indication) and HoFH is also superficially plausible: both conditions involve lipid accumulation, xanthoma formation, and accelerated cardiovascular disease. In CTX, CYP27A1 mutations impair bile acid synthesis, leading to cholestanol buildup; CDCA replaces the deficient primary bile acid and restores normal FXR signaling. This lipid-regulatory background gives the model a biologically coherent — if indirect — rationale for the HoFH prediction.

However, the mechanistic case has a fundamental limitation that materially weakens clinical translatability. HoFH is defined by the near-complete loss of functional LDL receptor (LDLR) protein, typically due to homozygous or compound-heterozygous LDLR mutations. FXR-mediated PCSK9 suppression can only augment LDL clearance when functional receptors are present. With severely reduced or absent LDLR, CDCA's lipid-lowering pathway contributes negligibly to LDL-C reduction — the primary therapeutic target in HoFH. The sole retrieved publication (PMID 25424010) is a CTX management review and was captured only because of shared cholesterol-related terminology; it provides no direct mechanistic or clinical evidence for CDCA in HoFH.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Review | *Orphanet Journal of Rare Diseases* | Comprehensive review of Cerebrotendinous Xanthomatosis (CTX) — a CYP27A1 mutation disorder causing cholestanol accumulation; describes CDCA bile acid replacement as primary treatment, not HoFH |

> **Important caveat:** This publication addresses CTX, not HoFH. Both conditions involve xanthomas and lipid dysregulation, but the underlying pathophysiology and treatment targets are entirely different. This paper does **not** constitute evidence supporting CDCA use in HoFH.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Detailed safety data (warnings, contraindications, drug interactions) were not available in this Evidence Pack. Known clinical concerns for CDCA class include hepatotoxicity (dose-dependent), diarrhea at high doses, and potential teratogenicity — formal characterization from the SmPC is required before any indication expansion planning.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The FXR/PCSK9 mechanistic pathway CDCA activates is fundamentally receptor-dependent, and HoFH's defining pathology is absent or severely dysfunctional LDLR — rendering CDCA's primary lipid-lowering mechanism unable to address the root cause. No clinical trials or HoFH-specific literature support this use, placing the prediction at L5 (AI model signal only).

**Additional context — higher-priority candidate within this Evidence Pack:**
The rank 7 prediction, **Diabetic Nephropathy**, carries a substantially stronger mechanistic and evidentiary basis (L4; 12 publications including animal RCT-equivalent studies, a metabolomics cohort, and FXR agonism data directly relevant to CDCA). If exploratory investment in CDCA is being considered, diabetic nephropathy represents a more scientifically grounded near-term research question than HoFH.

**To advance HoFH beyond Hold, the following would be needed:**
- Mechanistic studies demonstrating CDCA efficacy via LDLR-independent pathways (e.g., LXR axis, intestinal cholesterol absorption, or VLDL metabolism) in HoFH-relevant models
- Proof-of-concept data in LDLR-knockout animal models specifically
- Pharmacokinetic and dosing characterization for cardiovascular (rather than biliary) indications
- Complete safety profile from SmPC: warnings, contraindications, drug interactions
- MOA documentation from DrugBank (currently a data gap blocking full mechanistic analysis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

