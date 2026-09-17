---
layout: default
title: Encorafenib
parent: High Evidence (L1-L2)
nav_order: 217
evidence_level: L2
indication_count: 10
---

# Encorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Encorafenib: From BRAF-Mutant Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Encorafenib is a selective BRAF kinase inhibitor originally developed for BRAF V600E/K-mutant melanoma (in combination with binimetinib) and BRAF V600E-mutant metastatic colorectal cancer (with cetuximab). TxGNN's single highest-scoring prediction — **choroideremia** — is explicitly flagged in the evidence pack as a likely embedding artifact (word-similarity between "choroid" and "melanoma") with zero supporting trials or literature, so this report instead focuses on the strongest evidence-backed candidate among the top-10 predictions: **Non-Cutaneous Melanoma**, supported by **36 queried clinical trial records** (including the pivotal Phase 3 COLUMBUS trial) and **1 case report**.

> **Note on model output:** TxGNN's rank-1 prediction (choroideremia, score 97.10%) and several other top-10 predictions (scrotum melanoma, central areolar choroidal dystrophy) returned zero clinical trials and zero literature, and the evidence pack's own mechanistic analysis judges these as spurious. This report is built around rank-2 ("non-cutaneous melanoma", score 96.55%), the highest-ranked prediction that is also substantiated by real evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in this jurisdiction (0 EU/local marketing authorizations on file); globally approved indication (per trial data): BRAF V600E/K-mutant melanoma (+ binimetinib), BRAF V600E-mutant metastatic colorectal cancer (+ cetuximab) |
| Predicted New Indication | Non-Cutaneous Melanoma |
| TxGNN Prediction Score | 96.55% |
| Evidence Level | L2 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is marked as a data gap in this evidence pack, but the repurposing rationale attached to the predictions is internally consistent and can be relied on: Encorafenib is described as a **selective BRAF kinase inhibitor**, approved (in combination with binimetinib) for BRAF V600E/K-mutant melanoma, and separately (with cetuximab) for BRAF V600E-mutant metastatic colorectal cancer.

"Non-cutaneous melanoma" is a mechanistically adjacent indication to the drug's known approved use — it is the same tumor lineage (melanoma), differing mainly by anatomic site (mucosal, acral, ocular/periocular, etc.) rather than by tumor biology. The key caveat is that BRAF V600 mutation prevalence is substantially lower in non-cutaneous melanoma subtypes (roughly 5–15%) compared to cutaneous melanoma (roughly 40–50%), so applicability is real but is contingent on confirming BRAF V600 mutation status in the individual tumor rather than being assumed across the whole non-cutaneous melanoma population.

This is corroborated by the sub-entity predictions ranked lower in the same batch: acral lentiginous melanoma (rank 10, L2, "Proceed with Guardrails", supported by an actively recruiting Phase 2 RCT) and superficial spreading melanoma (rank 7, L4) both point to the same underlying mechanism, reinforcing that the signal is a genuine BRAF-pathway extension rather than noise — unlike the rank-1 choroideremia prediction, which has no plausible mechanistic link (choroideremia is a CHM-gene retinal degeneration unrelated to the BRAF/MAPK pathway) and no evidence trail.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01909453](https://clinicaltrials.gov/study/NCT01909453) | Phase 3 | Completed | 921 | Pivotal COLUMBUS trial: encorafenib + binimetinib vs. vemurafenib and encorafenib monotherapy in unresectable/metastatic BRAF V600-mutant melanoma — established the approved combination regimen. |
| [NCT05270044](https://clinicaltrials.gov/study/NCT05270044) | Phase 3 | Active, not recruiting | 815 | COLUMBUS-AD: adjuvant encorafenib + binimetinib vs. placebo/surveillance in fully resected Stage IIB/C BRAF V600E/K melanoma. |
| [NCT04657991](https://clinicaltrials.gov/study/NCT04657991) | Phase 3 | Active, not recruiting | 257 | Encorafenib + binimetinib + pembrolizumab vs. placebo + pembrolizumab in treatment-naive BRAF V600E/K-mutant advanced/metastatic melanoma. |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EORTC EBIN study: sequential encorafenib+binimetinib induction followed by nivolumab+ipilimumab vs. immediate immunotherapy in BRAF V600-mutant unresectable/metastatic melanoma. |
| [NCT03898908](https://clinicaltrials.gov/study/NCT03898908) | Phase 2 | Completed | 48 | Encorafenib + binimetinib activity before local treatment in BRAF-mutant melanoma with (a)symptomatic brain metastases. |
| [NCT02159066](https://clinicaltrials.gov/study/NCT02159066) | Phase 2 | Completed | 158 | LOGIC2: sequential encorafenib(LGX818)/binimetinib(MEK162) followed by rational combination with targeted agents after progression, in locally advanced/metastatic BRAF V600 melanoma. |
| [NCT05004350](https://clinicaltrials.gov/study/NCT05004350) | Phase 2 | Completed | 107 | Encorafenib + cetuximab vs. chemotherapy/cetuximab regimens in Chinese patients with BRAF V600E-mutant metastatic colorectal cancer — supports drug activity outside melanoma. |
| [NCT03911869](https://clinicaltrials.gov/study/NCT03911869) | Phase 2 | Terminated (13 enrolled) | 13 | Standard- vs. high-dose encorafenib + binimetinib in BRAF V600-mutant melanoma brain metastasis; stopped early, limits evidence strength. |
| [NCT03864042](https://clinicaltrials.gov/study/NCT03864042) | Phase 1 | Completed | 56 | Drug-drug interaction study of agents co-administered with encorafenib + binimetinib in BRAF V600-mutant melanoma/solid tumors. |
| [NCT01436656](https://clinicaltrials.gov/study/NCT01436656) | Phase 1 | Completed | 107 | First-in-human dose-escalation study of oral encorafenib (LGX818) in BRAF-mutant melanoma and BRAF-mutant metastatic colorectal cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case Report | Pigment Cell & Melanoma Research | Molecular profiling used to diagnose epidermotropic metastatic melanoma presenting as eruptive primary melanomas in a BRAF-inhibitor-treated patient; illustrates diagnostic overlap between metastatic and primary melanoma lesions. |

---

## EU Market Information

Currently no EU marketing authorization on file for Encorafenib in this dataset (0 licenses; market status: Not marketed/Not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective BRAF kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Encorafenib's approved mechanism (BRAF V600 kinase inhibition) is directly relevant to non-cutaneous melanoma, and the pivotal Phase 3 COLUMBUS trial plus two additional ongoing Phase 3 studies establish strong efficacy/safety data for BRAF V600-mutant melanoma broadly — but no trial in the dataset specifically stratifies or confirms activity in the non-cutaneous subtype, where BRAF mutation prevalence is markedly lower.

**To proceed, the following is needed:**
- Formal mechanism-of-action documentation from DrugBank (currently a data gap, DG002)
- TFDA/EMA label warnings and contraindications (currently a blocking data gap, DG001) before any S1 safety screening
- BRAF V600 mutation testing/confirmation protocol for non-cutaneous melanoma patients prior to treatment
- Subgroup or dedicated trial data specific to mucosal/acral/uveal melanoma populations
- Formal DDI review (current query returned "not found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

