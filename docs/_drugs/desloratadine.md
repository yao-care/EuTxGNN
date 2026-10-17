---
layout: default
title: Desloratadine
parent: AI Predictions (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Desloratadine: predicted new indication Cold urticaria (evidence level L5). Approved use: Relief of symptoms of allergic rhinitis and urticaria"
monitor_inn: "Desloratadine"
predicted_indications: ["cold urticaria", "nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis", "headache disorder", "trigeminal autonomic cephalalgia", "punctate epithelial keratoconjunctivitis"]
---

# Desloratadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Desloratadine: From Allergic Rhinitis and Urticaria to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation antihistamine, originally used to relieve symptoms of allergic rhinitis and urticaria.
The TxGNN model predicts it may be effective for **cold urticaria**,
with **2 clinical trials** and **6 publications** currently supporting this direction (3 of them randomized or placebo-controlled studies of desloratadine in cold urticaria).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relief of symptoms of allergic rhinitis and urticaria |
| Predicted New Indication | Cold urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (see note in the evidence section) |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 7 (all cancelled) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Desloratadine is a selective peripheral H1-receptor inverse agonist. The formal mechanism-of-action field was not available in the data compiled for this report, so this description reflects general pharmacological knowledge about the drug class.

Cold urticaria is a physical urticaria in which mast cells release histamine after cold exposure. H1 blockade directly reduces wheals and raises the cold provocation threshold. This is the same mechanism behind desloratadine's approved use in urticaria, so the new indication is a close extension of the original one.

Raising the dose above the standard 5 mg (up to 20 mg) is an established strategy in guideline-based management of cold urticaria. Dose-escalation studies of desloratadine have been run in this very condition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-center, double-blind dose-escalation study (5, 10 and 20 mg) to find the desloratadine dose sufficient to inhibit symptoms of acquired cold urticaria |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study comparing 5 mg vs. 20 mg desloratadine and placebo on experimentally induced cold urticaria lesions |

**Note on the evidence level:** Both trials are Phase 4 rather than Phase 3, and both are small. Under a strict reading of the grading rules, this does not meet the Phase 3 criterion for L1. The L1 grade rests on the randomized, controlled design of the trials and the consistent supporting randomized literature. Readers should treat it as moderate-to-strong rather than definitive evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomized, placebo-controlled crossover study: high-dose desloratadine decreased wheal volume and improved cold provocation thresholds compared with standard dose in acquired cold urticaria |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomized trial of H1-antihistamine dose escalation using critical temperature threshold measurement in cold urticaria |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatol Treat | 5 mg desloratadine for 4 days, tested with ice cubes before and after treatment in 12 patients with cold urticaria |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of the causes, management and current and future treatment options for chronic urticaria |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of ebastine (a different antihistamine) in allergic rhinitis and chronic idiopathic urticaria; indirect context only |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | Cold-induced urticaria after black ant bite anaphylaxis; background on the condition, not evidence for desloratadine |

## EU Market Information

All seven EU authorizations for desloratadine are cancelled. There is currently no valid single-ingredient or combination authorization.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002404 | Desloratadine ratiopharm | Not specified | Adults: relief of symptoms of allergic rhinitis and chronic idiopathic urticaria as initially diagnosed by a physician |
| EMEA/H/C/000313 | Aerius | Not specified | Relief of symptoms of allergic rhinitis; urticaria |
| EMEA/H/C/002435 | Desloratadine Actavis | Not specified | Treatment of allergic rhinitis and urticaria |
| EMEA/H/C/000314 | Neoclarityn | Not specified | Relief of symptoms of allergic rhinitis; urticaria |
| EMEA/H/C/002419 | Desloratadine Teva | Not specified | Relief of symptoms of allergic rhinitis; urticaria |

## Safety Considerations

- **Disease-drug contraindication signals (knowledge graph, not label text):** The TxGNN knowledge graph links desloratadine to contraindications in the following conditions: hypertension, kidney disease, liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, angle-closure glaucoma, and hyperthyroidism (including Graves disease and thyrotoxicosis). These come from the graph and should be verified against the official product information.
- **Drug interactions:** The interaction screen returned 100 potential interacting drugs, but none has a severity grade. Examples include calcitriol, phentermine, pantoprazole, doxycycline, morphine, metformin, omeprazole, cimetidine, simvastatin, epinephrine and prednisone. Their clinical relevance cannot be judged from the available data.
- **Dose-escalation consideration:** The supporting cold urticaria studies use doses up to 20 mg, which is four times the standard 5 mg dose. Safety at these doses needs specific review.

Official warnings and contraindications from the EU product information were not available. Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed randomized, controlled Phase 4 trials and several randomized publications directly test desloratadine in cold urticaria, and the mechanism is the same as in its approved urticaria use. The trials are small, and no Phase 3 trial exists. No EU authorization is currently valid.

**To proceed, the following is needed:**
- Official EU product information (warnings and contraindications), to complete the safety review
- Formal mechanism-of-action data from a curated source
- Safety review of high-dose use (up to 20 mg), including cardiac, hepatic and renal considerations
- Review of the relevant interacting drugs and the knowledge-graph contraindicated conditions
- Clarification of the regulatory pathway, since all current EU authorizations are cancelled
- Larger confirmatory trial, ideally Phase 3, if a formal label extension is intended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

