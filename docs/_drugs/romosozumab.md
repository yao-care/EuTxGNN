---
layout: default
title: Romosozumab
parent: AI Predictions (L5)
nav_order: 536
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Romosozumab: predicted new indication Obsolete vitamin D deficiency (evidence level L5). Approved use: Severe osteoporosis in postmenopausal women at high risk of fracture"
monitor_inn: "Romosozumab"
predicted_indications: ["obsolete vitamin D deficiency", "calcium-alkali syndrome", "primary bone dysplasia with defective bone mineralization", "severe nonproliferative diabetic retinopathy", "renal osteodystrophy", "osteomalacia (disease)", "autosomal dominant neovascular inflammatory vitreoretinopathy", "Worth syndrome", "impaired renal function disease"]
---

# Romosozumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Romosozumab: From Severe Postmenopausal Osteoporosis to Impaired Renal Function Disease

## One-Sentence Summary

Romosozumab is a sclerostin-inhibiting antibody originally authorised in the EU for severe osteoporosis in postmenopausal women at high risk of fracture.
The TxGNN model's top-ranked prediction is **obsolete vitamin D deficiency**, but it has no supporting evidence and is flagged as an obsolete disease term.
The best-supported entry among the predictions is **impaired renal function disease** (rank 10), with **1 clinical trial** and **16 publications**. This evidence concerns using romosozumab for osteoporosis in patients with reduced kidney function, not treating the kidney impairment itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe osteoporosis in postmenopausal women at high risk of fracture |
| Predicted New Indication | Obsolete vitamin D deficiency (rank 1); the best-evidenced prediction is impaired renal function disease (rank 10) |
| TxGNN Prediction Score | 97.83% (rank 1); 91.50% (rank 10) |
| Evidence Level | L5 (rank 1); L2 (rank 10) |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails (rank 10, restricted to osteoporosis in CKD) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general knowledge, romosozumab is a monoclonal antibody that inhibits sclerostin. This increases bone formation and reduces bone resorption, which is why it is used in severe osteoporosis.

**Rank 1 (obsolete vitamin D deficiency):** No direct mechanistic link was identified. Romosozumab does not correct vitamin D status. The high score most likely reflects network proximity in bone metabolism, and the disease term is flagged as obsolete. The same applies to the other low-evidence predictions (calcium-alkali syndrome, defective-mineralisation bone dysplasia, osteomalacia, diabetic retinopathy, ADNIV, and Worth syndrome). Worth syndrome involves excess bone density from enhanced Wnt signalling, so romosozumab would be mechanistically unsuitable.

**Rank 10 (impaired renal function disease):** This entry is best read as osteoporosis in people with reduced kidney function. Chronic kidney disease (CKD) raises fracture risk, and sclerostin is elevated in CKD mineral and bone disorder. Pivotal-trial subgroup analyses in women with mild-to-moderate CKD and a meta-analysis across CKD stages support efficacy and safety for bone outcomes. These data do not show that romosozumab improves kidney function.

**Other entries with some literature:** Pregnancy-associated osteoporosis (rank 7, L4) is mechanistically plausible, supported by case reports and a 2026 position statement. Renal osteodystrophy (rank 5, L4) has only indirect, mostly cautionary review literature.

---

## Clinical Trial Evidence

