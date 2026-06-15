---
layout: default
title: Bedaquiline
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Bedaquiline
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

# Bedaquiline: From MDR Tuberculosis to Tuberculosis, Bovine

## One-Sentence Summary

Bedaquiline is a diarylquinoline antibiotic approved for multidrug-resistant tuberculosis (MDR-TB), acting by selectively inhibiting the mycobacterial ATP synthase.
The TxGNN model predicts it may be effective for **Tuberculosis, Bovine**,
with **0 clinical trials** and **3 publications** (all preclinical or mechanistic studies) currently supporting this direction.
Given the absence of human clinical evidence, this indication is currently at the hypothesis-generation stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multidrug-resistant tuberculosis (MDR-TB) |
| Predicted New Indication | Tuberculosis, Bovine |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bedaquiline is a first-in-class diarylquinoline that kills mycobacteria by selectively inhibiting the **c subunit of mycobacterial F₀F₁-ATP synthase**, the enzyme responsible for generating ATP essential for bacterial survival. Critically, PMID 19075053 (Haagsma et al., 2009) directly demonstrated that human mitochondrial ATP synthase has greater than 20,000-fold lower sensitivity to bedaquiline compared to mycobacterial ATP synthase, confirming the mechanistic basis for selective anti-mycobacterial activity with low host toxicity.

Bovine tuberculosis is caused by *Mycobacterium bovis*, a member of the *Mycobacterium tuberculosis* complex (MTBC). *M. bovis* and *M. tuberculosis* share highly conserved ATP synthase subunit c structure — the exact molecular target of bedaquiline. This structural conservation is the principal biological rationale behind the TxGNN prediction: the mechanism is not merely analogous, it is directly applicable at the molecular level. PMID 27210281 assessed bedaquiline MIC against *M. tuberculosis* H37Rv under varying in vitro conditions, providing methodological groundwork for extending susceptibility testing to closely related *M. bovis* strains.

However, all current evidence is restricted to in vitro or mechanistic studies. There are no animal models of bovine tuberculosis with bedaquiline, no pharmacokinetic data in cattle or relevant species, and no human clinical data. The primary use case for bovine TB treatment also raises a distinct regulatory question — whether this would be pursued as a veterinary application or as part of zoonosis control — making the translational path substantially different from conventional drug repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27210281](https://pubmed.ncbi.nlm.nih.gov/27210281/) | 2016 | In Vitro | Médecine et Maladies Infectieuses | Assessed how in vitro culture conditions (media, pH, inoculum) affect bedaquiline MIC against *M. tuberculosis* H37Rv; findings relevant to standardizing susceptibility testing for MTBC including *M. bovis* |
| [19075053](https://pubmed.ncbi.nlm.nih.gov/19075053/) | 2009 | Basic Science | Antimicrobial Agents and Chemotherapy | Demonstrated >20,000-fold selectivity of bedaquiline for mycobacterial over human mitochondrial ATP synthase; bovine heart mitochondria showed very low sensitivity, supporting specificity for MTBC targets |
| [18480227](https://pubmed.ncbi.nlm.nih.gov/18480227/) | 2008 | Methodology / Animal | Journal of Clinical Microbiology | Studied drug carryover prevention using bovine serum albumin-enriched media in *M. tuberculosis* titrations; established MIC of 0.03 µg/ml on unsupplemented media, providing methodological basis for future *M. bovis* susceptibility studies |

---

## Taiwan Market Information

Bedaquiline is currently **not marketed in Taiwan**. No TFDA authorizations are registered. This reflects the drug's limited global regulatory footprint outside of accelerated/conditional approvals in the US (FDA, 2012) and EU (EMA, 2014) for MDR-TB, where it is available under managed access programmes rather than broad commercial distribution.

---

## Safety Considerations

Detailed Taiwan-specific label warnings and contraindications are not available in this Evidence Pack. Based on published regulatory information:

- **QT Prolongation**: Bedaquiline carries a black-box warning (FDA) for increased risk of QT prolongation and potential fatal arrhythmia; ECG monitoring is mandatory during treatment.
- **Hepatotoxicity**: Elevated liver enzymes have been reported; baseline and periodic liver function tests are required.
- **Drug Interactions**: Bedaquiline is metabolised primarily by CYP3A4; co-administration with strong CYP3A4 inducers (e.g., rifampicin) significantly reduces plasma exposure, and CYP3A4 inhibitors (e.g., ketoconazole) increase it.

For complete label information, please refer to the approved SmPC or FDA prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence for bedaquiline in bovine tuberculosis is mechanistic or in vitro in nature (L4); there are no clinical trials, no animal models specific to *M. bovis* infection, and no pharmacokinetic data to support a repurposing hypothesis beyond mechanistic plausibility. While the shared MTBC ATP synthase target provides a credible biological foundation, the absence of any translational data warrants a hold until foundational preclinical work is completed.

**To proceed, the following is needed:**
- **In vitro MIC studies** against *M. bovis* strains under standardised conditions (the existing *M. tuberculosis* MIC data provides a methodological template via PMID 27210281)
- **Animal model data** in a *M. bovis* infection model to confirm in vivo efficacy and PK/PD parameters
- **Regulatory pathway clarification**: determine whether this is a veterinary drug application or a human zoonosis/occupational exposure indication, as this fundamentally changes the development strategy
- **MOA data from DrugBank** (DG002 gap) to complete mechanism-of-action linkage analysis
- **Broader indication context**: consider whether **Inactive Tuberculosis** (rank 4, L2 evidence, BREACH-TB trial NCT06568484 with 2,530 participants) represents a higher-priority, more actionable repurposing candidate within the same drug portfolio
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

