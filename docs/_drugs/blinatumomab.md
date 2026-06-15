---
layout: default
title: Blinatumomab
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Blinatumomab
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

# Blinatumomab: From B-cell Precursor Acute Lymphoblastic Leukemia to Primary Release Disorder of Platelets

## One-Sentence Summary

Blinatumomab is a bispecific T-cell engager (BiTE) antibody originally developed and approved for relapsed or refractory B-cell precursor acute lymphoblastic leukemia (B-ALL), as evidenced by multiple completed Phase 3 trials in that indication.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
however **no clinical trials or published literature** directly support this indication — and notably, thrombocytopenia is itself a known Grade 3–4 adverse effect of blinatumomab, raising significant mechanistic and safety concerns.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory B-cell precursor acute lymphoblastic leukemia (B-ALL) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 95.20% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, blinatumomab is a bispecific T-cell engager (BiTE) antibody that simultaneously binds CD19 on B cells and CD3 on T cells, directing cytotoxic T lymphocytes to eliminate CD19-positive B cells. Its established efficacy in B-cell precursor ALL is well-supported by completed Phase 2 and Phase 3 trials.

The predicted new indication — primary release disorder of platelets (α/δ-storage pool deficiency) — involves an intrinsic defect in platelet granule content or secretion, a pathology entirely unrelated to the CD19+ B-cell compartment. There is no established biological link between B-cell depletion and platelet granule function. Furthermore, blinatumomab's known safety profile includes Grade 3–4 thrombocytopenia in approximately 11% of patients, meaning administration to patients with an underlying platelet disorder could substantially worsen their hemorrhagic risk.

The TxGNN high prediction score most likely reflects network proximity effects within the knowledge graph (e.g., shared disease ontology nodes or co-occurrence in rare disease clusters) rather than a true biological rationale. This is a case where the model's graph-based signal does not translate to a clinically meaningful repurposing hypothesis.

---

## Clinical Trial Evidence

