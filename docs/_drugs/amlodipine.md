---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Intracerebral Hemorrhage

## One-Sentence Summary

Amlodipine is an L-type calcium channel blocker established in clinical practice for hypertension and angina pectoris. Across 10 TxGNN predictions, the highest-ranked new indication is **brain stem infarction** (score 99.94%), while the best-evidenced actionable candidate is **intracerebral hemorrhage** — supported by **1 completed Phase 3 RCT** (TRIDENT trial, n = 1,671) and **8 publications**. This report focuses on intracerebral hemorrhage as the primary clinically actionable prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; angina pectoris (established clinical use — Taiwan regulatory data not available in current dataset) |
| Top TxGNN Prediction | Brain stem infarction |
| Best-Evidenced New Indication | Intracerebral hemorrhage |
| TxGNN Prediction Score (ICH) | 99.79% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed (per current dataset; TFDA verification recommended) |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Amlodipine is a dihydropyridine-class calcium channel blocker that reduces peripheral vascular resistance by blocking L-type calcium channels in vascular smooth muscle, resulting in sustained arterial vasodilation. Detailed MOA data from DrugBank was not retrieved in this analysis; however, the drug's mechanism is extensively documented in the literature: it produces long-acting, gradual blood pressure reduction with minimal negative inotropic effect, making it among the most widely prescribed antihypertensives globally. Its slow offset and high bioavailability contribute to consistent 24-hour blood pressure control.

The link between amlodipine and intracerebral hemorrhage (ICH) is mechanistically direct. Hypertension is the strongest single modifiable risk factor for ICH, responsible for approximately 70–80% of cases. Sustained elevation of blood pressure generates wall stress on small penetrating cerebral arteries (lenticulostriate, thalamoperforators) — the vessels most vulnerable to rupture. By lowering and maintaining blood pressure below critical thresholds, CCBs such as amlodipine directly reduce the hemodynamic forces that precipitate vessel rupture. This rationale underpins the TRIDENT trial (NCT02699645), which tested a fixed low-dose triple pill comprising perindopril + indapamide + **amlodipine** specifically in patients with prior ICH, representing the first Phase 3 trial to directly investigate this strategy in an ICH cohort.

Importantly, TxGNN's predictions converge on multiple cerebrovascular indications simultaneously: brain stem infarction (rank 1), cerebral artery occlusion (rank 6), MRI-defined brain infarcts (rank 8), and intracerebral hemorrhage (rank 10). All share the same underlying biological pathway — cerebrovascular protection via sustained blood pressure control — which strongly reinforces the plausibility of the model's output. The convergence across distinct but related cerebrovascular endpoints suggests the signal is robust rather than coincidental.

---

## Clinical Trial Evidence

*Primary focus: Intracerebral Hemorrhage (Rank 10)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | **TRIDENT**: Multicentre, double-blind, placebo-controlled RCT testing fixed low-dose triple pill (perindopril + indapamide + **amlodipine**) in patients with prior ICH; primary endpoint: time to first recurrent stroke |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | **CASE-J**: ARB monotherapy vs. ARB + CCB (**amlodipine** as CCB representative) in Japanese elderly high-risk hypertensives; cardiovascular outcomes including cerebral haemorrhage |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | **IPAD**: Antihypertensive therapy in type 2 diabetes with high-normal blood pressure; ICH included as secondary endpoint; antihypertensive regimen may include CCBs |
| [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) | NA | Unknown | 8,000 | **STEP**: Intensive (< 130 mmHg) vs. standard (< 150 mmHg) SBP control in elderly hypertensives (60–80 years); MRI-defined brain infarct among endpoints; amlodipine not a specific test agent |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; terminated early with only 4 participants enrolled — no usable data |

---

## Literature Evidence

*Primary focus: Intracerebral Hemorrhage (Rank 10)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | RCT Protocol | Int J Stroke | TRIDENT trial rationale and design paper: describes scientific basis for triple-pill strategy (including **amlodipine**) in ICH secondary prevention; confirms feasibility across international sites |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT | Hypertension Research | CASE-J trial design: candesartan vs. candesartan + CCB in high-risk Japanese hypertensives; ICH captured as cardiovascular outcome; demonstrates CCB + RAS blockade strategy |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Comparative Study | Neurological Sciences | Atenolol vs. standard care in hypertensive ICH (n = 138); contextualises antihypertensive choice in acute ICH and 3-month functional outcome |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovascular Drugs and Therapy | CCB mechanisms in severe hypertension: reduction of systemic vascular resistance as primary mechanism; supports first-choice use in hypertensive emergencies with cerebrovascular risk |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with right thalamic haemorrhagic stroke — **safety signal** relevant to this population |

