---
layout: default
title: Blinatumomab
parent: AI Predictions (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Blinatumomab: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: CD19-positive relapsed or refractory B-cell precursor acute lymphobla…"
---

# Blinatumomab
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

# Blinatumomab: From B-Cell Precursor Acute Lymphoblastic Leukaemia to Primary Release Disorder of Platelets

## One-Sentence Summary

Blinatumomab is a CD19/CD3 bispecific T-cell engager, originally used to treat CD19-positive B-cell precursor acute lymphoblastic leukaemia (ALL).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this prediction, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CD19-positive relapsed or refractory B-cell precursor acute lymphoblastic leukaemia (ALL) in adults, plus other ALL settings (MRD-positive disease, paediatric patients, consolidation therapy) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 95.20% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, blinatumomab is a bispecific T-cell engager that binds CD19 on B cells and CD3 on T cells. This redirects T cells to kill CD19-positive cells, which explains its efficacy in B-cell precursor ALL.

The predicted new indication does not appear to share this biology. Primary platelet release (secretion) disorders arise from intrinsic defects in platelet granule content or signalling, and are unrelated to the CD19 axis. The high TxGNN score (0.952) appears to be a graph-based association with no supporting clinical or literature evidence. In addition, cytopenias, including thrombocytopenia, are known adverse effects of blinatumomab, which argues against benefit.

The other top-ranked predictions are mostly platelet-function or bleeding disorders (Glanzmann thrombasthenia, pseudo-von Willebrand disease, constitutional thrombocytopenia, collagen receptor defect). Others are unrelated conditions (drug-induced osteoporosis, severe nonproliferative diabetic retinopathy, psoriasis, Ledderhose disease, penile fibromatosis). None has a plausible mechanistic link to CD19-directed T-cell engagement, and all are rated L5 and Hold. They likely reflect network proximity in the knowledge graph rather than biological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003731 (cancelled) | Blincyto | Not specified | Monotherapy for CD19-positive relapsed or refractory B-cell precursor acute lymphoblastic leukaemia (ALL) in adults. Patients with Philadelphia chromosome-positive... |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (bispecific T-cell engager, CD19/CD3) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (cytopenias, including thrombocytopenia, are known adverse effects) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions; at minimum CBC with differential, liver function, and monitoring for cytokine release syndrome and neurological toxicity |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records, of which 20 are shown in the data compiled for this report. Major-level interactions include:
  - Bupropion
  - Deferiprone
  - Iohexol
  - Iopamidol
  - Samarium (153Sm) lexidronam

  Moderate-level interactions include naltrexone, warfarin, dicoumarol, theophylline, aminophylline, dyphylline, oxtriphylline, roflumilast, hydrocodone, chloramphenicol, lindane, strontium chloride Sr-89, polyethylene glycol (3350 with electrolytes), picosulfuric acid, and sodium sulfate. Interactions with the anticoagulants warfarin and dicoumarol deserve particular attention in any bleeding-disorder setting.
- **Other safety information**: Please refer to the SmPC for warnings and contraindications.
- **Class-related risks noted in the prediction rationale**: Cytokine release syndrome, neurotoxicity, and cytopenias (including thrombocytopenia).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials or publications, and there is no plausible mechanism. Blinatumomab's known thrombocytopenia risk and its toxicity profile (cytokine release syndrome, neurotoxicity) argue against use in a platelet function disorder. The only EU authorization is also cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Safety information from the SmPC (warnings and contraindications)
- A credible biological rationale, such as an immune-mediated component, supported by preclinical or observational data
- Any clinical or literature evidence in the predicted indication
- Clarification of the EU regulatory status, since the only authorization is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

