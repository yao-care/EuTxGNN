---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Hydroxocobalamin
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

Using the report template above (no skill match for this pure write‑up task — it's a direct data‑to‑markdown transformation, not TxGNN pipeline engineering), I built the report from the Evidence Pack. One structural note before the report: `predicted_indications[0]` (the headline candidate per the template's extraction rule) turns out to have **zero supporting evidence** and a rationale that itself flags weak mechanistic plausibility, while a lower-ranked candidate (rank 9, vitamin deficiency disorder) has real trial/literature support but is likely just recovering the drug's already-known core use (masked here because `original_indications` is empty due to a data gap). I followed the template's mandated structure for the rank‑1 candidate, and added one extra transparency table (not part of the template, but necessary given this is a 10-indication batch) so the discrepancy isn't hidden.

---

# Hydroxocobalamin: From Vitamin B12 Deficiency to Esophageal Varices with Bleeding

> **Note on scope:** This Evidence Pack contains 10 TxGNN-predicted indications for Hydroxocobalamin. Per the reporting convention, this report focuses on the top-ranked prediction (Esophageal Varices with Bleeding). A summary of all 10 predictions is provided in the "Other Predicted Indications in This Batch" section, because the top-ranked prediction has no supporting evidence while a lower-ranked one does.

## One-Sentence Summary

Hydroxocobalamin (DB00200) is the parenteral form of vitamin B12; formal original-indication and mechanism-of-action data are flagged as data gaps in this pack, and no EU marketing authorization record exists for it in this dataset. The TxGNN model's top prediction is **Esophageal Varices with Bleeding** (score **99.23%**), but this prediction currently has **zero clinical trials and zero publications** supporting it, and the model's own rationale flags the mechanistic link as unsubstantiated — this is an **L5, AI-prediction-only** candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this pack (no EU license record; `original_indications` and `original_moa` are data gaps). Hydroxocobalamin is generally known as an injectable vitamin B12 form used for B12 deficiency and as a cyanide-poisoning antidote — general background knowledge, not confirmed by this Evidence Pack |
| Predicted New Indication | Esophageal Varices with Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Hydroxocobalamin in this pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, Hydroxocobalamin is a cobalamin (vitamin B12) analogue whose established actions are (1) correction of B12 deficiency and (2) detoxification of cyanide, via binding of the cyanide ion to form cyanocobalamin, which is renally excreted.

Esophageal varices with bleeding is a complication of portal hypertension secondary to cirrhosis — a vascular/hemodynamic disease process with no established connection to B12 metabolism or cyanide detoxification. The Evidence Pack's own rationale for this prediction states that the high TxGNN score "very likely reflects an indirect connection through vascular/bleeding-related nodes in the knowledge graph, lacking pharmacological plausibility," and no clinical trial or literature evidence was found for this drug–disease pair.

In short: mechanistically, this prediction is **not well supported**. The high score most plausibly reflects a knowledge-graph artifact (shared "bleeding/vascular" neighbor nodes) rather than a genuine pharmacological signal, and should be treated as a low-confidence hypothesis requiring independent mechanistic validation before any further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorization records were found for Hydroxocobalamin in this dataset (market status: Not Marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and DDI data are all marked as data gaps in this pack — DG001, "TFDA/EMA label warnings and contraindications," is flagged as a Blocking severity gap that must be resolved before any Stage 1 safety assessment.)*

---

## Other Predicted Indications in This Batch

Because the top-ranked prediction (above) has no supporting evidence, the full batch is summarized here for transparency:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Esophageal varices with bleeding | 99.23% | L5 | S0 | Hold |
| 2 | Esophageal varices without bleeding | 99.23% | L5 | S0 | Hold |
| 3 | Varicose disease | 98.89% | L5 | S0 | Hold |
| 4 | Immune-mediated necrotizing myopathy | 98.69% | L5 | S0 | Hold |
| 5 | Antisynthetase syndrome | 98.64% | L5 | S0 | Hold |
| 6 | Focal myositis | 98.56% | L5 | S0 | Hold |
| 7 | Inflammatory myopathy with abundant macrophages | 98.46% | L5 | S0 | Hold |
| 8 | Idiopathic eosinophilic myositis | 98.46% | L5 | S0 | Hold |
| **9** | **Vitamin deficiency disorder** | 98.44% | **L2** | **S3** | **Proceed with Guardrails*** |
| 10 | Congenital prothrombin deficiency | 98.32% | L5 | S0 | Hold |

\* **Important caveat:** "Vitamin deficiency disorder" is the only candidate in this batch with real supporting evidence (below), but this most likely represents Hydroxocobalamin's **already-established core use** (B12/cobalamin deficiency treatment) resurfacing as a "new" prediction — an artifact of the `original_indications` field being empty in this pack (data gap), not a genuine repurposing discovery. It is presented below for completeness, not as the headline finding.

### Supporting Evidence for "Vitamin Deficiency Disorder" (Rank 9, for reference only)

