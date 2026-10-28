---
layout: default
title: Temsirolimus
parent: AI Predictions (L5)
nav_order: 598
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Temsirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "vulva sarcoma"]
description: "Temsirolimus: predicted new indication Liposarcoma (evidence level L5). Approved use: Renal-cell carcinoma Torisel is indicated for the first-line treatmen…"
---

# Temsirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Temsirolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Temsirolimus was originally authorised in the EU for advanced renal-cell carcinoma and relapsed or refractory mantle-cell lymphoma.
The TxGNN model predicts it may be effective for **liposarcoma**,
but only **2 indirect clinical trials** (mixed sarcoma populations, combination regimens) and **1 review article** currently relate to this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal-cell carcinoma Torisel is indicated for the first-line treatment of adult patients with advanced renal-cell carcinoma (RCC) who have at least three of six prognostic risk factors. Mantle-cell lymphoma Torisel is indicated for the treatment of adult patients with relapsed and / or refractory ma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 (see note below) |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

*Note on the evidence level: the data compiled for this report assign L2 to liposarcoma, but this is generous. The two Phase 1/2 and Phase 2 trials enrolled mixed sarcoma populations and combination regimens, and no completed Phase 2/3 RCT is specific to liposarcoma. In practice the evidence is closer to indirect and exploratory.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Temsirolimus is a known mTOR inhibitor, and its efficacy in advanced renal-cell carcinoma and mantle-cell lymphoma has led to regulatory approval.

The PI3K/AKT/mTOR pathway is commonly activated in soft tissue sarcomas, including liposarcoma subtypes such as MDM2/CDK4-amplified well-differentiated and dedifferentiated disease. This gives a plausible mechanistic reason to test an mTOR inhibitor in this setting.

The supporting evidence is still indirect. The listed trials enrolled mixed sarcoma populations rather than liposarcoma specifically, so subtype-specific efficacy has not been established. The high TxGNN score should be read as a hypothesis, not as proof of benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/Phase 2 | Completed | 24 | Temsirolimus plus liposomal doxorubicin in recurrent advanced soft tissue and bone sarcomas. It aimed to identify a safe dose and assess efficacy. Liposarcoma may be among the enrolled histologies, but the drug-specific contribution is unclear. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab plus temsirolimus in a pediatric population with recurrent or refractory solid tumours, including sarcoma. Its applicability to adult liposarcoma is limited. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | Reviews targeted treatments for rare connective tissue tumours and sarcomas, grouped by molecular subtype. It is not specific to temsirolimus in liposarcoma. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000799 | Torisel | Not specified | Renal-cell carcinoma: first-line treatment of adult patients with advanced RCC who have at least three of six prognostic risk factors. Mantle-cell lymphoma: relapsed and/or refractory... |

The only EU authorisation is recorded as cancelled.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for safety information.

- **Contraindication signals from the knowledge graph (not label text):** The TxGNN knowledge graph links temsirolimus to contraindication edges with kidney disease, liver disease, gallbladder disease, hyperglycaemia and diabetes (including diabetic ketoacidosis), hyperlipidaemia (including familial), stroke and cerebrovascular disorders, cerebral infarction, hyperbilirubinaemia (including Gilbert syndrome), interstitial lung disease, and several brain tumours (including astrocytoma subtypes and oligodendroglial tumour). These need confirmation against the official label.
- **Drug interactions:** The query returned 100 interactions in total. Major-level interactions among those listed include:
  - Amphotericin B (including the lipid complex)
  - Dexamethasone
  - Clarithromycin

  Moderate-level interactions include antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide) and corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide), as well as aprepitant, cimetidine, mesalazine and balsalazide.
- This is relevant to intestinal and retroperitoneal sites.

## Other Predicted Indications (for Context)

| Predicted Indication | TxGNN Score | Evidence Level | Evidence Summary |
|------|------|------|------|

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mTOR rationale for soft tissue sarcoma is plausible, but the available trials are mixed-population, combination-based and not specific to liposarcoma. No liposarcoma-specific efficacy data exist. Temsirolimus's EU authorisation is cancelled, and label-level safety data are missing. Clinical development is not supported on the current evidence, though liposarcoma remains a reasonable research question.

**To proceed, the following is needed:**
- Subtype-level (liposarcoma) results from NCT00949325 and the published soft-tissue sarcoma Phase 2 data
- Mechanism of action data (MOA) from DrugBank
- Warnings and contraindications from the EMA package insert, which are a blocking gap for safety screening
- Review of the knowledge-graph contraindication signals and the major drug interactions, especially bowel perforation risk
- Clarification of why the EU authorisation was cancelled, and of the regulatory route for any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

