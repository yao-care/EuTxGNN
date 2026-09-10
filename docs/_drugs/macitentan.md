---
layout: default
title: Macitentan
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Macitentan
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

# Macitentan: From Pulmonary Arterial Hypertension to Pulmonary Arterial Hypertension Associated with Congenital Heart Disease (CHD-PAH)

> **Note on indication selection**: TxGNN generated 10 candidate indications for Macitentan in this evidence pack. The single highest-scoring candidate (pulmonary arteriovenous malformation, score 98.9%) has **no supporting clinical trials or literature** and its own mechanistic rationale states the pathology is structural, not endothelin-driven — it is scored L5/Hold. This report instead focuses on **CHD-PAH (rank 2)**, the candidate with the strongest actual evidence (L1, Phase 3 data, multiple RCTs) and the most defensible mechanistic link to Macitentan's approved use in pulmonary arterial hypertension (PAH).

## One-Sentence Summary

> Macitentan is a dual endothelin receptor antagonist (ETA/ETB) approved for the long-term treatment of pulmonary arterial hypertension (PAH). The TxGNN model — supported by real clinical evidence — indicates it may also be effective for **PAH associated with congenital heart disease (CHD-PAH)**, a recognized WHO Group 1 PAH subtype, with **2 clinical trials** and **19 publications** (including two Phase 3 RCTs, MAESTRO and TOMORROW) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) — inferred from repurposing rationale text; official TFDA label text not yet available (see DG001) |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Congenital Heart Disease (CHD-PAH) |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L1 |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Macitentan is not directly available in this evidence pack (data gap DG002). However, the repurposing rationale fields consistently describe Macitentan as a **dual endothelin receptor antagonist (ETA/ETB)**, blocking endothelin-1–mediated pulmonary vascular vasoconstriction and smooth muscle proliferation — the core pathological mechanism underlying WHO Group 1 pulmonary arterial hypertension (PAH), which is Macitentan's established indication.

CHD-PAH is not a distinct disease but a **recognized clinical subtype of WHO Group 1 PAH**, arising from chronic left-to-right or right-to-left shunting in congenital heart disease that drives the same endothelin-mediated vascular remodeling seen in idiopathic PAH. Because the pathophysiology converges on the same endothelin pathway, the mechanistic rationale for Macitentan in CHD-PAH is strong — and in fact, Macitentan's pivotal SERAPHIN trial population already included CHD-PAH patients, and the Eisenmenger-syndrome subgroup (a severe CHD-PAH phenotype) was independently confirmed in the Phase 3 MAESTRO trial.

This is therefore less a novel mechanistic hypothesis and more a **subtype-extension repurposing case**: the drug's approved mechanism directly applies to a pathophysiologically related patient subgroup, which is reflected in the much richer clinical trial and literature base compared to the other, more speculative predictions in this pack (e.g., dermatological indications with no mechanistic or evidentiary support).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05179876](https://clinicaltrials.gov/study/NCT05179876) | Phase 3 | Recruiting | 280 | Open-label, long-term follow-up platform study for participants continuing pulmonary hypertension treatment (including Macitentan) after closure of parent studies; assesses long-term safety across PH populations, including CHD-PAH. |
| [NCT05731492](https://clinicaltrials.gov/study/NCT05731492) | Phase 1 | Withdrawn | 0 | Planned PK/safety study of Macitentan in children (1 month–2 years) with PAH; withdrawn before enrollment, contributes no data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28867027](https://pubmed.ncbi.nlm.nih.gov/28867027/) | 2017 | RCT | Heart, Lung & Circulation | Clinical evaluation of Macitentan specifically in PAH associated with congenital heart defects. |
| [30586694](https://pubmed.ncbi.nlm.nih.gov/30586694/) | 2019 | RCT (MAESTRO, Phase 3) | Circulation | Multicenter, double-blind, randomized, placebo-controlled 16-week trial of Macitentan in Eisenmenger syndrome (a CHD-PAH phenotype); evaluated efficacy and safety on exercise capacity. |
| [41796854](https://pubmed.ncbi.nlm.nih.gov/41796854/) | 2026 | RCT (TOMORROW) | The Journal of Pediatrics | Randomized trial of Macitentan vs standard of care in pediatric PAH, evaluating PK, efficacy, and safety. |
| [38276220](https://pubmed.ncbi.nlm.nih.gov/38276220/) | 2023 | Review | Journal of Personalized Medicine | Reviews current management of PAH-CHD, noting novel PAH-specific agents (including endothelin receptor antagonists) improve morbidity and mortality in this subgroup. |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic Review/Meta-analysis | Medicine | Evaluates the role of PAH-specific drug therapy, including endothelin receptor antagonists, in Eisenmenger syndrome. |
| [39585521](https://pubmed.ncbi.nlm.nih.gov/39585521/) | 2024 | Cohort (Real-world) | Cardiology and Therapy | OPUS/OrPHeUS real-world data on patient characteristics, treatment patterns, and outcomes in CHD-PAH patients newly initiating Macitentan. |
| [40616677](https://pubmed.ncbi.nlm.nih.gov/40616677/) | 2026 | Cohort | Pediatric Cardiology | Multicenter Spanish registry experience of oral Macitentan in pediatric PAH (Group 1), assessing safety and efficacy. |
| [36329372](https://pubmed.ncbi.nlm.nih.gov/36329372/) | 2023 | Cohort (Post-marketing) | Drugs - Real World Outcomes | Prospective multicenter post-marketing surveillance of Macitentan safety and clinical outcomes in Asian PAH patients. |
| [36196862](https://pubmed.ncbi.nlm.nih.gov/36196862/) | 2022 | Cohort | Anatolian Journal of Cardiology | Single-center comparison of Macitentan efficacy/safety and survival predictors between idiopathic and CHD-associated PAH. |
| [35514768](https://pubmed.ncbi.nlm.nih.gov/35514768/) | 2022 | Cohort (POTENT) | Pulmonary Circulation | Prospective assessment of PAH patients (including CTD/CHD subtypes) switched from bosentan to Macitentan. |

---

## EU/TW Market Information

Macitentan currently has **no marketing authorization on record in Taiwan** in this dataset (`market_status: 未上市`, 0 licenses). TFDA label and warning data collection is flagged as a blocking data gap (DG001) and has not yet been completed.

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data for Macitentan have not yet been collected for this market (blocking data gap DG001); these must be resolved before any clinical safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CHD-PAH is a well-established subtype of Macitentan's approved indication (PAH), supported by L1-level evidence including two Phase 3 RCTs (MAESTRO in Eisenmenger syndrome, TOMORROW in pediatric PAH) and multiple real-world cohort studies (OPUS/OrPHeUS, Asian post-marketing surveillance). The mechanistic rationale is strong and evidence is substantially more mature than the other candidates in this prediction set.

**To proceed, the following is needed:**
- TFDA-approved label text, warnings, and contraindications for Macitentan (DG001, blocking)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Confirmation of Taiwan marketing/licensing status, since current data shows 0 licenses despite global approval
- Drug-drug interaction data, currently unavailable (`ddi.query_status: not_found`)
- A formal safety monitoring plan for the CHD-PAH population, particularly for pediatric and Eisenmenger-syndrome subgroups

*Note: Other PAH-subtype predictions in this pack (CTD-PAH, L3; HIV-PAH, L4) share the same endothelin mechanistic logic and may warrant secondary consideration, while the non-PAH predictions (pulmonary arteriovenous malformation, alopecia-related conditions) lack both mechanistic plausibility and evidentiary support and are not recommended for further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

