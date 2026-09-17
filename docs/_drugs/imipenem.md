---
layout: default
title: Imipenem
parent: High Evidence (L1-L2)
nav_order: 304
evidence_level: L2
indication_count: 10
---

# Imipenem
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

# Imipenem: From Bacterial Infections to Staphylococcus Aureus Infection

## One-Sentence Summary

Imipenem is a carbapenem antibiotic originally developed to treat severe, often multidrug-resistant, bacterial infections. Among 10 TxGNN-predicted indications in this evidence pack, **Staphylococcus Aureus Infection** has by far the strongest support — **13 clinical trials** (including a completed Phase 4 combination trial) and **20 publications** spanning four decades — though this represents an extension of Imipenem's existing antibacterial spectrum rather than a truly novel repurposing. The model's single highest-scoring prediction (diffuse scleroderma) is explicitly flagged in the evidence pack as a knowledge-graph artifact with no supporting evidence and is not a viable candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally available — Imipenem is not currently marketed in this jurisdiction (0 licenses on file); known pharmacologically as a carbapenem antibiotic for severe bacterial infections |
| Predicted New Indication | Staphylococcus Aureus Infection (strongest-evidence candidate among 10 predictions in this pack) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data is currently a documented gap (see DG002 below). However, the evidence pack's own rationale annotations consistently describe Imipenem as a carbapenem β-lactam antibiotic that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins (PBPs), giving it a broad spectrum of activity against many Gram-positive and Gram-negative organisms.

Because the original indication for Imipenem is bacterial infection in general, its predicted activity against Staphylococcus aureus infection is not a mechanistic leap into a new disease category — it is a direct application of its existing antibacterial mechanism. This is reflected in the evidence: in vitro susceptibility data, animal infection models (endocarditis, endophthalmitis), and a completed Phase 4 trial (NCT00871104) evaluating fosfomycin plus imipenem against MRSA endocarditis versus vancomycin. The main caveat is that Imipenem alone has limited activity against methicillin-resistant strains (MRSA), so most of the higher-quality evidence involves combination regimens (with fosfomycin or linezolid) rather than monotherapy.

