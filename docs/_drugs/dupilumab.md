---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

## One-Sentence Summary

Dupilumab is a human monoclonal antibody targeting the IL-4 receptor alpha subunit, with well-documented efficacy in Th2/type 2-driven allergic diseases such as moderate-to-severe atopic dermatitis and asthma (per the literature evidence collected in this pack).
The TxGNN model predicts it may be effective for **Bronchitis**, with **1 indirect clinical trial** and **6 publications** currently informing this direction — none of which directly studied bronchitis as the primary indication.
Evidence is therefore preliminary and largely proxy-based (asthma/COPD/upper-airway Th2 disease), warranting a **Hold** pending direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (moderate-to-severe) / asthma — referenced consistently across the collected literature and trial descriptions; formal EU regulatory license data is not on record in this dataset (see Safety Considerations / Data Gaps) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (per regulatory database; 0 licenses on record) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in structured form for this candidate (flagged as a High-severity data gap, DG002). Based on information available within the collected literature, Dupilumab is a fully human IgG4 monoclonal antibody that binds the shared IL-4 receptor alpha subunit, blocking downstream signaling of both interleukin-4 and interleukin-13 — the key cytokines driving type 2 helper T-cell (Th2)-mediated inflammation (PMID 36705657, 29557246). Its efficacy in Th2-driven diseases such as atopic dermatitis and asthma has been repeatedly demonstrated in randomized controlled trials referenced throughout this evidence pack.

Bronchitis, particularly chronic or eosinophilic/allergic phenotypes, can share Th2/eosinophilic inflammatory pathways with asthma and other atopic airway diseases. Since Dupilumab already has an established role in reducing exacerbations in moderate-to-severe asthma and is under investigation in related Th2 upper- and lower-airway conditions (e.g., chronic rhinosinusitis without nasal polyps, COPD), it is mechanistically plausible that IL-4/IL-13 blockade could benefit selected bronchitis phenotypes with a Th2/eosinophilic signature.

However, the repurposing rationale in this pack explicitly flags this as a **cross-indication extrapolation**: the only retrieved clinical trial studied CRSsNP (not bronchitis), and most of the retrieved literature addresses asthma or COPD broadly rather than bronchitis specifically. Only one narrow pediatric review (PMID 38488768, eosinophilic plastic bronchitis) directly references the term "bronchitis." This means the mechanistic plausibility is reasonable, but direct clinical support for the bronchitis indication itself remains thin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab in chronic rhinosinusitis without nasal polyps (CRSsNP) — a Th2 upper-airway disease model. Not a direct bronchitis trial; graded "C" relevance as indirect supporting evidence only. |

*Note: This is the only trial retrieved under the "bronchitis" search; it provides indirect mechanistic support (shared Th2 airway pathway) rather than direct efficacy data for bronchitis.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT (open-label extension) | Lancet Respir Med | TRAVERSE study: long-term safety and efficacy of dupilumab beyond 1 year in moderate-to-severe asthma. |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review/Meta-analysis | J Asthma | Pooled RCT analysis confirming efficacy and safety of dupilumab in uncontrolled asthma. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review | Tuberc Respir Dis | Comprehensive review of pharmacologic therapies, including biologics, for preventing COPD exacerbations. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Discusses smoking-induced airway diseases (chronic bronchitis, emphysema) contributing to asthma-COPD overlap symptom burden. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review | Pediatr Pulmonol | Reviews novel therapies, including biologics, for eosinophilic pediatric plastic bronchitis — the only literature directly referencing "bronchitis." |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Cohort (imaging) | Chest | MRI-based study of anti-T2 biologic treatment effects on lung ventilation in prednisone-dependent asthma. |

---

## EU Market Information

No EU marketing authorizations are on record for Dupilumab in the current regulatory dataset (0 licenses). This is flagged internally as a data gap — literature evidence in this pack (e.g., PMID 34126094, 36705657) references Dupilumab as an approved biologic for moderate-to-severe atopic dermatitis and severe asthma in other markets, so this discrepancy should be reconciled against the official EMA/SmPC record before further evaluation.

---

## Safety Considerations

Please refer to the SmPC for safety information. No structured warnings, contraindications, or drug-drug interaction data are currently available in this dataset (labeling/warning data is flagged as a **Blocking** severity data gap, DG001 — required before any S1 safety pre-screening can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial evidence retrieved for bronchitis is an indirect CRSsNP study (Grade C relevance), and the supporting literature predominantly addresses asthma and COPD rather than bronchitis itself — only one narrow pediatric review directly references the target disease. Combined with two unresolved Blocking/High-severity data gaps (missing SmPC warnings/contraindications and missing formal MOA documentation), the evidence base is insufficient to advance beyond a research question stage.

**To proceed, the following is needed:**
- TFDA/EMA-sourced SmPC warnings, contraindications, and precautions (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation via DrugBank or equivalent source (High gap, DG002)
- Direct bronchitis-specific (not proxy asthma/CRSsNP) clinical trial evidence, ideally in an eosinophilic/Th2-defined bronchitis subpopulation
- Reconciliation of the "0 EU licenses" regulatory record against literature references to approved atopic dermatitis/asthma indications
- A formal drug-drug interaction (DDI) query, currently returning "not_found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

