---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: From Plaque Psoriasis to Strongyloidiasis

## One-Sentence Summary

Brodalumab is a human monoclonal antibody targeting IL-17 receptor A (IL-17RA), globally approved for moderate-to-severe plaque psoriasis but not currently marketed in Taiwan.

The TxGNN model ranks **strongyloidiasis** as its top predicted new indication (score 99.84%); however, this prediction carries a **critical mechanistic red flag** — IL-17/Th17 immunity is the host's primary defense against helminth infections, meaning IL-17RA blockade would theoretically worsen rather than treat this disease.

There are **no clinical trials and no publications** supporting Brodalumab in strongyloidiasis; the second-ranked prediction, **eye disease** (99.82%), holds greater biological plausibility with emerging IL-17 pathway evidence in ocular inflammation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan (globally: moderate-to-severe plaque psoriasis) |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on publicly known information, Brodalumab is a fully human monoclonal antibody that binds to interleukin-17 receptor A (IL-17RA), blocking signaling from multiple IL-17 family cytokines — including IL-17A, IL-17F, IL-17C, and IL-17E (IL-25). This broad receptor-level blockade distinguishes Brodalumab from IL-17A–selective agents such as secukinumab and ixekizumab. It is this mechanism that drives its efficacy in psoriasis, where excessive Th17 activity underlies chronic skin inflammation.

**Regarding the strongyloidiasis prediction — the mechanistic direction is reversed.** The IL-17/Th17 axis is a critical arm of host immunity against extracellular pathogens, including *Strongyloides stercoralis*. Blocking IL-17RA would be expected to impair parasite clearance and significantly increase the risk of strongyloidiasis hyperinfection syndrome — a life-threatening complication. From a pharmacological standpoint, this indication is not merely unsupported; it is a potential contraindication. The TxGNN high score most likely reflects a non-specific association through shared "inflammation" nodes in the knowledge graph, constituting a false positive.

For reference, the second-ranked prediction — **eye disease** — carries substantially more biological plausibility. IL-17 signaling has a documented role in ocular autoimmune inflammation (uveitis, scleritis, episcleritis), and class-level evidence exists for other IL-17–targeting agents in these contexts. Brodalumab's broader IL-17RA blockade profile may have distinct effects from IL-17A–selective agents, which themselves carry a paradoxical uveitis safety signal. This direction is worth pursuing as a research question, even if direct clinical evidence for Brodalumab is currently absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brodalumab in strongyloidiasis.

---

> **Supplementary — Eye Disease (Rank 2, Score 99.82%):** The following trial appeared when querying Brodalumab against eye disease; it does not directly evaluate Brodalumab as an ocular intervention.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Observational biomarker profiling of six immune-mediated inflammatory skin diseases (including psoriasis and atopic dermatitis) in real-world practice. Not a Brodalumab intervention trial; relevance to eye disease is indirect, limited to background IL-17 biology in inflammatory skin–eye overlap conditions. |

---

## Literature Evidence

Currently no related literature available for Brodalumab in strongyloidiasis.

---

> **Supplementary — Eye Disease (Rank 2):** The following review provides mechanistic background relevant to IL-17 blockade in rheumatic and ocular inflammatory disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32993066](https://pubmed.ncbi.nlm.nih.gov/32993066/) | 2020 | Review | Int J Mol Sci | Comprehensive overview of IL-17 blockade strategies in systemic rheumatic diseases. Discusses the immunological rationale for targeting the IL-17 axis in autoimmune inflammation, providing background context for potential ocular applications. Not specific to Brodalumab or strongyloidiasis. |

---

## Taiwan Market Information

Brodalumab is currently not marketed in Taiwan. No marketing authorizations are on record in the Taiwan regulatory database (total licenses: 0).

---

## Safety Considerations

Please refer to the SmPC (or global prescribing information such as the FDA label for Siliq®) for complete safety information.

> **Clinically important note in the context of this prediction:** Given Brodalumab's mechanism (IL-17RA blockade), use in patients with active or undetected *Strongyloides* infection would be expected to suppress the very immune pathway needed to control parasite burden. Screening for strongyloidiasis prior to initiating any IL-17 pathway inhibitor is a standard precaution — the TxGNN prediction pointing toward *strongyloidiasis as an indication* is mechanistically inverted from this established clinical concern.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (strongyloidiasis) is a likely false positive — blocking IL-17RA is mechanistically contraindicated in parasitic helminth infection rather than therapeutic, and zero clinical or preclinical evidence supports this indication. Brodalumab has no Taiwan marketing authorization, providing no regulatory foundation to build on.

**To proceed with any evaluation, the following is needed:**

- Obtain formal MOA documentation via DrugBank API (currently marked as Data Gap)
- Retrieve TFDA prescribing information or global SmPC for complete safety and contraindication data
- For the more biologically plausible **eye disease** prediction (rank 2): conduct a targeted literature search for Brodalumab in uveitis, scleritis, and related ocular inflammatory conditions — and review the class-level safety signal of paradoxical uveitis with IL-17 inhibitors
- Consider flagging strongyloidiasis (and similar anti-parasitic/anti-helminth indications) as a systematic false positive class for immunosuppressants acting on the IL-17 axis, to improve the knowledge graph's specificity for future predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

