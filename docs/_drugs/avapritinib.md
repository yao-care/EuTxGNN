---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: From GIST / Systemic Mastocytosis to Axial Spondylometaphyseal Dysplasia

> **Note:** Avapritinib carries no EU/Taiwan marketing authorization. Original indications referenced above are based on FDA approval status and contextual information within this Evidence Pack (repurposing_rationale identifies it as a PDGFRA/KIT inhibitor). EU regulatory data is unavailable.

---

## One-Sentence Summary

Avapritinib is a selective KIT and PDGFRA receptor tyrosine kinase inhibitor, approved by the FDA for PDGFRA exon 18-mutant gastrointestinal stromal tumors (GIST) and indolent systemic mastocytosis, but holding no marketing authorization in the EU or Taiwan.
The TxGNN model predicts it may have activity in **Axial Spondylometaphyseal Dysplasia**,
however, **no clinical trials and no publications** currently support this direction — this remains a pure AI-derived prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in EU/Taiwan (FDA-approved: PDGFRA exon 18-mutant GIST; indolent systemic mastocytosis) |
| Predicted New Indication | Axial Spondylometaphyseal Dysplasia |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on information embedded in the repurposing rationale, Avapritinib is a potent and selective inhibitor of KIT and PDGFRA — two receptor tyrosine kinases that, when constitutively activated by somatic mutations, drive diseases such as GIST and systemic mastocytosis.

The theoretical mechanistic link to axial spondylometaphyseal dysplasia rests on one observation: PDGFRA is expressed in chondrocytes and plays a documented role in skeletal development. PDGFR signaling participates in endochondral ossification, meaning that modulating this pathway could, in principle, affect bone and cartilage biology.

However, axial spondylometaphyseal dysplasia is a **genetic developmental disorder** — a structural defect arising from germline mutations affecting bone formation during embryogenesis — rather than a disease driven by aberrant kinase activation. There is no known kinase-activating mechanism underlying this condition, and PDGFRA inhibition has no established or proposed therapeutic role in skeletal dysplasia. The mechanistic connection is considered extremely weak, and the high TxGNN score likely reflects a statistical graph-embedding association rather than a clinically actionable biological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Avapritinib is a targeted oncology agent (KIT/PDGFRA inhibitor) used in GIST and mastocytosis and meets the antineoplastic criterion for this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective KIT/PDGFRA tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | CBC with differential, liver function tests, renal function; intracranial hemorrhage surveillance per SmPC |
| Handling Protection | Follow institutional protocols for oral targeted therapy handling |

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(All available safety fields — key warnings, contraindications, and drug–drug interactions — returned no data for this Evidence Pack. TFDA package insert data is identified as a blocking gap [DG001].)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure AI model prediction (L5) with zero supporting clinical trials or published literature, and the proposed mechanistic link — PDGFRA inhibition in a germline skeletal developmental disorder — is biologically implausible. No further development steps are justified until critical data gaps are resolved.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): Obtain EU SmPC / local package insert data to enable a safety pre-screen (S1 gate)
- Resolve DG002 (High): Retrieve full MOA data from DrugBank API to confirm kinase target profile
- Commission a targeted literature review on PDGFRA/KIT expression in axial spondylometaphyseal dysplasia and related skeletal dysplasias — absence of evidence must be confirmed, not assumed
- Reassess against higher-ranked, biologically plausible candidates in this batch (e.g., Ranks 3/5/7: ALS-spectrum diseases with documented KIT+ mast cell neuroinflammation rationale) before allocating further resources to Rank 1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

