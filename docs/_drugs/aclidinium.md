---
layout: default
title: Aclidinium
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Aclidinium
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

# Aclidinium: From COPD to Open-Angle Glaucoma

## One-Sentence Summary

Aclidinium is a long-acting muscarinic antagonist (LAMA) bronchodilator used for COPD maintenance treatment (not currently registered in Taiwan).
The TxGNN model predicts potential activity in **Open-Angle Glaucoma** (score: 89.36%), but mechanistic analysis reveals a pharmacologically **opposing relationship** — M3 receptor antagonism may raise intraocular pressure rather than lower it.
Currently, there are **no clinical trials and no publications** specifically supporting this repurposing direction; all 10 predicted indications remain at evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | COPD maintenance bronchodilation (inferred from DrugBank DB08897 and referenced clinical evidence; no Taiwan registration) |
| Predicted New Indication | Open-Angle Glaucoma |
| TxGNN Prediction Score | 89.36% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory dossier. Based on known information, Aclidinium is a long-acting muscarinic antagonist (LAMA) that selectively blocks M3 muscarinic receptors in airway smooth muscle, producing sustained bronchodilation. This mechanism underpins its proven efficacy in COPD.

For glaucoma, the pharmacological direction is actually reversed. Muscarinic **agonists** — most notably pilocarpine — are established first-line glaucoma medications that activate M3 receptors in the ciliary muscle, increasing aqueous humor outflow and reducing intraocular pressure (IOP). As an M3 **antagonist**, Aclidinium would theoretically reduce ciliary muscle tone, impair trabecular outflow, and potentially *raise* IOP. Anticholinergic drugs already carry a class contraindication in narrow-angle glaucoma, and there is no established mechanistic rationale for LAMA therapy as a treatment for any glaucoma subtype.

The TxGNN model's high prediction score (89.36%) most likely reflects shared disease-node representations in the underlying knowledge graph — for example, COPD–glaucoma comorbidity links — rather than direct pharmacological evidence for glaucoma treatment. This prediction should be treated with caution, as the mechanistic basis actively conflicts with standard-of-care glaucoma pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for open-angle glaucoma.

---

## Literature Evidence

Currently no related literature available for open-angle glaucoma.

---

## Taiwan Market Information

Aclidinium is currently **not marketed in Taiwan**. No TFDA regulatory authorizations have been identified for this drug.

---

## Full Prediction Landscape (All 10 Indications)

The following table summarizes all TxGNN predictions in this multi-indication evidence pack. All indications are L5 with no supporting clinical evidence.

| Rank | Disease | TxGNN Score | Recommendation | Key Mechanistic Issue |
|------|---------|-------------|----------------|-----------------------|
| 1 | Open-Angle Glaucoma | 89.36% | Hold | M3 antagonism opposes standard IOP-lowering mechanism |
| 2 | Primary Hereditary Glaucoma | 88.95% | Hold | Same opposing mechanism; genetic pathology lacks LAMA target |
| 3 | Migraine Disorder | 86.15% | Hold | Headache is a known anticholinergic adverse effect |
| 4 | Migraine with Brainstem Aura | 85.36% | Hold | Inhaled route insufficient for CNS/brainstem penetration |
| 5 | Irritable Bowel Syndrome | 84.56% | Research Question | Class effect plausible (M3 antispasmodics exist); primary barrier is rapid systemic hydrolysis (t½ < 1 hr) limiting GI exposure |
| 6 | Headache Disorder | 83.48% | Hold | Only trial (NCT02165826) monitors headache as a COPD safety endpoint, not a therapeutic target |
| 7 | Trigeminal Autonomic Cephalalgia | 82.74% | Hold | Inhaled route cannot target pterygopalatine ganglion; CGRP-based therapies more mechanistically direct |
| 8 | Glaucoma 1, Open Angle | 79.57% | Hold | Duplicate of Rank 1 (OMIM reclassification); same concerns apply |
| 9 | Gastroduodenitis | 79.52% | Hold | Systemic concentrations after inhalation insufficient for gastric M3 effect; standard therapies (PPI, H. pylori eradication) far superior |
| 10 | Dermatitis | 79.28% | Hold | Only supporting evidence (PMID 23679347) is a COPD safety extension study — dermatitis appears as an adverse event, not a treatment target |

**Sole signal worth flagging**: IBS (Rank 5) is the only prediction with a coherent mechanistic class effect — approved antispasmodics (dicyclomine, hyoscyamine) share M3 antagonism with Aclidinium. However, the key research question is whether systemic bioavailability after inhalation can reach therapeutic concentrations in the gastrointestinal tract, given rapid plasma hydrolysis.

---

## Safety Considerations

Please refer to the SmPC for complete safety information.

> As an anticholinergic drug, Aclidinium carries a class-level concern for **narrow-angle glaucoma** (a known contraindication for anticholinergic agents). This is especially relevant given that 3 of the 10 TxGNN predictions involve glaucoma or ophthalmic indications. Full TFDA SmPC data (warnings, contraindications) was not available in this evidence pack and must be obtained before any clinical repurposing assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are at evidence level L5 with no supporting clinical trials or targeted publications. The highest-ranked prediction (open-angle glaucoma) is mechanistically counterindicated — M3 antagonism is pharmacologically opposite to the required IOP-lowering action. Multiple headache predictions are undermined by the fact that headache is a documented anticholinergic adverse effect. The only biologically plausible direction (IBS, Rank 5) faces a significant delivery barrier that has not been assessed.

**To proceed, the following is needed:**

- **Immediate (Data Gaps)**: Obtain TFDA SmPC to document warnings and contraindications (Data Gap DG001, Blocking severity); retrieve MOA details from DrugBank API (Data Gap DG002, High severity)
- **For IBS pathway only**: Conduct pharmacokinetic modeling or preclinical gut motility studies to determine whether Aclidinium achieves therapeutic concentrations at gastrointestinal M3 receptors after inhalation or alternative delivery routes
- **For glaucoma predictions**: No further investigation recommended — mechanistic direction opposes therapeutic requirement; flag class contraindication risk in safety review
- **General**: Reassess all predictions after completing MOA documentation, as the mechanistic conflict identified here applies broadly to any indication requiring intact M3 receptor activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

