---
layout: default
title: Turoctocog Alfa
parent: AI Predictions (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog alfa: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa is a recombinant Factor VIII (FVIII) replacement therapy, established for the treatment and prevention of bleeding episodes in congenital Factor VIII deficiency (Haemophilia A). The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanistic rationale flags this as a likely false-positive association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital Factor VIII deficiency (Haemophilia A) — inferred from known drug class; not populated in the current EU regulatory data extract |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.99% (rank 125 of all candidates) |
| Evidence Level | L5 — model prediction only, no supporting trials or literature |
| EU Market Status | ✗ Not marketed (per current data extract) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this Evidence Pack (flagged as a High-severity data gap). Based on established pharmacological knowledge, Turoctocog alfa is a B-domain–truncated recombinant human Factor VIII (rFVIII), which acts as a cofactor for activated Factor IX in the intrinsic tenase complex, accelerating thrombin generation during secondary (plasma-phase) haemostasis. Its proven efficacy is in congenital FVIII deficiency (Haemophilia A), where the underlying defect is a quantitative or qualitative lack of functional FVIII protein.

Primary release disorder of platelets, by contrast, is a defect of **primary haemostasis** — platelets fail to release granule contents (ADP, serotonin, thromboxane, etc.) needed to recruit and activate additional platelets at the injury site. This pathway does not involve FVIII, and supplementing FVIII does not correct impaired granule secretion. The Evidence Pack's own mechanistic rationale for this candidate explicitly notes the link is "weak" and may reflect TxGNN over-generalizing across the shared "bleeding disorder" semantic neighborhood in the knowledge graph, rather than a genuine, pathway-specific therapeutic relationship.

Notably, this pattern is not isolated: across the top 10 TxGNN predictions for this drug, 8 of 10 (including ranks 2–4, 6–7, 9–10) carry similarly weak or even mechanistically contradictory rationales — platelet-count disorders, receptor defects, and even thrombotic (pro-clotting) conditions where FVIII supplementation could theoretically worsen outcomes (e.g., thrombotic thrombocytopenic purpura). Only two lower-ranked candidates (rank 5, "acquired coagulation factor deficiency," and rank 8, "flood factor deficiency" — likely a mislabelled/mis-mapped entry for combined FV/FVIII deficiency) retain a biologically plausible link to FVIII replacement and are flagged as open research questions rather than Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorizations are recorded for this drug in the current data extract (0 licenses on file; market status reported as "not marketed"). This is inconsistent with the drug's broader public profile as an approved rFVIII product and likely reflects incomplete data ingestion for this entry rather than an actual absence of EU authorization — see data gaps below.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and drug interaction data were all marked as data gaps in this Evidence Pack — TFDA/EMA label warnings and contraindications are flagged as a Blocking-severity gap, meaning this candidate cannot pass initial safety screening (S1) until resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (primary release disorder of platelets) has no supporting clinical trials or literature (L5, decision stage S0), and the mechanistic rationale itself indicates the FVIII pathway is not relevant to platelet granule-release defects — this is most likely a knowledge-graph semantic over-generalization rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Resolve the Blocking-severity data gap: obtain TFDA/EMA SmPC warnings and contraindications (required before any S1 safety screening can proceed)
- Resolve the High-severity data gap: confirm mechanism of action via DrugBank API
- Correct/verify the EU market status and authorization data, which currently conflicts with the drug's known regulatory profile
- If pursuing further investigation, redirect resources away from rank 1 and toward the two "Research Question" candidates instead:
  - Re-run targeted ClinicalTrials.gov/PubMed searches for **"acquired haemophilia A"** to test whether rank 5 ("acquired coagulation factor deficiency") reflects real-world evidence
  - Verify whether rank 8 ("flood factor deficiency") is a mislabelled entry for **combined Factor V/VIII deficiency (F5F8D)**, then search accordingly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

