---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Lapatinib
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

# Lapatinib: From HER2-Positive Breast Cancer to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib (Tykerb/Tyverb) is a dual tyrosine kinase inhibitor targeting EGFR and HER2, originally approved for the treatment of HER2-positive metastatic breast cancer in combination with other agents.
The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, with a prediction confidence of **99.30%** — however, **no clinical trials or supporting literature** currently exist for this combination, and the mechanistic rationale is limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive metastatic breast cancer (not registered in Taiwan) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans (DFSP) |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Lapatinib is a small-molecule inhibitor that reversibly binds the ATP-binding pocket of both EGFR (HER1/ErbB1) and HER2 (ErbB2) tyrosine kinases. This dual blockade suppresses downstream PI3K/AKT and RAS/MAPK signaling cascades — pathways that are critical for proliferation and survival in HER2-amplified tumors. Its oral bioavailability and CNS penetration distinguish it from antibody-based HER2 therapies such as trastuzumab.

Dermatofibrosarcoma Protuberans (DFSP) is a rare dermal sarcoma characterized by the COL1A1-PDGFB gene fusion, which drives constitutive PDGFR (platelet-derived growth factor receptor) signaling. The established targeted therapy for advanced DFSP is Imatinib, a PDGFR inhibitor — not an EGFR/HER2 inhibitor. EGFR overexpression or HER2 amplification has not been documented as a key oncogenic mechanism in DFSP, making the mechanistic basis for Lapatinib in this setting comparatively weak.

The TxGNN model's high confidence score (99.30%) most likely reflects network-level structural similarity within the receptor tyrosine kinase inhibitor drug class and overlapping graph topology, rather than a direct mechanistic match with the primary DFSP driver. Notably, among all 10 predicted indications reviewed, the most scientifically coherent signal is for *Plasmodium falciparum* malaria (Rank 8, L4 evidence), where in vitro studies directly demonstrate haemozoin inhibition — a mechanism with substantially stronger scientific support than the DFSP prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorization records are present in the current evidence pack (market status: not marketed, 0 registered licenses). This may reflect a data gap rather than confirmed absence from the EU market, as Lapatinib is known internationally under the brand name Tyverb. Verification against the EMA product database is recommended.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Dual EGFR/HER2 tyrosine kinase inhibitor (TKI); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate (neutropenia and thrombocytopenia are reported but less frequent than with traditional chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs; hepatotoxicity risk), left ventricular ejection fraction (LVEF assessment prior to and during treatment), CBC with differential, QTc interval (cardiac monitoring), skin toxicity evaluation (rash, hand-foot syndrome) |
| Handling Protection | Classified as a hazardous drug on the NIOSH list; standard cytotoxic-safe handling precautions are recommended per institutional pharmacy guidelines |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model's high algorithmic confidence (99.30%), there is no clinical trial evidence and no supporting literature for Lapatinib in DFSP, and the primary oncogenic driver of DFSP — PDGFR activation via the COL1A1-PDGFB fusion — is mechanistically distinct from Lapatinib's EGFR/HER2 targets, leaving no established scientific basis for this repurposing direction at this time.

**To proceed, the following is needed:**
- Evidence of EGFR or HER2 overexpression in DFSP tumor samples (IHC, FISH, or transcriptomic analysis) to establish a target-disease link
- Preclinical sensitivity testing of Lapatinib in DFSP cell lines or patient-derived xenograft models
- Full MOA data retrieval from DrugBank (data gap DG002) to strengthen mechanistic rationale analysis
- TFDA SmPC retrieval and parsing (data gap DG001, blocking severity) to enable safety pre-screening
- **Priority redirection**: Consider advancing the *Plasmodium falciparum* malaria signal (Rank 8, L4 evidence; 3 supporting publications including direct haemozoin inhibition data, PMID 32235391) as a higher-priority repurposing candidate for focused investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

