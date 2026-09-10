---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Ketoconazole
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

# Ketoconazole: From Fungal Infections to Acne

## One-Sentence Summary

Ketoconazole is a broad-spectrum imidazole antifungal agent (inhibits fungal 14α-demethylase/CYP51, blocking ergosterol synthesis) used to treat various fungal infections. The TxGNN model predicts it may also be effective for **Acne (disease)**, with **1 ongoing clinical trial** and **15 publications** currently associated with this direction — though most of the supporting literature addresses adjacent conditions (fungal folliculitis, hyperandrogenism) rather than acne vulgaris directly, so the evidence should be read as suggestive rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug is an established azole antifungal; no formal indication text on file) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| EU Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ketoconazole in this evidence pack. Based on known information reflected elsewhere in the pack, ketoconazole is an imidazole-class antifungal that inhibits fungal 14α-demethylase (CYP51), blocking ergosterol synthesis — its efficacy against fungal pathogens (e.g., *Candida*, dermatophytes) is well established mechanistically.

The rationale for acne is a dual hypothesis rather than a single clean mechanistic link. First, ketoconazole has documented in vitro activity against *Propionibacterium (Cutibacterium) acnes* — inhibiting its lipase activity and showing direct antimicrobial effect — which could plausibly reduce sebum-metabolite-driven inflammation in acne. Second, at high oral doses ketoconazole inhibits adrenal/gonadal steroidogenesis (antiandrogenic effect), which has a theoretical basis for androgen-driven acne (e.g., in PCOS). However, the pack's own relevance assessment cautions that much of the acne-related evidence may actually reflect *Malassezia furfur*/Pityrosporum folliculitis — a condition frequently misdiagnosed as acne vulgaris — rather than classic acne itself, and that the ongoing comparator trial (vs. adapalene) may be testing this differential rather than true acne vulgaris.

Given this ambiguity, the mechanistic plausibility is real but the specificity to acne vulgaris (as opposed to fungal folliculitis or hyperandrogenic acne subtypes) remains unconfirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | NA | Active, not recruiting | 52 | Randomized comparison of topical ketoconazole 2% cream vs. topical adapalene 2% cream in mild comedonal/papulopustular acne; aims to assess whether ketoconazole is an alternative to retinoids with fewer side effects. No results reported yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33216275](https://pubmed.ncbi.nlm.nih.gov/33216275/) | 2021 | RCT (Levoketoconazole, SONICS study) | Pituitary | Levoketoconazole improved clinical signs/patient-reported outcomes in Cushing's syndrome via cortisol suppression — supports the steroidogenesis-inhibition mechanism relevant to androgen-driven acne, but not a direct acne trial. |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology (Basel) | Overview of systemic acne treatments (antibiotics, hormonal agents); provides background context, not ketoconazole-specific. |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review (PCOS) | BMJ Clinical Evidence | PCOS review noting association with acne, hirsutism, and androgen excess; supports antiandrogenic-acne rationale indirectly. |
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | In vitro mechanistic study | Microbiology and Immunology | Ketoconazole inhibits *P. acnes* lipase activity, suggesting a potential alternative mechanism for acne treatment amid rising antibiotic resistance. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro mechanistic study | Biological & Pharmaceutical Bulletin | Azole antifungals, including ketoconazole, show in vitro activity against *P. acnes* isolated from acne vulgaris patients. |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Clinical review | Polski Tygodnik Lekarski | Discusses reduction of hirsutism, acne, and seborrhea with hormonal/antiandrogenic therapy in PCOS. |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Archives of Dermatology | Neonatal *Malassezia furfur* pustulosis — a condition often misdiagnosed as neonatal acne, illustrating the differential-diagnosis overlap. |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | The Keio Journal of Medicine | Reviews *Pityrosporum (Malassezia) ovale* skin diseases including folliculitis, relevant to the fungal-folliculitis-vs-acne distinction. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case series | Clinical and Experimental Dermatology | *Pityrosporum* folliculitis frequently misdiagnosed as acne vulgaris; 62 patients evaluated clinically and histologically. |
| [35029850](https://pubmed.ncbi.nlm.nih.gov/35029850/) | 2022 | Case report | Archives of Endocrinology and Metabolism | Cushing's syndrome case from ectopic ACTH secretion — background on steroidogenesis-related pathology relevant to antiandrogenic mechanism. |

---

## EU Market Information

Ketoconazole currently has no EU marketing authorization on record in this evidence pack (0 authorizations, market status: 未上市 / Not Marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction has a plausible dual mechanism (anti-*P. acnes* activity and antiandrogenic steroidogenesis inhibition) and one actively running comparative trial, but the evidence base (L3) is largely indirect — dominated by reviews, case reports, and studies of adjacent conditions (fungal folliculitis, PCOS-related hyperandrogenism) rather than confirmed acne vulgaris outcomes. Both key data gaps flagged in this evidence pack (TFDA/SmPC warnings — Blocking; MOA — High) must be resolved before any safety-sensitive decision.

**To proceed, the following is needed:**
- TFDA/EU SmPC warnings and contraindications (currently missing — flagged as Blocking for safety pre-screening)
- Confirmed mechanism of action data from DrugBank or equivalent source
- Results from NCT07237763 once completed, to clarify efficacy in true acne vulgaris vs. fungal folliculitis
- Clarification of target population (classic acne vulgaris vs. androgen-driven/PCOS-associated acne vs. Malassezia folliculitis) given the mixed evidence base
- Drug-drug interaction (DDI) data, currently unavailable (query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

