---
layout: default
title: Ripretinib
parent: AI Predictions (L5)
nav_order: 508
evidence_level: L5
indication_count: 10
---

# Ripretinib
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

# Ripretinib: From Gastrointestinal Stromal Tumor to Multiple Endocrine Neoplasia

## One-Sentence Summary

Ripretinib is a KIT/PDGFRA switch-control kinase inhibitor used as a fourth-line treatment for gastrointestinal stromal tumor (GIST). The TxGNN model's top prediction — **Multiple Endocrine Neoplasia (MEN)** — scores highly (98.84%), but is supported by **zero clinical trials** and **zero publications**, and the evidence pack itself flags the mechanistic rationale as likely a knowledge-graph false positive, since MEN is driven by RET/MEN1 mutations with no known link to the KIT/PDGFRA pathway.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastrointestinal Stromal Tumor (GIST), 4th-line — inferred from mechanistic rationale text; no structured EU authorization data available |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (flagged as a High-severity data gap). Based on known pharmacology referenced in the evidence pack's rationale, ripretinib is a switch-control tyrosine kinase inhibitor targeting KIT and PDGFRA, approved as a fourth-line therapy for GIST.

The top-ranked prediction, multiple endocrine neoplasia, is driven by RET mutations (MEN2) or MEN1 gene loss, neither of which has an established mechanistic connection to KIT/PDGFRA signaling. The evidence pack's own repurposing rationale explicitly states this link is "weak" and "may be a knowledge-graph embedding false positive" — there is no supporting clinical or preclinical evidence.

This skepticism extends across the full set of 10 predicted indications reviewed: HER2-positive and hormone-receptor-defined breast cancer subtypes (driven by ERBB2/ER/PR pathways, unrelated to KIT/PDGFRA), two veterinary bovine viral diseases (infectious bovine rhinotracheitis, malignant catarrh — flagged as species-mismatch noise from a model trained partly on non-human data), cytomegalovirus infection (no antiviral mechanism), and amenorrhea (no established mechanistic link). Notably, the 19 literature records retrieved for "breast tumor luminal A or B" are B-cell immunology and Hepatitis B vaccine papers — a keyword-matching artifact on the letter "B," not genuine evidence. None of the 10 candidates in this pack currently clear even preliminary mechanistic plausibility screening.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (Multiple Endocrine Neoplasia).

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication (Multiple Endocrine Neoplasia).

## EU Market Information

Ripretinib currently holds **no EU marketing authorizations** (0 licenses on file; market status: Not marketed).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (KIT/PDGFRA switch-control tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — TFDA/EMA label data collection is a blocking gap in this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this pack are Evidence Level L5 (AI prediction only, no clinical or trial support), and the top-ranked candidate (MEN) is explicitly flagged within the evidence pack as a likely mechanistic false positive with no known pathway overlap. The drug also has no EU marketing authorization and no confirmed structured MOA/safety data, so it cannot advance past S0.

**To proceed, the following is needed:**
- Regulatory label data (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed structured mechanism of action data (DG002)
- Independent literature/trial search specifically for MEN, RET, or MEN1 to test (or refute) the mechanistic hypothesis before any further screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

