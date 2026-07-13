---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Infections to Rheumatoid Arthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic approved in major global markets for treating serious Gram-positive bacterial infections, including complicated skin and soft tissue infections, *Staphylococcus aureus* bacteremia, and right-sided endocarditis.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** (rank 2, score 99.84%), with **2 publications** — both from 2025 — providing direct animal model evidence of NF-κB-mediated anti-inflammatory activity in collagen-induced arthritis.
Although **Osteoarthritis** ranks #1 in TxGNN predictions (score 99.86%), analysis of the supporting literature confirms this is a knowledge graph artifact: the associated publications reflect daptomycin use for prosthetic joint infections occurring in OA patients, not any direct therapeutic effect on OA pathology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-positive bacterial infections (complicated skin/soft tissue infections, *S. aureus* bacteremia, right-sided endocarditis) |
| Predicted New Indication | Rheumatoid Arthritis (TxGNN Rank 2; Rank 1 Osteoarthritis confirmed as false positive) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack. Based on published literature, Daptomycin is a cyclic lipopeptide antibiotic whose antibacterial action is calcium-dependent: it inserts its lipophilic tail into the bacterial cell membrane, causes irreversible membrane depolarization, and triggers rapid cell death through intracellular content leakage. This membrane-targeting mechanism is central to both its therapeutic efficacy and its toxicity profile.

The repurposing hypothesis for Rheumatoid Arthritis rests on a pleiotropic mechanism that lies outside this primary antibacterial action. The working model proposes that Daptomycin's hydrophobic tail can intercalate into lipid rafts of immune cell membranes, disrupting Toll-like receptor signaling clusters and indirectly suppressing NF-κB — the master transcriptional regulator driving expression of IL-1β, IL-6, and TNF-α, which are the key cytokines fueling RA synovial inflammation. Additionally, Daptomycin's calcium-chelating capacity may interfere with calcium-dependent immune transcription factors such as NFAT, further dampening adaptive immune activation. RA and bacterial infection share the NF-κB/inflammatory cytokine axis as a common pathological node, which provides a pharmacologically coherent bridge between the original and proposed indications.

