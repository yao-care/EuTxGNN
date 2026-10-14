---
layout: default
title: Filgrastim
parent: AI Predictions (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Chemotherapy-Induced Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim (G-CSF) was originally used to shorten neutropenia and reduce febrile neutropenia in patients receiving cytotoxic chemotherapy, and to mobilise blood stem cells.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reduction in the duration of neutropenia and the incidence of febrile neutropenia in patients treated with established cytotoxic chemotherapy for malignancy (excluding chronic myeloid leukaemia and myelodysplastic syndromes); also PBPC mobilisation, severe chronic neutropenia, and persistent neutropenia in advanced HIV infection |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisations in the data compiled) |
| Number of Authorizations | 7 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Filgrastim is a recombinant G-CSF. It is known to act on the neutrophil lineage through the G-CSF receptor. Its efficacy in neutropenia is established.

The link to the predicted indication is weak. Primary release disorder of platelets is a disorder of platelet granule release and function. G-CSF has no established effect on platelet function. The very high TxGNN score reflects the knowledge-graph pattern rather than a biological rationale. The other top predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome and others) show the same pattern of platelet or coagulation disorders without a plausible G-CSF mechanism, and none has any trial or literature support.

## Clinical Trial Evidence

No trials were found for the top-ranked predicted indication. Currently no related clinical trials are registered.

For context, seven trials were retrieved for a lower-ranked prediction, platelet-type bleeding disorder (rank 10). All are stem cell transplantation protocols for haematologic malignancies. Filgrastim is likely only supportive care or mobilisation within these regimens, and none tests it as a treatment for a bleeding disorder. They were all graded low relevance (C).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Completed | 25 | Low-dose allogeneic PBSC transplant for high-risk low-grade haematologic malignancies |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Completed | N/A | CD34-enriched stem cell augmentation in allogeneic transplant for haematologic cancer |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Completed | 55 | Multiple cord blood unit transplant after non-myeloablative conditioning |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Withdrawn | 0 | Busulfan and fludarabine conditioning; no data (0 enrolled) |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Unknown | 35 | Non-myeloablative allogeneic transplant with matched unrelated donors |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Completed | 20 | T-cell depleted, reduced-intensity haploidentical transplant |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Completed | N/A | T-cell depleted partially matched related donor transplant with CD34 "veto" cells |

## EU Market Information

All seven EU authorisations are cancelled.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000825 | Ratiograstim | Not specified | Reduction in duration of neutropenia and febrile neutropenia in patients on cytotoxic chemotherapy; PBPC mobilisation; sever... |
| EMEA/H/C/000827 | Tevagrastim | Not specified | Reduction in duration of neutropenia and febrile neutropenia in patients on cytotoxic chemotherapy; PBPC mobilisation; sever... |
| EMEA/H/C/006400 | Zefylti | Not specified | Reduction in duration of neutropenia and febrile neutropenia in patients on cytotoxic chemotherapy; PBPC mobilisation; sever... |
| EMEA/H/C/000918 | Filgrastim Hexal | Not specified | Reduction in duration of neutropenia and febrile neutropenia in patients on cytotoxic chemotherapy; PBPC mobilisation; sever... |
| EMEA/H/C/003956 | Accofil | Not specified | Reduction in duration of neutropenia and febrile neutropenia in patients on cytotoxic chemotherapy; PBPC mobilisation; sever... |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, and the 20 reviewed were all of moderate severity. Examples include radiopharmaceuticals and radioimmunotherapy (iobenguane I-131, fludeoxyglucose F-18, ibritumomab tiuxetan, tositumomab), and cytotoxic or targeted anticancer agents (paclitaxel, mercaptopurine, azacitidine, bendamustine, arsenic trioxide, abemaciclib, acalabrutinib, alemtuzumab). Levamisole, aldesleukin and trimetrexate also appear.

For warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). There are no trials or publications for the predicted indication, and no plausible mechanism links G-CSF to platelet granule release. The only retrieved trials relate to a different, lower-ranked prediction, and they are transplant protocols with filgrastim as supportive care.

**To proceed, the following is needed:**
- Mechanism of action data for filgrastim, and a testable rationale for platelet function disorders
- Any preclinical or clinical evidence in platelet release disorders
- Warnings and contraindications from the SmPC for the safety screening
- Clarification of the EU market status, since all authorisations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

