---
layout: default
title: L-Lysine
parent: AI Predictions (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "L-Lysine: predicted new indication Gastroparesis (evidence level L5). Approved use: Reduction of renal radiation exposure during PRRT with lutetium (177L…"
---

# L-Lysine
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

# L-Lysine: From Renal Radiation Protection and MSUD Management to Gastroparesis

## One-Sentence Summary

L-Lysine is an amino acid used in two EU-authorized products: one to reduce kidney radiation exposure during peptide-receptor radionuclide therapy (PRRT), and one for acute decompensation in maple syrup urine disease (MSUD).
The TxGNN model predicts it may be effective for **gastroparesis**, but there are **0 clinical trials** and only **1 publication** (a preclinical stem-cell delivery study that does not test L-lysine), so the prediction is unsupported by real evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reduction of renal radiation exposure during PRRT with lutetium (177Lu) oxodotreotide in adults |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (all authorizations cancelled) |
| Number of Authorizations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. L-Lysine is an essential amino acid. In its authorized uses, it competes for renal tubular uptake of the radionuclide (LysaKare, given with arginine) and serves as part of an amino acid infusion in MSUD (Maapliv).

No credible mechanistic link to gastroparesis could be established from the data compiled for this report. The only retrieved publication describes delivery of mesenchymal stem cells from hydrogels into the stomach. It does not evaluate L-lysine, so the match appears incidental. The very high TxGNN score should therefore be treated as a computational signal only.

Other predicted indications were also reviewed (congenital prothrombin deficiency, vitamin D deficiency, dyspepsia, familial visceral myopathy, vitamin deficiency disorder, hypophosphatemic rickets, renal tubular acidosis, biotin metabolic disease, postgastrectomy syndrome). All remain at L4–L5 with no clinical trials. Notably, for renal tubular acidosis, the only publication reports a transient proximal tubulopathy induced by amino acid infusion during PRRT, which is an adverse-effect signal and argues against repurposing for that indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical | Bioengineering (Basel) | Delivery of mesenchymal stem cells from gelatin-alginate hydrogels to the stomach lumen for gastroparesis; does not evaluate L-lysine |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004541 | LysaKare | Not specified | Reduction of renal radiation exposure during Peptide-Receptor Radionuclide Therapy (PRRT) with lutetium (177Lu) oxodotreotide in adults. |
| EMEA/H/C/005557 | Maapliv | Not specified | Maple syrup urine disease (MSUD) presenting with an acute decompensation episode in patients from birth who are not eligible for an oral and enteral branched-chain amino acids free (BCAA-free)... |

Both authorizations are cancelled.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (derived from drug-disease relationships in a knowledge graph, not from label text): kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter, hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease, heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation, phenylketonuria and disorders of phenylalanine metabolism.

Label-based warnings, contraindications and drug interaction data were not available. Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, the single publication does not involve L-lysine, and all EU authorizations are cancelled. The knowledge graph also flags numerous renal and cardiac contraindication signals.

**To proceed, the following is needed:**
- Label warnings and contraindications from the EMA documents (a blocking gap for safety screening)
- Mechanism of action data for L-lysine (for example, from DrugBank)
- A plausible mechanistic rationale linking L-lysine to gastric motility, plus targeted literature searches
- Preclinical or early clinical evidence testing L-lysine itself in gastroparesis
- A review of the renal and cardiac contraindication signals relevant to any proposed population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

