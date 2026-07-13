---
layout: default
title: Dacomitinib
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Dacomitinib
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

# Dacomitinib: From Non-Small Cell Lung Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Dacomitinib (Vizimpro) is an irreversible pan-HER inhibitor approved internationally for first-line treatment of EGFR-mutated non-small cell lung cancer (NSCLC), though it has not received marketing authorization in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** with a prediction score of **97.79%**,
however **no clinical trials or published literature** currently support this repurposing direction — making it an L5 (model prediction only) candidate at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | EGFR-mutated NSCLC (FDA/EMA approved internationally; not registered in Taiwan) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 97.79% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on published pharmacology, Dacomitinib is an irreversible covalent inhibitor of the entire HER (ErbB) receptor family — specifically EGFR (HER1), HER2, and HER4 — distinguished from first-generation EGFR inhibitors by its broader target coverage and covalent binding mechanism. Its proven efficacy in EGFR-mutated NSCLC stems from permanently blocking oncogenic EGFR signaling that drives tumor cell proliferation and survival.

The theoretical link to rheumatoid arthritis (RA) rests on EGFR expression in synovial fibroblast-like synoviocytes (FLS), which are key mediators of joint destruction in RA. EGFR signaling promotes FLS proliferation, invasiveness, and pro-inflammatory cytokine secretion. In principle, pan-HER inhibition could attenuate synovial hyperplasia and reduce articular inflammation — a hypothesis that has driven interest in EGFR inhibitors for autoimmune joint disease more broadly.

However, this mechanistic link is distant and remains entirely unvalidated for Dacomitinib. First-generation EGFR inhibitors (erlotinib, gefitinib) have been explored in inflammatory arthritis models with inconsistent results. The TxGNN prediction most likely reflects shared pathway topology in the knowledge graph rather than direct biological evidence. There is currently no preclinical or clinical data to support this specific repurposing direction.

> **Actionable note:** Among Dacomitinib's top 10 TxGNN predictions, **Pulmonary Arterial Hypertension (PAH, rank 4, score 96.51%)** carries the strongest mechanistic rationale and is the only prediction with direct preclinical evidence — EGFR signaling drives pulmonary artery smooth muscle cell (PASMC) proliferation, the core pathological mechanism of PAH, and one animal study (PMID 30753867, see Literature Evidence below) has directly demonstrated Dacomitinib's efficacy in PAH models. This direction may warrant prioritization over RA.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for **rheumatoid arthritis**.

---

**Supporting data for PAH direction (Rank 4 prediction):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01121575](https://clinicaltrials.gov/study/NCT01121575) | Phase 1 | Completed | 70 | Dacomitinib + crizotinib (cMET inhibitor) combination dose-escalation study in advanced NSCLC — not a PAH study, but provides human PK parameters, tolerability profile, and maximum tolerated dose data that would directly inform future PAH trial design |

---

## Literature Evidence

Currently no related literature available for **rheumatoid arthritis**.

---

**Supporting data for PAH direction (Rank 4 prediction):**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30753867](https://pubmed.ncbi.nlm.nih.gov/30753867/) | 2019 | Preclinical/Animal Study | European Journal of Pharmacology | Dacomitinib significantly attenuated pulmonary vascular remodeling and right ventricular hypertrophy in both hypoxia-induced and monocrotaline-induced PAH rat models; provides direct mechanistic validation that pan-EGFR inhibition can reverse PAH-associated vascular pathology |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Irreversible pan-HER/ErbB tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low (less myelosuppressive than conventional chemotherapy; mild neutropenia may occur) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential; liver function (ALT/AST/bilirubin); renal function; electrolytes; skin toxicity surveillance (dermatitis acneiform is the most common class effect); diarrhea grading; mucositis assessment |
| Handling Protection | Standard oral targeted therapy precautions apply; cytotoxic drug handling protocols recommended per institutional policy |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (rheumatoid arthritis) has no supporting preclinical or clinical evidence; the mechanistic connection between pan-HER inhibition and RA synoviocyte pathology remains a theoretical inference without experimental validation, and issuing a Go or Proceed recommendation would be premature.

**To proceed, the following is needed:**

- **Redirect primary investigation to PAH**: Pulmonary arterial hypertension (rank 4) has direct preclinical evidence (PMID 30753867) demonstrating Dacomitinib efficacy in rat models, a coherent mechanistic rationale (EGFR-driven PASMC proliferation = PAH core pathology), and an existing human safety/PK dataset (NCT01121575) — this is a substantially more actionable repurposing hypothesis
- **MOA documentation**: Retrieve full pharmacological profile from DrugBank (DB11963) to support mechanistic analysis for all predicted indications
- **Safety data**: Obtain TFDA package insert (or EMA SmPC for Vizimpro) to complete warnings, contraindications, and DDI assessment before any S1 safety evaluation
- **RA preclinical study**: If RA direction is to be further evaluated, FLS/synoviocyte EGFR inhibition studies with Dacomitinib specifically (not first-generation EGFR inhibitors) are required as a prerequisite
- **Taiwan registration pathway**: If PAH evidence matures to Phase 2 level, evaluate Taiwan NDA pathway given current 未上市 status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

