---
layout: default
title: Amikacin
parent: Medium Evidence (L3-L4)
nav_order: 44
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Amikacin: predicted new indication Paratyphoid fever (evidence level L4). Approved use: NTM lung infections caused by Mycobacterium avium Complex (MAC) in ad…"
monitor_inn: "Amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "meningococcemia"]
---

# Amikacin
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

# Amikacin: From Non-Tuberculous Mycobacterial Lung Infection to Paratyphoid Fever

## One-Sentence Summary

Amikacin is an aminoglycoside antibiotic. Its liposomal inhaled form (Arikayce liposomal) was authorised in the EU for non-tuberculous mycobacterial (NTM) lung infections caused by *Mycobacterium avium* Complex (MAC).
The TxGNN model predicts it may be effective for **paratyphoid fever**, but there are currently **0 registered clinical trials** and **8 publications**, all of them surveillance, susceptibility or case-level reports with no amikacin-specific outcome data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NTM lung infections caused by *Mycobacterium avium* Complex (MAC) in adults with limited treatment options who do not have cystic fibrosis |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Amikacin is known to be an aminoglycoside that inhibits the bacterial 30S ribosomal subunit and has broad Gram-negative activity. This makes activity against *Salmonella enterica* serovar Paratyphi plausible on paper.

The original indication (a mycobacterial lung infection) and the predicted indication (an enteric *Salmonella* infection) are both bacterial infections, which is probably why the model links them. However, there are important mechanistic limits. *Salmonella* is a facultative intracellular pathogen, and aminoglycosides penetrate host cells poorly. In vitro susceptibility therefore does not translate reliably into clinical efficacy, and aminoglycosides are not standard therapy for enteric fever.

The literature gathered contains no amikacin-specific clinical outcome data for paratyphoid fever. Related typhoid fever evidence points the same way: one small study reported a clinical effective rate of 36.4% for amikacin versus 100% for ofloxacin (PMID 2598731). At most, amikacin could be a salvage option for extensively drug-resistant isolates, which would need dedicated clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective cohort | J Indian Med Assoc | 145 blood-culture-positive paediatric enteric fever cases; clinical profile and antibiotic sensitivity of *S. typhi* and *S. paratyphi* |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Clinical report | Mikrobiyol Bul | 48 patients with paratyphi B infection resistant to classical treatment; antibiotics used and outcomes reported |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatr Hematol Oncol | Child with leukaemia and acalculous cholecystitis due to *S. paratyphi* B, treated successfully with cefepime, amikacin and granulocyte support (combination therapy) |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Susceptibility study | Med J Armed Forces India | In vitro susceptibility of *S. typhi* and *S. paratyphi* A from 45 enteric fever cases; chloramphenicol sensitivity re-emerging |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiology | New Microbiol | Occurrence of *S. typhi* and *S. paratyphi* in Jordan, 1988–2000 |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Microbiological study | Pak J Biol Sci | Isolation and identification of *S. paratyphi* from enteric fever patients in Quetta |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Antibiogram survey | JNMA J Nepal Med Assoc | Blood culture isolates and antibiograms in a teaching hospital |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case series | J Pediatr Surg | Splenic abscess in 4 children managed by needle aspiration and antibiotics (only indirect relevance) |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005264 (cancelled) | Arikayce liposomal | Not specified | Treatment of non-tuberculous mycobacterial (NTM) lung infections caused by *Mycobacterium avium* Complex (MAC) in adults with limited... |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, pyoureter, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, central nervous system origin vertigo, myasthenia gravis (including adult-onset), neuromuscular junction disease, parkinsonian disorders and Parkinson disease.
- **Drug Interactions:** 100 interactions were identified. The major-level ones in the data reviewed are **magnesium sulfate** and **mannitol**. Moderate-level interactions include other aminoglycosides (kanamycin, neomycin), amphotericin B formulations, proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole), aspirin, mesalazine and related agents, and exenatide.

Please also refer to the SmPC for full safety information, as label-based warnings and contraindications were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is a computational output. There are no clinical trials, and the literature is almost entirely epidemiology and susceptibility data with no amikacin-specific outcome evidence for paratyphoid fever. Aminoglycosides penetrate cells poorly, effective standard therapies exist, and the only comparative signal in related typhoid literature was unfavourable for amikacin. The product's only EU authorisation is also cancelled.

**To proceed, the following is needed:**
- Label-based warnings and contraindications from the SmPC (currently a blocking safety data gap)
- Mechanism of action data (for example from DrugBank)
- Clinical outcome data for amikacin in enteric fever, ideally restricted to extensively drug-resistant isolates
- A nephrotoxicity and ototoxicity risk assessment, given the kidney and neuromuscular associations flagged
- Clarification of the route of administration, since the previously authorised product is an inhaled liposomal formulation and enteric fever would require systemic dosing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

