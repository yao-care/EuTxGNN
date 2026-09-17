---
layout: default
title: Luspatercept
parent: AI Predictions (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Luspatercept
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

# Luspatercept: From Anemia in β-Thalassemia/MDS to Pyruvate Kinase Deficiency of Red Cells

## One-Sentence Summary

> Luspatercept is a biologic used internationally to treat anemia associated with transfusion-dependent β-thalassemia and myelodysplastic syndromes (MDS), both driven by ineffective erythropoiesis.
> The TxGNN model predicts it may also be relevant for **Pyruvate Kinase Deficiency of Red Cells**, a hereditary hemolytic anemia with a similar underlying pathophysiology.
> However, this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational hypothesis (L5) that has not yet been tested.

**Note on candidate selection:** This Evidence Pack contains 10 TxGNN-predicted indications for luspatercept. The single highest-scoring prediction (*monosomy X*, score 95.99%) is explicitly flagged in the evidence pack's own rationale as likely knowledge-graph noise with no plausible mechanistic link. Among the 10 candidates, only three (Pyruvate Kinase Deficiency, Thalassemia beta+ silent allele, Hb Bart's hydrops fetalis) reach decision stage S1 ("Research Question") rather than S0 ("Hold"). This report focuses on **Pyruvate Kinase Deficiency of Red Cells** as the most biologically coherent and clinically meaningful candidate; the full candidate landscape is summarized near the end of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan regulatory data (drug not marketed in Taiwan). Per evidence-pack rationale text, internationally approved for anemia in transfusion-dependent β-thalassemia and MDS |
| Predicted New Indication | Pyruvate Kinase Deficiency of Red Cells |
| TxGNN Prediction Score | 93.84% (rank 43,686 of all drug-disease pairs) |
| Evidence Level | L5 — model prediction only, no clinical trials or literature |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (flagged internally as "Research Question") |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is flagged as a data gap (DG002) in this evidence pack. However, the pack's own rationale text describes luspatercept as an **ActRIIB-Fc fusion protein ("ligand trap")** that binds TGF-β superfamily ligands (GDF11, activin B) and inhibits downstream Smad2/3 signaling, thereby promoting **late-stage erythroid maturation**. This mechanism is distinct from erythropoietin-stimulating agents, acting instead on the terminal differentiation step of red blood cell production.

Luspatercept's established indications — β-thalassemia and MDS — share a common pathophysiological feature: **ineffective erythropoiesis**, where red blood cell precursors fail to mature properly, leading to chronic anemia despite adequate or excessive erythroid precursor numbers. Pyruvate kinase (PK) deficiency of red cells is a hereditary enzymopathy causing chronic hemolytic anemia with a **compensatory but ineffective erythropoiesis** response — mechanistically analogous to the underlying biology luspatercept already addresses in its approved indications.

Because luspatercept acts downstream, at the late erythroid maturation stage rather than on a disease-specific upstream defect, there is a plausible (though untested) rationale that it could partially normalize red cell output in PK deficiency as well. This is explicitly framed in the evidence pack as a *hypothesis extrapolated from mechanistic analogy*, not as evidence of proven efficacy — safety data on the use of luspatercept in a distinct hemolytic anemia population are entirely unavailable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Luspatercept currently holds **no marketing authorizations in Taiwan** (market status: Not marketed, total licenses: 0). No product, dosage form, or approved indication text is available from the local regulatory dataset for this evidence pack.

---

## Safety Considerations

Please refer to the SmPC for safety information.

**Critical data gap:** TFDA label warnings and contraindications (DG001) are marked as a **Blocking** data gap in this evidence pack — this must be resolved before any safety-stage (S1) evaluation can proceed. No drug-drug interaction data was found (`query_status: not_found`).

---

## Other Predicted Indications in This Evidence Pack

For transparency, the full set of 10 TxGNN-predicted indications for luspatercept is summarized below, ranked by TxGNN score. Only three reach decision stage S1 ("Research Question"); the rest are held at S0 due to weak or absent mechanistic plausibility per the evidence pack's own rationale.

| Rank | Disease | TxGNN Score | Decision Stage | Recommendation | Mechanistic Plausibility |
|------|---------|-----------|-----------------|-----------------|---------------------------|
| 1 | Monosomy X (Turner syndrome) | 95.99% | S0 | Hold | Likely KG noise — no direct link |
| 2 | Hepatic infarction | 95.70% | S0 | Hold | No plausible pathway |
| 3 | Hepatic veno-occlusive disease | 94.91% | S0 | Hold | Speculative TGF-β/fibrosis link, unvalidated |
| 4 | Peliosis hepatis | 94.75% | S0 | Hold | No direct mechanistic link |
| 5 | Combined immunodeficiency syndrome | 94.28% | S0 | Hold | No plausible pathway |
| **6** | **Pyruvate kinase deficiency of red cells** | **93.84%** | **S1** | **Research Question** | Shared ineffective erythropoiesis biology |
| 7 | Thalassemia, beta+, silent allele | 93.32% | S1 | Research Question | Mechanistically overlaps with approved β-thalassemia indication |
| 8 | Familial apolipoprotein C-II deficiency | 93.05% | S0 | Hold | No known pathway overlap |
| 9 | Adenosine deaminase deficiency | 92.86% | S0 | Hold | No plausible pathway |
| 10 | Hb Bart's hydrops fetalis | 92.75% | S1 | Research Question | Same thalassemia-family biology; fetal safety unknown |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by mechanistic analogy (L5, model prediction only) with zero clinical trials and zero publications. Additionally, luspatercept is not currently marketed in Taiwan, and a **Blocking** safety data gap (TFDA warnings/contraindications) prevents any progression to a formal safety-stage evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/international label warnings and contraindications
- Resolve DG002 (High): confirm formal MOA documentation via DrugBank API
- Identify or commission preclinical/proof-of-concept data specific to PK deficiency of red cells
- Monitor ClinicalTrials.gov and PubMed for emerging evidence, as this candidate is currently a pure research question with no active studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

