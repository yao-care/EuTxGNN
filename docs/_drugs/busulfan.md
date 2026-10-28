---
layout: default
title: Busulfan
parent: High Evidence (L1-L2)
nav_order: 116
evidence_level: L1
indication_count: 10
monitor_inn: "Busulfan"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "feline acquired immunodeficiency syndrome"]
last_modified_at: 2026-10-28
description: "Busulfan: predicted new indication Myelodysplastic syndrome (evidence level L1). Approved use: Conditioning treatment before conventional HPCT (BuCy2 in adults"
---

# Busulfan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Busulfan: From Conditioning Before Haematopoietic Cell Transplantation to Myelodysplastic Syndrome
{: .text-alpha }

## One-Sentence Summary

Busulfan is an alkylating chemotherapy agent. In the EU it is authorised as conditioning treatment before haematopoietic progenitor cell transplantation (HPCT) in adults and children.
The TxGNN model predicts it may be useful in **myelodysplastic syndrome (MDS)**, and the compiled data include **38 clinical trials** and **19 publications** on this direction, including two completed Phase 3 randomised trials. Almost all of this evidence concerns busulfan as part of transplant conditioning regimens, not as stand-alone therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Conditioning treatment before conventional HPCT (BuCy2 in adults; BuCy4 or BuMel in paediatric patients) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L1 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Busulfan is a bifunctional alkylating agent. It cross-links DNA and destroys bone marrow cells (myeloablation). Detailed mechanism-of-action data were not included in the compiled data, but this general mechanism is well established. In transplant conditioning it eliminates the abnormal blood-forming clone and clears marrow space for donor stem cells.

Allogeneic stem cell transplantation is the only potentially curative approach for MDS, and a conditioning regimen is required first. The approved use (conditioning before HPCT) is therefore closely related to the predicted use. The prediction describes busulfan-based conditioning in MDS patients undergoing transplant, not busulfan as a disease-modifying drug on its own.

MDS is not an approved indication for busulfan in the EU data compiled for this report. The link comes from the model prediction and the trial and literature evidence below.

## Clinical Trial Evidence

The table shows 10 of the 38 trials, chosen for direct relevance to busulfan-based conditioning in MDS.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Phase 3 | Completed | 240 | Randomised comparison of busulfan-TBI versus cyclophosphamide-TBI before sibling stem cell transplant in advanced MDS or MDS-related AML |
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Phase 3 | Completed | 570 | Treosulfan-based conditioning versus reduced-intensity busulfan-based conditioning in AML or MDS patients ineligible for standard conditioning |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | Recruiting | 324 | Venetoclax added to a fractionated busulfan regimen in high-risk AML and MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | G-CSF + decitabine + BuCy versus G-CSF + decitabine + BF conditioning in high-risk MDS |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | Same comparison in RAEB-1, RAEB-2 and AML secondary to MDS |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | Completed | 200 | IV busulfan plus fludarabine with allogeneic transplant in AML and MDS |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Venetoclax with timed sequential busulfan, cladribine and fludarabine before transplant in AML and MDS |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | Completed | 68 | Busulfan, fludarabine and anti-thymocyte globulin plus azacitidine in high-risk MDS and older AML patients |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | Unknown | 59 | Single-arm FLU-BU-MEL conditioning in MDS |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | Completed | 34 | Reduced-intensity busulfan/clofarabine conditioning before allogeneic transplant |

In most of these trials busulfan is one part of a combination regimen, so its individual contribution is hard to isolate. In NCT00822393, busulfan is the comparator arm.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (Phase 3) | The Lancet. Haematology | Non-inferiority trial of treosulfan versus reduced-intensity busulfan, each with fludarabine, in older AML/MDS patients |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT (Phase 3) | American Journal of Hematology | Final analysis of the same trial; event-free survival with treosulfan versus reduced-intensity busulfan |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (Phase 3) | The Lancet. Haematology | G-CSF + decitabine + BuCy versus BuCy conditioning on relapse in MDS and secondary AML |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | RCT (Phase 2) | Transplantation and Cellular Therapy | Two fractionation schedules of myeloablative busulfan with fludarabine and cladribine in AML or MDS |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Registry, propensity-matched | Bone Marrow Transplantation | Fludarabine/busulfan versus busulfan/cyclophosphamide myeloablative conditioning in MDS |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Registry, propensity-matched | Transplantation and Cellular Therapy | Myeloablative versus reduced-intensity fludarabine/busulfan in MDS |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Meta-analysis | Frontiers in Oncology | Long-term outcomes of treosulfan- versus busulfan-based conditioning in MDS and AML |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Meta-analysis | Frontiers in Oncology | Reduced-intensity versus myeloablative conditioning in AML and MDS |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | American Journal of Hematology | Allogeneic transplant is the only potentially curative therapy for MDS and myelofibrosis |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | Risk assessment | Pediatric Blood & Cancer | Evidence-based assessment of secondary malignancy risk after busulfan exposure |

## EU Market Information

| Authorization Number | Product Name | Approved Indication |
|---------|------|-----------|
| EMEA/H/C/002806 | Busulfan Fresenius Kabi | Busulfan Fresenius Kabi followed by cyclophosphamide (BuCy2) is indicated as conditioning treatment prior to conv... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (used for myeloablation) |
| Monitoring Items | Haematological parameters (complete blood count); please refer to the SmPC for the full monitoring schedule |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the SmPC warnings and precautions for emetogenicity classification.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The TxGNN knowledge graph records contraindication relations with epilepsy, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia and Fanconi anaemia), pulmonary fibrosis, hyperglycaemia, hyperuricaemia, potassium deficiency, and fungal, dermatophyte and other infectious diseases. These come from a knowledge graph, not from product labelling, and should be checked against the SmPC.
- **Drug Interactions:** The interaction screening returned 100 entries. Those with a stated severity level include metronidazole (Major), aprepitant and miconazole (Moderate), and levofloxacin (Minor). Many other entries have an unknown severity level.
- **Long-term risk:** A published risk assessment addresses subsequent malignancy after busulfan exposure (PMID 37856098).

Please refer to the SmPC for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 randomised trials and several Phase 2/3 trials directly study busulfan-based conditioning in MDS, and the use is mechanistically coherent with the approved conditioning indication. The evidence concerns combination transplant regimens, not busulfan alone, and MDS is not an authorised indication.

**To proceed, the following is needed:**
- The SmPC warnings and contraindications, which were not available in the compiled data
- Detailed mechanism-of-action data
- Evidence that isolates busulfan's contribution within combination regimens
- Review of the knowledge-graph contraindication relations (e.g., cytopenias, pulmonary fibrosis) against the label
- Dose and exposure monitoring plans for older or comorbid MDS patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

