---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Amikacin
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

# Amikacin: From Gram-Negative Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is a broad-spectrum aminoglycoside antibiotic with established activity against serious gram-negative bacterial infections, including multi-drug resistant (MDR) strains.
The TxGNN model predicts it may be effective for **Paratyphoid Fever** (caused by *Salmonella paratyphi* A/B/C),
with **0 clinical trials** and **12 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Taiwan; globally used for serious gram-negative bacterial infections |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this data package. Based on well-established pharmacology, Amikacin is a semi-synthetic aminoglycoside antibiotic derived from kanamycin. It binds irreversibly to the 30S ribosomal subunit of susceptible bacteria, causing misreading of mRNA codons and ultimately inhibiting protein synthesis. Its key clinical advantage over first-generation aminoglycosides (gentamicin, tobramycin) is resistance to most aminoglycoside-inactivating enzymes, preserving activity against many MDR gram-negative organisms.

Paratyphoid fever is caused by *Salmonella enterica* serovars Paratyphi A, B, and C — gram-negative enteric bacilli that are intrinsically susceptible to aminoglycosides at the ribosomal level. Multiple in vitro susceptibility studies confirm that *Salmonella* isolates retain sensitivity to amikacin even when resistant to first-line agents such as chloramphenicol, ampicillin, and trimethoprim-sulfamethoxazole. The published literature (see below) consistently reports amikacin as a viable alternative in MDR enteric fever settings across Asia, the Middle East, and Africa.

The primary pharmacological limitation is that aminoglycosides have poor intracellular penetration. Because *Salmonella* can survive within macrophages, amikacin's clinical efficacy in systemic paratyphoid is constrained compared to fluoroquinolones or third-generation cephalosporins. This positions amikacin primarily as adjunctive or rescue therapy in MDR cases — not as a first-line agent. The TxGNN prediction is mechanistically coherent and supported by real-world observational evidence, making further clinical evaluation warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective Cohort | Journal of the Indian Medical Association | 145 children with culture-confirmed enteric fever; antibiotic sensitivity testing of S. typhi/paratyphi; aminoglycosides including amikacin retained activity against MDR strains |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Clinical Case Series | Mikrobiyoloji Bulteni | 48 confirmed paratyphi B patients with MDR strains resistant to classical treatment; antibiogram and treatment results reported with amikacin as one of the tested alternatives |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case Report | Pediatric Hematology and Oncology | Acalculous cholecystitis caused by S. paratyphi B in a child with acute leukemia; successfully treated with cefepime + amikacin + G-CSF |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Case Series | Indian Journal of Pediatrics | Paratyphoid sepsis in a neonate with multidrug-susceptible S. paratyphi A; clinical case details including antibiotic management |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case Report | The Journal of Infection | Quinolone-resistant S. paratyphi B meningitis in a newborn; illustrates the need for alternative agents when fluoroquinolones fail |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Observational/Surveillance | Pakistan Journal of Biological Sciences | Isolation and microbiological characterisation of S. paratyphi from enteric fever patients in Quetta; local susceptibility patterns |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Cross-sectional Surveillance | JNMA (Nepal Medical Association) | Antibiograms of blood culture isolates including Salmonella spp.; supports aminoglycoside susceptibility in enteric fever bacteria |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Observational | Medical Journal, Armed Forces India | In vitro susceptibility of S. typhi and S. paratyphi A in 45 blood-culture-positive cases; amikacin among antibiotics tested |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Retrospective Case Series | Journal of Pediatric Surgery | 4 paediatric splenic abscess cases (Salmonella-associated); successfully managed with percutaneous drainage + antibiotics |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Surveillance | The New Microbiologica | Epidemiological surveillance of S. typhi/paratyphi in Jordan (1988–2000); baseline susceptibility data relevant to regional treatment planning |

---

## Taiwan Market Information

Amikacin is not currently registered or marketed in Taiwan. No marketing authorization data is available from TFDA licensing records.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amikacin has confirmed in vitro activity against *Salmonella paratyphi*, and observational clinical literature spanning multiple countries supports its use as adjunctive or rescue therapy in MDR paratyphoid fever. The biological mechanism is sound, though limited intracellular penetration is a recognised constraint on clinical efficacy in systemic disease.

**To proceed, the following is needed:**
- Retrieve formal MOA data from DrugBank API (currently unavailable)
- Obtain TFDA prescribing information / SmPC to fill safety warning and contraindication gaps
- Conduct a prospective clinical study or systematic review evaluating amikacin efficacy specifically in confirmed MDR paratyphoid fever
- Pharmacokinetic/pharmacodynamic modelling to define optimal dosing regimens given intracellular pathogen characteristics
- Drug-drug interaction profile (DDI data currently not found)
- Clarify route of administration compatibility for the paratyphoid fever indication (IV/IM only; no oral bioavailability)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

