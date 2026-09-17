---
layout: default
title: Sildenafil
parent: AI Predictions (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Sildenafil
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

Using no additional skill — this is a direct document-generation task with an explicit template and complete input data, so I'll produce the report directly.

---

# Sildenafil: From an Unregistered Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Sildenafil's original indication cannot be characterized from this evidence pack — the drug is **not currently marketed** in this jurisdiction and no license records exist. The TxGNN model predicts a possible link to **Ambras type hypertrichosis universalis congenita**, an ultra-rare congenital hair-overgrowth syndrome, but this pairing is supported by **zero clinical trials** and **zero publications**, and the model's own rationale flags it as a likely knowledge-graph artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available — drug is not marketed in this jurisdiction; 0 authorizations on file |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 98.41% (rank 13,938 among all predictions) |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently unavailable for sildenafil in this evidence pack (flagged as a **High-severity data gap**, DG002). Separately within the same evidence pack, literature attached to a different candidate indication (PMID 30292404) describes sildenafil as a PDE5 inhibitor that increases intracellular cGMP and causes vasodilation — a mechanism that plausibly affects vascular/follicular tissue but has no established connection to Ambras type hypertrichosis, a congenital genetic overgrowth syndrome.

Critically, the model's own repurposing rationale for this candidate states that the high TxGNN score "may reflect indirect connections in the knowledge graph with other hair/vascular-related nodes, without direct mechanistic evidence supporting sildenafil's action in this indication." In other words, this is very likely a **graph-topology artifact** (shared neighbors with unrelated hair/vascular nodes) rather than a biologically grounded hypothesis. Given the extreme rarity of this syndrome and complete absence of trials or literature, there is currently no basis to treat this as a credible repurposing signal.

**Note for consideration**: within this same evidence pack, a lower-ranked candidate — **genetic alopecia** (rank 9, score 75.03%) — has substantially stronger support: one completed early-phase RCT (NCT06527729, sildenafil lipid nanocarrier vs. placebo in alopecia areata, n=28), one additional relevant trial (NCT05369481, topical sildenafil vs. minoxidil), and a mechanistic publication (PMID 30292404) directly studying sildenafil's effect on human hair follicles. That candidate is already scored L3 / Research Question stage and may warrant prioritized evaluation over the top-ranked but evidence-free Ambras hypertrichosis prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Sildenafil has **no marketing authorizations on file** in this dataset (`market_status`: Not Marketed, `total_licenses`: 0). No license table can be generated.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings and contraindications for this drug are recorded as a **Blocking-severity data gap** (DG001) — TFDA/label safety data has not yet been retrieved. This must be resolved before any safety evaluation (S1 stage) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support, and the model's own rationale identifies it as a likely spurious knowledge-graph connection rather than a genuine mechanistic hypothesis. In addition, two blocking data gaps — missing label/safety data (DG001, Blocking) and missing MOA documentation (DG002, High) — prevent this candidate from advancing past S0.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (DG001 — currently blocking)
- Confirmed mechanism-of-action documentation for sildenafil (DG002)
- Any direct preclinical or mechanistic evidence specifically linking sildenafil to Ambras type hypertrichosis (currently none exists)
- Consider redirecting evaluation effort toward the better-evidenced **genetic alopecia** candidate (rank 9, L3, Research Question) identified in the same evidence pack, which already has a completed RCT and supporting mechanistic literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

