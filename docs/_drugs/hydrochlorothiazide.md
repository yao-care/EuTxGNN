---
layout: default
title: Hydrochlorothiazide
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Hydrochlorothiazide
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

# Hydrochlorothiazide: From Hypertension to Multiple Candidate Indications (10-Candidate Evidence Pack)

## One-Sentence Summary

Hydrochlorothiazide (HCTZ, DrugBank DB00999) is a thiazide diuretic long used clinically to manage **hypertension and oedema**, though no formal approved-indication text or marketing license is present in this dataset (drug currently **not marketed** in the covered jurisdiction). The TxGNN model surfaced **10 candidate indications**, led by **Malignant Hypertensive Renal Disease** (score 98.42%), but only **2 of the 10 candidates** — chronic and acute pulmonary heart disease (cor pulmonale) — have any supporting clinical trial or literature evidence (2 trials, ~17 relevant publications combined); the remaining 8 candidates are supported by the model score alone (L5, no trials, no literature).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (0 licenses on file); HCTZ is globally known as a thiazide diuretic for hypertension and oedema |
| Predicted New Indication (top-ranked) | Malignant Hypertensive Renal Disease *(9 additional candidates evaluated — see table below)* |
| TxGNN Prediction Score (top-ranked) | 98.42% |
| Evidence Level (top-ranked) | L5 (model prediction only) |
| Best-Evidence Candidate | Acute Pulmonary Heart Disease — L3, decision stage S2 |
| Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (top-ranked candidate); **Research Question** for the two cor pulmonale candidates |

### All Predicted Indications — Overview

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|:-----------:|:---------------:|:---------------:|-----------------|
| 1 | Malignant hypertensive renal disease | 98.42% | L5 | S0 | Hold |
| 2 | Malignant renovascular hypertension | 98.42% | L4 | S0 | Hold |
| 3 | Pulmonary hypertension owing to lung disease/hypoxia | 98.35% | L5 | S0 | Hold |
| 4 | Pulmonary hypertension, unclear multifactorial mechanism | 98.35% | L5 | S0 | Hold |
| 5 | Braddock syndrome | 97.92% | L5 | S0 | Hold |
| 6 | Chronic pulmonary heart disease | 97.80% | L3 | S1 | Research Question |
| 7 | Acute pulmonary heart disease | 93.17% | L3 | S2 | Research Question |
| 8 | Primary hereditary glaucoma | 90.87% | L5 | S0 | Hold |
| 9 | Open-angle glaucoma | 86.16% | L5 | S0 | Hold |
| 10 | Hypotrichosis simplex of the scalp | 74.54% | L5 | S0 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Hydrochlorothiazide is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on established pharmacology, HCTZ is a **thiazide-class diuretic** that inhibits the Na⁺/Cl⁻ cotransporter in the distal convoluted tubule, reducing sodium and water reabsorption; its clinical efficacy in hypertension and fluid overload/oedema is well established.

For the top-ranked candidates (malignant hypertensive renal disease, malignant renovascular hypertension, pulmonary hypertension subtypes, glaucoma, Braddock syndrome), the mechanistic link is **weak or purely theoretical** — these candidates carry high TxGNN scores but no direct experimental or clinical support. Two notable caveats from the rationale data:
- HCTZ (like other thiazides) carries a **known safety signal for acute angle-closure glaucoma**, which is the opposite of a therapeutic effect for glaucoma candidates (ranks 8–9) — this should be treated as a safety flag, not a repurposing opportunity.
- The 20 literature hits under "pulmonary hypertension owing to lung disease/hypoxia" are mostly generic hypoxia-biology papers (brain aging, cancer metabolism, immunology) matched only on the keyword "hypoxia," not genuine HCTZ-disease evidence.

The two candidates with actual clinical support — **chronic pulmonary heart disease** and **acute pulmonary heart disease** (cor pulmonale) — are mechanistically plausible in a narrower, symptomatic sense: both conditions frequently present with right heart failure and systemic congestion, and thiazide diuretics (including HCTZ) are an established **adjunct to loop diuretics** for decongestive therapy in heart failure (e.g., the CLOROTIC trial combining HCTZ with furosemide). This is a **supportive/symptomatic** rationale, not evidence that HCTZ modifies the underlying pulmonary vascular or cardiac disease process.

---

## Clinical Trial Evidence

