---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Meropenem
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

# Meropenem: From Serious Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic originally used for serious bacterial infections such as complicated intra-abdominal infection, complicated skin/skin-structure infection, and bacterial meningitis.
The TxGNN model predicts it may also be effective for **Bacterial Arthritis**,
with **1 clinical trial** and **20 publications** currently associated with this direction — though most of the literature is indirect (case reports and retrospective cohorts on melioidosis-related septic arthritis) rather than trials designed specifically for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated intra-abdominal infection, complicated skin/skin-structure infection, bacterial meningitis (general carbapenem-class indication; no formal license currently on file in this jurisdiction) |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Meropenem is part of the **carbapenem class** of broad-spectrum beta-lactam antibiotics. Its efficacy in serious bacterial infections — complicated intra-abdominal infection, complicated skin/skin-structure infection, and bacterial meningitis — has been well established across decades of clinical use.

Bacterial arthritis (septic arthritis) is most often caused by Gram-positive cocci (e.g., *Staphylococcus aureus*, streptococci) and Gram-negative bacilli, and in specific epidemiological settings by organisms such as *Burkholderia pseudomallei* (melioidosis). Carbapenems inhibit bacterial cell-wall synthesis via penicillin-binding proteins and possess an unusually broad spectrum covering Gram-positive, Gram-negative, and anaerobic pathogens — mechanistically this overlaps well with the pathogen profile seen in musculoskeletal infections.

The supporting literature in this evidence pack largely comes from retrospective cohorts and case series of **osteoarticular/musculoskeletal melioidosis**, where meropenem susceptibility was consistently demonstrated, plus population pharmacokinetic data supporting adequate systemic exposure. This provides reasonable mechanistic plausibility, but the evidence is indirect (it reflects *in vitro* susceptibility and observational case series rather than a trial designed to evaluate meropenem specifically for bacterial arthritis).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Evaluated levofloxacin prophylaxis against bacteremia/infection in pediatric acute leukemia and HSCT patients; not a meropenem-specific arthritis trial, but establishes the broader antibiotic-prophylaxis context for bacterial infection in immunocompromised patients. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective Cohort | Indian J Med Microbiol | Review of 22 musculoskeletal melioidosis cases; septic arthritis and osteomyelitis observed, all isolates susceptible to meropenem |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Retrospective Cohort | Le infezioni in medicina | Characterizes osteoarticular melioidosis presentations, a neglected but treatable cause of septic arthritis |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Retrospective/Cross-sectional | Clinical Laboratory | Pathogen distribution and antimicrobial resistance patterns in pediatric bone and joint infections |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case Report | Pharmaceuticals (Basel) | Uncommon septic arthritis of the hip due to *Bacillus/Paenibacillus* spp., illustrating broad-spectrum coverage needs in culture-atypical septic arthritis |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Retrospective Antibiogram Study | Eur J Orthop Surg Traumatol | Local antibiogram for empiric antibiotic selection in non-spinal orthopaedic infections including septic arthritis |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | Preclinical/In vitro | J Bone Joint Surg Am | Thermal stability and elution kinetics of meropenem (among other alternative antibiotics) in PMMA bone cement for orthopaedic infection |
| [31319190](https://pubmed.ncbi.nlm.nih.gov/31319190/) | 2019 | Preclinical (animal model) | Int J Antimicrob Agents | Colistin-cement spacer combined with systemic antibiotics for carbapenemase-producing *K. pneumoniae* prosthetic joint infection |
| [39288382](https://pubmed.ncbi.nlm.nih.gov/39288382/) | 2024 | Case Report + Systematic Review | J Infect Dev Ctries | Leptospirosis-melioidosis coinfection presenting with osteomyelitis, reviewed alongside treatment approaches |
| [38808002](https://pubmed.ncbi.nlm.nih.gov/38808002/) | 2024 | Case Report | Frontiers in Public Health | *Streptococcus suis* meningitis, a pathogen that can also present with arthritis |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | Pharmacokinetic Study | Clinical Pharmacokinetics | Population PK of meropenem across the adult lifespan, supporting dosing adequacy for systemic infections including musculoskeletal sites |

---

## EU Market Information

No marketing authorization records are currently on file for this drug in this jurisdiction (`total_licenses: 0`; market status: **Not Marketed**).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: A blocking data gap exists — TFDA/EMA label warnings, contraindications, and drug-interaction data are not currently available for this drug. This must be resolved before any safety-stage review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN prediction score is high (99.92%) and the supporting literature (L3 — retrospective cohorts/case series on musculoskeletal melioidosis with confirmed meropenem susceptibility) offers reasonable mechanistic plausibility, a **Blocking** data gap prevents this candidate from entering the S1 safety evaluation stage: no TFDA/EMA labelling data (warnings, contraindications) is currently available. The drug also has no active marketing authorization on file in this jurisdiction (0 licenses, Not Marketed), and no trial has directly evaluated meropenem for bacterial arthritis as a primary endpoint.

**To proceed, the following is needed:**
- TFDA/EMA SmPC data — warnings, contraindications, and drug-interaction profile (resolves blocking gap DG001)
- Detailed mechanism of action documentation from DrugBank (resolves DG002)
- Confirmation of marketing authorization / licensing pathway in this jurisdiction
- A clinical trial or structured retrospective analysis directly evaluating meropenem outcomes in bacterial/septic arthritis, rather than relying on indirect melioidosis-cohort susceptibility data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

