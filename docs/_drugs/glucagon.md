---
layout: default
title: Glucagon
parent: AI Predictions (L5)
nav_order: 288
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Glucagon"
predicted_indications: ["irritable bowel syndrome"]
description: "Glucagon: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Ogluo is indicated for the treatment of severe hypoglycaemia in adult…"
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Glucagon: Irritable bowel syndrome
{: .text-alpha }

## One-Sentence Summary

Glucagon is a peptide hormone used to treat severe hypoglycaemia in people with diabetes. The TxGNN model predicts it may be useful for **irritable bowel syndrome**, but no study has tested glucagon itself in this condition. The related evidence (**2 early-phase trials** and several publications) concerns GLP-1 and GLP-1 receptor agonists, which are different drugs, so the evidence level is **L5**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ogluo is indicated for the treatment of severe hypoglycaemia in adults, adolescents, and children aged 2 years and over with diabetes mellitus.; Baqsimi is indicated for the treatment of severe hypoglycaemia in adults, adolescents, and children aged 4 years and over with diabetes mellitus. |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for glucagon: "Glucagon increases blood glucose concentration by activating hepatic glucagon receptors, thereby stimulating glycogen breakdown and release of glucose from the liver. Hepatic stores of glycogen are necessary for glucagon to produce an antihypoglycemic effect." ([DailyMed: glucagon prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e4be1c0e-0fe6-45a0-9229-5cde98434b84), label version 2020-09-16; accessed 2026-11-19.) Glucagon is a known short-acting relaxant of gastrointestinal smooth muscle, which is mechanistically plausible for spasm-related symptoms in irritable bowel syndrome.

Peptides of the glucagon/GLP-1 family also slow gastrointestinal motility and may influence visceral sensation through the gut-brain axis. However, the studies behind this idea used GLP-1 or the GLP-1 analogue ROSE-010, not glucagon. The link to glucagon is therefore indirect, and no trial in the compiled data evaluates glucagon for irritable bowel syndrome.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analogue, not glucagon) on gastrointestinal motor function in women with constipation-predominant IBS |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 versus ROSE-010 on meal-related stomach, duodenal and jejunal motility; a physiology study, not an IBS efficacy trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review | Frontiers in Endocrinology | GLP-1 receptor agonists and IBS; GLP-1 and ROSE-010 reduce gastrointestinal motility in IBS patients |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | The Journal of Headache and Pain | Role of GLP-1 receptor agonists in headache and pain disorders |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Possible role of GLP-1 in the pathophysiology of IBS |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Exploratory substudy | Scandinavian Journal of Gastroenterology | Pain relief with the GLP-1 agonist ROSE-010 in IBS, analysed by patient characteristics |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Advances in Experimental Medicine and Biology | Aerosolised GLP-1 for diabetes and IBS |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Annals of Gastroenterology | Prescription and discontinuation patterns of GLP-1 receptor agonists in IBS patients |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cellular and Molecular Gastroenterology and Hepatology | Brain-gut-microbiome axis |

None of these publications studies glucagon in irritable bowel syndrome.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/003848 | Baqsimi | Glucagon | Valid |
| EMEA/H/C/005391 | Ogluo | Glucagon | Valid |

<!-- licenses:end -->

Both authorizations are valid.

## Safety Considerations

- **Drug Interactions**: 25 interactions are recorded, all graded Minor. They include warfarin and a range of beta-blockers (for example atenolol, bisoprolol, carvedilol, metoprolol, propranolol and timolol, including ophthalmic forms).

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests glucagon in irritable bowel syndrome. The supporting trials and publications concern GLP-1 and its analogue ROSE-010, so the evidence level is L5 and the high TxGNN score (0.9924) rests on indirect, mechanism-based reasoning.

**To proceed, the following is needed:**
- Preclinical or early clinical data on glucagon itself in irritable bowel syndrome, for example on symptom relief or motility
- Mechanism of action data for glucagon
- Review of the SmPC warnings and contraindications
- Assessment of whether the available routes of administration suit a gastrointestinal indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: glucagon prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e4be1c0e-0fe6-45a0-9229-5cde98434b84) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

