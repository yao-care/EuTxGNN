---
layout: default
title: Avibactam
parent: AI Predictions (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Avibactam: predicted new indication Streptococcal pneumonia (evidence level L5). Approved use: Complicated intra-abdominal infection (cIAI)…"
---

# Avibactam
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

# Avibactam: From Complicated Bacterial Infections to Streptococcal Pneumonia

## One-Sentence Summary

Avibactam is a beta-lactamase inhibitor used with partner antibiotics (such as ceftazidime) to treat complicated intra-abdominal infections, complicated urinary tract infections, and hospital-acquired pneumonia.
The TxGNN model predicts it may be effective for **streptococcal pneumonia**, but **no clinical trials and no publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated intra-abdominal infection (cIAI), hospital-acquired pneumonia (HAP) including ventilator-associated pneumonia (VAP), and complicated urinary tract infection (cUTI) including pyelonephritis |
| Predicted New Indication | Streptococcal pneumonia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, avibactam is a non-beta-lactam beta-lactamase inhibitor with no antibacterial activity of its own. It protects partner beta-lactams from Ambler class A, C and some class D enzymes.

The link to the predicted indication is weak. Resistance in *Streptococcus pneumoniae* is mainly caused by altered penicillin-binding proteins, not beta-lactamases, so avibactam adds little mechanistic value. The high TxGNN score most likely reflects the drug's association with respiratory infections (HAP/VAP) and is probably a model artifact.

The other top-ranked predictions are even less plausible. Influenza susceptibility, polyclonal hyperviscosity syndrome, hyperamylasemia, squamous cell lung carcinoma and congenital analbuminemia have no apparent mechanistic link. Urinary schistosomiasis is a parasitic disease. Ureter and renal tuberculosis have only a theoretical rationale, via the mycobacterial beta-lactamase BlaC. *Staphylococcus aureus* infection (rank 7) is the only other prediction with retrieved literature, and that literature is indirect (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for streptococcal pneumonia.

For context, the closest-ranked prediction with literature is *Staphylococcus aureus* infection (rank 7). Its literature consists of reviews, surveillance studies and in vitro work on multidrug-resistant infections, which provide only indirect context:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40910659](https://pubmed.ncbi.nlm.nih.gov/40910659/) | 2025 | Review | Curr Opin Crit Care | Recommendations for managing MDR/XDR bloodstream infections and VAP in the critically ill |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Off-label use versus formal recommendations of antibiotics for MDR bacterial infections |
| [42661422](https://pubmed.ncbi.nlm.nih.gov/42661422/) | 2026 | Review | Dtsch Arztebl Int | Guideline on antibiotic treatment of severe multiresistant bacterial infections |
| [28314920](https://pubmed.ncbi.nlm.nih.gov/28314920/) | 2017 | Review | Med Klin Intensivmed Notfmed | Overview of six new antibiotics, including ceftazidime/avibactam |
| [22733066](https://pubmed.ncbi.nlm.nih.gov/22733066/) | 2012 | In vitro study | Antimicrob Agents Chemother | Ceftaroline-avibactam activity against beta-lactamase-producing Gram-negatives and MRSA (a different partner agent, in vitro only) |
| [24041891](https://pubmed.ncbi.nlm.nih.gov/24041891/) | 2013 | Animal model | Antimicrob Agents Chemother | Ceftaroline fosamil-avibactam efficacy in a murine polymicrobial infection model |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/006113 | Emblaveo | Not specified | Adults: cIAI, HAP/VAP, cUTI including pyelonephritis; infections due to aerobic Gram-negative organisms with limited treatment options... |
| EMEA/H/C/004027 | Zavicefta | Not specified | Adults and children aged 3 months and older: cIAI, cUTI, HAP/VAP, bacteraemia associated with these infections... |

Both authorizations are listed as cancelled.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). No trials or publications support streptococcal pneumonia, and the mechanism is implausible because pneumococcal resistance is not beta-lactamase-mediated. Both EU authorizations are also listed as cancelled.

**To proceed, the following is needed:**
- Confirmation of the current EU authorization status, since both licenses are listed as cancelled
- Safety data from the SmPC (warnings and contraindications), which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Direct in vitro or clinical evidence for avibactam combinations against *S. pneumoniae*
- Route and dosage form compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

