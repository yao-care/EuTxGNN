---
noindex: true
sitemap: false
layout: default
title: Amlodipine As Amlodipine Besilate
parent: AI Predictions (L5)
nav_order: 47
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amlodipine As Amlodipine Besilate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
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

## Amlodipine: Evidence Pack Incomplete — TxGNN Predictions Pending
{: .text-alpha }

## One-Sentence Summary

Amlodipine (as amlodipine besilate) is a dihydropyridine calcium channel blocker widely used for hypertension and angina pectoris. This evidence pack currently contains **no TxGNN-predicted new indications**, and two blocking data gaps remain unresolved, preventing a complete repurposing evaluation. The recommended action is to hold until the pipeline is re-run with complete inputs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; Chronic stable angina (based on general pharmacological knowledge — not recorded in evidence pack) |
| Predicted New Indication | Not yet available |
| TxGNN Prediction Score | Not yet available |
| Evidence Level | N/A — pipeline has not returned predictions |
| EU Market Status | Marketed (valid licences: 8 of 12) |
| Number of Authorizations | 12 (valid: 8) |
| Recommended Decision | Hold |

> ⚠️ **Market Status Note:** Amlodipine is a globally off-patent drug available in most major markets including the EU. A result of "0 authorizations" strongly suggests a data query issue rather than a genuine absence from the market. This field should be re-verified before any regulatory decision is made.

---

## Why is This Prediction Reasonable?

No TxGNN predictions are currently available for amlodipine in this evidence pack, so a formal mechanism-to-indication analysis cannot be completed at this stage.

However, amlodipine's pharmacology is well-established: it is a long-acting dihydropyridine **calcium channel blocker (CCB)** that inhibits transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle cells. This results in arterial vasodilation, reduced peripheral vascular resistance, and decreased cardiac oxygen demand — mechanisms that underpin its efficacy in hypertension and chronic stable angina.

From a repurposing perspective, CCBs have been investigated in a broad range of indications beyond cardiovascular disease, including Raynaud's phenomenon, pulmonary arterial hypertension, certain arrhythmias, neuroprotection, and even some oncology-adjacent contexts. Once TxGNN predictions are generated, the mechanistic plausibility of each candidate indication can be assessed against this known biological profile.

Currently, detailed mechanism of action data was not returned by the pipeline (Data Gap DG002). Querying the DrugBank API with the INN `amlodipine` is the recommended remediation step.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Safety data (key warnings, contraindications, and drug-drug interactions) were not returned by the evidence collection pipeline (Data Gap DG001, severity: Blocking). TFDA SmPC PDFs should be downloaded and parsed to populate this section before any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack is structurally incomplete — the `predicted_indications` array is empty, two data gaps are flagged at Blocking/High severity, and the regulatory query returned zero results despite amlodipine being a globally common drug. A meaningful repurposing evaluation cannot proceed until these issues are resolved.

**To proceed, the following is needed:**

- **[DG002 — High]** Retrieve mechanism of action (MOA) from DrugBank API using the INN `amlodipine` (note: the current evidence pack records `drugbank_id: null` — DrugBank lookup by name may be needed)
- **Re-run TxGNN prediction pipeline** after resolving the above gaps to generate predicted indications
- Once predictions are available, re-generate this report using a complete evidence pack

<!-- review:begin eu-lic-20261106-amlodipine_as_amlodipine_besilate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "**[DG001 — Blocking]** Obtain TFDA package insert warnings and contraindications: download SmPC PDF from the TFDA official website and parse the relevant sections / **[DG002 — High]** Retrieve mechanism of action (MOA) from DrugBank API using the INN `amlodipine` (note: the current evidence pack records `drugbank_id: null` — DrugBank lookup by name may be needed)" Removed: leftover template text about Taiwan's TFDA, which does not apply to this EU page. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-amlodipine_as_amlodipine_besilate-1 -->

<!-- review:begin eu-lic-20261106-amlodipine_as_amlodipine_besilate-2 -->

> **Review correction (2026-11-06)**: Originally stated: "**Re-run TxGNN prediction pipeline** after resolving the above gaps to generate predicted indications / **Verify EU market authorization status** — query the EMA product database directly for amlodipine; the current "0 authorizations" result is inconsistent with known market reality and likely reflects a lookup failure" Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 12 EU marketing authorisations for this drug, 8 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-amlodipine_as_amlodipine_besilate-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "**[DG001 — Blocking]** Obtain TFDA package insert warnings and contraindications: download SmPC PDF from the TFDA official website and parse" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-06 | Removed: "**Verify EU market authorization status** — query the EMA product database directly for amlodipine; the current "0 authorizations" result is" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

