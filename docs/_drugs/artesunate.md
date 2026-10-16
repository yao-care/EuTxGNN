---
layout: default
title: Artesunate
parent: AI Predictions (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Artesunate: predicted new indication Acne (disease) (evidence level L5). Approved use: Initial treatment of severe malaria in adults and children"
---

# Artesunate
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

# Artesunate: From Severe Malaria to Acne

## One-Sentence Summary

Artesunate is an antimalarial drug, originally used for the initial treatment of severe malaria in adults and children.
The TxGNN model predicts it may be effective for **acne**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Initial treatment of severe malaria in adults and children |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 79.21% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, artesunate is an artemisinin-class antimalarial. Its efficacy in severe malaria is established, and it may be mechanistically applicable to acne, but this link has not been verified.

One possible link is the anti-inflammatory and immunomodulatory activity reported for artemisinin derivatives, such as suppression of NF-kB signalling and inflammatory cytokines. Acne is an inflammatory skin disease, so such activity could be relevant. This is hypothesis-level reasoning and is not supported by any trial or publication in the compiled data.

The prediction therefore stays at the model level. Malaria and acne are clinically very different diseases, and the similarity to the original indication has not been assessed.

### Other Predicted Indications

The model also ranked the following indications. None has clinical trial or literature support in the compiled data, and all remain at L5 with a Hold recommendation.

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Smouldering systemic mastocytosis | 79.18% | No clear mechanistic rationale |
| 3 | Lymphoadenopathic mastocytosis with eosinophilia | 77.26% | Likely driven by proximity to other mastocytosis nodes in the knowledge graph |
| 4 | Gastrin secretion abnormality | 76.71% | No plausible mechanism evident |
| 5 | Systemic mastocytosis | 71.44% | Clusters with the other mastocytosis predictions, suggesting a shared graph signal |
| 6 | Leishmaniasis, diffuse cutaneous | 66.16% | Most coherent rationale (antiparasitic link, preclinical leishmania work), but unverified |
| 7 | Abnormality of glucagon secretion | 61.77% | Speculative link to alpha-cell and glucagon signalling |
| 8 | Pyogenic arthritis-pyoderma gangrenosum-acne syndrome | 59.66% | Autoinflammatory disorder; anti-inflammatory activity relevant only in principle |
| 9 | Wiskott-Aldrich syndrome 2 | 59.41% | Unlikely to be addressed by a small-molecule antimalarial |
| 10 | Alacrima, achalasia, and intellectual disability syndrome | 59.33% | Appears to be a graph-based artifact |

Among these, cutaneous leishmaniasis has the most biologically coherent rationale and may merit a targeted literature review first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005550 (cancelled) | Artesunate Amivas | Not specified | Artesunate Amivas is indicated for the initial treatment of severe malaria in adults and children. Consideration should be given to official guidance on the appropriate use of... |

## Cytotoxicity

Artesunate is an antimalarial, not an antineoplastic drug, so this section does not apply.

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 74 interacting drugs. The first 20 returned include one Major interaction and 19 Moderate interactions.
  - **Major**: Eluxadoline
  - **Moderate (examples)**: Eliglustat, Rolapitant, Cobicistat, Eltrombopag, Fostamatinib, Alpelisib, Valsartan, Apalutamide, Atazanavir, Axitinib, Carbamazepine, Diclofenac, Crizotinib

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acne is supported only by a model score of 79.21%, with no clinical trials or publications (Evidence Level L5). The only EU authorization is cancelled, and warning and contraindication data are missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Safety information (warnings and contraindications) from the EMA product information, which blocks safety screening
- Mechanism of action data for artesunate (for example from DrugBank)
- A targeted literature review of artemisinin derivatives in acne and inflammatory skin disease, and of cutaneous leishmaniasis as the most plausible alternative
- Assessment of route compatibility, as a topical or oral route for a skin indication has not been evaluated
- Preclinical or early clinical evidence to move beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

