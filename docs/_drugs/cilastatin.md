---
layout: default
title: Cilastatin
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Cilastatin
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

# Cilastatin: From Imipenem Protectant (DHP-I Inhibitor) to Staphylococcus Aureus Infection

## One-Sentence Summary

Cilastatin is a renal dehydropeptidase-I (DHP-I) inhibitor with no intrinsic antibacterial activity, developed exclusively as a pharmacokinetic protectant co-administered with imipenem to prevent its renal inactivation — it has no approved standalone indication.
The TxGNN model predicts it may be effective against **Staphylococcus aureus infection**,
with **3 clinical trials** and **20 publications** currently supporting this direction — all evidence, however, pertains to the **imipenem/cilastatin combination product**, not cilastatin alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered standalone indication (not marketed as a single agent) |
| Predicted New Indication | Staphylococcus aureus infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cilastatin is a specific inhibitor of renal tubular dehydropeptidase-I (DHP-I), an enzyme that hydrolyzes and inactivates imipenem in the kidney before it can reach therapeutic tissue concentrations. By blocking DHP-I, cilastatin preserves imipenem's pharmacokinetic stability, maintaining effective serum and tissue drug levels that enable broad-spectrum antibacterial activity. Cilastatin itself has no antibacterial properties — its sole clinical purpose is to act as a pharmacokinetic enabler for imipenem. Detailed MOA data from DrugBank is currently unavailable (Data Gap DG002).

The biological rationale for the TxGNN prediction derives from the well-documented antibacterial spectrum of the imipenem/cilastatin combination. Imipenem/cilastatin demonstrates excellent coverage against methicillin-susceptible *Staphylococcus aureus* (MSSA), with MICs typically far below clinical breakpoints. Against methicillin-resistant *S. aureus* (MRSA), coverage is significantly reduced — MRSA is intrinsically resistant to all beta-lactams including carbapenems via the *mecA*-encoded PBP2a — but synergistic combinations of imipenem/cilastatin with vancomycin or fosfomycin have been explored in refractory or bacteremic MRSA cases. Early observational studies (Fan et al., 1986) and more recent case reports (Sakoulas, 2020) document clinical responses across both MSSA and select MRSA contexts.

**Critical limitation**: All supporting evidence originates from the **imipenem/cilastatin combination**, not from cilastatin as an isolated agent. Any repurposing trajectory must be attributed to the combination product, with cilastatin explicitly identified as the pharmacokinetic enabler rather than the active antibacterial component. This distinction is essential for regulatory framing and clinical translation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational RCT — imipenem/cilastatin/relebactam vs piperacillin/tazobactam for HABP/VABP; non-inferiority in 28-day all-cause mortality demonstrated; covers serious S. aureus-related pneumonia |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Phase 2 | Terminated | 108 | Tigecycline vs imipenem/cilastatin for hospital-acquired pneumonia (≥70% VAP); two dose levels of tigecycline assessed; terminated early with unclear cause — data completeness uncertain |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Linezolid ± carbapenem for MRSA VAP — imipenem/cilastatin used as adjunct, not primary intervention; status unknown, reliability low |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Clinical Observational | Antimicrobial Agents and Chemotherapy | Imipenem-cilastatin in 23 patients (11 MRSA, 12 MSSA) — effective for MSSA soft tissue, endovascular, skeletal infections; limited efficacy against MRSA |
| [8072190](https://pubmed.ncbi.nlm.nih.gov/8072190/) | 1994 | Clinical Observational | Japanese Journal of Antibiotics | Arbekacin + imipenem/cilastatin combination showed synergistic MIC reductions against MRSA clinical isolates compared to either agent alone |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In Vitro / In Vivo | Journal of Antimicrobial Chemotherapy | Vancomycin + imipenem showed synergy/additivity in 36 of 36 MRSA isolates in vitro and confirmed efficacy in neutropenic mouse thigh infection model |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Review | International Journal of Antimicrobial Agents | Comprehensive review of MRSA pathogenesis, virulence strategies, and key clinical trials; includes analysis of imipenem-based combination regimens for serious MRSA infections |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case Report | Antimicrobial Agents and Chemotherapy | Imipenem/cilastatin + fosfomycin novel combination for refractory bacteremic MRSA infection — individualized therapy as a model for challenging cases unlikely to yield RCT data |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Narrative Review | International Journal of Antimicrobial Agents | Off-label antibiotic use for MDR Gram-positive cocci including MRSA and VRE; discusses carbapenem-based combination strategies in treatment-refractory settings |
| [18649613](https://pubmed.ncbi.nlm.nih.gov/18649613/) | 2008 | Review | American Family Physician | Diabetic foot infections — S. aureus and beta-hemolytic streptococci as dominant pathogens; imipenem/cilastatin among options for severe polymicrobial cases |
| [3378959](https://pubmed.ncbi.nlm.nih.gov/3378959/) | 1988 | Animal Model | Journal of Antimicrobial Chemotherapy | Imipenem/cilastatin vs vancomycin in rabbit MRSA aortic valve endocarditis — imipenem bacteriostatic (MIC90 8 mg/L) while vancomycin bactericidal (MIC90 2 mg/L); imipenem showed better vegetal sterilization criteria despite lower in vitro activity |
| [8514648](https://pubmed.ncbi.nlm.nih.gov/8514648/) | 1993 | Animal Model | Journal of Antimicrobial Chemotherapy | Imipenem/cilastatin + cefotiam synergistic activity in mouse bacteremia model — effective against both beta-lactamase-producing and non-producing MRSA strains |
| [12878512](https://pubmed.ncbi.nlm.nih.gov/12878512/) | 2003 | Animal Model | Antimicrobial Agents and Chemotherapy | Imipenem-cilastatin inactive against MRSA in systemic infection model (ED50 >100 mg/kg) vs vancomycin (ED50 ~7 mg/kg) — directly quantifies activity limitation against MRSA |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The imipenem/cilastatin combination carries Phase 3 RCT-level evidence (L1) for serious bacterial infections encompassing susceptible *S. aureus*, and published combination strategies exist for refractory MRSA contexts, making the TxGNN prediction biologically plausible. However, cilastatin itself is not the antibacterial agent — all clinical benefit derives from imipenem — and no standalone repurposing case for cilastatin can be constructed without acknowledging this fundamental pharmacological dependency.

**To proceed, the following is needed:**

- **Reframe the candidate**: All downstream analysis should attribute the therapeutic effect to imipenem/cilastatin as a combination; cilastatin should be described as the pharmacokinetic enabler, not the active moiety
- **Resolve Data Gap DG001 (Blocking)**: Obtain SmPC/TFDA prescribing information to complete safety profiling — warnings, contraindications, and precautions are currently unavailable
- **Resolve Data Gap DG002 (High)**: Query DrugBank API for cilastatin MOA entry to formally document DHP-I inhibition mechanism in the evidence record
- **Narrow the indication**: "Staphylococcus aureus infection" is overly broad; define a specific clinical scenario (e.g., MSSA bacteremia, S. aureus HAP in ICU, refractory MRSA bacteremia with combination therapy) for a focused evidence synthesis
- **MRSA vs MSSA stratification**: Separate evidence streams for MSSA (strong coverage) and MRSA (limited intrinsic activity; requires combination) are needed before any formulary or guideline proposal
- **Antimicrobial stewardship review**: Carbapenem-class agents face stewardship restrictions in most health systems; any proposed expansion of use requires institutional prescribing pathway documentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

