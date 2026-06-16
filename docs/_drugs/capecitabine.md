---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug that is enzymatically converted to 5-fluorouracil (5-FU) preferentially within tumour tissues, widely used globally for colorectal cancer, gastric cancer, and breast cancer treatment.
The TxGNN model predicts it may be effective for **Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)** — a rare hereditary gastric cancer syndrome —
with **0 clinical trials** and **0 publications** currently supporting this specific indication, placing the evidence at **L5 (AI prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in this database (Taiwan/EU data gap) |
| Predicted New Indication | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Market Status | Not marketed (0 authorizations on record) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack (flagged as Data Gap). Based on known pharmacology, Capecitabine is an oral fluoropyrimidine prodrug that undergoes a three-step enzymatic conversion to 5-fluorouracil (5-FU), with the final activation step catalysed by Thymidine Phosphorylase (TP), which is overexpressed in many tumour tissues relative to healthy tissue. The active metabolite 5-FU inhibits Thymidylate Synthase (TS), thereby blocking de novo pyrimidine synthesis and DNA replication, ultimately triggering tumour cell apoptosis. This tumour-selective activation underlies its established use across multiple gastrointestinal cancers.

GAPPS (Gastric Adenocarcinoma and Proximal Polyposis of the Stomach) is an ultra-rare hereditary syndrome caused by germline point mutations in the *APC* gene Promoter 1B, resulting in diffuse fundic gland polyposis in the gastric fundus and body with high malignant transformation potential. Mechanistically, Capecitabine's TS inhibition pathway is theoretically applicable to GAPPS-associated adenocarcinoma, since the target enzyme is relevant to rapidly proliferating cancer cells regardless of tumour origin. The transformation from GAPPS polyps to frank adenocarcinoma shares histopathological features with sporadic gastric cancer.

However, the high TxGNN prediction score almost certainly reflects generalisation from the broader gastric cancer knowledge graph rather than GAPPS-specific biological signal. GAPPS is so rare (fewer than 100 reported families worldwide) that no clinical chemotherapy data exist for this syndrome, and TP expression levels in GAPPS-associated tumours have never been characterised. Proceeding to repurposing for this specific entity requires disease-specific preclinical evidence generation before any clinical steps.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Capecitabine in Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS).

---

## Literature Evidence

Currently no related literature available for Capecitabine in Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS).

---

## Market Information

No marketing authorizations on record for Capecitabine in this Evidence Pack (market status: not marketed, 0 licenses).

> **Data Note**: This reflects a data collection gap. Capecitabine (Xeloda®) holds established regulatory approvals in multiple jurisdictions (EMA, FDA, PMDA, and others) for colorectal cancer, gastric cancer, and breast cancer. If Taiwan/EU SmPC data is obtained (see Conclusion section), the above status should be updated accordingly.

---

## Cytotoxicity

Capecitabine is a fluoropyrimidine antineoplastic agent (conventional cytotoxic) and this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug of 5-FU) |
| Myelosuppression Risk | Low to moderate — less myelosuppressive than intravenous 5-FU; neutropenia and lymphopenia may occur |
| Emetogenicity Classification | Low (oral route; nausea more common than vomiting) |
| Monitoring Items | CBC with differential count, liver function (AST/ALT/bilirubin), renal function (CrCl — dose reduction required if 30–50 mL/min), INR/PT (critical if co-administered with warfarin), hand-foot syndrome (palmar-plantar erythrodysaesthesia) grading |
| Handling Protection | Standard oral cytotoxic handling precautions apply; tablets should not be crushed; caregivers should avoid direct contact with broken tablets |

> No cytotoxicity data is available from this Evidence Pack. The above is based on the drug's established fluoropyrimidine class profile. Please refer to the SmPC for complete prescribing information.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> All safety fields in this Evidence Pack (key warnings, contraindications, drug-drug interactions) are flagged as data gaps. Obtaining the TFDA/EMA SmPC is classified as a **Blocking** data gap (DG001) and must be resolved before any clinical safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
GAPPS is an ultra-rare hereditary syndrome with no published clinical evidence supporting the use of Capecitabine, and the TxGNN L5 prediction most likely reflects gastric cancer knowledge graph generalisation rather than disease-specific signal. The absolute absence of trials, publications, or case reports for this indication — combined with the blocking safety data gap — makes advancement beyond hypothesis generation premature at this stage.

**To proceed, the following is needed:**

- **Resolve blocking data gap (DG001):** Obtain TFDA/EMA SmPC to complete safety pre-screening before any further evaluation
- **Resolve high-severity data gap (DG002):** Query DrugBank API to confirm Capecitabine's MOA and TP/TS pathway details formally
- **Preclinical evidence:** Characterise TP and TS expression levels in GAPPS-associated fundic gland polyps and adenocarcinoma tissue (IHC or transcriptomic data from published GAPPS case series)
- **Registry/case series search:** Systematic search of GAPPS patient registries (e.g., GAPPS International Registry) for any recorded chemotherapy use after malignant transformation
- **Consider broader gastric cancer evidence context:** Other gastric cancer subtypes in this Evidence Pack (gastric tubular adenocarcinoma — Rank 3, L1; gastric cardia adenocarcinoma — Rank 5, L1; gastric body carcinoma — Rank 8, L1) carry substantially stronger clinical evidence for Capecitabine and may be more productive repurposing targets for regulatory review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

