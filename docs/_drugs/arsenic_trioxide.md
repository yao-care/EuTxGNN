---
layout: default
title: Arsenic Trioxide
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide: From Acute Promyelocytic Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Arsenic trioxide (ATO) is a well-established treatment for Acute Promyelocytic Leukemia (APL), exerting its effect through apoptosis induction and forced differentiation of malignant promyelocytes. The TxGNN model predicts it may be effective across the **Myelodysplastic Syndrome (MDS)** spectrum — the single most evidence-rich predicted indication — supported by **24 clinical trials** and **20 publications**, including a 2025 randomized controlled trial and a 2023 systematic meta-analysis directly evaluating ATO in MDS. Among all 10 predicted indications, MDS (rank 6) carries the strongest clinical evidence base and an actionable **"Proceed with Guardrails"** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Promyelocytic Leukemia (APL) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed (TFDA) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured source (DrugBank query pending). Based on established pharmacology, arsenic trioxide (As₂O₃) is an inorganic cytotoxic compound with multi-target activity originally proven in APL, where it degrades the PML-RARα fusion protein, generates reactive oxygen species (ROS) to trigger mitochondrial apoptosis, and forces malignant promyelocytes to mature into normal white cells.

APL and MDS share a common origin: both arise from clonal dysfunction of bone marrow myeloid progenitor cells. ATO's mechanisms extend naturally into the MDS context through at least four pathways: **(1) Apoptosis induction** — downregulation of Bcl-2/NF-κB anti-apoptotic signalling in dysplastic myeloid clones; **(2) Differentiation promotion** — aberrant myeloid precursors are pushed toward maturation, reducing blast burden; **(3) Immune modulation** — correction of abnormal Treg proportions and re-balancing of the IFN-γ/IL-17/TGF-β1 cytokine axis implicated in immune-mediated MDS variants; **(4) Epigenetic synergy** — cooperative DNA demethylation when combined with hypomethylating agents (decitabine or azacitidine), validated both in vitro (PMID 30898879) and in a 2025 RCT (PMID 40167011).

