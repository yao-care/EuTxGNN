---
layout: default
title: Sacubitril
parent: AI Predictions (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
---

# Sacubitril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Sacubitril: From Heart Failure (ARNI Combination Component) to Brain Small Vessel Disease 1 with or without Ocular Anomalies

## One-Sentence Summary

> Sacubitril is the neprilysin-inhibitor prodrug component of the ARNI combination Sacubitril/Valsartan (Entresto), which has established efficacy in heart failure; sacubitril alone holds no standalone EU marketing authorization.
> The TxGNN model's top-ranked prediction for this compound is **Brain Small Vessel Disease 1 with or without Ocular Anomalies**, but this pairing is supported by **0 clinical trials** and **18 publications that are all mechanistically unrelated** (mostly ophthalmic/genetic case reports), indicating the prediction is very likely disease-ontology matching noise rather than a genuine drug-disease signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack for standalone Sacubitril (no EU mono-substance authorization); as background context, Sacubitril is the prodrug component of Sacubitril/Valsartan (Entresto), approved for heart failure with reduced ejection fraction |
| Predicted New Indication | Brain Small Vessel Disease 1 with or without Ocular Anomalies |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed (as standalone substance) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for standalone Sacubitril is currently unavailable in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, Sacubitril is a prodrug that is converted to LBQ657, an inhibitor of neprilysin (neutral endopeptidase). By blocking the breakdown of natriuretic peptides (ANP/BNP), it potentiates natriuresis, vasodilation, and anti-fibrotic signaling — the basis of its use as a component of the ARNI combination for heart failure.

**However, this specific top-ranked prediction does not have a plausible mechanistic link.** Brain small vessel disease 1 with or without ocular anomalies is a rare monogenic vasculopathy caused by *COL4A1* mutations, affecting basement membrane collagen integrity — a pathway with no established connection to neprilysin inhibition or natriuretic peptide signaling. The 18 associated publications are almost entirely case reports and reviews on unrelated congenital ophthalmic/craniofacial syndromes (e.g., Axenfeld-Rieger syndrome, ocular coloboma, holoprosencephaly, tilted disc syndrome), none of which mention Sacubitril or neprilysin. This pattern is consistent with **disease-ontology co-occurrence noise** in the knowledge graph rather than a true drug-repurposing signal.

Notably, a lower-ranked candidate in this same prediction set — **diabetic nephropathy (rank 3, L3 evidence)** — has a far more biologically coherent rationale (natriuretic-peptide-mediated renoprotection) and is backed by preclinical models, one completed real-world study, and one not-yet-recruiting Phase 4 RCT. Decision-makers reviewing this drug may wish to prioritize that candidate over the nominal top-ranked (but likely spurious) prediction discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brain Small Vessel Disease 1 with or without Ocular Anomalies.

---

## Literature Evidence

All 18 retrieved publications concern unrelated congenital ophthalmic, craniofacial, or genetic syndromes and do not reference Sacubitril or its mechanism of action. They are listed below for completeness, with a note that none provide supporting evidence for this drug-disease pairing.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35882526](https://pubmed.ncbi.nlm.nih.gov/35882526/) | 2023 | Review (unrelated) | J Med Genet | Overview of Axenfeld-Rieger syndrome phenotypes; no mention of Sacubitril |
| [6782689](https://pubmed.ncbi.nlm.nih.gov/6782689/) | 1981 | Review (unrelated) | Surv Ophthalmol | General review of ocular coloboma etiology |
| [30182440](https://pubmed.ncbi.nlm.nih.gov/30182440/) | 2018 | Review (unrelated) | Am J Med Genet C | Neuropathology of holoprosencephaly |
| [33870948](https://pubmed.ncbi.nlm.nih.gov/33870948/) | 2022 | Case series (unrelated) | J Neuroophthalmol | Optic nerve aplasia case findings |
| [11941259](https://pubmed.ncbi.nlm.nih.gov/11941259/) | 2002 | Review (unrelated) | J Fr Ophtalmol | Congenital megalocornea review |
| [10498002](https://pubmed.ncbi.nlm.nih.gov/10498002/) | 1999 | Review (unrelated) | Optom Vis Sci | Tilted disc syndrome morphology |
| [6390155](https://pubmed.ncbi.nlm.nih.gov/6390155/) | 1983 | Review (unrelated) | Neurol Clin | Optic disk abnormalities overview |
| [1458324](https://pubmed.ncbi.nlm.nih.gov/1458324/) | 1992 | Review (unrelated, veterinary) | Vet Clin North Am Equine Pract | Congenital ocular anomalies in horses |
| [16848213](https://pubmed.ncbi.nlm.nih.gov/16848213/) | 2006 | Case report (unrelated) | Acta Med Croatica | Distichiasis case description |
| [22963965](https://pubmed.ncbi.nlm.nih.gov/22963965/) | 2012 | Case report (unrelated) | Ann Dermatol Venereol | Branchio-oculo-facial syndrome case |

---

## EU Market Information

No EU marketing authorizations were found for standalone Sacubitril (`total_licenses: 0`). Sacubitril is only marketed in the EU as a component of the fixed-dose combination Sacubitril/Valsartan (Entresto); no combination-product license data was included in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in the current evidence pack (flagged as a Blocking data gap, DG001 — TFDA/regulatory label warnings and contraindications).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Brain Small Vessel Disease 1 with or without Ocular Anomalies) has a high model score but no plausible mechanistic link, zero clinical trials, and literature that is entirely unrelated to Sacubitril's pharmacology — consistent with disease-ontology matching noise rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001 (regulatory label warnings/contraindications) before any safety evaluation can proceed
- Resolve High-severity data gap DG002 (confirmed MOA data via DrugBank API) to properly assess mechanistic plausibility for any candidate indication
- If pursuing repurposing work for this compound, prioritize evaluation of the **diabetic nephropathy** candidate (rank 3, L3 evidence, "Research Question" stage) instead, given its stronger mechanistic rationale and existing preclinical/clinical data
- Review the TxGNN disease-ontology mapping pipeline to filter out low-plausibility rare-disease predictions like this one before they reach reporting stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

