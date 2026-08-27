---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation to Stroke

## One-Sentence Summary

Dronedarone is a Class III antiarrhythmic agent used to maintain sinus rhythm in patients with atrial fibrillation (AF) or atrial flutter.
The TxGNN model predicts it may reduce the risk of **Stroke**, as a downstream benefit of rhythm control in AF,
with **19 clinical trials** and **20 publications** — including Phase 3/4 RCT data — currently supporting this direction.

> ⚠️ This candidate carries a **Blocking** data gap (no TFDA label/warning data available) and mixed efficacy/safety signals across trials — see Conclusion below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial Fibrillation / Atrial Flutter (established use, per clinical trial and literature context — TFDA license text unavailable) |
| Predicted New Indication | Stroke (TxGNN term: "stroke disorder") |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All TxGNN Predicted Indications for Dronedarone

Because this evidence pack bundles multiple candidate indications (`TW-DB04855-multi`), the full ranked list is shown for transparency. Only rank 1 (and, secondarily, rank 4, which is mechanistically identical) has actionable evidence; the rest are AI-only signals or likely embedding-space noise.

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Recommendation |
|------|-------------------|-------------|-----------------|-----------------|
| 1 | Stroke ("stroke disorder") | 99.97% | L1 | Proceed with Guardrails |
| 2 | Obsolete susceptibility to ischemic stroke | 99.96% | L5 | Hold (obsolete/non-clinical UMLS term) |
| 3 | ABri amyloidosis | 99.92% | L5 | Hold (no biological rationale) |
| 4 | Cerebrovascular disorder | 99.71% | L1 | Proceed with Guardrails (overlaps with Rank 1) |
| 5 | Brain stem infarction | 99.71% | L5 | Hold (no dedicated evidence) |
| 6 | Sick sinus syndrome 2, autosomal dominant | 99.63% | L5 | Hold — **safety signal, not an indication** (dronedarone is negatively chronotropic; caution/contraindication territory) |
| 7 | Duodenal obstruction | 99.56% | L5 | Hold (no plausible mechanism) |
| 8 | Cerebral artery occlusion | 99.44% | L4 | Research Question (only indirect trial support) |
| 9 | Sarcoglycanopathy | 99.43% | L5 | Hold (no biological rationale) |
| 10 | Wildervanck syndrome | 99.37% | L5 | Hold (no biological rationale) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from DrugBank is not available for this candidate (Data Gap DG002). Based on known pharmacology, Dronedarone is a **Class III, multichannel-blocking antiarrhythmic** — structurally related to amiodarone but without the iodine moiety — that restores and maintains sinus rhythm in AF/atrial flutter, with additional negative chronotropic, antiadrenergic, and mild sodium/calcium-channel blocking effects.

The proposed new indication, stroke, is not a direct pharmacological target of dronedarone but a **downstream consequence of its established AF indication**: atrial fibrillation is the leading cause of cardioembolic stroke, and by preventing AF recurrence and sustaining sinus rhythm, dronedarone reduces left atrial blood stasis and thrombus formation — the proximate cause of AF-related stroke. This is consistent with the mechanistic rationale supplied with the prediction: "restoring and maintaining sinus rhythm reduces intra-atrial thrombus formation associated with AF, thereby lowering the risk of cardioembolic stroke."

