---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Dasatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dasatinib: From Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral BCR-ABL/Src family kinase inhibitor approved for the treatment of chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL).
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **2 clinical trials** and **8 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myeloid leukemia (CML); Ph+ acute lymphoblastic leukemia |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Taiwan Market Status | Not registered (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dasatinib's primary approved mechanism is inhibition of the BCR-ABL1 fusion protein — the oncogenic driver in CML — along with potent inhibition of Src family kinases (SFKs), c-KIT, and PDGFR. This multi-target kinase profile makes it roughly 325-fold more potent than imatinib against BCR-ABL in vitro. Formal MOA documentation from DrugBank was not retrieved in this evidence pack; the mechanistic description is derived from repurposing rationale and supporting literature.

The rationale for extending dasatinib to Ewing sarcoma centers on Src kinase dysregulation. Ewing sarcoma cells demonstrate constitutively elevated Src activity that drives invadopodia formation, cell migration, and metastatic invasion — processes critical to the disease's aggressive biology. In vitro studies have shown that dasatinib suppresses both proliferation and migration of Ewing sarcoma cell lines at nanomolar concentrations through blockade of c-KIT and PDGFR in addition to Src (PMID 18202781). The FAK-Src complex has been independently validated as a therapeutic target in Ewing sarcoma (PMID 35655525), and multiple groups have demonstrated that microenvironmental stress amplifies Src-dependent invasive behavior (PMID 31521948, 27566104), further supporting the mechanistic case.

Clinical translation, however, has been modest. The completed Phase 2 trial in advanced sarcomas (NCT00464620) tested dasatinib as a single agent across a mixed population; subgroup results for Ewing sarcoma did not demonstrate sufficient single-agent activity to support monotherapy development. The dedicated pediatric Ewing sarcoma trial (NCT00788125) was terminated after enrolling only 7 patients. The gap between compelling preclinical biology and limited clinical response is the central challenge for this repurposing direction, and suggests that combinatorial approaches or patient selection by Src expression status may be required.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric Ewing sarcoma: dasatinib combined with ifosfamide, carboplatin, and etoposide chemotherapy to enhance tumor cell kill. Terminated early with only 7 patients enrolled; termination reason undisclosed — no reliable efficacy conclusions can be drawn. |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Advanced sarcomas (mixed histology cohort including Ewing sarcoma): evaluated 6-month progression-free survival rate and overall response rate for dasatinib monotherapy. Largest completed trial in this space; primary publication review required to confirm Ewing sarcoma-specific subgroup outcomes. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical (in vitro) | Oncology Reports | Dasatinib shows antiproliferative and antimigratory activity in Ewing sarcoma and neuroblastoma cell lines; c-KIT and PDGFR identified as key molecular targets. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical (in vitro/in vivo) | Cancer Research | Dasatinib inhibits migration and invasion in diverse human sarcoma cell lines; induces apoptosis in bone sarcoma cells dependent on Src kinase for survival. Foundational sarcoma Src study. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preclinical/Mechanistic | Sarcoma | FAK-Src complex is a validated target in Ewing sarcoma, DSRCT, and rhabdomyosarcoma; confirms dasatinib single-agent failed in Phase 2 but supports rational combination strategies. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin-C and Src cooperate to drive invadopodia formation in Ewing sarcoma; microenvironmental stress amplifies Src-dependent invasion pathways. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Microenvironmental stress induces Src-dependent invadopodia activation and cell migration in Ewing sarcoma; supports Src as a key driver of metastatic progression. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Overview of Src signaling significance in sarcoma biology: expression patterns, role in proliferation/apoptosis/metastasis, and feasibility as a therapeutic target. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclinical | Cell Communication and Signaling | CXCR4 antagonist plerixafor activates receptor tyrosine kinase signaling in Ewing sarcoma cells; contextual evidence of RTK/Src pathway crosstalk in disease progression. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Current Treatment Options in Oncology | Systemic therapy options for chondrosarcoma, including antiangiogenic approaches; indirect relevance as comparative sarcoma treatment landscape reference. |

---

## Cytotoxicity

Dasatinib is an antineoplastic targeted therapy with cancer indications (CML, Ph+ ALL).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — BCR-ABL/Src/c-KIT/PDGFR tyrosine kinase inhibitor (2nd-generation TKI) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count (CBC) with differential; liver and renal function; pulmonary status (pleural effusion, including chylothorax, and interstitial pneumonitis have been reported in clinical literature) |
| Handling Protection | Standard oral antineoplastic handling precautions apply |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between dasatinib and Ewing sarcoma is biologically coherent — Src kinase dependency in Ewing sarcoma is well-established across multiple independent preclinical studies, and the drug's known Src inhibitory activity directly addresses this target. However, clinical evidence is limited to a completed mixed-sarcoma Phase 2 trial without definitive single-agent activity, and a dedicated Ewing sarcoma trial was terminated after only 7 patients. Evidence is sufficient to justify further investigation, but not to support clinical use without additional data.

**To proceed, the following is needed:**
- Retrieval of formal MOA and complete safety profile from DrugBank (Data Gaps DG001, DG002)
- Review of Ewing sarcoma–specific subgroup data from NCT00464620 primary publication to confirm response rates
- Clarification of termination reasons for NCT00788125 (safety-driven vs. enrollment failure changes the risk interpretation)
- Design of a combination trial (dasatinib + standard chemotherapy backbone such as ifosfamide/etoposide) in patients with molecularly confirmed Src overexpression or activation
- Biomarker strategy: define patient selection criteria based on Src/FAK expression or phosphorylation status to improve signal-to-noise in future trials
- Registration and safety monitoring plan for any Taiwan-based clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

