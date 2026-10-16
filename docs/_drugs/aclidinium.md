---
layout: default
title: Aclidinium
parent: AI Predictions (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aclidinium: predicted new indication Open-angle glaucoma (evidence level L5). Approved use: Maintenance bronchodilator treatment to relieve symptoms in adult pat…"
monitor_inn: "Aclidinium"
predicted_indications: ["open-angle glaucoma", "primary hereditary glaucoma", "migraine disorder", "migraine with brainstem aura", "irritable bowel syndrome", "headache disorder", "trigeminal autonomic cephalalgia", "glaucoma 1, open angle", "gastroduodenitis", "dermatitis"]
---

# Aclidinium
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

# Aclidinium: From COPD to Open-Angle Glaucoma

## One-Sentence Summary

Aclidinium is an inhaled long-acting muscarinic antagonist, originally used as a maintenance bronchodilator for chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts it may be effective for **open-angle glaucoma**, but **no clinical trials and no directly relevant publications** currently support this direction. The antimuscarinic mechanism also points toward a safety concern rather than a benefit in glaucoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Maintenance bronchodilator treatment to relieve symptoms in adult patients with chronic obstructive pulmonary disease (COPD) |
| Predicted New Indication | Open-angle glaucoma |
| TxGNN Prediction Score | 89.36% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, aclidinium is an inhaled long-acting muscarinic antagonist. Its efficacy in COPD has been established, but mechanistically it is **not** clearly applicable to open-angle glaucoma.

Antimuscarinic agents can cause pupil dilation (mydriasis) and may raise intraocular pressure in susceptible patients, particularly where there is an angle-closure risk. The mechanistic direction is therefore not supportive of therapeutic benefit in glaucoma. The prediction appears to be a graph-based association from the model, with no verifiable mechanistic rationale.

Other top-ranked predictions are also unsupported by evidence:
- **Primary hereditary glaucoma and glaucoma 1, open angle**: related glaucoma entries with the same concern.
- **Migraine disorder, migraine with brainstem aura, headache disorder, trigeminal autonomic cephalalgia**: speculative links. Headache is a reported adverse event in aclidinium COPD trials rather than a therapeutic effect.
- **Irritable bowel syndrome and gastroduodenitis**: antimuscarinics are used for gastrointestinal symptoms as a class, but aclidinium is inhaled with minimal systemic exposure, and there is no drug-specific evidence.
- **Dermatitis**: the only retrieved paper concerns COPD, not dermatitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly related to open-angle glaucoma is available.

For reference, the only publication retrieved across the predicted indications (listed under dermatitis) concerns the approved COPD indication and gives no evidence for the predicted use:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23679347](https://pubmed.ncbi.nlm.nih.gov/23679347/) | 2013 | RCT (extension study, COPD population) | COPD | 52-week extension of ACCORD COPD I evaluating long-term safety and tolerability of aclidinium 200 μg and 400 μg twice daily in COPD patients |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002211 (cancelled) | Eklira Genuair | Not specified (inhaled) | Maintenance bronchodilator treatment to relieve symptoms in adult patients with COPD |
| EMEA/H/C/002706 (cancelled) | Bretaris Genuair | Not specified (inhaled) | Maintenance bronchodilator treatment to relieve symptoms in adult patients with COPD |

---

## Safety Considerations

**Drug Interactions**: The interaction screen identified 100 interacting drugs, all of the 20 listed being Moderate level. The main ones are other anticholinergic or antimuscarinic agents, where additive effects are expected:
- Atropine, scopolamine, hyoscyamine
- Clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline, trospium
- Glycopyrronium (including topical)
- Antihistamines and tricyclics with anticholinergic activity: promethazine, chlorpheniramine, acrivastine, amitriptyline

Other moderate interactions include eluxadoline, prucalopride, acetylcholine, physostigmine (ophthalmic) and inhaled rapid-acting human insulin.

**Class-level concern for the predicted indication**: antimuscarinic activity may raise intraocular pressure in susceptible patients, which is directly relevant to glaucoma.

For warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or relevant literature. The antimuscarinic mechanism raises a safety concern in glaucoma rather than suggesting benefit. In addition, both EU authorizations are cancelled.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, and an explanation of why the model links aclidinium to glaucoma
- SmPC warnings and contraindications, particularly regarding narrow-angle glaucoma and intraocular pressure
- Preclinical or clinical evidence of intraocular pressure effects with inhaled aclidinium
- Assessment of route compatibility, since the drug is inhaled and glaucoma treatment is typically ocular
- Confirmation of whether any valid EU marketing authorization is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

