---
layout: default
title: Teriflunomide
parent: High Evidence (L1-L2)
nav_order: 583
evidence_level: L1
indication_count: 10
---

# Teriflunomide
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

# Teriflunomide: From No Documented Original Indication to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

> This evidence pack records no approved indication or authorization for teriflunomide in the regulatory dataset (0 licenses on file, market status "not marketed"), and the original mechanism-of-action field is also a data gap.
> The TxGNN model's top-ranked prediction is **Relapsing-Remitting Multiple Sclerosis (RRMS)**, supported by **27 clinical trials** and **20 publications** — including several completed Phase 3 RCTs.
> **Important caveat:** the literature evidence in this pack itself (e.g. PMID 26758290) states that teriflunomide (Aubagio®) has been licensed in the EU since 2013 specifically for RRMS. This means the "predicted new indication" is very likely the drug's **already-known, already-approved indication**, not a genuine repurposing signal — the empty regulatory license data appears to be a data gap rather than a reflection of clinical reality.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the regulatory license dataset (0 licenses on file) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed (per dataset — see discrepancy note below) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Data discrepancy note:** The regulatory record shows 0 EU authorizations and "not marketed," yet the literature evidence in this same pack (PMID 26758290) explicitly states teriflunomide has been EU-licensed for RRMS since August 2013, with the SmPC later expanded (Sept 2014) to include first clinical demyelinating events. This inconsistency should be reconciled against the EMA/EU register before any downstream decision relies on the "not marketed" status.

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in this dataset (`original_moa` = data gap). However, the evidence pack's own repurposing rationale supplies substantive mechanistic information: teriflunomide is a **dihydroorotate dehydrogenase (DHODH) inhibitor** that blocks de novo pyrimidine synthesis, selectively suppressing proliferation of rapidly dividing, activated T and B lymphocytes. This anti-proliferative, immunomodulatory action is the accepted core mechanism underlying its use in autoimmune-mediated demyelinating disease.

Multiple Sclerosis — specifically the relapsing-remitting subtype — is an immune-mediated, T/B-lymphocyte-driven neurodegenerative disease. Given teriflunomide's selective lymphocyte-proliferation-blocking mechanism, its applicability to RRMS is mechanistically direct rather than a distant cross-indication inference.

The critical interpretive point, however, is that this mechanistic fit is not novel: it reflects teriflunomide's well-established, already-approved use (as Aubagio®) for RRMS in the EU since 2013, corroborated by multiple pivotal trials (TEMSO, TENERE) and head-to-head Phase 3 comparator trials against newer agents (ofatumumab, ublituximab, tolebrutinib, ponesimod, evobrutinib). In other words, this TxGNN output functions here as a **validation case** — correctly recovering a known drug-disease relationship — rather than as a genuine repurposing candidate. Within this same evidence pack, a secondary, more novel signal is visible at a lower rank: teriflunomide combined with dexamethasone for **primary immune thrombocytopenia (ITP)**, which has active Phase 2 RCTs (e.g. NCT07065968) testing a use outside its known label — that candidate would warrant separate, dedicated evaluation as a true repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1,088 | TEMSO pivotal trial: randomized, double-blind, placebo-controlled study establishing teriflunomide's effect on relapse frequency and disability accumulation in relapsing MS; the key trial underpinning original approval |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term extension of the TEMSO trial documenting sustained safety, tolerability, and durability of efficacy on disability, relapse rate, and MRI outcomes |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | TENERE trial: rater-blinded comparison of teriflunomide vs interferon beta-1a on time to treatment failure, relapse frequency, and patient-reported outcomes |
| [NCT03302442](https://clinicaltrials.gov/study/NCT03302442) | N/A | Completed | 3,000 | Large real-world observational comparison (French MS Observatory) of dimethyl fumarate vs teriflunomide on clinical and MRI outcomes in RRMS |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: compares early intensive high-efficacy therapy vs escalation strategy to inform overall treatment philosophy in RRMS |
| [NCT06663189](https://clinicaltrials.gov/study/NCT06663189) | Phase 3 | Not yet recruiting | 200 | TWINS trial: randomized, open-label study evaluating disease-modifying therapy withdrawal in inactive RRMS patients aged ≥55 |
| [NCT06843382](https://clinicaltrials.gov/study/NCT06843382) | N/A | Not yet recruiting | 100 | ROOF-MS: real-world prospective cohort comparing teriflunomide vs dimethyl fumarate on physical and cognitive fatigability in MS |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension study assessing durability of teriflunomide's safety and efficacy in relapsing MS |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | Completed | 12 | Determined teriflunomide 14 mg concentration in serum and cerebrospinal fluid in RRMS patients |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Phase 4 open-label mechanistic study identifying regulatory B lymphocytes as central mediators of teriflunomide's therapeutic effect |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | N Engl J Med | ASCLEPIOS trials: compared anti-CD20 ofatumumab against teriflunomide in relapsing MS |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | N Engl J Med | ULTIMATE trials: evaluated ublituximab (B-cell depleting antibody) versus teriflunomide in relapsing MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | N Engl J Med | Compared BTK inhibitor tolebrutinib against teriflunomide for efficacy and safety in relapsing MS |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | RCT | CNS Drugs | Reviews the EU SmPC for teriflunomide, confirming EU licensure since August 2013 for RRMS, with key clinical/safety outcomes and prescribing considerations |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network Meta-analysis | Cochrane Database Syst Rev | Compares relative benefits of immunomodulators, immunosuppressants, and biologics (including teriflunomide) in RRMS |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM trial: first Phase 3 active-comparator study of ponesimod vs teriflunomide in relapsing MS |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | evolutionRMS1/2: Phase 3 trials comparing BTK inhibitor evobrutinib against teriflunomide in relapsing MS |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | RCT | Mult Scler | ASCLEPIOS I/II subgroup analysis: ofatumumab showed superior clinical and MRI outcomes vs teriflunomide in newly diagnosed, treatment-naive patients |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | General review of MS diagnosis and treatment, summarizing the evidence base for current disease-modifying therapies |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Comprehensive review of teriflunomide's efficacy and tolerability in RRMS, based on RCT and real-world evidence |

---

## EU Market Information

Currently no EU marketing authorization records are available in this dataset (0 licenses on file). This conflicts with literature evidence (PMID 26758290) indicating EU licensure since 2013; the regulatory database should be verified/reconciled.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Multiple completed Phase 3 RCTs (TEMSO, TENERE, and several active-comparator trials) provide L1-level evidence for teriflunomide's efficacy in RRMS, but this evidence supports a **known, already-approved indication** rather than a novel repurposing candidate. Regulatory and safety data gaps prevent this from being treated as a validated new-use decision at this stage.

**To proceed, the following is needed:**
- Product label warnings/contraindications (source: TFDA website; blocking gap — required before any safety pre-screening/S1 stage can proceed)
- Detailed mechanism-of-action data (source: DrugBank API; high-priority gap — needed to properly assess mechanistic linkage for lower-ranked, more novel candidates)
- Reconciliation of the "not marketed / 0 licenses" regulatory status against the EU approval history cited in the literature evidence
- If genuine repurposing value is the goal, separate dedicated evaluation of the immune thrombocytopenia (ITP) signal (rank 5 in this pack), which has active Phase 2 RCTs testing teriflunomide outside its known indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