This pathway is directly supported by post-hoc analyses of the ATHENA trial and by the EAST-AFNET 4 trial (NCT01288352), both of which link early rhythm-control therapy to reduced cardiovascular/cerebrovascular events. However, the effect is **AF-subtype dependent**: the PALLAS trial (NCT01151137, Phase 3, terminated) found dronedarone *increased* the risk of stroke, MI, and death in patients with **permanent** AF and additional risk factors. This makes the mechanism plausible and evidence-backed for paroxysmal/persistent AF populations, but it defines a clear safety boundary that must guardrail any repurposing pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | PALLAS trial: dronedarone 400mg BID added to standard therapy in **permanent** AF with risk factors — stopped early due to a significant **increase** in stroke, MI, and cardiovascular death. Key negative safety signal defining the population boundary for use. |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET 4: early rhythm-control therapy (including dronedarone) vs. usual care in AF — evaluated prevention of AF-related complications including stroke. |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Completed | 1,015 | International observational cohort comparing real-world effectiveness of dronedarone vs. other antiarrhythmics, including cardiovascular/stroke-related outcomes. |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early dronedarone vs. usual care in first-detected AF, evaluating whether earlier antiarrhythmic therapy alongside stroke-prevention therapy improves outcomes. |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Amiodarone vs. dronedarone for maintenance of sinus rhythm post-cardioversion in persistent AF, a population with elevated stroke risk. |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA trial: catheter ablation vs. antiarrhythmic drug therapy (dronedarone as one arm) for AF, with cardiovascular/stroke-relevant follow-up. |
| [NCT02618577](https://clinicaltrials.gov/study/NCT02618577) | Phase 3 | Terminated | 2,608 | NOAH-AFNET 6: anticoagulation vs. current therapy for stroke/systemic embolism prevention in atrial high-rate episodes; relevant background trial for the AF–stroke pathway. |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1,746 | Early comprehensive rhythm-control therapy vs. usual care specifically in patients with acute ischemic stroke and AF — direct future test of the stroke-prevention hypothesis. |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs. antiarrhythmic drug therapy (dronedarone as a comparator) as first-line treatment for persistent AF. |
| [NCT02294955](https://clinicaltrials.gov/study/NCT02294955) | N/A | Unknown | 152 | Catheter ablation vs. optimized pharmacological therapy for symptomatic AF, informing relative-risk context for drug-based rhythm control. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT (post-hoc) | Clin Res Cardiol | Long-term safety of amiodarone and dronedarone for early rhythm control in the EAST-AFNET 4 trial population. |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (primary publication) | N Engl J Med | PALLAS trial: dronedarone in high-risk **permanent** AF — study halted due to increased major vascular events (stroke, MI, death). Defines the key safety boundary. |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Regulatory approval review of dronedarone; cites ATHENA trial post-hoc analysis suggesting reduced stroke risk in the approved (non-permanent) AF population. |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort/Pharmacovigilance | J Atr Fibrillation | Real-world comparison of cardiovascular events, stroke, heart failure, and liver injury: dronedarone vs. amiodarone and other antiarrhythmics. |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort (comparative effectiveness) | Circ Arrhythm Electrophysiol | Head-to-head comparison of dronedarone vs. sotalol in antiarrhythmic-naive veterans with AF. |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Cohort/Subgroup (post-hoc) | Eur J Heart Fail | ATHENA post-hoc analysis: dronedarone in AF/atrial flutter with concomitant HFpEF/HFmrEF. |
| [33888353](https://pubmed.ncbi.nlm.nih.gov/33888353/) | 2021 | Cohort (real-world) | Clin Ther | Evaluates digitalis intoxication risk from concomitant dronedarone + digoxin use — relevant drug-interaction signal. |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic/basic research | Atherosclerosis | Dronedarone shows anticoagulant/antiplatelet effects independent of its antiarrhythmic action, offering a possible additional mechanistic link to stroke reduction. |
| [22920480](https://pubmed.ncbi.nlm.nih.gov/22920480/) | 2012 | Review | Curr Cardiol Rev | Broader review of stroke prevention concepts and controversies in atrial fibrillation. |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | General review of AF management, including stroke risk stratification and thromboprophylaxis context. |

---

## Taiwan Market Information

Dronedarone is currently **not marketed** in Taiwan (未上市); the evidence pack records **0 TFDA product licenses**, so no approved-indication text, dosage form, or SmPC data is available locally. Any repurposing pathway would need to first establish a regulatory route (e.g., named-patient import, new drug application, or reference to EMA/FDA labeling) before a Taiwan-specific authorization table can be produced.

---

## Safety Considerations

Official TFDA warnings, contraindications, and drug-interaction data are not yet available for this candidate (Data Gap DG001, **Blocking** severity — required before this candidate can enter Stage 1 safety screening). Please refer to the SmPC (from a market where dronedarone is approved) for authoritative safety information.

**Evidence-derived safety signals** (from clinical trial/literature evidence in this pack, not official labeling):
- **AF-subtype dependent risk**: the PALLAS trial (NCT01151137) was terminated early after dronedarone significantly increased stroke, MI, and cardiovascular death in patients with **permanent** AF — the drug should not be assumed protective outside paroxysmal/persistent AF populations.
- **Sinus node caution**: dronedarone's negative chronotropic effect makes sick sinus syndrome a mechanistic contraindication/caution area (flagged independently by TxGNN as rank 6, "sick sinus syndrome 2, autosomal dominant").
- **Digoxin interaction**: real-world data (PMID 33888353) indicate increased digitalis intoxication risk with concomitant dronedarone + digoxin use, likely via P-glycoprotein inhibition.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3/4 trials (EAST-AFNET 4, PALLAS, real-world cohorts) and ATHENA post-hoc analyses directly evaluate dronedarone's effect on stroke-related outcomes in AF patients (L1 evidence), supporting a plausible and mechanistically consistent repurposing pathway. However, evidence is bidirectional — protective in paroxysmal/persistent AF, harmful in permanent AF (PALLAS) — so any use for stroke prevention must be strictly bounded to the appropriate AF subtype.

**To proceed, the following is needed:**
- TFDA-equivalent warnings, contraindications, and DDI data (Data Gap DG001, Blocking — currently prevents entry into Stage 1 safety screening)
- Confirmed mechanism-of-action documentation from DrugBank (Data Gap DG002)
- A regulatory pathway assessment, since Dronedarone currently holds zero Taiwan licenses (未上市)
- An explicit patient-selection guardrail excluding permanent AF, based on the PALLAS safety signal
- A formal evidence plan (e.g., real-world study or trial) using stroke incidence as a primary endpoint, since existing trials treat stroke as a secondary/composite outcome rather than the primary target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

