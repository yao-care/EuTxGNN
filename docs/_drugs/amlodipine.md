---
layout: default
title: Amlodipine
parent: AI Predictions (L5)
nav_order: 46
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Amlodipine: predicted new indication Brain stem infarction . Intracerebral hemorrhage is the best-supporte… (evidence level L4). Approved use: Essential hypertension (patients not adequately controll…"
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Amlodipine: From Essential Hypertension to Brain Stem Infarction
{: .text-alpha }

## One-Sentence Summary

Amlodipine is a calcium channel blocker originally used to treat essential hypertension, including in several fixed-dose combination products.
The TxGNN model's top-ranked prediction is **Brain Stem Infarction**, but no clinical trials or publications support it.
The best-supported prediction in the data compiled for this report is **Intracerebral Hemorrhage** (secondary prevention), backed by **4 clinical trials** and **10 publications**, including a completed Phase 3 trial of 1,671 patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Essential hypertension (patients not adequately controlled on amlodipine or valsartan monotherapy) |
| Predicted New Indication | Brain stem infarction (top-ranked prediction). Intracerebral hemorrhage is the best-supported one (see below). |
| TxGNN Prediction Score | 0.9994 (brain stem infarction); 0.9979 (intracerebral hemorrhage) |
| Evidence Level | L5 (brain stem infarction); L1 (intracerebral hemorrhage) |
| EU Market Status | Marketed (valid licences: 8 of 8) |
| Number of Authorizations | 8 (valid: 8) |
| Recommended Decision | Hold (brain stem infarction); Proceed with Guardrails (intracerebral hemorrhage) |

**Note:** The top-ranked prediction, brain stem infarction, is a model output only. The sections below therefore focus on intracerebral hemorrhage, the prediction with real clinical evidence, and briefly summarize the other predictions.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Amlodipine is known to be an L-type calcium channel blocker that lowers blood pressure by reducing systemic vascular resistance.

For brain stem infarction, the link is only plausible in general terms: blood pressure lowering and vasodilation might contribute to secondary stroke prevention. No direct evidence exists.

For intracerebral hemorrhage, the link is stronger. Blood pressure control is the main modifiable risk factor for recurrent hemorrhage. Amlodipine is one component of a triple low-dose single-pill regimen tested in the TRIDENT trial. Two caveats apply. The benefit comes from the combination pill, so amlodipine's own contribution cannot be separated. And the benefit works through blood pressure lowering, which is already within amlodipine's approved use. This supports a secondary-prevention strategy more than a novel mechanism. The trial results have not been reviewed here, so the size of the effect needs to be verified from the full publication.

**Other predictions (all Hold unless noted):**

| Predicted Indication | Evidence Level | Comment |
|------|------|------|
| Pulmonary hypertension (unclear multifactorial mechanism) | L5 | No supporting data |
| Pulmonary hypertension owing to lung disease/hypoxia | L4 | Preclinical support only; vasodilators may worsen V/Q mismatch, and one case report links amlodipine to hypoxia during one-lung ventilation |
| Malignant renovascular hypertension | L4 | Two pediatric case reports; largely restates the existing hypertension indication |
| Malignant hypertensive renal disease | L5 | No supporting data |
| Cerebral artery occlusion | L3 | Animal neuroprotection data; clinical trials are indirect, tiny, or terminated (Research Question) |
| Braddock syndrome | L5 | No supporting data or plausible rationale |
| MRI-defined brain infarct | L5 | No supporting data |
| ABri amyloidosis | L5 | No supporting data |

---

## Clinical Trial Evidence

Trials for intracerebral hemorrhage:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: double-blind, placebo-controlled trial of a low-dose triple antihypertensive single pill (including amlodipine) on top of standard care to prevent recurrent stroke after intracerebral hemorrhage |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | NA | Recruiting | 140 | Triple antihypertensive medication for blood pressure control after intracerebral hemorrhage (TRICH score) |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; too small to be informative |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; no usable data |

Trials for cerebral artery occlusion (indirect evidence):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) | Phase 4 | Terminated | 400 | Carotid endarterectomy vs optimal medical treatment in asymptomatic carotid stenosis; amlodipine is not the studied intervention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT | N Engl J Med | TRIDENT main publication: low-dose triple-pill antihypertensive after intracerebral hemorrhage |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial design paper | Int J Stroke | Rationale and design of TRIDENT; single-pill combination as secondary prevention |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with hemorrhagic stroke (safety signal) |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Calcium antagonists in hypertension and supraventricular arrhythmias |
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Preclinical | J Neurosci Res | Amlodipine plus atorvastatin protected against ischemic injury in rats (cerebral artery occlusion) |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Preclinical | Am J Hypertens | Amlodipine reduced stroke size in ApoE-deficient mice |
| [11282121](https://pubmed.ncbi.nlm.nih.gov/11282121/) | 2001 | Preclinical | Eur J Pharmacol | Amlodipine attenuated pulmonary vascular remodelling in hypoxic rats |
| [36856509](https://pubmed.ncbi.nlm.nih.gov/36856509/) | 2023 | Case report | Heart Surg Forum | Amlodipine possibly linked to hypoxia during one-lung ventilation |
| [35261597](https://pubmed.ncbi.nlm.nih.gov/35261597/) | 2022 | Case report | Saudi J Anaesth | Amlodipine overdose complicated by non-cardiogenic pulmonary edema (safety signal) |
| [10759437](https://pubmed.ncbi.nlm.nih.gov/10759437/) | 2000 | Crossover trial | Eur Respir J | Amlodipine and responses to hypoxia in mountaineers (small, healthy volunteers) |

---

## EU Market Information

The drug is marketed in this country, with all 8 of 8 licences valid.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000776 | Dafiro | Not specified | Essential hypertension not adequately controlled on amlodipine or valsartan monotherapy (valid) |
| EMEA/H/C/000774 | Copalia | Not specified | Essential hypertension not adequately controlled on amlodipine or valsartan monotherapy (valid) |
| EMEA/H/C/000716 | Exforge | Not specified | Essential hypertension not adequately controlled on amlodipine or valsartan monotherapy (valid) |
| EMEA/H/C/004037 | Amlodipine / Valsartan Mylan | Not specified | Essential hypertension in adults not adequately controlled on monotherapy (valid) |
| EMEA/H/C/001224 | Twynsta | Not specified | Essential hypertension in adults: add-on or replacement therapy with telmisartan and amlodipine (valid) |

Three further cancelled authorizations (Exforge HCT, Dafiro HCT, Copalia HCT) cover substitution therapy with the amlodipine, valsartan and hydrochlorothiazide combination.

---

## Safety Considerations

- **Disease contraindications flagged by the knowledge graph (not label text):** liver failure and liver disease, kidney disease, angioedema (including hereditary and RAAS-blocker-induced forms), hypotensive disorders, diabetes and diabetic ketoacidosis, systemic lupus erythematosus, neutropenia and agranulocytosis, pancreatitis, hypothyroidism, myopathy, and others. These come from model-derived edges and must be confirmed against the SmPC.
- **Drug interactions:** 100 interactions were found; those listed are all moderate. Examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide), aprepitant, acetylsalicylic acid, bupropion, calcium salts, SGLT2 inhibitors (canagliflozin, dapagliflozin), clarithromycin and clotrimazole.
- **Signals from the literature:** a case of probable amlodipine-induced angioedema, and an overdose case with non-cardiogenic pulmonary edema.

Please refer to the SmPC for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for brain stem infarction (top-ranked prediction); Proceed with Guardrails for intracerebral hemorrhage (secondary prevention)**

**Rationale:**
- Brain stem infarction is a model prediction only, with no trials or literature, so it cannot be advanced.
- Intracerebral hemorrhage has a completed Phase 3 trial (TRIDENT, N=1,671) and a 2026 NEJM publication. However, the intervention is a three-drug pill, the benefit works through blood pressure lowering, and all EU licenses for amlodipine-containing products are cancelled.

**To proceed, the following is needed:**
- Review of the full TRIDENT results (effect size, safety, and the contribution of each component)
- Mechanism of action data and the SmPC warnings and contraindications, which are missing here
- Regulatory status: marketed, with 8 valid licences out of 8
- A safety plan for patients with the flagged comorbidities (angioedema, hepatic or renal impairment, hypotension)
- Further evidence for any other predicted indication before reconsideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

