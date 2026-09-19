---
layout: default
title: Glucagon
parent: Medium Evidence (L3-L4)
nav_order: 280
evidence_level: L4
indication_count: 10
---

# Glucagon
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Glucagon: From Unknown/Not Marketed Indication to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon currently has **not obtained marketing authorization in the EU** (0 approvals); this evidence package also does not provide its original indication text and mechanism of action data. The TxGNN model lists **Irritable Bowel Syndrome (IBS)** as the top predicted indication with a score of **99.24%**, and **11 clinical trials** and **20 literature articles** were retrieved; however, upon careful review, the vast majority of these findings actually study **GLP-1 (glucagon-like peptide-1) receptor agonists** rather than glucagon itself, posing a clear risk of drug name/entity confusion.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Data gap — this product is not marketed in the EU; the evidence package does not provide approved indication text (see DG001) |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, this product's mechanism of action (MOA) data is missing (DG002, classified as High severity, Limits mechanistic-link analysis), and because this product is not marketed in the EU, the evidence package also lacks approved indication text for comparison (DG001, classified as Blocking severity, which consequently prevents the safety initial assessment S1 from being completed). Therefore, routine mechanistic comparison between "original indication" and "predicted new indication" cannot be performed.

It must be particularly noted that among the 11 clinical trials and 20 literature articles retrieved, evidence is heavily concentrated on studies of **GLP-1 receptor agonists** (such as ROSE-010, exendin-4) and their derivative drugs (dulaglutide, liraglutide, semaglutide, tirzepatide) in IBS motility disorders and pain relief, rather than glucagon itself. This represents a typical entity confusion caused by name similarity between "glucagon" and "glucagon-like peptide-1 (GLP-1)," potentially causing the knowledge graph to generate noisy pairings.

It is clinically known that glucagon has the effect of inducing relaxation of intestinal smooth muscle (commonly used for smooth muscle relaxation before endoscopy/barium imaging), which theoretically relates to IBS-associated intestinal motility disorders; however, in the currently retrieved evidence, **there is almost no data directly studying glucagon itself for IBS use**. Thus, this association currently remains at the hypothesis level rather than an evidence-supported mechanistic pathway.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | NA | Completed | 12 | Study of idiopathic reactive hypoglycemia prevalence and fructooligosaccharide supplementation; no glucagon drug intervention, low relevance (grade C) |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | NA | Completed | 37 | Study of butyrate mechanism of action in human colon; not related to glucagon (grade C) |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | NA | Completed | 33 | Gut microbiota nutritional intervention study investigating intestinal barrier integrity under high altitude exposure; no glucagon component (grade C) |
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | Evaluation of ROSE-010 (synthetic GLP-1 analog, not glucagon) on gastrointestinal motility in patients with constipation-predominant IBS (grade C, drug identity mismatch) |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | Completed | 66 | Comparison of two exercise intensities on gut dysbiosis and GLP-1 hormone in IBS patients |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Study of natural GLP-1 (not glucagon) on postprandial gastroduodenal jejunal motility inhibition (grade C) |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | Establishment of small intestinal organoid model to evaluate effects of nutritional antigens or therapeutic agents |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | NA | Completed | 33 | Study of whole grain rye bread on gut-brain axis microbiota modulation |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | NA | Unknown | 110 | Comparison of low-calorie diet combined with behavioral therapy vs. combined with gastric balloon on efficacy in obese adults |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | NA | Completed | 41 | Study of eating speed of ultra-processed food on dietary intake behavior and metabolic response |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scandinavian Journal of Gastroenterology | Cross-sectional analysis of GLP-1 receptor agonist ROSE-010 on IBS pain relief (not glucagon) |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Review | Frontiers in Endocrinology | Systematic review and meta-analysis of GLP-1 receptor agonists for IBS improvement |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Therapeutic Advances in Gastroenterology | Review of current IBS treatment status (therapies beyond fiber and antispasmodic agents) |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opinion on Investigational Drugs | Review of newly developed drugs for constipation-predominant IBS |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Preclinical/Early | Advances in Experimental Medicine and Biology | Early research of inhaled GLP-1 in diabetes and IBS treatment |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | The endocrine regulatory role of GLP-1 in IBS pathophysiology |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Animal Study | Neurogastroenterology and Motility | GLP-1 agonist exendin-4 improves gastrointestinal dysfunction in IBS rat model |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Observational Study | Clinics and Research in Hepatology and Gastroenterology | Correlation of decreased serum GLP-1 concentration and abdominal pain in patients with constipation-predominant IBS |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Observational Study | Frontiers in Nutrition | Effects of low-FODMAP diet on circulating GLP-1 concentration in IBS patients |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Real-World Study | Annals of Gastroenterology | Prescription and discontinuation patterns of GLP-1 receptor agonists in IBS patients |

> Note: The main body of all the above literature revolves around **GLP-1 receptor agonists**, not direct efficacy evidence of glucagon itself.

## EU Market Information

Currently, this product has not obtained any marketing authorization in the EU (0 approval records) and cannot list authorization information.

## Safety Considerations

Please refer to the SmPC for safety information.

(DDI query yielded no results; warning and contraindication data are all gaps, corresponding to DG001 — classified as Blocking severity, requiring first obtaining TFDA/EU SmPC prescribing information before safety initial assessment can be performed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This product is not marketed in the EU with no safety labeling data (DG001, Blocking), and mechanism of action is unknown (DG002). Although the TxGNN score for IBS reaches 99.24% and evidence level reaches L4, the vast majority of study subjects in the supporting evidence are actually GLP-1 receptor agonists rather than glucagon itself, posing a high risk of drug entity confusion. The remaining 9 predicted indications (cauda equina syndrome, neurogenic bladder, etc.) are all L5, with no clinical or literature support, or pointing in the opposite direction (such as pharyngitis, filariasis being reverse evidence of drug side effects/disease-influenced hormones). The overall quality of evidence is insufficient to support proceeding.

**To proceed, the following is needed:**
- Obtain TFDA/EU SmPC prescribing information warnings and contraindications (DG001)
- Complete DrugBank mechanism of action data (DG002)
- Confirm whether the glucagon node in the knowledge graph has entity confusion or incorrect merging with the GLP-1 (glucagon-like peptide-1) node
- Re-execute IBS-specific clinical trial and literature search for glucagon (not GLP-1 analogs) itself
- If proceeding further, supplementary route compatibility and dosage form compatibility data are needed (currently pending)

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

