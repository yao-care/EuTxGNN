---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

> Omalizumab is a humanized anti-IgE monoclonal antibody originally used for moderate-to-severe allergic asthma and chronic spontaneous urticaria (per literature evidence in this pack; no formal marketing-authorization record is available in this jurisdiction).
> The TxGNN model predicts it may be effective for **Bronchitis**,
> with **2 clinical trials** and **8 publications** currently identified, though the trial evidence largely reflects asthma populations rather than bronchitis-specific cohorts.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic asthma / chronic spontaneous urticaria (inferred from literature evidence; not derived from a formal marketing authorization, as no license record exists in this dataset) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a High-severity data gap, DG002). Based on the literature collected for this candidate, omalizumab is a humanized monoclonal antibody that binds the constant (Cε3) region of the IgE heavy chain, lowering free serum IgE and downregulating FcεRI expression on mast cells, basophils, and dendritic cells. This reduction in IgE-driven cell activation has been shown to decrease airway eosinophilic inflammation — a mechanism well established in allergic asthma (PMID 16222080, PMID 15753888).

Allergic asthma and bronchitis both involve airway inflammation, and there is a recognized clinical overlap in the "eosinophilic bronchitis" phenotype, where steroid-sparing anti-IgE therapy could plausibly extend from asthma. However, "bronchitis" as a diagnostic label spans a much broader and mechanistically distinct group of conditions (including infectious and smoking-induced chronic bronchitis) that are not primarily IgE-mediated.

Critically, the two trials linked to this prediction (NCT02477332, NCT02049294) do not appear to be bronchitis-specific studies: NCT02477332 is a chronic spontaneous urticaria dose-finding trial, and NCT02049294, while nominally addressing "eosinophilic bronchitis," enrolled only 11 patients within an asthma steroid-sparing design. This raises a real possibility that the TxGNN association reflects asthma-bronchitis comorbidity mislabeling rather than a genuine, bronchitis-specific therapeutic signal. The mechanistic rationale is therefore plausible in a narrow eosinophilic subphenotype but not well supported for bronchitis broadly.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Phase 2b dose-finding, add-on QGE031 (ligelizumab) in chronic spontaneous urticaria — not bronchitis-specific; design targets an allergic/urticaria population. |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Steroid-sparing effect of omalizumab in patients with asthma and eosinophilic bronchitis; very small sample (n=11), primary endpoint centers on prednisone dose reduction rather than bronchitis resolution. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort/Observational | Postepy dermatologii i alergologii | Biologic therapy (omalizumab) may benefit middle-aged/older patients with severe allergic asthma–COPD overlap phenotype. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clinical reviews in allergy & immunology | Describes omalizumab's anti-IgE mechanism, reduced airway inflammation, and approval/post-approval experience in asthma. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Review/Safety | Current medical research and opinion | Pooled safety analysis of omalizumab in children with allergic (IgE-mediated) asthma. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | J Investig Allergol Clin Immunol | Rare case of plastic bronchitis following bronchial thermoplasty (procedural complication, not an omalizumab efficacy study). |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | pending | Expert Opinion on Pharmacotherapy | Discusses treatment challenges in smoking-induced airway disease (chronic bronchitis, ACO) overlapping with asthma. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | pending | Allergologia et immunopathologia | General overview of monoclonal antibody use in pediatric allergic and other disorders. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | pending | Revue des maladies respiratoires | French expert review on definitions, pathophysiology, and treatment of adult asthma exacerbations. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | pending | Masui (Jpn J Anesthesiology) | Preoperative management of bronchial asthma/chronic bronchitis; notes omalizumab's role per Japanese severe allergic asthma guidelines. |

---

## EU Market Information

Omalizumab has no marketing authorization records in the current dataset (`market_status: 未上市`, `total_licenses: 0`). No license table can be produced.

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this dataset (DG001, flagged as a **Blocking** data gap — safety data must be obtained before this candidate can enter the S1 safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on L3-level evidence, but on closer inspection the two supporting trials are predominantly asthma/urticaria studies rather than bronchitis-specific research, raising concern about disease-label mismatch. This is compounded by a Blocking safety data gap (TFDA/label warnings and contraindications, DG001) that prevents any formal safety pre-assessment, and a High-severity gap in mechanism-of-action data (DG002).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the drug label/SmPC warnings, contraindications, and interaction data before any S1 safety evaluation can proceed.
- Resolve DG002 (High): obtain a verified mechanism-of-action record (e.g., via DrugBank API) to support mechanistic-link analysis.
- Clarify whether NCT02477332 and NCT02049294 actually enrolled bronchitis (vs. asthma/urticaria) populations, to confirm the prediction isn't an artifact of comorbidity mislabeling.
- If pursued further, seek bronchitis-specific (ideally eosinophilic bronchitis) trial data with adequate sample size before advancing beyond a research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

