---
layout: default
title: Voretigene Neparvovec
parent: AI Predictions (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
---

# Voretigene Neparvovec
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

# Voretigene neparvovec: From Inherited Retinal Dystrophy to Myxomatous Mitral Valve Prolapse

## One-Sentence Summary

> Voretigene neparvovec is an AAV2-delivered gene therapy used for RPE65 mutation-associated inherited retinal dystrophy, administered by subretinal injection to restore the visual cycle in retinal pigment epithelial cells.
> The TxGNN model's top-ranked candidate suggests a possible link to **Myxomatous Mitral Valve Prolapse**, but with a low prediction score (**56.4%**), a rank of over 374,000, and **zero clinical trials or publications** supporting this direction.
> The evidence pack's own mechanistic assessment identifies this as likely knowledge-graph topological noise rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | RPE65 mutation-associated inherited retinal dystrophy (inferred from mechanism-of-action description in the evidence pack; no formal EU-approved indication text is available in this dataset) |
| Predicted New Indication | Myxomatous Mitral Valve Prolapse |
| TxGNN Prediction Score | 56.42% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Voretigene neparvovec is an AAV2 (adeno-associated virus serotype 2) vector-based gene therapy that is administered exclusively by subretinal injection. It works locally within retinal pigment epithelial cells to deliver a functional copy of the *RPE65* gene, correcting the visual-cycle defect caused by biallelic *RPE65* mutations. This is a highly localized, single-organ therapy with no evidence of systemic biodistribution.

Myxomatous mitral valve prolapse is a degenerative connective-tissue disorder of the cardiac valve apparatus, driven by distinct biological pathways (extracellular matrix remodeling, valvular interstitial cell dysfunction) that are unrelated to the retinal visual cycle or *RPE65* biology. There is no known shared gene, pathway, or tissue target between the original indication and this predicted one.

The evidence pack's own repurposing rationale explicitly flags this: given the low TxGNN score (0.56, near the bottom of the model's ranking distribution at position 374,391 out of the full candidate space) and the complete absence of corroborating clinical or literature evidence, the prediction is most plausibly explained as knowledge-graph topological noise rather than a genuine mechanistic association. All nine other top-10 candidates for this drug (pituitary dwarfism, cystic hygroma, conductive hearing loss, median nerve mononeuropathy susceptibility, Wiskott-Aldrich syndrome 2, esophageal malformation, hypermobility syndrome, woolly hair, and an obsolete hypertension term) show the same pattern: low scores, no supporting evidence, and no mechanistic overlap with a gene therapy restricted to subretinal, single-organ delivery.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorization records are available for this drug in the current dataset (market status: Not marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a low TxGNN score (56.4%) and an extremely low rank (~374,000), no supporting clinical trials or literature, and no plausible mechanistic link between a localized subretinal *RPE65* gene therapy and a degenerative cardiac valve disorder. The evidence pack itself assesses this as likely model noise rather than a true signal, and the same pattern holds across all ten top-ranked candidates for this drug.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (currently a blocking data gap; required before any safety pre-assessment, S1, can begin)
- Confirmed mechanism-of-action and formal indication text from DrugBank or an official regulatory source (currently a data gap; the MOA used in this report was inferred from narrative rationale text, not a verified structured field)
- Any future TxGNN re-run with updated evidence should re-check whether higher-scoring, mechanistically plausible candidates emerge before further investment in this drug's repurposing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

