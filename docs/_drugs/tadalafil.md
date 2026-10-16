---
layout: default
title: Tadalafil
parent: AI Predictions (L5)
nav_order: 582
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Erectile dysfunction (sexual stimulation is required for efficacy"
---

# Tadalafil
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

# Tadalafil: From Erectile Dysfunction to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used to treat erectile dysfunction, benign prostatic hyperplasia, and pulmonary arterial hypertension.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a knowledge-graph prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction (sexual stimulation is required for efficacy; not indicated for use by women) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 5 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, tadalafil is a PDE5 inhibitor that raises cGMP and causes vasodilation. Its efficacy in erectile dysfunction, benign prostatic hyperplasia, and pulmonary arterial hypertension is established.

The link to the predicted indication is weak. Ambras syndrome is a rare congenital disorder tied to chromosome 8q22 rearrangements affecting TRPS1 regulation. No plausible route is known by which PDE5 inhibition would treat it.

Hypertrichosis has also been reported with other vasodilators (e.g., minoxidil). The prediction may therefore reflect an adverse-effect-like association rather than a therapeutic one. The same concern applies to the other top-ranked predictions (hypertrichosis, hair shaft abnormalities, trichomegaly), which are likely driven by graph proximity between hair-related phenotypes. Whether TxGNN is predicting treatment or inducing the phenotype needs to be clarified before any further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For context, the lower-ranked predictions of migraine disorder and migraine with brainstem aura have only sparse literature, and it points in the wrong direction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache. This is an adverse event signal, not a treatment effect. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000436 | Cialis | Not specified | Treatment of erectile dysfunction. In order for tadalafil to be effective, sexual stimulation is required. Cialis is not i... |
| EMEA/H/C/004666 | Tadalafil Lilly | Not specified | Treatment of erectile dysfunction in adult males. In order for tadalafil to be effective, sexual stimulation is required. ... |
| EMEA/H/C/001021 | Adcirca (previously Tadalafil Lilly) | Not specified | Adults: pulmonary arterial hypertension (PAH), WHO functional class II and III, to improve exercise capacity. Paediatric p... |
| EMEA/H/C/003787 | Tadalafil Mylan | Not specified | Treatment of erectile dysfunction in adult males. In order for tadalafil to be effective, sexual stimulation is required. ... |
| EMEA/H/C/004297 | Talmanco (previously Tadalafil Generics) | Not specified | Talmanco is indicated in adults for the treatment of pulmonary arterial hypertension (PAH) classified as WHO functional cl... |

All five authorizations are listed as cancelled.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (derived from drug-disease edges, not label text): liver failure, epilepsy, aortic stenosis and other aortic valve disease, hypotensive disorder, blood coagulation disease, acute coronary syndrome, myocardial infarction, stroke and cerebrovascular disorders, sickle cell anemia and other hemoglobinopathies, plasma cell myeloma, leukemia, priapism, Peyronie disease, hearing loss disorder, and hypertrophic cardiomyopathy.
- **Drug Interactions**: 100 interactions were identified in total. The most notable moderate-level ones include aprepitant, dexamethasone, clarithromycin, cimetidine, miconazole, clotrimazole, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Papaverine is a minor interaction. Several others (e.g., metformin, omeprazole, morphine) have an unknown severity level.
- A literature report also notes that PDE5 inhibition and nitric oxide/cGMP signaling can trigger migraine.

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials or literature, and the evidence level is L5. The plausible mechanism points toward promoting hair growth rather than treating hypertrichosis, and no route is known by which PDE5 inhibition would address Ambras syndrome. No authorizations are currently valid in the EU.

**To proceed, the following is needed:**
- Clarification of the direction of the TxGNN prediction (treatment vs. inducing the phenotype)
- Mechanism of action data and a documented mechanistic link to the predicted indication
- Warnings and contraindications from the SmPC to enable safety screening
- Any preclinical or clinical evidence in the predicted indication
- If a more plausible candidate is wanted, evaluation of kyphoscoliotic heart disease (rank 7), which is linked to secondary pulmonary hypertension and is the most biologically plausible of the novel predictions, although still an unvalidated hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

