---
layout: default
title: Idarucizumab
parent: AI Predictions (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

# Idarucizumab: From Dabigatran Anticoagulant Reversal to Hemoglobinopathy

## One-Sentence Summary

Idarucizumab is a humanized monoclonal antibody fragment (Fab) whose established role is reversing the anticoagulant effect of dabigatran. The TxGNN model predicts it may be effective for **Hemoglobinopathy**, but currently **0 clinical trials** and **0 publications** support this direction, and the evidence pack's own mechanistic analysis concludes the high score likely reflects knowledge-graph embedding noise rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — this evaluation pack contains no approved indication text; based on the drug's described mechanism, its established use is reversal of dabigatran's anticoagulant activity |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 95.66% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| EU Market Status | Not Marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap (DG002, High severity) in this evidence pack. However, the accompanying rationale for the top-ranked prediction describes idarucizumab's mechanism: it binds dabigatran specifically and irreversibly, with affinity far exceeding dabigatran's affinity for thrombin, thereby neutralizing dabigatran's anticoagulant activity. It has no described action on erythrocyte structure, hemoglobin synthesis, or any related metabolic pathway.

Hemoglobinopathy refers to inherited disorders of red blood cell structure or hemoglobin synthesis — a disease category with no known overlap with the coagulation cascade or thrombin-related targets that idarucizumab acts on. The rationale accompanying this prediction states directly that the high TxGNN score likely arises from drug-disease node embedding similarity in the knowledge graph rather than a biologically grounded mechanism.

This assessment is reinforced by the pattern across all ten of TxGNN's top predictions for this drug: none of the other nine (rheumatoid arthritis, chromosome 16p deletion, beta-thalassemia, pyruvate kinase deficiency, bronchitis, gout, and others) present a plausible mechanistic bridge to idarucizumab's known activity either, and each is independently flagged as Hold at decision stage S0. On current evidence, this prediction does not meet minimal biological plausibility and should be treated as a candidate for further investigation, not as a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

This product currently holds no marketing authorization in the evaluated jurisdiction — market status is "Not Marketed" with 0 authorizations on file, so no license table can be produced.

---

## Safety Considerations

Please refer to the SmPC for safety information.

Note: complete TFDA label warnings and contraindications for this drug are currently missing (data gap DG001, Blocking severity) — this absence by itself prevents the candidate from proceeding to an initial safety screening (S1), independent of the efficacy evidence gap above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are zero clinical trials and zero publications supporting a hemoglobinopathy indication, and the mechanistic rationale supplied with the prediction itself concludes the signal is likely a knowledge-graph artifact rather than genuine pharmacology. Separately, a blocking data gap in TFDA label warnings/contraindications means this candidate cannot yet enter even an initial safety review.

**To proceed, the following is needed:**
- TFDA/SmPC label warnings and contraindications (DG001, Blocking) — required before any S1 safety screening
- Verified mechanism-of-action data for idarucizumab (DG002, High) — required for a rigorous mechanistic relevance analysis
- An independent mechanistic hypothesis or preclinical evidence linking dabigatran-reversal pharmacology to hemoglobinopathy, since none currently exists
- Resolution of the drug-drug interaction query, which currently returns "not_found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

