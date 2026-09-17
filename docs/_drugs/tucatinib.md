---
layout: default
title: Tucatinib
parent: AI Predictions (L5)
nav_order: 621
evidence_level: L5
indication_count: 10
---

# Tucatinib
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

# Tucatinib: From HER2-Positive Cancer to Migraine Disorder

## One-Sentence Summary

Tucatinib is referenced throughout this Evidence Pack as an HER2-directed tyrosine kinase inhibitor (HER2 TKI); however, its formal original indication text and mechanism-of-action documentation are flagged as data gaps in this pack, and the drug currently has no marketing authorization in this jurisdiction. The TxGNN model predicts it may be effective for **Migraine Disorder** (score 98.62%), but **0 clinical trials** and **0 publications** currently support this specific pairing — the evidence pack itself explicitly notes there is no known biological mechanism linking HER2 inhibition to migraine pathology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (data gap); repurposing rationale entries consistently describe tucatinib as an HER2-directed tyrosine kinase inhibitor |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.62% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for tucatinib in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale text accompanying each predicted indication, tucatinib is consistently described as an HER2-directed tyrosine kinase inhibitor (HER2 TKI) — a targeted class typically used in HER2-positive solid tumors — but no confirmed original indication text or formal MOA record is included in this pack.

Critically, the rationale associated with this specific prediction (migraine disorder) explicitly states that **no known mechanistic relationship exists** between HER2 tyrosine kinase inhibition and migraine pathophysiology (vascular tone regulation, CGRP signaling). The rationale characterizes this as "a high TxGNN knowledge-graph embedding score without biological support," suggesting the association likely reflects a structural artifact of the knowledge graph (e.g., shared node connectivity) rather than a genuine pharmacological hypothesis.

This pattern is consistent across the full set of top-10 TxGNN predictions for tucatinib in this pack: reviewer annotations for related candidates (e.g., multiple endocrine neoplasia, nephrogenic syndrome of inappropriate antidiuresis, Prinzmetal angina, homozygous familial hypercholesterolemia) independently flag "no mechanistic link," "mismatched pairing," or "likely false positive from sparse KG nodes." Taken together, this indicates the migraine disorder prediction should be treated as a low-confidence, mechanism-free lead rather than a validated repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Tucatinib has no marketing authorizations recorded in this Evidence Pack (total_licenses = 0; market_status = Not marketed). No authorization table can be generated at this time.

---

## Cytotoxicity

Repurposing rationale text in this Evidence Pack repeatedly identifies tucatinib as an HER2-directed tyrosine kinase inhibitor, which is consistent with classification as an antineoplastic/targeted cancer therapy. However, no DrugBank category field, original indication text, or toxicity data is included in this pack to confirm details.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed tyrosine kinase inhibitor, based on repurposing rationale references in this pack) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are zero clinical trials and zero publications supporting a tucatinib–migraine disorder association, and the evidence pack's own rationale explicitly states there is no known mechanistic link between HER2 tyrosine kinase inhibition and migraine pathophysiology. This candidate is best characterized as an unsupported knowledge-graph embedding artifact (Evidence Level L5) rather than a plausible repurposing lead.

**To proceed, the following is needed:**
- TFDA/regulatory-label warnings and contraindications (currently a Blocking data gap — DG001), required before any S1 safety pre-assessment
- Confirmed mechanism-of-action documentation from DrugBank or the manufacturer (High-severity data gap — DG002)
- A biologically plausible mechanistic hypothesis (e.g., CGRP or vascular pathway involvement) linking HER2 inhibition to migraine, supported by preclinical data
- Confirmation of tucatinib's original approved indication and regulatory status, since no marketing authorization or approved indication text currently exists in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

