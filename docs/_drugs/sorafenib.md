---
layout: default
title: Sorafenib
parent: High Evidence (L1-L2)
nav_order: 551
evidence_level: L2
indication_count: 10
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sorafenib: From Renal Cell Carcinoma and Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multi-target tyrosine kinase inhibitor whose established use — based on the literature referenced in this Evidence Pack — spans renal cell carcinoma and hepatocellular carcinoma. The TxGNN model predicts it may also be effective for **Liposarcoma**, currently supported by **2 clinical trials** and **8 publications**, including a direct preclinical study in liposarcoma cell lines.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma / hepatocellular carcinoma (based on literature references within this Evidence Pack; formal EU marketing-authorization data for the original indication is not available in this dataset) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The drug-level mechanism-of-action field is currently a data gap. However, literature within this Evidence Pack (PMID 15466206) describes sorafenib (BAY 43-9006) as a multi-targeted kinase inhibitor of Raf-1/B-RAF (blocking the RAF/MEK/ERK signaling pathway) as well as receptor tyrosine kinases including VEGFR-1/2/3, PDGFR-β, FLT3, and c-KIT — targets involved in both tumor proliferation and angiogenesis. This dual antiproliferative/antiangiogenic mechanism underlies sorafenib's established activity in renal cell carcinoma and hepatocellular carcinoma.

Liposarcoma and other soft tissue sarcomas frequently show dysregulation of the same pathways — activated Ras/Raf/MAPK signaling and PDGFR-driven proliferation — providing a plausible mechanistic bridge from the original oncology indications to this new one. Directly supporting this link, PMID 18413802 reports that sorafenib inhibited growth and MAPK signaling in two dedifferentiated liposarcoma cell lines (LS141 and DDLS), giving direct preclinical evidence for antitumor activity in liposarcoma specifically, in addition to the broader clinical experience with sorafenib across soft tissue sarcoma subtypes (e.g., the SWOG S0505 Phase 2 trial, PMID 21751200).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib evaluated in advanced soft tissue sarcomas; rationale based on its ability to block cell-growth enzymes and tumor blood flow. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol testing oral regorafenib (a sorafenib-related multi-kinase inhibitor) across selected sarcoma subtypes; trial rationale explicitly cites documented sorafenib activity in soft tissue sarcomas. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Clinical Trial (Phase 2) | Cancer | SWOG intergroup Phase 2 trial (S0505) of sorafenib in advanced soft tissue sarcomas, targeting Raf/VEGFR/PDGFR/c-KIT pathways relevant to sarcoma biology. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Clinical Trial (Phase 1) | Annals of Surgical Oncology | Phase I trial of neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma, based on synergy between antiangiogenic therapy and radiotherapy. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Review of sarcoma PDOX mouse models identifying effective combination therapies with targeted agents, supporting continued rationale for kinase-inhibitor approaches in sarcoma. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Review of soft tissue sarcoma treatment by histological subtype, noting the growing role of targeted therapies alongside cytotoxics. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven therapy review for soft tissue sarcomas, noting subtype-specific activity of targeted/cytotoxic agents including in liposarcoma. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibited growth and MAPK signaling in dedifferentiated liposarcoma cell lines (LS141, DDLS) and MPNST cells — direct mechanistic evidence for the liposarcoma prediction. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | American Journal of Pathology | Dedifferentiated liposarcoma xenograft models revealed PTEN down-regulation as a malignant signature and response to PI3K pathway inhibition, providing molecular rationale for targeted therapy in liposarcoma. |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case Report | Anti-Cancer Drugs | Case report of response to trabectedin (not sorafenib) in advanced synovial sarcoma with lung metastases; included as sarcoma-treatment background context. |

---

## EU Market Information

No EU marketing-authorization records are available for sorafenib in the current dataset (`taiwan_regulatory.licenses` is empty and `market_status` is recorded as "Not marketed"). This should be independently verified, since sorafenib is a well-established oncology drug and an absence of EU licensing data likely reflects a gap in this Evidence Pack rather than actual withdrawal from the market.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor — RAF/MEK/ERK, VEGFR, PDGFR, c-KIT, FLT3; per PMID 15466206) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score, a directly relevant preclinical study in liposarcoma cell lines, and multiple completed Phase 2 trials in soft tissue sarcoma provide reasonable mechanistic and clinical plausibility. However, TFDA-equivalent/SmPC safety data (warnings and contraindications) is flagged as a **Blocking** data gap that prevents entry into the initial safety assessment (S1), and EU marketing-authorization status for sorafenib is currently unverified in this dataset.

**To proceed, the following is needed:**
- Retrieve official safety labeling (warnings, contraindications) — blocking gap (DG001)
- Confirm drug-level MOA documentation via DrugBank API query (DG002)
- Verify actual EU regulatory/licensing status for sorafenib (current "not marketed" record appears inconsistent with its known global approvals and should be re-checked)
- Obtain liposarcoma-specific (rather than broad soft-tissue-sarcoma) clinical trial data to strengthen the indication-specific evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

