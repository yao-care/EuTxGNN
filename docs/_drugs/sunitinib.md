---
layout: default
title: Sunitinib
parent: High Evidence (L1-L2)
nav_order: 558
evidence_level: L2
indication_count: 10
---

# Sunitinib
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

# Sunitinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sunitinib is an established multi-targeted tyrosine kinase inhibitor used to treat renal cell carcinoma (RCC) and gastrointestinal stromal tumours (GIST) by blocking VEGFR, PDGFR, and KIT.
The TxGNN model predicts it may also be effective for **Liposarcoma**, a soft-tissue sarcoma,
with **3 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (RCC) / GIST — Sunitinib's established, globally approved indication (confirmed by trial annotations in this evidence pack, e.g., NCT01254864: *"Sunitinib malate is FDA-approved for the treatment of gastrointestinal tumors and renal cell carcinoma"*); not itself recorded as a formal license in this EU dataset |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed (no authorization currently tracked in this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question (interim stage — more evidence needed before Guardrails) |

> **Note on data quality:** This candidate record (`TW-DB01268-multi`) contains ten TxGNN-predicted indications for Sunitinib. One of them — rank 9, "renal carcinoma" (L1, Proceed with Guardrails) — is flagged in its own rationale as **not a genuine new indication**: it is Sunitinib's already-established approved use, misclassified as "new" because the original-indication field in this database is empty. This report focuses on the top-ranked genuinely novel candidate, **liposarcoma**, but this data gap should be corrected before any downstream use of the full candidate list.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for Sunitinib is marked as a data gap in the structured drug record. However, mechanistic annotations embedded in the evidence pack consistently describe Sunitinib as a multi-targeted oral tyrosine kinase inhibitor (TKI) that blocks VEGFR, PDGFR, and KIT — the same pathway-inhibition profile responsible for its efficacy in RCC and GIST.

Liposarcoma is a soft-tissue sarcoma, and several soft-tissue sarcoma subtypes (including liposarcoma, leiomyosarcoma, and malignant fibrous histiocytoma) show angiogenesis dependence and, in some cases, PDGFR-driven proliferation — mechanistically overlapping with Sunitinib's known targets. This provides a plausible pharmacological bridge from RCC/GIST to liposarcoma.

This plausibility is supported by direct clinical testing: two completed Phase II trials (NCT00400569, NCT00474994) specifically enrolled liposarcoma patients within broader soft-tissue sarcoma cohorts, and a dedicated Phase II study (PMID 21154746) reported on Sunitinib's activity in a liposarcoma-containing cohort. A case report (PMID 23482782) further describes long-lasting clinical benefit in a heavily pre-treated metastatic liposarcoma patient, reinforcing that the mechanistic rationale has some early clinical corroboration, though not yet at the level of a dedicated randomized trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label single-site study of Sunitinib in unresectable/metastatic soft-tissue sarcoma, explicitly including liposarcoma, leiomyosarcoma, fibrosarcoma, and malignant fibrous histiocytoma (MFH). |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing study of Sunitinib in non-GIST sarcomas, covering metastatic, locally advanced, or recurrent disease, including liposarcoma subgroups. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 basket protocol testing **regorafenib** (not Sunitinib) across selected sarcoma subtypes; included as indirect supporting evidence for TKI-class activity in sarcoma, based on precedent from sunitinib/sorafenib/pazopanib activity in soft-tissue sarcoma. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase II single-arm | International Journal of Cancer | Phase II study of Sunitinib in relapsed/refractory soft-tissue sarcoma, focusing on leiomyosarcoma, liposarcoma, and malignant fibrous histiocytoma; reports safety and efficacy in these histologies. |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case report | Anticancer Research | Describes long-lasting clinical benefit of Sunitinib in a heavily pre-treated patient with metastatic liposarcoma. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review (molecular) | Cancers | Reviews genetic, epigenetic, and transcriptomic alterations in liposarcoma relevant to selecting targeted therapies. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven soft-tissue sarcoma treatment review; notes particularly high trabectedin activity in myxoid liposarcoma and general rationale for subtype-specific targeted agents. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Review of Anticancer Therapy | Reviews emerging targeted therapies (including TKIs) for adult soft-tissue sarcoma. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Reviews medical treatment of soft-tissue sarcomas stratified by histological subtype. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Molecular profiling | Oncotarget | Next-generation sequencing of extraskeletal myxoid chondrosarcoma; evaluates predictive factors for Sunitinib benefit in a related sarcoma subtype. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Case series | American Journal of Surgical Pathology | Clinicopathologic analysis of a distinct myofibroblastic sarcoma subtype; broader sarcoma-classification context rather than direct liposarcoma data. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol (regorafenib) | BMC Cancer | Protocol for the REGOSARC trial of regorafenib in advanced soft-tissue sarcoma; cites sunitinib-refractory GIST precedent for angiogenesis-targeted therapy in sarcoma. |

---

## EU Market Information

No EU marketing authorizations for Sunitinib are currently recorded in this dataset (`total_licenses: 0`, `market_status: Not Marketed`). This is inconsistent with Sunitinib's well-documented global oncology approval status referenced elsewhere in this evidence pack (e.g., trial NCT01254864 describes it as FDA-approved for GIST and RCC), and should be treated as a regulatory data gap requiring verification rather than an indication that the drug is genuinely unavailable in the EU.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — multi-targeted oral tyrosine kinase inhibitor (VEGFR/PDGFR/KIT inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Not specified in the current evidence pack; please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Not specified in the current evidence pack; please refer to the SmPC warnings and precautions |
| Monitoring Items | Blood pressure (hypertension is a documented class effect of multikinase inhibitors including Sunitinib, per PMID 28230776 and PMID 31547602), thyroid function (hypothyroidism was tracked as a secondary outcome in NCT00684645), complete blood count, and liver/renal function |
| Handling Protection | Oral capsule formulation; institutional policies for oral targeted anticancer agents commonly still require cytotoxic-safe handling and dispensing precautions — refer to local institutional protocol |

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-interaction data for this candidate have not yet been retrieved (this is flagged as a **Blocking** data gap — DG001 — preventing a formal Stage 1 safety assessment).

---

## Conclusion and Next Steps

**Decision: Research Question** (intermediate stage — insufficient for "Proceed with Guardrails," but stronger than a simple "Hold")

**Rationale:**
Two completed Phase II trials and a supportive case report demonstrate that Sunitinib has documented activity in liposarcoma-containing soft-tissue sarcoma cohorts, and the VEGFR/PDGFR/KIT mechanism provides a plausible biological rationale. However, no trial has isolated liposarcoma as a primary endpoint, and blocking safety data gaps prevent formal risk-benefit assessment at this stage.

**To proceed, the following is needed:**
- TFDA/EU SmPC warnings, precautions, and contraindications (Blocking gap — DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-priority gap — DG002)
- Verification of Sunitinib's true EU marketing/authorization status, given the apparent inconsistency between "Not Marketed" and its known global oncology approval
- Liposarcoma-specific subgroup efficacy data (rather than pooled soft-tissue sarcoma basket-trial results)
- A completed drug-drug interaction (DDI) review (current status: not found)
- Correction of the "renal carcinoma" entry elsewhere in this candidate set, which the evidence pack itself identifies as a misclassified pre-existing indication rather than a genuine repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

