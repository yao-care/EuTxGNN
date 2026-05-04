---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutated AML to Myelodysplastic/Myeloproliferative Disease

## One-Sentence Summary

Ivosidenib (Tibsovo) is an oral, first-in-class inhibitor of mutant IDH1, approved by the FDA for IDH1-mutated relapsed/refractory AML and cholangiocarcinoma, but not currently approved in Taiwan.
The TxGNN model's highest-evidence prediction suggests it may benefit patients with **Myelodysplastic/Myeloproliferative Disease (MDS/MPN overlap syndromes)**, supported by **5 clinical trials** at an **L2 evidence level**.

> **Note on ranking**: The TxGNN #1 prediction (bulbar polio, 99.31%) is assessed as a knowledge graph proximity artifact with no plausible IDH1 mechanistic basis. The MDS/MPN prediction (rank 7, 98.56%) carries the strongest clinical evidence in this evidence pack and is the primary subject of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | IDH1-mutated AML / cholangiocarcinoma (FDA-approved globally; no Taiwan authorization) |
| Predicted New Indication | Myelodysplastic/Myeloproliferative Disease |
| TxGNN Prediction Score | 98.56% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ivosidenib selectively inhibits the neomorphic IDH1 R132 mutant enzyme. Under normal conditions, IDH1 catalyzes the conversion of isocitrate to α-ketoglutarate (α-KG). The R132 gain-of-function mutation redirects this reaction to produce the oncometabolite 2-hydroxyglutarate (2-HG), which competitively inhibits α-KG-dependent dioxygenases—most importantly TET2 and histone demethylases—causing widespread epigenetic hypermethylation, blocked hematopoietic differentiation, and clonal expansion. Ivosidenib suppresses 2-HG production, restores TET2-dependent DNA demethylation, and allows leukemic progenitors to resume differentiation.

MDS/MPN overlap syndromes (chronic myelomonocytic leukemia [CMML], atypical CML, MDS/MPN-unclassifiable) share the same core pathobiology as IDH1-mutated AML: epigenetically driven differentiation arrest in clonal myeloid progenitors. IDH1 R132 mutations occur in approximately 5–8% of MDS/MPN cases. In this IDH1-mutated subset, the 2-HG–driven epigenetic silencing that arrests blast maturation in AML is mechanistically identical to the differentiation block seen in MDS/MPN progenitors—making ivosidenib's mechanism directly applicable.

Clinical practice further supports this rationale: the standard-of-care backbone for MDS/MPN (hypomethylating agents such as azacitidine) is precisely the combination arm being investigated in the pivotal Phase 1b/2 basket trial NCT03471260. The convergence of mechanism, mutation prevalence, and ongoing clinical investigation makes this one of the most biologically credible repurposing directions for ivosidenib beyond its approved indications.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03471260](https://clinicaltrials.gov/study/NCT03471260) | Phase 1b/2 | Recruiting | 96 | Ivosidenib + venetoclax ± azacitidine in IDH1-mutated hematologic malignancies; basket design includes MDS/MPN subtypes; evaluates safety, optimal dose, and efficacy of the triplet combination |
| [NCT02074839](https://clinicaltrials.gov/study/NCT02074839) | Phase 1 | Recruiting | 291 | Large dose-escalation and dose-expansion study of ivosidenib across advanced IDH1-mutated hematologic malignancies; four expansion cohorts expected to include MDS/MPN subgroups |
| [NCT04493164](https://clinicaltrials.gov/study/NCT04493164) | Phase 2 | Recruiting | 30 | CPX-351 liposomal chemotherapy + ivosidenib in IDH1-mutated AML or high-risk MDS; directly co-enrolls high-risk MDS patients alongside AML |
| [NCT04250051](https://clinicaltrials.gov/study/NCT04250051) | Phase 1 | Active, not recruiting | 2 | Ivosidenib + FLAG chemotherapy in relapsed/refractory IDH1+ AML; very limited enrollment (n=2); indirect reference value only |
| [NCT04603001](https://clinicaltrials.gov/study/NCT04603001) | Phase 1 | Active, not recruiting | 260 | LY3410738, a covalent IDH1/2 inhibitor (distinct from ivosidenib), across IDH1/2-mutated hematologic malignancies; provides class-level mechanistic support for IDH1 inhibition in MDS/MPN |

---

## Literature Evidence

Currently no related literature directly linking ivosidenib to MDS/MPN overlap syndromes is available in this evidence pack.

---

## Taiwan Market Information

Ivosidenib currently holds **no marketing authorization in Taiwan** (market status: 未上市). There are no Taiwan FDA (TFDA) licenses on record. Patients in Taiwan seeking access would require enrollment in a clinical trial or application for compassionate use / expanded access through TFDA.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective mutant IDH1 inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate; classic myelosuppression is not the primary concern—**differentiation syndrome** (febrile illness, respiratory distress, hypoxia during blast maturation) is the hallmark toxicity requiring vigilant monitoring |
| Emetogenicity Classification | Low (oral targeted agent, once-daily dosing) |
| Monitoring Items | CBC with differential, LFTs, serum bilirubin, ECG (QTc interval), coagulation panel; 2-HG plasma levels if available; daily clinical assessment for differentiation syndrome signs during the first 8 weeks |
| Handling Protection | Standard oral antineoplastic precautions apply; full cytotoxic IV handling protocols are not required |

---

## Safety Considerations

Formal TFDA prescribing information is not available as the drug is not approved in Taiwan. Based on the FDA-approved label and EMA scientific opinion, the following are the key safety signals:

- **Differentiation Syndrome**: The most important drug-specific risk; may be life-threatening. Manifests as fever, dyspnea, hypoxia, pulmonary infiltrates, or multi-organ dysfunction during the first weeks of treatment. Requires prompt corticosteroid treatment and temporary dose interruption.
- **QTc Prolongation**: ECG monitoring required at baseline, during the first month, and periodically thereafter. Risk is amplified with concomitant QTc-prolonging drugs.
- **Guillain-Barré Syndrome**: Rare but reported; neurological symptoms (ascending weakness, areflexia) warrant immediate evaluation and drug discontinuation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The IDH1 inhibition mechanism is directly applicable to the ~5–8% of MDS/MPN patients carrying IDH1 R132 mutations, and two Phase 1b/2 basket trials (NCT03471260, NCT04493164) are actively co-enrolling MDS patients, providing L2-level evidence that the clinical hypothesis is already being tested.

**To proceed, the following is needed:**

- **Resolve blocking data gap**: Obtain TFDA prescribing information (SmPC equivalent) via official PDF download and parsing to enable formal S1 safety assessment
- **Patient selection strategy**: Establish IDH1 R132 mutation testing protocol for MDS/MPN patients (NGS or ddPCR); this is a prerequisite for any biomarker-enriched trial design
- **Regulatory pathway**: Define Taiwan access route—NDA submission, compassionate use, or co-enrollment in an international basket trial (e.g., NCT03471260)
- **Sub-group data extraction**: Request IDH1-mutated MDS/MPN sub-group outcomes from NCT02074839 investigators to quantify response rate and durability in this subset
- **Safety management plan**: Formalize differentiation syndrome surveillance protocol and QTc monitoring plan prior to any expanded use in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

