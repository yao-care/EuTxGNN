---
layout: default
title: Bedaquiline
parent: High Evidence (L1-L2)
nav_order: 85
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-15
description: "Bedaquiline: predicted new indication Inactive tuberculosis (evidence level L2). Approved use: Pulmonary tuberculosis due to M. tuberculosis resistant to at least r…"
monitor_inn: "Bedaquiline"
predicted_indications: ["tuberculosis, bovine", "tuberculoma", "tuberculous ascites", "inactive tuberculosis", "tuberculosis, avian", "vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "cutaneous tuberculosis", "esophageal candidiasis"]
---

# Bedaquiline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Bedaquiline: From Drug-Resistant Pulmonary Tuberculosis to Inactive Tuberculosis

## One-Sentence Summary

Bedaquiline is an antimycobacterial drug originally used as part of combination regimens for pulmonary tuberculosis caused by Mycobacterium tuberculosis resistant to at least rifampicin and isoniazid.
The TxGNN model predicts it may be effective for **inactive tuberculosis** (the top-ranked prediction with meaningful supporting evidence), with **3 clinical trials** and **19 publications** currently supporting this direction.
Most of the evidence is general tuberculosis literature, and the key prevention trial has no results yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis due to M. tuberculosis resistant to at least rifampicin and isoniazid (adults and children aged 2 years to under 18 years, weighing at least 7 kg), as part of a combination regimen |
| Predicted New Indication | Inactive tuberculosis (the top-ranked prediction, tuberculosis, bovine, has only one in vitro study; the most evidence-supported prediction is presented here) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bedaquiline inhibits mycobacterial ATP synthase (the c subunit of F-ATP synthase), cutting off the bacterium's energy supply. This mechanism also acts on slow-growing and dormant bacilli. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is drawn from general knowledge and the mechanistic notes attached to the predictions.

Inactive (latent) tuberculosis is caused by the same pathogen, M. tuberculosis, that bedaquiline already treats in drug-resistant disease. Because the drug's activity does not depend on rapid bacterial replication, it is plausible that it could also work in preventive treatment. This would extend its use from treatment toward prevention, particularly in people with HIV and in close contacts of people with rifampicin-resistant TB.

Important caveats: the key Phase 2/3 prevention trial is still recruiting and has no results, and most of the retrieved literature consists of general TB reviews rather than studies of bedaquiline for prevention.

**Other predictions reviewed (lower priority):**
- **Tuberculoma** (score 99.96%, L4): several case reports describe CNS tuberculoma or granuloma resolution on bedaquiline-containing regimens, but the cases are confounded by concurrent multidrug therapy, CNS penetration is uncertain, and no trials are registered. Suitable as a research question.
- **Tuberculosis, bovine** (99.96%, L4): only one in vitro MIC methodology study. Activity is plausible because M. bovis belongs to the M. tuberculosis complex, but there are no clinical data.
- **Tuberculous ascites, cutaneous tuberculosis** (L5 and L4): the retrieved papers concern drug-induced liver injury and skin reactions to anti-TB drugs, not bedaquiline efficacy.
- **Avian tuberculosis, vulvovaginal candidiasis, fascioliasis, urea cycle disorder, esophageal candidiasis**: no supporting evidence and no established mechanistic link. These appear to be model artifacts and should be held.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Phase 2/3 | Recruiting | 2530 | BREACH-TB: open-label, non-inferiority trial comparing 4 weeks of bedaquiline with a standard regimen for preventing TB disease over 72 weeks in people living with HIV and high-risk close contacts of people with drug-susceptible or rifampin-resistant TB. Directly tests the indication; no results yet. |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | Active, not recruiting | 288 | CRUSH-TB: 17-week bedaquiline, moxifloxacin and pyrazinamide regimens plus rifabutin or delamanid versus the standard six-month regimen in pulmonary TB. Informs bedaquiline regimen efficacy and safety in active disease. |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Phase 1 | Not yet recruiting | 60 | Single-dose pharmacokinetic study of anti-TB drugs including bedaquiline in plasma and breast milk of breastfeeding women. Supports exposure and safety data only, not efficacy. |

---

## Literature Evidence

No randomized controlled trials were retrieved. The table lists the most relevant publications, prioritizing bedaquiline-specific and review articles.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Review | Recent Patents on Anti-Infective Drug Discovery | Bedaquiline as a hope for shorter and better anti-TB regimens |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Review | Antibiotics (Basel) | M. tuberculosis F-ATP synthase inhibitors and targets, the mechanism underlying bedaquiline |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Review | Infectious Disorders Drug Targets | Bedaquiline-based delivery systems for MDR-TB; notes activity against persistent or latent bacilli |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Review | Respirology | Clinical update on TB as a disease spectrum, including subclinical disease |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Review | Clinical Pharmacology and Therapeutics | Overview of treatment of latent and active TB |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Review | International Journal of Molecular Sciences | TB pathogenesis, current regimens and new drug targets |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Review | Zhejiang Da Xue Xue Bao Yi Xue Ban | Progress in diagnosis and treatment of latent TB infection |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Review | The Lancet Infectious Diseases | Progress in new TB drugs, regimens and host-directed therapies |
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | Review | Pathogens | Pediatric drug-resistant TB; newer drugs such as bedaquiline and delamanid, and preventive strategies |
| [28776518](https://pubmed.ncbi.nlm.nih.gov/28776518/) | 2017 | Review | International Journal of Mycobacteriology | Drugs targeting nonreplicating M. tuberculosis bacilli |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002614 (cancelled) | Sirturo | Not specified | Part of an appropriate combination regimen in adult and paediatric patients (2 years to less than 18 years, at least 7 kg) with pulmonary tuberculosis due to M. tuberculosis resistant to at least rifampicin and isoniazid... |

---

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 entries in total; 20 were available for review. The following are classified as **Major**:
- Dexamethasone
- Clarithromycin
- Picosulfuric acid
- Polyethylene glycol (3350 with electrolytes)
- Dolasetron
- Palonosetron
- Sodium sulfate

Many others are classified as Moderate, including acarbose, famotidine, doxycycline, minocycline, tetracycline, pioglitazone, loperamide, bupropion, bisacodyl, chenodeoxycholic acid, oxandrolone, oxymetholone and naltrexone.

For warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for inactive tuberculosis only; the other predictions should be held or kept as research questions)

**Rationale:**
- A Phase 2/3 trial (BREACH-TB, n=2530) directly tests bedaquiline for TB prevention, and supporting Phase 2/3 and pharmacokinetic studies exist. However, no results are available yet, and the EU authorization shown is cancelled.

**To proceed, the following is needed:**
- Results from BREACH-TB (expected after the 72-week follow-up; completion is listed as 2027)
- The SmPC warnings and contraindications, which were not available in the data compiled for this report and are needed for safety screening
- Detailed mechanism-of-action data from DrugBank
- A safety review for prophylactic use in healthy or latently infected people, including QT-prolongation risk with the interacting drugs listed above, since the benefit-risk balance differs from treating drug-resistant disease
- Clarification of the EU regulatory status, given that the only listed authorization is cancelled
- For the tuberculoma prediction: CNS penetration data and prospective studies beyond case reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

