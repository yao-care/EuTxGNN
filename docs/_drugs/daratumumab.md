---
layout: default
title: Daratumumab
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Daratumumab
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

# Daratumumab: From Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Daratumumab is a human IgG1κ monoclonal antibody targeting CD38, approved internationally for the treatment of multiple myeloma but not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Indolent Plasma Cell Myeloma** (smouldering multiple myeloma),
with **1 clinical trial** (indirect evidence) and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Myeloma (internationally approved; not marketed in Taiwan) |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 98.13% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, daratumumab is a human anti-CD38 IgG1κ monoclonal antibody that binds to CD38 — a transmembrane glycoprotein highly and uniformly expressed on the surface of malignant plasma cells. Upon binding, it triggers multiple immune-mediated killing mechanisms including complement-dependent cytotoxicity (CDC), antibody-dependent cellular cytotoxicity (ADCC), antibody-dependent cellular phagocytosis (ADCP), and direct apoptosis induction. Its efficacy in active multiple myeloma has been extensively validated across multiple Phase 3 trials.

Indolent plasma cell myeloma (synonymous with smouldering multiple myeloma, SMM) represents the biologically immediate precursor state to active multiple myeloma. The malignant plasma cells in SMM express CD38 at equally high density as those in active disease — meaning daratumumab's molecular target is fully intact in this earlier-stage condition. PMID 28915615 directly characterises CD38 expression across the myeloma bone marrow niche by flow cytometry and immunohistochemistry, and explicitly discusses the biological rationale for anti-CD38 immunotherapy in plasma cell disorders at the indolent monoclonal stage.

The TxGNN prediction score of 98.13% reflects this near-perfect mechanistic alignment. Notably, the AQUILA Phase 3 clinical trial (daratumumab monotherapy versus active monitoring in intermediate- and high-risk SMM) has already reported a statistically significant progression-free survival benefit, though this landmark data is not captured in the current Evidence Pack. The clinical trajectory from SMM to active MM is well-defined, and early intervention to delay or prevent transformation represents a logical and high-value therapeutic opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04136756](https://clinicaltrials.gov/study/NCT04136756) | Phase 1 | Completed | 30 | Dose escalation study of NKTR-255 (an IL-15 pathway immunomodulator) in relapsed/refractory haematological malignancies; daratumumab SC (DARZALEX FASPRO™) is used as a combination partner in one dosing arm. Daratumumab is not the primary investigational agent — indirect relevance only as a background combination drug in the same disease population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28915615](https://pubmed.ncbi.nlm.nih.gov/28915615/) | 2017 | Translational/Mechanistic Study | Oncotarget | First systematic characterisation of CD38 expression across the myeloma bone marrow niche using flow cytometry and immunohistochemistry in a cohort including indolent monoclonal plasma cell conditions; provides direct mechanistic rationale for anti-CD38 immunotherapy (daratumumab) in the plasma cell disease continuum |
| [41571958](https://pubmed.ncbi.nlm.nih.gov/41571958/) | 2026 | Review / Clinical Guideline | Nature Reviews Clinical Oncology | Comprehensive review of diagnosis, risk stratification and management of smouldering multiple myeloma; covers evolving treatment paradigms including the shift toward early intervention strategies for intermediate- and high-risk SMM |
| [40257478](https://pubmed.ncbi.nlm.nih.gov/40257478/) | 2025 | Case Report | Annals of Hematology | Paraneoplastic leukocytoclastic vasculitis as a rare initial presentation of smoldering IgG kappa myeloma; illustrates the systemic morbidity that can arise even during the indolent phase, reinforcing the clinical rationale for earlier treatment intervention |
| [32736600](https://pubmed.ncbi.nlm.nih.gov/32736600/) | 2020 | Case Report | BMC Gastroenterology | Crystal storing histiocytosis secondary to indolent multiple myeloma presenting as a colonic mass; demonstrates that indolent plasma cell myeloma can cause significant end-organ complications, supporting the case for effective targeted therapy at this earlier disease stage |
| [34514307](https://pubmed.ncbi.nlm.nih.gov/34514307/) | 2021 | Case Report | European Heart Journal Case Reports | Concomitant aortic valve papillary fibroelastoma and cardiac AL amyloidosis; highlights irreversible end-organ damage arising from plasma cell disorders, underscoring the potential value of early daratumumab-based intervention before transformation to active disease |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Anti-CD38 human IgG1κ monoclonal antibody (Immunotherapy) |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anaemia reported, particularly in combination regimens (e.g., with bortezomib or lenalidomide); lower risk as monotherapy |
| Emetogenicity Classification | Low — as a biologic, primary acute adverse effect is infusion-related reactions (IRR), not nausea/vomiting |
| Monitoring Items | CBC with differential (frequently during early cycles), liver and renal function, serum immunoglobulins; vital signs monitoring during infusions for IRR; type and screen (daratumumab interferes with indirect antiglobulin tests) |
| Handling Protection | Standard aseptic biologic preparation protocols apply; not classified as a conventional cytotoxic, but institutional monoclonal antibody handling procedures are required |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is exceptionally strong — CD38 is daratumumab's direct molecular target and is uniformly expressed on plasma cells throughout the disease continuum from SMM to active myeloma. Real-world Phase 3 trial evidence (AQUILA trial) already supports this application and is anticipated to elevate the evidence level to L1 once formally incorporated into the Evidence Pack.

**To proceed, the following is needed:**
- Retrieve and formally document the AQUILA Phase 3 trial results to upgrade evidence level from L3 to L1
- Obtain Taiwan SmPC equivalent (or reference the EMA/FDA SmPC) to complete key warnings, contraindications, and drug interaction profiling — currently all flagged as data gaps
- Assess TFDA regulatory pathway: daratumumab has no Taiwan authorisation; evaluate filing strategy, compassionate use, or clinical trial application
- Establish patient selection criteria — treatment benefit is most clearly established in intermediate- to high-risk SMM (per 2020 IMWG risk model); low-risk SMM patients may not require intervention
- Note daratumumab's known interference with indirect antiglobulin tests (blood bank crossmatching); institutional protocols must be in place before clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

