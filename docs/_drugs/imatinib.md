---
layout: default
title: Imatinib
parent: Medium Evidence (L3-L4)
nav_order: 313
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Imatinib: predicted new indication Heart fibrosarcoma (evidence level L4). Approved use: Newly diagnosed Philadelphia chromosome-positive (Ph+) chronic myeloi…"
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Imatinib: From Chronic Myeloid Leukaemia to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor originally used to treat Philadelphia chromosome-positive chronic myeloid leukaemia (CML), as well as GIST and other conditions.
The TxGNN model predicts it may be effective for **heart fibrosarcoma**, but **no clinical trials** and only **1 general commentary article** currently support this direction, so the prediction rests mainly on model output.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Newly diagnosed Philadelphia chromosome-positive (Ph+) chronic myeloid leukaemia (CML), among others |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, imatinib inhibits the PDGFR, KIT and ABL kinases. Its efficacy in CML, GIST and dermatofibrosarcoma protuberans (DFSP) is established.

Fibrosarcoma-type tumours, including those arising in the heart, may depend on PDGFB/PDGFR signalling, as in DFSP, where a COL1A1-PDGFB fusion drives constitutive receptor activation. This gives a plausible but unverified rationale. No cardiac-specific data are available, and the single literature item is a general commentary stating that the evidence for new imatinib indications is not robust.

Other predicted indications from the same model run show how uneven the support is:

- **Fibroblastic neoplasm** (score 99.94%, L4, Proceed with Guardrails): this is dominated by DFSP, which is already an approved indication, so it confirms an existing label rather than a new repurposing finding.
- **Conventional fibrosarcoma** and **kidney fibrosarcoma**: the evidence is indirect, with no disease-specific efficacy data.
- **Liposarcoma**: three completed phase 1/2 or phase 2 soft tissue sarcoma trials exist, but liposarcoma is mostly driven by MDM2/CDK4 rather than KIT/PDGFR, so the mechanistic link is weak.
- Several other predictions (low grade fibromyxoid sarcoma, liver fibrosarcoma, familial Mediterranean fever, ovarian myxoid liposarcoma, familial rhabdoid tumour) have little or no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for heart fibrosarcoma.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire international | Commentary on imatinib's expanding indications, concluding that the evidence for the new indications is not robust. It is not specific to heart fibrosarcoma. |

## EU Market Information

All three authorizations are cancelled.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002585 | Imatinib Teva | Not specified | Imatinib Teva is indicated for the treatment of Adult and paediatric patients with newly diagnosed Philadelphia chromosome (bcr?abl) positive (Ph+)... |
| EMEA/H/C/000406 | Glivec | Not specified | Glivec is indicated for the treatment of adult and paediatric patients with newly diagnosed Philadelphia-chromosome (bcr-abl)-positive (Ph+) chro... |
| EMEA/H/C/002681 | Imatinib Accord | Not specified | Imatinib Accord is indicated for the treatment of adult and paediatric patients with newly diagnosed Philadelphia chromosome (bcr-abl) positive (Ph+)... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions. Haematological parameters, liver function and renal function are commonly monitored for this class. |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (derived from drug-disease relationship edges, not from label text): hypertension, liver failure and liver disease, kidney disease, congestive heart failure and heart failure, coronary artery disease, heart valve disease, congenital heart disease, pericardial effusion, pulmonary edema, brain edema, thrombocytopenia, neutropenia, agranulocytosis, anemia, diabetes mellitus, diabetic ketoacidosis, hyperbilirubinemia (including Gilbert syndrome), active peptic ulcer disease, gallbladder disease, hypophosphatemia, obesity disorder, and pyoureter.

These should be verified against the SmPC. Several cardiac entries are particularly relevant to a cardiac tumour indication.

**Drug Interactions**: 100 interactions were found in total. Examples from the 20 listed:
- **Major**: eliglustat, naloxegol
- **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), pioglitazone, glimepiride, saxagliptin, aprepitant, morphine, cimetidine, clarithromycin, lansoprazole, dexlansoprazole, naltrexone, naldemedine, metreleptin

Please refer to the SmPC for the full set of safety information, including warnings and contraindications.

A case report in the compiled literature describes a drug reaction with eosinophilia and systemic symptoms (DRESS) linked to imatinib in a patient with DFSP.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for heart fibrosarcoma is supported only by a model score, a plausible PDGFR-based mechanism, and a single general commentary that itself calls the evidence not robust. There are no trials, no cardiac-specific data, and no valid EU marketing authorization at present.

**To proceed, the following is needed:**
- Disease-specific evidence, such as case series, registry data or preclinical models of cardiac fibrosarcoma, including PDGFR/KIT dependence testing
- Mechanism of action data (DrugBank) and SmPC warnings and contraindications (EMA)
- A cardiac safety assessment, given the cardiac-related contraindication signals in the knowledge graph
- Clarification of the status of the cancelled EU authorizations, since no valid authorization is currently listed
- If the team wants a nearer-term candidate from this prediction list, review **fibroblastic neoplasm** (DFSP), though it is an existing label, and treat **liposarcoma** and **kidney fibrosarcoma** as research questions only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

