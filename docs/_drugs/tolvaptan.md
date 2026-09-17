---
layout: default
title: Tolvaptan
parent: High Evidence (L1-L2)
nav_order: 606
evidence_level: L1
indication_count: 10
---

# Tolvaptan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tolvaptan: From Original Indication (Not Specified in Evidence Pack) to Polycystic Kidney Disease 3 with or without Polycystic Liver Disease

## One-Sentence Summary

Tolvaptan's original approved indication is not captured in this Evidence Pack (no EU authorization record present), though it is broadly known in the published literature as an oral vasopressin V2-receptor antagonist.
The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 with or without Polycystic Liver Disease** (an autosomal dominant polycystic kidney disease [ADPKD]-spectrum condition),
with **0 clinical trial registrations** but **20 relevant publications** — including two large completed Phase 3 RCTs (TEMPO 3:4 and REPRISE) — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and no EU license record exists in this Evidence Pack |
| Predicted New Indication | Polycystic Kidney Disease 3 with or without Polycystic Liver Disease (ADPKD-spectrum) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, the structured mechanism-of-action field for this drug is a documented data gap (`original_moa: [Data Gap]`, flagged as `DG002 — High severity` in the meta section). However, the literature evidence collected alongside this prediction consistently and independently identifies tolvaptan as an **oral vasopressin V2-receptor antagonist**. Multiple abstracts in the evidence set (e.g., PMID 23121377, PMID 35134221) describe its mechanism directly: blocking the V2 receptor in renal collecting duct cells reduces intracellular cAMP, which in turn slows cyst growth and the decline of kidney function in cystic kidney disease.

The predicted indication — a polycystic kidney/liver disease phenotype — is mechanistically well aligned with this V2-receptor/cAMP pathway. Cystogenesis in ADPKD and related ciliopathies is driven by cAMP-mediated proliferation and fluid secretion in tubular epithelial cells, which is precisely the pathway tolvaptan antagonizes. This is not a speculative mechanistic leap: the literature pack includes two landmark completed Phase 3 randomized controlled trials — **TEMPO 3:4** (PMID 23121377, NEJM 2012) and **REPRISE** (PMID 29105594, NEJM 2017) — both of which directly tested tolvaptan in ADPKD populations and are further reinforced by an ERA/EASL consensus statement (PMID 35134221) and a 2024 Cochrane systematic review (PMID 39356039) on disease-modifying agents for ADPKD.

In effect, this prediction largely **recovers an already well-established therapeutic use** of tolvaptan in the polycystic kidney/liver disease spectrum rather than identifying a truly novel signal, which is why the evidentiary strength here (L1) is unusually high for a TxGNN-generated candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in `clinical_trials` or `ictrp_trials` for this candidate pair. (Note: pivotal trial evidence exists as published RCTs — see Literature Evidence below — but was not captured via the trial-registry collectors for this pairing.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (TEMPO 3:4) | The New England Journal of Medicine | Landmark Phase 3 RCT showing the V2-receptor antagonist tolvaptan slows total kidney volume growth and eGFR decline in early ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (REPRISE) | The New England Journal of Medicine | Phase 3 RCT extending efficacy data to later-stage ADPKD (lower baseline eGFR), confirming benefit with more hepatotoxicity monitoring required |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Reviews disease-modifying interventions for ADPKD progression, including tolvaptan |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review / Meta-analysis | Nefrologia | Pools efficacy and safety data for tolvaptan across ADPKD trials, confirming benefit in delaying progression to ESRD |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrology, Dialysis, Transplantation | ERA/European Rare Kidney Disease Network consensus on evidence-based initiation criteria for tolvaptan in ADPKD |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive review of ADPKD epidemiology, genetics, and management including tolvaptan |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Reviews ADPKD/polycystic liver disease overlap and notes tolvaptan's effect on slowing renal function deterioration and cyst growth |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Current Opinion in Nephrology and Hypertension | Notes tolvaptan remains the only approved disease-modifying therapy for ADPKD; reviews emerging alternatives |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Review | International Journal of Molecular Sciences | Reviews ADPKD pathophysiology (PKD1/PKD2) and treatment advances including V2-receptor antagonism |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Advances in Kidney Disease and Health | Reviews genetic spectrum of polycystic kidney/liver disease phenotypes relevant to the predicted indication |

---

## EU Market Information

No EU marketing authorizations are recorded for this drug in the current Evidence Pack (`total_licenses: 0`, `market_status: Not Marketed`). No product/authorization data is available to tabulate.

---

## Safety Considerations

Please refer to the SmPC for safety information. Both `key_warnings` and `contraindications` are recorded as data gaps in this Evidence Pack, and the DDI query returned no results (`query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence for this indication is strong (L1: two completed Phase 3 RCTs — TEMPO 3:4 and REPRISE — plus a Cochrane systematic review and an ERA consensus statement), but a **Blocking** data gap (`DG001`: TFDA label warnings/contraindications) prevents the candidate from entering the S1 safety pre-assessment stage, and a **High**-severity gap (`DG002`: structured MOA) limits formal mechanistic scoring.

**To proceed, the following is needed:**
- Resolve `DG001`: retrieve and parse the TFDA/SmPC label (warnings, contraindications) — required before any S1 safety evaluation can proceed.
- Resolve `DG002`: query DrugBank API for structured MOA to support formal mechanistic-link scoring.
- Clarify EU marketing/authorization status, since `total_licenses: 0` conflicts with tolvaptan's known regulatory history and should be re-verified against source data.
- Populate DDI records, since the current query returned no interactions on file.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

