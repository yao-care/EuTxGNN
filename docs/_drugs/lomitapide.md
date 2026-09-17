---
layout: default
title: Lomitapide
parent: High Evidence (L1-L2)
nav_order: 361
evidence_level: L1
indication_count: 10
---

# Lomitapide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Lomitapide: From Homozygous Familial Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Lomitapide is a microsomal triglyceride transfer protein (MTP) inhibitor originally developed and used for homozygous familial hypercholesterolemia (HoFH). Among the 10 TxGNN-predicted indications in this evidence pack, only **Hyperlipoproteinemia** is backed by real-world evidence — **12 clinical trials and 19 publications** — while the nine higher-ranked candidates (all rare platelet disorders) have **zero clinical trials or literature** and appear to be a systematic prediction artifact rather than genuine signals.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Homozygous Familial Hypercholesterolemia (HoFH) — inferred from clinical evidence context; no formal Taiwan/EU license record is available in this dataset |
| Predicted New Indication | Hyperlipoproteinemia (rank 9 of 10; the only candidate with supporting evidence) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on the top-ranked candidates**: TxGNN's highest-scoring predictions (rank 1–8, 10; scores 0.995–0.999) are all rare platelet/hemostasis disorders — e.g. *marcothrombocytopenia with mitral valve insufficiency*, *Glanzmann thrombasthenia*, *dense granule disease*. None have any supporting clinical trial or literature evidence, and the evidence pack itself flags this as a likely **systematic clustering bias** in the knowledge graph rather than a genuine mechanistic signal. These are scored "Hold" and are not discussed further in this report.

## Why is This Prediction Reasonable?

Lomitapide is a microsomal triglyceride transfer protein (MTP) inhibitor. It blocks the assembly and secretion of hepatic VLDL and intestinal chylomicrons, thereby directly lowering ApoB-containing lipoproteins (LDL-C). This is the drug's well-established core pharmacology, already exploited clinically in HoFH.

"Hyperlipoproteinemia" as a predicted indication is not a mechanistically distant "new use" — it is a broader disease-classification term that encompasses HoFH and related dyslipidemias. In other words, the TxGNN model is largely re-identifying the drug's known therapeutic space rather than proposing a genuinely novel repurposing hypothesis. The supporting trials (see below) are overwhelmingly Lomitapide-in-HoFH studies (adult, pediatric, Japanese, and long-term follow-on populations), plus one related program in familial chylomicronemia syndrome (FCS), which is mechanistically adjacent (triglyceride/ApoB metabolism).

