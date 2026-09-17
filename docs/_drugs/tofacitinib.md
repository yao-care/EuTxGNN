---
layout: default
title: Tofacitinib
parent: Medium Evidence (L3-L4)
nav_order: 604
evidence_level: L3
indication_count: 10
---

# Tofacitinib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Tofacitinib: From Autoimmune Inflammatory Disease to Plasma Cell Myeloma

## One-Sentence Summary

Tofacitinib is a JAK1/JAK3 inhibitor commonly used for autoimmune inflammatory conditions such as rheumatoid arthritis. Among ten TxGNN-predicted indications in this Evidence Pack, **Plasma Cell Myeloma** is the only candidate supported by actual literature (rather than pure model score), based on the IL-6/JAK/STAT3 signaling axis in the bone marrow microenvironment — but the evidence base is still early-stage, with **3 publications**, **no clinical trials**, and mixed directionality (therapeutic potential vs. epidemiological risk signal).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack (regulatory/MOA data gap). Tofacitinib is generally known as a JAK1/JAK3 inhibitor indicated for autoimmune inflammatory diseases (e.g., rheumatoid arthritis) |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 96.09% (rank #4 by score among candidates; the top-ranked candidate was excluded — see note below) |
| Evidence Level | L3 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note on candidate selection:** The TxGNN model's #1-ranked candidate by raw score, *colobomatous microphthalmia-rhizomelic dysplasia syndrome*, is explicitly flagged in the Evidence Pack's own rationale as knowledge-graph embedding noise with no biological plausibility (a rare congenital skeletal/ocular developmental syndrome unrelated to JAK-STAT signaling). Ranks #1–3 and #6–10 are similarly disease groups with no mechanistic link, no clinical trials, and no literature. **Plasma Cell Myeloma (rank #4)** is the only candidate reaching decision stage S1 with real literature support, so it is used as the focus of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for tofacitinib is not available in this Evidence Pack (data gap DG002). Based on generally known information, tofacitinib is a JAK1/JAK3 inhibitor approved for autoimmune inflammatory diseases; its efficacy in conditions such as rheumatoid arthritis is well established through blockade of cytokine-driven JAK-STAT signaling in immune cells.

The IL-6/JAK/STAT3 axis is also a central survival and proliferation pathway for multiple myeloma cells within the bone marrow microenvironment: bone marrow stromal cells secrete IL-6, which activates JAK1/JAK2/JAK3-STAT3 signaling in malignant plasma cells. Because tofacitinib blocks this same pathway, there is mechanistic plausibility for an anti-myeloma effect, and this is directly supported by a preclinical drug-repurposing study (PMID 29622655) showing tofacitinib reverses bone-marrow-microenvironment-induced growth-promoting effects on myeloma cells.

However, two pharmacoepidemiology studies in this Evidence Pack (PMID 38071595, PMID 39819734) examine DMARD/JAK-inhibitor exposure in relation to multiple myeloma risk rather than treatment benefit, meaning the directionality of the drug-disease relationship (protective vs. risk-associated) is not yet resolved. This is why the evidence level is capped at L3 (observational-level evidence) rather than higher.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for tofacitinib in plasma cell myeloma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [29622655](https://pubmed.ncbi.nlm.nih.gov/29622655/) | 2018 | Preclinical (mechanistic) | Haematologica | Tofacitinib, identified via a prior repurposing screen, reversed the growth-promoting effects of bone marrow mesenchymal stromal cells on myeloma cells by blocking JAK/STAT signaling |
| [38071595](https://pubmed.ncbi.nlm.nih.gov/38071595/) | 2024 | Cohort/registry association study | J Eur Acad Dermatol Venereol | FDA FAERS pharmacovigilance study found associations between multiple myeloma, immunosuppressive/immunomodulatory drugs, and sebaceous carcinoma reporting — informative on immune context but not a treatment-efficacy study |
| [39819734](https://pubmed.ncbi.nlm.nih.gov/39819734/) | 2025 | Cohort (pharmacoepidemiology) | BMC Rheumatology | US Veterans cohort study assessing whether biologic/targeted synthetic DMARD use (including JAK inhibitors) in rheumatoid arthritis patients affects subsequent multiple myeloma incidence |

---

## EU Market Information

Currently no EU marketing authorization is on record for tofacitinib in this Evidence Pack (market status: Not Marketed, 0 authorizations, no license entries available).

---

## Other TxGNN Candidates (Screened Out)

For transparency, the remaining candidates in this Evidence Pack were assessed and deprioritized:

| Disease | TxGNN Score | Evidence Level | Reason for Deprioritization |
|---------|------------|-----------------|------------------------------|
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.96% | L5 | Congenital structural syndrome, no JAK-STAT relevance — flagged as model noise |
| Brachydactyly-syndactyly syndrome | 98.88% | L5 | Congenital limb syndrome, no mechanistic link, no evidence |
| Indolent plasma cell myeloma | 96.66% | L5 | Extrapolated from plasma cell myeloma signal, but no independent trials or literature |
| Myeloid leukemia | 95.43% | L4 | Mixed/contradictory signal — preclinical synergy with imatinib in CML vs. a case report of CML onset during tofacitinib therapy; no prospective evidence |
| Ganglioneuroblastoma | 79.55% | L5 | Pediatric neuroblastic tumor, no mechanistic or clinical support |
| Macrothrombocytopenia with mitral valve insufficiency | 76.17% | L5 | Rare genetic platelet disorder, unrelated to JAK-STAT immunomodulation |
| Hereditary thrombocytopenia with normal platelets | 75.76% | L5 | Genetic platelet disorder, not inflammation/immune-driven |
| Vertebral anomalies with variable endocrine and T-cell dysfunction | 75.34% | L5 | Congenital T-cell developmental defect — tofacitinib would suppress, not restore, T-cell function (mechanism runs opposite to therapeutic need) |
| Retroperitoneal neoplasm | 75.26% | L5 | Heterogeneous tumor group, no JAK-STAT dependency evidence |

---

## Safety Considerations

Please refer to the SmPC for safety information. Note that TFDA label warnings/contraindications for tofacitinib are currently a **blocking data gap** (DG001) in this Evidence Pack, and must be resolved before any safety-stage (S1+) evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Plasma cell myeloma is the only TxGNN-predicted indication with genuine mechanistic and literature support (L3, one supportive preclinical repurposing study), but the two pharmacoepidemiology studies raise an unresolved question of whether JAK inhibition is protective or a risk factor for myeloma. Combined with the absence of any clinical trials and a blocking gap in formal safety/label data, the evidence is not yet sufficient to proceed.

**To proceed, the following is needed:**
- TFDA/EMA product label warnings and contraindications (DG001, blocking)
- Documented mechanism of action (MOA) confirmation (DG002)
- Resolution of the directionality question (anti-myeloma therapeutic effect vs. myeloma risk association) through dedicated mechanistic or prospective clinical studies
- Confirmation of current EU marketing authorization status, since this Evidence Pack shows the drug as not marketed
- Initiation of an early-phase clinical trial or structured case-series review if preclinical rationale is prioritized further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

