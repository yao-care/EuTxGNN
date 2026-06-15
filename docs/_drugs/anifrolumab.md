---
layout: default
title: Anifrolumab
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to Diabetic Cataract

## One-Sentence Summary

Anifrolumab (Saphnelo) is an anti-IFNAR1 monoclonal antibody that blocks type I interferon signaling, approved in the US and EU for moderate-to-severe systemic lupus erythematosus (SLE), though not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, with **0 clinical trials** and **0 publications** directly supporting this direction.
Critically, all top 10 predictions cluster around cataract subtypes with near-identical scores, raising a high-confidence concern that these reflect knowledge graph propagation artifacts rather than genuine mechanistic opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic Lupus Erythematosus (SLE) — moderate-to-severe (US/EU approved; not marketed in Taiwan) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not yet available for this analysis. From publicly known information, Anifrolumab is an anti-IFNAR1 monoclonal antibody that competitively blocks the type I interferon receptor subunit 1, thereby suppressing all downstream type I interferon (IFN-α, IFN-β, IFN-ω) signaling. Its efficacy in SLE is well-established because type I interferons are central pathogenic drivers of lupus flares. The drug is administered as an intravenous infusion every four weeks.

Diabetic cataract arises from lens protein oxidation, glycation, and activation of the polyol (aldose reductase) pathway under chronic hyperglycemia — none of which are directly downstream of IFNAR1. There is no established biological pathway by which blocking type I interferon signaling would reduce lens opacification. The proposed indirect connection, supported by the evidence pack's mechanistic analysis, is that SLE patients receiving long-term corticosteroids face an elevated steroid-induced cataract risk; this creates KG edges linking Anifrolumab → SLE → corticosteroid use → cataract. This reflects a confounded association, not therapeutic potential.

The most important red flag in this prediction set is the **score identity pattern**: six distinct cataract subtypes (mature, immature, tetanic, diabetes mellitus type 2 associated, craniostenosis, and cortical cataracts at ranks 2–6) all share an identical TxGNN score of 0.9842435121536256 — identical to 16 decimal places across biologically unrelated disease entities. Genuine biological predictions would produce distinct scores. This pattern is characteristic of a knowledge graph batch propagation artifact, where a cluster of disease nodes inherits scores from a shared upstream node rather than from drug-specific mechanistic modeling. The appearance of tetanic cataract (caused by hypocalcemia-induced lens metabolic failure) and craniostenosis cataract (caused by elevated intracranial pressure during skull development) — both entirely unrelated to immune signaling — further confirms this is a KG artifact rather than a real repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the primary predicted indication (diabetic cataract).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The entire top-10 prediction cluster for Anifrolumab consists of cataract subtypes where multiple entries share mathematically identical TxGNN scores — a pattern conclusively indicating knowledge graph propagation artifacts. No clinical trials or disease-specific literature exist to support Anifrolumab as a cataract treatment, and the mechanistic link between IFNAR1 blockade and lens opacification is absent. Proceeding with this prediction would not represent a credible repurposing opportunity.

**To proceed, the following is needed:**
- **KG path audit**: Manually trace the knowledge graph path connecting Anifrolumab to cataract nodes to confirm the confound (SLE → corticosteroid → cataract) and formally classify as an artifact
- **Taiwan SmPC safety data**: Currently blocked (DG001, Blocking severity) — TFDA SmPC must be retrieved before any safety evaluation can proceed
- **MOA data from DrugBank** (DG002): Needed if mechanistic re-analysis is required for future non-artifact predictions
- **Alternative indication triage**: If continuing Anifrolumab repurposing evaluation, diabetic retinopathy (rank 10, score 98.19%) warrants separate assessment — it has a more plausible (though uncertain) mechanistic rationale via IFN-driven retinal inflammation, and the direction-of-effect question should be investigated before any clinical hypothesis is formed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

