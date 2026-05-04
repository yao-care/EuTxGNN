---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Ipilimumab
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

# Ipilimumab: From Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab is an anti-CTLA-4 monoclonal antibody checkpoint inhibitor, globally recognized as a standard treatment for melanoma and several other solid tumors, though it is currently not approved in Taiwan.
The TxGNN model predicts it may be effective for **Choroideremia** with a prediction score of **99.06%**; however, this prediction is supported by **no clinical trials** and **no published literature**, placing it at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not approved in Taiwan — no regulatory data available |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ipilimumab (Yervoy) is a fully human IgG1 monoclonal antibody that binds and blocks CTLA-4, a co-inhibitory receptor expressed on activated T-cells. By removing this checkpoint "brake," ipilimumab allows cytotoxic T-cells to mount a more sustained anti-tumor immune response. This mechanism underpins its regulatory approvals for melanoma, renal cell carcinoma, MSI-H colorectal cancer, and hepatocellular carcinoma in major markets. The drug's entire therapeutic rationale rests on immune system re-activation in the oncology setting.

Choroideremia, however, is a fundamentally different disease category. It is an X-linked recessively inherited retinal dystrophy caused by loss-of-function mutations in the *CHM* gene, which encodes Rab Escort Protein 1 (REP1). The resulting defect in vesicle trafficking leads to progressive, irreversible degeneration of the retinal pigment epithelium and photoreceptors — a cell-autonomous, genetically driven process. No established link exists between CTLA-4 checkpoint signaling and CHM-related photoreceptor degeneration.

The high TxGNN score almost certainly reflects indirect topological proximity in the knowledge graph — for example, shared nodes related to retinal pigment epithelium biology or broad immune cell annotations — rather than a true biological or pharmacological relationship. This is a recognized limitation of graph-based AI predictions: high connectivity does not equal mechanistic plausibility. Without any preclinical signal or published hypothesis connecting CTLA-4 blockade to genetic retinal disease, advancing this candidate is not warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Ipilimumab is an antineoplastic immunotherapy; it is **not** a conventional cytotoxic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-CTLA-4 checkpoint inhibitor (monoclonal antibody); not a conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low (no direct bone marrow suppression; immune-related cytopenias such as immune thrombocytopenia are rare but reported) |
| Emetogenicity Classification | Minimal (IV infusion; nausea is not a primary toxicity concern) |
| Monitoring Items | Liver function tests (LFTs), thyroid function, cortisol/ACTH axis, CBC with differential, serum creatinine, fasting glucose; broad immune-related adverse event (irAE) surveillance required |
| Handling Protection | Standard biologic/monoclonal antibody handling procedures apply; does not require cytotoxic chemotherapy containment protocols |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting ipilimumab's use in choroideremia, and the drug's established mechanism — CTLA-4 immune checkpoint blockade — has no known relevance to the CHM gene mutation-driven, cell-autonomous retinal degeneration that defines this condition. This prediction is assessed as a knowledge graph topological artifact rather than a biologically plausible repurposing candidate.

**To proceed, the following would be needed:**
- Demonstration of an immune or inflammatory component in choroideremia pathogenesis that could plausibly be modulated by CTLA-4 blockade
- Preclinical evidence (animal model or in vitro) linking CTLA-4 signaling to REP1 deficiency or retinal pigment epithelium survival
- Any published hypothesis or mechanistic rationale connecting immune checkpoint regulation to inherited retinal dystrophies
- Retrieval of detailed MOA and safety data from DrugBank to complete the drug-level characterization (currently data gap)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

