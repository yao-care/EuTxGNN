---
layout: default
title: Prucalopride
parent: AI Predictions (L5)
nav_order: 502
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prucalopride: predicted new indication Hypoalphalipoproteinemia (evidence level L5). Approved use: Symptomatic treatment of chronic constipation in adults in whom laxat…"
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Prucalopride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Prucalopride: From Chronic Constipation to Hypoalphalipoproteinemia

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist (a gastrointestinal prokinetic), originally used for the symptomatic treatment of chronic constipation in adults whom laxatives fail to relieve.
The TxGNN model predicts it may be effective for **hypoalphalipoproteinemia** (low HDL cholesterol), but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of chronic constipation in adults in whom laxatives fail to provide adequate relief |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the data compiled for this report. Based on general pharmacology, prucalopride is a selective 5-HT4 receptor agonist that enhances gastrointestinal motility, and its efficacy in chronic constipation is established.

For the top-ranked prediction, hypoalphalipoproteinemia, no plausible mechanistic link could be identified. HDL metabolism and lipoprotein regulation have no known connection to 5-HT4 agonism, so the high score looks like an artifact of the knowledge-graph prediction rather than a pharmacological signal. The other top predictions are similarly weak:

- **Lipid disorders** (homozygous familial hypercholesterolemia, familial combined hyperlipidemia): no mechanistic rationale. The first stems from LDL receptor pathway defects, and the second is an obsolete ontology term.
- **Infections** (oral candidiasis, strongyloidiasis, HIV): prucalopride has no antifungal, antiparasitic or antiviral action.
- **Duodenal ulcer**: only a speculative link through upper GI motility. Ulcers are driven by acid and *H. pylori*, and prokinetics are not an established therapy.
- **Amyloidosis-related conditions** (amyloidosis, primary amyloidosis, acquired amyloid peripheral neuropathy): the only indirectly plausible group. Amyloidosis can cause GI dysmotility such as chronic intestinal pseudo-obstruction, where a prokinetic might relieve symptoms. This would be symptom management, not treatment of the amyloid disease itself.

## Clinical Trial Evidence

Currently no related clinical trials registered for hypoalphalipoproteinemia, nor for any of the other top-10 predicted indications.

## Literature Evidence

Currently no related literature available for hypoalphalipoproteinemia.

For context, literature was found only for the amyloidosis-related predictions (ranks 6 and 9). It does not demonstrate prucalopride efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case report | Cureus | A 61-year-old man with amyloidosis presenting as chronic intestinal pseudo-obstruction after repeated hospitalizations and laparotomies without a diagnosis |
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Cohort | Turk J Gastroenterol | Specific GI motility disorders (gastroparesis, pseudo-obstruction, colonic inertia) are often misdiagnosed as functional GI disorders by community physicians |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001012 (cancelled) | Resolor | Not specified | Resolor is indicated for symptomatic treatment of chronic constipation in adults in whom laxatives fail to provide adequate relief. |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not label text): ulcerative colitis, inflammatory bowel disease, intestinal perforation.
- **Drug Interactions**: 98 interactions were recorded. Those listed below are from the first 20 reviewed, with no Major-level interactions among them.
  - Moderate: anticholinergic or antimuscarinic agents (aclidinium, atropine, benzatropine, biperiden, clidinium, glycopyrronium, hyoscyamine), which oppose the prokinetic effect, and hormonal contraceptives (levonorgestrel, norethisterone, ethinylestradiol).
  - Minor: nifedipine, afatinib, alpelisib, amiodarone, cobicistat, captopril, diltiazem, spironolactone, carvedilol, conivaptan.

Please refer to the SmPC for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hypoalphalipoproteinemia, has no clinical trials, no literature and no plausible mechanistic link (Evidence Level L5). The high TxGNN score is likely a graph-based artifact. In addition, the EU authorization for Resolor is currently cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) from DrugBank
- Label warnings and contraindications from the SmPC, which are required for safety screening
- Confirmation of the current EU regulatory status of prucalopride products
- If a lead is wanted, the amyloidosis-related GI dysmotility indications (Evidence Level L4) are the more credible research question. They would need to be framed as symptom management and supported by targeted studies of prucalopride in that setting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