*Supporting evidence: Cerebral Artery Occlusion (Rank 6, L4)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Animal Study | J Neurosci Research | Amlodipine + atorvastatin show additive neuroprotection via anti-apoptotic and anti-autophagic mechanisms after 90-min MCAO in Zucker metabolic syndrome rats |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Animal Study | Brain Research | Combination amlodipine + atorvastatin reduces infarct volume and neuronal damage synergistically vs. either agent alone at 24h post-MCAO |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Animal Study | Brain Research | Amlodipine + atorvastatin superior to monotherapy for ischemic stroke protection; physical/serum parameter analysis confirms metabolic benefits |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Animal Study | Brain Research | CCBs with antioxidative properties (including amlodipine) reduce neuronal damage after focal ischemia; proposes antioxidant activity as mechanism beyond calcium antagonism |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Animal Study | Am J Hypertension | Amlodipine reduces stroke size after focal brain ischemia in ApoE-deficient mice; suggests benefit even in the presence of dyslipidaemia |

---

## Taiwan Market Information

Per the current dataset, amlodipine shows **0 active Taiwan FDA (TFDA) licenses** and market status of **not marketed**. This likely reflects a data retrieval gap rather than true market absence — amlodipine is a WHO Essential Medicine and a first-line antihypertensive recommended by ESC/ESH, AHA/ACC, and Taiwan Hypertension Society guidelines alike. Verification via direct TFDA database query is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Taiwan FDA prescribing information (warnings, contraindications) was not available in this analysis. A drug-drug interaction query returned no results.

Based on established pharmacological knowledge applicable to the ICH indication:

- **Blood pressure over-correction risk**: In post-ICH patients, excessive BP lowering may compromise cerebral perfusion pressure, particularly in the acute phase. Careful titration to target is essential.
- **Peripheral oedema**: The most common adverse effect of amlodipine (up to 10–15% at therapeutic doses); clinically important in post-stroke patients with limited mobility.
- **Additive hypotension**: When used in the triple-pill combination (as in TRIDENT), additive hypotensive effects from perindopril + indapamide + amlodipine require active monitoring, especially in elderly patients.
- **Angioedema signal**: One case report (PMID 19299323) describes probable amlodipine-associated angioedema in a haemorrhagic stroke patient — relevant safety consideration for ICH management.

> Please refer to the Taiwan FDA SmPC and the TRIDENT trial protocol for complete safety information specific to the ICH population.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The completed Phase 3 TRIDENT trial directly evaluated an amlodipine-containing triple pill in 1,671 patients with prior intracerebral haemorrhage, providing Level 2 evidence that this strategy is feasible and specifically designed for the ICH secondary prevention context. The mechanistic rationale (blood pressure reduction → reduced wall stress on penetrating cerebral arteries) is unambiguous, and multiple independent TxGNN predictions converging on cerebrovascular indications further reinforce the signal.

**To proceed, the following is needed:**

- **TRIDENT primary results**: Publication of the main efficacy outcomes from NCT02699645 (completion date August 2025) — confirm or refute the superiority of triple-pill strategy
- **Taiwan FDA verification**: Direct TFDA database query to confirm amlodipine's current regulatory status and retrieve official SmPC warnings/contraindications
- **DrugBank MOA data**: Retrieve full pharmacological profile (targets, pathways, drug interactions) to complete the mechanistic analysis
- **BP target specification**: Define safe blood pressure targets for the post-ICH population to be used in any local protocol development
- **DDI re-query**: Expand drug interaction search using DrugBank API, focusing on common post-ICH co-medications (anticoagulants, antiplatelets, antiepileptics)
- **Population-specific safety review**: Assess amlodipine tolerability data specifically in Asian/Taiwanese post-ICH cohorts, including peripheral oedema and hypotension event rates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

