---
layout: default
title: Nonacog Beta Pegol
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
---

# Nonacog Beta Pegol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Nonacog Beta Pegol: From Factor IX Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

> Nonacog beta pegol is a PEGylated recombinant coagulation factor IX, used as replacement therapy in factor IX deficiency (Hemophilia B).
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
> but currently **no clinical trials** and **no literature** support this specific pairing, and the evidence pack's own mechanistic review flags the prediction as likely a knowledge-graph artifact rather than a genuine pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Factor IX deficiency (Hemophilia B) — inferred from drug pharmacology; no formal indication text on file |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is not available in structured form for this drug (data gap DG002). Based on the pharmacological description referenced in the evidence pack, Nonacog beta pegol is a PEGylated recombinant coagulation factor IX that acts on the intrinsic coagulation pathway (activated FIX converts FX to FXa), and is used to replace missing clotting factor in Factor IX deficiency.

The top-ranked predicted indication, primary release disorder of platelets, is a **platelet granule-release/storage pool defect** — the underlying pathology is intrinsic platelet dysfunction, not a coagulation factor deficiency. Replacing FIX does not correct a platelet secretion defect, so there is no established pharmacological pathway connecting the two conditions. The evidence pack's own rationale states that the high TxGNN score most likely arises from shared "bleeding phenotype" clustering in the knowledge graph rather than a true mechanistic relationship.

This pattern repeats across all 10 ranked predictions for this drug: Glanzmann thrombasthenia (GPIIb/IIIa defect), pseudo-von Willebrand disease (GP1BA gain-of-function), constitutional thrombocytopenia, collagen-receptor bleeding disorders, Scott syndrome, diabetic retinopathy, FNAIT, platelet-type bleeding disorder, and hereditary thrombocytosis with limb defect — none share FIX's mechanistic pathway, and each rationale explicitly notes the mismatch. This suggests the predictions in this batch are driven by symptomatic (bleeding-phenotype) similarity in the graph rather than actionable drug-repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: NCT04398628, "ATHN Transcends," is a multi-disorder natural-history registry that includes Glanzmann thrombasthenia and platelet-type bleeding disorder patients, but it is an observational registry — not a drug-specific interventional trial — and is graded C-relevance in the source evidence.)*

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations on file — the drug is currently not marketed (0 licenses recorded).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: Drug label warnings/contraindications are marked as a **Blocking** data gap (DG001) — TFDA/EMA label data have not yet been retrieved and are required before this candidate can enter S1 safety screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 ranked predictions for this drug are Evidence Level L5 (model prediction only), with no supporting interventional trials or literature for any pairing. The top-ranked indication's own mechanistic review concludes the FIX pathway does not plausibly explain platelet release disorders, and the same disconnect recurs across the remaining candidates — indicating the signal is likely graph noise rather than a real repurposing opportunity. The drug is also not currently marketed, and critical safety data (label warnings/contraindications) are missing.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA label warnings and contraindications (blocking gap DG001)
- Obtain formal, structured MOA documentation (gap DG002)
- If pursuing further, prioritize re-scoring or manual review of candidates outside this bleeding-phenotype cluster, since the current top-10 list shows systematically weak mechanistic plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