Only the rank 10 prediction (impaired renal function disease) has a registered trial:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01833754](https://clinicaltrials.gov/study/NCT01833754) | Phase 1 | Completed | 24 | Single 210 mg subcutaneous dose in healthy participants and in those with stage 4 or stage 5 (haemodialysis) renal impairment; assessed safety, tolerability, and immunogenicity. Early-phase, no efficacy assessment. |

For the other predictions (including the top-ranked obsolete vitamin D deficiency), no related clinical trials are registered.

---

## Literature Evidence

Selected publications for rank 10 (impaired renal function disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35466448](https://pubmed.ncbi.nlm.nih.gov/35466448/) | 2022 | Post hoc analysis of RCTs (FRAME and ARCH) | J Bone Miner Res | Efficacy and safety of romosozumab in postmenopausal women with osteoporosis and mild-to-moderate CKD |
| [35639174](https://pubmed.ncbi.nlm.nih.gov/35639174/) | 2022 | Post hoc analysis of RCT (FRAME) | J Bone Miner Metab | Efficacy and safety in a Japanese subgroup with osteoporosis and CKD |
| [38972312](https://pubmed.ncbi.nlm.nih.gov/38972312/) | 2024 | Meta-analysis of RCTs | Kidney Blood Press Res | Efficacy and safety of anti-osteoporotic agents across CKD stages |
| [35304747](https://pubmed.ncbi.nlm.nih.gov/35304747/) | 2022 | Phase 1 PK/PD study | J Clin Pharmacol | Exposure was 31% and 43% higher in severe renal impairment and haemodialysis, respectively, versus normal renal function |
| [36330828](https://pubmed.ncbi.nlm.nih.gov/36330828/) | 2023 | Analysis (type not classified) | J Bone Miner Res | Cardiovascular safety of romosozumab in postmenopausal women with CKD |
| [42512844](https://pubmed.ncbi.nlm.nih.gov/42512844/) | 2026 | Retrospective cohort | Medicina (Kaunas) | Cardiovascular outcomes of romosozumab versus denosumab in CKD |
| [41171457](https://pubmed.ncbi.nlm.nih.gov/41171457/) | 2026 | Narrative review | Osteoporos Int | Efficacy and safety of romosozumab in CKD with osteoporosis |
| [29846712](https://pubmed.ncbi.nlm.nih.gov/29846712/) | 2019 | Review | Nephrol Dial Transplant | "Think first before you block it": caution about sclerostin blockade in CKD-MBD |
| [35980440](https://pubmed.ncbi.nlm.nih.gov/35980440/) | 2022 | Case report | Osteoporos Int | Romosozumab in a haemodialysis patient with severe osteoporosis |
| [40457078](https://pubmed.ncbi.nlm.nih.gov/40457078/) | 2025 | Review | Curr Osteoporos Rep | Management of osteoporosis in CKD |

Pregnancy- and lactation-associated osteoporosis (rank 7) is supported by case reports ([36676643](https://pubmed.ncbi.nlm.nih.gov/36676643/), [40978131](https://pubmed.ncbi.nlm.nih.gov/40978131/), [40330931](https://pubmed.ncbi.nlm.nih.gov/40330931/)) and a [2026 position statement](https://pubmed.ncbi.nlm.nih.gov/42464584/). No related literature is available for obsolete vitamin D deficiency.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004465 | Evenity | Not specified | Treatment of severe osteoporosis in postmenopausal women at high risk of fracture (status: cancelled) |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not label text): hypercalcaemia, nephrocalcinosis, and phosphorus metabolism disease.
- **Drug interactions:** 29 interactions were identified. The most significant is **Major** with etelcalcetide. Most others are **Moderate**, including:
  - Corticosteroids: hydrocortisone, prednisone, prednisolone, methylprednisolone, dexamethasone, betamethasone, budesonide, triamcinolone, deflazacort, fludrocortisone
  - Anti-angiogenic and oncology agents: bevacizumab, ramucirumab, axitinib, cabozantinib, pazopanib, regorafenib, dasatinib, lenalidomide, pomalidomide
- **Context from the literature:** Reviews report greater hypocalcaemia in advanced CKD (eGFR < 30 mL/min), attenuated bone response in CKD, and cardiovascular safety concerns.

Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (obsolete vitamin D deficiency); Proceed with Guardrails for the impaired renal function entry, limited to osteoporosis in CKD**

**Rationale:**
- The top predictions (ranks 1–4, 6, 8, 9) are model outputs only (L5), with no trials, no literature, and no plausible mechanism. Some are mechanistically contraindicated.
- The rank 10 entry has the strongest support (L2): a completed Phase 1 study and post hoc RCT analyses. However, it supports use for osteoporosis in people with reduced kidney function, not treatment of kidney impairment, and data in severe CKD or dialysis are limited.
- Pregnancy-associated osteoporosis and renal osteodystrophy (both L4) are research questions only.
- Evidence is not sufficient for the EU market, where the only authorisation is cancelled.

**To proceed, the following is needed:**
- Warnings and contraindications from the EMA product information (currently a blocking data gap)
- Mechanism of action data from DrugBank
- Clarification of why the EU authorisation was cancelled and the current regulatory status
- Controlled data in advanced CKD and dialysis, including cardiovascular, hypocalcaemia, and adynamic bone disease risks
- Dedicated trials or registries for pregnancy- and lactation-associated osteoporosis, if pursued
- Redefinition of the "impaired renal function" indication as osteoporosis in CKD, with a clear target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

