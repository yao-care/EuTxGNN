---
layout: default
title: Ponatinib
parent: AI Predictions (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
---

# Ponatinib
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

# Ponatinib: From Unspecified Original Indication to Gingival Fibromatosis

## One-Sentence Summary

Ponatinib (DrugBank ID DB08901) has no original indication or mechanism-of-action data on file in this evidence pack. The TxGNN model's top-ranked prediction proposes potential effectiveness for **Gingival Fibromatosis**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure AI embedding-similarity output with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indications or market licenses on file (data gap) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ponatinib is not available in this evidence pack (flagged as a High-severity data gap). However, literature attached to other candidate indications in this same pack (not to gingival fibromatosis specifically) consistently describes Ponatinib as a third-generation, multi-target tyrosine kinase inhibitor acting on BCR-ABL, FGFR, PDGFR, SRC, KIT, and RET, historically used in hematologic malignancies (e.g., PMID 37399979, PMID 36927623).

For the top-ranked prediction itself — Gingival Fibromatosis — the evidence pack's own rationale is explicit: there is **no known kinase-driven mechanism** connecting Ponatinib's target profile to this disease. The prediction is described as "purely a TxGNN embedding similarity output, with no literature or trial support" (`repurposing_rationale.mechanistic_link`). In other words, the model surfaced a statistical association in the knowledge graph, not a biologically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

No marketing authorizations on file — the drug is recorded as not currently marketed in this jurisdiction (0 licenses).

## Cytotoxicity

*(Ponatinib is included here as an antineoplastic based on class-level context found elsewhere in the evidence pack — literature describes it as a tyrosine kinase inhibitor used in leukemia treatment — though drug-level DrugBank categories and toxicity data are not available in this pack.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: BCR-ABL/FGFR/PDGFR/SRC/KIT/RET) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Based on toxicity signals reported in pack literature for this drug class: cardiovascular monitoring (blood pressure, ECG), pulmonary symptoms, renal function, CBC — final list per SmPC |
| Handling Protection | Oral hazardous/antineoplastic drug handling precautions recommended pending SmPC confirmation |

## Safety Considerations

Please refer to the SmPC for safety information. *(All key warnings, contraindications, and DDI fields in this evidence pack are unfilled; the missing TFDA/regulatory label data is flagged as a Blocking gap.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gingival Fibromatosis) has no supporting clinical trials or literature, and the evidence pack itself states there is no known mechanistic link — this is a pure model-score artifact. Combined with a Blocking gap on safety labeling data, this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- TFDA/regulatory safety labeling (warnings, contraindications) — Blocking gap
- Detailed mechanism-of-action data from DrugBank — High-priority gap
- Any preclinical or mechanistic rationale specifically linking Ponatinib to gingival fibromatosis, if it exists
- Re-evaluate other candidates within this same pack that carry stronger evidence (see below)

---

### Note: Other Predictions in This Evidence Pack

This pack contains 10 ranked predictions for Ponatinib. The top-scored one (above) has no evidence, but two lower-ranked, lower-score predictions show materially stronger support and may warrant separate evaluation:

| Rank | Disease | Score | Evidence Level | Recommendation |
|------|---------|-------|-----------------|-----------------|
| 2 | Liposarcoma | 99.00% | L4 | Research Question |
| 9 | Lung benign neoplasm | 98.83% | L3 | Research Question |

Both are supported by literature suggesting FGFR/PDGFR/SRC pathway relevance (e.g., kinase screening in liposarcoma cell lines; FGFR1 mRNA/copy-number-based patient preselection for Ponatinib in lung tumors), unlike the zero-evidence gingival fibromatosis prediction. If a "Go" pathway is sought within this candidate set, ranks 2 and 9 are the more defensible starting points.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

