---
layout: default
title: Axicabtagene Ciloleucel
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Axicabtagene Ciloleucel
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

# Axicabtagene Ciloleucel: From Large B-Cell Lymphoma to Crohn's Colitis

## One-Sentence Summary

Axicabtagene ciloleucel (Yescarta) is an autologous CD19-directed CAR-T cell therapy, internationally approved for relapsed or refractory large B-cell lymphoma, but not currently registered in Taiwan.
The TxGNN model predicts it may be applicable to **Crohn's Colitis**, ranking it first among predicted new indications with a score of **91.39%**.
However, **no clinical trials or publications** currently support this specific combination, making this a purely model-driven prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Large B-Cell Lymphoma (international approval; not registered in Taiwan) |
| Predicted New Indication | Crohn's Colitis |
| TxGNN Prediction Score | 91.39% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Axicabtagene ciloleucel (Yescarta) is an autologous, ex vivo-engineered CAR-T cell therapy targeting the CD19 antigen expressed on the surface of B cells. It works by reprogramming the patient's own T cells to recognize and eliminate CD19-positive cells, achieving deep and durable B-cell depletion. This mechanism has been clinically validated in aggressive B-cell malignancies — most notably diffuse large B-cell lymphoma (DLBCL), primary mediastinal large B-cell lymphoma, and follicular lymphoma.

The link to Crohn's colitis rests on the role B cells play in intestinal inflammation. CD19⁺ B cells residing in the gut-associated lymphoid tissue (GALT) and intestinal mucosa produce pro-inflammatory cytokines (IL-6, TNF-α) and disease-associated autoantibodies that sustain chronic mucosal injury. By eliminating this B-cell compartment, CD19 CAR-T therapy could theoretically interrupt a key amplification loop in Crohn's disease pathogenesis. Critically, a 2024 proof-of-concept published by Schett et al. demonstrated that CD19-directed CAR-T cells (using a different CAR-T product, not axi-cel) can induce drug-free remission in refractory systemic autoimmune diseases — including systemic lupus erythematosus and systemic sclerosis — extending the therapeutic concept beyond oncology.

That said, the mechanistic plausibility for Crohn's colitis specifically is rated **moderate at best**. Crohn's disease is predominantly driven by T-cell dysregulation (Th1/Th17 pathways, innate immune activation), with B cells playing a supporting rather than primary role. No clinical data exist for axi-cel — or any CD19 CAR-T product — in inflammatory bowel disease specifically. This prediction remains firmly in hypothesis-generating territory and should not be advanced without prospective mechanistic and safety evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Axicabtagene ciloleucel is **not registered** with the Taiwan Food and Drug Administration (TFDA) and has no issued marketing authorizations. No Taiwan-specific prescribing information (仿單) is available.

---

## Cytotoxicity

Axicabtagene ciloleucel is an antineoplastic immunotherapy indicated for large B-cell lymphoma. This section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy — autologous CAR-T cell therapy (adoptive cell transfer) |
| Myelosuppression Risk | High — significant cytopenias (neutropenia, thrombocytopenia, anemia) result from the mandatory lymphodepleting conditioning regimen (fludarabine + cyclophosphamide) administered prior to infusion; prolonged cytopenias lasting weeks are common |
| CRS / ICANS Risk | High — cytokine release syndrome (CRS) and immune effector cell-associated neurotoxicity syndrome (ICANS) are the primary serious adverse events; Grade ≥3 CRS observed in approximately 13–22% of patients in pivotal trials |
| Monitoring Items | CBC with differential (daily during hospitalization and frequently post-discharge), ferritin, CRP, cytokine panels, neurological assessments, vital signs; monitor for at least 4 weeks at certified treatment center |
| Handling Protection | Cryopreserved gene-modified cell therapy product; requires certified treatment center, chain-of-custody documentation, and specialized thawing procedures; follow institutional cell therapy and REMS program protocols |

---

## Safety Considerations

Taiwan-specific prescribing information is unavailable as the drug is not registered with the TFDA. Based on international labeling, key safety signals include:

- **Cytokine Release Syndrome (CRS)**: Potentially fatal; ranges from fever and hypotension to life-threatening multiorgan dysfunction; managed with tocilizumab and corticosteroids per institutional protocol
- **Neurological Toxicity (ICANS)**: Includes encephalopathy, aphasia, seizure, and cerebral edema; requires REMS (Risk Evaluation and Mitigation Strategy) enrollment in the United States
- **Prolonged Cytopenias**: Resulting from lymphodepleting conditioning; increases risk of serious infections including bacterial, viral, and fungal pathogens
- **Hypogammaglobulinemia**: Consequence of sustained B-cell aplasia; may require immunoglobulin replacement therapy

Please refer to the full prescribing information (SmPC / US PI) for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies Crohn's colitis as the highest-ranked new indication for axicabtagene ciloleucel, grounded in a biologically coherent — if mechanistically secondary — role for B-cell depletion in intestinal inflammation. However, with zero supporting clinical trials or publications, an all-L5 evidence base, a drug not registered in Taiwan, and a serious toxicity profile requiring highly specialized delivery infrastructure, there is no basis to advance this candidate toward clinical development at this time.

**To proceed, the following is needed:**

- **Clinical signal generation**: Identify published or ongoing studies of any CD19 CAR-T product (not necessarily axi-cel) in Crohn's disease or other inflammatory bowel diseases; assess whether the Schett 2024 autoimmune framework is being extended to IBD
- **Mechanistic validation**: Quantify the relative contribution of B cells vs. T cells and innate immunity in the specific Crohn's colitis subtype targeted; determine whether gut GALT B-cell depletion is achievable and durable with systemic CAR-T infusion
- **Regulatory prerequisite**: Obtain TFDA prescribing information (仿單) to complete Taiwan-specific safety screening and determine whether compassionate use or clinical trial pathways are feasible
- **Feasibility assessment**: Evaluate T-cell collection adequacy in refractory Crohn's patients (who may be on immunosuppressants affecting T-cell quality), manufacturing logistics, and treatment center certification requirements in Taiwan
- **Signal prioritization review**: Note that 9 of the 10 top TxGNN predictions for this drug carry significant mechanistic concerns — several target diseases (mastocytosis, HER2⁺ breast cancer, multiple endocrine neoplasia) whose tumor cells do not express CD19 at all, suggesting the model may be pattern-matching on graph proximity rather than true biological relevance; rheumatoid vasculitis (Rank 10) carries the strongest mechanistic rationale among the non-Crohn's predictions and may warrant parallel evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

