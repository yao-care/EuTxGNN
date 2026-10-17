---
layout: default
title: Cabozantinib
parent: Medium Evidence (L3-L4)
nav_order: 119
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-15
description: "Cabozantinib: predicted new indication Liposarcoma (evidence level L3). Approved use: Progressive…"
monitor_inn: "Cabozantinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Cabozantinib: From Medullary Thyroid Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is a multi-kinase inhibitor originally authorised in the EU for progressive, unresectable locally advanced or metastatic medullary thyroid carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** (a mixed soft tissue sarcoma study) and **1 publication** (a Phase 1 study) currently supporting this direction.
Evidence for this top-ranked prediction is limited, and the data compiled for this report show stronger evidence for renal cell carcinoma subtypes (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Progressive, unresectable locally advanced or metastatic medullary thyroid carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| EU Market Status | Cancelled only (the single Cometriq authorisation is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold (treat as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on the target profile described in the evidence review, cabozantinib inhibits VEGFR2, MET and AXL. These kinases drive angiogenesis and tumour survival signalling, and are relevant in several solid tumours, including soft tissue sarcomas.

Its efficacy in medullary thyroid carcinoma has been established, and mechanistically it may be applicable to liposarcoma. However, the link is plausible but not subtype-specific. Available clinical data come from mixed sarcoma populations, not liposarcoma alone.

Note that lower-ranked predictions have more evidence than the top-ranked one. Unclassified renal cell carcinoma (L2, Phase 2 trials and published Phase 2 results with nivolumab) and renal carcinoma overall (L1, Phase 3 trials) are better supported. Renal carcinoma is already an approved indication for cabozantinib elsewhere, so it is not strictly a repurposing finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomised study of ipilimumab + nivolumab with or without cabozantinib in advanced soft tissue sarcoma. Not liposarcoma-specific, and no results yet (expected completion 2028). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 trial | Am J Clin Oncol | Neoadjuvant cabozantinib with radiation therapy in extremity sarcomas. It evaluated safety, given concerns about fistula or perforation risk with concurrent radiotherapy. Cabozantinib has shown activity in multiple soft tissue sarcoma subtypes. |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002640 | Cometriq | Not specified | Treatment of adult patients with progressive, unresectable locally advanced or metastatic medullary thyroid carcinoma. |

The authorisation status is cancelled. The data compiled for this report suggest the "Cancelled only" status may reflect a labelling artefact for a specific product and should be verified.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The first 20 reviewed include these **Major** interactions:
  - Acetylsalicylic acid
  - Cisapride
  - Clarithromycin
  - Dolasetron
  - Granisetron
  - Levofloxacin

  Several **Moderate** interactions were also listed, including loperamide, aprepitant, dexamethasone, bisacodyl, clotrimazole and various laxatives.

- **Additional note**: A Phase 1 sarcoma study (PMID 41770651) specifically examined the fistula and perforation risk when cabozantinib is combined with radiotherapy.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The liposarcoma prediction has a high model score, but its supporting evidence is a single Phase 2 trial in mixed soft tissue sarcoma and one Phase 1 safety study. Neither is liposarcoma-specific, and no efficacy results are available. The sub-ranked predictions for ovarian myxoid liposarcoma, amyotrophic lateral sclerosis, polymicrogyria and angiolipoma have no supporting evidence and should remain on hold.

**To proceed, the following is needed:**
- Liposarcoma-specific efficacy data, such as subtype-stratified results from NCT05836571 or a dedicated liposarcoma trial
- Detailed mechanism of action data (MOA)
- EU safety information (warnings and contraindications) from the SmPC
- Verification of the "Cancelled only" EU market status
- A separate evaluation of the renal cell carcinoma indications. Unclassified RCC has Phase 2 evidence and could be considered "Proceed with Guardrails", while renal carcinoma overall has Phase 3 evidence but is not a true repurposing case.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

