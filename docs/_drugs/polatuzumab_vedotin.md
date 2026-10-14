---
layout: default
title: Polatuzumab Vedotin
parent: AI Predictions (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Polatuzumab Vedotin
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

# Polatuzumab vedotin: From Diffuse Large B-Cell Lymphoma to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate originally used to treat diffuse large B-cell lymphoma (DLBCL).
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**, but **no clinical trials and no relevant publications** currently support this direction. The prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory DLBCL (with bendamustine and rituximab) in adults not eligible for haematopoietic stem cell transplant; previously untreated DLBCL (with R-CHP) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization in the compiled data) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, polatuzumab vedotin is an antibody-drug conjugate. It pairs an anti-CD79b antibody with the microtubule-disrupting agent monomethyl auristatin E (MMAE). Its efficacy in DLBCL has been established.

The link to HER2-positive breast carcinoma is weak. CD79b is a component of the B-cell receptor and is restricted to B-lineage cells. It is not a recognized target in HER2-positive breast cancer. The only conceivable connection is the generic cytotoxicity of MMAE, which would not be tumour-selective in this setting. The high TxGNN score therefore appears to be a graph-based computational signal without a supporting mechanistic or clinical rationale.

The other top predictions show the same pattern. They include other breast cancer subtypes, drug-induced osteoporosis, acne, and several coagulation disorders. None has retrieved trials, and none has a plausible CD79b-related mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications directly address HER2-positive breast carcinoma. The compiled data does contain 18 publications retrieved for another breast cancer prediction (luminal A or B). All of them concern DLBCL or other B-cell lymphomas, and none supports use in breast cancer. They are shown below only to illustrate the drug's established evidence base in its original indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34904799](https://pubmed.ncbi.nlm.nih.gov/34904799/) | 2022 | RCT | N Engl J Med | POLARIX: polatuzumab vedotin with R-CHP in previously untreated DLBCL |
| [40991874](https://pubmed.ncbi.nlm.nih.gov/40991874/) | 2025 | RCT (long-term follow-up) | J Clin Oncol | 5-year POLARIX update showing sustained progression-free survival benefit of Pola-R-CHP vs R-CHOP |
| [40085955](https://pubmed.ncbi.nlm.nih.gov/40085955/) | 2025 | RCT subgroup analysis | Blood Adv | POLARIX analysis in older patients (≥60 years) |
| [41037766](https://pubmed.ncbi.nlm.nih.gov/41037766/) | 2025 | Phase 3 | J Clin Oncol | SUNMO: mosunetuzumab plus polatuzumab vedotin in transplant-ineligible relapsed/refractory LBCL |
| [31693429](https://pubmed.ncbi.nlm.nih.gov/31693429/) | 2020 | Clinical trial | J Clin Oncol | Polatuzumab vedotin in relapsed/refractory DLBCL |
| [34749395](https://pubmed.ncbi.nlm.nih.gov/34749395/) | 2022 | Clinical trial update | Blood Adv | Polatuzumab vedotin plus bendamustine and rituximab in relapsed/refractory DLBCL: survival update and extension cohort |
| [38072960](https://pubmed.ncbi.nlm.nih.gov/38072960/) | 2024 | Phase 1b/2 | Nat Med | Mosunetuzumab plus polatuzumab vedotin in relapsed/refractory aggressive LBCL |
| [41115257](https://pubmed.ncbi.nlm.nih.gov/41115257/) | 2025 | Phase Ib/II | J Clin Oncol | Glofitamab plus polatuzumab vedotin in relapsed/refractory LBCL |
| [40995463](https://pubmed.ncbi.nlm.nih.gov/40995463/) | 2025 | Guideline | HemaSphere | EHA clinical practice guidelines for large B-cell lymphoma |
| [25925619](https://pubmed.ncbi.nlm.nih.gov/25925619/) | 2015 | Phase 1 | Lancet Oncol | Safety and activity in relapsed/refractory B-cell NHL and CLL |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004870 | Polivy | Not specified | Polivy in combination with bendamustine and rituximab is indicated for the treatment of adult patients with relapsed/refractory diffuse large B-cell lymphoma (DLBCL) who are not candidates for... |

The authorization status in the compiled data is "cancelled". Verify the current status against the official EMA register before relying on it.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate delivering a cytotoxic microtubule inhibitor (MMAE) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (the prediction rationale notes myelosuppression as a recognized toxicity) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Haematological parameters (CBC), signs of peripheral neuropathy and infection; please refer to the SmPC |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screen. The list reviewed contains these major-level interactions:
  - Clarithromycin
  - Cobicistat
  - Deferiprone
  - Samarium (153Sm) lexidronam

  Moderate-level interactions include aprepitant, cimetidine, metronidazole, miconazole, rosuvastatin, simvastatin, ticagrelor, chloroquine, hydroxychloroquine and disulfiram, among others.
- **Known toxicity profile (from the compiled prediction rationale)**: peripheral neuropathy, myelosuppression and infection risk.

Label warnings and contraindications were not available in the compiled data. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for HER2-positive breast carcinoma is supported only by the TxGNN score (Evidence Level L5). There are no clinical trials or relevant literature, and there is no plausible link between CD79b targeting and this tumour type. Established HER2-directed therapies already exist, and the toxicity of a cytotoxic ADC makes the risk-benefit balance unfavourable without supporting data.

**To proceed, the following is needed:**
- Evidence of CD79b (or another suitable target) expression in HER2-positive breast tumours
- Preclinical studies in HER2-positive breast cancer models
- Mechanism of action data and EU label warnings and contraindications
- Confirmation of the current EU authorization status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