It is also notable that TxGNN simultaneously predicted multiple MDS-spectrum conditions among its top-10 outputs (unclassified MDS, refractory cytopenia of childhood, aregenerative anemia, 5q− syndrome), suggesting the model identifies a coherent mechanistic signal across the entire bone marrow failure landscape rather than an isolated statistical artefact. This convergent pattern strengthens confidence in the biological plausibility of ATO repurposing for MDS.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00093366](https://clinicaltrials.gov/study/NCT00093366) | Phase 1/2 | Completed | 32 | ATO + etanercept (TNF-α inhibitor) for advanced MDS; completed with efficacy and safety readouts, directly addressing ATO in MDS |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2,000 | Largest trial in this data set; elderly AML and high-risk MDS patients, testing gemtuzumab ozogamicin, tipifarnib, and ATO-based combinations; provides Phase 3-level context |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | Completed | 92 | Randomized three-arm study: decitabine vs. decitabine + carboplatin vs. decitabine + ATO for relapsed/refractory and elderly AML/MDS; provides direct comparative evidence for ATO add-on benefit |
| [NCT00195104](https://clinicaltrials.gov/study/NCT00195104) | Phase 1/2 | Completed | 87 | ATO + low-dose cytarabine in high-risk MDS and poor-prognosis AML; 17% complete remission rate, tolerable toxicity profile |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | Completed | 13 | Decitabine + ATO + ascorbic acid triple combination in MDS and AML; safety and feasibility confirmed |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | Completed | 30 | ATO + gemtuzumab ozogamicin for advanced MDS; completed with safety and response data |
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | Completed | 7 | Pilot study of decitabine + ATO + ascorbic acid in MDS; triple combination safety confirmed |
| [NCT00020969](https://clinicaltrials.gov/study/NCT00020969) | Phase 2 | Terminated | N/A | ATO monotherapy MDS-specific trial; terminated early, limiting conclusions but confirming biological interest |
| [NCT00803530](https://clinicaltrials.gov/study/NCT00803530) | Phase 2 | Terminated | 55 | Multicenter ATO + ascorbic acid in MDS; terminated with partial accrual, provides safety signal data |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | Recruiting | 30 | Oral ATO (Arsenol®) + ascorbic acid for previously untreated or relapsed/refractory TP53-mutated AML/MDS/CMML; active 2025 trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | Meta-analysis | Hematology (Amsterdam) | Systematic review and component network meta-analysis of ATO-containing regimens in MDS; evaluates overall efficacy and adverse event profiles across multiple combination strategies |
| [40167011](https://pubmed.ncbi.nlm.nih.gov/40167011/) | 2025 | RCT | Hematology (Amsterdam) | Randomized controlled trial of decitabine + ATO versus decitabine monotherapy in elderly high-risk MDS; demonstrates superior outcomes with the combination approach |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase 1/2 clinical | Leukemia Research | ATO + low-dose cytarabine in 49 previously untreated intermediate-2/high-risk MDS patients; 17% CR including patients with unfavorable cytogenetics |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | Review | Curr Hematol Malignancy Rep | Comprehensive review of ATO as MDS treatment covering pro-apoptotic, antiproliferative, and anti-angiogenic mechanisms and clinical trial landscape |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | Review | Clin Lymphoma Myeloma | Summary of ATO clinical data in leukemia and MDS; >80% CR in relapsed APL, extrapolation rationale to MDS |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | Comparative clinical | Immunopharmacol Immunotoxicol | Comparative immunological characterization of oral vs. IV arsenic in MDS murine model; delineates immune reprogramming differences relevant to treatment optimization |
| [30898879](https://pubmed.ncbi.nlm.nih.gov/30898879/) | 2019 | In vitro mechanistic | J Investig Med | Decitabine + ATO induces synergistic apoptosis in MUTZ-1 and SKM-1 MDS cells via endoplasmic reticulum stress; provides combination mechanistic rationale |
| [22964015](https://pubmed.ncbi.nlm.nih.gov/22964015/) | 2012 | Mechanistic/Clinical | J Hematol Oncol | ATO + ascorbic acid modulates BCL2 family apoptotic gene expression in primary MDS bone marrow samples (ex vivo, n=12); validates in vivo apoptotic mechanism |
| [16105982](https://pubmed.ncbi.nlm.nih.gov/16105982/) | 2005 | Mechanistic | Blood | NF-κB and FLIP upregulation in advanced MDS cells; ATO-induced apoptosis via NF-κB suppression validated in primary patient CD34+ cells |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | Clinical | Leukemia Research | ATO + retinoic acid + thalidomide combination in higher-risk MDS; clinical efficacy and safety evaluation |

---

## Taiwan Regulatory Status

Arsenic trioxide is currently **not marketed in Taiwan (TFDA)**. No domestic marketing authorizations were identified.

**International Reference**: ATO is approved as Trisenox® by the US FDA and EMA for the treatment of Acute Promyelocytic Leukemia (APL) — both relapsed/refractory and, in combination with ATRA, as front-line therapy for newly diagnosed low- to intermediate-risk APL.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic with targeted properties (inorganic arsenic compound; induces ROS-mediated apoptosis and differentiation in myeloid malignancies) |
| Myelosuppression Risk | Moderate — leukocytosis is characteristic during APL treatment (differentiation syndrome risk); in MDS, cytopenia worsening may occur early in treatment; CBC monitoring mandatory |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during induction), liver function (ALT/AST/bilirubin), renal function (creatinine/BUN), electrolytes (K⁺, Mg²⁺, Ca²⁺), QTc interval via ECG before initiation and during treatment, blood glucose |
| Handling Protection | Must follow cytotoxic drug handling regulations; arsenic-containing compounds require dedicated containment, PPE, and waste disposal per hazardous drug protocols |

---

## Safety Considerations

Please refer to the SmPC for safety information.

**Note**: TFDA label warnings and contraindications could not be retrieved (Data Gap DG001 — blocking). Based on established pharmacology, the following safety signals are well-characterised for ATO and should be verified against the formal label before any clinical application: **QTc prolongation** (potentially fatal arrhythmia risk; avoid with other QT-prolonging agents), **electrolyte disturbances** (hypokalemia and hypomagnesemia increase arrhythmia risk), **hepatotoxicity** (transaminase elevation), and **APL differentiation syndrome** (relevant to APL indication; monitor for respiratory distress in MDS patients with high blast counts who may develop a similar syndrome).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
ATO has demonstrated coherent multi-mechanism biological plausibility in the MDS setting, backed by a 2025 RCT and a 2023 network meta-analysis directly supporting its clinical utility — particularly in high-risk and elderly MDS in combination with decitabine. Multiple completed Phase 1/2 trials confirm a manageable safety profile in this population.

**To proceed, the following is needed:**

- **Resolve safety data gap first (blocking)**: Obtain and parse the TFDA drug label (SmPC) to complete the mandatory S1 safety gate assessment (DG001)
- **Clarify MOA data**: Query DrugBank API for structured mechanism of action data to strengthen the mechanistic narrative (DG002)
- **Define patient population**: Specify MDS subtype (IPSS-R low/intermediate vs. high-risk), TP53 mutation status, and prior treatment history as stratification variables — recent trials suggest TP53-mutated MDS as a particularly compelling subgroup
- **Select dosing strategy**: Evaluate IV (conventional) vs. emerging oral formulation (Arsenol®, currently recruiting in NCT06778187 and NCT06670222) based on Taiwan patient access and safety preferences
- **Establish cardiac safety protocol**: Pre-treatment ECG, electrolyte correction plan, and monitoring schedule (QTc) must be defined before initiating any Taiwan clinical investigation
- **Design a focused Taiwan feasibility study**: Given the existing Phase 2 evidence base globally, a prospective observational registry or a small randomized Phase 2 in Taiwan-eligible elderly high-risk MDS patients (decitabine ± ATO) would be appropriate next steps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

