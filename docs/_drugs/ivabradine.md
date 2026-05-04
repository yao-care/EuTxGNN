---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Ivabradine
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

# Ivabradine: From Heart Failure to Pulmonary Hypertension

## One-Sentence Summary

Ivabradine is a selective I_f (funny current / HCN4) channel blocker approved for chronic heart failure with reduced ejection fraction (HFrEF) and stable angina pectoris, reducing heart rate without impairing myocardial contractility.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with **3 clinical trials** and **20 publications** currently identified in support of this direction.

> **⚠️ Model Artifact Alert**: The top TxGNN predictions (Ranks 1–2, 5, 8: hypertrichosis, Ambras syndrome, isolated hair shaft abnormality, familial trichomegaly) reflect **reverse causality artifacts** — the model has mislearned ivabradine's known side effect of abnormal hair growth (hypertrichosis/trichomegaly) as a therapeutic target signal. These predictions are not clinically actionable. **Pulmonary Hypertension (Rank 7)** is the highest-ranked mechanistically plausible candidate and is the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure with reduced ejection fraction (HFrEF); stable angina pectoris |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on referenced literature, ivabradine selectively blocks the hyperpolarization-activated I_f (funny current / HCN4) channel in sinoatrial node pacemaker cells, slowing the rate of spontaneous diastolic depolarization and thereby reducing heart rate. Critically, this effect is independent of myocardial contractility, blood pressure, or autonomic nervous system activation — a pharmacological profile that distinguishes ivabradine from beta-blockers.

In pulmonary hypertension, elevated pulmonary vascular resistance chronically overloads the right ventricle (RV). Patients typically develop compensatory sinus tachycardia, which paradoxically worsens the situation: a faster heart rate shortens RV diastolic filling time, increases RV oxygen demand, and reduces coronary perfusion per cardiac cycle — accelerating RV failure. Ivabradine's ability to selectively lower heart rate can improve RV filling time, reduce myocardial oxygen consumption, and restore more efficient RV-PA coupling, without the negative inotropic risk that makes beta-blockers poorly tolerated or contraindicated in many PH patients.

Animal model studies using monocrotaline-induced and SU5416+hypoxia-induced PH in rats have directly demonstrated that ivabradine reduces RV fibrosis and hypertrophy and improves biventricular function. Multiple small clinical studies — including case series in systemic sclerosis-associated PAH and prospective studies in COPD-related pulmonary hypertension — have shown hemodynamic and functional improvement with ivabradine. While no dedicated Phase 2/3 RCT exists, the convergence of mechanistic rationale, animal data, and pilot clinical evidence makes this a scientifically credible repurposing hypothesis.

---

## Clinical Trial Evidence