The two trials retrieved by keyword matching were returned due to the drug name ("blinatumomab"), not the indication. Neither trial investigates platelet release disorders.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04524455](https://clinicaltrials.gov/study/NCT04524455) | Phase 1b | Completed | 17 | Safety/tolerability of blinatumomab + AMG 404 (anti-PD-1) in adults with R/R B-ALL; evaluated MTD and RP2D of AMG 404. **Not relevant to platelet disorders.** |
| [NCT03476239](https://clinicaltrials.gov/study/NCT03476239) | Phase 3 | Completed | 121 | Efficacy/safety of blinatumomab in Chinese adults with R/R B-precursor ALL; assessed hematological CR/CRh rates. **Not relevant to platelet disorders.** |

> ⚠️ **Note**: Both trials match on drug name only. No trials for primary release disorder of platelets were identified.

---

## Literature Evidence

Currently no related literature available for the combination of blinatumomab and primary release disorder of platelets.

---

## Taiwan Market Information

Blinatumomab is not currently authorized or marketed in Taiwan. No TFDA licenses on record.

---

## Cytotoxicity

Blinatumomab is an antineoplastic immunotherapy agent indicated for hematological malignancy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Bispecific T-cell Engager (BiTE antibody) |
| Myelosuppression Risk | High — Grade 3/4 thrombocytopenia (~11%), neutropenia, and febrile neutropenia reported in pivotal trials |
| Emetogenicity Classification | Low (not a cytotoxic agent; nausea may occur but emetogenicity is minimal) |
| Monitoring Items | CBC with differential (mandatory), liver function tests, neurological assessment (cytokine release syndrome, neurotoxicity), renal function |
| Handling Protection | Administered as continuous IV infusion (cIV); follow institutional protocols for biologic/immunotherapy agents; standard safe handling precautions apply |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) and TFDA labeling for full safety information, as local prescribing data is not available in this evidence pack.

Of particular relevance to the predicted indication: **blinatumomab's known toxicity profile includes Grade 3–4 thrombocytopenia**, which directly and adversely overlaps with the target indication of a platelet release disorder.

---

## Full Predicted Indication Summary

For completeness, all 10 TxGNN-predicted indications are summarized below:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Link |
|------|---------|------------|----------------|----------------|-----------------|
| 1 | Primary release disorder of platelets | 95.20% | L5 | Hold | None — B-cell depletion is unrelated to platelet granule secretion; adverse thrombocytopenia risk |
| 2 | Glanzmann thrombasthenia | 95.02% | L5 | Hold | None — ITGA2B/ITGB3 genetic defect; no B-cell mechanism |
| 3 | Pseudo-von Willebrand disease | 94.13% | L5 | Hold | None — GPIbα gain-of-function mutation; no B-cell link |
| 4 | Drug-induced osteoporosis | 92.70% | L4 | Research Question | Indirect: blinatumomab may reduce cumulative steroid exposure in ALL treatment, potentially reducing bone loss as a secondary outcome |
| 5 | Severe nonproliferative diabetic retinopathy | 89.25% | L5 | Hold | No established B-cell pathway in DR pathology |
| 6 | Psoriasis | 88.92% | L5 | Hold | Theoretical risk of worsening via T-cell over-activation; prior B-cell depletion (rituximab) has inconsistent benefit in psoriasis |
| 7 | Ledderhose disease | 88.41% | L5 | Hold | TGF-β/myofibroblast fibrosis; no B-cell connection |
| 8 | Hemorrhagic disorder due to constitutional thrombocytopenia | 87.88% | L5 | Hold | Genetic platelet deficit; drug-induced thrombocytopenia risk outweighs benefit |
| 9 | Penile fibromatosis (Peyronie's disease) | 87.80% | L5 | Hold | TGF-β1 collagen fibrosis; no B-cell mechanism |
| 10 | Bleeding diathesis due to collagen receptor defect | 87.72% | L5 | Hold | GPVI/α2β1 genetic platelet activation defect; no immunological mechanism |

> **Notable observation**: Ranks 1–3, 8, and 10 all involve inherited or primary platelet/bleeding disorders. The clustering suggests a knowledge graph artefact (shared rare disease network neighborhood) rather than a genuine biological signal.
>
> **The only indication with any indirect biological rationale is Rank 4 (drug-induced osteoporosis)**, where blinatumomab's role as a chemotherapy-sparing immunotherapy could theoretically reduce steroid-driven bone loss in ALL patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (primary release disorder of platelets) has no biologically plausible mechanism connecting B-cell–targeted immunotherapy to platelet granule secretion defects, and blinatumomab's own toxicity profile includes clinically significant thrombocytopenia — making it contraindicated in a patient population with baseline platelet dysfunction. The nine remaining top-ranked indications share similar mechanistic disconnects or active safety concerns.

**The one exception worth noting:**
Rank 4 — **drug-induced osteoporosis** — carries an indirect research hypothesis: if blinatumomab reduces cumulative steroid exposure in ALL induction/consolidation regimens, bone mineral density preservation could be a secondary benefit. This merits a hypothesis-driven secondary endpoint in future ALL trials, not a standalone repurposing program.

**To move any indication forward, the following is needed:**

- **Mechanism of action data** (DrugBank API query; DG002 remediation): Required before any mechanistic link analysis can proceed
- **TFDA prescribing information** (DG001 remediation): Required for safety baseline, especially given the complete absence of local regulatory data
- **For Rank 4 only**: Review NCT07227584 full protocol to confirm whether bone density is a prespecified endpoint; if not, consider proposing it as an exploratory outcome in the next ALL trial amendment
- **Broader evidence sweep**: A dedicated ClinicalTrials.gov and PubMed search scoped to blinatumomab + bone density / osteoporosis / corticosteroid sparing in ALL populations
- **Safety review**: Formal assessment of whether blinatumomab's known thrombocytopenic adverse effect constitutes an absolute contraindication across all platelet disorder indications (Ranks 1–3, 8, 10)

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

