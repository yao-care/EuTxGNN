---
layout: default
title: Eribulin
parent: AI Predictions (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Eribulin: predicted new indication Autosomal recessive familial Mediterranean fever (evidence level L5). Approved use: Locally advanced or metastatic breast cancer after at least one chemo…"
---

# Eribulin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Eribulin: From Breast Cancer and Liposarcoma to Autosomal Recessive Familial Mediterranean Fever

## One-Sentence Summary

Eribulin is a microtubule dynamics inhibitor, originally used to treat locally advanced or metastatic breast cancer and unresectable liposarcoma.
The TxGNN model's top-ranked prediction is **autosomal recessive familial Mediterranean fever**, but this prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.
The best-supported direction among the top 10 predictions is **fibroblastic neoplasm** (mainly solitary fibrous tumor), with **1 completed Phase 2 trial** and several supporting publications (mostly preclinical).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Locally advanced or metastatic breast cancer after at least one chemotherapy regimen for advanced disease; unresectable liposarcoma after prior anthracycline therapy |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, eribulin is a microtubule dynamics inhibitor (a cytotoxic chemotherapy). Its efficacy in breast cancer and liposarcoma has been established, and it may be mechanistically applicable to other mesenchymal tumours.

For the top-ranked prediction, familial Mediterranean fever, **no mechanistic link is supported**. The disease is an autoinflammatory condition driven by dysregulation of the pyrin inflammasome (MEFV gene). Colchicine, another microtubule-targeting agent, is used in this disease, but it works differently and does not validate eribulin. A cytotoxic chemotherapy is also unlikely to be appropriate for a chronic non-malignant condition. The very high score (0.998) appears to be a model-only signal.

Other predictions fall into three groups:
- **Mesothelioma family** (pleural, peritoneal, biphasic, epithelioid): a general antimitotic rationale only, with no trials or literature.
- **Sarcoma family**: dermatofibrosarcoma protuberans, ovarian myxoid liposarcoma, heart fibrosarcoma and fibroblastic neoplasm. These are biologically plausible given eribulin's approved liposarcoma use. DFSP, however, is driven by the COL1A1-PDGFB fusion and is usually treated with surgery and imatinib. The ovarian liposarcoma prediction is better seen as label-adjacent than as new repurposing evidence.
- **Pleural adenomatoid tumor**: generally benign, so cytotoxic chemotherapy is unlikely to be justified.

The strongest direction is **fibroblastic neoplasm**, represented mainly by solitary fibrous tumor (SFT). A Phase 2 study tested eribulin directly in this tumor type, and preclinical work in fibrosarcoma cells adds supportive evidence.

---

## Clinical Trial Evidence

There are no clinical trials for the top-ranked indication (familial Mediterranean fever). The only registered trial among the top 10 predictions is for fibroblastic neoplasm (rank 8):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | ERASING study: eribulin in advanced solitary fibrous tumor (Italian Sarcoma Group). Results were not available in the data compiled for this report. |

---

## Literature Evidence

There is no literature for the top-ranked indication. The two most relevant sets are below.

**Fibroblastic neoplasm (rank 8)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | Diagnosis and treatment of extrameningeal solitary fibrous tumors |
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Preclinical (patient-derived xenograft) | Eur J Cancer | SFT xenografts highly sensitive to doxorubicin/dacarbazine; trabectedin and eribulin may also be effective |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Preclinical (in vitro) | Anticancer Res | Recombinant methioninase synergizes with eribulin against fibrosarcoma cells but not normal fibroblasts |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Preclinical (in vitro) | Anticancer Res | Methioninase increased eribulin efficacy 16-fold in highly eribulin-resistant HT1080 fibrosarcoma cells |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Preclinical (in vivo, nude mice) | In Vivo | Super eribulin-resistant fibrosarcoma cells were arrested by eribulin combined with methionine restriction |

**Dermatofibrosarcoma protuberans (rank 2)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/) | 2016 | Review | Cancer | General review of soft tissue sarcoma chemotherapy; indirect evidence only |

---

## EU Market Information

All three EU authorizations for eribulin are cancelled.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/006191 | Eribulin Baxter | Not specified | Locally advanced or metastatic breast cancer after at least one chemotherapy regimen for advanced disease; unresectable liposarcoma after prior... |
| EMEA/H/C/002084 | Halaven | Not specified | Locally advanced or metastatic breast cancer after at least one chemotherapeutic regimens for advanced disease (see section 5.1). Prior therapy... |
| EMEA/H/C/006134 | Mevlyq | Not specified | Locally advanced or metastatic breast cancer after at least one chemotherapeutic regimen for advanced disease; unresectable liposarcoma after... |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (microtubule dynamics inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions. Knowledge-graph links to neutropenia, agranulocytosis and thrombocytopenia suggest haematological toxicity is relevant. |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function, electrolytes (including potassium), ECG (QT interval), and neurological assessment for peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text): long QT syndrome (including familial), thrombocytopenia, potassium deficiency, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, and constipation disorder.
- **Drug interactions**: 100 interactions were identified. Those listed here are the **Major** ones:
  - Dolasetron (Major)
  - Cisapride (Major)

  Moderate interactions include ondansetron, palonosetron, clarithromycin, levofloxacin, metronidazole, tinidazole, famotidine, simvastatin, rosuvastatin, loperamide, and several laxatives (bisacodyl, picosulfuric acid, lactulose, lactitol, polyethylene glycol, sodium sulfate, castor oil). Many of these are QT-prolonging agents or drugs affecting gastrointestinal motility and electrolytes, which matches the knowledge-graph QT and potassium signals.

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (familial Mediterranean fever) has no clinical or literature support and no plausible mechanistic link. The high TxGNN score is a prediction-only signal, and a cytotoxic chemotherapy is unlikely to suit a chronic non-malignant disease.
- The most promising direction among the top 10 is fibroblastic neoplasm (solitary fibrous tumor). It should be treated as a research question rather than a ready candidate, because the completed Phase 2 trial has no available results and the supporting literature is mostly preclinical.
- All EU authorizations are currently cancelled.

**To proceed, the following is needed:**
- Results (response rate, progression-free survival, safety) of the ERASING Phase 2 study (NCT03840772).
- Mechanism of action data to support mechanistic-link analysis.
- Safety information from the SmPC (warnings and contraindications), which is currently a blocking gap for safety screening.
- Clarification of the reasons for the cancelled EU authorizations and of current availability.
- A dedicated literature search for the mesothelioma and rare sarcoma predictions.
- A safety monitoring plan covering QT prolongation, neutropenia, and peripheral neuropathy, and a review of concomitant QT-prolonging drugs.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

