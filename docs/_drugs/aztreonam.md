---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: From Gram-Negative Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Aztreonam is a monobactam antibiotic used to treat serious gram-negative aerobic bacterial infections, including urinary tract infections, lower respiratory tract infections, and septicemia.
The TxGNN model identifies **Gonococcal Urethritis** as the most evidence-supported repurposing target, backed by **1 completed Phase 2/3 clinical trial** and **8 publications** directly evaluating aztreonam against *Neisseria gonorrhoeae*.
This repurposing direction is mechanistically sound and clinically timely, given the global emergence of ceftriaxone-resistant gonorrhea with no reliable alternative therapies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (UTI, lower respiratory tract infections, septicemia) |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is unavailable for this report. Based on established pharmacology, Aztreonam is a monocyclic β-lactam (monobactam) antibiotic that selectively binds to Penicillin-Binding Protein 3 (PBP3) on the outer membrane of gram-negative aerobic bacteria, inhibiting cell wall synthesis and triggering bacterial lysis. Its selectivity is narrow and precise — it has no intrinsic activity against gram-positive organisms or anaerobes.

*Neisseria gonorrhoeae*, the causative pathogen of gonorrhea, is a gram-negative diplococcus, placing it squarely within aztreonam's spectrum of action. The PBP3 on gonococci is a high-affinity aztreonam target, providing a strong mechanistic rationale for repurposing. The clinical argument is reinforced by the global antimicrobial resistance crisis: *N. gonorrhoeae* has sequentially developed resistance to sulfonamides, penicillins, tetracyclines, fluoroquinolones, and now increasingly to third-generation cephalosporins (ceftriaxone-resistant gonorrhea, CRNG). The CDC has classified antimicrobial-resistant *N. gonorrhoeae* as one of the top three urgent threats in the United States. With parenteral cephalosporins becoming unreliable, repurposing older antibiotics such as aztreonam represents a rapid path to new rescue therapies.

One critical caveat has emerged from surveillance data: aztreonam-high-resistant *N. gonorrhoeae* strains not producing beta-lactamase have been documented in Japan since 2001 (PMID 11406757). Any clinical deployment must be preceded by local antimicrobial susceptibility testing to confirm aztreonam still covers circulating strains.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Evaluated single-dose aztreonam 2 g IM specifically for pharyngeal gonorrhea — the most difficult anatomical site to eradicate. Framed as a rescue approach for multidrug-resistant *N. gonorrhoeae* given exhaustion of first-line antibiotic classes. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Clinical Trial (Single-arm) | Antimicrobial Agents and Chemotherapy | Open-label trial of aztreonam 2 g IM for *N. gonorrhoeae*, linked to NCT03867734; assessed eradication at pharyngeal and urogenital sites as a ceftriaxone-resistant gonorrhea contingency |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical Study | Antimicrobial Agents and Chemotherapy | Aztreonam 1 g IM vs. spectinomycin 2 g IM for uncomplicated gonorrhea — zero treatment failures in either arm across urethral, rectal, and endocervical sites |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical Study | Genitourinary Medicine | Single 1 g IM injection cleared infection in 61 men and 26 women at all sites; effective against both penicillin-sensitive and penicillin-resistant strains with no adverse effects |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Clinical Study | Journal of Infectious Diseases | Demonstrated efficacy against penicillinase-producing *N. gonorrhoeae* (PPNG) including spectinomycin-resistant strains — established aztreonam's niche in resistant gonorrhea |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Clinical Study | Japanese Journal of Antibiotics | 30 male patients with gonococcal urethritis; bacteriological and clinical evaluation of PPNG (15%) and non-PPNG strains; established early Japanese clinical experience |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Clinical Study | Acta Urologica Japonica | Single-shot aztreonam therapy for gonorrheal infections; epidemiologic analysis of 244 strains including 17.2% PPNG; supported one-dose IM regimen |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Clinical Study | Giornale Italiano di Dermatologia e Venereologia | Early Italian clinical study of aztreonam in acute gonococcal urethritis |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Observational/Microbiology | Journal of Infection and Chemotherapy | **Key resistance signal**: documents emergence of aztreonam-high-resistant *N. gonorrhoeae* not producing beta-lactamase — essential surveillance data for risk stratification before clinical use |

---

## Taiwan Market Information

Aztreonam is currently **not marketed in Taiwan**. There are no active TFDA marketing authorizations on record. Any clinical use in Taiwan would require a special import license or approval through a formal clinical trial protocol.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2/3 trial and eight clinical publications, spanning four decades, consistently support aztreonam's bacteriological and clinical efficacy against *N. gonorrhoeae*. The mechanistic basis is strong, the unmet medical need is urgent (rising CRNG globally), and the drug's existing safety profile is well characterized. The primary guardrail is emerging aztreonam resistance in gonococci, which must be addressed through local susceptibility surveillance before any formal indication development.

**To proceed, the following is needed:**

- **Local susceptibility data**: Confirm aztreonam MIC distribution against circulating Taiwan *N. gonorrhoeae* strains; endemic aztreonam resistance would halt development
- **Full SmPC review**: Obtain TFDA product insert (or EU/US SmPC) to document contraindications, key warnings, and drug-drug interactions
- **MOA confirmation**: Retrieve full mechanism of action data from DrugBank API (DG002 remediation)
- **Dose regimen selection**: Clarify whether 1 g or 2 g IM single dose is optimal; 2020 trial used 2 g for pharyngeal sites
- **Regulatory pathway**: Assess requirements for special import authorization or IND application in Taiwan for formal clinical evaluation
- **Comparative study design**: Define comparator arm (ceftriaxone 500 mg IM currently preferred) and primary endpoint (microbiological cure at all anatomical sites)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

