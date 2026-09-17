---
layout: default
title: Entrectinib
parent: Medium Evidence (L3-L4)
nav_order: 223
evidence_level: L4
indication_count: 10
---

# Entrectinib
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

Using the evidence pack as given (no invented data). One flag up front: `predicted_indications[0]` (multiple endocrine neoplasia) is the weakest-supported candidate in this pack — its own `repurposing_rationale` says the cited evidence doesn't actually back it. Rank 8 (female breast carcinoma, L2, Proceed with Guardrails) is far stronger. I built the report around rank 1 per the spec, and flagged the stronger candidate at the end rather than silently swapping it in.

# Entrectinib: From NTRK/ROS1-Driven Solid Tumours to Multiple Endocrine Neoplasia

## One-Sentence Summary

Entrectinib (DrugBank DB11986) has no EU marketing authorization on record in this pack, so its registered original indication cannot be confirmed here; literature evidence within this pack identifies it as a TRKA/B/C, ROS1 and ALK kinase inhibitor used in NTRK-fusion / ROS1-positive solid tumours. The TxGNN model's top prediction is **Multiple Endocrine Neoplasia (MEN)**, but the only supporting clinical trials and literature retrieved are judged **not relevant** to MEN by the pack's own relevance grading — this is a Hold, not a promising lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no EU licenses on record; literature (PMID 31862477) describes use in NTRK1/2/3- and ROS1-driven solid tumours |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is not available from DrugBank in this pack (`original_moa: [Data Gap]`). Based on literature retrieved elsewhere in this evidence pack (PMID 31862477, PMID 35695563), entrectinib is a small-molecule inhibitor of TRKA/B/C, ROS1 and ALK, developed for tumours driven by NTRK, ROS1 or ALK gene fusions/rearrangements.

Multiple Endocrine Neoplasia type 2 (MEN2) is driven predominantly by germline **RET** mutations, not by NTRK, ROS1 or ALK alterations. The single literature hit returned for this pairing (PMID 38438731) discusses acquired resistance mechanisms to *selective* RET inhibitors (selpercatinib, pralsetinib) in RET-driven medullary thyroid carcinoma — it does not evaluate entrectinib itself, and entrectinib is explicitly characterized in the rationale as having only weak/off-target RET activity. The two clinical trials returned (NCT04551495, NCT03878524) enrolled breast cancer and general precision-oncology basket populations, not MEN patients, and both are graded "C" relevance (topic mismatch).

In short, the mechanistic case for entrectinib in MEN is weak: the TxGNN score is high, but none of the retrieved real-world evidence actually supports this specific pairing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | Active, not recruiting | 65 | ROSALINE: neoadjuvant ROS1-targeted therapy + endocrine therapy in invasive lobular breast carcinoma — not a MEN study (relevance grade C) |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART-PRIME precision-oncology basket trial, terminated with only 2 enrolled; not MEN-specific (relevance grade C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical/Mechanistic | NPJ Precision Oncology | Describes resistance mechanisms to selective RET inhibitors (selpercatinib/pralsetinib) in RET-driven medullary thyroid carcinoma; does not study entrectinib in MEN |

## EU Market Information

No EU marketing authorizations found in this evidence pack (`market_status`: Not Marketed, `total_licenses`: 0).

## Cytotoxicity

Entrectinib is an antineoplastic targeted kinase inhibitor (per literature evidence in this pack, PMID 31862477: an FDA-approved small-molecule protein kinase inhibitor used in oncology), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (TRKA/B/C, ROS1, ALK tyrosine kinase inhibitor) |
| Myelosuppression Risk | Not formally characterized in this pack. A case report elsewhere in the evidence set (PMID 41002576) associates entrectinib therapy with thrombocytopenia occurring alongside pulmonary tumour thrombotic microangiopathy (PTTM), rather than classic marrow suppression |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Platelet count/CBC, pulmonary status (dyspnoea, hypoxemia), liver and renal function |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information (`key_warnings`, `contraindications`, and DDI query all returned no data in this pack).

**Literature-derived safety signal (not from the formal safety dataset, but present in this evidence pack):** a 2025 case report (PMID 41002576) describes PTTM with worsening pulmonary hypertension and thrombocytopenia occurring during entrectinib therapy for NTRK-fusion-positive colon cancer — this is an adverse-event signal, not treatment evidence, and should not be mistaken for support of the "thrombocytopenia" or "pulmonary hypertension" predictions elsewhere in this pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The MEN prediction has a high TxGNN score but no supporting clinical or mechanistic evidence — the retrieved trials and literature are off-target (breast cancer basket trials, RET-inhibitor resistance biology unrelated to entrectinib). Two Blocking/High data gaps (TFDA/EMA label warnings, confirmed MOA) also block any safety pre-assessment (S1).

**To proceed, the following is needed:**
- TFDA/EMA label data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism-of-action data via DrugBank API — currently High priority (DG002)
- If MEN2 is still of interest: dedicated RET-relevant pharmacology data for entrectinib (current evidence suggests only weak/off-target RET activity)

**Note on this evidence pack:** a separate candidate in the same pack — **female breast carcinoma** (rank 8, TxGNN score 97.76%, evidence level **L2**, recommendation **Proceed with Guardrails**) — is substantially better supported, with a Phase 2 basket trial (STARTRK-2, n=534) and a completed Phase 2 RCT (ROSALINE) targeting NTRK/ROS1-fusion-positive breast cancers. That pairing aligns with entrectinib's known mechanism and may warrant its own evaluation report rather than being folded into this one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

