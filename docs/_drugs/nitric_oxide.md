---
layout: default
title: Nitric Oxide
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# Nitric Oxide: From No Marketed Indication to Pulmonary Arterial Hypertension Associated with Congenital Heart Disease

## One-Sentence Summary

> Nitric oxide currently holds no marketing authorization or approved indication on file in this jurisdiction, so there is no established baseline use to compare against.
> Among TxGNN's ranked predictions, **pulmonary arterial hypertension associated with congenital heart disease** is the candidate with genuine mechanistic and clinical grounding — not simply the highest model score —
> supported by **14 clinical trials** and **20 publications**, several directly testing inhaled nitric oxide in overlapping patient populations.

**Note on prediction selection**: TxGNN's raw top-ranked predictions (ranks 1–6 by score — e.g. "malformation syndrome with odontal/periodontal component," "hypertrichosis") show no mechanistic link to nitric oxide biology, and the evidence pack itself flags rank 1 as a likely **embedding-level false positive**. This report instead presents **pulmonary arterial hypertension associated with congenital heart disease** (rank 8), the only candidate in the full ranked list reaching Evidence Level L2 and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file — Nitric Oxide has no marketing authorization in this jurisdiction |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Congenital Heart Disease |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L2 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nitric oxide is not available in this evidence pack. Based on the trial and literature data that are present, nitric oxide's biological role as an endogenous vasodilator acting through the NO–cGMP signalling pathway is well documented, and endothelial NO deficiency is a recognized contributor to pulmonary vascular remodeling and elevated pulmonary vascular resistance.

In the congenital heart disease (CHD) population specifically, chronically increased pulmonary blood flow and shear stress drive endothelial dysfunction and impaired NO bioavailability, which is proposed as a direct mechanistic driver of PAH-CHD (see literature on eNOS polymorphisms, perioperative NO/H2S levels, and plasma NO levels in CHD children with increased pulmonary flow, below). Inhaled NO is already used clinically as a pulmonary vasodilator and as the standard agent for acute pulmonary vasoreactivity testing, including in neonatal and post-cardiac-surgery PAH settings — this is not a novel biological hypothesis but an extension of an existing, mechanistically anchored clinical use pattern into a chronic-disease context.

