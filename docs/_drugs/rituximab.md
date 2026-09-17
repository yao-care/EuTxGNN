---
layout: default
title: Rituximab
parent: High Evidence (L1-L2)
nav_order: 513
evidence_level: L1
indication_count: 10
---

# Rituximab
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

# Rituximab: From B-Cell Non-Hodgkin Lymphoma to Follicular Lymphoma

## One-Sentence Summary

> Rituximab is an anti-CD20 monoclonal antibody with an established role in treating CD20-positive B-cell non-Hodgkin lymphomas.
> The TxGNN model's top prediction — **Follicular Lymphoma** — is supported by an unusually deep evidence base:
> **10+ Phase 3 trials** (several already completed with >1,000 patients) and **20+ publications**, including RCTs and clinical guidelines,
> indicating this signal largely *confirms* an already well-established standard-of-care use rather than representing a novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in the regulatory dataset (no marketing authorizations on file for this jurisdiction) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 96.08% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Rituximab is not available as a standalone field in this dataset. However, the evidence pack's own repurposing rationale confirms that Rituximab is an **anti-CD20 monoclonal antibody**, and that CD20 is broadly expressed on malignant B cells in follicular lymphoma — making anti-CD20 antibody therapy the accepted standard mechanism of action for this disease.

Importantly, the volume and nature of the supporting evidence (dozens of Phase 3 trials spanning first-line induction, maintenance, and relapsed/refractory settings, all using rituximab as a backbone or comparator arm) indicate that Rituximab is *already* a cornerstone therapy for follicular lymphoma in real-world practice. This is not a novel biological hypothesis being tested for the first time — it is a case where the TxGNN model has correctly re-identified an existing, extensively validated drug–disease relationship. This should be flagged for the review team: the "prediction" here functions more as a validation signal for the model's reliability than as a genuine new-indication discovery.

Nonetheless, because this dataset lacks a formal original-indication text and MOA field (per data gaps DG001/DG002), the connection should still be treated as **evidence-supported but not formally regulatory-confirmed** until label data is obtained.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01476787](https://clinicaltrials.gov/study/NCT01476787) | Phase 3 | Completed | 1030 | RELEVANCE trial: Rituximab+Lenalidomide vs. Rituximab+Chemotherapy in previously untreated follicular lymphoma |
| [NCT06097364](https://clinicaltrials.gov/study/NCT06097364) | Phase 3 | Active, not recruiting | 733 | OLYMPIA-2: Odronextamab+chemo vs. Rituximab+chemo in untreated follicular lymphoma |
| [NCT05409066](https://clinicaltrials.gov/study/NCT05409066) | Phase 3 | Active, not recruiting | 549 | EPCORE FL-1: Epcoritamab+Rituximab+Lenalidomide vs. Rituximab+Lenalidomide in relapsed/refractory FL |
| [NCT04224493](https://clinicaltrials.gov/study/NCT04224493) | Phase 3 | Recruiting | 612 | Symphony-1: Tazemetostat/placebo + Lenalidomide+Rituximab in relapsed/refractory FL |
| [NCT01938001](https://clinicaltrials.gov/study/NCT01938001) | Phase 3 | Completed | 358 | Rituximab+Lenalidomide vs. Rituximab+Placebo in relapsed/refractory follicular/marginal zone lymphoma |
| [NCT00006721](https://clinicaltrials.gov/study/NCT00006721) | Phase 3 | Active, not recruiting | 571 | CHOP+Rituximab vs. CHOP+Tositumomab in newly diagnosed follicular NHL |
| [NCT00003204](https://clinicaltrials.gov/study/NCT00003204) | Phase 3 | Completed | 515 | Maintenance anti-CD20 antibody vs. observation after induction in low-grade lymphoma |
| [NCT01701232](https://clinicaltrials.gov/study/NCT01701232) | Phase 3 | Completed | 174 | Biosimilar rituximab (BCD-020) vs. MabThera monotherapy in CD20+ indolent NHL |
| [NCT00363636](https://clinicaltrials.gov/study/NCT00363636) | Phase 3 | Terminated | 340 | Galiximab+Rituximab vs. Rituximab+Placebo in relapsed/refractory follicular NHL |
| [NCT00460109](https://clinicaltrials.gov/study/NCT00460109) | Phase 2 | Completed | 24 | Denileukin diftitox + Rituximab in previously untreated follicular B-cell NHL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40306831](https://pubmed.ncbi.nlm.nih.gov/40306831/) | 2025 | RCT | Lancet Haematology | Long-term results: early rituximab monotherapy vs. watchful waiting improves time-to-next-treatment in advanced, asymptomatic, low tumour burden FL |
| [33249059](https://pubmed.ncbi.nlm.nih.gov/33249059/) | 2021 | Guideline | Annals of Oncology | ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up of newly diagnosed and relapsed FL |
| [28628883](https://pubmed.ncbi.nlm.nih.gov/28628883/) | 2017 | Review | Cancer Treatment Reviews | Pros and cons of rituximab maintenance therapy in follicular lymphoma |
| [36345167](https://pubmed.ncbi.nlm.nih.gov/36345167/) | 2022 | Systematic Review/Meta-analysis | J Clin Pharm Ther | Efficacy and safety of rituximab biosimilars vs. reference product as first-line therapy in low-tumour-burden FL |
| [31831752](https://pubmed.ncbi.nlm.nih.gov/31831752/) | 2019 | Review | Nature Reviews Disease Primers | Comprehensive review of follicular lymphoma biology and treatment |
| [35908982](https://pubmed.ncbi.nlm.nih.gov/35908982/) | 2023 | Review | Blood Reviews | Follicular lymphoma treatment landscape and path toward cure |
| [37061956](https://pubmed.ncbi.nlm.nih.gov/37061956/) | 2023 | Review | Leukemia & Lymphoma | Update on FL biology and optimal therapy |
| [36255040](https://pubmed.ncbi.nlm.nih.gov/36255040/) | 2022 | Review | American Journal of Hematology | 2023 update on FL diagnosis and management |
| [29314206](https://pubmed.ncbi.nlm.nih.gov/29314206/) | 2018 | Review | American Journal of Hematology | 2018 update on FL diagnosis and management |
| [12857561](https://pubmed.ncbi.nlm.nih.gov/12857561/) | 2003 | Review | Haematologica | Comprehensive review of rituximab efficacy as primary, relapsed, re-treatment, and maintenance therapy in FL |

---

## EU Market Information

No marketing authorizations are currently on file for Rituximab in this jurisdiction (market status: **Not Marketed**, 0 licenses recorded in this dataset).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Rituximab in follicular lymphoma is exceptionally strong (L1, multiple completed Phase 3 RCTs including a 1,030-patient trial), and the mechanistic rationale (anti-CD20 targeting of CD20+ malignant B cells) is directly documented in the evidence pack. However, because this signal largely reflects an already-established use rather than a novel indication, and because regulatory label data (MOA, warnings, contraindications) is missing (DG001, DG002), formal sign-off cannot proceed without confirming current label status.

**To proceed, the following is needed:**
- TFDA/EMA product label (SmPC) to confirm whether follicular lymphoma is already an approved indication in this jurisdiction
- Formal mechanism-of-action documentation (DrugBank or label-sourced)
- Confirmation of current marketing authorization status, since 0 licenses are recorded despite Rituximab being a globally marketed product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

