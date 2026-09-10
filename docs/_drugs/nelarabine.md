---
layout: default
title: Nelarabine
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Nelarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Nelarabine: From T-cell Acute Lymphoblastic Leukemia to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine is a purine nucleoside antimetabolite originally used to treat T-cell acute lymphoblastic leukemia (T-ALL) and T-cell lymphoblastic lymphoma (T-LBL).
The TxGNN model predicts it may be effective for **Relapsing-Remitting Multiple Sclerosis (RRMS)**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying rationale flags a direct mechanistic contradiction with the drug's known neurotoxicity profile.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | T-cell acute lymphoblastic leukemia (T-ALL) / T-cell lymphoblastic lymphoma (T-LBL) (per literature record; no local marketing authorization data available) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nelarabine is not available in the current dataset. Based on information found in the supporting literature within this evidence pack, nelarabine is a prodrug that is converted to ara-GTP and acts as a T-cell-selective DNA synthesis inhibitor, exploiting the high deoxycytidine kinase (dCK) to adenosine deaminase/purine nucleoside phosphorylase (ADA:PNP) ratio characteristic of malignant T-lymphoblasts. This selective T-cell cytotoxicity underlies its approved use in T-ALL/T-LBL.

However, the relationship between this cytotoxic mechanism and RRMS runs in the opposite direction of what MS therapy requires. RRMS management centers on immune modulation and myelin protection, whereas nelarabine carries a known black-box warning for severe neurotoxicity, including demyelinating lesions and encephalopathy. Applying a drug whose principal dose-limiting toxicity is demyelination/CNS injury to a demyelinating autoimmune disease is mechanistically contradictory rather than merely under-evidenced — this is explicitly noted in the model's own repurposing rationale.

For this reason, despite a high TxGNN similarity score, this candidate does not represent a biologically plausible repurposing direction and should not be interpreted as a promising lead without independent confirmatory evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Nelarabine currently has no marketing authorization in this jurisdiction (market status: Not Marketed; total licenses: 0). No product-level data is available for reporting.

## Cytotoxicity

Nelarabine is an antineoplastic agent (purine nucleoside antimetabolite; approved for T-ALL/T-LBL), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Purine nucleoside antimetabolite; same class as fludarabine, cladribine) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count (CBC), neurological examination (given the drug's known severe neurotoxicity profile), liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: The repurposing rationale for this candidate independently flags that nelarabine carries a known black-box warning for severe neurotoxicity (demyelinating lesions, encephalopathy), which is directly relevant to evaluating its use in a demyelinating disease context such as RRMS.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (L5, model prediction only), and the proposed mechanism runs counter to nelarabine's known neurotoxic/demyelinating liability — a direct conflict with the therapeutic goal in RRMS. There is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Formal mechanism-of-action (MOA) data for nelarabine from DrugBank or the manufacturer
- TFDA/EMA-equivalent labeling data on warnings, contraindications, and neurotoxicity (currently a blocking data gap per this evidence pack)
- Preclinical evidence specifically addressing whether any subpopulation-selective immunomodulatory effect could offset the demyelination risk in an autoimmune CNS disease model
- Independent expert (neurology/oncology) review before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

