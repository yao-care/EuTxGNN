---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From Hodgkin Lymphoma to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin (BV) is a CD30-targeting antibody-drug conjugate approved globally for relapsed/refractory classical Hodgkin lymphoma and systemic anaplastic large cell lymphoma (sALCL), though it currently holds no Taiwan regulatory authorization.
The TxGNN model predicts it may be effective for **follicular lymphoma**,
with **6 clinical trials** and **20 publications** currently supporting this direction, including one actively recruiting Phase 2 trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma / systemic anaplastic large cell lymphoma (globally approved; not registered in Taiwan) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Brentuximab vedotin is an antibody-drug conjugate (ADC) composed of an anti-CD30 monoclonal antibody (brentuximab) covalently linked to the potent cytotoxin monomethyl auristatin E (MMAE) via a protease-cleavable linker. Upon binding to CD30-expressing tumor cells, the conjugate is internalized, MMAE is released intracellularly, and microtubule polymerization is disrupted — inducing G2/M cell cycle arrest and apoptosis. This targeted delivery mechanism is the cornerstone of BV's utility across CD30-expressing malignancies.

Follicular lymphoma (FL) is a low-grade B-cell non-Hodgkin lymphoma that does not uniformly express CD30. However, CD30 expression is detectable in a clinically relevant subset — particularly in cases with higher tumor burden or during histological transformation to diffuse large B-cell lymphoma (DLBCL) or anaplastic large cell lymphoma (ALCL), where CD30 upregulation is well-documented. A case report (PMID 32476657) directly demonstrates BV achieving complete response in a Grade I FL that transformed to CD30+ ALK1− ALCL, illustrating this mechanistic pathway in real patients.

