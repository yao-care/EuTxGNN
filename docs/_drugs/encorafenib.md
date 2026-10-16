---
layout: default
title: Encorafenib
parent: AI Predictions (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Encorafenib: predicted new indication Choroideremia (evidence level L5). Approved use: Unresectable or metastatic melanoma with a BRAF V600 mutation (with b…"
monitor_inn: "Encorafenib"
predicted_indications: ["choroideremia", "non-cutaneous melanoma", "epithelioid cell melanoma", "eyelid melanoma", "scrotum melanoma", "choroidal dystrophy, central areolar", "superficial spreading melanoma", "lentigo maligna melanoma", "balloon cell malignant melanoma", "acral lentiginous melanoma (disease)"]
---

# Encorafenib
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

# Encorafenib: From BRAF V600-Mutant Melanoma, Colorectal Cancer and NSCLC to Choroideremia (Top TxGNN Prediction) and Non-Cutaneous Melanoma (Best-Supported Prediction)

## One-Sentence Summary

Encorafenib is a BRAF inhibitor originally used, in combination with binimetinib or cetuximab, to treat BRAF-mutant melanoma, colorectal cancer and non-small cell lung cancer.
The TxGNN model's top-ranked prediction is **choroideremia** (97.10%), but it has **no clinical trials and no publications** and no plausible mechanistic rationale, so it is a likely model artifact.
The best-supported prediction is **non-cutaneous melanoma** (96.55%), with **3 related clinical trials** and **1 publication** (a case report).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unresectable or metastatic melanoma with a BRAF V600 mutation (with binimetinib); metastatic colorectal cancer with a BRAF V600E mutation after prior systemic therapy (with cetuximab); advanced NSCLC with a BRAF V600E mutation (with binimetinib) |
| Predicted New Indication | Choroideremia (rank 1 by TxGNN score); non-cutaneous melanoma assessed as the most relevant candidate (rank 2) |
| TxGNN Prediction Score | Choroideremia: 97.10%; non-cutaneous melanoma: 96.55% |
| Evidence Level | Choroideremia: L5; non-cutaneous melanoma: L2 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Choroideremia: Hold; non-cutaneous melanoma: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, encorafenib is a BRAF kinase inhibitor, used with a MEK inhibitor (binimetinib) or an EGFR antibody (cetuximab). Its efficacy in BRAF V600-mutant melanoma, colorectal cancer and NSCLC is reflected in its authorized indications.

**Choroideremia (rank 1).** This is an X-linked retinal degeneration caused by loss of function of the CHM (REP1) gene. It is not driven by BRAF/MAPK pathway activation. The high TxGNN score is most likely a graph-based artifact, and no mechanistic rationale supports using a BRAF inhibitor here.

**Non-cutaneous melanoma (rank 2).** BRAF V600-mutant melanoma is the approved setting for encorafenib plus binimetinib. Non-cutaneous subtypes such as mucosal melanoma that carry a BRAF V600 mutation share the same target biology. However, BRAF mutations are less frequent in these subtypes, and the tumour biology differs from cutaneous disease. A Phase 2 trial and indirect Phase 1 data support feasibility, but randomized evidence specific to non-cutaneous subtypes is lacking.

**Other melanoma-related predictions (ranks 3–10).** Several lower-ranked predictions are melanoma subtypes: epithelioid cell, eyelid, scrotal, superficial spreading, lentigo maligna, balloon cell and acral lentiginous melanoma. Each falls mechanistically within the approved melanoma indication when a BRAF V600 mutation is confirmed, but each lacks subtype-specific evidence. Central areolar choroidal dystrophy (rank 6) is an inherited retinal disorder with no BRAF/MAPK driver, and MEK/BRAF inhibitors are associated with ocular toxicity such as serous retinopathy, which argues against use.

---

## Clinical Trial Evidence

Choroideremia has no registered clinical trials. The trials below are for non-cutaneous melanoma (rank 2), plus one relevant trial listed under acral lentiginous melanoma (rank 10).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04045691](https://clinicaltrials.gov/study/NCT04045691) | N/A (non-interventional) | Recruiting | 750 | Real-world effectiveness, quality of life and safety of encorafenib plus binimetinib in BRAF V600-mutant unresectable or metastatic melanoma in Germany, Austria and Switzerland (BERING-MELANOMA) |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | Randomized EORTC study (EBIN): encorafenib plus binimetinib induction followed by ipilimumab plus nivolumab versus immunotherapy alone in BRAF V600-mutant melanoma |
| [NCT04511013](https://clinicaltrials.gov/study/NCT04511013) | Phase 2 | Recruiting | 112 | Randomized trial of encorafenib plus binimetinib plus nivolumab versus ipilimumab plus nivolumab in BRAF V600-mutant melanoma with brain metastases; not acral-specific, no results reported |
| [NCT02857270](https://clinicaltrials.gov/study/NCT02857270) | Phase 1 | Completed | 210 | Safety of the ERK1/2 inhibitor LY3214996 alone or combined with other agents in advanced cancer; encorafenib is only one possible partner (indirect evidence) |

---

## Literature Evidence

Only literature for non-cutaneous melanoma and the closely related melanoma subtypes was retrieved. Choroideremia has none.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case report | Pigment Cell & Melanoma Research | Epidermotropic metastatic melanoma presenting as eruptive primary melanomas, diagnosed by molecular profiling |
| [40878071](https://pubmed.ncbi.nlm.nih.gov/40878071/) | 2025 | Case report | South Dakota Medicine | Malignant melanoma developing during encorafenib plus cetuximab therapy for a gastrointestinal cancer, highlighting the need for skin monitoring |
| [31804055](https://pubmed.ncbi.nlm.nih.gov/31804055/) | 2021 | Case report/series | Italian Journal of Dermatology and Venereology | Mutational analysis of multiple second primary melanomas arising under BRAF inhibitors, consistent with paradoxical MAPK activation |
| [38590555](https://pubmed.ncbi.nlm.nih.gov/38590555/) | 2024 | Review | Advances in Ophthalmology Practice and Research | Personalized treatment concepts in extraocular (periocular) cancer |

These publications are indirect and mostly describe safety signals (new primary melanomas under BRAF inhibition) rather than efficacy.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004580 | Braftovi | Not specified | Melanoma (with binimetinib), colorectal cancer (with cetuximab), non-small cell lung cancer (with binimetinib), all with BRAF V600 mutation... |

The single authorization is recorded with a status of cancelled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BRAF kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions; skin examinations and ophthalmic monitoring are suggested by the retrieved literature and the known ocular toxicity of BRAF/MEK inhibitors |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 interacting drugs, of which 20 were reviewed. Major interactions include aprepitant, dexamethasone, clarithromycin, dolasetron and cisapride. Moderate interactions include famotidine, metformin, loperamide, bisacodyl, saxagliptin, empagliflozin, linagliptin, glyburide, granisetron, eliglustat, fidaxomicin, castor oil, glycerin, picosulfuric acid and polyethylene glycol with electrolytes.
- **Skin and second malignancies**: Case reports describe new primary melanomas during BRAF inhibitor therapy, probably from paradoxical MAPK activation in BRAF wild-type cells. Regular skin examination is advisable.
- **Ocular toxicity**: MEK/BRAF inhibitors are associated with ocular toxicity such as serous retinopathy, which is a concern for retinal indications.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for choroideremia (rank 1); Proceed with Guardrails for non-cutaneous melanoma (rank 2)**

**Rationale:**
- Choroideremia has no clinical or literature evidence and no mechanistic basis, so the high score is likely a model artifact (L5).
- Non-cutaneous melanoma is within the target biology of the approved melanoma indication and has Phase 2 trial support (L2), but no randomized evidence specific to non-cutaneous subtypes, and use should be restricted to confirmed BRAF V600 mutation.
- The EU authorization is recorded as cancelled, which needs clarification before any development plan.

**To proceed, the following is needed:**
- Confirmation of the current EU regulatory and market status (the only license is recorded as cancelled)
- Warnings and contraindications from the EU product information (SmPC)
- Mechanism of action data
- BRAF V600 mutation testing and subtype-specific efficacy data for non-cutaneous melanoma
- A skin and ocular safety monitoring plan, and review of the major drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

