---
layout: default
title: Belatacept
parent: AI Predictions (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Belatacept: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Prophylaxis of graft rejection in adult recipients of a renal transpl…"
monitor_inn: "Belatacept"
predicted_indications: ["plasma cell myeloma", "indolent plasma cell myeloma", "relapsing-remitting multiple sclerosis", "Crohn's colitis", "heart disease", "Laubry-Pezzi syndrome", "hyperthyroidism", "genetic syndromic Pierre Robin syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "colonic neoplasm"]
---

# Belatacept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Belatacept: From Kidney Transplant Rejection Prophylaxis to Plasma Cell Myeloma

## One-Sentence Summary

Belatacept is a CTLA-4-Ig fusion protein originally used to prevent graft rejection in adult kidney transplant recipients.
The TxGNN model predicts it may be effective for **plasma cell myeloma**, but **no clinical trials** and **no publications** currently support this specific direction.
The prediction is a computational signal only, and the immunosuppressive nature of the drug raises a safety concern in a plasma cell malignancy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of graft rejection in adult recipients of a renal transplant (in combination with corticosteroids and a mycophenolic acid) |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 97.03% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, belatacept is a CTLA-4-Ig fusion protein that blocks CD28-CD80/CD86 costimulation of T cells. This is how it prevents graft rejection in kidney transplantation.

A theoretical link to myeloma would be modulation of the T-cell and antigen-presenting-cell microenvironment. However, no supporting data were provided, and the high TxGNN score is a computational prediction only. Immunosuppression could also plausibly raise risk, including post-transplant lymphoproliferative disorder (PTLD), which is a labelled concern for this drug class.

The same reasoning applies to the closely related prediction, indolent plasma cell myeloma (score 96.94%). It likely comes from the same graph neighbourhood and is equally speculative.

### Other Predictions Reviewed

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Indolent plasma cell myeloma | 96.94% | L5 | Same rationale as myeloma; no data |
| Relapsing-remitting multiple sclerosis | 96.82% | L5 | Costimulation blockade is biologically plausible, but no data were provided |
| Crohn's colitis | 96.18% | L4 | The only evidence is a case report of colitis *caused* by belatacept, which points to potential harm rather than benefit |
| Heart disease | 94.62% | L3 | Literature reflects use in heart transplant recipients and avoidance of calcineurin-inhibitor toxicity, not treatment of heart disease itself |
| Hyperthyroidism | 93.81% | L5 | Plausible autoimmune rationale, but no data |
| Colonic neoplasm | 93.63% | L5 | No evidence; immunosuppression may impair tumour surveillance |
| Laubry-Pezzi syndrome and Pierre Robin entries | 93.6–94.1% | L5 | No plausible mechanistic link; likely graph artefacts |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for plasma cell myeloma.

---

## Literature Evidence

Currently no related literature available for plasma cell myeloma.

For context, the highest-ranked prediction with literature is Crohn's colitis. It has one case report:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29358873](https://pubmed.ncbi.nlm.nih.gov/29358873/) | 2017 | Case report | World J Gastroenterol | Severe stricturing Crohn's disease-like colitis in a kidney transplant patient treated with belatacept, suggesting a possible adverse event |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002098 (cancelled) | Nulojix | Not specified | Nulojix, in combination with corticosteroids and a mycophenolic acid (MPA), is indicated for prophylaxis of graft rejection in adult recipients of a renal transplant. |

---

## Safety Considerations

- **Drug Interactions**: 72 interactions were identified. Major-level examples include:
  - Deferiprone
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Bacillus Calmette-Guérin (live) vaccine

  Moderate-level examples include roflumilast, alemtuzumab, anakinra, azathioprine, canakinumab and several vaccines. The zinc salts are minor.
- **Malignancy and immune risk**: Immunosuppression carries a labelled risk of malignancy, including PTLD. This is particularly relevant when considering a plasma cell malignancy.
- **Colitis signal**: A case report links belatacept to a severe Crohn's-like colitis.

Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The plasma cell myeloma prediction rests only on a model score, with no clinical trials or publications. The mechanism (T-cell immunosuppression) gives a plausible safety concern rather than a clear therapeutic rationale. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic analysis specific to myeloma
- Preclinical evidence of anti-myeloma activity
- SmPC warnings and contraindications, with a risk assessment for malignancy and PTLD
- A review of why the EU authorization was cancelled, and of the available routes and dosage forms
- If a repurposing direction is pursued, prioritize those with some literature support (such as transplant-related cardiac use) over the myeloma prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

