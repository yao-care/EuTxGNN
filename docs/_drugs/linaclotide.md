---
layout: default
title: Linaclotide
parent: AI Predictions (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Linaclotide: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Symptomatic treatment of moderate to severe irritable bowel syndrome…"
monitor_inn: "Linaclotide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)", "autonomic nervous system disease", "familial mitral valve prolapse", "mitral valve prolapse (disease)", "MVP1", "gastroduodenitis", "large intestine disease", "rhinitis"]
---

# Linaclotide
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

## Linaclotide: From Irritable Bowel Syndrome with Constipation to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Linaclotide is a guanylate cyclase-C agonist, originally authorised in the EU for moderate to severe irritable bowel syndrome with constipation (IBS-C) in adults.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. The score is a model output only.
Among the top 10 predictions, the only signal with some biological plausibility is **large intestine disease**, which largely overlaps with the existing approved use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of moderate to severe irritable bowel syndrome with constipation (IBS-C) in adults |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, linaclotide is a guanylate cyclase-C (GC-C) agonist that acts locally in the gut lumen with minimal systemic absorption. Activating GC-C raises cGMP, which increases intestinal fluid secretion and speeds transit.

A plausible mechanistic route from this local gut action to cauda equina syndrome, a neurological compression disorder, was not identified. The high score most likely reflects shared bowel and bladder dysfunction features in the knowledge graph rather than a pharmacological link. Therefore the prediction should be regarded as unsupported.

**Other top-ranked predictions** (all Hold unless noted):

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Neurogenic bladder (obsolete term) | 99.89% | L5 | No trials or publications. Preclinical colitis-model work suggests visceral cross-sensitisation, but it does not support this as a treatment target. |
| 3 | Insomnia | 99.51% | L5 | No evidence or plausible mechanism. |
| 4 | Autonomic nervous system disease | 98.85% | L4 | Three reviews on autonomic disorders and GI dysmotility. Any relevance is indirect (treating constipation as a symptom). |
| 5–7 | Familial mitral valve prolapse, mitral valve prolapse, MVP1 | 97.84%, 97.45%, 96.90% | L5 | Likely redundant ontology nodes, with no mechanistic plausibility. |
| 8 | Gastroduodenitis | 96.51% | L4 | One IBS-C review, which concerns the existing use. No direct evidence in upper GI inflammation. |
| 9 | Large intestine disease | 95.14% | L3 | Most plausible, but it overlaps with the approved use. Research question stage. |
| 10 | Rhinitis | 94.67% | L5 | No evidence or plausible mechanism. |

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome, nor for any of the other top 10 predicted indications.

## Literature Evidence

No literature is available for cauda equina syndrome. The most relevant publications come from the ninth-ranked prediction, **large intestine disease**, and are shown below for context. They are not evidence for the primary prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41413756](https://pubmed.ncbi.nlm.nih.gov/41413756/) | 2026 | Randomised crossover clinical physiology study | Neurogastroenterol Motil | Effect of linaclotide on colonic motility assessed by high-resolution manometry in healthy subjects |
| [23958540](https://pubmed.ncbi.nlm.nih.gov/23958540/) | 2013 | Preclinical (animal) | Gastroenterology | Linaclotide inhibits colonic nociceptors and relieves abdominal pain via GC-C and extracellular cGMP |
| [30282832](https://pubmed.ncbi.nlm.nih.gov/30282832/) | 2018 | Preclinical (animal) | JCI Insight | Chronic linaclotide reduces colitis-induced neuroplasticity and reverses persistent bladder dysfunction |
| [34546338](https://pubmed.ncbi.nlm.nih.gov/34546338/) | 2021 | Preclinical (animal) | J Exp Med | Activating GUCY2C mutation in mice: excess gut cGMP drives colitis and dysbiosis (possible safety signal) |
| [23464519](https://pubmed.ncbi.nlm.nih.gov/23464519/) | 2013 | Review | Future Med Chem | Overview of linaclotide's development and approval for IBS-C and chronic idiopathic constipation |
| [31724881](https://pubmed.ncbi.nlm.nih.gov/31724881/) | 2020 | Review | Expert Opin Pharmacother | Pharmacological management of IBS-C (rank 8, gastroduodenitis) |
| [41404536](https://pubmed.ncbi.nlm.nih.gov/41404536/) | 2025 | Review | Curr Treat Options Neurol | Update on treatment of autonomic disorders (rank 4) |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002490 | Constella (status: cancelled) | Not specified | Symptomatic treatment of moderate to severe irritable-bowel syndrome with constipation (IBS-C) in adults. |

## Safety Considerations

Safety information from the product label was not available in the data compiled for this report. Please refer to the SmPC for warnings and contraindications.

**Drug Interactions:** 56 interactions were recorded. The 20 shown in the data include:
- **Moderate:** levonorgestrel, ethinylestradiol, norethisterone, levothyroxine, porcine thyroid
- **Minor:** proton pump inhibitors (rabeprazole, esomeprazole, dexlansoprazole), NSAIDs (ketorolac, ibuprofen, diclofenac, oxaprozin, bromfenac), and other laxatives (bisacodyl, sodium picosulfate, docusate, polyethylene glycol, castor oil, cascara)

**Theoretical consideration:** A mouse model with excess GC-C/cGMP signalling showed colitis and dysbiosis (PMID 34546338). This raises a possible concern in inflammatory bowel settings, which would need clarification before any expansion of use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, cauda equina syndrome, has no trials or publications and no plausible pharmacological mechanism. The score reflects model association only. The EU authorisation has been cancelled. The only biologically plausible signal, large intestine disease, largely overlaps with the already-approved IBS-C use and is not a clearly new indication.

**To proceed, the following is needed:**
- Label safety data (warnings and contraindications) from the SmPC
- Mechanism of action data confirmed from DrugBank
- A defined, non-redundant new indication, such as a specific colonic or visceral pain/hypersensitivity condition, with supporting clinical data
- Clarification of why the EU authorisation was cancelled (commercial or safety reasons)
- Review of the colitis/cGMP safety signal before any use in inflammatory conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

