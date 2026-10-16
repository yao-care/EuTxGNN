---
layout: default
title: Ivosidenib
parent: AI Predictions (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ivosidenib: predicted new indication Bulbar polio (evidence level L5). Approved use: Newly diagnosed IDH1 R132-mutated AML (with azacitidine…"
monitor_inn: "Ivosidenib"
predicted_indications: ["bulbar polio", "acute myeloid leukemia and myelodysplastic syndromes related to alkylating agent", "acute myeloid leukemia and myelodysplastic syndromes related to radiation", "5q35 microduplication syndrome", "neuralgic amyotrophy", "amyotrophic neuralgia", "myelodysplastic/myeloproliferative disease", "acute panmyelosis with myelofibrosis", "bilineal acute myeloid leukemia", "familial thrombocytosis"]
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutant AML and Cholangiocarcinoma to Bulbar Polio

## One-Sentence Summary

Ivosidenib is a targeted inhibitor of mutant IDH1, originally used for IDH1 R132-mutated acute myeloid leukaemia (AML) and cholangiocarcinoma.
The TxGNN model's top-ranked prediction is **bulbar polio**, but there are **0 clinical trials** and **0 publications** supporting it, so it is very likely a model artifact.
The more credible repurposing direction is **myelodysplastic/myeloproliferative disease** (the best-supported candidate, with **3 clinical trials**), discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Newly diagnosed IDH1 R132-mutated AML (with azacitidine, for patients not eligible for standard induction chemotherapy); previously treated, locally advanced or metastatic IDH1 R132-mutated cholangiocarcinoma (monotherapy) |
| Predicted New Indication | Bulbar polio (rank 1) |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (marketing authorization cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ivosidenib inhibits mutant IDH1 (R132), an alteration relevant to certain cancers, and its efficacy in IDH1-mutant AML and cholangiocarcinoma is the basis of its approval.

For **bulbar polio**, no plausible mechanistic link exists. Polio is a viral infection of motor neurons, whereas ivosidenib acts on a tumour-associated metabolic enzyme mutation. The high score (0.993) is a graph-based result with no supporting clinical or literature evidence and is likely a model artifact. The same applies to other top-ranked predictions with no mechanistic rationale: 5q35 microduplication syndrome, neuralgic amyotrophy, amyotrophic neuralgia and familial thrombocytosis.

By contrast, several lower-ranked predictions are biologically plausible because they are myeloid neoplasms that can carry IDH1 R132 mutations:

- **Myelodysplastic/myeloproliferative disease** (score 98.56%): the strongest-supported candidate. Evidence level L2 by the model's scoring, though the available trials are Phase 1/2 and Phase 2 studies that are not specific to this disease, so the evidence is only partial.
- **Therapy-related AML/MDS** (alkylating-agent-related and radiation-related, both 99.26%), **acute panmyelosis with myelofibrosis** (98.03%) and **bilineal AML** (97.68%): plausible by extrapolation from the approved AML indication, but no subtype-specific trials or literature exist. Efficacy would depend on IDH1 mutation status rather than disease etiology.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction, bulbar polio. Currently no related clinical trials registered.

For reference, the following trials relate to the best-supported candidate, myelodysplastic/myeloproliferative disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03471260](https://clinicaltrials.gov/study/NCT03471260) | Phase 1/2 | Recruiting | 96 | Ivosidenib with venetoclax ± azacitidine in IDH1-mutated hematologic malignancies; dose and safety being studied |
| [NCT04493164](https://clinicaltrials.gov/study/NCT04493164) | Phase 2 | Recruiting | 30 | CPX-351 plus ivosidenib in IDH1-mutated AML or high-risk MDS; small sample |
| [NCT04250051](https://clinicaltrials.gov/study/NCT04250051) | Phase 1 | Terminated | 2 | Ivosidenib with FLAG chemotherapy in relapsed/refractory IDH1-mutant AML; terminated after only 2 participants, so negligible usable evidence |

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005936 | Tibsovo | Not specified | Tibsovo in combination with azacitidine is indicated for the treatment of adult patients with newly diagnosed acute myeloid leukaemia (AML) with an... |

Note: this authorization has a status of cancelled, and no valid authorizations currently exist.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions (typically haematological parameters, liver and renal function) |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs in total. Those listed in the data compiled for this report include:
  - **Major**: aprepitant, clarithromycin, dolasetron, palonosetron, cisapride, granisetron, levofloxacin
  - **Moderate**: famotidine, loperamide, bisacodyl, picosulfuric acid, polyethylene glycol (3350 with electrolytes), saxagliptin, eliglustat, linagliptin, sodium sulfate, castor oil, glycerin, lactitol, lactulose

  Several of the major interactions involve drugs that prolong the QT interval (e.g. 5-HT3 antagonists, cisapride, levofloxacin), so co-administration warrants caution.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, bulbar polio, has no mechanistic link and no clinical or literature evidence (L5); its high score appears to be a model artifact. In addition, the only EU authorization has been cancelled.
- The myeloid-neoplasm predictions (especially myelodysplastic/myeloproliferative disease) are more credible and could be pursued separately as research questions, restricted to IDH1-mutation-positive patients.

**To proceed, the following is needed:**
- Mechanism of action data (MOA)
- Warnings and contraindications from the SmPC (currently missing; this blocks safety screening)
- For the myeloid candidates: disease-specific trial results or publications, and IDH1 mutation-based patient selection criteria
- Clarification of the reasons and implications of the cancelled EU authorization
- Review of the QT-related and CYP-related drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

