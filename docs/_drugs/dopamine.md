---
layout: default
title: Dopamine
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Dopamine
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

# Dopamine: From Vasopressor Use in Shock to Postural Orthostatic Tachycardia Syndrome (POTS)

## One-Sentence Summary

Dopamine (DrugBank DB00988) is an endogenous catecholamine classically used clinically as a vasopressor/inotropic agent in shock and severe hypotension — no formal EU-approved indication text is available in this evidence pack. The TxGNN model predicts a possible new role in **Postural Orthostatic Tachycardia Syndrome (POTS)**, currently supported by **6 clinical trials** and **7 publications**, though the trials found are largely mechanistic/physiological studies of endogenous renal dopamine rather than interventional trials testing dopamine as a POTS treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (`original_indications` is empty). Based on general pharmacological knowledge, dopamine hydrochloride is used as a vasopressor/inotropic agent in shock and hypotension — TFDA/EMA-specific indication wording is a documented data gap (DG001) |
| Predicted New Indication | Postural Orthostatic Tachycardia Syndrome (POTS) |
| TxGNN Prediction Score | 88.00% (raw score 0.8800; model rank 82,652) |
| Evidence Level | L4 (mechanistic/observational human studies; no direct interventional evidence of dopamine treating POTS) |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, dopamine is an endogenous catecholamine and biosynthetic precursor of norepinephrine; as dopamine hydrochloride injection, it is used for its vasopressor and positive inotropic effects via dopaminergic (D1/D2) and adrenergic (α/β) receptor activity, supporting blood pressure and cardiac output in shock states. This receptor pharmacology also plays a physiological role in autonomic regulation of heart rate, vascular tone, and renal sodium handling.

POTS is a disorder of autonomic/sympathetic dysregulation, frequently accompanied by impaired plasma volume expansion and abnormal renal sodium handling — processes in which the renal dopaminergic system is known to participate. This provides a plausible biological rationale for TxGNN's association between dopamine and POTS: both the original (presumed) use and the predicted indication converge on sympathetic nervous system and vascular/volume regulation.

