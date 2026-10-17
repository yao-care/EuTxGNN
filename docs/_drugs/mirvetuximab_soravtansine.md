---
layout: default
title: Mirvetuximab Soravtansine
parent: AI Predictions (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mirvetuximab Soravtansine: predicted new indication Antithrombin deficiency type 2 (evidence level L5). Approved use: FRα-positive, platinum-resistant high grade serous epithelial ovarian…"
monitor_inn: "Mirvetuximab Soravtansine"
predicted_indications: ["antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "candidiasis", "plasma cell myeloma", "indolent plasma cell myeloma", "tinea corporis", "thrombophilia", "uterine polyp", "pediatric systemic lupus erythematosus"]
---

# Mirvetuximab Soravtansine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Mirvetuximab Soravtansine: From Platinum-Resistant Ovarian Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Mirvetuximab soravtansine is an antibody-drug conjugate (ADC) originally used to treat folate receptor-alpha (FRα) positive, platinum-resistant ovarian, fallopian tube, or primary peritoneal cancer.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but **no clinical trials and no publications** support this prediction, and it looks like a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | FRα-positive, platinum-resistant high grade serous epithelial ovarian, fallopian tube, or primary peritoneal cancer (after one to three prior systemic regimens) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 97.95% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the target information that is available, mirvetuximab soravtansine is an antibody-drug conjugate. Its antibody component binds FRα (gene *FOLR1*) with very high affinity (Kd about 0.08 nM in vitro). It delivers the maytansinoid payload DM4, a microtubule inhibitor, to FRα-expressing tumour cells.

Antithrombin deficiency type 2 is an inherited, qualitative defect of a coagulation inhibitor caused by *SERPINC1* variants. A cytotoxic, tumour-targeted ADC has no known role in correcting this defect. The high score (0.98) therefore appears to be an artifact of the knowledge graph and not a biologically grounded signal. The same pattern appears in the other top-ranked predictions (heparin cofactor 2 deficiency, factor 5 excess with spontaneous thrombosis, thrombophilia), which are all coagulation-related and likely cluster together by graph proximity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for antithrombin deficiency type 2.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005036 (status: cancelled) | Elahere | Not specified | Monotherapy for adult patients with folate receptor-alpha (FRα) positive, platinum-resistant high grade serous epithelial ovarian, fallopian tube, or primary peritoneal cancer who have received one to three prior systemic treatment regimens. |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate delivering a cytotoxic microtubule inhibitor (maytansinoid DM4) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions; ophthalmic (corneal) monitoring is relevant given the ocular toxicity noted for this drug |
| Handling Protection | Please refer to the SmPC warnings and precautions; follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug-specific toxicity**: Ocular (corneal) toxicity has been reported with this drug. It can be resolved with short-term topical steroid administration.
- **Drug Interactions**: The interaction query completed, but the only entry is the drug's pharmacological target (FRα), not an interacting drug. No clinically relevant drug-drug interactions were identified in the compiled data.

For other safety information, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications, and there is no plausible mechanistic link between an FRα-targeted cytotoxic ADC and a qualitative coagulation-inhibitor defect. In addition, the only EU authorization is cancelled, and cytotoxic exposure would carry significant risk for a non-malignant condition.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and label-based warnings and contraindications from the SmPC
- Any biological evidence linking FRα or the DM4 payload to antithrombin or *SERPINC1* biology
- Preclinical data supporting efficacy in this condition
- A review of other predicted indications (for example, gynaecologic or FRα-expressing malignancies), which may be better candidates than the coagulation-related predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