Two independent 2025 publications provide the first direct experimental support for this hypothesis. PMID 39571268 demonstrates that daptomycin significantly alleviates collagen-induced arthritis (CIA) in mice — the gold-standard preclinical model for RA — by suppressing NF-κB signaling and downregulating IL-1β, IL-6, and TNF-α, with histological improvement in joint tissue. PMID 40923559 subsequently reports that novel cyclic lipopeptide compounds structurally derived from daptomycin's scaffold achieve even greater anti-arthritic efficacy in the same CIA model, confirming that the lipopeptide architecture itself constitutes an anti-inflammatory pharmacophore. The convergence of two independent research groups publishing concurrently in 2025 elevates this from a speculative signal to a testable mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Daptomycin in Rheumatoid Arthritis (searches conducted via ClinicalTrials.gov and ICTRP as of 2026-03-09).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | Animal Study (CIA Mouse Model) | International Immunopharmacology | **Direct evidence**: Daptomycin alleviates collagen-induced arthritis via NF-κB suppression and downregulation of IL-1β, IL-6, TNF-α — first reported anti-RA evaluation of daptomycin |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | Basic Science / Animal Study | Journal of Medicinal Chemistry | **Direct evidence**: Novel DAP-derived cyclic lipopeptide compounds show enhanced anti-arthritic effects in CIA mice; confirms daptomycin's lipopeptide scaffold as anti-inflammatory pharmacophore |
| [41257050](https://pubmed.ncbi.nlm.nih.gov/41257050/) | 2023 | Observational Study | Journal of Clinical Practice and Research | Surgeon-specific infection rates and risk factors for prosthetic joint infections; daptomycin used as treatment option — RA is background comorbidity, not the treated indication |
| [32650057](https://pubmed.ncbi.nlm.nih.gov/32650057/) | 2020 | In vitro Study | Pharmacological Research | Flufenamic acid (an NSAID used in RA) tested for antibacterial activity against MRSA; daptomycin referenced as comparator — indirect relevance only |
| [27891149](https://pubmed.ncbi.nlm.nih.gov/27891149/) | 2016 | Case Report | Case Reports in Medicine | Daptomycin used for prosthetic valve endocarditis in a patient on chronic prednisone for RA — RA is background comorbidity, daptomycin treats the infection |
| [27031898](https://pubmed.ncbi.nlm.nih.gov/27031898/) | 2016 | Case Report | Le Infezioni in Medicina | Daptomycin for MRSA-infected total hip arthroplasty in a patient with RA — RA is background comorbidity, not treatment target |

> **Note**: Only PMIDs 39571268 and 40923559 are directly relevant to the RA repurposing hypothesis. The remaining four citations involve daptomycin treating infections in patients who happen to carry an RA diagnosis; they do not constitute evidence for daptomycin as an RA therapy.

---

## Taiwan Market Information

Daptomycin is not currently registered in Taiwan's TFDA drug approval database, with zero domestic marketing authorizations on record. The drug is internationally available under the brand name **Cubicin** (originator: Cubist/Merck, now Pfizer), having received US FDA approval in 2003 and EMA approval in Europe. Generic formulations are also globally available. The absence of Taiwan regulatory approval means that TFDA prescribing information, official Chinese-language package insert warnings, and contraindication data have not been formally retrieved — this constitutes a **blocking data gap (DG001)** that must be resolved before any Taiwan-based clinical safety evaluation can proceed.

---

## Safety Considerations

**Key safety signal directly relevant to repurposing:**

- **Rhabdomyolysis (dose-dependent)**: Daptomycin-induced rhabdomyolysis is the most clinically significant adverse effect. A case report (PMID 36693494) documents rhabdomyolysis occurring within the standard 7–10 day antibacterial treatment window, which subsequently triggered acute gouty arthritis through massive purine release and hyperuricemia. For any anti-inflammatory repurposing — which may require prolonged administration or modified dosing regimens — the therapeutic window between anti-inflammatory efficacy and rhabdomyolysis risk must be rigorously characterized. Serum creatine kinase (CK) monitoring is mandatory.
- **Eosinophilic Pneumonia**: A rare but serious pulmonary adverse effect documented in the antibacterial setting; relevance to prolonged or chronic dosing at anti-inflammatory dose ranges is unknown.

For complete warning and contraindication details, please refer to the current SmPC. TFDA prescribing data (DG001 — Blocking severity) has not been retrieved and represents a critical gap before safety profiling in the Taiwan context.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Two independent 2025 animal model studies provide the first direct mechanistic evidence that daptomycin suppresses rheumatoid arthritis-like inflammation in the CIA mouse model via NF-κB pathway inhibition and pro-inflammatory cytokine downregulation. This is a genuine emerging L4 signal — not a knowledge graph artifact — that warrants structured translational investigation. However, the complete absence of human data, the dose-dependent rhabdomyolysis risk, and uncharacterized PK/PD parameters at anti-inflammatory doses mean that clinical development cannot be initiated without substantial additional groundwork.

**To proceed, the following is needed:**

- **Mechanism validation in human cells**: Confirm NF-κB suppression and cytokine downregulation in human RA synovial fibroblasts (FLS) and macrophage cell lines (e.g., THP-1) to bridge the CIA mouse model findings to human biology
- **Dose-response profiling**: Define the anti-inflammatory effective concentration range in animal models and benchmark against the established rhabdomyolysis-risk threshold; assess therapeutic index
- **PK/PD modeling**: Determine whether plasma concentrations achievable within safe human dosing limits can sustain meaningful anti-inflammatory activity at the target tissue (synovium)
- **TFDA safety data retrieval — DG001 (Blocking)**: Download and parse TFDA SmPC PDF to extract all warnings, contraindications, and drug interaction alerts before clinical safety assessment
- **MOA documentation — DG002 (High)**: Query DrugBank API to obtain full mechanism of action, pharmacodynamic targets, and transporter/enzyme interaction profile
- **Benchmark against existing RA therapies**: Assess potential therapeutic differentiation versus conventional DMARDs (methotrexate, leflunomide) and biologics (TNF inhibitors, IL-6 blockers, JAK inhibitors) — daptomycin must show a plausible niche or combination rationale
- **Analog development pathway assessment**: Evaluate whether direct daptomycin repurposing or structural optimization of the cyclic lipopeptide scaffold (as explored in PMID 40923559) is the more viable development strategy, given daptomycin's existing safety liabilities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

