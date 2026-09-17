---
layout: default
title: Tisagenlecleucel
parent: AI Predictions (L5)
nav_order: 598
evidence_level: L5
indication_count: 10
---

# Tisagenlecleucel
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

# Tisagenlecleucel: From B-Cell Malignancies to Crohn's Colitis

## One-Sentence Summary

Tisagenlecleucel is a CD19-directed CAR-T cell therapy whose established use is in B-cell malignancies (ALL, DLBCL); a confirmed original-indication record and formal EU licence data are not available in this evidence pack. The TxGNN model predicts it may be effective for **Crohn's Colitis**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review flags the link as biologically weak and potentially safety-contradictory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | B-cell malignancies (ALL, DLBCL) — per known CAR-T drug class, referenced in the evidence pack's rationale text; not confirmed by EU licence data (none provided) |
| Predicted New Indication | Crohn's Colitis |
| TxGNN Prediction Score | 91.39% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the limited contextual information in the evidence pack, Tisagenlecleucel is an anti-CD19 chimeric antigen receptor (CAR) T-cell therapy, with established use in B-cell malignancies such as acute lymphoblastic leukemia (ALL) and diffuse large B-cell lymphoma (DLBCL). Its therapeutic effect depends on recognizing and eliminating CD19-expressing B cells.

Crohn's colitis, however, is predominantly driven by Th1/Th17-mediated intestinal inflammation and innate immune dysregulation, with B cells playing a secondary role at most. The evidence pack's own rationale assessment explicitly notes that the high TxGNN score most likely reflects an indirect graph-embedding association between CD19/B-cell nodes and gut-immune nodes, rather than genuine mechanistic plausibility — no direct biological pathway connects CD19-CAR-T activity to Crohn's colitis pathophysiology.

More importantly, the rationale raises a potential safety conflict rather than simple inefficacy: CAR-T therapy carries a known risk of cytokine release syndrome (CRS), which stands in direct tension with the therapeutic goal of controlling gut inflammation in Crohn's disease. Given the L5 evidence level, the absence of any supporting clinical or literature data, and this internally flagged mechanistic contradiction, this candidate should not be interpreted as a validated repurposing signal at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Currently no EU marketing authorizations on record (drug status: Not Marketed; total licences = 0).

---

## Cytotoxicity

Tisagenlecleucel is a genetically modified cellular immunotherapy approved for B-cell malignancies, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy — CD19-directed genetically modified autologous T-cell therapy (CAR-T), not a conventional cytotoxic agent |
| Myelosuppression Risk | High — B-cell aplasia and cytopenias are recognized class effects of CD19 CAR-T therapy; please refer to the SmPC for detailed haematologic toxicity data (not available in this evidence pack) |
| Emetogenicity Classification | Low — not a conventional cytotoxic chemotherapeutic agent |
| Monitoring Items | CBC with differential, B-cell counts/immunoglobulin levels, CRP/ferritin (cytokine release syndrome monitoring), neurological assessment (ICANS) |
| Handling Protection | Requires specialized handling per cellular/gene therapy product regulations (not conventional cytotoxic drug handling); administration restricted to certified treatment centers |

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug interaction data are not available in this evidence pack, and TFDA/EMA label data acquisition is flagged as a **Blocking** data gap preventing initial safety review (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or published literature currently support any of the ten TxGNN-predicted indications for Tisagenlecleucel; all remain at evidence level L5 (decision stage S0). The top-ranked candidate, Crohn's colitis, is itself flagged by the evidence pack's own mechanistic review as biologically weak and potentially safety-contradictory (CRS risk vs. anti-inflammatory treatment goal), and a Blocking data gap prevents entry into the safety initial-evaluation stage.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: obtain official TFDA/EMA label warnings and contraindications
- Confirm mechanism of action and original-indication documentation from a regulatory source (DrugBank query)
- Await emergence of actual clinical trial or literature evidence before advancing any candidate beyond S0
- If prioritizing among the 10 candidates, note that two others — ankylosing spondylitis and rheumatoid vasculitis — are flagged in the pack as "Research Question" (more biologically plausible B-cell-mediated autoimmune mechanisms) and may merit closer monitoring ahead of Crohn's colitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

