---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Pediatric Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine (Clolar/Evoltra) is a second-generation purine nucleoside analog, originally approved by the FDA (2004) and EMA (2006) for the treatment of relapsed or refractory acute lymphoblastic leukemia (ALL) in pediatric patients aged 1–21 years.
The TxGNN model predicts it may be effective for **Myeloid Leukemia** (including AML and CML blast crisis), with **50+ clinical trials** and **20 publications** supporting this direction.
The evidence base is exceptionally strong, anchored by a completed Phase 3 trial (NCT00703820, n=324), a large Phase 2/3 program (NCT00454480, n=2,000), and an ongoing randomized Phase 3 trial (FLUCLORIC, NCT05917405, n=302), placing this at the highest evidence level (L1).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory acute lymphoblastic leukemia (ALL) in pediatric patients (context from FDA/EMA approval; no EU authorizations recorded in current database) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| EU Market Status | Not confirmed (0 authorizations in current database) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clofarabine is a halogenated purine nucleoside analog specifically engineered to combine the best pharmacological properties of fludarabine and cladribine while overcoming their respective weaknesses. Once taken up by cells, it is phosphorylated by intracellular deoxycytidine kinase (DCK) to its active triphosphate form (CloFATP). CloFATP exerts cytotoxicity through two complementary mechanisms: first, inhibition of ribonucleotide reductase, which depletes the intracellular pool of deoxyribonucleoside triphosphates (dNTPs) required for DNA synthesis; and second, direct inhibition of DNA polymerases α and ε, halting replication and repair. Beyond these actions, clofarabine disrupts mitochondrial membrane integrity, triggering the intrinsic apoptosis pathway in a manner independent of cell-cycle phase. Its resistance to deamination by adenosine deaminase and to phosphorolysis also gives it superior metabolic stability compared to earlier-generation analogs.

The mechanistic link to myeloid leukemia is direct and well-characterized. AML blast cells characteristically overexpress DCK, making them highly efficient at converting clofarabine to its active form — this is the same biochemical vulnerability that makes ALL blasts sensitive, and it is equally prominent in the myeloid lineage. Both AML and ALL share the key features of rapid blast proliferation and heavy reliance on de novo DNA synthesis, making the purine nucleoside analog class broadly effective across acute leukemia subtypes. The pharmacological rationale for extending clofarabine's use from lymphoid to myeloid leukemia is therefore straightforward.

