---
layout: default
title: Tislelizumab
parent: AI Predictions (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
---

# Tislelizumab
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

# Tislelizumab: From Advanced Solid Tumors to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Tislelizumab is an anti-PD-1 immune checkpoint inhibitor used in multiple advanced solid tumors (per literature evidence in this pack, including NSCLC, esophageal, cervical, and colorectal cancer regimens). The TxGNN model predicts a possible link to **mixed-type autoimmune hemolytic anemia**, but this prediction is currently supported by **zero clinical trials and zero relevant publications**, and the underlying mechanism points in the opposite direction — PD-1 blockade is expected to worsen, not treat, autoimmune hemolysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No EU marketing authorization on file; literature in this pack indicates use across multiple advanced solid tumors (e.g., NSCLC, esophageal, cervical, colorectal cancer) |
| Predicted New Indication | Mixed-Type Autoimmune Hemolytic Anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action field is not available in this evidence pack. However, literature captured elsewhere in the pack (e.g., PMID 41268547) confirms tislelizumab is a humanized IgG4 anti-PD-1 monoclonal antibody that blocks the PD-1/PD-L1 checkpoint pathway to reactivate anti-tumor T-cell immunity — consistent with its known class as an immune checkpoint inhibitor used across multiple oncology indications.

The relationship between the original use case (reactivating suppressed anti-tumor immunity) and the predicted indication (autoimmune hemolytic anemia, a condition driven by pathological immune destruction of red blood cells) is not supportive — it is contradictory. Removing the PD-1 "brake" on T-cell activity is the opposite of what is needed to control an overactive autoimmune process. The evidence pack's own mechanistic rationale explicitly flags this: the TxGNN score likely reflects the knowledge graph's encoding of **PD-1 inhibitor-associated immune-related adverse events (irAEs)** — including hematologic and dermatologic autoimmune toxicity — rather than a genuine treatment signal.

This concern is reinforced by the other top-10 TxGNN predictions in this pack: idiopathic aplastic anemia, drug-induced autoimmune hemolytic anemia, dermatitis, proteinuria, and amyopathic dermatomyositis are all conditions independently documented in the literature as **adverse effects of tislelizumab**, not therapeutic targets. For example, the dermatitis and proteinuria predictions (rank 3 and 6) are backed by real literature, but that literature consists of case reports of tislelizumab-induced SJS/TEN, DRESS, and renal thrombotic microangiopathy — evidence of harm, not efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Tislelizumab has no EU marketing authorization on file (market status: not marketed; 0 authorizations recorded). No product-level licensing table is available for this evidence pack.

---

## Cytotoxicity

Tislelizumab is classified as an antineoplastic agent (immune checkpoint inhibitor used in multiple solid tumor indications per literature in this pack), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) — not a conventional cytotoxic |
| Myelosuppression Risk | Low overall compared to conventional cytotoxics; however, rare immune-mediated agranulocytosis has been reported (PMID 38910480) |
| Emetogenicity Classification | Low (checkpoint inhibitors are minimally emetogenic) |
| Monitoring Items | CBC with differential (rare agranulocytosis), renal function/urinalysis (reported TMA and ANCA-associated vasculitis with proteinuria), skin examination (SJS/TEN, DRESS risk), thyroid and other endocrine panels, liver function |
| Handling Protection | Standard IV infusion precautions for a monoclonal antibody; not typically subject to cytotoxic hazardous-drug handling protocols used for alkylating/cytotoxic chemotherapy, but institutional hazardous-drug policy and the SmPC should be confirmed |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug interaction data are marked as data gaps in this evidence pack — see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on an AI-generated association (L5) with no supporting clinical trials or literature, and the drug's known mechanism (PD-1 checkpoint blockade → immune activation) is biologically contradictory to treating an autoimmune hemolytic condition. Related predictions in this same evidence pack (dermatitis, proteinuria) are in fact documented in the literature as *adverse effects* of tislelizumab, reinforcing that the knowledge graph signal here likely reflects known immune-related toxicity rather than a therapeutic opportunity.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (flagged as a **Blocking** data gap — required before any S1 safety review)
- Confirmed mechanism-of-action data sourced directly from DrugBank (flagged as a **High**-severity data gap)
- Independent preclinical or mechanistic validation specifically addressing why checkpoint activation would be therapeutic in an autoimmune hemolytic setting, before any further investment
- If pursued despite the above, a formal EU regulatory pathway assessment, since tislelizumab currently holds no EU marketing authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

