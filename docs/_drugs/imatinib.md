---
layout: default
title: Imatinib
parent: AI Predictions (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
last_modified_at: 2026-11-20
description: "Imatinib: predicted new indication heart fibrosarcoma (evidence level L5). Approved use: Imatinib Teva is indicated for the treatment of Adult and paediatric…"
---

# Imatinib
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

## Imatinib: tyrosine kinase inhibitor (BCR-ABL, KIT, PDGFR) → heart fibrosarcoma
{: .text-alpha }

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor that blocks BCR-ABL, KIT and PDGFR kinases.
The TxGNN model predicts it may be effective for **heart fibrosarcoma**, but **no clinical trials** are registered for this disease and only **1 publication** (a general commentary on new imatinib indications, stating the evidence is not robust) was retrieved, so this remains a model-based prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Imatinib Teva is indicated for the treatment of  Adult and paediatric patients with newly diagnosed Philadelphia chromosome (bcr?abl) positive (Ph+) chronic myeloid leukaemia (CML) for whom bone marrow transplantation is not considered as the first line of treatment. Adult and paediatric patients wi |
| Predicted New Indication | heart fibrosarcoma |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 3 of 7) |
| Number of Authorizations | 7 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for imatinib: "Imatinib mesylate is a protein-tyrosine kinase inhibitor that inhibits the BCR-ABL tyrosine kinase, the constitutive abnormal tyrosine kinase created by the Philadelphia chromosome abnormality in CML. Imatinib inhibits proliferation and induces apoptosis in BCR-ABL positive cell lines as well as fresh leukemic cells from Philadelphia chromosome positive chronic myeloid leukemia." ([DailyMed: Gleevec (imatinib mesylate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=211ef2da-2868-4a77-8055-1cb2cd78e24b), label version 2026-07-13; accessed 2026-11-19.) Based on what is known, imatinib inhibits PDGFR, KIT and ABL kinases.

Fibrosarcoma-type tumours may depend on PDGFB/PDGFR signalling, as seen in COL1A1-PDGFB-driven dermatofibrosarcoma protuberans. This gives a plausible mechanistic rationale for a tumour of fibroblastic origin arising in the heart. However, this link is unverified, and no cardiac-specific data are available.

The only publication retrieved is a general commentary on new imatinib indications, and it does not study heart fibrosarcoma. No cited study directly addresses the predicted disease, so the evidence level is L5 (model prediction only).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire international | Commentary on the expanding indications of imatinib (e.g. Ph+ acute lymphoblastic leukaemia); concludes that the evidence for the new indications is not robust. Does not address heart fibrosarcoma. |

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000406 | Glivec | imatinib | Valid |
| EMEA/H/C/002585 | Imatinib Teva | imatinib | Valid |
| EMEA/H/C/002681 | Imatinib Accord | imatinib | Valid |
| EMEA/H/C/002594 | Imatinib Actavis | imatinib | Withdrawn |
| EMEA/H/C/002692 | Imatinib medac | imatinib | Withdrawn |
| EMEA/H/C/004748 | Imatinib Teva B.V. | imatinib mesilate | Withdrawn |
| EMEA/H/C/005595 | Imatinib Koanaa | imatinib mesilate | Withdrawn |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions; blood counts and liver and renal function are commonly monitored for antineoplastic agents |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded in total. Major-level interactions include eliglustat and naloxegol. Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), pioglitazone, glimepiride, saxagliptin, aprepitant, morphine, cimetidine, clarithromycin, lansoprazole, dexlansoprazole, naltrexone, naldemedine and metreleptin.

For warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and a plausible but unverified PDGFR-based rationale. There are no trials, and the single publication retrieved does not study heart fibrosarcoma.

**To proceed, the following is needed:**
- Disease-specific evidence for cardiac fibrosarcoma (case series, preclinical or clinical data, and PDGFR/KIT dependence of the tumour)
- Detailed mechanism of action data
- Warnings and contraindications from the SmPC for safety screening
- A safety monitoring plan, including the interaction profile above

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Gleevec (imatinib mesylate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=211ef2da-2868-4a77-8055-1cb2cd78e24b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

