---
layout: default
title: Mitotane
parent: AI Predictions (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Mitotane
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

# Mitotane: From Adrenocortical Carcinoma to Multiple Endocrine Neoplasia

## One-Sentence Summary

Mitotane is an adrenolytic (adrenal-cortex-selective cytotoxic) agent whose established clinical use, based on the literature in this evidence pack, is **adrenocortical carcinoma (ACC)**. The TxGNN model predicts it may also be effective for **Multiple Endocrine Neoplasia (MEN)**, with **5 clinical trials** and **17 publications** currently associated with this signal — though most of this evidence actually documents mitotane's role in ACC rather than MEN itself, and should be interpreted with caution (see rationale below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenocortical Carcinoma (ACC) — inferred from literature in this pack (e.g., PMID 38608694: "Mitotane is the only approved therapy for adrenocortical carcinoma"); no structured Taiwan regulatory indication text is available |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.05% |
| Evidence Level | L3 (per evidence pack scoring) |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on the literature evidence collected, mitotane is known as an **adrenolytic agent** — it is selectively cytotoxic to adrenocortical cells and has been the mainstay treatment for adrenocortical carcinoma, though its use is "based on retrospective and occasionally conflicting evidence" (PMID 32098326).

The link between mitotane and "multiple endocrine neoplasia" in this prediction is likely driven by **ontological overlap rather than a genuine new pharmacological hypothesis**: MEN type 1 syndrome carries an elevated risk (1.4–6%) of developing adrenocortical carcinoma (PMID 31118348, PMID 30863550), and several case reports in the evidence set describe ACC arising in patients with MEN1 or Carney complex (a MEN-related syndrome). The knowledge graph appears to be picking up mitotane's well-established ACC signal and attributing it, via this comorbid overlap, to the broader "multiple endocrine neoplasia" disease label.

**Important caveat**: This is not, at present, evidence that mitotane treats MEN syndromes directly. It reflects mitotane's already-confirmed role in treating ACC, a tumor type that sometimes occurs within MEN syndromes. Any regulatory or clinical development decision based on this prediction should explicitly clarify whether the target population is "ACC arising in MEN patients" versus "MEN syndrome" as a whole, since these are pharmacologically distinct claims.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00568139](https://clinicaltrials.gov/study/NCT00568139) | N/A (Observational) | Active, not recruiting | 400 | Directly evaluates adverse effects of mitotane therapy in ACC patients — the most directly mitotane-relevant trial in this set (Grade A relevance). |
| [NCT00453674](https://clinicaltrials.gov/study/NCT00453674) | N/A (Registry) | Recruiting | 1000 | German Adrenocortical Carcinoma Registry; large real-world dataset for treatment/prognosis, but non-interventional and not mitotane-specific (Grade B). |
| [NCT00778817](https://clinicaltrials.gov/study/NCT00778817) | Phase 2 | Terminated | 20 | IMC-A12 (anti-IGF1R monoclonal antibody) + mitotane vs. mitotane alone in inoperable/metastatic ACC; direct mitotane comparator arm, but study was terminated (Grade C). |
| [NCT07085572](https://clinicaltrials.gov/study/NCT07085572) | Phase 2 | Recruiting | 31 | Cemiplimab maintenance immunotherapy in advanced ACC after first-line chemotherapy (which typically includes mitotane); not a mitotane trial itself (Grade C). |
| [NCT04318730](https://clinicaltrials.gov/study/NCT04318730) | Phase 2 | Recruiting | 21 | Camrelizumab + Apatinib as second-line therapy in recurrent/metastatic ACC after mitotane-based first-line failure; not mitotane-specific (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38608694](https://pubmed.ncbi.nlm.nih.gov/38608694/) | 2024 | RCT (non-mitotane) | Lancet Oncology | Phase 2 cabozantinib monotherapy trial in advanced ACC; notes mitotane as "the only approved therapy for adrenocortical carcinoma." |
| [33875173](https://pubmed.ncbi.nlm.nih.gov/33875173/) | 2020 | Review | Endocrine Practice | AACE clinical review on evaluation and management of ACC in adults. |
| [32098326](https://pubmed.ncbi.nlm.nih.gov/32098326/) | 2020 | Review | Cancers | Reviews adjuvant therapy in ACC; mitotane has been the mainstay adjuvant therapy but evidence base is retrospective and mixed. |
| [35317446](https://pubmed.ncbi.nlm.nih.gov/35317446/) | 2022 | Review | Exp Ther Med | Pediatric aspects of ACC, an orphan malignancy often presenting with hormonal syndromes. |
| [30798468](https://pubmed.ncbi.nlm.nih.gov/30798468/) | 2019 | Review | Curr Oncol Rep | Summary of current clinical management approaches for ACC. |
| [37435451](https://pubmed.ncbi.nlm.nih.gov/37435451/) | 2022 | Review | Endocrine Oncology | Adjuvant therapy in ACC — prognostic factors and treatment options, mostly retrospective evidence. |
| [25402388](https://pubmed.ncbi.nlm.nih.gov/25402388/) | 2015 | Cohort | Hormones (Athens) | 10-year follow-up of low-dose mitotane regimen correcting hypercortisolism in Carney complex (a MEN-related syndrome). |
| [31118348](https://pubmed.ncbi.nlm.nih.gov/31118348/) | 2019 | Case Report | Endocrine Journal | Myxoid variant ACC in a patient with MEN type 1; notes 1.4–6% ACC incidence in MEN1 patients. |
| [30863550](https://pubmed.ncbi.nlm.nih.gov/30863550/) | 2019 | Case Report | Oxford Med Case Rep | Metastatic ACC case, noting association with familial syndromes including MEN1. |
| [22355500](https://pubmed.ncbi.nlm.nih.gov/22355500/) | 2011 | Case Report | Rare Tumors | Aldosterone-secreting metastatic ACC treated with adjuvant mitotane chemotherapy. |

---

## EU/Taiwan Market Information

Mitotane is currently **not marketed** in Taiwan and no marketing authorizations are recorded in this evidence pack (0 licenses).

---

## Cytotoxicity

Mitotane is a conventional cytotoxic agent (adrenolytic class), used as chemotherapy for adrenocortical carcinoma.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (adrenolytic agent, adrenal-cortex-selective) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence for mitotane in adrenocortical carcinoma is well established and includes an observational trial directly studying its adverse effects (NCT00568139), but the specific "multiple endocrine neoplasia" prediction is likely a disease-ontology overlap artifact rather than a distinct new indication — the underlying clinical signal is ACC occurring within MEN syndromes, not MEN treatment itself.

**To proceed, the following is needed:**
- Clarify whether the intended target population is "ACC in MEN1/Carney complex patients" versus "MEN syndrome" broadly, before advancing this candidate
- Obtain formal mechanism of action (MOA) data from DrugBank (DG002)
- Obtain TFDA/SmPC label warnings and contraindications, currently blocked (DG001)
- Confirm Taiwan/EU regulatory and market authorization status, since none are currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

