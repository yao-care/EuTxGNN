---
layout: default
title: Lenvatinib
parent: Medium Evidence (L3-L4)
nav_order: 362
evidence_level: L3
indication_count: 5
last_modified_at: 2026-11-06
monitor_inn: "lenvatinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax", "endocrine-cerebro-osteodysplasia syndrome"]
description: "Lenvatinib: predicted new indication Liposarcoma (evidence level L3). Approved use: Kisplyx is indicated for the treatment of adults with advanced renal…"
---

# Lenvatinib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Lenvatinib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Lenvatinib is an oral multi-kinase inhibitor that blocks tumour blood-vessel growth and related growth signalling. The TxGNN model predicts it may be useful in **liposarcoma**, mainly in combination with eribulin. The evidence is **1 completed single-arm Phase 1b/2 trial** and **4 publications**, one of which reports that trial. No randomized trial exists, so the evidence level is **L3**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Kisplyx is indicated for the treatment of adults with advanced renal cell carcinoma (RCC): in combination with pembrolizumab, as first-line treatment (see section 5.1). in combination with everolimus, following one prior vascular endothelial growth factor (VEGF)-targeted therapy.; Lenvima&nbsp;is in |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L3 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Lenvatinib inhibits VEGFR1-3, FGFR1-4, PDGFRα, KIT and RET. These receptors drive tumour angiogenesis and growth signalling, which are also relevant in soft tissue sarcomas. Detailed mechanism-of-action data for the drug are not otherwise available in the data compiled for this report.

Eribulin is a microtubule inhibitor with known activity in liposarcoma. Combining it with an anti-angiogenic kinase inhibitor is therefore mechanistically plausible. Preclinical work on eribulin combinations and a CDK4 biomarker study in dedifferentiated liposarcoma give additional background for combination approaches. This is supporting context rather than direct proof that lenvatinib works in liposarcoma.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/Phase 2 | Completed | 30 | LEADER study: single-arm test of lenvatinib plus eribulin in inoperable or metastatic adipocytic sarcoma and leiomyosarcoma, assessing safety and efficacy. No randomized comparator. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase 1b/2 single-arm trial | Clinical Cancer Research | Report of the LEADER study (lenvatinib plus eribulin) in advanced liposarcoma and leiomyosarcoma, a setting with limited treatment options. |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical / biomarker study | Experimental Hematology & Oncology | CDK4 as a prognostic biomarker in soft tissue sarcoma, with a synergistic effect of CDK4 inhibition in sequential treatment of dedifferentiated liposarcoma. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical review | Anticancer Research | Broad preclinical antitumour activity of eribulin in combination with agents of differing mechanisms. |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Reports in Oncology | Marked tumour reduction in a patient with dedifferentiated liposarcoma and lung metastasis receiving individualized comprehensive treatment. |

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/003727 | Lenvima | lenvatinib mesilate | Valid |
| EMEA/H/C/004224 | Kisplyx | lenvatinib mesilate | Valid |

<!-- licenses:end -->

Both authorizations are currently valid.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor). Eribulin, the proposed combination partner, is a conventional cytotoxic agent. |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions. Haematological parameters and liver and renal function are generally followed in oncology use. |
| Handling Protection | Please refer to the SmPC; follow local rules for handling antineoplastic drugs. |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 260 entries. The first 20 reviewed include two **Major** interactions, with dolasetron and cisapride. Most of the others are Moderate:
  - famotidine
  - loperamide
  - bisacodyl
  - clarithromycin
  - picosulfuric acid
  - polyethylene glycol (3350 with electrolytes)
  - palonosetron
  - sodium sulfate
  - naltrexone
  - castor oil
  - glycerin
  - granisetron
  - lactitol
  - lactulose
  - levofloxacin
  - magnesium citrate
  - magnesium hydroxide

  Metronidazole is the only Minor one in this subset. Several of these are QT-prolonging or gastrointestinal agents, so combination use should be checked against the full interaction list.

For warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The main prediction (TxGNN score 0.9951) is supported by one completed single-arm Phase 1b/2 study (n=30; PMID 36129471, NCT03526679) of lenvatinib plus eribulin. Supporting material is preclinical or anecdotal, and no randomized trial exists. Further work should therefore stay within a controlled research setting.

**To proceed, the following is needed:**
- Randomized or larger controlled data in liposarcoma, ideally by subtype (for example, dedifferentiated versus well-differentiated)
- Parsed SmPC warnings and contraindications to complete the safety review
- Detailed mechanism-of-action data
- A monitoring plan for the lenvatinib–eribulin combination, including the interaction checks above

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