The gap is that most identified trials test acute or perioperative NO use, adjunct therapies (sildenafil, iloprost, sotatercept), or NO as a diagnostic/vasoreactivity tool — direct long-term efficacy data for inhaled or systemic NO as chronic maintenance therapy in PAH-CHD is limited.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00955487](https://clinicaltrials.gov/study/NCT00955487) | Phase 2 | Completed | 124 | Early low-dose inhaled NO evaluated to reduce bronchopulmonary dysplasia and associated pulmonary hypertension in premature newborns |
| [NCT00352430](https://clinicaltrials.gov/study/NCT00352430) | Phase 1 | Completed | 31 | Cardiopulmonary function assessment and NO-based therapies in hemolysis-associated pulmonary hypertension |
| [NCT01959828](https://clinicaltrials.gov/study/NCT01959828) | Phase 3 | Completed | 18 | Safety and effectiveness of inhaled NO (IK-3001) in Japanese patients with PH associated with cardiac surgery |
| [NCT00023296](https://clinicaltrials.gov/study/NCT00023296) | Phase 1 | Completed | 59 | Inhaled NO plus transfusion therapy for pulmonary hypertension secondary to sickle cell anemia |
| [NCT02951130](https://clinicaltrials.gov/study/NCT02951130) | Phase 2 | Completed | 66 | Milrinone evaluated in CDH-associated PPHN that is frequently resistant to conventional pulmonary vasodilators including inhaled NO |
| [NCT03314233](https://clinicaltrials.gov/study/NCT03314233) | N/A | Completed | 21 | Delayed cord clamping in CDH infants at risk for pulmonary hypoplasia/hypertension requiring NO, ECMO or vasopressor support |
| [NCT02261883](https://clinicaltrials.gov/study/NCT02261883) | Phase 2 | Terminated | 42 | IV treprostinil as add-on therapy for persistent pulmonary hypertension of the newborn |
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Iloprost safety/tolerability/hemodynamics in adult PAH-CHD (Eisenmenger physiology) |
| [NCT07356778](https://clinicaltrials.gov/study/NCT07356778) | Phase 4 | Recruiting | 36 | Sotatercept add-on vs standard PAH therapy in vasodilator-resistant unrepaired congenital shunts (ASD/VSD/PDA), including Eisenmenger syndrome |
| [NCT05201144](https://clinicaltrials.gov/study/NCT05201144) | Phase 2 | Recruiting | 40 | Phosphodiesterase-5 inhibitor for postnatal pulmonary hypertension in neonatal congenital diaphragmatic hernia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35699093](https://pubmed.ncbi.nlm.nih.gov/35699093/) | 2022 | Cohort (genetic) | Clin Exp Hypertens | eNOS gene polymorphisms (rs1799983, rs2070744, rs61722009) associated with PAH in newborns with CHD |
| [33555425](https://pubmed.ncbi.nlm.nih.gov/33555425/) | 2021 | Cohort (prognostic) | Eur J Pediatr | Perioperative endogenous H2S and NO levels linked to prognosis in children with CHD-PAH |
| [40681972](https://pubmed.ncbi.nlm.nih.gov/40681972/) | 2025 | Clinical trial | BMC Cardiovasc Disord | Novel electrochemical NO generator evaluated for postoperative PH in adult CHD-PAH patients after cardiac surgery |
| [28608969](https://pubmed.ncbi.nlm.nih.gov/28608969/) | 2017 | Cohort | Clin Exp Pharmacol Physiol | Iloprost effect on NO, endothelin-1, ADMA and other endothelial biomarkers in CHD-PAH |
| [22526220](https://pubmed.ncbi.nlm.nih.gov/22526220/) | 2012 | Cohort | Pediatr Cardiol | Elevated homocysteine and ADMA levels associated with PH in congenital heart disease |
| [18041423](https://pubmed.ncbi.nlm.nih.gov/18041423/) | 2007 | Cohort | J Med Assoc Thai | Plasma NO levels measured in children with CHD and increased pulmonary blood flow |
| [19009218](https://pubmed.ncbi.nlm.nih.gov/19009218/) | 2008 | Review | J Bras Pneumol | Inhaled NO identified as the preferred agent for pulmonary vasoreactivity testing due to selective effect and short half-life |
| [18333354](https://pubmed.ncbi.nlm.nih.gov/18333354/) | 2007 | Review | Rom J Intern Med | Management approaches for PAH associated with congenital heart disease |
| [10564299](https://pubmed.ncbi.nlm.nih.gov/10564299/) | 1999 | Review | Artif Organs | Pathophysiology of pulmonary hypertension in congenital heart disease, including endothelial NO contribution |
| [16919006](https://pubmed.ncbi.nlm.nih.gov/16919006/) | 2006 | Review | Eur J Clin Invest | Treatment options in pediatric PAH, including vasoreactivity testing and bosentan experience |

---

## EU Market Information

Nitric oxide currently has no marketing authorizations on file in this dataset (0 licenses, market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mechanistic plausibility is strong (NO deficiency/endothelial dysfunction is an established driver of PAH-CHD, and inhaled NO is already standard-of-care for acute pulmonary vasoreactivity testing and perioperative PH in this population), and this is the only candidate among the 10 ranked predictions reaching Evidence Level L2. However, most trials evaluate acute/perioperative use, adjunct agents, or diagnostic testing rather than chronic maintenance therapy with NO itself, so efficacy for sustained PAH-CHD treatment remains unproven.

**To proceed, the following is needed:**
- Mechanism of action data (DG002 — currently a data gap, blocks mechanistic relevance analysis)
- TFDA/EMA label warnings and contraindications (DG001 — Blocking; required before any S1 safety screening)
- A regulatory pathway assessment, since nitric oxide is not currently marketed in this jurisdiction (0 authorizations)
- Route/delivery feasibility data for chronic (vs. acute/diagnostic) administration in PAH-CHD
- A dedicated efficacy trial in the chronic PAH-CHD population, since current evidence is drawn largely from adjacent populations (neonatal PH, post-cardiac surgery PH, hemolysis-associated PH) rather than PAH-CHD directly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

