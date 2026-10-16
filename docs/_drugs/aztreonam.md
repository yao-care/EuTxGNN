---
layout: default
title: Aztreonam
parent: AI Predictions (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aztreonam: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Suppressive therapy of chronic pulmonary infections due to Pseudomona…"
---

# Aztreonam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Aztreonam: From Pseudomonas Lung Infection in Cystic Fibrosis to Hyperamylasemia

## One-Sentence Summary

Aztreonam is a monobactam antibiotic, originally used to treat chronic Pseudomonas aeruginosa lung infections in cystic fibrosis and serious Gram-negative infections in adults.
The TxGNN model's top-ranked prediction is **hyperamylasemia**, but there are **no clinical trials** and **no publications** supporting it, and the mechanism is implausible.
Among the other top-10 predictions, only **gonococcal urethritis** has meaningful (though dated and limited) supporting literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Suppressive therapy of chronic pulmonary infections due to Pseudomonas aeruginosa in patients with cystic fibrosis aged 6 years and older (Cayston) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| EU Market Status | ✗ Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, aztreonam is a monobactam beta-lactam that inhibits bacterial cell wall synthesis by binding to penicillin-binding protein 3 (PBP3). It is active only against aerobic Gram-negative bacteria.

For the top-ranked prediction, **hyperamylasemia**, no plausible mechanistic link exists. It is a laboratory finding rather than a bacterial infection, and has no antibacterial target. The high TxGNN score is most likely an artifact of the knowledge graph. The same applies to the next-ranked predictions: polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, and premalignant hematological system disease. None have any mechanistic rationale for an antibacterial. Ureaplasma urethritis is also biologically implausible, because Ureaplasma lacks a cell wall and is intrinsically resistant to beta-lactams.

Some lower-ranked predictions are biologically more sensible because they involve Gram-negative bacteria:
- **Gonococcal urethritis (rank 5):** *Neisseria gonorrhoeae* is susceptible to PBP-targeting beta-lactams. Aztreonam showed activity in older studies and in a 2020 single-arm trial. Resistance reports and established first-line regimens limit the case, so it might only be an alternative in beta-lactam allergy or multidrug-resistant cases.
- **Epiglottitis (rank 8):** This is within the Gram-negative spectrum, but the only evidence is indirect (a 1986 pediatric case series).
- **Xanthogranulomatous pyelonephritis (rank 10):** Antibacterial activity is plausible as an adjunct, but definitive management is surgical and there is no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (hyperamylasemia), nor for any of the other top-10 predictions.

---

## Literature Evidence

Currently no related literature is available for hyperamylasemia. The table below lists literature for other top-10 predicted indications, for reference only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm open-label trial | Antimicrob Agents Chemother | Single-dose intramuscular aztreonam 2 g tested in men with *N. gonorrhoeae* infection (gonococcal urethritis) |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical efficacy study | Antimicrob Agents Chemother | Aztreonam 1 g IM vs spectinomycin 2 g IM in uncomplicated gonorrhea: no failures with either drug |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Single-dose clinical study | Genitourin Med | Single 1 g IM dose cleared infection in 61 men and 26 women at all sites except one pharynx; well tolerated |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologic/therapeutic study | Hinyokika Kiyo | Single-dose aztreonam study in gonorrheal infections, with epidemiologic data |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro/clinical activity study | J Infect Dis | Activity of aztreonam against penicillin-resistant gonococci |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance/microbiology report | J Infect Chemother | Emergence of cephem- and aztreonam-high-resistant, non-beta-lactamase-producing *N. gonorrhoeae* |
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Case series | Am J Dis Child | Open trial in 59 children with serious Gram-negative infections, including one epiglottitis case (indirect evidence for epiglottitis) |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Clinical study | Jpn J Antibiot | Infections in hematologic disorders; 51.1% efficacy rate (indirect, not about gammopathy itself) |
| [34956120](https://pubmed.ncbi.nlm.nih.gov/34956120/) | 2021 | Microbiology/genomic report | Front Microbiol | blaNDM-1 and mcr-9 co-occurrence in a Klebsiella isolate; not relevant to blood group incompatibility (likely a keyword-matching artifact) |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| EMEA/H/C/000996 | Cayston | Not specified | Suppressive therapy of chronic pulmonary infections due to Pseudomonas aeruginosa in patients with cystic fibrosis (CF) aged 6 years and older. Consideration should be given to... | Cancelled |
| EMEA/H/C/006113 | Emblaveo | Not specified | Complicated intra-abdominal infection (cIAI), hospital-acquired pneumonia (HAP) including VAP, complicated urinary tract infection (cUTI) including pyelonephritis, and infections due to aerobic Gram-negative organisms in adult patients with limited... | Cancelled |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, bronchial disease.
- **Drug Interactions:** 27 interactions were identified in total. Those classified as **Moderate** are:
  - Picosulfuric acid
  - Dicoumarol
  - Warfarin

  The remaining interactions have an unclassified severity level. Examples include vancomycin, amikacin, amphotericin B, tacrolimus, heparin, acetylsalicylic acid, and the proton pump inhibitors (omeprazole, pantoprazole, lansoprazole).

For label-based warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (hyperamylasemia) has no clinical or literature support and no plausible antibacterial mechanism. Its high TxGNN score appears to be a graph-prediction artifact.
- Both EU authorizations are cancelled, so there is no currently marketed product.
- Gonococcal urethritis (L3) is the only prediction worth a follow-up research question. Its evidence is limited to small, mostly 1980s studies and one 2020 single-arm trial.

**To proceed, the following is needed:**
- Mechanism of action data
- Label-based warnings and contraindications from the SmPC
- For gonococcal urethritis: confirmatory controlled trials against current first-line regimens, and an assessment of resistance data
- Route and formulation compatibility assessment for any pursued indication
- Clarification of why EU authorizations were cancelled and whether any alternative supply exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

