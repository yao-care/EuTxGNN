---
layout: default
title: Imlifidase
parent: AI Predictions (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Imlifidase
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

# Imlifidase: From Kidney Transplant Desensitization to Diabetic Cataract

## One-Sentence Summary

Imlifidase is an IgG-cleaving cysteine protease approved for antibody desensitization prior to kidney transplantation. The TxGNN model's top prediction flags **diabetic cataract** as a possible new indication, but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale states no known biological pathway connects the drug's mechanism to cataract pathology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Kidney transplant desensitization (removal of anti-HLA antibodies) — inferred from repurposing rationale text; no formal license/indication record available |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the available repurposing rationale, imlifidase is an IgG-degrading enzyme (cysteine protease) that also inhibits complement activation; its approved use is antibody desensitization before kidney transplantation in highly sensitized patients.

Diabetic cataract results from lens protein oxidation and polyol-pathway–driven osmotic damage — a metabolic and structural process with no established connection to IgG cleavage or complement inhibition. The evidence pack's own mechanistic assessment explicitly states there is **no known biological pathway overlap** between imlifidase's pharmacology and cataract formation.

The high TxGNN score most likely reflects a graph-embedding artifact: imlifidase and the ten disease candidates cluster near shared "diabetes" and "diabetic complication" nodes in the knowledge graph, rather than reflecting a genuine mechanistic signal. This pattern repeats across all ten top-ranked candidates (nine cataract subtypes/stages plus diabetic retinopathy), all scoring within a narrow 0.9848–0.9875 band and all flagged the same way in their rationale text — consistent with node-proximity noise rather than independent, mechanism-based hypotheses.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Confirmed by systematic queries against ClinicalTrials.gov, ICTRP, and PubMed for imlifidase against all 10 predicted indications — all returned 0 results.)*

---

## EU Market Information

Imlifidase currently has 0 marketing authorizations on record and is **not marketed** in this jurisdiction, so no authorization table is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: this is flagged as a Blocking data gap — TFDA/regulatory label warnings and contraindications have not yet been retrieved, which prevents any formal safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for imlifidase are cataract-related conditions or diabetic retinopathy, all rated L5 (prediction only), with zero clinical trials or publications found across 32 systematic evidence queries. The model's own rationale for each candidate explicitly states there is no known mechanistic link, pointing to knowledge-graph node-proximity artifacts rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (currently a High-severity data gap)
- TFDA/EU label warnings and contraindications (currently a Blocking data gap — required before any safety pre-assessment)
- Independent preclinical evidence linking IgG cleavage/complement inhibition to diabetic ocular complications
- At minimum, exploratory case reports or mechanistic literature before this candidate can move beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

