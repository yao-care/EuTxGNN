---
layout: default
title: Artesunate
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Artesunate
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

# Artesunate: From Malaria to Acne

## One-Sentence Summary

Artesunate is a semisynthetic artemisinin derivative derived from *Artemisia annua*, widely used as a first-line treatment for severe and cerebral malaria due to its rapid parasiticidal action via reactive oxygen species generation.
The TxGNN model predicts it may have potential activity against **Acne (disease)**, likely through NF-κB-mediated suppression of *Cutibacterium acnes*-driven sebaceous gland inflammation.
Currently, **no clinical trials** and **no published literature** directly support this specific repurposing direction — this is a pure model prediction at L5 evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (severe/cerebral malaria) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 79.21% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Artesunate is a water-soluble hemisuccinate ester of dihydroartemisinin. Its core mechanism involves the endoperoxide bridge reacting with ferrous heme iron inside infected erythrocytes to generate carbon-centred free radicals and reactive oxygen species (ROS) that are lethal to *Plasmodium* parasites. Beyond this antiparasitic action, artesunate has demonstrated secondary anti-inflammatory activity through inhibition of the NF-κB signalling pathway and downregulation of pro-inflammatory mediators including IL-1β, IL-6, and TNF-α. Detailed pharmacological MOA data from DrugBank was not available at the time of this assessment; the description above is based on published literature.

Acne vulgaris is fundamentally an inflammatory disease of the pilosebaceous unit. *Cutibacterium acnes* activates TLR2 and the NLRP3 inflammasome, driving NF-κB-dependent production of pro-inflammatory cytokines in sebaceous glands, leading to follicular hyperkeratosis and comedone formation. Artesunate's capacity to inhibit NF-κB could theoretically attenuate this specific inflammatory cascade — offering a mechanistically plausible alternative to antibiotics (facing increasing resistance) or isotretinoin (with significant teratogenicity risk).

The TxGNN score of 79.21% reflects indirect pathway associations in the drug-disease knowledge graph, most likely through shared inflammatory signalling nodes. However, no validated in vitro sebocyte experiments or animal acne models using artesunate have been identified in this dataset. The mechanistic hypothesis is biologically coherent but entirely unverified. Notably, artesunate also ranks highly for a cluster of mastocytosis indications (ranks 2, 3, 5) and diffuse cutaneous leishmaniasis (rank 6) — the leishmaniasis prediction carries particularly strong mechanistic rationale given artesunate's known broad-spectrum anti-protozoal activity and may warrant prioritisation alongside or ahead of the acne indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Artesunate in acne.

---

## Literature Evidence

Currently no related literature available for Artesunate in acne.

---

## Taiwan Market Information

Artesunate is not currently registered or marketed in Taiwan. No marketing authorizations are on file (0 licenses). WHO prequalified injectable artesunate formulations exist internationally for severe malaria, but no TFDA approval has been recorded in this dataset.

---

## Safety Considerations

TFDA labelling data (warnings and contraindications) was not available at the time of this assessment. Drug interaction data returned no results from the DDI database query.

Please refer to the WHO/manufacturer's product information for complete safety information, including known risks such as post-treatment haemolysis in non-immune patients receiving IV artesunate for severe malaria.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on TxGNN's mechanistic inference with no supporting clinical trials or literature (L5), and the mechanistic link between artesunate's NF-κB inhibition and acne pathophysiology, while plausible, requires in vitro proof-of-concept before any further development commitment is justified.

**To proceed, the following is needed:**
- **In vitro proof-of-concept**: Test artesunate against *C. acnes*-stimulated sebocyte cell lines (e.g., SZ95 cells) measuring IL-1β, IL-6, and NF-κB reporter activity
- **Literature re-sweep**: Confirm no relevant publications were missed — search PubMed for `"artesunate" AND ("acne" OR "sebocyte" OR "Propionibacterium" OR "Cutibacterium")`
- **Prioritise competing indications**: The leishmaniasis (rank 6) and mastocytosis cluster (ranks 2, 3, 5) predictions carry stronger mechanistic rationale and may represent higher-value research questions; consider whether acne is the optimal lead indication for this molecule
- **TFDA SmPC retrieval**: Obtain full prescribing information to complete safety profiling and identify contraindicated populations
- **DrugBank MOA data**: Retrieve complete pharmacology record (DB09274) to formalise the mechanistic link assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