The three trials retrieved are only tangentially related; no trial was specifically designed to evaluate ivabradine for pulmonary hypertension.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03650205](https://clinicaltrials.gov/study/NCT03650205) | N/A | Unknown | 160 | Ivabradine to prevent anthracycline-induced cardiotoxicity — explores I_f blockade as cardiac protection; tangentially relevant to RV protection concept, but designed for cardiooncology, not PH |
| [NCT00757055](https://clinicaltrials.gov/study/NCT00757055) | Phase 2 | Withdrawn | 0 | Ivabradine in diastolic heart failure (HFpEF) — mechanistically related via diastolic filling improvement; however, withdrawn before enrollment and yields no usable data |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Sacubitril/Valsartan in HFrEF in India — different drug entirely; retrieved due to database search overlap, not relevant |

> No dedicated ivabradine + pulmonary hypertension clinical trial has been registered. This represents a key evidence gap.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32915674](https://pubmed.ncbi.nlm.nih.gov/32915674/) | 2020 | Preclinical (rat PH model) | Am J Respir Cell Mol Biol | Ivabradine reduces RV fibrosis and improves RV function in both MCT-PH and SU5416+hypoxia PH rat models; demonstrates that HR reduction independent of beta-blockade is mechanistically sufficient |
| [29146614](https://pubmed.ncbi.nlm.nih.gov/29146614/) | 2018 | Preclinical (experimental PAH) | Am J Physiol Heart Circ Physiol | Ivabradine vs. carvedilol in PAH rats: both improve biventricular function and RV-PA interactions via HR reduction; ivabradine delivers HR-specific benefit without beta-blockade side effects |
| [37742537](https://pubmed.ncbi.nlm.nih.gov/37742537/) | 2023 | Clinical observational (COPD-PH) | Am J Cardiol | Ivabradine improves RV systolic function in COPD patients with cor pulmonale; prospective study providing direct clinical hemodynamic evidence |
| [24556029](https://pubmed.ncbi.nlm.nih.gov/24556029/) | 2014 | Pilot clinical / Case series (PAH) | J Card Fail | Ivabradine improves functional capacity in PAH patients; pilot study with small sample but direct clinical endpoint data |
| [22792738](https://pubmed.ncbi.nlm.nih.gov/22792738/) | 2012 | Clinical study (COPD-PH) | Kardiologiia | In 60 COPD Stage III–IV patients with PH: 2-week ivabradine (10 mg/day) produced statistically significant reduction in pulmonary hypertension severity |
| [23021874](https://pubmed.ncbi.nlm.nih.gov/23021874/) | 2012 | Case series (SSc-PAH) | Eur J Intern Med | Ivabradine in systemic sclerosis-related PAH — associated with functional improvement and tolerated without major adverse events |
| [22383181](https://pubmed.ncbi.nlm.nih.gov/22383181/) | 2012 | Case series (SSc-PH) | Clin Res Cardiol | Safe and well-tolerated ivabradine use in SSc-associated PH; supports the safety profile in this difficult-to-treat PH subtype |
| [23389056](https://pubmed.ncbi.nlm.nih.gov/23389056/) | 2013 | Clinical (PAH) | Clin Res Cardiol | Ivabradine in PAH may delay the need for parenteral prostanoid escalation — suggests potential disease-modifying role as adjunct therapy |
| [32248556](https://pubmed.ncbi.nlm.nih.gov/32248556/) | 2020 | Scoping Review | Pharmacotherapy | Comprehensive review of novel (off-label) ivabradine uses beyond HF and angina — PH included; contextualizes the breadth of available small-study evidence |
| [28701278](https://pubmed.ncbi.nlm.nih.gov/28701278/) | 2017 | Review | Eur J Intern Med | Safety and tolerability of ivabradine as supportive therapy in PH alongside ACEi/ARBs/beta-blockers; addresses key safety concerns for clinical use planning |

---

## Taiwan Market Information

Ivabradine is not registered in Taiwan. There are no authorized products on record.

---

## Safety Considerations

Please refer to the prescribing information (SmPC or equivalent) for complete safety data.

> **Note**: All safety fields in this Evidence Pack are unavailable. For a cardiovascular drug with known bradycardic and arrhythmogenic risk, a formal safety review against the current SmPC is a **blocking prerequisite** before advancing any clinical planning in pulmonary hypertension. Key concerns to verify include bradycardia risk thresholds, atrial fibrillation risk, and contraindications in decompensated right heart failure.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple small clinical studies and animal model experiments demonstrate a physiologically sound mechanism — selective HR reduction improving RV function and RV-PA coupling — with some direct clinical evidence in PAH and COPD-PH subgroups. Evidence currently sits at L3, and no dedicated Phase 2/3 RCT exists, meaning this hypothesis is scientifically credible but not yet clinically confirmed.

**To proceed, the following is needed:**
- Retrieve and review the full SmPC for ivabradine (BLOCKING — required before safety assessment)
- Obtain MOA and complete pharmacological profile from DrugBank (DB09083)
- Define the target PH subgroup (Group 1 PAH vs. Group 3 COPD-PH vs. Group 2 post-capillary), as mechanistic fit and risk profile differ by PH etiology
- Establish hemodynamic safety thresholds: excessive HR reduction (<50 bpm) in PH patients with fixed low cardiac output may be harmful — patient selection criteria are critical
- Design a dedicated Phase 2 proof-of-concept RCT with right heart catheterization endpoints (mPAP, PVR, RV function) as primary outcomes
- Investigate regulatory pathway given Taiwan's non-marketing status: compassionate use, IND, or regional Phase 2 trial sponsorship
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

