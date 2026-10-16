---
layout: default
title: Meropenem
parent: AI Predictions (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Meropenem: predicted new indication Bacterial arthritis (evidence level L5). Approved use: Complicated urinary tract infection (cUTI) including pyelonephritis…"
monitor_inn: "Meropenem"
predicted_indications: ["bacterial arthritis", "epiglottitis", "staphylococcus aureus infection", "laryngitis", "paratyphoid fever", "urinary tract infection (disease)", "Lyme disease", "Peptostreptococcus infectious disease", "Ureaplasma urethritis", "gonococcal urethritis"]
---

# Meropenem
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

# Meropenem: From Complicated Bacterial Infections (Vaborem Label) to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic. In the EU it was authorised as part of Vaborem (meropenem-vaborbactam) for complicated urinary tract infection, complicated intra-abdominal infection, hospital-acquired pneumonia and related bacteraemia.
The TxGNN model's top-ranked prediction is **bacterial arthritis**, but this is supported by **0 clinical trials** and only indirect literature (case reports, reviews and susceptibility or pharmacokinetic studies).
The prediction with the strongest evidence is **urinary tract infection** (rank 6), which is already an approved indication of the original label, so it is not true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated urinary tract infection (cUTI) including pyelonephritis, complicated intra-abdominal infection (cIAI), hospital-acquired pneumonia including ventilator-associated pneumonia (HAP/VAP), bacteraemia associated with these infections, and infections due to aerobic Gram-negative organisms in adults with limited treatment options |
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (indirect literature and mechanism only; no trials for this indication) |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known pharmacology, meropenem is a carbapenem that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against many Gram-negative and Gram-positive bacteria, and its efficacy in serious Gram-negative infections is established.

Bone and joint infections are often caused by organisms that meropenem covers, including Enterobacterales, Pseudomonas and *Burkholderia pseudomallei* (melioidosis). Published cases are consistent with this. One report describes ESBL-producing *Klebsiella pneumoniae* septic arthritis treated successfully with meropenem plus amikacin and joint washout, and a melioidosis series found all isolates susceptible to meropenem.

The evidence is still indirect. It consists of retrospective series, case reports, resistance surveys and pharmacokinetic papers. No trial has tested meropenem in bacterial arthritis, so the prediction is mechanistically plausible but clinically unproven.

Other predictions in the list vary in plausibility:
- **Complicated UTI** (rank 6): strongest evidence, and already an approved indication of the original label.
- **Paratyphoid fever** (rank 5): a possible research question for extensively drug-resistant enteric fever.
- **Ureaplasma urethritis** (rank 9): *Ureaplasma* lacks a cell wall, so beta-lactam efficacy is not expected. The high score is likely a graph artifact.
- **Laryngitis** (rank 4): mostly viral, with no rationale for a carbapenem. The high score is likely a graph artifact.
- **Epiglottitis, Lyme disease, *Staphylococcus aureus* infection, Peptostreptococcus infection and gonococcal urethritis** (ranks 2, 3, 7, 8 and 10): all have established first-line alternatives, little or no direct evidence, and stewardship concerns about using a broad-spectrum carbapenem.

## Clinical Trial Evidence

No clinical trials are registered for bacterial arthritis (the top-ranked prediction).

For reference, the best-supported prediction, urinary tract infection, has the following trials involving meropenem. Most use meropenem as a comparator or co-administered agent, and the role is not always clear from the registry titles:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03477422](https://clinicaltrials.gov/study/NCT03477422) | Phase 3 | Completed | 230 | CSE-1034 (ceftriaxone + sulbactam + EDTA) vs meropenem in cUTI/pyelonephritis due to ESBL/MBL-producing Gram-negative bacteria |
| [NCT03840148](https://clinicaltrials.gov/study/NCT03840148) | Phase 3 | Completed | 661 | Cefepime/VNRX-5133 vs meropenem in adults with cUTI including acute pyelonephritis |
| [NCT02142751](https://clinicaltrials.gov/study/NCT02142751) | Phase 3 | Completed | 161 | Fosfomycin vs meropenem or ceftriaxone in bacteraemic urinary infection due to multidrug-resistant *E. coli* |
| [NCT01970371](https://clinicaltrials.gov/study/NCT01970371) | Phase 3 | Completed | 69 | Plazomicin vs colistin, each combined with meropenem or tigecycline, in carbapenem-resistant Enterobacterales infection |
| [NCT03543436](https://clinicaltrials.gov/study/NCT03543436) | Phase 3 | Completed | 29 | Temocillin vs a carbapenem in ESBL-related urinary tract infection (small trial) |
| [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) | Phase 4 | Suspended | 198 | Piperacillin/tazobactam vs carbapenems in non-bacteraemic ESBL urinary tract infection |
| [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) | Phase 2 | Completed | 134 | Ceftolozane/tazobactam vs meropenem in paediatric cUTI, with a safety and tolerability focus |
| [NCT00771316](https://clinicaltrials.gov/study/NCT00771316) | Phase 3 | Terminated | 6 | MK0826 vs meropenem in cUTI; terminated early with no interpretable efficacy data |
| [NCT03174795](https://clinicaltrials.gov/study/NCT03174795) | Phase 1 | Completed | 20 | Pharmacokinetics of RO7079901 co-administered with meropenem in cUTI |

## Literature Evidence

Literature for the top-ranked prediction, bacterial arthritis, is limited to reviews, case reports and observational or pharmacokinetic work:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/) | 2007 | Case report | Joint Bone Spine | ESBL *Klebsiella pneumoniae* septic arthritis in two immunocompromised patients, treated successfully with meropenem, amikacin and arthroscopic washout |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective review | Indian J Med Microbiol | 22 musculoskeletal melioidosis cases (osteomyelitis, septic arthritis); all isolates susceptible to meropenem |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Cohort | Le Infezioni in Medicina | Retrospective cohort characterising osteoarticular melioidosis |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Off-label use versus formal recommendations of antibiotics for multidrug-resistant bacterial infections |
| [36678359](https://pubmed.ncbi.nlm.nih.gov/36678359/) | 2022 | Review | Pathogens | Antibiotics versus phage therapy for melioidosis |
| [39380073](https://pubmed.ncbi.nlm.nih.gov/39380073/) | 2024 | Case report | J Med Case Rep | Disseminated melioidosis with septic arthritis, initially misdiagnosed |
| [38649034](https://pubmed.ncbi.nlm.nih.gov/38649034/) | 2024 | Preclinical/PK | Int J Antimicrob Agents | Effect of lung injury on tissue penetration of meropenem and vancomycin (not specific to arthritis) |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | PK study | Clin Pharmacokinet | Population pharmacokinetics of meropenem across the adult lifespan |

For the related cUTI indication, higher-quality evidence exists:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) | 2018 | RCT | JAMA | TANGO I: meropenem-vaborbactam vs piperacillin-tazobactam in cUTI, including pyelonephritis |
| [30270406](https://pubmed.ncbi.nlm.nih.gov/30270406/) | 2018 | RCT | Infect Dis Ther | TANGO II: meropenem-vaborbactam vs best available therapy in carbapenem-resistant Enterobacteriaceae infections |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic review / network meta-analysis | J Comp Eff Res | Efficacy of treatment options for cUTI including acute pyelonephritis |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Cohort | Antimicrob Agents Chemother | Meropenem-vaborbactam vs ceftazidime-avibactam in carbapenem-resistant Enterobacteriaceae infections |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004669 | Vaborem | Not specified | Complicated UTI including pyelonephritis, complicated intra-abdominal infection, hospital-acquired pneumonia including VAP, bacteraemia associated with these infections, and infections due to aerobic Gram-negative organisms in adults with limited treatment options... |

This authorization has a **cancelled** status. No currently valid authorization is recorded.

## Safety Considerations

- **Contraindications flagged in the drug knowledge graph (not label text):** epilepsy, kidney disease, pyoureter, thrombocytopenia, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis. These come from model graph edges and need confirmation against the SmPC.
- **Drug interactions:** 14 interactions were identified, of which 3 are Major:
  - Bupropion
  - Iohexol
  - Iopamidol

  Moderate interactions include:
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)
  - Sodium sulfate
  - Nitisinone
  - Lindane
  - Ethinylestradiol
  - Alpelisib
  - Encorafenib
  - Mycophenolic acid
  - Pemetrexed
  - Teriflunomide
- **Other:** Carbapenems are known to interact with valproate, and renal dose adjustment is needed. Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For bacterial arthritis, the top-ranked prediction, there are no clinical trials and only indirect evidence (case reports, retrospective series and susceptibility data), so the evidence level is L4. Several other predictions (laryngitis, *Ureaplasma* urethritis) appear to be graph artifacts, and the rest have effective first-line alternatives. The one well-supported indication, complicated UTI, is already part of the original approved label and would merit "Proceed with Guardrails" (stewardship, reserve use for resistant or ESBL organisms, renal dosing, valproate interaction), but it is not repurposing. The EU authorization for Vaborem is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data to support the mechanistic-link analysis
- Warnings and contraindications from the EMA product information (SmPC), which are currently missing and block safety screening
- Prospective or comparative clinical data for meropenem in bacterial joint infection, including bone and joint penetration pharmacokinetics
- Confirmation of the current EU regulatory status and availability of meropenem-containing products
- A stewardship-based assessment of where meropenem would fit relative to existing first-line options (for example, as a reserve option for ESBL or extensively drug-resistant infections)
- For the paratyphoid fever prediction, a defined research question for extensively drug-resistant enteric fever
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

