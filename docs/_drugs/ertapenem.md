---
layout: default
title: Ertapenem
parent: Medium Evidence (L3-L4)
nav_order: 233
evidence_level: L3
indication_count: 10
---

# Ertapenem
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

# Ertapenem: From Complicated Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Ertapenem is a broad-spectrum carbapenem antibiotic with established use against complicated intra-abdominal, skin/soft-tissue, and urinary tract infections. The TxGNN model predicts it may also be effective for **Bacterial Arthritis** (septic arthritis), a direction currently supported by **0 registered clinical trials** but **8 relevant publications** (mostly case reports and retrospective cohorts).

> **Data caveat:** This evidence pack's `original_indications` field is empty and `original_moa` is a data gap. One of the *other* candidates in this pack (rank 7, urinary tract infection) is explicitly flagged internally as an already-approved indication for Ertapenem elsewhere — meaning it is not a genuine new use but an artifact of missing baseline-indication data. Bacterial arthritis, by contrast, is not a labeled indication and represents a real off-label repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Ertapenem holds no Taiwan license (0 authorizations); internal data flags urinary tract infection as an indication already approved for Ertapenem elsewhere, indicating this is a data gap rather than a drug with no prior indications |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ertapenem in this evidence pack. Based on known information, Ertapenem is a broad-spectrum carbapenem (β-lactam) antibiotic with bactericidal activity against most Enterobacteriaceae (including ESBL producers), several anaerobes, and methicillin-susceptible *Staphylococcus aureus* (MSSA). Its established efficacy spans complicated intra-abdominal infections, skin/soft-tissue infections, complicated urinary tract infections, and community-acquired pneumonia.

Bacterial (septic) arthritis is caused predominantly by the same organism classes Ertapenem already targets — Enterobacteriaceae, anaerobes, and MSSA — so extending its use to joint-space infections is a pharmacologically plausible extension rather than a novel mechanism. This is reinforced by Ertapenem's once-daily dosing and long half-life, which make it well suited to the prolonged outpatient parenteral antimicrobial therapy (OPAT) regimens that bone and joint infections typically require.

Real-world practice already reflects this overlap: retrospective cohorts and multiple pathogen-specific case reports (Klebsiella, Citrobacter, Clostridium, Prevotella) describe Ertapenem being used successfully to treat septic arthritis and osteomyelitis, even though no prospective randomized trial has tested it as a primary treatment for bacterial arthritis specifically. This is why the evidence level sits at L3 (observational/case evidence) rather than L1/L2.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Retrospective cohort | Antimicrob Agents Chemother | Among 306 outpatients on long-term ertapenem OPAT, bone and joint infections were a common indication alongside intra-abdominal infections and pneumonia |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Retrospective cohort | J Antimicrob Chemother | Cohort of 10 patients on subcutaneous suppressive β-lactam therapy (including ertapenem) for prosthetic joint infection/chronic osteomyelitis, used as off-label salvage therapy |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Epidemiological/retrospective | Clin Lab | Pathogen distribution and antimicrobial resistance analysis in bone and joint infections in young children |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case report | BMJ Case Reports | Citrobacter koseri osteomyelitis with concomitant gouty arthritis in a diabetic patient, successfully treated with ertapenem |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case report | Anaerobe | First reported case of Clostridium paraputrificum native shoulder septic arthritis and osteomyelitis |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case report | J Chemother | Klebsiella pneumoniae septic wrist arthritis successfully treated with ertapenem plus levofloxacin |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case report | J Investig Med High Impact Case Rep | Prevotella bivia septic arthritis of the knee in an immunocompetent adult |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro/preclinical | Diagn Microbiol Infect Dis | Auranofin restores ertapenem susceptibility against carbapenem-resistant E. coli via synergy (mechanistic, not arthritis-specific) |

## Safety Considerations

Please refer to the SmPC for safety information. Note: this evidence pack flags TFDA labeling data (warnings/contraindications) as a **blocking** data gap (DG001) — a formal S1 safety review cannot proceed until this is obtained, and no drug-drug interaction data was found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for bacterial arthritis is limited to retrospective cohorts and case reports (L3) with no clinical trials or prospective studies, and Ertapenem currently holds no Taiwan marketing authorization. A blocking safety data gap (missing TFDA warnings/contraindications) also prevents completion of the mandatory S1 safety screen.

**To proceed, the following is needed:**
- TFDA-equivalent label data (warnings, contraindications) to close blocking gap DG001
- Detailed mechanism of action documentation from DrugBank to close gap DG002
- Clarification of Ertapenem's Taiwan/global original-indication set, since the current data gap caused urinary tract infection to be mis-flagged as a "new" indication when it is already approved elsewhere
- A prospective or larger comparative study specifically in bacterial/septic arthritis to move evidence from L3 toward L1/L2 before any Guardrails-based proceed decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