However, it is important to note that the clinical trial evidence retrieved for this candidate largely investigates the *endogenous* renal dopaminergic system in POTS patients (e.g., using carbidopa to suppress dopamine synthesis, measuring urinary dopamine excretion, or studying dietary dopamine precursors) rather than administering dopamine itself as a therapeutic intervention for POTS. This is a meaningful distinction: the evidence supports a mechanistic link between the dopaminergic pathway and POTS pathophysiology, but does not directly demonstrate therapeutic benefit of dopamine administration in POTS patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00685919](https://clinicaltrials.gov/study/NCT00685919) | Phase 2/3 | Completed | 32 | Investigated how suppressing renal dopamine synthesis (via carbidopa) affects urinary sodium excretion in POTS patients vs. healthy volunteers — a mechanistic study, not a dopamine treatment trial |
| [NCT01563107](https://clinicaltrials.gov/study/NCT01563107) | N/A | Completed | 38 | Examined how dietary sodium intake affects urinary sodium and dopamine excretion in POTS patients, exploring renal dopaminergic involvement in plasma volume regulation |
| [NCT01547117](https://clinicaltrials.gov/study/NCT01547117) | N/A | Completed | 38 | Studied whether high-sodium diet appropriately expands plasma volume in POTS and how renin-angiotensin-aldosterone and renal dopamine respond |
| [NCT01064739](https://clinicaltrials.gov/study/NCT01064739) | Early Phase 1 | Completed | 14 | Characterized diuretic effects of dietary catecholamine sources (e.g., fava beans, which raise endogenous dopamine) on renal sodium handling |
| [NCT00001418](https://clinicaltrials.gov/study/NCT00001418) | N/A | Completed | 335 | Used PET imaging (fluorodopamine) to measure sympathetic nervous system activity in patients with neurocardiologic/autonomic disorders |
| [NCT00748228](https://clinicaltrials.gov/study/NCT00748228) | N/A | Terminated | 22 | Studied dopamine-beta-hydroxylase (DBH) genetic variation and its relationship to blood pressure/heart rate response and dietary sodium in orthostatic intolerance |

**Note:** None of the above trials test exogenous dopamine administration as a treatment for POTS; all are mechanistic/physiological studies of the endogenous dopaminergic system in POTS or related autonomic disorders.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29937049](https://pubmed.ncbi.nlm.nih.gov/29937049/) | 2018 | Systematic Review & Meta-analysis | Mayo Clinic Proceedings | Evaluates efficacy of existing POTS treatments overall; provides context for the current lack of clearly beneficial therapies but does not specifically evaluate dopamine |
| [12403667](https://pubmed.ncbi.nlm.nih.gov/12403667/) | 2002 | Observational (clinical) study | Circulation | Found orthostatic intolerance in POTS/NCS occurs without persistent sympathetic neurocirculatory failure, informing cardiac sympathetic dysautonomia mechanisms relevant to dopaminergic signaling |
| [28522107](https://pubmed.ncbi.nlm.nih.gov/28522107/) | 2017 | Observational study | Autonomic Neuroscience: Basic & Clinical | Compared neurohumoral/hemodynamic responses to head-up tilt between high- and normal-norepinephrine POTS subtypes |
| [26608337](https://pubmed.ncbi.nlm.nih.gov/26608337/) | 2016 | Observational study | American Journal of Physiology (Heart & Circ.) | Characterized neurohumoral biomarker profiles in children with orthostatic intolerance to help predict treatment options |
| [32606041](https://pubmed.ncbi.nlm.nih.gov/32606041/) | 2020 | Retrospective case series | Journal of Investigative Medicine | Retrospective review of bupropion (a dopamine/norepinephrine reuptake inhibitor, not dopamine itself) in 47 POTS patients showing symptom improvement |
| [16601453](https://pubmed.ncbi.nlm.nih.gov/16601453/) | 2006 | Review | Current Opinion in Cardiology | Reviews familial/genetic factors in orthostatic tachycardia, including a norepinephrine transporter mutation |
| [12102462](https://pubmed.ncbi.nlm.nih.gov/12102462/) | 2002 | Review | Clinical Autonomic Research | Reviews catecholamine abnormalities including DBH deficiency, which causes elevated dopamine and orthostatic hypotension |

---

## EU Market Information

Dopamine currently has **no EU marketing authorization on record** in this evidence pack (`total_licenses: 0`, `market_status: 未上市 / Not marketed`, `licenses: []`). No product-level authorization details are available for review.

---

## Safety Considerations

Please refer to the SmPC for safety information. All safety fields in this evidence pack (key warnings, contraindications, drug interactions) are marked as data gaps, and the DDI query returned no results (`query_status: not_found`).

Notably, this evidence pack flags a **Blocking-severity data gap (DG001)**: TFDA/SmPC warning and contraindication labeling is missing, which prevents this candidate from entering initial safety screening (S1). A **High-severity gap (DG002)** also exists for formal mechanism-of-action data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication is supported only by mechanistic/observational human studies of the endogenous renal dopaminergic system in POTS, not by direct interventional evidence that dopamine administration improves POTS symptoms.
- A Blocking-severity safety data gap (missing TFDA/SmPC warnings and contraindications) prevents even an initial safety assessment, and the drug has no current EU marketing authorization.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the TFDA/SmPC label for warnings and contraindications before any safety screening can proceed
- Resolve DG002: query DrugBank API for a complete mechanism-of-action profile
- Identify or commission interventional evidence testing dopamine (or dopaminergic agents) specifically as a POTS therapy, rather than as a physiological research probe
- Complete a formal DDI screen (current status: not found)
- Clarify current regulatory/market status and any historical licensing in EU jurisdictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