Given the drug's original MOA and the disease overlap, the biological plausibility is high — but this should be framed as **evidence consolidation/label-adjacent expansion** rather than true repurposing into an unrelated therapeutic area.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04681170](https://clinicaltrials.gov/study/NCT04681170) | Phase 3 | Completed | 46 | Single-arm, open-label study of Lomitapide efficacy/long-term safety in pediatric HoFH patients on stable lipid-lowering therapy |
| [NCT00730236](https://clinicaltrials.gov/study/NCT00730236) | Phase 3 | Completed | 29 | Pivotal registration trial of AEGR-733 (Lomitapide) in HoFH; basis for original approval |
| [NCT02173158](https://clinicaltrials.gov/study/NCT02173158) | Phase 3 | Completed | 9 | Efficacy/safety of Lomitapide in Japanese HoFH patients on concurrent lipid-lowering therapy |
| [NCT00943306](https://clinicaltrials.gov/study/NCT00943306) | Phase 3 | Completed | 19 | Long-term follow-on study confirming continued efficacy/safety of Lomitapide in HoFH |
| [NCT02135705](https://clinicaltrials.gov/study/NCT02135705) | N/A | Recruiting | 300 | LOWER Registry — global, long-term, prospective observational cohort on real-world safety/effectiveness |
| [NCT06832371](https://clinicaltrials.gov/study/NCT06832371) | N/A | Active, not recruiting | 73 | Observational study evaluating major adverse cardiovascular events (MACE) in HoFH patients on Lomitapide |
| [NCT00690443](https://clinicaltrials.gov/study/NCT00690443) | Phase 2 | Completed | 44 | Randomized, double-blind trial of AEGR-733 + atorvastatin vs. atorvastatin monotherapy in moderate hypercholesterolemia |
| [NCT00559962](https://clinicaltrials.gov/study/NCT00559962) | Phase 2 | Completed | 260 | Randomized, placebo-controlled study of low-dose MTP inhibitor on hepatic fat accumulation |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Open-label dose-escalation study establishing safety/tolerability of Lomitapide across 4 dose levels in HoFH |

*Three trials (NCT02399852, NCT02765841 — both withdrawn with 0 enrollment; NCT05611528 — an Evinacumab trial, not Lomitapide) were excluded as low-relevance or off-target.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39426393](https://pubmed.ncbi.nlm.nih.gov/39426393/) | 2024 | Phase 3 Study | Lancet Diabetes Endocrinol | APH-19: efficacy/safety results of Lomitapide in pediatric HoFH patients on standard-of-care lipid-lowering therapy |
| [40494715](https://pubmed.ncbi.nlm.nih.gov/40494715/) | 2025 | Review | J Clin Lipidol | Over 10 years of long-term efficacy and safety experience with Lomitapide in HoFH |
| [36152419](https://pubmed.ncbi.nlm.nih.gov/36152419/) | 2022 | Review | Atherosclerosis | Efficacy/safety of Lomitapide extended to familial chylomicronemia syndrome (FCS) |
| [35148370](https://pubmed.ncbi.nlm.nih.gov/35148370/) | 2022 | Review | Eur J Prev Cardiol | Understanding the efficacy and safety of Lomitapide in HoFH |
| [33829367](https://pubmed.ncbi.nlm.nih.gov/33829367/) | 2021 | Review | Advances in Therapy | Real-world case reports of Lomitapide use in HoFH patients in Saudi Arabia |
| [31741187](https://pubmed.ncbi.nlm.nih.gov/31741187/) | 2019 | Review | Curr Atheroscler Rep | Lomitapide and Mipomersen — MTP and apoB100 synthesis inhibition mechanisms |
| [28598687](https://pubmed.ncbi.nlm.nih.gov/28598687/) | 2017 | Review | Expert Opin Pharmacother | Lomitapide for the treatment of hypercholesterolemia |
| [25936301](https://pubmed.ncbi.nlm.nih.gov/25936301/) | 2015 | Review | Atherosclerosis Suppl | Mipomersen and Lomitapide as new HoFH treatment options |
| [24231894](https://pubmed.ncbi.nlm.nih.gov/24231894/) | 2014 | Review | J Cardiovasc Nurs | Lomitapide and Mipomersen — novel lipid-lowering agents for FH management |
| [21846156](https://pubmed.ncbi.nlm.nih.gov/21846156/) | 2011 | Review | Am J Cardiovasc Drugs | Early development review of Lomitapide as an MTP inhibitor for hypercholesterolemia |

## EU Market Information

Lomitapide is currently **not marketed** in this dataset's regulatory registry (market status: Not marketed, total authorizations: 0). No marketing authorization records are available to summarize.

## Safety Considerations

Structured safety fields (key warnings, contraindications, DDI) are marked as data gaps (DG001, severity: Blocking) and could not be populated from TFDA/EMA sources in this pack.

Contextual note from the evidence review: one prediction rationale in this pack independently flags that Lomitapide carries **serious hepatotoxicity and teratogenicity warnings**, consistent with its known boxed-warning profile as an MTP inhibitor. This has not been formally verified against a parsed SmPC/label in this evidence pack.

Please refer to the SmPC for complete safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2/3 trials and a substantial literature base support Lomitapide's efficacy in the HoFH/hyperlipoproteinemia space, but this largely reflects the drug's *already-established* therapeutic use rather than a novel repurposing opportunity. Formal safety documentation (TFDA/EMA label) is missing and is flagged as a Blocking gap, preventing a full S1 safety assessment.

**To proceed, the following is needed:**
- TFDA/EMA product label (warnings, contraindications) to close the Blocking data gap (DG001) before any safety-stage evaluation
- Confirmed mechanism of action data via DrugBank API to formally close DG002 (currently inferred only from trial/literature narrative)
- Clarification of whether "Hyperlipoproteinemia" represents a distinct regulatory opportunity or is already covered under existing HoFH indications in relevant markets
- No further action recommended on the nine platelet-disorder predictions (ranks 1–8, 10) unless independent mechanistic or clinical evidence emerges — current pattern is consistent with a knowledge-graph prediction artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

