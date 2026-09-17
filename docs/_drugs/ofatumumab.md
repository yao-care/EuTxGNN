---
layout: default
title: Ofatumumab
parent: High Evidence (L1-L2)
nav_order: 429
evidence_level: L2
indication_count: 10
---

# Ofatumumab
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Ofatumumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

> Ofatumumab is a fully human anti-CD20 monoclonal antibody historically approved (as Arzerra) for chronic lymphocytic leukemia (CLL), though it is currently **not marketed in Taiwan** (0 licenses) and its Taiwan approved-indication text is not on file.
> Among 10 TxGNN-predicted indications in this evidence pack, the strongest and most clinically credible new signal is **Follicular Lymphoma**,
> supported by **16 clinical trials** (including one randomized Phase 2 trial) and **18 publications**.
> Note: several other TxGNN predictions in this pack (ranked #1, #2, #5) are CLL/SLL or its molecular subtypes — these likely overlap with ofatumumab's known historical indication rather than representing genuinely new repurposing opportunities; this is flagged as a probable data gap in the `original_indications` field.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan regulatory data (0 licenses on file). Evidence within this pack indicates ofatumumab was historically approved internationally as Arzerra for CLL, withdrawn from market in 2019 — this is contextual information, not TFDA-sourced |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.70% (score 0.99701, rank 3785) |
| Evidence Level | L2 |
| Market Status (Taiwan) | ✗ Not marketed (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field is a flagged data gap (DG002), but the mechanism can be reconstructed from the evidence pack's own trial and literature records: ofatumumab is a fully human IgG1κ monoclonal antibody that binds a distinct small-loop epitope on CD20, depleting CD20-positive B cells via complement-dependent cytotoxicity (CDC) and antibody-dependent cell-mediated cytotoxicity (ADCC) (PMID 18535937, 22830942, NCT01077622).

Follicular lymphoma (FL) and CLL are both CD20-positive, B-cell-lineage lymphoproliferative malignancies. Ofatumumab's efficacy was originally established in CLL (accelerated FDA approval 2009, EMA conditional approval 2010), and the same CD20-targeting mechanism is directly applicable to FL, which is also a CD20+ mature B-cell neoplasm.

The class analogy is strong: rituximab, the prototypical anti-CD20 antibody, is already standard of care in FL. Multiple prospective trials in this pack (front-line monotherapy, chemoimmunotherapy combinations, and a randomized Phase 2 comparison) directly test ofatumumab in FL populations, moving this beyond a purely mechanistic extrapolation into an indication with dedicated, disease-specific clinical evidence — unlike several other predictions in this pack (e.g., malignant spiradenoma, Langerhans cell histiocytosis) which lack any biological rationale for CD20 involvement.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 (Randomized) | Completed | 135 | CALGB 50904: ofatumumab+bendamustine vs. ofatumumab+bendamustine+bortezomib in untreated high-risk FL — highest-grade direct RCT evidence |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | Completed | 116 | Single-arm international multicenter trial of ofatumumab monotherapy in rituximab-refractory FL |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | Completed | 51 | CALGB trial of single-agent ofatumumab in previously untreated stage II–IV FL |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | Completed | 43 | Ofatumumab as initial systemic treatment for indolent B-cell lymphoma, including FL |
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | Terminated | 346 | Randomized ofatumumab+bendamustine vs. bendamustine monotherapy in rituximab-unresponsive indolent B-NHL |
| [NCT01294579](https://clinicaltrials.gov/study/NCT01294579) | Phase 2 | Completed | 49 | Ofatumumab+bendamustine followed by ofatumumab maintenance in relapsed indolent B-NHL (incl. FL) |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | Completed | 59 | Two-dose ofatumumab combined with CHOP in previously untreated FL |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | Completed | 110 | MIRO trial: radiotherapy ± ofatumumab in stage I/II FL, MRD-driven approach |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | Completed | 6 | Japanese safety/tolerability/PK study of ofatumumab in FL and CLL |
| [NCT01397591](https://clinicaltrials.gov/study/NCT01397591) | Phase 2 | Terminated | 3 | Ofatumumab+bortezomib in relapsed CD20+ DLBCL, FL, or MCL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT | Cancer | CALGB 50904: ofatumumab+bendamustine ± bortezomib in previously untreated high-risk FL |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Phase 2 Cohort | Br J Haematol | CALGB 50901: single-agent ofatumumab in untreated low/intermediate-risk FL |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Multicenter Cohort | Blood | Ofatumumab monotherapy in rituximab-refractory FL (n=116); ORR 13% |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Cohort | Lancet Haematology | FIL MIRO: local radiotherapy + MRD-driven ofatumumab in early-stage FL, final results |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Phase 2 Cohort | Br J Haematol | Ofatumumab + CHOP (O-CHOP) as frontline chemoimmunotherapy for FL |
| [24443277](https://pubmed.ncbi.nlm.nih.gov/24443277/) | 2014 | PK Study | J Clin Pharmacol | Population pharmacokinetics of ofatumumab across CLL, FL, and RA populations |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Phase 1/2 Trial | Blood | First clinical use of ofatumumab in relapsed/refractory FL |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Evidence Review | Clin Lymphoma Myeloma Leuk | Evidence-based review of anti-CD20 regimens in relapsed/refractory CLL, DLBCL, FL |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Review | Advances in Therapy | 20-year review of rituximab (anti-CD20 class) in B-cell hematologic malignancies |
| [21083037](https://pubmed.ncbi.nlm.nih.gov/21083037/) | 2010 | Review | Expert Rev Hematol | Emerging therapeutic strategies in follicular lymphoma |

---

## Market Authorization Information (Taiwan)

Currently no marketing authorization records are on file for ofatumumab in Taiwan (`taiwan_regulatory.total_licenses = 0`, `market_status = Not marketed`). No approved-indication text is available for extraction.

---

## Cytotoxicity

Ofatumumab is an antineoplastic biologic (anti-CD20 monoclonal antibody used for CD20+ B-cell malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy — targeted anti-CD20 monoclonal antibody (CDC/ADCC-mediated B-cell depletion, not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low as monotherapy; Medium when combined with chemotherapy backbones such as bendamustine, CHOP, or fludarabine-cyclophosphamide (as used in most trials above) |
| Emetogenicity Classification | Low (monoclonal antibody class; infusion-related reactions are the more relevant acute toxicity than emesis) |
| Monitoring Items | CBC with differential, infusion-reaction monitoring, hepatitis B reactivation screening (standard precaution for anti-CD20 agents), immunoglobulin levels |
| Handling Protection | Standard biologic infusion precautions; not classified under cytotoxic hazardous-drug handling regulations. Please refer to the SmPC for institution-specific protocols |

---

## Safety Considerations

No structured safety data is available in this evidence pack (`key_warnings`, `contraindications`, and `ddi` are all data gaps or empty).

> Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ofatumumab's efficacy in Follicular Lymphoma is supported by an L2 evidence base — one randomized Phase 2 trial and multiple single-arm Phase 1/2 studies with consistent mechanistic rationale (anti-CD20 activity established in CLL and validated by the rituximab class precedent in FL). However, the drug currently has zero marketing authorizations in Taiwan, and two blocking/high-severity data gaps (TFDA label warnings/contraindications, structured MOA) remain unresolved.

**To proceed, the following is needed:**
- TFDA product label (warnings, contraindications) — DG001, Blocking, required before any S1 safety assessment
- Structured MOA data from DrugBank — DG002, High priority
- Manual review of the `original_indications` data source: this pack shows an empty field despite trial/literature evidence (e.g., NCT00824265, NCT01313689) indicating a prior CLL indication history — likely a data extraction gap rather than a true absence of prior indication
- Regulatory pathway assessment for a currently unmarketed (Not marketed) product in Taiwan
- Clarification of whether TxGNN predictions ranked #1, #2, and #5 (CLL/SLL and its IGHV subtypes) represent genuinely new indications or rediscovery of the historical indication, before including them in any repurposing decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

