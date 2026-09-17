---
layout: default
title: Micafungin
parent: Medium Evidence (L3-L4)
nav_order: 391
evidence_level: L3
indication_count: 10
---

# Micafungin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Micafungin: From Invasive Fungal Infections to Candida Urinary Tract Infection (Candiduria)

## One-Sentence Summary

Micafungin is an echinocandin antifungal, originally developed for invasive fungal infections such as invasive/esophageal candidiasis. The TxGNN model predicts potential efficacy against **urinary tract infection** — specifically fungal UTI (candiduria) caused by *Candida* species — with **0 clinical trials** but **13 supporting publications** (case series, cohort studies, and case reports) currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the regulatory dataset (drug is unlicensed in this jurisdiction). Based on known drug-class information, micafungin (echinocandin) is used for invasive fungal infections including invasive candidiasis and esophageal candidiasis. |
| Predicted New Indication | Urinary Tract Infection — specifically *Candida* spp. candiduria |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the structured dataset. Based on known information, micafungin belongs to the echinocandin class of antifungals, which inhibits fungal 1,3-β-D-glucan synthase and disrupts fungal cell wall synthesis. Its efficacy in invasive candidiasis has been well established in prior clinical use, and mechanistically this same glucan-synthase inhibition is directly applicable to *Candida*-caused urinary tract infections (candiduria).

Importantly, the supporting literature makes clear that the TxGNN-predicted "urinary tract infection" is **not** a general bacterial UTI indication. Every publication retrieved describes fungal UTIs caused by *Candida* species (including *C. glabrata*, *C. krusei*, and the multidrug-resistant *C. auris*), often in patients with fluconazole-resistant organisms, indwelling catheters, transplant history, or neonatal/pediatric ICU exposure. This is mechanistically coherent: echinocandins target fungal cell walls, not bacterial pathogens, so their plausible therapeutic niche is specifically candiduria rather than bacterial UTI.

Notably, this candidate set also contained several lower-ranked TxGNN predictions (e.g., *Ureaplasma* urethritis, gonococcal urethritis, and four mesothelioma variants) that lack any mechanistic plausibility — echinocandins have no activity against cell-wall-free bacteria, peptidoglycan-based bacteria, or malignant tumor biology. These were appropriately screened to **Hold** (L5, no supporting evidence) and are excluded from further development consideration, reinforcing that the candiduria signal is a genuine, biologically grounded finding rather than embedding-space noise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Cohort/PK | Int J Antimicrob Agents | Urinary micafungin concentrations, despite low renal excretion, were sufficient to successfully treat *Candida* UTIs, including fluconazole-resistant species. |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Cohort | Int Urol Nephrol | Evaluated candiduria eradication rates among hospitalized patients treated with micafungin, an off-label use given low historical urinary penetration data. |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Multi-institutional cohort | Antimicrob Agents Chemother | Retrospective cohort of 305 hospitalized patients characterizing candiduria management patterns and antifungal overuse in asymptomatic cases. |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Case series (pediatric) | Pediatr Int | Reported treatment outcomes of micafungin in critically ill pediatric ICU patients with hospital-acquired *Candida* UTIs, with success rates by species. |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case series | Med Mycol Case Rep | Five cases of candiduria treated with parenteral micafungin for ≥6 days, all achieving resolution within 30 days despite echinocandins' low urinary concentration. |
| [39781278](https://pubmed.ncbi.nlm.nih.gov/39781278/) | 2025 | Susceptibility survey | Ther Adv Infect Dis | Surveyed *Candida* species distribution and antifungal susceptibility (including micafungin) in vulvovaginal candidiasis and UTI cases in Vietnam. |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case report | Transplant Infect Dis | Increased-dose micafungin successfully eradicated chronic symptomatic *C. krusei* UTI in a liver/kidney transplant recipient with limited antifungal options. |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case report | Front Pediatr | Micafungin successfully treated *C. glabrata* urinary infection in a premature neonate with an indwelling urinary catheter. |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case report | Cureus | Described management of multidrug-resistant *C. auris* UTI in a comorbid nursing home patient. |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case report | Med Mycol Case Rep | Unilateral renal fungus ball caused by micafungin-susceptible *C. glabrata*, successfully managed with antifungal therapy plus endoscopic extraction. |

---

## EU Market Information

Micafungin currently holds **no marketing authorizations** in this jurisdiction (market status: not marketed; total licenses: 0). No product/authorization records are available for review.

---

## Safety Considerations

Please refer to the SmPC for safety information. Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a **Blocking** data gap — TFDA label warnings/contraindications must be obtained before proceeding to safety assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple cohort studies, case series, and case reports (13 publications, L3 evidence) consistently and mechanistically support micafungin's use specifically for *Candida*-caused urinary tract infections (candiduria), particularly in fluconazole-resistant or multidrug-resistant cases. However, no controlled clinical trials exist, the drug is unlicensed in this jurisdiction, and critical safety label data (warnings/contraindications) are missing — this is a **Blocking** gap that must be resolved before any safety-related decision.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap DG001) — required before S1 safety pre-assessment can begin
- Formal mechanism-of-action documentation from DrugBank (High-priority gap DG002)
- A prospective study or registry specifically targeting *Candida*-confirmed UTI (candiduria), not general/bacterial UTI populations
- Explicit diagnostic scoping in any future indication label to exclude bacterial UTI, given the mechanism is fungal-cell-wall-specific
- Regulatory pathway review, since micafungin currently holds zero authorizations in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

