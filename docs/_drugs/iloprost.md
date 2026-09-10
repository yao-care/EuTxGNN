---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Iloprost
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

# Iloprost: From Pulmonary Arterial Hypertension to Pulmonary Arterial Hypertension Associated with HIV Infection

## One-Sentence Summary

Iloprost is a synthetic prostacyclin (PGI2) analog established for the treatment of pulmonary arterial hypertension (PAH) through pulmonary vasodilation and reduced pulmonary vascular resistance. Among ten TxGNN-predicted indications screened for this drug, the strongest and most actionable signal is **Pulmonary Arterial Hypertension Associated with HIV Infection**, supported by **1 completed Phase 3 RCT** and **4 supporting publications**. The remaining nine candidates (other PAH subtypes, alopecia/hypotrichosis) currently range from L2 to L5 evidence, with most (including the top TxGNN-ranked "hypotrichosis simplex of the scalp") having no clinical or literature support at all.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this jurisdiction's dataset (drug not marketed; formal label text missing). Per the mechanistic rationale captured in this evidence pack, iloprost is already an established PAH therapy. |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with HIV Infection |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original-indication and MOA fields are flagged as data gaps in this pack (DG001, DG002). However, the repurposing rationale attached to the evidence itself states that iloprost is a synthetic prostacyclin (PGI2) analog that works through pulmonary vasodilation and reduction of pulmonary vascular resistance — the standard mechanism by which it treats pulmonary arterial hypertension broadly.

HIV-associated PAH shares the same downstream pathophysiology as other PAH subtypes — endothelial dysfunction and pulmonary vascular remodeling — regardless of the underlying trigger. Because iloprost's vasodilatory mechanism acts on this shared final common pathway rather than on HIV-specific biology, extending its use to HIV-associated PAH is closer to a **label-scope expansion** than a novel mechanistic hypothesis.

This is reinforced by the clinical evidence: the completed Phase 3 PROWESS-15 trial explicitly enrolled patients with idiopathic/familial PAH as well as HIV- and drug/toxin-associated PAH under one protocol, treating them as a single mechanistically-unified population. This is a materially stronger evidence base than most of the other candidate indications generated for this drug in the same screening run, many of which (e.g., hypotrichosis, alopecia) rely purely on the vasodilation-to-hair-follicle-blood-flow analogy with zero clinical or literature backing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | PROWESS-15: multicenter, double-blind, randomized, placebo-controlled crossover study assessing effect of a single dose of inhaled iloprost on exercise capacity in symptomatic PAH patients (idiopathic/familial PAH, or PAH associated with HIV or drugs/toxins), naive to treatment or on stable background bosentan/ambrisentan/sildenafil. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Cohort (Registry) | Terapevticheskii arkhiv | Six-year National Registry analysis of PAH prevalence, clinical course, treatment, and mortality, including secondary PAH etiologies. |
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Review | The Mount Sinai Journal of Medicine, New York | Overview of HIV-related pulmonary arterial hypertension (~0.5% incidence in HIV-infected individuals), pathogenesis, and clinical presentation. |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Review of controlled trials of prostacyclin and synthetic analogues (including iloprost) across PAH etiologies, including HIV infection. |
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review | American Journal of Respiratory Medicine | Review of prostanoid therapy for PAH, noting shared obstructive pulmonary microvascular pathology across idiopathic PAH and PAH associated with connective tissue disease, congenital shunts, portal hypertension, and HIV infection. |

---

## EU Market Information

Currently no marketing authorization records available — the drug is not marketed in this jurisdiction (0 licenses on file).

---

## Safety Considerations

Please refer to the SmPC for safety information. No drug-drug interaction data, contraindications, or warnings are currently on file for iloprost in this pack (DDI query: not found; safety fields: data gap).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3, double-blind, placebo-controlled RCT (PROWESS-15, n=64) enrolled HIV-associated PAH patients under a shared PAH mechanistic framework with iloprost showing efficacy signal, giving this candidate the strongest evidence base (L1) among the ten indications screened for this drug. However, HIV-PAH was not the trial's sole target population, and no HIV-PAH-specific subgroup results, safety data, or antiretroviral drug-interaction data are currently available.

**To proceed, the following is needed:**
- Iloprost MOA and TFDA/EMA label data (currently blocking data gaps DG001, DG002)
- Subgroup-level efficacy/safety results for the HIV-associated PAH patients within NCT00709956
- Drug-drug interaction review with antiretroviral therapy (ART) regimens
- Confirmation of local marketing/regulatory pathway, since the drug is not currently marketed in this jurisdiction

*Note: This report focuses on the highest-evidence candidate from a 10-indication TxGNN screen for iloprost. The TxGNN top-ranked candidate by raw score alone ("hypotrichosis simplex of the scalp," 99.45%) has no supporting clinical trials or literature (L5, Hold) and is not recommended for further evaluation at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

