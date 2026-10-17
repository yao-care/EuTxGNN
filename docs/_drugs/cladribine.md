---
layout: default
title: Cladribine
parent: AI Predictions (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cladribine: predicted new indication Parameningeal embryonal rhabdomyosarcoma (evidence level L5). Approved use: Treatment of adult patients with highly active relapsing multiple scl…"
monitor_inn: "Cladribine"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma", "skeletal muscle neoplasm", "gestational trophoblastic neoplasm", "pleural adenomatoid tumor"]
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Cladribine: From Multiple Sclerosis and Hairy-Cell Leukaemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analogue originally used to treat highly active relapsing multiple sclerosis and hairy-cell leukaemia.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**,
but **no clinical trials and no publications** currently support this prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of adult patients with highly active relapsing multiple sclerosis (MS) as defined by clinical or imaging features |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for the original indication is not available in the data compiled for this report. Based on general pharmacology, cladribine (2-chlorodeoxyadenosine) is resistant to adenosine deaminase and is phosphorylated by deoxycytidine kinase. It accumulates as cladribine triphosphate, which causes DNA strand breaks and apoptosis. Its effect is mainly in lymphocytes and monocytes, which have a high ratio of deoxycytidine kinase to 5'-nucleotidase.

Its proven activity is in lymphoid disease (hairy-cell leukaemia and multiple sclerosis). Rhabdomyosarcoma is a solid mesenchymal tumour and lacks this lymphocyte-specific enzyme profile. Activity there would be plausible only as a general cytotoxic effect.

The high score (0.998) most likely reflects proximity to other rhabdomyosarcoma-related terms in the knowledge graph, not a demonstrated mechanistic link. The same cluster produced several related predictions (embryonal rhabdomyosarcoma of the vagina, prostate and bile duct, rhabdomyosarcoma in general, and skeletal muscle neoplasm). None of them has clinical or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

Among the lower-ranked predictions, the only publication found is PMID [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) (2004, case report, *Der Hautarzt*). It describes successful cladribine therapy in smoldering systemic mastocytosis, linked to the "liver sarcoma" prediction. This is a haematologic neoplasm, so it does not support efficacy in rhabdomyosarcoma or liver sarcoma.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004230 | Mavenclad | Not specified | Treatment of adult patients with highly active relapsing multiple sclerosis (MS) as defined by clinical or imaging features. |
| EMEA/H/C/000504 | Litak | Not specified | Litak is indicated for the treatment of hairy-cell leukaemia. |

Both authorizations are listed as cancelled in the data compiled for this report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analogue / antimetabolite) |
| Myelosuppression Risk | High. Knowledge-graph contraindication links include neutropenia, thrombocytopenia, agranulocytosis and anaemia |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function (kidney disease appears among the knowledge-graph contraindications), and neurological status (peripheral neuropathy appears among them) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindications (knowledge-graph links, not label text)**: kidney disease, pyoureter, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, peripheral neuropathy, peripheral nervous system disease, hyperuricaemia.
- **Drug Interactions** (100 interactions recorded; main ones shown):
  - **Major**: systemic and other corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, triamcinolone, budesonide); deferiprone; radiopharmaceuticals and radioimmunotherapy agents (ibritumomab tiuxetan, iobenguane I-131, tositumomab, samarium-153 lexidronam, strontium-89 chloride).
  - **Moderate**: palifermin, dipyridamole, cilostazol, eltrombopag.

Label-based warnings and contraindications were not available. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score. There are no clinical trials or publications for rhabdomyosarcoma, and the pharmacology of cladribine (selective for lymphoid cells) does not clearly fit this tumour type. Both EU authorizations are cancelled, and the safety profile includes significant myelosuppression risk.

**To proceed, the following is needed:**
- Preclinical data on cladribine in rhabdomyosarcoma cell lines or models, including dCK and 5'-nucleotidase expression
- Mechanism of action data (MOA)
- Label-based warnings and contraindications from the SmPC
- Clarification of the current EU regulatory status, since both authorizations are cancelled
- Comparison against established rhabdomyosarcoma chemotherapy regimens
- A myelosuppression and immunosuppression risk assessment for a paediatric and young adult population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

