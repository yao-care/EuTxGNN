---
layout: default
title: Avanafil
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Avanafil
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

# Avanafil: From Erectile Dysfunction to Raynaud Disease

## One-Sentence Summary

Avanafil is a selective PDE5 inhibitor approved in multiple markets for erectile dysfunction, functioning through the same cGMP-mediated vasodilation pathway as its sibling drugs Sildenafil and Tadalafil.

The TxGNN model generated **10 predicted repurposing candidates**, of which **Raynaud disease** emerges as the most mechanistically grounded new indication — supported by robust class-effect evidence from Sildenafil and Tadalafil (multiple completed RCTs), though no Avanafil-specific clinical data exists to date.

Three of the top 10 predictions are veterinary diseases representing knowledge graph noise, and one uses a deprecated ontology term; the actionable human-disease signal is concentrated in **Raynaud disease**, with secondary interest in amenorrhea and stroke-related indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erectile dysfunction |
| Featured Predicted Indication | Raynaud disease *(highest-evidence candidate among 10 predictions)* |
| TxGNN Prediction Score | 88.54% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Prediction Landscape (Top 10)

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Signal Quality |
|------|---------|-------------|----------------|----------|----------------|
| 1 | Amenorrhea | 94.59% | L5 | Hold | Weak — indirect KG path via reproductive vasculature |
| 2 | Hypoalphalipoproteinemia | 91.54% | L5 | Hold | Weak — no direct mechanistic link to HDL |
| 3 | Infectious bovine rhinotracheitis | 90.62% | L5 | Hold | ⚠️ Veterinary disease — KG cross-species noise |
| 4 | Malignant catarrh | 90.62% | L5 | Hold | ⚠️ Veterinary disease — KG batch-scoring noise |
| **5** | **Raynaud disease** | **88.54%** | **L4** | **Research Question** | ✅ Strong class-effect from Sildenafil/Tadalafil RCTs |
| 6 | Ambras hypertrichosis universalis congenita | 87.79% | L5 | Hold | Weak — monogenic developmental disorder, no PDE5 rationale |
| 7 | Ischemic stroke susceptibility *(obsolete)* | 87.28% | L5 | Hold | ⚠️ Deprecated ontology node — consider mapping to ischemic stroke |
| 8 | Malformation w/ periodontal component | 80.46% | L5 | Hold | ⚠️ 20 literature hits are irrelevant periodontology background |
| 9 | Stroke disorder | 79.21% | L5 | Hold | Weak — overlaps with #7; preclinical signal only |
| 10 | Adrenal gland hyperfunction | 79.06% | L5 | Hold | Weak — no known PDE5–adrenal cortex mechanistic link |

---

## Why is This Prediction Reasonable?

Avanafil belongs to the PDE5 (phosphodiesterase type 5) inhibitor class, which also includes Sildenafil and Tadalafil. All three drugs block PDE5-mediated degradation of cyclic GMP (cGMP) in vascular smooth muscle, leading to sustained vasodilation. Detailed mechanism of action data was not available in this Evidence Pack; however, Avanafil's class membership, selectivity profile, and clinical pharmacology are well-characterized in the published literature and its approved SmPC.

Raynaud disease is defined by episodic vasospasm of the digital arteries triggered by cold or emotional stress, causing ischemia, pain, and characteristic color changes in the extremities. The PDE5 inhibitor mechanism — amplifying cGMP signaling to promote vasodilation and reduce vascular tone — directly counteracts this vasospastic pathophysiology. Multiple Phase 2/3 RCTs and systematic reviews have demonstrated that Sildenafil and Tadalafil significantly reduce the frequency, duration, and severity of Raynaud attacks, establishing a clear class-effect rationale. Avanafil's shared mechanism makes it a pharmacologically logical candidate for the same therapeutic goal.

A critical open question is pharmacokinetic suitability. Avanafil has a relatively fast onset and shorter effective duration (~6 hours) compared to Tadalafil (~17–36 hours). Raynaud disease management typically benefits from sustained baseline vasodilation rather than on-demand dosing, which may favor Tadalafil's profile. Whether Avanafil's kinetics can be adapted through twice-daily dosing or if they represent a genuine limitation is the central research question to resolve before committing resources to a clinical trial.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating Avanafil for Raynaud disease, or for any of the 10 predicted indications, are registered on ClinicalTrials.gov or ICTRP.

> Class-effect trial evidence exists for Sildenafil and Tadalafil in Raynaud disease (multiple completed Phase 2/3 studies) but these fall outside the scope of this Avanafil-specific Evidence Pack and are not tabulated here.

---

## Literature Evidence

Currently no publications directly linking Avanafil to Raynaud disease, or to any of the other 10 predicted indications, were identified.

> The 20 publications retrieved under the periodontal indication (rank 8) are general periodontology background literature (microbiology, surgical technique, inflammation pathways) with no connection to Avanafil or PDE5 inhibition. These are irrelevant keyword-collision hits and are excluded from this report.

---

## Taiwan Market Information

Avanafil does not hold any marketing authorization in Taiwan as of the data cutoff (2026-06-01).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No authorizations on record |

> For reference: Avanafil is approved in the EU as **Spedra** (Menarini) and in the US as **Stendra** (Vivus/Endo International) for erectile dysfunction. A Taiwan regulatory submission would be required before any repurposing trial could be initiated locally.

---

## Safety Considerations

Detailed safety data including key warnings, contraindications, and drug-drug interactions were not available in this Evidence Pack.

Please refer to the current Summary of Product Characteristics (SmPC) or the TFDA prescribing information for complete safety information before proceeding with any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Research Question** *(Raynaud disease only)* **/ Hold** *(all other 9 predicted indications)*

**Rationale:**
Raynaud disease is the sole prediction with a mechanistically coherent link to PDE5 inhibition and with indirect supporting evidence from the same drug class; the remaining nine predictions lack either mechanistic grounding or direct clinical evidence, and three are veterinary or deprecated-ontology entries that should be dismissed as knowledge graph artifacts.

**To advance the Raynaud disease research question, the following steps are needed:**

- **Close the MOA data gap**: Retrieve Avanafil's full pharmacological profile from DrugBank or the approved SmPC to formally confirm PDE5 selectivity, tissue distribution, and kinetic parameters
- **Close the safety data gap (blocking)**: Obtain TFDA SmPC warnings and contraindications — flagged as a blocking gap in this pack; this must be resolved before any safety assessment can proceed
- **Class-effect literature synthesis**: Conduct a structured review of Sildenafil and Tadalafil RCTs in Raynaud disease to quantify expected effect sizes and optimal dosing regimens
- **Pharmacokinetic suitability assessment**: Formally evaluate whether Avanafil's shorter half-life (~6 h) is compatible with chronic Raynaud prophylaxis, or whether twice-daily dosing would mitigate this
- **Taiwan regulatory pathway mapping**: Since Avanafil is not marketed in Taiwan, determine the feasibility of an investigational use authorization or expedited review for a repurposing study
- **Pilot trial design**: If the above assessments are favorable, consider a small investigator-initiated trial (IIT) using the existing Sildenafil Raynaud RCT protocols as a design template
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

