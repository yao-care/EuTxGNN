---
layout: default
title: Tacrolimus
parent: High Evidence (L1-L2)
nav_order: 560
evidence_level: L1
indication_count: 10
---

# Tacrolimus
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

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor best known for preventing organ transplant rejection and, in its topical ointment form (Protopic®), for treating atopic dermatitis.
The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (topical, Protopic®) / organ transplant rejection prophylaxis (systemic) — based on established drug classification; a specific licensed indication text was not available in this Evidence Pack |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed (per this Evidence Pack — see note in EU Market Information) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not populated in the drug record for this pack, but the evidence pack's own repurposing rationale provides the relevant pharmacology: tacrolimus is a calcineurin inhibitor that blocks IL-2 gene transcription in T cells, thereby suppressing local inflammatory activation. This is the same mechanism underlying tacrolimus ointment's established, guideline-recognized use in atopic dermatitis.

Seborrheic dermatitis is a chronic inflammatory skin condition in which impaired skin-barrier function and an abnormal immune-inflammatory response (often linked to Malassezia colonization) drive relapsing erythema and scaling — a pathophysiology that overlaps substantially with atopic dermatitis. Because topical tacrolimus already down-regulates the same T-cell-driven inflammatory cascade in the skin, extending its use to seborrheic dermatitis is mechanistically coherent rather than speculative.

This reasoning is reinforced by direct clinical evidence: two completed trials (one Phase 3, one Phase 4) specifically tested tacrolimus ointment as maintenance therapy for severe facial seborrheic dermatitis in adults, and a substantial literature base — including RCTs and cohort studies — supports its use as an off-label, corticosteroid-sparing treatment option in this condition.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic®) as maintenance therapy for severe facial seborrheic dermatitis in adults, aiming to reduce relapse frequency, prolong remission, and reduce topical steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed proactive once- or twice-weekly application of 0.1% tacrolimus ointment to maintain remission and reduce exacerbation incidence in adult facial seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter, double-blind RCT comparing tacrolimus 0.1% to ciclopiroxolamine 1% for maintenance therapy in severe facial seborrheic dermatitis — the first long-term maintenance trial in this population |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Annals of Parasitology | Compared efficacy of sertaconazole 2% cream vs. tacrolimus 0.03% cream in 60 seborrheic dermatitis patients |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | RCT | Indian J Dermatol Venereol Leprol | Compared oral itraconazole plus topical tacrolimus vs. topical tacrolimus alone for maintenance treatment of seborrheic dermatitis in Vietnam |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Cohort | Annals of Dermatology | Evaluated 0.1% tacrolimus ointment as maintenance therapy for facial seborrheic dermatitis, building on the proactive-therapy model established in atopic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, calcineurin inhibitors) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviews pathophysiology, safety, and efficacy of topical calcineurin inhibitors (incl. tacrolimus) as a safe alternative to corticosteroids in seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of facial seborrheic dermatitis pathophysiology and therapeutic horizons, including calcineurin inhibitors |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-Label Pilot Study | J Am Acad Dermatol | Single-center open-label pilot in 18 patients: 61% achieved complete clearance of seborrheic dermatitis with 0.1% tacrolimus over 28 days |
| [28685715](https://pubmed.ncbi.nlm.nih.gov/28685715/) | 2017 | Observational | Chinese Medical Journal | Investigated Staphylococcus epidermidis colonization and impaired skin barrier in facial seborrheic dermatitis, supporting an inflammatory/barrier-based rationale for anti-inflammatory topical therapy |
| [16094289](https://pubmed.ncbi.nlm.nih.gov/16094289/) | 2005 | Observational | Jpn J Med Mycology | PCR-based analysis of Malassezia species in seborrheic and atopic dermatitis patients, supporting shared pathophysiologic mechanisms between the two conditions |

---

## EU Market Information

No EU marketing authorization records for tacrolimus were captured in this Evidence Pack (`total_licenses = 0`, `market_status = Not Marketed`). Tacrolimus is a long-established active substance with multiple products marketed in the EU (e.g., systemic Prograf®/Advagraf® for transplant rejection prophylaxis, and topical Protopic® for atopic dermatitis); the absence of license records here likely reflects a gap in this dataset's regulatory-data collection rather than an actual absence of EU authorization, and should be verified against the EMA/national registers before use in decision-making.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed trials (Phase 3 and Phase 4) directly evaluate tacrolimus ointment for maintenance treatment of severe facial seborrheic dermatitis, supported by a consistent body of RCT, cohort, and pilot-study literature. The mechanism (calcineurin inhibition → suppression of skin T-cell-driven inflammation) is already clinically validated through the drug's approved atopic dermatitis indication, giving strong biological plausibility.

**To proceed, the following is needed:**
- Formal mechanism-of-action documentation for the regulatory dossier (currently a data gap, DG002)
- TFDA/EU product label warnings and contraindications (currently a data gap, DG001 — Blocking for safety review)
- Verification of current EU marketing authorization status for tacrolimus products (discrepancy noted above)
- A dedicated safety monitoring plan for chronic topical use in seborrheic dermatitis (e.g., local skin reactions, photosensitivity, long-term malignancy signal monitoring consistent with class labeling)
- Formal drug-drug interaction review, since no DDI data were returned in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

