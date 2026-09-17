---
layout: default
title: Tigecycline
parent: Medium Evidence (L3-L4)
nav_order: 591
evidence_level: L4
indication_count: 10
---

# Tigecycline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tigecycline: From Bacterial Infections to Disorder of Tyrosine Metabolism

## One-Sentence Summary

> Tigecycline is a glycylcycline-class antibiotic originally used to treat bacterial infections.
> The TxGNN model predicts potential efficacy for **Disorder of Tyrosine Metabolism**, but the supporting evidence appears to be a label/knowledge-graph mismatch —
> the single associated trial and most of the **4 publications** actually concern tigecycline's mitochondrial-inhibition effects in leukemia and myeloma, not tyrosine metabolism, and the drug currently holds **no marketing authorization** in the EU.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (glycylcycline antibiotic class; no formal indication text on file — see Data Gap DG001) |
| Predicted New Indication | Disorder of Tyrosine Metabolism |
| TxGNN Prediction Score | 95.76% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (Data Gap DG002). Based on information found within the supporting literature itself, tigecycline is a glycylcycline antibiotic (a tetracycline derivative) that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit and is used for complicated infections. This antimicrobial mechanism has no established biological pathway connecting it to tyrosine catabolism, the enzymatic pathway underlying disorder of tyrosine metabolism — a rare inherited metabolic disease.

The original indication (bacterial infection) and the predicted new indication (a congenital metabolic disorder) sit in entirely different disease domains, and the Evidence Pack itself flags this as a likely label/knowledge-graph mismatch. Rather than supporting the tyrosine-metabolism label, the one associated clinical trial (NCT02883036) and three of the four cited publications actually investigate a different, better-characterized signal: tigecycline's inhibition of mitochondrial protein synthesis (mitoribosome/OXPHOS), which has shown activity against chronic myeloid leukemia stem cells and, in a separately ranked prediction, multiple myeloma cells (see rank #10, monoclonal gammopathy, which carries the same mechanistic signal with more coherent supporting literature).

Only one cited publication (PMID 41009505) touches tangentially on tyrosine metabolism — via melanocyte pigmentation, since melanin is a downstream product of tyrosine catabolism — but this concerns a cutaneous adverse-effect pathway, not a therapeutic mechanism for the metabolic disorder itself. Given this, the predicted indication should be treated as a low-confidence model output that requires knowledge-graph node-mapping verification before any further evaluation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02883036](https://clinicaltrials.gov/study/NCT02883036) | N/A | Unknown | 100 | Studies changes in mitochondrial biogenesis and metabolic characteristics with tigecycline treatment in chronic myeloid leukemia (CML) in vitro; not directly related to tyrosine metabolism. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29404396](https://pubmed.ncbi.nlm.nih.gov/29404396/) | 2018 | Commentary/Review | Molecular & Cellular Oncology | Summarizes findings that tigecycline plus imatinib disrupts mitochondrial respiration to eradicate CML leukemic stem cells. |
| [31765940](https://pubmed.ncbi.nlm.nih.gov/31765940/) | 2020 | Preclinical (mechanistic) | Neoplasia | Targeting mitochondrial OXPHOS (relevant to tigecycline's mechanism) eradicates EGFR-TKI-resistant lung adenocarcinoma cancer stem cells. |
| [41009505](https://pubmed.ncbi.nlm.nih.gov/41009505/) | 2025 | Preclinical (in vitro) | International Journal of Molecular Sciences | Tigecycline affects human epidermal melanocyte and fibroblast homeostasis, linked to its melanin-binding affinity and pigmentary/phototoxic skin adverse effects — tangential connection to tyrosine/melanin pathway, not a therapeutic mechanism. |
| [28920959](https://pubmed.ncbi.nlm.nih.gov/28920959/) | 2017 | Preclinical (in vitro/in vivo mechanistic) | Nature Medicine | Targeting mitochondrial oxidative phosphorylation eradicates therapy-resistant CML leukemic stem cells; tigecycline used as OXPHOS inhibitor. |

**Note:** None of the above evidence directly addresses tyrosine metabolism disorder; the cluster of evidence instead supports a mitochondrial-OXPHOS-inhibition mechanism relevant to hematologic malignancies (see rank #10, monoclonal gammopathy).

## EU Market Information

Tigecycline currently holds no marketing authorization on file in the EU dataset (0 authorizations, market status: Not Marketed).

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug interaction data are not currently available in this Evidence Pack (Data Gap DG001, classified as Blocking for safety assessment).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted disease label (disorder of tyrosine metabolism) does not match the actual content of the supporting trial and literature, which instead describe a mitochondrial-OXPHOS mechanism relevant to hematologic malignancies — this is most likely a knowledge-graph node-mapping error rather than a genuine repurposing signal.
- The drug has no EU marketing authorization, and blocking safety data (TFDA labeling/warnings, DG001) and mechanism-of-action data (DG002) are both missing, so this candidate cannot proceed past S0/S1 review.

**To proceed, the following is needed:**
- Verify the TxGNN knowledge-graph node mapping for "disorder of tyrosine metabolism" against tigecycline to rule out a label/entity mismatch.
- Obtain TFDA/EMA label warnings and contraindications (Data Gap DG001) before any safety evaluation.
- Obtain formal mechanism-of-action data from DrugBank (Data Gap DG002).
- Consider re-scoping this candidate toward the mitochondrial-OXPHOS-inhibition signal actually supported by the evidence (e.g., rank #10, monoclonal gammopathy/multiple myeloma, which is already at decision stage S1 with a "Research Question" recommendation and coherent mechanistic literature) rather than pursuing the tyrosine-metabolism label as currently ranked.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

