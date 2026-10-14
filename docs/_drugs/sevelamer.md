---
layout: default
title: Sevelamer
parent: AI Predictions (L5)
nav_order: 559
evidence_level: L5
indication_count: 10
---

# Sevelamer
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

# Sevelamer: From Hyperphosphataemia in Dialysis to Breast Fibrocystic Disease

## One-Sentence Summary

Sevelamer is a non-absorbed phosphate-binding polymer, originally used to control hyperphosphataemia in adult patients receiving haemodialysis or peritoneal dialysis.
The TxGNN model predicts it may be effective for **breast fibrocystic disease**, but **no clinical trials and no publications** currently support this prediction.
The best-supported alternative direction among the top ten predictions is **HIV infection / AIDS**, which has only early-stage evidence (**3 publications**: one small single-arm study, one primate study and one unrelated case report).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Control of hyperphosphataemia in adult patients receiving haemodialysis or peritoneal dialysis |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 92.46% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sevelamer is a non-absorbed phosphate-binding polymer. Its efficacy in controlling hyperphosphataemia in dialysis patients is established, and it acts in the gut rather than systemically.

For the top-ranked prediction, breast fibrocystic disease, no plausible link to this mechanism is evident. The same applies to the other breast-related predictions (apocrine adenosis, blunt duct adenosis, benign mammary dysplasia, breast abscess, fat necrosis). Several of them share identical scores, which suggests a correlated knowledge-graph pattern within a cluster of benign breast conditions rather than independent evidence. These predictions should be treated as computational signals only.

The only direction with a plausible, if indirect, rationale is HIV infection/AIDS. Sevelamer binds bacterial endotoxin (lipopolysaccharide) in the gut and might reduce microbial translocation and chronic immune activation. However, the one human study found that sevelamer did not lower lipopolysaccharide or soluble CD14 levels, so the mechanism is not confirmed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for breast fibrocystic disease.

---

## Literature Evidence

Currently no related literature available for breast fibrocystic disease.

For reference, the literature found for the next best-supported predictions (HIV infection and AIDS):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24864123](https://pubmed.ncbi.nlm.nih.gov/24864123/) | 2014 | Single-arm clinical study (36 participants) | J Infect Dis | 8 weeks of sevelamer in untreated HIV infection did not significantly change markers of microbial translocation (lipopolysaccharide, soluble CD14), but reduced soluble tissue factor, LDL cholesterol and oxidized LDL cholesterol |
| [24837437](https://pubmed.ncbi.nlm.nih.gov/24837437/) | 2014 | Preclinical animal study | J Clin Invest | In acutely SIV-infected macaques, sevelamer-based blockade of microbial translocation reduced inflammation and viral replication |
| [42371456](https://pubmed.ncbi.nlm.nih.gov/42371456/) | 2026 | Case report | Cureus | Recurrent calciphylaxis in a patient with HIV-associated end-stage renal disease; does not support a treatment effect in HIV |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000254 (cancelled) | Renagel | Not specified | Control of hyperphosphataemia in adult patients receiving haemodialysis or peritoneal dialysis. Renagel should be used within the context of a multiple... |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Those graded Moderate include vitamin D and its analogues (cholecalciferol, calcifediol, calcitriol, dihydrotachysterol, ergocalciferol), levofloxacin and vitamin A. Others are of unknown severity, for example pantoprazole, omeprazole, lansoprazole, cimetidine, vancomycin, morphine, prednisone and acarbose.
- **Knowledge-graph contraindication signals** (not label text): vitamin D deficiency, osteomalacia, rickets, hypophosphatemia and gastroparesis. These come from a computational knowledge graph and need verification against the product information.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (breast fibrocystic disease, score 0.92) is a computational output only, with no trials, no publications and no plausible mechanism for a non-absorbed phosphate binder. The EU authorization is also cancelled. HIV/AIDS is better framed as a research question than as a development candidate, because the human data did not confirm the proposed mechanism.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link to the predicted indications
- Warnings and contraindications from the product information (SmPC), including review of the knowledge-graph contraindication signals
- For HIV/AIDS: verification of the study designs, and a controlled trial assessing clinically meaningful outcomes beyond the biomarkers already tested
- Clarification of why the EU authorization was cancelled, and whether it affects any further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

