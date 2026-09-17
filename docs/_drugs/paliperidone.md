---
layout: default
title: Paliperidone
parent: AI Predictions (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Paliperidone is an atypical antipsychotic drug (per supporting literature in this evidence pack, it is used for schizophrenia and related psychotic disorders). The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**, but this prediction is currently supported by **0 clinical trials** and only general ophthalmology literature with no direct relevance to the drug — the model's rationale itself flags this as likely a knowledge-graph proximity artifact rather than a true pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorization or original-indication data in this evidence pack (drug not marketed in this jurisdiction); literature elsewhere in this pack indicates an existing schizophrenia indication |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for paliperidone in this evidence pack. Based on other information contained in the pack (see the treatment-refractory schizophrenia candidate below), paliperidone is a D2/5-HT2A receptor antagonist belonging to the second-generation (atypical) antipsychotic class, and its efficacy in schizophrenia is well established.

For the top-ranked prediction — retinal dystrophy with or without extraocular anomalies — there is **no identified biological or pharmacological link** to paliperidone's known mechanism. The model's own rationale states that this high score likely reflects proximity within the knowledge graph rather than a genuine pharmacological relationship. The attached literature (orbital infection, diplopia, congenital ptosis, lens anomalies, etc.) covers general ophthalmology topics and does not discuss paliperidone or antipsychotic pharmacology at all.

Given the absence of mechanistic rationale, clinical trials, or targeted literature, this prediction should be treated as a pure model output requiring substantial further validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | General review of orbital infections; no mention of paliperidone or retinal dystrophy |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Diagnostic approach to diplopia; general neuro-ophthalmology, not drug-specific |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Overview of congenital ptosis and extraocular muscle fibrosis |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape; anterior segment dysgenesis |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Case series of unilateral cryptophthalmia with orbital malformation |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuroophthalmol | Isolated case of congenital trochlear-oculomotor synkinesis |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome: vitreoretinal degeneration and extraocular features |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging review of pediatric ocular pathologies including congenital lesions |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optom Vis Sci | Case of congenital extraocular muscle fibrosis with variable divergence |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Ther Adv Ophthalmol | Review of ocular involvement in inherited metabolic disorders |

**Note:** None of the above literature discusses paliperidone, antipsychotic pharmacology, or retinal dystrophy treatment directly — all are general ophthalmology/neuro-ophthalmology background references.

---

## EU Market Information

No marketing authorizations found. This drug is not currently marketed in the covered jurisdiction, so no product/dosage-form/indication data is available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are flagged as a Blocking data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (retinal dystrophy with or without extraocular anomalies) has no clinical trials, no directly relevant literature, and no plausible mechanistic link — it is an L5, model-only signal (S0 stage) that the model's own rationale flags as likely a knowledge-graph artifact rather than a real pharmacological relationship.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a **Blocking** gap that prevents any S1 safety assessment
- Confirmed mechanism of action via DrugBank (currently unavailable)
- Independent mechanistic or preclinical rationale connecting paliperidone to retinal/ophthalmic pathology before any further evaluation
- **Portfolio note:** a lower-ranked candidate in this same pack — *treatment-refractory schizophrenia* (score 99.80%, L2 evidence, "Proceed with Guardrails") — has a direct pharmacological rationale (D2/5-HT2A antagonism), a completed Phase 4 observational study, and ongoing Phase 4 trials. This is a substantially stronger candidate and may warrant prioritization over the top TxGNN-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

