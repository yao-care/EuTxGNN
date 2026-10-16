---
layout: default
title: Memantine
parent: AI Predictions (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Memantine: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Treatment of patients with moderate to severe Alzheimer's disease"
monitor_inn: "Memantine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura", "rheumatoid arthritis", "nephrogenic syndrome of inappropriate antidiuresis", "atrophoderma vermiculata", "migraine with or without aura, susceptibility to", "ulerythema ophryogenesis", "brachydactyly-syndactyly syndrome"]
---

# Memantine
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

# Memantine: From Alzheimer's Disease to Pulmonary Hypertension

## One-Sentence Summary

Memantine was originally authorised in the EU for moderate to severe Alzheimer's disease. The TxGNN model predicts it may be effective for **pulmonary hypertension** (the top-ranked prediction), but **no clinical trials** and only **2 publications** were found, and neither addresses memantine in this disease directly. The best-supported alternative direction in the data compiled for this report is **migraine disorder** (rank 2): one completed Phase 3 trial and numerous publications.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of patients with moderate to severe Alzheimer's disease |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Cancelled only (no currently valid authorisations) |
| Number of Authorizations | 8 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, memantine is an NMDA receptor antagonist (a glutamatergic modulator), and its efficacy in moderate to severe Alzheimer's disease has been established through its authorisation.

For pulmonary hypertension, the link is weak. One paper (PMID 33500723) notes that the glutamate/NMDA receptor axis has been associated with pulmonary arterial hypertension, acute lung injury and diabetes, but the study itself concerns insulin sensitivity and lipid metabolism. The other paper concerns MN-08, a nitrate derivative of memantine under development for pulmonary arterial hypertension, studied in a Phase 1 safety study in healthy volunteers. That is a different compound, so it does not demonstrate that memantine itself works. The high TxGNN score is therefore a computational signal, not clinical support.

**Other predicted indications in the data (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 2 | Migraine disorder | 99.52% | L2 | Completed Phase 3 trial (n=33), reviews, meta-analyses; evidence described as limited |
| 4 | Migraine with brainstem aura | 99.41% | L3 | Evidence extrapolated from migraine without aura |
| 5 | Rheumatoid arthritis | 98.73% | L4 | Preclinical/in vitro only |
| 8 | Migraine with or without aura, susceptibility to | 98.43% | L3 | Evidence inherited from the broader migraine indication |
| 3, 6, 7, 9, 10 | Kyphoscoliotic heart disease, nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata, ulerythema ophryogenesis, brachydactyly-syndactyly syndrome | 98.1–99.4% | L5 | No evidence or mechanistic link; prediction only |

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension.

For reference, the only completed trial identified across the predicted indications relates to migraine (rank 2):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Memantine vs sodium valproate for prophylaxis of episodic migraine; directly relevant but small, limiting confidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclinical/Mechanistic | Theranostics | NMDA receptor activation regulates insulin sensitivity and lipid metabolism; mentions an NMDAR link to pulmonary arterial hypertension only as background |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/safety (different compound) | Clinical Drug Investigation | MN-08, a nitrate derivative of memantine being developed for pulmonary arterial hypertension, assessed for safety, tolerability and pharmacokinetics in healthy Chinese volunteers |

## EU Market Information

All authorisations are cancelled; none is currently valid.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002660 | Memantine Mylan | Not specified | Treatment of patients with moderate to severe Alzheimer's disease. |
| EMEA/H/C/002711 | Memantine Merz | Not specified | Treatment of patients with moderate to severe Alzheimer's disease. |
| EMEA/H/C/002671 | Memantine ratiopharm | Not specified | Treatment of patients with moderate to severe Alzheimer's disease |
| EMEA/H/C/002766 | Memantine Accord | Not specified | Treatment of patients with moderate to severe Alzheimer's disease. |
| EMEA/H/C/002680 | Nemdatine | Not specified | Treatment of patients with moderate to severe Alzheimer's disease. |

The remaining three authorisations (Axura, Ebixa, Marixino) carry the same indication and are also cancelled.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from drug-disease links in the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, impaired renal function.
- **Drug Interactions**: 100 interactions were recorded. The listed ones are mostly Minor or Moderate.
  - Moderate: anticholinergic/antispasmodic agents such as hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium and mepenzolate.
  - Minor: ranitidine, metformin, cimetidine and potassium citrate.
  - Unclassified: glimepiride, doxycycline, lansoprazole, loperamide, famotidine and acetylsalicylic acid.

Please refer to the SmPC for the full safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction rests on a very high model score alone. No trials exist, and the two retrieved papers do not show that memantine itself works in this disease; one concerns a different compound. The evidence level is L5. In addition, all EU authorisations are cancelled.

**To proceed, the following is needed:**
- Preclinical studies of memantine itself in pulmonary hypertension models, and review of the MN-08 programme to judge whether it is relevant to memantine
- Mechanism of action data for memantine, to support mechanistic-link analysis
- Warnings and contraindications from the official product information, which are required before safety screening can proceed
- If a more evidence-rich direction is preferred, a separate evaluation of **migraine prophylaxis** (L2): a larger, adequately powered randomised trial is needed, since the existing Phase 3 trial has only 33 participants and the literature describes the evidence as limited
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

