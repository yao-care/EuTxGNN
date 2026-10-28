---
layout: default
title: Ceftolozane
parent: AI Predictions (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
monitor_inn: "Ceftolozane"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
last_modified_at: 2026-10-23
description: "Ceftolozane: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Complicated intra-abdominal infections"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ceftolozane: From Complicated Bacterial Infections to Ureaplasma Urethritis
{: .text-alpha }

## One-Sentence Summary

Ceftolozane is a cephalosporin antibiotic, authorised in the EU (as Zerbaxa) for complicated intra-abdominal infections, acute pyelonephritis, complicated urinary tract infections and hospital-acquired pneumonia.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but there are **no clinical trials and no publications** supporting this prediction, and the biological plausibility is low.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated intra-abdominal infections; acute pyelonephritis; complicated urinary tract infections; hospital-acquired pneumonia (including ventilator-associated pneumonia) in adults |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Ceftolozane is a beta-lactam cephalosporin, a class that kills bacteria by inhibiting cell wall synthesis. It is used against Gram-negative bacteria, including resistant *Pseudomonas aeruginosa*, and is authorised in the EU for several serious infections.

For the predicted indication, the mechanistic link is weak. *Ureaplasma* species have no cell wall, so beta-lactam antibiotics are expected to be intrinsically inactive against them. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a real pharmacological signal.

### Other Predictions Reviewed

The same model run produced nine further predictions. None has any supporting clinical trial, and only one has a (non-specific) publication.

| Predicted Indication | Score | Assessment |
|------|------|------|
| Gonococcal urethritis | 0.9989 | Class-level rationale exists (other cephalosporins treat gonorrhoea), but there is no activity or clinical data for ceftolozane and effective first-line options already exist. Evidence level L5. |
| Uterine inflammatory disease | 0.9988 | Only partial plausibility. Pelvic infections are polymicrobial; ceftolozane has limited anaerobic activity and none against atypical organisms. Evidence level L5. |
| Xanthogranulomatous pyelonephritis | 0.9988 | Closest to the approved uses (pyelonephritis), but this is a chronic condition usually managed surgically, and the only retrieved paper is a general review of febrile UTI. Indirect evidence only. |
| Urogenital tuberculosis | 0.9950 | Weak support; *M. tuberculosis* produces a beta-lactamase and there are no clinical data. Evidence level L5. |
| Polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological system disease | 99.1–0.9950 | No plausible mechanism; likely model artifacts. Evidence level L5. |

For xanthogranulomatous pyelonephritis, the single retrieved review does not study that disease specifically, so the evidence level is L5 under the rule requiring direct study of the predicted disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications directly address ureaplasma urethritis. The only publication retrieved across all predictions is a general review related to the xanthogranulomatous pyelonephritis prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Review | Current Opinion in Infectious Diseases | General review of febrile urinary tract infections, including pyelonephritis and urosepsis; not specific to xanthogranulomatous pyelonephritis or to ceftolozane |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003772 | Zerbaxa | Not specified | Zerbaxa is indicated for the treatment of the following infections in adults: Complicated intra abdominal infections; Acute pyelonephritis; Complicated urinary tract infections; Hospital-acquired pneumonia (HAP)... |

## Safety Considerations

- **Drug Interactions** (11 interactions recorded, all rated Moderate): aminoglycosides (kanamycin, neomycin, streptomycin, amikacin including liposomal amikacin, gentamicin), chloramphenicol, anticoagulants (warfarin, dicoumarol), ethinylestradiol and mycophenolic acid.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials or directly relevant publications. The mechanism is also biologically implausible, because *Ureaplasma* has no cell wall and is therefore expected to be unaffected by beta-lactams. The other predictions are either artifacts or only extensions of existing approved uses.

**To proceed, the following is needed:**
- In vitro susceptibility data for ceftolozane/tazobactam against *Ureaplasma* species (and other proposed target organisms)
- Detailed mechanism-of-action data
- Warnings and contraindications from the SmPC
- If any urinary tract-related indication is pursued (for example xanthogranulomatous pyelonephritis), disease-specific clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

