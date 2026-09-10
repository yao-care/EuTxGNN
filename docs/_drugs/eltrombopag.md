---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Eltrombopag
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

# Eltrombopag: From Thrombocytopenia (ITP) to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is a thrombopoietin (TPO) receptor agonist originally used to raise platelet counts in chronic immune thrombocytopenia (ITP) and related thrombocytopenic conditions. The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **5 clinical trials** and **10 publications** currently associated with this pairing — though as detailed below, most of this evidence addresses managing thrombocytopenia *in* HIV patients rather than treating HIV itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocytopenia (ITP) — no formal EU label text available (regulatory data gap, see DG001) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured DrugBank MOA record is not yet available for this drug (data gap DG002). However, the evidence pack's own trial and literature annotations consistently describe eltrombopag as a **TPO receptor (MPL) agonist** used clinically to stimulate platelet production in ITP and other thrombocytopenic conditions. It has no known intrinsic antiviral pharmacophore.

The apparent link to HIV is largely **indirect**: HIV infection is a well-recognized cause of secondary immune thrombocytopenia and, less commonly, aplastic anemia, so eltrombopag has been used off-label to manage these hematologic complications in HIV-positive patients — not to treat the underlying viral infection. This distinction matters, because it suggests TxGNN's association may partly reflect comorbidity co-occurrence in the knowledge graph rather than a direct therapeutic mechanism against HIV.

One notable exception is an in vitro high-throughput screening study (PMID 32977702) that identified eltrombopag as a candidate modulator of HIV-1 proviral transcription — a preliminary mechanistic hypothesis that has not been validated in cellular models beyond the screen or in any clinical study. Taken together, the mechanistic rationale supports eltrombopag's role in *supportive care* for HIV-associated cytopenias with a speculative, unconfirmed direct antiviral hypothesis layered on top.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Open-label rollover safety/tolerability study in HCV-related thrombocytopenia (ITP), enabling antiviral therapy initiation — not HIV-specific (relevance grade C). |
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Double-blind, placebo-controlled trial reducing platelet transfusion need in chronic liver disease patients undergoing invasive procedures — terminated early, no direct HIV relevance (grade C). |
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | Placebo-controlled ITP pivotal trial in HCV thrombocytopenia to enable antiviral therapy (peginterferon alfa-2b + ribavirin) — HIV not a study condition (grade C). |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | Open-label study raising platelet counts in HCV-related thrombocytopenia with compensated cirrhosis — not HIV-focused (grade C). |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | Placebo-controlled ITP pivotal trial in HCV thrombocytopenia (peginterferon alfa-2a + ribavirin) — HIV not a study condition (grade C). |

**Note:** None of the five registered trials were designed to test efficacy against HIV infection; all target thrombocytopenia in hepatitis C / liver disease populations and are only indirectly relevant via shared TPO-agonist pharmacology.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematology/Oncology Clinics of North America | Reviews infectious causes (HCV, HIV, H. pylori) of chronic immune thrombocytopenia; treating the underlying infection often improves platelet counts. |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Seminars in Hematology | Reviews therapeutic strategies for infection-related (including HIV) immune thrombocytopenia. |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Review | Internal Medicine Journal | Reviews TPO-receptor agonist use in ITP of less than 6 months' duration. |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Cohort (registry) | Platelets | Danish registry of off-label TPO-receptor agonist use in refractory ITP, including secondary cases. |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case series | Journal of the International Association of Providers of AIDS Care | Case series on TPO-receptor agonists (eltrombopag, romiplostim) as salvage therapy for refractory HIV-associated ITP after HAART optimization. |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case report | AIDS | Successful use of eltrombopag without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia. |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case report | AIDS | Successful treatment of HIV-associated severe aplastic anemia with eltrombopag; suggests an immunomodulatory effect (reduced Th1/Th17, increased Treg/Th ratio). |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case report | Journal of the College of Physicians and Surgeons Pakistan | Case of hepatitis B (not HIV) leading to megaloblastic anemia and severe thrombocytopenia; tangential relevance. |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case report | Farmacia Hospitalaria | Two case reports of eltrombopag for thrombocytopenia in chronic hepatitis C, not HIV. |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro screening | Viruses | High-throughput screen of FDA-approved drugs identifying eltrombopag as a candidate modulator of HIV-1 proviral transcription — preclinical hypothesis only, not clinically validated. |

---

## EU Market Information

Eltrombopag currently has **no EU marketing authorization on record** in this dataset (market status: Not Marketed, 0 authorizations). No product-level licensing data is available to tabulate.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and drug interaction data are marked as data gaps in the evidence pack — see DG001, a Blocking-severity gap that prevents a formal S1 safety assessment until TFDA/EMA label warnings are retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical trial and literature evidence for this pairing almost entirely addresses eltrombopag's established role in managing HIV-associated thrombocytopenia and aplastic anemia (a secondary complication), not a direct antiviral effect against HIV itself; the one mechanistic hypothesis for direct antiviral activity (PMID 32977702) is an unvalidated in vitro screening hit. Combined with a Blocking safety data gap and no EU marketing authorization, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA/EMA-sourced label warnings and contraindications (DG001, Blocking)
- A validated DrugBank/MOA record confirming mechanistic plausibility (DG002)
- Follow-up mechanistic or clinical work validating whether eltrombopag modulates HIV-1 proviral transcription in vivo, distinct from its known role in treating HIV-associated cytopenias

*Note: Nine additional candidate indications were returned for this drug (ranks 2–10), but eight are scored "Hold" at evidence level L5 (model prediction only, including two veterinary/animal-model diseases and one obsolete disease term) or L4 with weak/indirect literature support (rheumatoid arthritis, female breast carcinoma). None currently warrant separate reporting beyond this top-ranked candidate.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