By contrast, several other predictions in this pack (diffuse scleroderma, paranasal sinus neoplasm, eosinophilia-myalgia syndrome) are explicitly annotated in the rationale data as having no plausible mechanistic link to an antibacterial drug and are treated as knowledge-graph embedding artifacts rather than genuine repurposing signals.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Phase 4 | Completed | 50 | Fosfomycin plus imipenem vs. vancomycin for MRSA infective endocarditis |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Linezolid alone vs. combined with carbapenem against MRSA in ventilator-associated pneumonia |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Imipenem/cilastatin/relebactam vs. piperacillin/tazobactam for hospital-acquired/ventilator-associated bacterial pneumonia |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Phase 2 | Terminated | 108 | Tigecycline vs. imipenem/cilastatin for hospital-acquired pneumonia |
| [NCT04292054](https://clinicaltrials.gov/study/NCT04292054) | Phase 3 | Recruiting | 506 | Antibiotic prophylaxis (incl. carbapenem-class regimens) for burn excision-graft surgery |
| [NCT03218397](https://clinicaltrials.gov/study/NCT03218397) | N/A | Completed | 500 | Rapid identification/susceptibility testing (RAPIDS-GN) for Gram-negative bacteremia |
| [NCT06174649](https://clinicaltrials.gov/study/NCT06174649) | N/A | Completed | 900 | Fast antibiotic susceptibility testing trial for Gram-negative bacteremia |
| [NCT06634940](https://clinicaltrials.gov/study/NCT06634940) | N/A | Recruiting | 1000 | International surveillance of antimicrobial resistance in cirrhosis-related bacterial infections |
| [NCT06044272](https://clinicaltrials.gov/study/NCT06044272) | N/A | Completed | 10000 | Retrospective antimicrobial resistance profiling, Meta State, Colombia (2018–2022) |
| [NCT06743529](https://clinicaltrials.gov/study/NCT06743529) | N/A | Recruiting | 686 | Immediate vs. substantiated antibiotic therapy for suspected ventilator-associated pneumonia |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Clinical treatment study | Antimicrob Agents Chemother | Imipenem-cilastatin evaluated in 23 patients with methicillin-sensitive and methicillin-resistant S. aureus infections |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case commentary | Antimicrob Agents Chemother | Imipenem/cilastatin plus fosfomycin as a novel combination for refractory MRSA infection |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In vitro/in vivo study | J Antimicrob Chemother | Combined vancomycin and imipenem synergistic/additive against MRSA in most isolates tested |
| [20680368](https://pubmed.ncbi.nlm.nih.gov/20680368/) | 2010 | In vitro/in vivo study | Eur J Clin Microbiol Infect Dis | Linezolid alone and combined with vancomycin/imipenem against S. aureus with reduced glycopeptide susceptibility |
| [7928812](https://pubmed.ncbi.nlm.nih.gov/7928812/) | 1994 | Animal model | J Antimicrob Chemother | Comparative efficacy of imipenem, oxacillin, vancomycin for chronic foreign-body MSSA/MRSA infection |
| [23089756](https://pubmed.ncbi.nlm.nih.gov/23089756/) | 2013 | Animal model | Antimicrob Agents Chemother | Imipenem (with fosfomycin/rifampin) evaluated in tissue-cage MRSA foreign-body infection model |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Animal model | J Antimicrob Chemother | Imipenem therapy of experimental S. aureus and S. faecalis endocarditis, comparable to nafcillin/penicillin combinations |
| [14618340](https://pubmed.ncbi.nlm.nih.gov/14618340/) | 2003 | Animal model | Graefe's Arch Clin Exp Ophthalmol | IV imipenem vs. ceftazidime/amikacin for S. aureus endophthalmitis in rabbit model |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Review | Int J Antimicrob Agents | Review of MRSA pathogenesis, key clinical trials, and antibacterial resistance implications |
| [36526264](https://pubmed.ncbi.nlm.nih.gov/36526264/) | 2023 | Systematic review | J Glob Antimicrob Resist | AMR prevalence of E. coli and S. aureus among bacteremic patients in Africa |

## Other Predicted Indications in This Evidence Pack

This candidate record (`TW-DB01598-multi`) contains 10 TxGNN predictions. For context, here is how the remaining nine compare:

| Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|---------|------|------|------|------|
| Diffuse scleroderma (rank 1, highest score) | 99.99% | L5 | S0 | Hold — no mechanistic link; likely KG artifact |
| Paratyphoid fever | 99.99% | L3 | S2 | Research Question |
| Salmonellosis | 99.99% | L3 | S2 | Research Question |
| Sinusitis | 99.99% | L3 | S1 | Research Question |
| Chronic rhinosinusitis | 99.98% | L4 | S0 | Hold |
| Typhoid fever | 99.98% | L3 | S2 | Proceed with Guardrails — carbapenems already used as last-line therapy for XDR S. Typhi |
| Chronic ethmoidal sinusitis | 99.98% | L4 | S0 | Hold |
| Paranasal sinus neoplasm | 99.98% | L5 | S0 | Hold — antibiotics have no antineoplastic mechanism; KG artifact |
| Eosinophilia-myalgia syndrome | 99.85% | L5 | S0 | Hold — non-infectious syndrome; no plausible mechanism |

Note that predicted TxGNN scores are uniformly high (all ≥99.8%) and do not by themselves discriminate evidence quality — several of the highest-scoring predictions (diffuse scleroderma, paranasal sinus neoplasm, eosinophilia-myalgia syndrome) are explicitly the weakest on independent clinical/mechanistic review.

## Safety Considerations

Please refer to the SmPC for safety information. A drug-drug interaction query returned no results, and formal TFDA warning/contraindication text is currently a **blocking data gap** (DG001) that must be resolved before any safety-relevant (S1) evaluation can proceed.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Staphylococcus Aureus Infection specifically; other candidates in this pack are Research Question or Hold — see table above)

**Rationale:**
Staphylococcus aureus infection is supported by a completed Phase 4 combination trial, decades of clinical and animal-model literature, and a mechanistically direct antibacterial rationale — but this is best framed as label/spectrum extension rather than novel repurposing, and Imipenem alone is not reliably effective against MRSA without a partner agent.

**To proceed, the following is needed:**
- TFDA warnings, contraindications, and full prescribing information (DG001 — blocking; currently missing)
- Formal mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Confirmation of local marketing/regulatory status, since this drug currently has zero authorizations on file in this jurisdiction
- A defined combination-therapy protocol (e.g., with fosfomycin or linezolid) if pursuing the MRSA-specific use case, since monotherapy evidence is weak for resistant strains
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

