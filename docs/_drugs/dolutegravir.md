---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Dolutegravir (DTG) is a second-generation integrase strand transfer inhibitor (INSTI) established globally as a preferred first-line treatment for HIV-1 infection, though it carries no market authorization in Taiwan.
The TxGNN model predicts it may be effective against **Feline Acquired Immunodeficiency Syndrome (FIV infection in cats)**,
with **1 veterinary observational study** directly supporting this direction; the 5 clinical trials retrieved were human HIV-1 studies matched by DTG's chemical identifier rather than the FIV indication itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan (globally used for HIV-1 infection) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Market Status | ✗ Not Marketed (Taiwan) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Dolutegravir is a second-generation integrase strand transfer inhibitor (INSTI) that blocks retroviral replication by chelating Mg²⁺ ions in the active site of viral integrase, thereby preventing the strand transfer step that inserts viral cDNA into the host genome. Although the mechanism of action field is not populated in this Evidence Pack, DTG's pharmacology is well-documented in published literature: it acts with high potency and maintains a substantially higher barrier to resistance than first-generation INSTIs such as raltegravir, making it the WHO-preferred first-line antiretroviral agent globally.

Feline Immunodeficiency Virus (FIV) is a lentivirus—the same retroviral subfamily as HIV-1—that causes progressive immunodeficiency in domestic cats, closely mirroring the pathophysiology of AIDS in humans. Because FIV encodes a structurally homologous integrase enzyme (sharing the conserved HHCC zinc-binding domain and DDE catalytic triad), the INSTI class is theoretically active against FIV replication. The mechanistic link is therefore biologically coherent: both HIV-1 and FIV rely on integrase-mediated proviral integration, and DTG's binding geometry to this shared active site forms a rational basis for cross-species activity.

A critical caveat is that domestic cats have substantially different pharmacokinetic profiles from humans—particularly reduced glucuronidation capacity (UGT1A deficiency) and distinct CYP450 expression patterns—meaning DTG's absorption, distribution, metabolism, and excretion in cats cannot be directly extrapolated from human data. A 2023 veterinary case series (PMID 37112803) directly addressed this gap by evaluating a cART regimen of DTG (2.5 mg/kg) combined with tenofovir and emtricitabine in FIV-infected domestic cats, examining pharmacokinetics and immunophenotype changes. This represents the first direct clinical evidence for this veterinary repurposing hypothesis, though the study remains preliminary and uncontrolled. This prediction sits firmly in the **veterinary medicine** domain rather than constituting a conventional human drug repurposing scenario.

---

## Clinical Trial Evidence

> **Important context**: All 5 retrieved trials are human HIV-1 studies matched by DTG's development code (GSK1349572). No clinical trials targeting FIV with DTG are currently registered.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | DTG + ABC/3TC vs Atripla (EFV/FTC/TDF) over 96 weeks in HIV-1 ART-naïve adults; demonstrated non-inferior antiviral activity for DTG arm |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | SPRING-2: DTG 50 mg once daily vs raltegravir 400 mg twice daily, both with NRTI backbone; established once-daily DTG dosing advantage |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Phase IIb dose-selection study for DTG in HIV-1 ART-naïve adults with ABC/3TC or TDF/FTC backbone; selected 50 mg QD as optimal dose |
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | DTG vs raltegravir in HIV-1 ART-experienced, integrase inhibitor–naïve adults with investigator-selected background regimen; DTG showed non-inferiority |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Single-arm CNS/plasma PK study of DTG + ABC/3TC in HIV-1 ART-naïve adults; characterized DTG CNS penetration |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Observational / Case Series (Veterinary) | *Viruses* | First evaluation of cART (DTG 2.5 mg/kg + tenofovir 20 mg/kg + emtricitabine 40 mg/kg) in FIV-infected specific pathogen-free domestic cats; examined pharmacokinetics and immunophenotype changes under treatment |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Veterinary context note**: Human safety data for DTG cannot be directly applied to feline patients. Cats' limited glucuronidation capacity (UGT1A deficiency) raises the risk of drug accumulation and dose-dependent toxicity at human-equivalent doses. Species-specific toxicology studies are prerequisite to any clinical feline use.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
While the mechanistic basis for DTG activity against FIV is biologically plausible—both viruses encode homologous integrase enzymes susceptible to INSTI-class inhibition—the current evidence rests on a single uncontrolled veterinary observational study. This is a veterinary medicine application rather than a human drug repurposing scenario, and no authorizations exist in Taiwan. The high TxGNN prediction score (99.85%) most likely reflects the knowledge graph's proximity between HIV and FIV lentiviral nodes rather than direct clinical validation.

**To proceed, the following is needed:**

- Controlled veterinary clinical trials (randomized where feasible) evaluating DTG efficacy, safety, and optimal dosing in FIV-infected cats
- Feline-specific pharmacokinetic/pharmacodynamic studies to characterize DTG absorption, metabolism, and safe dose ranges given known UGT1A limitations in cats
- In vitro FIV integrase susceptibility profiling and resistance mutation characterization for DTG
- Long-term feline safety monitoring data covering hepatic enzymes, renal function, complete blood count, and body weight
- DTG mechanism of action data (DG002 gap: currently absent from Evidence Pack; recommend DrugBank API query)
- Regulatory pathway assessment for veterinary drug authorization in the target jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

