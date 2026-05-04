---
layout: default
title: Ivacaftor
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Ivacaftor
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

# Ivacaftor: From Cystic Fibrosis to Rheumatoid Arthritis

## One-Sentence Summary

Ivacaftor (Kalydeco) is a CFTR potentiator originally approved for cystic fibrosis (CF) in patients with specific CFTR gating mutations.
The TxGNN model predicts it may have therapeutic potential in **Rheumatoid Arthritis (RA)**,
supported by **1 observational clinical study** and **1 animal/mechanistic publication** — both indirect in nature.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cystic fibrosis (CFTR gating mutations, e.g. G551D) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 96.97% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ivacaftor acts as a CFTR potentiator — it binds to the CFTR protein at the cell surface and increases the time the chloride channel remains open, restoring ion transport function in epithelial and immune cells. Although formal MOA data is not available in this Evidence Pack, its mechanism is well-established in the CF literature and is central to understanding its potential in RA.

The proposed mechanistic bridge rests on CFTR's role in immune cell regulation. In neutrophils, CFTR modulates NOX2-dependent reactive oxygen species (ROS) production and NETosis — the process by which neutrophils release DNA nets that can drive synovial inflammation in RA. By restoring CFTR function, Ivacaftor may dampen excessive neutrophil activation and reduce joint inflammation. Supporting this, PMID 28634110 demonstrated that CFTR restoration in ductal cells significantly reduced inflammasome-driven inflammation in mouse models of Sjögren's syndrome and autoimmune pancreatitis — autoimmune conditions with mechanistic similarities to RA synovitis.

However, the biological leap from CF to RA is substantial. Cystic fibrosis is a monogenic channelopathy; RA is a complex autoimmune disorder driven by T-cell dysregulation, anti-CCP antibodies, and cytokine cascades (TNF-α, IL-6, IL-17). No direct clinical evidence links Ivacaftor to RA treatment. The current evidence is hypothesis-generating rather than confirmatory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | Observational | Completed | 47 | Examined neutrophil phenotype and function in CF patients; assessed impact of CFTR modulators (including Ivacaftor) and Pseudomonas aeruginosa infection on neutrophil biology. Provides indirect mechanistic data on CFTR's role in innate immune regulation, but does not study RA. |

> **Note:** This trial is an observational study of CF patients, not a RA intervention trial. Its relevance to Ivacaftor repurposing for RA is indirect (Grade C relevance).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28634110](https://pubmed.ncbi.nlm.nih.gov/28634110/) | 2017 | Animal/Mechanistic Study | Gastroenterology | CFTR restoration in ductal cells rescued acinar cell function and reduced inflammation in mouse models of Sjögren's syndrome and autoimmune pancreatitis. Suggests that Ivacaftor-mediated CFTR potentiation may dampen autoimmune-driven glandular and exocrine inflammation via inflammasome pathways. No RA-specific data. |

---

## Taiwan Market Information

Ivacaftor is not currently approved or marketed in Taiwan. No TFDA-issued drug licenses are on record for this compound.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No Taiwan licenses found |

> Ivacaftor (brand name Kalydeco) is approved in the United States (FDA, 2012) and Europe (EMA) for CF with CFTR gating/residual function mutations. Taiwan TFDA marketing authorization has not been obtained.

---

## Safety Considerations

Formal safety data (product warnings, contraindications, drug interaction records) are not available in this Evidence Pack for the Taiwan context.

> Please refer to the EU Summary of Product Characteristics (SmPC) or FDA Prescribing Information for Kalydeco for complete safety information, including hepatotoxicity monitoring requirements and CYP3A4 drug interaction risks.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis linking CFTR potentiation to RA is biologically plausible but entirely preclinical and indirect — no human RA trials, no RA-focused animal models, and no clinical outcome data exist. The single observational CF trial and mouse autoimmune study (in non-RA conditions) are insufficient to justify advancing to clinical investigation without additional foundational work.

**To proceed, the following is needed:**

- **MOA validation in RA models:** Conduct in vitro studies in RA synoviocytes and/or neutrophils to confirm that Ivacaftor modulates NETosis and inflammasome activity in RA-relevant cell types
- **Animal model evidence:** Test Ivacaftor in a collagen-induced arthritis (CIA) mouse model to establish proof-of-concept before any human study
- **Taiwan regulatory pathway assessment:** Obtain TFDA prescribing information and safety data; evaluate whether compassionate use or an IND application is feasible given the current zero-license status in Taiwan
- **Patient stratification hypothesis:** Determine whether RA patients with any CFTR variant frequency might preferentially respond (precision medicine angle)
- **Drug interaction profile:** Ivacaftor is a strong CYP3A4 substrate and inhibitor; a formal DDI analysis is required before any combination therapy is designed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

