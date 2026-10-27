---
layout: default
title: Teriflunomide
parent: High Evidence (L1-L2)
nav_order: 604
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Teriflunomide: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L1). Approved use: Relapsing-remitting multiple sclerosis (adults and paediatric patient…"
monitor_inn: "Teriflunomide"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "transient neonatal thrombocytopenia", "thrombocytopenia", "dense granule disease", "penile fibromatosis", "Ledderhose disease", "chronic hepatitis C virus infection", "palmar fibromatosis"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Teriflunomide: From Relapsing-Remitting Multiple Sclerosis to Relapsing-Remitting Multiple Sclerosis (Model Confirms the Existing Indication)
{: .text-alpha }

## One-Sentence Summary

Teriflunomide is an oral immunomodulator already approved in the EU for relapsing-remitting multiple sclerosis (RRMS) in adults and children aged 10 years and older.
The TxGNN model's top prediction is **relapsing-remitting multiple sclerosis**, which is the drug's existing indication rather than a new one. The data compiled for this report show **13 clinical trials** and **20 publications** for it, so the prediction agrees with established use.
The most credible genuinely new direction is **immune thrombocytopenia (ITP)**, currently at Phase 2 only, with no results yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing-remitting multiple sclerosis (adults and paediatric patients aged 10 years and older) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis (top-ranked prediction, identical to the approved indication) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Proceed with Guardrails |

> Note: the L1 level and the decision apply to the MS indication, which is already approved. For the one new-indication candidate with trial activity (thrombocytopenia/ITP), the evidence is L2 and the stage is a research question only.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the DrugBank-derived record compiled for this report. Based on the available literature, teriflunomide's active form inhibits the mitochondrial enzyme dihydroorotate dehydrogenase (DHODH). This limits de novo pyrimidine synthesis and reduces the proliferation of activated T and B lymphocytes, which drive the autoimmune damage in MS.

The top prediction is not a repurposing finding. It reflects the drug's existing, regulator-approved use, and the high score is consistent with that. It serves as a sanity check on the model rather than a new opportunity.

Among the other predictions, immune thrombocytopenia has a plausible mechanistic basis. The same lymphocyte-suppressing effect could reduce autoimmune platelet destruction. By contrast, most remaining predictions (rare inherited platelet disorders, fibromatoses such as Ledderhose disease and penile fibromatosis, and chronic hepatitis C) have no clinical evidence. Some may simply reflect shared phenotypes in the knowledge graph. For several of these, safety concerns argue against use, such as neonatal thrombocytopenia (teratogenicity) and hepatitis C (hepatotoxicity).

---

## Clinical Trial Evidence

**Relapsing-remitting multiple sclerosis (existing indication)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1088 | Placebo-controlled pivotal study of teriflunomide on relapse frequency and disability progression |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Teriflunomide (two doses) versus interferon beta-1a, rater-blinded, with long-term extension |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term safety extension of the pivotal study (7 mg and 14 mg doses) |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Ofatumumab versus first-line DMT (physician's choice, may include teriflunomide) in newly diagnosed RMS |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension of the Phase 2 study; safety and efficacy |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | Real-world observational effectiveness of teriflunomide over at least 2 years |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Mechanistic study on regulatory B lymphocytes as mediators of teriflunomide's effect |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | Early intensive versus escalation treatment strategies (indirectly relevant) |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Completed | 900 | Early aggressive versus escalation therapy; teriflunomide is part of the escalation comparator |
| [NCT07189325](https://clinicaltrials.gov/study/NCT07189325) | Phase 3 | Recruiting | 250 | Anti-CD20 maintenance versus de-escalation (not specific to teriflunomide) |

**Thrombocytopenia / immune thrombocytopenia (potential new indication)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07065968](https://clinicaltrials.gov/study/NCT07065968) | Phase 2 | Recruiting | 132 | Teriflunomide plus high-dose dexamethasone versus dexamethasone alone, first-line newly diagnosed ITP |
| [NCT06176911](https://clinicaltrials.gov/study/NCT06176911) | Phase 2 | Unknown | 124 | Teriflunomide plus danazol versus danazol in steroid-resistant or relapsed ITP |
| [NCT06190145](https://clinicaltrials.gov/study/NCT06190145) | Phase 2 | Unknown | 40 | Single-arm study of teriflunomide in steroid-resistant or relapsed ITP |
| [NCT06176235](https://clinicaltrials.gov/study/NCT06176235) | Phase 2 | Withdrawn | 0 | Teriflunomide plus dexamethasone in newly diagnosed ITP; withdrawn before enrolment, so provides no evidence |

---

## Literature Evidence

**Relapsing-remitting multiple sclerosis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurol | OPTIMUM: ponesimod versus teriflunomide, the first Phase 3 head-to-head of two oral DMTs in relapsing MS |
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | N Engl J Med | Ofatumumab versus teriflunomide in MS (teriflunomide as active comparator) |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | N Engl J Med | Ublituximab versus teriflunomide in relapsing MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | N Engl J Med | Tolebrutinib versus teriflunomide in relapsing MS |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurol | Evobrutinib versus teriflunomide in two Phase 3 trials |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Relative benefit of immunomodulators and immunosuppressants in RRMS |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide is effective and generally well tolerated, based on RCTs and real-world evidence; DHODH inhibition mechanism |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | Overview of MS diagnosis and treatment |
| [37578431](https://pubmed.ncbi.nlm.nih.gov/37578431/) | 2023 | Observational | Eur J Neurol | Real-world comparison of dimethyl fumarate and teriflunomide |
| [34046085](https://pubmed.ncbi.nlm.nih.gov/34046085/) | 2021 | Observational | Ther Adv Neurol Disord | Teriflunomide effectiveness and safety by age and pre-treatment status |

**Thrombocytopenia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34267852](https://pubmed.ncbi.nlm.nih.gov/34267852/) | 2021 | Case report | J Hematol | Leflunomide-induced thrombotic thrombocytopenic purpura; a safety signal for the drug class, not evidence of efficacy |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002514 | Aubagio | Not specified | Relapsing remitting multiple sclerosis in adults and paediatric patients aged 10 years and older... (cancelled) |
| EMEA/H/C/005960 | Teriflunomide Accord | Not specified | Relapsing remitting multiple sclerosis in adults and paediatric patients aged 10 years and older... (cancelled) |
| EMEA/H/C/005962 | Teriflunomide Viatris (previously Teriflunomide Mylan) | Not specified | Relapsing remitting multiple sclerosis in adults and paediatric patients aged 10 years and older (body weight > 40 kg)... (cancelled) |

All three authorizations are listed as cancelled in the data compiled for this report, so the current EU market status should be verified before any planning.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries. Most flagged as Major include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Antibiotics: clarithromycin, minocycline
  - Others: acetylsalicylic acid, pioglitazone, acarbose, bupropion, chenodeoxycholic acid, oxandrolone, oxymetholone
  - Moderate-level interactions include cimetidine, empagliflozin, sitagliptin and alosetron.

  The corticosteroid interactions matter for the ITP trials, which combine teriflunomide with high-dose dexamethasone.
- **Class concerns noted in the analysis**: hepatotoxicity (boxed warning), teratogenicity (contraindicated in pregnancy), and hematologic toxicity such as cytopenias, including a reported case of leflunomide-induced TTP.

Please refer to the SmPC for the full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- For RRMS, multiple Phase 3 trials and numerous head-to-head RCTs support teriflunomide (evidence level L1). It is an established therapy, so this is a confirmation rather than a repurposing candidate.
- For genuinely new indications, only ITP has trial activity (Phase 2, L2, no results). Teriflunomide can itself cause cytopenias, so ITP stays a research question. All other predictions have no supporting evidence and should be held.

**To proceed, the following is needed:**
- Verify the current EU authorization status, since all three licences are listed as cancelled.
- Obtain the SmPC warnings and contraindications, which are currently missing.
- Obtain detailed mechanism-of-action data from DrugBank.
- Follow the results of NCT07065968 and the other ITP trials, with careful hematologic and liver monitoring.
- Do not pursue the other predicted conditions (rare inherited thrombocytopenias, fibromatoses, hepatitis C) without supporting preclinical or clinical data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