The prediction therefore carries a biologically grounded rationale, provided patient selection relies on prospective CD30 immunohistochemistry (IHC) screening. One ongoing Phase 2 trial (NCT04587687) is directly investigating BV plus bendamustine in relapsed/refractory FL, representing the most immediate clinical test of this hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | BV + bendamustine for R/R follicular lymphoma; currently enrolling; provides the most direct clinical evidence for this repurposing direction |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized trial of rituximab + bendamustine ± BV for R/R CD30+ DLBCL; terminated early but 25 patients enrolled provide partial efficacy signals applicable to the FL/DLBCL spectrum |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + rituximab as frontline for CD30+ and/or EBV+ lymphomas (FL eligible); terminated with 20 patients, providing preliminary safety data in a CD30-selected lymphoma population |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | Planned BV + bendamustine + rituximab for R/R CD30+ B-cell NHL including FL; withdrawn before enrollment — study design directly relevant but no efficacy data obtained |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Risk-stratified sequential rituximab + BV ± bendamustine for newly diagnosed CD20/CD30+ post-transplant lymphoproliferative disorder; withdrawn before enrollment |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | BV + pembrolizumab for recurrent PTCL; withdrawn — indirect relevance; suggests checkpoint inhibitor combinations merit consideration |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Phase 2 Study | Blood Advances | LYSA Phase 2 study of BV + gemcitabine (GBV) followed by BV maintenance in R/R PTCL; ORR evaluated after 4 induction cycles in CD30+ (≥5%) patients |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | Gulf J Oncology | Grade I FL transforming to CD30+ ALK1− ALCL — complete response achieved with BV + high-dose methotrexate; direct clinical demonstration of BV efficacy in FL transformation |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Prospective Clinical Study | Advances in Therapy | Real-world study of BV + CEP in untreated CD30+ PTCL (including TFH phenotype); high overall remission rates in CD30+ B/T-cell lymphomas |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Retrospective Cohort | Eur J Haematol | BV + ICE (ifosfamide, carboplatin, etoposide) for R/R PTCL; assessed BV combination efficacy in relapsed lymphoma with poor prognosis |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology (ASH Ed.) | Comprehensive review of BV and novel agents in PTCL management, including frontline and salvage settings |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Treatment of common nodal PTCL subtypes; documents BV + CHP as established frontline regimen for CD30+ disease |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Immunotherapy in indolent NHL including FL; reviews emerging roles of novel agents in FL treatment landscape |
| [41409526](https://pubmed.ncbi.nlm.nih.gov/41409526/) | 2025 | Case Report | Skin Appendage Disorders | Extensive alopecia mucinosa (folliculotropic mycosis fungoides) responding to BV; demonstrates activity in follicle-associated T-cell malignancy |
| [28340875](https://pubmed.ncbi.nlm.nih.gov/28340875/) | 2017 | Review | Hematol Oncol Clin N Am | Angioimmunoblastic T-cell lymphoma (T-follicular helper-derived); BV discussed as novel therapeutic approach |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplantation | Post-ASCT maintenance in lymphomas including FL; BV referenced in maintenance framework applicable to FL |

---

## Taiwan Regulatory Information

Brentuximab vedotin is currently **not registered or marketed in Taiwan**. No Taiwan FDA (TFDA) product licenses have been issued.

> Internationally, brentuximab vedotin (Adcetris®) has received regulatory approval in the United States (FDA), European Union (EMA), Japan (PMDA), and other jurisdictions for relapsed/refractory classical Hodgkin lymphoma and systemic anaplastic large cell lymphoma. Any clinical use in Taiwan for follicular lymphoma would require either a new TFDA approval application or an expanded access / compassionate use protocol.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (ADC); anti-CD30 antibody conjugated to MMAE (microtubule-disrupting cytotoxin; conventional cytotoxic payload) |
| Myelosuppression Risk | High — neutropenia is the most frequently reported serious adverse event; febrile neutropenia occurs; G-CSF prophylaxis is commonly employed |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (prior to each cycle), peripheral neuropathy assessment (clinical grading each visit), liver function tests, renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations; MMAE is a potent antimitotic agent — standard ADC/cytotoxic handling precautions apply |

---

## Safety Considerations

No Taiwan TFDA contraindication or warning data is available (TFDA SmPC not retrieved — classified as a blocking data gap per DG001). Based on published clinical literature, the following safety signals are established for brentuximab vedotin:

- **Peripheral neuropathy**: Cumulative, dose-limiting toxicity — both sensory and motor neuropathy are well-documented across trials; dose delays and reductions are frequently required
- **Severe neutropenia / febrile neutropenia**: The most common hematological toxicity; prophylactic G-CSF is recommended in many protocols
- **Progressive multifocal leukoencephalopathy (PML)**: Rare but potentially fatal JC virus reactivation has been reported; requires vigilance especially in immunocompromised patients
- **Pulmonary toxicity**: Non-infectious pneumonitis has been reported and may be treatment-limiting

Please retrieve the full TFDA SmPC or reference the EMA/FDA prescribing information for complete contraindications and drug interaction data before clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between BV and follicular lymphoma is biologically plausible via CD30 expression in a subset of FL patients (especially at transformation), and an actively recruiting Phase 2 trial (NCT04587687) provides direct prospective evidence generation. Evidence at L2 is sufficient to support continued development, but patient selection by CD30 IHC is essential and efficacy data from the ongoing trial remains awaited.

**To proceed, the following is needed:**
- **Results from NCT04587687**: This actively recruiting Phase 2 trial of BV + bendamustine in R/R FL is the critical evidence gate — monitor for interim and final readouts
- **CD30 IHC prevalence data in FL**: Characterize the proportion of FL patients with clinically meaningful CD30 expression (commonly defined as ≥10% or ≥1% by IHC) to estimate the eligible patient population in Taiwan
- **Taiwan TFDA approval or expanded access pathway**: BV is not registered in Taiwan; a regulatory strategy (new NDA or compassionate use) must be defined before any clinical application
- **Complete safety profile retrieval**: Download TFDA SmPC PDF (or EMA/FDA label) to address data gap DG001 (blocking) and enable full safety assessment
- **MOA confirmation via DrugBank API**: Address data gap DG002 (high severity) to support formal mechanistic rationale documentation
- **Dose and schedule optimization for FL**: Confirm whether standard BV dosing (1.8 mg/kg IV Q3W) is appropriate, or whether the weekly schedule (1.2 mg/kg QW) used in some ADC trials offers a better tolerability profile for indolent FL patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

