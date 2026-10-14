---
layout: default
title: Panitumumab
parent: AI Predictions (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
---

# Panitumumab
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

# Panitumumab: From Metastatic Colorectal Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Panitumumab is an anti-EGFR monoclonal antibody, originally used to treat RAS wild-type metastatic colorectal cancer.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction is computational only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adult patients with wild-type RAS metastatic colorectal cancer (mCRC): first-line with FOLFOX or FOLFIRI; second-line with FOLFIRI after first-line fluoropyrimidine-based chemotherapy (excluding irinotecan); or as monotherapy after failure of fluoropyrimidine-, oxaliplatin-, and irinotecan-containing regimens |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization in the compiled data) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, panitumumab is an anti-EGFR (epidermal growth factor receptor) monoclonal antibody. Its efficacy in RAS wild-type metastatic colorectal cancer has been established, which is how it came to be authorized.

The link to drug-induced osteoporosis is speculative. In preclinical settings, EGFR signaling has a role in osteoblast differentiation and bone remodeling, so a theoretical connection exists. However, no clinical or literature evidence was provided to support it, and the relationship between a colorectal cancer therapy and a bone-loss condition has not been characterized. The high TxGNN score (0.991) reflects a graph-based computational prediction, not an experimentally confirmed finding.

Other predicted indications in the same analysis (diabetic retinopathy and several cataract subtypes) also have no supporting evidence. Identical scores across cataract subtypes suggest a class-level knowledge graph signal rather than independent findings.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000741 (cancelled) | Vectibix | Not specified | Vectibix is indicated for the treatment of adult patients with wild-type RAS metastatic colorectal cancer (mCRC): in first-line in combination with Folfox or Folfiri. in sec... |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 27 interactions were identified in total (the 20 listed in the data compiled for this report include the following). Major-level interactions include:
  - **Bevacizumab**
  - **Irinotecan** and **liposomal irinotecan**
  - QT-prolonging or antiarrhythmic agents: **amiodarone, dofetilide, dronedarone, droperidol, levacetylmethadol, arsenic trioxide**
  - **Aminolevulinic acid**
- Moderate-level interactions include proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), methoxsalen, topical aminolevulinic acid, disopyramide, and idelalisib.
- **Context from the prediction analysis**: Systemic EGFR blockade is known to carry ocular and dermatologic toxicities, and panitumumab can cause hypomagnesemia and hypocalcemia. These are relevant when considering any new use.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no registered clinical trials and no publications. The EU authorization in the data is cancelled, and mechanism of action, warnings, and contraindications are missing.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Warnings and contraindications from the EMA product information, to allow safety screening
- Preclinical or mechanistic studies of EGFR blockade in bone remodeling and osteoporosis models
- A literature and trial search specific to drug-induced osteoporosis
- Verification of the current EU marketing status of Vectibix, since only a cancelled authorization is recorded
- A risk-benefit assessment, given systemic EGFR-inhibitor toxicity and the availability of established osteoporosis therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

