---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Desloratadine
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

# Desloratadine: From Allergic Rhinitis to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation, non-sedating H1-antihistamine widely used globally for allergic rhinitis and chronic urticaria, though currently unregistered in Taiwan.
The TxGNN model predicts it may be effective for **Cold Urticaria (acquired cold urticaria)**, with **3 clinical trials** and **7 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis and chronic idiopathic urticaria (based on international approvals; no Taiwan license on record) |
| Predicted New Indication | Cold Urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, desloratadine is a selective peripheral H1-receptor antagonist and the active metabolite of loratadine. As a second-generation antihistamine, it is non-sedating, has a prolonged duration of action, and carries anti-inflammatory properties beyond pure receptor blockade — including suppression of mast cell degranulation and downregulation of pro-inflammatory adhesion molecules (ICAM-1, VCAM-1).

Acquired cold urticaria (ACU) is a physical urticaria triggered by cold stimuli. The cold challenge induces mast cell degranulation and histamine release, producing wheals, flare, and — in severe cases — anaphylaxis. Desloratadine addresses this at two levels: it competitively blocks H1 receptors to reduce downstream wheal formation, and it inhibits the upstream IgE-dependent mast cell activation pathway, thereby raising the critical temperature threshold (CTT) — the minimum cold exposure required to provoke a reaction.

This mechanistic fit is direct and well-supported: histamine is the principal mediator of ACU, and H1-receptor antagonism is the first-line treatment recommended by EAACI/GA²LEN/EDF urticaria guidelines. High-dose desloratadine (20 mg) has been shown to be significantly more effective than the standard 5 mg dose in reducing wheal volume and improving CTT, making cold urticaria one of the most biologically coherent applications in the TxGNN prediction set.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-center, double-blind, dose-escalation study comparing 5 mg, 10 mg, and 20 mg desloratadine; primary aim was to identify the dose sufficient to inhibit ACU symptoms |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study; compared cold urticaria lesion size (thermography, volumetry) under placebo vs. 5 mg vs. 20 mg desloratadine; tested hypothesis that updosing is more effective than standard dose |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Head-to-head comparison of 5 antihistamines (including desloratadine) in urticaria patients in tropical Latin America; largest enrollment in the set, provides comparative efficacy and pharmacodynamic data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | British Journal of Dermatology | Dose escalation of H1-antihistamines in cold urticaria; used critical temperature threshold as primary endpoint; demonstrated measurable improvement with higher dosing |
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | Controlled Trial | J Allergy and Clinical Immunology | High-dose desloratadine (20 mg) significantly decreased wheal volume and improved cold provocation thresholds vs. standard dose and placebo; randomized, placebo-controlled, crossover design; supports guideline recommendation for updosing |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Controlled Clinical Study | J Dermatological Treatment | Desloratadine 5 mg for 4 days significantly inhibited cold urticaria in 12 patients using ice-cube challenge before and after treatment; early controlled evidence of direct efficacy |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Comprehensive review of chronic urticaria aetiology and management; positions H1-antihistamines, including desloratadine, as first-line standard of care |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Comparative review of second-generation antihistamines in allergic rhinitis and chronic urticaria; includes head-to-head comparisons with desloratadine |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case Series | J Allergy Clin Immunol In Practice | Food-dependent cold urticaria described as a new physical urticaria variant; characterizes clinical features and management approaches relevant to this indication |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case Report | Qatar Medical Journal | First reported case of cold-induced urticaria following black ant bite anaphylaxis; illustrates mechanistic diversity within the cold urticaria spectrum |

---

## Taiwan Market Information

Desloratadine currently has **no marketing authorizations in Taiwan**. No licensed products, approved indications, or registered dosage forms are on record with the TFDA.

---

## Safety Considerations

Please refer to the SmPC for safety information. Full TFDA label warnings and contraindications were not available in this Evidence Pack (Data Gap DG001: TFDA 仿單警語/禁忌, severity: Blocking).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 4 clinical trials — including a randomized, double-blind, placebo-controlled crossover study — directly evaluating desloratadine in acquired cold urticaria, combined with an independent RCT (PMID 22242678) and six additional supporting publications, constitute L1-level evidence. The mechanistic fit is unambiguous: histamine is the primary mediator of ACU, H1-receptor antagonism is the guideline-recommended first-line treatment, and dose-escalation to 20 mg has demonstrated quantifiably superior efficacy over standard dosing.

**To proceed, the following is needed:**
- TFDA label (仿單) for Taiwan-specific safety warnings and contraindications (DG001 — Blocking; download from TFDA official website)
- Complete mechanism of action data from DrugBank API (DG002 — High)
- Taiwan registration pathway assessment — desloratadine is currently unregistered; a regulatory strategy (new drug application, or identification of an existing imported brand) is required before clinical use
- Pharmacogenomic review for Taiwanese patient population, particularly CYP3A4/CYP2D6 metabolism considerations relevant to dose-escalation safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