Only the **acute pulmonary heart disease** candidate has registered clinical trials on file; no trials were found for any of the other 9 candidates.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07008365](https://clinicaltrials.gov/study/NCT07008365) | Phase 3 | Recruiting | 168 | Uses intra-abdominal pressure and POCUS to guide decongestive/diuretic therapy in acute heart failure; relevant to diuretic-class congestion management but not HCTZ-specific (Relevance grade B). |
| [NCT06273397](https://clinicaltrials.gov/study/NCT06273397) | Not applicable | Not yet recruiting | 1050 | Compares acetazolamide vs. metolazone (a thiazide-like diuretic, same class as HCTZ) added to standard therapy in acute heart failure decongestion (Relevance grade B). |

*For the remaining 8 candidates (malignant hypertensive renal disease, malignant renovascular hypertension, both pulmonary hypertension subtypes, Braddock syndrome, chronic pulmonary heart disease, both glaucoma types, hypotrichosis): currently no related clinical trials registered.*

---

## Literature Evidence

Below are the most relevant publications across the two evidence-supported candidates (chronic/acute pulmonary heart disease) and the tangential single-paper candidates. The 20 hits returned for "pulmonary hypertension owing to lung disease/hypoxia" were excluded as false-positive keyword matches (generic hypoxia biology, unrelated to HCTZ or the target disease).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38215973](https://pubmed.ncbi.nlm.nih.gov/38215973/) | 2024 | RCT (post-hoc/subgroup) | Revista Clínica Española | CLOROTIC trial: adding HCTZ to furosemide improved diuretic response in acute heart failure; this analysis examines sex-based outcome differences. |
| [11219471](https://pubmed.ncbi.nlm.nih.gov/11219471/) | 2001 | RCT | Clinical Therapeutics | 26-week randomized multicenter trial comparing telmisartan vs. atenolol, with HCTZ added as needed, in mild-to-moderate hypertension. |
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Controlled trial | Fortschritte der Medizin | Verapamil + triamterene/HCTZ combination improved hemodynamics (BP, heart rate) in chronic heart failure over 4 weeks. |
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Crossover study | Deutsche Medizinische Wochenschrift | Compared HCTZ+triamterene diuretic combination vs. digitalis in chronic heart failure (n=16); diuretic reduced pulmonary wedge pressure. |
| [36595088](https://pubmed.ncbi.nlm.nih.gov/36595088/) | 2023 | Review | European Journal of Pediatrics | Reviews diuretic classes (including thiazides) for congestive heart failure and pulmonary hypertension in pediatric patients. |
| [33224781](https://pubmed.ncbi.nlm.nih.gov/33224781/) | 2020 | Case report | Cardiovascular Diagnosis and Therapy | Mineralocorticoid receptor blockade improved pulmonary hypertension/RV function in an infant with bronchopulmonary dysplasia (diuretic-class relevance, not HCTZ-specific). |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC: Heart Failure | Reviews the pathophysiological transition from hypertension to heart failure, relevant background for cor pulmonale congestion management. |
| [17269602](https://pubmed.ncbi.nlm.nih.gov/17269602/) | 2007 | Case report | Clinical Nephrology | Heart and renal failure secondary to renovascular hypertension from giant cell arteritis; tangential relevance to malignant renovascular hypertension candidate. |
| [6292087](https://pubmed.ncbi.nlm.nih.gov/6292087/) | 1982 | Case report | Hypertension (Dallas) | Severe hypertension in a neurofibromatosis patient with renal artery stenosis; the only literature hit for "malignant renovascular hypertension," not HCTZ-specific. |

*No literature was found for: malignant hypertensive renal disease, pulmonary hypertension (unclear multifactorial mechanism), Braddock syndrome, primary hereditary glaucoma, open-angle glaucoma, or hypotrichosis simplex of the scalp.*

---

## Market Information

Currently no marketing authorization records are available for Hydrochlorothiazide in this jurisdiction's dataset — **0 licenses on file, market status: Not Marketed**. No product name, dosage form, or approved-indication text could be extracted.

---

## Safety Considerations

Please refer to the official package insert (label/SmPC) for safety information — no structured warnings, contraindications, or drug-interaction data are currently available in this dataset.

Note: retrieval of the TFDA-equivalent package insert (warnings/contraindications) is flagged as a **Blocking** data gap (DG001) — this must be resolved before any candidate here can undergo an initial safety assessment, independent of how promising the efficacy evidence is.

---

## Conclusion and Next Steps

**Decision: Hold** (for the dataset as a whole), **with chronic/acute pulmonary heart disease carried forward as Research Questions**

**Rationale:**
- 8 of the 10 TxGNN-predicted indications (including the top-ranked "malignant hypertensive renal disease") are supported by the model score alone, with zero clinical trials or literature — insufficient to justify any action beyond monitoring (L5, Hold).
- The two candidates with real supporting evidence — chronic pulmonary heart disease (L3) and acute pulmonary heart disease (L3) — reflect HCTZ's known role as an *adjunct diuretic for congestion management* in heart failure, not a disease-modifying mechanism for the pulmonary vascular disease itself; neither of the two registered trials studies HCTZ directly (one uses a POCUS-guided general diuretic protocol, the other compares acetazolamide vs. metolazone).
- A Blocking data gap (missing TFDA/label safety data) prevents any candidate from proceeding to a formal safety pre-assessment regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- Official package insert / SmPC (warnings, contraindications, DDI) — Blocking gap, DG001
- Detailed mechanism-of-action data via DrugBank API — High-priority gap, DG002
- Confirmation of HCTZ's regulatory/marketing status in the target jurisdiction (currently 0 licenses on file)
- For the cor pulmonale candidates: trial-level data confirming HCTZ (not just diuretics/thiazide-like agents in general) is the active study drug, before advancing past the current Research Question stage
- Independent clinical review of the glaucoma candidates given HCTZ's known association with acute angle-closure glaucoma as an adverse effect (safety signal, not a repurposing rationale)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