Clinical validation of this mechanistic reasoning is extensive. The AML08 trial (Phase 3, n=324) demonstrated that a clofarabine-based induction regimen can directly replace conventional anthracycline-etoposide combinations in childhood AML without compromising remission rates. The NCT00454480 program (Phase 2/3, n=2,000) explored clofarabine across a broad spectrum of older AML patients. The ongoing FLUCLORIC trial (Phase 3, n=302) is currently testing whether replacing fludarabine with clofarabine in pre-transplant conditioning improves outcomes in AML patients — retrospective data strongly favor clofarabine in this setting. Together, these studies represent the most robust translational bridge from the original ALL indication to the myeloid leukemia context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2,000 | Largest clofarabine AML programme: evaluated multiple drug combinations (including gemtuzumab ozogamicin and tipifarnib) in older AML and high-risk MDS patients; established clofarabine as a viable backbone for elderly-specific regimens |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | Completed | 324 | AML08: randomized Phase 3 in childhood AML comparing clofarabine+cytarabine versus conventional daunorubicin+etoposide induction; demonstrated clofarabine can replace anthracyclines and etoposide with comparable efficacy |
| [NCT05917405](https://clinicaltrials.gov/study/NCT05917405) | Phase 2/3 | Recruiting | 302 | FLUCLORIC: ongoing randomized Phase 3 comparing clofarabine/busulfan vs. fludarabine/busulfan as reduced-intensity conditioning before allogeneic SCT in AML; retrospective data favor clofarabine for anti-leukemic activity |
| [NCT00098033](https://clinicaltrials.gov/study/NCT00098033) | Phase 2 | Completed | 64 | Phase 2 pharmacodynamic study in AML, ALL, and CML accelerated/blast phase; established single-agent antileukemic activity and provided foundational pharmacodynamic data |
| [NCT01794702](https://clinicaltrials.gov/study/NCT01794702) | Phase 1/2 | Completed | 65 | Decitabine priming followed by clofarabine/idarubicin/cytarabine (CIA) in acute leukemia; demonstrated that epigenetic sensitization enhances clofarabine-based combination efficacy |
| [NCT01025154](https://clinicaltrials.gov/study/NCT01025154) | Phase 2 | Completed | 63 | Clofarabine+idarubicin+cytarabine (CIA) as induction in younger AML patients (18–60 years); assessed complete remission rates and safety of this triplet combination |
| [NCT00602225](https://clinicaltrials.gov/study/NCT00602225) | Phase 1/2 | Completed | 50 | Dose escalation of clofarabine+cytarabine+G-CSF priming in relapsed/refractory AML; established optimal dosing schedule for the CLAG-like regimen |
| [NCT00924443](https://clinicaltrials.gov/study/NCT00924443) | Phase 2 | Completed | 69 | Clofarabine monotherapy in older AML patients unsuitable for intensive chemotherapy; key trial supporting use in a population with limited treatment options |
| [NCT00067028](https://clinicaltrials.gov/study/NCT00067028) | Phase 2 | Completed | 116 | Randomized comparison of three clofarabine-containing regimens (with idarubicin and/or cytarabine) in first relapse or primary refractory AML and high-grade MDS |
| [NCT01252667](https://clinicaltrials.gov/study/NCT01252667) | Phase 2 | Completed | 44 | Clofarabine+low-dose TBI as conditioning for allogeneic PBSCT in AML; aimed to improve 6-month relapse rates following non-myeloablative transplant conditioning |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT | J Clin Oncology | AML08 Phase 3: Clofarabine+cytarabine can replace daunorubicin+etoposide in childhood AML induction; equivalent remission rates with reduced anthracycline cardiotoxicity exposure |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohort | Transplantation and Cellular Therapy | Clofarabine+busulfan (Clo/Bu4) myeloablative conditioning for active myeloid malignancies: acceptable toxicity profile with meaningful anti-leukemic activity in patients aged ≤70 years |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Clinical Study | Cancer Medicine | CLAM regimen (clofarabine+cytarabine+mitoxantrone) in R/R AML: high complete response rates and effective bridging to allogeneic HSCT in a Phase 2 study |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Clinical Study | Cancers | CLARA consolidation (clofarabine-based) vs. high-dose cytarabine in younger AML: clofarabine significantly improves relapse-free survival in patients with micro-complex karyotype |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leukemia & Lymphoma | Comprehensive review of clofarabine in AML: mechanism of action, pharmacology, and clinical data across monotherapy and combination strategies in first-line and salvage settings |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncology/Hematology | Role of clofarabine in adult AML: development from monotherapy to multi-drug combinations; summarizes promising results across multiple Phase 1/2 trial programs |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Clinical Study | American J Hematology | Phase I/II multisite trial: clofarabine+2 Gy TBI as non-myeloablative conditioning for allogeneic HCT in AML; improved 6-month relapse rate without excess toxicity |
| [18756533](https://pubmed.ncbi.nlm.nih.gov/18756533/) | 2008 | Clinical Study | Cancer | Clofarabine combinations with cytarabine and idarubicin as AML salvage therapy; established feasibility and efficacy with manageable toxicity in heavily pre-treated patients |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Clinical Study | Haematologica | Phase IB: clofarabine+high-dose cytarabine+liposomal daunorubicin in pediatric R/R AML; identified recommended Phase 2 dose, demonstrating combinability with anthracycline-containing regimens |
| [21182488](https://pubmed.ncbi.nlm.nih.gov/21182488/) | 2011 | Review | Current Medicinal Chemistry | Novel agents for AML including clofarabine: positions clofarabine among next-generation nucleoside analogs with superior stability vs. fludarabine and cladribine |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analog (second-generation halogenated adenosine analog; classified as antimetabolite) |
| Myelosuppression Risk | **High** — Clofarabine causes profound and prolonged myelosuppression; neutropenia, thrombocytopenia, and anemia are expected in virtually all patients receiving therapeutic doses; neutropenic fever and opportunistic infections are common serious adverse events |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (at minimum weekly during active treatment), hepatic function tests (ALT, AST, bilirubin), renal function (serum creatinine, eGFR), serum electrolytes (K⁺, Mg²⁺, PO₄³⁻), signs of systemic inflammatory response syndrome (SIRS) or capillary leak syndrome |
| Handling Protection | Must follow institutional cytotoxic drug handling regulations; personal protective equipment (PPE) required for preparation and administration; closed-system drug transfer devices (CSTDs) recommended |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information. No formal safety data (key warnings, contraindications, or drug-drug interactions) were captured in the current evidence pack for this drug.

Based on published clinical literature and the known class profile of purine nucleoside analogs, clinicians should be aware of the following safety signals associated with clofarabine:

- **Severe myelosuppression**: Expected in all patients; prolonged neutropenia increases infectious risk
- **Hepatotoxicity**: Elevated transaminases and hyperbilirubinemia have been reported; dose modification may be required
- **Systemic inflammatory response / capillary leak syndrome**: A recognized risk, particularly during rapid blast lysis; may require corticosteroid prophylaxis
- **Opportunistic infections**: Including fungal and bacterial infections secondary to prolonged neutropenia

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supporting clofarabine in myeloid leukemia is among the most robust in this repurposing dataset. A completed Phase 3 randomized trial (AML08, n=324) has already demonstrated that clofarabine-based regimens are equivalent to conventional anthracycline-based induction in childhood AML, and the ongoing FLUCLORIC Phase 3 trial (n=302) is actively testing its superiority in pre-transplant conditioning. The mechanistic rationale — AML blast overexpression of DCK enabling highly efficient clofarabine phosphorylation — is well-established and directly parallels the pharmacology underlying its approved ALL indication.

**To proceed, the following is needed:**

- **Safety data reconciliation**: Obtain the full SmPC / EMA Product Information for Evoltra (clofarabine) to formally document warnings, contraindications, and drug interactions for the safety assessment stage
- **EU market authorization verification**: Confirm current EU registration status — clofarabine (Evoltra, Sanofi/Genzyme) received EMA approval in 2006 for pediatric ALL but product availability may have changed; verify against current EMA database
- **MOA formal documentation**: Retrieve complete DrugBank mechanistic profile (DB00631) to satisfy the formal pharmacological data requirement
- **Patient population definition**: Specify target subpopulation for this indication (newly diagnosed AML vs. R/R AML; pediatric vs. adult; transplant-eligible vs. ineligible) to focus the clinical development or access pathway strategy
- **Competitive landscape assessment**: Evaluate current position of clofarabine-based regimens relative to recently approved AML therapies (venetoclax combinations, FLT3 inhibitors, IDH inhibitors) to identify best positioning strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

