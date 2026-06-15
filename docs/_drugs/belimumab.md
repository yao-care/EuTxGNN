---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Belimumab
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab (Benlysta) is a human monoclonal antibody that inhibits BLyS/BAFF, globally approved for the treatment of Systemic Lupus Erythematosus (SLE) — though not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets** with a prediction score of 99.96%;
however, only **1 clinical trial** (indirectly related, relevance grade C) and **no supporting publications** have been identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic Lupus Erythematosus (SLE) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DrugBank query flagged as a data gap). Based on well-established pharmacological knowledge, Belimumab is a human IgG1λ monoclonal antibody that selectively inhibits B-lymphocyte stimulator (BLyS, also known as BAFF) — a cytokine essential for B cell survival, maturation, and differentiation into autoantibody-producing plasma cells. By blocking BLyS, belimumab reduces circulating B cells and pathogenic autoantibody titres, which is the mechanistic basis for its efficacy in SLE and lupus nephritis.

Primary release disorder of platelets refers to defects in platelet alpha-granule or dense-granule secretion upon activation. The BLyS/BAFF pathway has no established direct role in platelet granule biology or megakaryocyte function. There is no preclinical evidence linking BAFF inhibition to improved platelet granule release. The TxGNN model likely inferred this association through indirect immunomodulatory nodes in its knowledge graph — for instance, shared inflammatory signalling between B cells and platelet-activating pathways — rather than a well-defined mechanistic relationship.

While immune dysregulation can secondarily affect platelet function (e.g., autoantibody-mediated platelet damage in immune thrombocytopenia), primary release disorder of platelets is fundamentally a granule biology defect, not an autoantibody-driven process. The mechanistic connection to belimumab's anti-BAFF action remains speculative and currently unsupported by any direct clinical or laboratory evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Open-label mechanistic study of belimumab (10 mg/kg IV at weeks 0, 2, then every 4 weeks for 24 weeks) in patients with PLA2R autoantibody-positive idiopathic membranous glomerulonephropathy. Evaluated efficacy, safety, and biomarker/autoantibody relationships. This trial targets a renal autoimmune indication and has no direct relevance to platelet release disorders (relevance grade C). |

> **Important caveat:** The only retrieved trial addresses idiopathic membranous glomerulonephropathy, a renal autoimmune condition. Its presence in this evidence set likely reflects algorithmic over-retrieval rather than a meaningful disease connection.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.96%), there is zero direct clinical or preclinical evidence supporting belimumab for primary release disorder of platelets, and the mechanistic rationale is not established — the BLyS/BAFF pathway has no known role in platelet granule secretion biology.

**To proceed, the following is needed:**

- **Mechanistic validation:** Preclinical studies (in vitro platelet aggregation/secretion assays, animal models) to determine whether BAFF inhibition affects platelet granule function
- **Knowledge graph audit:** Review whether the high TxGNN score reflects a genuine biological connection or a graph topology artefact (e.g., spurious immunomodulatory node proximity)
- **Safety assessment:** Retrieve full SmPC/TFDA labelling to document key warnings, contraindications, and pregnancy category (known concern given belimumab's pregnancy category C and neonatal B cell depletion risk)
- **MOA data retrieval:** Complete the DrugBank API query (flagged as data gap DG002) to enable formal mechanism-of-action analysis

---

> **Note on higher-priority signal:** Among all 10 predicted indications in this evidence pack, **Inflammatory Bowel Disease (IBD, rank 9)** carries meaningfully stronger evidence (Evidence Level L4; 2 clinical trials and 9 publications), with a well-documented mechanistic rationale: BAFF/BLyS is upregulated in IBD mucosa, and B cells play a documented role in intestinal inflammation. Investigators may wish to prioritise IBD as a more tractable repurposing hypothesis for belimumab ahead of platelet release disorders.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

