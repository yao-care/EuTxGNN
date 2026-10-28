---
layout: default
title: Venetoclax
parent: AI Predictions (L5)
nav_order: 663
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "Venetoclax"
predicted_indications: ["Hodgkins lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Ewing sarcoma", "follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma"]
description: "Venetoclax: predicted new indication Hodgkins lymphoma (evidence level L5). Approved use: Venclyxto in combination with obinutuzumab is indicated for the treat…"
---

# Venetoclax
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Venetoclax: Hodgkins lymphoma
{: .text-alpha }

## One-Sentence Summary

Venetoclax is a selective BCL-2 inhibitor, originally authorised in the EU for chronic lymphocytic leukaemia (CLL) and for newly diagnosed acute myeloid leukaemia (AML) in patients ineligible for intensive chemotherapy.
For this top-ranked prediction, the data compiled for this report contain **no registered clinical trials** and **1 publication** (a biological study of the B-cell receptor). Supporting evidence comes mainly from the approved CLL indication, not from studies of this subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Venclyxto in combination with obinutuzumab is indicated for the treatment of adult patients with previously untreated chronic lymphocytic leukaemia (CLL) (see section 5.1). Venclyxto in combination with rituximab is indicated for the treatment of adult patients with CLL who have received at least on |
| Predicted New Indication | Hodgkins lymphoma |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 (as assigned in the compiled data, based on the approved CLL indication; see note below) |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

*Note:* No trials are registered specifically for this predicted subtype. The L1 level reflects the strength of evidence in CLL as a whole (for example the Phase 3 MURANO trial), not subtype-specific studies.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank are not available in the compiled data. Venetoclax is nonetheless known as a selective, oral BCL-2 inhibitor. CLL cells depend on BCL-2 overexpression to survive, and blocking BCL-2 restores apoptosis.

The predicted indication is not a new disease. "Pregerminal center CLL/SLL" is the unmutated-IGHV subset of CLL, which is typically associated with a poorer prognosis. Venetoclax is already authorised in the EU for CLL, so this prediction is essentially a refinement of the existing indication. BCL-2 dependence is a general feature of CLL/SLL, and the approved CLL indication therefore applies directly.

The single publication identified (Forconi et al., 2022) is a review of tumour B-cell receptor structure and function in CLL. It explains the biology of the U-CLL and M-CLL subsets but does not test venetoclax.

The same CLL/SLL rationale applies to the second-ranked prediction, CLL/SLL with somatic hypermutation of the immunoglobulin heavy chain variable region (the mutated-IGHV subset).

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the predicted indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Biological/translational study | Cancers | Reviews how the tumour B-cell receptor shapes CLL biology and clinical behaviour, including the unmutated-IGHV (pre-germinal center, poorer prognosis) and mutated-IGHV (post-germinal center, better prognosis) subsets. It does not directly test venetoclax. |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004106 | Venclyxto | Not specified | Venclyxto in combination with obinutuzumab is indicated for the treatment of adult patients with previously untreated chronic lymphocytic... |


---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCL-2 inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interactions in total. Among the main ones listed, the following are classified as **Major**: aprepitant, dexamethasone, clarithromycin, eliglustat, rolapitant, fidaxomicin, cobicistat, deferiprone and samarium (153Sm) lexidronam. Moderate interactions include alvimopan, loperamide, cimetidine, miconazole, rifaximin and clotrimazole. Several of these (for example clarithromycin and cobicistat) are consistent with strong CYP3A inhibitors affecting venetoclax exposure.

Warnings and contraindications from the product label were not available. Please refer to the SmPC for the full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is a molecular subset of CLL/SLL, a disease for which venetoclax is already approved and supported by Phase 3 evidence. However, no trials or efficacy studies exist specifically for this subtype, and the EU authorisation is recorded as cancelled.

**To proceed, the following is needed:**
- Safety information from the SmPC (warnings and contraindications), which is currently a blocking gap
- Confirmation of the current EU authorisation status of Venclyxto
- Mechanism of action data from DrugBank
- Subtype-level (IGHV status) efficacy analyses from existing CLL trials
- A drug-interaction management plan, particularly for CYP3A inhibitors and inducers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

