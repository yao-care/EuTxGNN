---
layout: default
title: Filgotinib
parent: AI Predictions (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Filgotinib
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

# Filgotinib: From Autoimmune Disease to HER2 Positive Breast Carcinoma

## One-Sentence Summary

> Filgotinib is a selective JAK1 inhibitor known for treating autoimmune conditions such as rheumatoid arthritis and ulcerative colitis.
> The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
> but **zero clinical trials** and **zero publications** currently support this specific direction — the evidence pack itself flags this as a likely false-positive prediction driven by graph-embedding proximity rather than a real mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ulcerative colitis (autoimmune diseases) — noted in evidence rationale; no Taiwan/EU regulatory license record exists in this dataset |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.88% |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on the known information in this evidence pack, filgotinib is a selective JAK1 inhibitor that modulates cytokine signaling (e.g., IL-6, IFN pathways) and is established for autoimmune indications such as rheumatoid arthritis and ulcerative colitis.

The evidence pack's own rationale, however, explicitly cautions against this prediction: there is **no known mechanistic link** between JAK1-mediated cytokine signaling and the HER2-driven tumorigenesis pathway that characterizes HER2-positive breast carcinoma. No clinical trials and no literature exist connecting filgotinib to this indication. The high TxGNN score most likely reflects proximity in the knowledge graph's embedding space rather than a biologically grounded relationship, and should be treated as a **potential false positive** pending further evidence.

By contrast, the pack's second-ranked prediction (thrombocytopenia) at least has literature-level evidence — though notably that evidence describes filgotinib **inducing** immune-mediated thrombocytopenia as an adverse reaction, not treating it. This further underscores that top TxGNN scores alone should not be read as therapeutic support without corroborating trial or literature data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Filgotinib currently holds **no market authorization records** in this dataset (market status: Not Marketed; total authorizations: 0). No approved product information is available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: A separate case report identified in this evidence pack — PMID [41458193](https://pubmed.ncbi.nlm.nih.gov/41458193/) — describes immune-mediated thrombocytopenia occurring after filgotinib initiation in a patient with ulcerative colitis. This is an adverse-event signal unrelated to the HER2 breast carcinoma prediction above, but relevant to overall drug safety awareness.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HER2 positive breast carcinoma, TxGNN score 98.88%) has zero clinical trial or literature support, and the evidence pack's own mechanistic assessment flags it as a likely false positive with no plausible biological link to JAK1 inhibition. Combined with blocking data gaps in TFDA safety labeling and mechanism of action, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA/SmPC warnings, precautions, and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap)
- Independent preclinical or mechanistic evidence specifically linking JAK1 inhibition to HER2-driven breast carcinoma pathways
- Re-screening of lower-ranked candidates (e.g., thrombocytopenia) with caution, given existing literature points to an adverse-reaction signal rather than therapeutic benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

