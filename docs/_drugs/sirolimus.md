---
layout: default
title: Sirolimus
parent: High Evidence (L1-L2)
nav_order: 544
evidence_level: L2
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Immunosuppression (Organ Transplant Rejection) to Liposarcoma

## One-Sentence Summary

> Sirolimus (rapamycin) is an mTOR inhibitor best known as an immunosuppressant used to prevent renal transplant rejection.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **5 clinical trials** and **12 publications** currently supporting this direction — including a completed Phase 2 trial testing sirolimus itself in this tumor type.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immunosuppression / prevention of organ (renal) transplant rejection — based on known drug-class information; no formal EU label text is on file since the drug is not marketed in the EU per this evidence pack |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this evidence pack (flagged as a High-severity data gap, DG002). However, across the supporting evidence, Sirolimus is consistently described as an **mTOR (mechanistic target of rapamycin) inhibitor** — the same molecular target it engages clinically as an immunosuppressant, where it blocks mTORC1-driven T-cell proliferation to prevent transplant rejection.

Dedifferentiated liposarcoma (DDL) and related soft tissue sarcomas show constitutive activation of the **Akt-mTOR and MAPK signaling pathways** (PMID 26518767). Because this is the same pathway sirolimus dampens in its immunosuppressive role, there is a plausible mechanistic bridge between its original indication and this oncology application: a pathway that is therapeutically *suppressed* in transplant patients is *aberrantly hyperactivated* in this tumor type, providing rationale for an antiproliferative effect.

This is reinforced by direct clinical evidence — **NCT02821507** tested sirolimus itself (not an analog) in a completed Phase 2, single-arm trial in myxoid liposarcoma and chondrosarcoma (n=70). Related mTOR-class agents (temsirolimus, everolimus, ridaforolimus) have also been evaluated in overlapping sarcoma populations across several Phase 1/2 trials, further supporting the class-wide mechanistic plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Direct Sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; single-arm, mTOR inhibition rationale based on preclinical in vivo data |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor) in advanced sarcoma; large sample, completed |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + Everolimus (mTOR inhibitor) in advanced dedifferentiated liposarcoma (DDL) and leiomyosarcoma (LMS) |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + Temsirolimus (sirolimus prodrug) in pediatric recurrent/refractory sarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus + liposomal doxorubicin in advanced soft tissue and bone sarcoma; dosing and efficacy assessment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT | Clin Cancer Res | SAR-096: Ribociclib + Everolimus in DDL and LMS; synergistic growth inhibition supports mTOR-pathway targeting |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Review of novel/targeted therapeutics in soft tissue sarcoma |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort | J Am Soc Nephrol | Sirolimus-based regimen (vs. cyclosporine) reduced malignancy risk in renal transplant recipients, supporting antineoplastic potential of mTOR inhibition |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Preclinical/Mechanism | Tumour Biol | Akt-mTOR and MAPK pathway activation demonstrated in 99 dedifferentiated liposarcoma specimens; in vitro mTOR inhibitor antitumor effect |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Chloroquine + rapamycin combination effective against well-differentiated liposarcoma via autophagy inhibition |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of new molecular-targeted treatments for advanced sarcomas |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Review of targeted treatment strategies across molecularly-defined sarcoma subgroups |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | MLN0128, an ATP-competitive mTOR kinase inhibitor, shows potent antitumor activity in bone/soft-tissue sarcoma models |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical (PDOX model) | In Vivo | Chloroquine + rapamycin arrests tumor growth in a dedifferentiated liposarcoma patient-derived xenograft mouse model |
| [20534289](https://pubmed.ncbi.nlm.nih.gov/20534289/) | 2010 | Case Series | Transplant Proc | Conversion to rapamycin immunosuppression after malignancy diagnosis in kidney transplant recipients |

---

## EU Market Information

Currently not marketed in the EU — no marketing authorizations are on file for this evidence pack (0 authorizations).

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (flagged as a Blocking-severity data gap, DG001) — this must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, direct Phase 2 trial of sirolimus itself in liposarcoma (NCT02821507), combined with mechanistic evidence of Akt-mTOR pathway activation in dedifferentiated liposarcoma, supports an L2 evidence rating. However, this rests on a single non-randomized trial rather than a confirmatory RCT, and critical drug-level safety and regulatory data remain unresolved.

**To proceed, the following is needed:**
- TFDA/EMA product label warnings and contraindications (Blocking gap, DG001)
- Formal mechanism-of-action documentation from DrugBank (High-priority gap, DG002)
- A regulatory access pathway assessment, since Sirolimus currently holds 0 EU marketing authorizations (named-patient import, off-label use, or new authorization)
- Confirmation that oncology dosing/route requirements are compatible with existing formulations approved for transplant indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

