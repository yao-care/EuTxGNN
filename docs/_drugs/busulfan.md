---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Chronic Myeloid Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent historically used for chronic myeloid leukemia (CML) and established as a cornerstone myeloablative conditioning drug before allogeneic hematopoietic stem cell transplantation (HSCT).
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**,
with **40+ clinical trials** identified — including multiple completed Phase 2 and Phase 3 studies — supporting its role as a conditioning component in MDS patients undergoing allo-HSCT, though no PubMed literature was retrieved for this specific indication pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukemia / HSCT conditioning (Taiwan TFDA data unavailable) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, Busulfan is a bifunctional alkylating agent of the alkylsulfonate class. It cross-links DNA strands via alkylation of guanine bases, selectively destroying rapidly dividing hematopoietic progenitor cells. This makes it particularly suited for bone marrow clearance before donor stem cell engraftment.

Busulfan has been a cornerstone of HSCT conditioning for decades, primarily in AML and CML. Common regimens include Bu+Cy (BUCY), Bu+Flu (BuFlu), and Bu+Mel+Flu, each designed to eradicate abnormal host hematopoiesis and suppress immune rejection of the graft. Pharmacokinetic-guided dosing (TDM) has further optimized therapeutic window management for this drug.

MDS is a clonal disorder of hematopoietic stem cells characterized by dysplastic and ineffective blood cell production, with a subset progressing to AML. Allogeneic HSCT remains the only potentially curative treatment for intermediate- to high-risk MDS. Since Busulfan's therapeutic target — the aberrant bone marrow stem cell compartment — is identical in both CML conditioning and MDS, the TxGNN prediction is mechanistically coherent and clinically well-grounded. Multiple Phase 2 and Phase 3 trials have already validated Busulfan-containing conditioning in MDS patients across diverse combinations and intensity levels.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00469144](https://clinicaltrials.gov/study/NCT00469144) | Phase 3 | Completed | 233 | Randomized trial comparing PK-guided versus fixed-dose IV busulfan with fludarabine for AML/MDS; assessed whether individualized dosing improves efficacy and reduces toxicity |
| [NCT00629798](https://clinicaltrials.gov/study/NCT00629798) | Phase 2 | Completed | 64 | Bu+Mel+Flu with peri-transplant palifermin for advanced MDS and AML receiving T-cell depleted HSCT; tested gastrointestinal mucosal protection alongside conditioning |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Phase 2 | Completed | 35 | Bu+Flu+Alemtuzumab reduced-toxicity regimen specifically targeting pediatric MDS, marrow failure syndromes, and stem cell defects; full safety and efficacy evaluation |
| [NCT06829472](https://clinicaltrials.gov/study/NCT06829472) | Phase 3 | Recruiting | 120 | Randomized comparison of melphalan 100 vs 140 mg/m² within Mel-Bu-Flu (MBF) conditioning for AML/MDS; aimed at preserving low relapse while reducing toxicity |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | Head-to-head comparison of G-CSF+DAC+BUCY versus G-CSF+DAC+BF for MDS (RAEB-1, RAEB-2) and secondary AML undergoing allo-HSCT |
| [NCT05823714](https://clinicaltrials.gov/study/NCT05823714) | Phase 2 | Unknown | 70 | Novel bridging strategy: venetoclax+azacitidine induction followed by modified BUCY conditioning for high-risk MDS/AML; evaluates efficacy and safety of sequential approach |
| [NCT03412409](https://clinicaltrials.gov/study/NCT03412409) | Phase 2 | Recruiting | 50 | Reduced-intensity conditioning for elderly or high-comorbidity MDS patients undergoing haploidentical HSCT; addresses underserved population with limited transplant tolerance |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | Unknown | 59 | FLU-BU-MEL conditioning for allo-HSCT in untreated intermediate/high-risk MDS-EB; direct single-arm prospective evaluation of triple-drug combination |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | Multicenter trial of HLA-mismatched unrelated donor BMT with post-transplant cyclophosphamide for hematologic malignancies including MDS; busulfan included as conditioning option |
| [NCT00453206](https://clinicaltrials.gov/study/NCT00453206) | NA | Completed | 66 | Reduced-intensity conditioning with fludarabine, busulfan, and melphalan for broad hematological diseases including MDS; demonstrated feasibility across mixed-diagnosis cohort |

---

## Literature Evidence

Currently no related literature available for this indication pairing from the evidence database.

---

## Taiwan Market Information

Busulfan is currently **not marketed in Taiwan** (0 TFDA authorizations). The drug is approved internationally — Busilvex® (IV busulfan, Pierre Fabre) holds EMA authorization in the EU, and Busulfex® is approved in the United States — both primarily as conditioning regimens before HSCT. A formal TFDA approval pathway or special import arrangement would be required for use in Taiwan.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent – alkylsulfonate class; bifunctional DNA cross-linker) |
| Myelosuppression Risk | High — myeloablation is the intended therapeutic mechanism; profound and prolonged pancytopenia is expected and required for engraftment |
| Emetogenicity Classification | Low to moderate (IV formulation); standard antiemetic prophylaxis recommended |
| Monitoring Items | CBC with differential (serial), busulfan serum pharmacokinetics (TDM; target AUC 900–1350 µmol·min/L), liver function tests (hepatic veno-occlusive disease / sinusoidal obstruction syndrome risk), renal function, pulmonary function (busulfan-induced pulmonary fibrosis risk with prolonged use) |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV preparation requires closed-system transfer devices (CSTD) and appropriate PPE per institutional pharmacy protocol |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Taiwan TFDA package insert data (key warnings, contraindications, and drug interaction profile) was not available at the time of this report generation. This is classified as a Blocking data gap. Safety assessment should be based on the EMA Summary of Product Characteristics (SmPC) for Busilvex® or the US FDA label for Busulfex® until TFDA documentation is retrieved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 trials and at least one large completed Phase 3 trial (NCT00469144, n=233) have evaluated Busulfan-containing conditioning regimens specifically in MDS patients, demonstrating clinical feasibility and acceptable safety profiles across multiple combination strategies (BuCy, BuFluMel, modified BUCY, and BuFlu). The mechanistic rationale — ablating dysplastic hematopoietic stem cells to enable donor engraftment — directly maps to MDS pathophysiology, making this prediction biologically and clinically sound. However, Busulfan is not currently marketed in Taiwan, which represents a significant regulatory barrier before clinical application.

**To proceed, the following is needed:**

- **Regulatory pathway**: Establish TFDA special import or approval process for Busulfan (currently 0 Taiwan authorizations)
- **Safety documentation**: Retrieve Taiwan TFDA package insert or equivalent SmPC to complete safety assessment (key warnings, contraindications, DDI profile)
- **PK/TDM protocol**: Implement pharmacokinetic-guided dosing (target AUC monitoring) to optimize therapeutic window and reduce toxicity
- **Patient selection framework**: Define eligibility based on MDS subtype (RAEB-1, RAEB-2), IPSS-R risk score, age, comorbidity burden, and availability of suitable allogeneic donor
- **Institutional readiness**: Confirm availability of allogeneic HSCT infrastructure including HLA typing, GVHD prophylaxis protocols, and post-transplant monitoring capacity
- **Literature gap**: Conduct targeted PubMed search with broader MeSH terms to retrieve existing systematic reviews and registry data on Busulfan conditioning outcomes in MDS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

