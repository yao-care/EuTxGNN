---
layout: default
title: Eptifibatide
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# Eptifibatide: From Acute Coronary Syndrome to Hemoglobinopathy (Sickle Cell Disease)

## One-Sentence Summary

> Eptifibatide is a GPIIb/IIIa (αIIbβ3 integrin) antagonist historically used to inhibit platelet aggregation in acute coronary syndromes.
> Among the 10 TxGNN-predicted indications for this drug, **Hemoglobinopathy** (sickle cell disease vaso-occlusive crisis) is the only candidate with real human trial data —
> **1 completed-phase clinical trial (terminated)** and **4 supporting publications** — even though it ranks 7th, not 1st, by raw TxGNN score.
> The top-ranked prediction (rheumatoid arthritis, score 99.99%) has zero supporting evidence and is therefore not the focus of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (ACS) / Unstable Angina — inferred from cited literature context; no formal regulatory label text is available since this product is not marketed in this jurisdiction |
| Predicted New Indication | Hemoglobinopathy (sickle cell disease, acute vaso-occlusive pain crisis) |
| TxGNN Prediction Score | 99.98% (rank #441 overall) |
| Evidence Level | L3 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eptifibatide is a cyclic heptapeptide GPIIb/IIIa (integrin αIIbβ3) receptor antagonist that blocks the final common pathway of platelet aggregation. This mechanism underlies its established antithrombotic use in acute coronary syndromes, where blocking fibrinogen cross-linking between platelets prevents thrombus propagation in the coronary vasculature (as referenced in the cited literature).

Sickle cell disease and related hemoglobinopathies share a pathophysiology in which platelet activation and adhesion contribute to microvascular occlusion, driving the acute painful crises that define the disease. Because Eptifibatide's core action — blocking platelet aggregation via αIIbβ3 — is mechanistically agnostic to the vascular bed involved, a link between Eptifibatide and hemoglobinopathy is biologically plausible. This is also the *only* candidate among this drug's top 10 TxGNN predictions that has already been tested directly in humans: a Phase I/II trial (NCT00834899) plus three independent publications from the same U.S. research group examining safety, pain-crisis outcomes, and inflammatory markers.

By comparison, the other high-scoring TxGNN candidates (rheumatoid arthritis, several sickle-cell subtype syndromes without independent data, beta-thalassemia, and the 16p13 deletion syndrome) rest mainly on ontological proximity within the knowledge graph rather than independent evidence, and should be treated as far more speculative. A separate, low-tier signal also exists for female breast carcinoma, based only on in vitro/microfluidic-chip data showing αIIbβ3 blockade may reduce platelet-tumor cell interactions relevant to metastasis — this is preclinical only and not pursued further here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1/2 | Terminated | 13 | Evaluated safety and efficacy of Eptifibatide for acute pain episodes in sickle cell disease, testing the hypothesis that platelet activation and resultant inflammation contribute to vaso-occlusive crises. Terminated early (2012); reason not stated in available data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase 1 Clinical Trial | British Journal of Haematology | First-in-SCA-patient study; Eptifibatide safely inhibited platelet aggregation and CD40 ligand release in 4 steady-state sickle cell anaemia patients, supporting the ACS-like platelet/CD40L pathophysiology rationale. |
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot Clinical Study | Thrombosis Research | Pilot study of Eptifibatide during acute painful episodes in SCD; evaluated safety and efficacy of αIIbβ3 blockade in reducing crisis-related platelet activation. |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Clinical Study (Post-hoc/Mechanistic) | American Journal of Hematology | Follow-up analysis from the same trial cohort examining Eptifibatide's effect on inflammatory markers during acute pain episodes. |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In Vitro Preclinical | The Journal of Clinical Investigation | Microfluidic "endothelialized" model of microvascular occlusion/thrombosis in hematologic diseases (SCD, HUS); supports the general biophysical mechanism but does not test Eptifibatide directly. |

---

## Safety Considerations

Please refer to the SmPC for safety information. No drug-drug interaction records, key warnings, or contraindication data were found for this drug in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is sound and this is the only one of Eptifibatide's 10 TxGNN-predicted indications with direct human trial data, but the pivotal trial (NCT00834899, n=13) was terminated for an undocumented reason and no properly powered efficacy trial exists. This is insufficient to move beyond a research hypothesis at this time.

**To proceed, the following is needed:**
- Reason for termination of NCT00834899 (safety, futility, or enrollment failure changes the risk calculus materially)
- Official mechanism-of-action and labeling/safety data (SmPC/TFDA-equivalent warnings and contraindications — currently a blocking data gap)
- A properly powered Phase 2 trial with vaso-occlusive crisis frequency/duration as a primary endpoint
- Bleeding-risk assessment specific to the SCD population, given baseline coagulopathy differences from the ACS population where Eptifibatide is conventionally used
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

