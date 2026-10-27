---
layout: default
title: Bosentan
parent: AI Predictions (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bosentan: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Pulmonary arterial hypertension (WHO functional class III…"
monitor_inn: "Bosentan"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "pseudoxanthoma elasticum, forme fruste", "kyphoscoliotic heart disease", "elastoma", "gout", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita"]
---

# Bosentan
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

## Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Bosentan was originally approved to treat pulmonary arterial hypertension (PAH) and to reduce new digital ulcers in systemic sclerosis.
The TxGNN model predicts it may be useful for **rheumatoid arthritis**, but there are **no registered clinical trials** and the supporting literature is mainly **animal-model studies** and reviews.
The prediction score is very high (99.80%), but it is not matched by human clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (WHO functional class III, with some improvement in class II); reduction of new digital ulcers in systemic sclerosis |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (preclinical and mechanism studies only) |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. The literature identifies bosentan as a dual endothelin receptor antagonist, blocking both ETA and ETB receptors.

Endothelin-1 is raised in the plasma and synovial membrane of rheumatoid arthritis patients. It contributes to inflammation, vasoconstriction and new blood vessel formation. In a mouse model of collagen-induced arthritis, bosentan reduced disease severity and was linked to lower TNF-α and other inflammatory mediators (PMID 22249931). In a zymosan-induced arthritis model, blocking endothelin receptors reduced neutrophil accumulation and swelling (PMID 18515326).

These findings give the prediction a plausible biological basis. However, they come from animal models only. The other retrieved papers mostly concern PAH in connective tissue disease rather than rheumatoid arthritis treatment. No human rheumatoid arthritis trial was found.

**Note on other predictions:** The model also predicted *limited systemic sclerosis* (score 99.65%). That is effectively an already-approved use of bosentan, since it is labeled to reduce new digital ulcers in systemic sclerosis. It is supported by a 2023 systematic review (PMID 36974107). The remaining high-scoring predictions have no trials or literature and look like knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Preclinical (mouse) | Inflamm Res | Bosentan ameliorated collagen-induced arthritis; TNF-α drives induction of endothelin system genes |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Preclinical (mouse) | J Leukoc Biol | Endothelin receptor blockade modulated inflammation in zymosan-induced arthritis (LTB4, TNF-α, CXCL-1) |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Preclinical (indirect) | Proc Natl Acad Sci USA | IL-15-induced joint pain sensitization was inhibited by a dual endothelin receptor antagonist |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Preclinical (indirect) | Pain | IL-17 mediates joint pain in antigen-induced arthritis; indirect link only |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH in connective tissue diseases, including rheumatoid arthritis to a lesser extent |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheum Dis Clin North Am | Connective-tissue-disease-associated PAH: poor prognosis, more treatment options available |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Vasculopathy and PAH in lupus, Sjögren's and vasculitides |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case report | Kardiol Pol | Child with Eisenmenger syndrome on bosentan who later developed juvenile rheumatoid arthritis; coincidental, not a treatment effect |

---

## EU Market Information

| Authorization Number | Product Name | Status | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002644 | Stayveer | Cancelled | Treatment of pulmonary arterial hypertension (PAH) to improve exercise capacity and symptoms in patients with World Health Organizat... |
| EMEA/H/C/000401 | Tracleer | Cancelled | Treatment of pulmonary arterial hypertension (PAH) to improve exercise capacity and symptoms in patients with WHO functional class... |

---

## Safety Considerations

- **Conditions linked to contraindications in the knowledge graph** (derived from drug-disease relationships, not from label text): liver failure, liver disease, drug-induced liver injury, gallbladder disease, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), thrombocytopenia, anemia (including macrocytic anemia), congestive heart failure, pulmonary edema, and pulmonary veno-occlusive disease.
- **Drug Interactions**: 100 interactions were recorded. The 20 reviewed are all rated Moderate, including:
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)
  - antidiabetics (pioglitazone, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, acetohexamide, chlorpropamide)
  - CYP-active drugs (clarithromycin, cimetidine, clotrimazole, metronidazole, aprepitant)
  - others (cisapride, dronabinol, eliglustat, eluxadoline)
- Bosentan is known to carry liver toxicity and embryo-fetal toxicity warnings. Please refer to the SmPC for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The very high model score rests only on animal-model data and indirect reviews. There are no human rheumatoid arthritis trials, and the EU authorizations are currently cancelled. The liver and embryo-fetal toxicity profile and the many drug interactions raise the bar for a chronic inflammatory indication.

**To proceed, the following is needed:**
- Human proof-of-concept evidence in rheumatoid arthritis (for example, a pilot or Phase 2 trial)
- Confirmation of mechanism-of-action data and the SmPC warnings and contraindications
- A benefit-risk assessment against existing rheumatoid arthritis therapies, including liver monitoring and contraception requirements
- Confirmation of current product availability, given the cancelled EU status
- Direct verification of the underlying trials for the systemic sclerosis use, if that on-label indication is pursued separately
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

