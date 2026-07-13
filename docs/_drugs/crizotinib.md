---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Crizotinib is a first-in-class ATP-competitive inhibitor of ALK, ROS1, and MET receptor tyrosine kinases, clinically established for the treatment of ALK- or ROS1-rearranged non-small cell lung cancer (NSCLC).
The TxGNN model ranks **Fibromatosis, Gingival** as the highest-scoring new indication (score 99.81%), yet **no clinical trials and no supporting literature** exist for this specific prediction; mechanistic analysis in this evidence pack identifies the signal as a likely knowledge graph topological artefact rather than a genuine therapeutic opportunity.
Based on the totality of evidence in this pack, the recommended decision for this top-ranked indication is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive or ROS1-positive non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| EU Market Status | No EMA authorizations recorded in dataset |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published information from the supporting literature, Crizotinib (Xalkori®) is an oral small-molecule inhibitor that competitively blocks three oncogenic receptor tyrosine kinases: ALK (anaplastic lymphoma kinase), ROS1 (c-ros oncogene 1), and MET (hepatocyte growth factor receptor). Its efficacy has been robustly demonstrated in ALK-rearranged and ROS1-rearranged advanced NSCLC, with regulatory approval in multiple major jurisdictions. Relevant peer-reviewed reviews (PMID 24756793, 30069759) summarise its approved mechanism and clinical profile.

Fibromatosis, gingival is a rare condition characterised by benign, progressive overgrowth of gingival connective tissue. The primary genetic aetiologies involve mutations in **SOS1** or **EPAS1**, while drug-induced forms are driven by cyclosporine or phenytoin use. None of these pathways have a known intersection with ALK, ROS1, or MET signalling — the three kinases that Crizotinib targets.

The TxGNN model's high prediction score of 99.81% is most plausibly explained by shared topological nodes in the knowledge graph — specifically, nodes associated with fibroblast proliferation that appear in proximity to both gingival fibromatosis and cancer-related stromal processes. This constitutes structural noise rather than a true mechanistic link. The complete absence of any clinical trial registration or peer-reviewed literature further confirms that this prediction does not represent a viable repurposing hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Fibromatosis, Gingival.

---

## Cytotoxicity

Crizotinib is an antineoplastic agent approved for malignant NSCLC with specific oncogenic driver mutations.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — ALK/ROS1/MET tyrosine kinase inhibitor (first-generation) |
| Myelosuppression Risk | Low to moderate; neutropenia reported but less severe than conventional cytotoxics; see PMID 41617059 for mechanism review |
| Emetogenicity Classification | Low to moderate; nausea and vomiting are among the most common adverse effects, typically manageable with anti-emetic support |
| Monitoring Items | Liver function tests (ALT, AST, total bilirubin), CBC with differential, 12-lead ECG for QTc prolongation, chest imaging for interstitial lung disease (ILD), ophthalmological assessment |
| Handling Protection | Standard cytotoxic drug handling precautions apply; personnel should follow institutional guidelines for oral antineoplastic agents |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** PMID 41617059 (2026 review) specifically addresses crizotinib-induced multisystem toxicities including hepatotoxicity, cardiotoxicity (QT prolongation, bradycardia — see also PMID 29717400), and interstitial lung disease. PMID 26898609 documents a case of fatal fulminant liver failure after 24 days of therapy. These signals warrant careful monitoring protocols in any future use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction for Crizotinib — Fibromatosis, Gingival — carries no clinical trial evidence, no supporting literature, and lacks any plausible mechanistic connection between ALK/ROS1/MET inhibition and gingival fibroblast overgrowth pathways (SOS1/EPAS1/drug-induced). The high model score is consistent with knowledge graph structural noise and does not constitute a research hypothesis.

**To proceed with any Crizotinib repurposing programme, the following is needed:**

- **Redirect to higher-evidence indications in this evidence pack:** Lung Germ Cell Tumor (Rank 6, L3, S1 — 4 clinical trials including NCI MATCH Phase 2 and a Phase 1b directly in ALK+ tumours) and Lung Hilum Carcinoma (Rank 4, L4, S1 — 2 case reports with ALK+ and ROS1+ molecular confirmation) are substantively more promising
- **Mandatory molecular pre-selection:** Any repurposing hypothesis for Crizotinib must be gated on ALK rearrangement, ROS1 fusion, or MET exon 14 skipping status in the target tumour type
- **Complete MOA data:** Retrieve full pharmacological profile from DrugBank API (gap DG002)
- **Safety pre-screening:** Obtain SmPC warnings and contraindications via TFDA/EMA official sources (gap DG001, currently blocking S1 safety evaluation)
- **DDI profiling:** No drug-drug interaction data was retrievable; formal DDI assessment required before any clinical pathway planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

