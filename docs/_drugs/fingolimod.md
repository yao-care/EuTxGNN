---
layout: default
title: Fingolimod
parent: AI Predictions (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fingolimod: predicted new indication Borderline ovarian serous tumor (evidence level L5). Approved use: Highly active relapsing remitting multiple sclerosis (adults and paed…"
---

# Fingolimod
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

# Fingolimod: From Relapsing Remitting Multiple Sclerosis to Borderline Ovarian Serous Tumor

## One-Sentence Summary

Fingolimod was originally approved for highly active relapsing remitting multiple sclerosis.
The TxGNN model predicts it may be effective for **borderline ovarian serous tumor**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly supporting this specific indication.
The only related signals are preclinical studies in ovarian cancer models, listed under other ovarian-related predictions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Highly active relapsing remitting multiple sclerosis (adults and paediatric patients aged 10 years and older) |
| Predicted New Indication | Borderline ovarian serous tumor |
| TxGNN Prediction Score | 94.94% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fingolimod (FTY720) is generally known as a sphingosine-1-phosphate (S1P) receptor modulator. It traps lymphocytes in lymphoid tissue, which is how it controls relapsing multiple sclerosis.

S1P signaling has been implicated in the biology of ovarian epithelial tumors, which is a plausible but hypothetical link to this prediction. The high TxGNN score (0.949) is a graph-based result, and no trial or publication directly supports it. The score may reflect similarity to other ovarian neoplasm nodes in the knowledge graph rather than independent evidence.

The nearest supporting signal is preclinical. A 2018 patient-derived xenograft study reported that FTY720 enhanced the activity of carboplatin and tamoxifen in ovarian cancer models. This is indirect, is not in borderline serous tumors, and has no human data behind it.

## Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Ovarian papillary cystadenoma | 94.62% | L5 | Benign tumor; weak risk-benefit case |
| 3 | Malignant ovarian Brenner tumor | 94.59% | L5 | Rare tumor; no tumor-specific rationale |
| 4 | Rete ovarii cystadenoma | 94.57% | L5 | Prediction only |
| 5 | Serous neoplasm | 94.32% | L4 | One preclinical study (PMID 30120964) |
| 6 | Ovarian mucinous cystadenofibroma | 94.27% | L5 | Benign; prediction only |
| 7 | Mucinous ovarian cystadenoma | 94.25% | L5 | Benign; histology differs from the serous preclinical signal |
| 8 | Ovarian benign neoplasm | 94.22% | L4 | Two preclinical studies, neither in benign neoplasm |
| 9 | Ovarian surface papilloma | 94.05% | L5 | Prediction only |
| 10 | Immunoerythromyeloid hypoplasia | 93.62% | L5 | Lymphopenia effect is mechanistically concerning |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for borderline ovarian serous tumor. The related preclinical publications found for other ovarian-related predictions are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30120964](https://pubmed.ncbi.nlm.nih.gov/30120964/) | 2018 | Preclinical (patient-derived xenograft) | Cancer Letters | FTY720 enhanced the anti-tumor activity of carboplatin and tamoxifen and sensitized drug-resistant ovarian cancer cells |
| [30388910](https://pubmed.ncbi.nlm.nih.gov/30388910/) | 2019 | Preclinical (NSCLC models) | Cancer Biology & Therapy | Fingolimod synergized with pemetrexed to kill NSCLC and ovarian cancer cells and overcame resistance to ERBB inhibition |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005661 (cancelled) | Fingolimod Mylan | Not specified | Single disease modifying therapy in highly active relapsing remitting multiple sclerosis for adults and paediatric patients aged 10 years and older... |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not label text): liver failure, kidney disease, pyoureter, diabetes mellitus, diabetic ketoacidosis, lung disease, leukopenia, uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, atrioventricular block, sick sinus syndrome, familial sick sinus syndrome.
- **Drug Interactions**: 100 interactions were found. The first 20 returned include these.
  - **Major**: corticosteroids (hydrocortisone, triamcinolone including ophthalmic, dexamethasone, betamethasone, budesonide, prednisone), clarithromycin, levofloxacin, ondansetron, dolasetron, palonosetron, cisapride.
  - **Moderate**: famotidine, ranitidine, cimetidine, nizatidine, loperamide, naltrexone.
  - **Minor**: metronidazole.

Please refer to the SmPC for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone, with no clinical trials and no publications in borderline serous tumors. Preclinical chemosensitization data in ovarian cancer are indirect. Borderline and benign tumors also offer a weak risk-benefit case for a systemic immunomodulator with cardiac, infectious and macular edema risks. The only EU authorization is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a documented link between S1P signaling and borderline serous tumor biology
- Direct preclinical evidence in borderline serous tumor models
- Official SmPC warnings and contraindications for the safety review
- A clear risk-benefit rationale, since the predicted indication is a low-grade or benign condition
- Clarification of route and formulation compatibility
- Consideration of whether a malignant serous ovarian indication, where preclinical data exist, is a more suitable research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