**Clinical Trials** (10 most relevant of 50 returned, by relevance grade):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06441721](https://clinicaltrials.gov/study/NCT06441721) | N/A | Not yet recruiting | 60 | Evaluates B12 level in chronic haemodialysis patients and its effect on anaemia and neuropathy |
| [NCT00843453](https://clinicaltrials.gov/study/NCT00843453) | N/A | Completed | 36 | Long-term PPI use and B12 deficiency in institutionalized elderly; tested cyanocobalamin nasal spray for repletion |
| [NCT00710138](https://clinicaltrials.gov/study/NCT00710138) | N/A | Completed | 100 | Cobalamin status in young children with developmental delay/regression; cobalamin treatment resolved symptoms |
| [NCT00326833](https://clinicaltrials.gov/study/NCT00326833) | Phase 4 | Unknown | 50 | Studies actual clinical need for vitamin B12 injection therapy |
| [NCT05099185](https://clinicaltrials.gov/study/NCT05099185) | N/A | Completed | 39 | Measures water-soluble vitamin (incl. B12) loss during post-dilution haemodiafiltration |
| [NCT03489538](https://clinicaltrials.gov/study/NCT03489538) | N/A | Completed | 708 | Homocysteine/B12-related metabolic changes after laparoscopic Roux-en-Y gastric bypass |
| [NCT00276198](https://clinicaltrials.gov/study/NCT00276198) | Phase 3 | Completed | 771 | Multi-micronutrient (incl. B12) supplementation effect on nutritional/health indicators in infants |
| [NCT04160767](https://clinicaltrials.gov/study/NCT04160767) | Phase 4 | Unknown | 90 | Probiotic supplementation effect on B6/B12/folate/vitamin D status in celiac patients |
| [NCT01465867](https://clinicaltrials.gov/study/NCT01465867) | N/A | Completed | 56 | Selenium (not B12) supplementation in autoimmune thyroid disease during pregnancy |
| [NCT00197743](https://clinicaltrials.gov/study/NCT00197743) | Phase 3 | Completed | 1085 | General multivitamin supplementation in HIV+ pregnant women, not B12-specific |

**Literature** (10 most relevant, prioritized by Guideline/Review tier):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24942828](https://pubmed.ncbi.nlm.nih.gov/24942828/) | 2014 | Guideline | British Journal of Haematology | Diagnosis/treatment guidelines for cobalamin and folate disorders |
| [27905001](https://pubmed.ncbi.nlm.nih.gov/27905001/) | 2017 | Guideline | Journal of Inherited Metabolic Disease | Guidelines for cobalamin-related remethylation disorders (cblC, cblD, etc.) |
| [25117994](https://pubmed.ncbi.nlm.nih.gov/25117994/) | 2015 | Review | European Journal of Clinical Nutrition | Clarifies treatment choice among methylcobalamin, cyanocobalamin, and hydroxocobalamin for B12 deficiency |
| [25189324](https://pubmed.ncbi.nlm.nih.gov/25189324/) | 2014 | Review | BMJ | Overview of vitamin B12 deficiency |
| [38987879](https://pubmed.ncbi.nlm.nih.gov/38987879/) | 2024 | Review | Food and Nutrition Bulletin | Brief overview of diagnosis and treatment of cobalamin (B12) deficiency |
| [32332011](https://pubmed.ncbi.nlm.nih.gov/32332011/) | 2020 | Review | BMJ | Overview of pernicious anaemia |
| [36669740](https://pubmed.ncbi.nlm.nih.gov/36669740/) | 2023 | Review | Revista Clínica Española | Vitamin B12/hydroxocobalamin uses beyond megaloblastic anemia |
| [11757269](https://pubmed.ncbi.nlm.nih.gov/11757269/) | 2001 | Review | La Revue du Praticien | Biermer's disease (autoimmune atrophic gastritis causing B12 deficiency) |
| [26597770](https://pubmed.ncbi.nlm.nih.gov/26597770/) | 2016 | Review | Nutrition Research | Metabolic B12 deficiency as a missed opportunity to prevent dementia/stroke |
| [4213505](https://pubmed.ncbi.nlm.nih.gov/4213505/) | 1973 | Case Report | Survey of Ophthalmology | Tobacco amblyopia case linked to B12 status |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The headline TxGNN prediction (Esophageal Varices with Bleeding, 99.23%) has no clinical trial or literature support and a mechanistically implausible rationale per the model's own annotation — this does not meet even the lowest bar for further investment. The one candidate in this batch with real evidence (Vitamin Deficiency Disorder, L2/S3) is very likely a recapitulation of Hydroxocobalamin's known core indication rather than a novel repurposing opportunity, given that `original_indications` is empty in the source data. Additionally, this drug has no EU marketing authorization on record and two critical drug-level data gaps (label warnings/contraindications — Blocking; MOA — High) remain unresolved, which independently precludes any safety-stage progression.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA/EMA SmPC warnings and contraindications before any Stage 1 safety review
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to properly assess mechanistic plausibility
- Backfill `original_indications` so genuine repurposing signals can be distinguished from known-indication recapitulation (needed to correctly interpret the Vitamin Deficiency Disorder result)
- If Esophageal Varices with Bleeding is still of interest, commission dedicated preclinical/mechanistic studies, since no existing evidence base exists
- Re-evaluate whether the 8 myositis/vascular predictions (ranks 1–8, all L5/S0) reflect a systematic knowledge-graph artifact rather than independent signals, given their near-identical, unsupported rationale pattern
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

