---
layout: default
title: Isatuximab
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Isatuximab
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

The txgnn-pipeline skill covers pipeline operations; the report format is fully specified in my system prompt. Proceeding with the report generation.

---

# Isatuximab: From Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Isatuximab (Sarclisa) is an anti-CD38 monoclonal antibody approved for relapsed/refractory multiple myeloma in major markets.
The TxGNN model predicts it may be effective for **Indolent Plasma Cell Myeloma** — an earlier stage on the same plasma cell dyscrasia spectrum — with a prediction score of **98.23%**.
However, only **2 publications** are currently available, both of which are case reports about infusion desensitization rather than direct efficacy evidence for this indication, placing the overall evidence at **L4 (mechanistic/preclinical level)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma (relapsed/refractory) |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Isatuximab is a monoclonal antibody that specifically targets CD38, a transmembrane glycoprotein and ectoenzyme that is constitutively and highly expressed on the surface of plasma cells. In multiple myeloma, isatuximab binding to CD38 triggers tumour cell death through multiple mechanisms, including antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and direct pro-apoptotic signalling.

The key mechanistic rationale for this prediction is that plasma cell disorders exist on a continuous biological spectrum — from MGUS (monoclonal gammopathy of undetermined significance) → smouldering/indolent myeloma → active multiple myeloma. CD38 is highly expressed at every stage of this continuum, not just at the symptomatic end. Indolent plasma cell myeloma (also referred to as smouldering multiple myeloma, SMM) shares the same cellular identity and surface marker profile as active MM, making the CD38-targeting mechanism directly applicable in principle.

This mechanistic connection is strong and biologically coherent. In fact, the clinical field is already actively exploring early intervention in high-risk SMM using daratumumab (a structurally related anti-CD38 mAb), which further validates the class-level plausibility. However, it is important to note that the benefit of treating indolent/smouldering disease — before it progresses to symptomatic MM — remains an ongoing research question with distinct risk-benefit considerations from active MM.

---

## Clinical Trial Evidence

Currently no clinical trials registered for Isatuximab in indolent plasma cell myeloma.

> **Note:** Trials of the related anti-CD38 agent daratumumab in smouldering multiple myeloma (e.g., AQUILA, NCT03301220) provide indirect class-level support, but direct isatuximab trials in this indication are absent.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38275249](https://pubmed.ncbi.nlm.nih.gov/38275249/) | 2024 | Letter / Reply | J Investig Allergol Clin Immunol | Reply regarding successful isatuximab desensitization in a patient with refractory multiple myeloma who also had indolent systemic mastocytosis |
| [38888584](https://pubmed.ncbi.nlm.nih.gov/38888584/) | 2024 | Case Report | J Investig Allergol Clin Immunol | Successful isatuximab desensitization protocol in a patient with refractory multiple myeloma and concurrent indolent systemic mastocytosis |

> ⚠️ **Evidence Quality Note:** Both publications describe hypersensitivity management (desensitization), not efficacy data for indolent plasma cell myeloma. The term "indolent" in these papers refers to *indolent systemic mastocytosis* (a distinct mast cell disease), not indolent plasma cell myeloma. These papers confirm isatuximab is used in active MM patients but provide no direct evidence for the predicted new indication. Relevance is assessed as **indirect only**.

---

## Taiwan Market Information

Isatuximab has not been approved by the TFDA and has no active marketing authorizations in Taiwan.

| Item | Content |
|------|---------|
| Taiwan Market Status | Not Marketed |
| TFDA Authorizations | 0 |

> **Reference:** Isatuximab (Sarclisa®) has received marketing approval from the EMA (EU) and FDA (US) for relapsed/refractory multiple myeloma. Taiwan market entry has not been established as of the data cutoff (2026-04-20).

---

## Cytotoxicity

Isatuximab is an antineoplastic agent (monoclonal antibody targeting CD38) indicated for a hematologic malignancy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — anti-CD38 monoclonal antibody (IgG1-κ); not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — neutropenia and anemia are common treatment-emergent adverse events, often compounding disease-related cytopenias in myeloma patients |
| Emetogenicity Classification | Low (consistent with other monoclonal antibodies; nausea is not a primary adverse effect) |
| Monitoring Items | CBC with differential (for neutropenia/anemia), hepatic and renal function, serum immunoglobulins, infusion reaction monitoring during and after each administration |
| Handling Protection | Standard biologic/monoclonal antibody handling required; dedicated cytotoxic chemotherapy handling precautions not mandated, but institutional biosafety protocols for parenteral biologics apply |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) or the FDA prescribing information for complete safety information, as Taiwan-specific label data is not available.

> **Known class-level concerns for anti-CD38 monoclonal antibodies:**
> - **Infusion-related reactions**: Occur in a significant proportion of patients, typically with the first infusion; pre-medication (antihistamines, corticosteroids, antipyretics) is standard practice.
> - **Interference with blood bank testing**: Anti-CD38 antibodies bind to red blood cell CD38, causing false-positive indirect antiglobulin tests (IAT/Coombs); blood bank must be notified prior to treatment.
> - **Immunosuppression**: Increased risk of serious infections, including upper respiratory tract infections and pneumonia.
> - **Contraindications**: Active severe infection is a clinical contraindication; use in pregnancy requires careful risk-benefit assessment (Fc-mediated placental transfer possible).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between isatuximab and indolent plasma cell myeloma is biologically sound — CD38 is constitutively expressed throughout the plasma cell dyscrasia spectrum — but the current evidence base is insufficient to advance this candidate beyond exploratory status. No clinical trials have been conducted, and the two retrieved publications are desensitization case reports with no relevance to efficacy in this specific indication.

**To proceed, the following is needed:**

- **Formal MOA documentation**: Obtain the complete DrugBank MOA record and pharmacodynamic data to support mechanism-based dossier construction
- **Smouldering MM trial data review**: Conduct a targeted literature review of anti-CD38 class trials in high-risk SMM (e.g., daratumumab AQUILA trial results) to establish class-level evidence and inform isatuximab-specific feasibility
- **TFDA regulatory pathway assessment**: Determine whether a Taiwan development pathway is feasible given the absence of local approval even for the base indication (active MM)
- **Taiwan market entry for base indication first**: Isatuximab's predicted new indication cannot be pursued in Taiwan without first establishing regulatory presence for its approved (active MM) indication
- **Safety profile gap closure**: Retrieve TFDA SmPC or EMA SmPC to complete the contraindications, warnings, and drug interaction profile (currently all marked as data gaps)
- **Prospective trial feasibility**: If mechanistic evidence review is positive, consider whether a Phase 2 investigator-initiated trial in high-risk SMM using isatuximab is feasible within the Taiwan or regional oncology network
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

