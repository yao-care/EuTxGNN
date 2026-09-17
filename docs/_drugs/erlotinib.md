---
layout: default
title: Erlotinib
parent: Medium Evidence (L3-L4)
nav_order: 232
evidence_level: L4
indication_count: 10
---

# Erlotinib
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

# Erlotinib: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

> Erlotinib is an EGFR (HER1) tyrosine kinase inhibitor most widely known as an anticancer agent (per attached literature, e.g. PMID 32164971).
> The TxGNN model predicts it may be effective for **Ewing Sarcoma**,
> currently supported by **1 clinical trial** (withdrawn, 0 enrolled) and **2 publications**, with no completed trial data confirming efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No regulatory record available in this evidence pack (`taiwan_regulatory.licenses` empty; general anticancer/NSCLC use noted only in cross-referenced literature, not sourced from regulatory data) |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 95.77% |
| Evidence Level | L4 |
| EU Market Status | Not Marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question (Decision Stage S1) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002, severity High). Based on information embedded in the evidence pack's rationale and cross-referenced literature, Erlotinib is an EGFR (HER1) tyrosine kinase inhibitor (EGFR-TKI) whose known anticancer activity operates by blocking EGFR-driven proliferation signaling.

The system's own repurposing rationale for this prediction states: some Ewing sarcoma tumors express EGFR/HER3, so an EGFR-TKI could theoretically show activity. However, Ewing sarcoma is primarily driven by the EWSR1-FLI1 fusion oncoprotein rather than EGFR signaling, making this mechanistic link indirect and relatively weak rather than a primary driver-pathway match.

Consistent with this weak/indirect link, the only related clinical trial identified (NCT02689336) was a genomically-targeted pediatric basket trial requiring an EGFR/ERBB2/JAK2 mutation for eligibility — it was withdrawn with zero enrollment, so no actual efficacy or safety signal exists yet. The supporting literature is likewise general (pediatric oncology review; a xenograft evaluation of a related EGFR/HER3-targeting combination), not Ewing-sarcoma-specific clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02689336](https://clinicaltrials.gov/study/NCT02689336) | Phase 2 | Withdrawn | 0 | Genomically-targeted pediatric basket trial combining erlotinib + temozolomide for relapsed/refractory solid tumors with EGFR/ERBB2/JAK2V617F mutations; withdrawn before enrollment, no outcome data generated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29080385](https://pubmed.ncbi.nlm.nih.gov/29080385/) | 2018 | Cohort/Trial evaluation | Pediatric blood & cancer | Evaluated patritumab (anti-HER3) with/without erlotinib combined with standard cytotoxics (cisplatin, vincristine, cyclophosphamide) in pediatric sarcoma xenograft models expressing EGFR/HER3. |
| [26835334](https://pubmed.ncbi.nlm.nih.gov/26835334/) | 2014 | Review | Translational pediatrics | General review of advances in pediatric cancer treatment; discusses risk-adapted therapy approaches, not Ewing-sarcoma/erlotinib-specific data. |

---

## EU Market Information

Currently no EU marketing authorization records available (`market_status`: Not marketed / Not Marketed; `total_licenses`: 0).

---

## Cytotoxicity

Erlotinib is classified here as antineoplastic based on its EGFR-TKI mechanism referenced in the repurposing rationale and cross-referenced literature (all predicted indications in this pack are oncology-related).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR-TKI), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps in this evidence pack — DG001, severity Blocking.)

---

## Conclusion and Next Steps

**Decision: Research Question (Decision Stage S1)**

**Rationale:**
- Evidence level is L4 (mechanistic/preclinical only) — the sole related trial (NCT02689336) was withdrawn with zero enrollment, and the mechanistic link (EGFR/HER3 expression in a subset of Ewing sarcoma) is indirect since EWSR1-FLI1 fusion, not EGFR, is the primary disease driver.

**To proceed, the following is needed:**
- TFDA/SmPC full prescribing information (warnings, contraindications, DDI) — currently blocking (DG001), required before any S1 safety pre-assessment can proceed
- Complete mechanism of action (MOA) documentation (DG002)
- A newly enrolled, non-withdrawn clinical trial or biomarker-selected cohort in EGFR/HER3-expressing Ewing sarcoma to generate actual efficacy/safety signal
- EU/Taiwan regulatory and market status confirmation, since no licenses are currently on record for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

