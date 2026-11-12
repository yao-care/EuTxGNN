---
layout: default
title: Tobramycin
parent: Medium Evidence (L3-L4)
nav_order: 623
evidence_level: L4
indication_count: 10
last_modified_at: 2026-11-12
description: "Tobramycin: predicted new indication Exposure keratitis (evidence level L4). Approved use: Suppressive therapy of chronic pulmonary infection due to Pseudomonas…"
monitor_inn: "Tobramycin"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "epidemic keratoconjunctivitis"]
---

# Tobramycin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tobramycin: From Cystic Fibrosis Pseudomonas Lung Infection to Exposure Keratitis
{: .text-alpha }

## One-Sentence Summary

Tobramycin is an aminoglycoside antibiotic, originally used (as an inhaled product) for suppressive therapy of chronic *Pseudomonas aeruginosa* lung infection in people with cystic fibrosis.
The TxGNN model predicts it may be effective for **exposure keratitis**, but **no clinical trials** and only **8 publications** are available for this indication. These are mostly case reports, in vitro studies and susceptibility studies, and none directly tests tobramycin in exposure keratitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Suppressive therapy of chronic pulmonary infection due to *Pseudomonas aeruginosa* in patients aged 6 years and older with cystic fibrosis |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L4 |
| EU Market Status | Marketed (valid licences: 2 of 3) |
| Number of Authorizations | 3 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tobramycin is a broad-spectrum aminoglycoside antibiotic with activity against *Pseudomonas aeruginosa* and *Staphylococcus* species. Its efficacy in *Pseudomonas* lung infection in cystic fibrosis has been established, and mechanistically it may be applicable to bacterial infections of the cornea.

Exposure keratitis happens when the cornea is not adequately protected by the eyelids, for example when a patient cannot close their eyes. The dried, damaged surface is then vulnerable to secondary infection by the same bacteria that tobramycin targets. Topical tobramycin is an established treatment for bacterial keratitis and ocular surface infections, which gives a plausible rationale for the secondary infection component.

However, no trial targets exposure keratitis itself. The retrieved literature also raises a caution: an in vitro study found that aminoglycosides, tobramycin included, are toxic to corneal epithelial cells, which is a concern for an already compromised corneal surface.

## Clinical Trial Evidence

Currently no related clinical trials registered for exposure keratitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42842711](https://pubmed.ncbi.nlm.nih.gov/42842711/) | 2026 | Retrospective cohort | Cornea | Compares MRSA and MSSA *Staphylococcus aureus* keratitis: characteristics, susceptibility, treatment and outcomes |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro study | Current Eye Research | Rabbit corneal epithelial cell cultures were used to test the cytotoxicity of neomycin, gentamicin, tobramycin and amikacin; raises a toxicity concern |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In vitro study | Nippon Ganka Gakkai Zasshi | MIC and post-antibiotic effect of eyedrops against isolates from infectious keratitis in Japan |
| [42358321](https://pubmed.ncbi.nlm.nih.gov/42358321/) | 2026 | In vitro (veterinary) | Frontiers in Veterinary Science | Fluorometholone effects on antibiotic susceptibility of canine ocular bacteria |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Multi-drug-resistant *Shewanella algae* keratitis in a patient who could not close his eyes |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | *Bacillus cereus* keratitis associated with contact lens wear |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis after photorefractive keratectomy |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao | Paracentral corneal dellen as a rare sign of Graves ophthalmopathy |

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002155 | Tobi Podhaler | tobramycin | Valid |
| EMEA/H/C/005086 | Vantobra | tobramycin | Valid |
| EMEA/H/C/002633 | Vantobra | tobramycin | Withdrawn |

<!-- licenses:end -->

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links in the TxGNN knowledge graph, not label text): kidney disease, myasthenia gravis and other neuromuscular junction disorders, Parkinson disease and parkinsonian disorders, open-angle glaucoma and ocular hypertension, diabetes mellitus and diabetic ketoacidosis, hypercalcemia, nephrocalcinosis, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and several eye infections and conditions (herpes simplex keratitis, viral and fungal eye infection, conjunctivitis, ocular tuberculosis, ophthalmic herpes zoster, corneal pigmentation). Because the proposed use is ocular, the eye-related entries deserve particular attention.
- **Drug interactions**: 100 interactions were found in total. Two are classified **Major**: magnesium sulfate and mannitol. Most others are Moderate, including other aminoglycosides and nephrotoxic or ototoxic agents (neomycin, kanamycin, vancomycin, amphotericin B), proton pump inhibitors (omeprazole, pantoprazole, lansoprazole, rabeprazole, dexlansoprazole), aminosalicylates (mesalazine, sulfasalazine, balsalazide, olsalazine), acetylsalicylic acid, and inhaled insulin.

Please refer to the SmPC for the label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it comes from the TxGNN model (deep learning) alone and may reflect similarities the model learned between related diseases, not biological evidence. No trials exist for exposure keratitis, and the literature is indirect (case reports, susceptibility studies) and includes a corneal epithelial toxicity signal.

<!-- review:begin eu-lic-20261106-tobramycin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "No trials exist for exposure keratitis, and the literature is indirect (case reports, susceptibility studies) and includes a corneal epithelial toxicity signal. Both EU authorizations for tobramycin are valid (2 valid licences of 2), and they cover inhaled products for cystic fibrosis rather than ocular use." Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 3 EU marketing authorisations for this drug, 2 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-tobramycin-1 -->

**To proceed, the following is needed:**
- Controlled or at least well-designed observational studies of topical tobramycin in exposure keratitis, with attention to corneal epithelial toxicity
- Mechanism of action data (MOA) for the mechanistic-link analysis
- Warnings and contraindications from the SmPC, since this safety data is missing and blocks safety screening
- Clarification of the route of administration and available ophthalmic formulations in the EU, because the authorizations are inhalation products

<!-- review:begin eu-lic-20261106-tobramycin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the route of administration and available ophthalmic formulations in the EU, because the cancelled authorizations are inhalation products" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 3 EU marketing authorisations for this drug, 2 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-tobramycin-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both EU authorizations for tobramycin are valid (2 valid licences of 2), and they cover inhaled products for cystic fibrosis rather than ocu" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-06 | Removed: "cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

