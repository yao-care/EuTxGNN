---
layout: default
title: Ketoconazole
parent: Medium Evidence (L3-L4)
nav_order: 345
evidence_level: L4
indication_count: 10
---

# Ketoconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ketoconazole: From Cushing's Syndrome to Acne

## One-Sentence Summary

Ketoconazole is an azole medicine authorised in the EU for endogenous Cushing's syndrome in adults and adolescents over 12 years old.
The TxGNN model predicts it may be effective for **acne**, but the evidence is thin: **1 small clinical trial** and several publications that are mostly indirect.
Among the other predictions, vulvovaginal candidiasis is better supported (2 Phase 3 trials), but the top-ranked prediction, acne, remains an early-stage hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endogenous Cushing's syndrome in adults and adolescents above 12 years of age |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ketoconazole is an azole antifungal that inhibits steroid synthesis (including CYP17A1), which is how it works in Cushing's syndrome. This mechanism also reduces androgen production.

The link to acne is plausible but indirect. Androgens drive sebum production, and ketoconazole also acts against Malassezia yeasts that can cause acne-like folliculitis. Laboratory studies show it inhibits *Propionibacterium acnes* growth and lipase activity. The related literature is mostly about polycystic ovary syndrome (PCOS)-related hyperandrogenism and Malassezia skin disease, so it does not directly show efficacy in acne vulgaris. The route also matters: systemic ketoconazole carries serious liver and adrenal risks, so only topical use would be a realistic option for acne.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | Not applicable | Active, not recruiting | 52 | Randomised comparison of topical ketoconazole 2% cream vs adapalene 2% cream in mild comedonal and papulopustular acne over 12 weeks; no results reported yet |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology | Update on systemic acne treatment; antibiotics and other options for moderate-to-severe acne |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Review | Pol Tyg Lek | Treatment of hyperandrogenic manifestations (including acne) in PCOS |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | BMJ Clin Evid | PCOS overview; acne listed as an associated feature |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | Keio J Med | *Pityrosporum ovale* and skin diseases, including folliculitis |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Arch Dermatol | Neonatal *Malassezia furfur* pustulosis, which mimics neonatal acne |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical study | Clin Exp Dermatol | *Pityrosporum* folliculitis is often misdiagnosed as acne vulgaris; therapeutic trials in 62 patients |
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Laboratory study | Microbiol Immunol | Ketoconazole inhibits *P. acnes* lipase activity and growth |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Laboratory study | Biol Pharm Bull | In vitro activity of azole antifungals against *P. acnes* from acne patients |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003906 (cancelled) | Ketoconazole Esteve (previously Ketoconazole HRA) | Not specified | Endogenous Cushing's syndrome in adults and adolescents above the age of 12 years. |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug–disease links in the TxGNN knowledge graph, not label text): long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis and related capillary disease, peripheral vascular disease and arterial disease, and achlorhydria.
- **Drug Interactions** (100 interactions found; examples shown):
  - Major: loperamide, triamcinolone, budesonide
  - Moderate: famotidine, ranitidine, omeprazole, rabeprazole (acid-reducing drugs), hydrocortisone, dexamethasone, betamethasone, pioglitazone, aprepitant, alosetron, atropine
  - Minor: amphotericin B

Official warnings and contraindications from the product information are not available in the data compiled for this report. Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction has a high model score, but the only trial is small, unphased, still active and without results, and the literature is indirect. The evidence level is L4, and systemic ketoconazole has serious safety limits, so any use would need to be topical. The EU authorisation is also cancelled.

**To proceed, the following is needed:**
- Results from NCT07237763 and larger controlled trials of topical ketoconazole in acne
- Mechanism of action data and a clearer account of how the mechanism applies to acne
- Safety information from the product label (warnings and contraindications)
- Confirmation of a suitable topical formulation and route

**Other predictions of note:**
- **Vulvovaginal candidiasis** has stronger support: two Phase 3 trials of vaginal ketoconazole products (NCT03473418, n=69, status unknown; NCT01293643, n=99, completed), plus a recent umbrella review and a secondary analysis of a randomised trial. Its evidence level is L1, but trial results and comparison with standard treatments such as fluconazole and terconazole are still lacking. It is worth a separate evaluation as a research question.
- **Nail infection** (L3) has only a Phase 1 trial and reviews, and newer agents are preferred.
- **Leprosy, elevated plasma zinc, aquagenic urticaria, punctate epithelial keratoconjunctivitis, tinea profunda, neonatal candidiasis and congenital candidiasis** have little or no supporting evidence. Several are likely spurious model associations, and neonatal use raises major safety concerns.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

