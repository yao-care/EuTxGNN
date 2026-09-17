---
layout: default
title: Nilotinib
parent: Medium Evidence (L3-L4)
nav_order: 415
evidence_level: L4
indication_count: 10
---

# Nilotinib
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

# Nilotinib: From Chronic Myeloid Leukemia to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

> Nilotinib is a BCR-ABL/PDGFR/KIT tyrosine kinase inhibitor; this specific original-indication text is not captured in the current Evidence Pack, but the drug is publicly known to have been developed and approved for chronic myeloid leukemia (CML).
> The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
> with **no dedicated clinical trials** and **1 supporting review article** currently available for this specific drug–disease pair.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this Evidence Pack (data gap, see DG002); generally known to be Chronic Myeloid Leukemia (CML) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (data gap DG002). Based on general pharmacological knowledge, nilotinib is a second-generation tyrosine kinase inhibitor originally developed against BCR-ABL for chronic myeloid leukemia, and it also potently inhibits PDGFR-α/β and KIT — targets that are unrelated to the BCR-ABL fusion driving CML but are shared with several soft-tissue sarcomas.

Dermatofibrosarcoma protuberans is a distinct tumour type driven in most cases by the COL1A1-PDGFB fusion gene, which causes constitutive PDGFR-β activation. Because nilotinib is a PDGFR inhibitor, it is mechanistically plausible that it could suppress this driver alteration, independent of its original CML indication.

The strongest supporting argument is a class-effect precedent: imatinib, a first-generation PDGFR/BCR-ABL/KIT inhibitor closely related to nilotinib, is already an approved and guideline-recommended treatment for DFSP. This establishes that PDGFR blockade is a clinically validated strategy in this tumour, lending biological plausibility to the TxGNN prediction for nilotinib — although no dedicated nilotinib-specific trial or case series in DFSP currently exists in the Evidence Pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: a Phase 1/2 trial of nilotinib in sarcomas — NCT02587169 — exists but is registered under liposarcoma/leiomyosarcoma, not DFSP; see the drug's other predicted indications for that evidence.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors — including nilotinib — in treating PDGF-driven neoplastic disorders; supports the mechanistic rationale but provides no DFSP-specific clinical data. |

---

## EU Market Information

No EU marketing authorization data is available for nilotinib in this dataset (0 authorizations, market status: Not marketed). This should be re-verified against the current EMA register, since nilotinib is authorized in the EU under the brand name Tasigna for CML — its absence here likely reflects an incomplete data pull rather than a true market gap.

---

## Cytotoxicity

Nilotinib is an antineoplastic tyrosine kinase inhibitor (targeted therapy class), so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCR-ABL / PDGFR / KIT tyrosine kinase inhibitor), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

**Important note:** TFDA/EMA label warnings and contraindications (DG001) are flagged as a **Blocking** data gap in this Evidence Pack — the package insert has not yet been retrieved and parsed. This must be resolved before any Stage 1 (S1) safety screening can be completed. Drug interaction data was also queried with no results found (`query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (DFSP) is supported only by mechanistic class-effect reasoning and a general PDGFR-inhibitor review article (L4) — there is no clinical trial or case-level evidence for nilotinib specifically in DFSP.
- A Blocking-severity data gap exists on TFDA/EMA safety labeling, which prevents any Stage 1 safety evaluation from being completed.
- EU market authorization status is unresolved (0 licenses recorded), which needs reconciliation before regulatory pathway planning.

**To proceed, the following is needed:**
- Retrieve and parse the official nilotinib package insert (TFDA/EMA SmPC) to close DG001 and DG002
- Confirm actual EU market/authorization status (likely a data extraction gap given nilotinib's known EU approval as Tasigna)
- Seek case reports, off-label use data, or a pilot study of nilotinib specifically in DFSP, given the existing imatinib class-effect precedent
- Note: the rank-2 candidate (liposarcoma) already has stronger evidence (L2, a completed Phase 1 trial NCT02587169 and a published Phase 1 paper) and may be a more actionable next candidate to evaluate in parallel
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

