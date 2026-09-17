---
layout: default
title: Temsirolimus
parent: High Evidence (L1-L2)
nav_order: 577
evidence_level: L2
indication_count: 10
---

# Temsirolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Temsirolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Temsirolimus is an mTOR inhibitor originally approved for the treatment of renal cell carcinoma (RCC). The TxGNN model predicts it may also be effective for **Liposarcoma**, with **5 clinical trials** (2 using temsirolimus/Torisel directly) and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (RCC) — not present in the local regulatory dataset, but consistently referenced across the supporting clinical/literature evidence as the approved indication |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L2 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not present in the structured drug record (flagged as a High-severity data gap). However, across the supporting clinical trial and literature evidence, Temsirolimus is consistently described as a selective inhibitor of mTORC1 (mammalian target of rapamycin complex 1), which blocks the PI3K/AKT/mTOR signaling pathway. This pathway is one of the central drivers of cell growth, proliferation, and survival, and Temsirolimus is approved for metastatic renal cell carcinoma, where dysregulated mTOR/HIF signaling drives tumor progression.

Liposarcoma — particularly the dedifferentiated subtype — frequently shows activation of the same PI3K/AKT/mTOR pathway. This shared molecular vulnerability is the mechanistic basis for repurposing mTOR-pathway inhibitors into soft-tissue sarcoma treatment. Multiple drugs in the same rapalog/mTOR-inhibitor class (sirolimus, everolimus, ridaforolimus) have already been tested in liposarcoma and related sarcoma subtypes, and Temsirolimus itself (as Torisel) has direct clinical evidence in advanced soft-tissue and bone sarcoma populations, reinforcing the biological plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus in pediatric recurrent/refractory sarcoma; direct temsirolimus evidence (Grade A) |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus) + liposomal doxorubicin in advanced soft tissue and bone sarcoma; dose-finding and efficacy assessment (Grade A, direct evidence) |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus (parent compound, not temsirolimus) + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; mTOR inhibition prevented tumor growth in preclinical models (Grade B, class-effect evidence) |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (mTOR inhibitor class, not temsirolimus) in advanced dedifferentiated liposarcoma and leiomyosarcoma (Grade B, class-effect evidence) |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor, AP23573) monotherapy in advanced sarcoma (Grade B, class-effect evidence) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Review of targeted treatment strategies for rare connective tissue tumors and sarcomas, including mTOR-pathway-directed therapies relevant to liposarcoma subtypes |

---

## EU Market Information

No EU marketing authorization is currently on record for Temsirolimus in this dataset (0 authorizations, market status: not marketed). This should be confirmed against the EMA product register, since Temsirolimus (Torisel) has historically held EU authorization for renal cell carcinoma and mantle cell lymphoma.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (rapalog class) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: A case report (PMID [24830996](https://pubmed.ncbi.nlm.nih.gov/24830996/)) describes bowel perforation associated with temsirolimus use in a recently irradiated patient with uterine leiomyosarcoma — this is a safety signal from the broader evidence set, not a confirmed contraindication, and should be reviewed alongside the official SmPC.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temsirolimus has direct clinical evidence (Torisel) in advanced soft-tissue and bone sarcoma populations, and mechanistically plausible class-effect evidence from other mTOR inhibitors specifically in liposarcoma. However, no trial to date has tested temsirolimus specifically and exclusively in a liposarcoma-confirmed cohort, and key safety/regulatory data are still missing.

**To proceed, the following is needed:**
- TFDA/EMA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Formal mechanism of action (MOA) documentation from DrugBank or equivalent source
- Confirmation of current EU marketing authorization status (dataset shows 0 licenses / not marketed, which should be reconciled with EMA records)
- A liposarcoma-subtype-specific trial or expanded-access data, since existing direct temsirolimus evidence is in mixed sarcoma populations rather than liposarcoma alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

