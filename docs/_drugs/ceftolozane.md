---
layout: default
title: Ceftolozane
parent: AI Predictions (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ceftolozane: predicted new indication Gonococcal urethritis (evidence level L5). Approved use: Complicated intra-abdominal infections"
---

# Ceftolozane
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

# Ceftolozane: From Complicated Intra-abdominal and Urinary Tract Infections to Gonococcal Urethritis

## One-Sentence Summary

Ceftolozane is a cephalosporin antibiotic, originally authorised in the EU (as Zerbaxa) for complicated intra-abdominal infections, acute pyelonephritis, complicated urinary tract infections and hospital-acquired pneumonia.
The TxGNN model predicts it may be effective for **gonococcal urethritis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated intra-abdominal infections; acute pyelonephritis; complicated urinary tract infections; hospital-acquired pneumonia (including ventilator-associated pneumonia) in adults |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ceftolozane is a cephalosporin, a class that inhibits bacterial penicillin-binding proteins and so blocks cell wall synthesis. Its efficacy in gram-negative infections of the urinary tract and abdomen is reflected in its approved indications.

Because gonococcal urethritis is a gram-negative bacterial infection of the urinary tract, a cephalosporin class effect against *Neisseria gonorrhoeae* is plausible. However, ceftolozane is not an established treatment for this condition, and no supporting data were found. The high score is a computational prediction only and needs experimental and clinical confirmation.

Other top-ranked predictions are much less credible and should be treated as likely model artefacts:
- **Ureaplasma urethritis:** Ureaplasma has no cell wall, so beta-lactams are mechanistically ineffective.
- **Uterine inflammatory disease:** Pelvic infections are polymicrobial, and ceftolozane's anaerobic coverage is weak, so partial plausibility only.
- **Xanthogranulomatous pyelonephritis:** An indirect link through the approved pyelonephritis indication. This chronic destructive condition usually also requires surgery, and one general review on febrile urinary tract infections is the only literature found.
- **Urogenital tuberculosis:** *M. tuberculosis* is intrinsically resistant to most beta-lactams.
- **Polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease:** Non-infectious conditions with no antibacterial rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gonococcal urethritis.

For the rank 4 prediction (xanthogranulomatous pyelonephritis), one general review was found, which does not address ceftolozane specifically:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Review | Current Opinion in Infectious Diseases | Overview of febrile urinary tract infections, including pyelonephritis and urosepsis |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003772 (status: cancelled) | Zerbaxa | Not specified | Treatment in adults of complicated intra-abdominal infections; acute pyelonephritis; complicated urinary tract infections; hospital-acquired pneumonia (HAP), including ventilator... |

## Safety Considerations

- **Drug Interactions:** 11 interactions of moderate level were identified:
  - Aminoglycosides: kanamycin, neomycin, streptomycin, amikacin (including liposomal), gentamicin
  - Anticoagulants: warfarin, dicoumarol
  - Others: chloramphenicol, ethinylestradiol, mycophenolic acid

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials or literature behind it (evidence level L5). The EU authorisation is cancelled, and warnings and contraindications could not be obtained. The other top predictions are mostly biologically implausible.

**To proceed, the following is needed:**
- Safety information (warnings and contraindications) from the EU product information
- Detailed mechanism of action data
- In vitro susceptibility data for *Neisseria gonorrhoeae* against ceftolozane
- Comparison against current guideline-recommended gonorrhoea therapies, and clarification of whether ceftolozane (typically combined with tazobactam) offers any advantage
- Confirmation of the current regulatory and supply status, given that the only EU authorisation is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

