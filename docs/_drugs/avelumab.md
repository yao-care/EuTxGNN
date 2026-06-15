---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Urothelial Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab (Bavencio) is a fully human anti-PD-L1 IgG1 monoclonal antibody internationally approved for Merkel cell carcinoma and platinum-treated urothelial carcinoma (UC) maintenance therapy, but currently not registered in Taiwan.
The TxGNN model's top-ranked prediction identifies **Human Herpesvirus 8 (HHV-8)-Related Tumor** as the primary repurposing candidate, with the biological rationale anchored in virally-encoded LANA-mediated PD-L1 upregulation — a specific immune evasion circuit directly targeted by checkpoint blockade — supported by class-effect evidence from pembrolizumab in Kaposi's sarcoma.
This is an **L4 mechanistic hypothesis** with **0 direct clinical trials** and **0 publications** for this specific indication; however, across this 10-indication panel, rank 9 (**prostatic urethra urothelial carcinoma**) carries the strongest actionable evidence at **L2 — Proceed with Guardrails**, backed by the JAVELIN Bladder 100 Phase 3 RCT (n=700, OS HR=0.69).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; internationally approved for Merkel cell carcinoma and urothelial carcinoma maintenance |
| Predicted New Indication (Rank 1) | Human Herpesvirus 8-Related Tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision (Rank 1) | Research Question |

---

## Why is This Prediction Reasonable?

Avelumab binds PD-L1 with high affinity, blocking its interaction with both PD-1 and B7-H1 on cytotoxic T lymphocytes, thereby lifting tumor-imposed immune suppression and restoring antitumor surveillance. Unlike some IgG4-subclass checkpoint inhibitors, avelumab's IgG1 backbone additionally mediates antibody-dependent cellular cytotoxicity (ADCC), providing a second, direct tumor-killing mechanism. This dual-action profile is clinically validated in JAVELIN Merkel 200 (Merkel cell carcinoma) and JAVELIN Bladder 100 (locally advanced/metastatic UC, OS HR=0.69, n=700, Phase 3), establishing the mechanistic foundation for extrapolation.

For HHV-8 (KSHV)-related tumors — encompassing Kaposi's sarcoma and primary effusion lymphoma — the link to PD-L1 blockade is biologically specific rather than generic. The viral latency-associated nuclear antigen (LANA) directly transcriptionally upregulates PD-L1 on infected tumor cells, creating a virally-encoded immune evasion circuit. This means HHV-8-driven tumors carry a defined, testable molecular trigger for checkpoint inhibition, not merely incidental PD-L1 expression.

Class-effect evidence lends indirect support: pembrolizumab (anti-PD-1) has demonstrated activity in Kaposi's sarcoma in published case reports and exploratory pilot studies, establishing proof-of-concept that the PD-L1/PD-1 axis is functionally active and therapeutically exploitable in this tumor context. No avelumab-specific studies exist for HHV-8 tumors at present, placing this at L4; however, the mechanistic specificity distinguishes this from the purely graph-structural predictions in ranks 2–8 and justifies a prospective Research Question designation rather than a blanket Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Human Herpesvirus 8-Related Tumor.

---

## Literature Evidence

Currently no related literature available for Human Herpesvirus 8-Related Tumor.

---

## All Predicted Indications Overview

This Evidence Pack covers 10 predicted indications. The table below summarizes the full panel ranked by TxGNN score:

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|---------------|---------|
| 1 | Human Herpesvirus 8-Related Tumor | 99.97% | L4 | Research Question |
| 2 | Middle Ear Neuroendocrine Tumor | 99.97% | L5 | Hold |
| 3 | Malignant Cutaneous Granular Cell Skin Tumor | 99.97% | L5 | Hold |
| 4 | Ectomesenchymoma | 99.97% | L5 | Hold |
| 5 | Adenosine Deaminase Deficiency | 99.95% | L5 | Hold |
| 6 | Reticular Dysgenesis | 99.94% | L5 | Hold |
| 7 | Immunoerythromyeloid Hypoplasia | 99.94% | L5 | Hold |
| 8 | Non-Severe Combined Immunodeficiency | 99.92% | L5 | Hold |
| **9** | **Prostatic Urethra Urothelial Carcinoma** | **99.92%** | **L2** | **Proceed with Guardrails** |
| 10 | Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma | 99.91% | L4 | Research Question |

> **Actionability Note:** Despite ranking 9th by TxGNN score, **prostatic urethra urothelial carcinoma** carries the highest actionable evidence (L2) in this panel, supported by direct class-effect from the JAVELIN Bladder 100 Phase 3 RCT. Ranks 5–8 (immune deficiency conditions) are rated Hold due to a fundamental mechanistic incompatibility: checkpoint inhibition requires functional effector T cells, which are absent or severely depleted in these conditions — the predictions are assessed as knowledge graph false positives, not genuine biological candidates.

### Supporting Trial for Rank 10: Kidney Pelvis Sarcomatoid TCC

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05431777](https://clinicaltrials.gov/study/NCT05431777) | N/A | Completed | 79 | Retrospective multicenter observational study evaluating real-world treatment patterns, safety, and outcomes of avelumab first-line maintenance in Japanese patients with locally advanced/metastatic urothelial carcinoma; provides baseline treatment pattern data relevant to this rare upper-tract sarcomatoid subtype |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — anti-PD-L1 checkpoint inhibitor (fully human IgG1 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low via direct cytotoxic mechanism; monitor for immune-related hematological events (immune thrombocytopenia, autoimmune hemolytic anemia) which are uncommon but reported |
| Emetogenicity Classification | Minimal — not associated with chemotherapy-induced nausea/vomiting |
| Monitoring Items | Thyroid function (TSH, free T4), liver enzymes (ALT/AST/bilirubin), CBC with differential, renal function (creatinine), blood glucose; infusion reaction assessment during each administration (pre-medication with antihistamine and acetaminophen per protocol) |
| Handling Protection | Standard biologic aseptic handling protocol; not classified as a hazardous cytotoxic drug under NIOSH or equivalent guidelines — conventional cytotoxic PPE not required; standard infusion safety and spill procedures apply |

---

## Safety Considerations

Detailed Taiwan TFDA prescribing information is unavailable (drug not registered in Taiwan). Please refer to the EMA SmPC for Bavencio (avelumab) for complete safety information, with particular attention to immune-related adverse events (irAEs) including pneumonitis, immune-mediated hepatitis, colitis, endocrinopathies (hypothyroidism, adrenal insufficiency, type 1 diabetes), and nephritis.

---

## Conclusion and Next Steps

---

### Priority 1 — Prostatic Urethra Urothelial Carcinoma (Rank 9)

**Decision: Proceed with Guardrails**

**Rationale:**
Prostatic urethra urothelial carcinoma is an anatomical subtype sharing the same histology, molecular drivers, and PD-L1 expression profile as bladder UC. The JAVELIN Bladder 100 Phase 3 RCT directly supports class-effect extrapolation; the absence of subtype-specific trial data reflects a search term limitation, not a lack of clinical relevance.

**To proceed, the following is needed:**
- Assess Taiwan import/compassionate use pathway given zero local registrations
- Confirm PD-L1 and TMB biomarker testing protocol for patient selection
- Review JAVELIN Bladder 100 subgroup analyses for upper tract and urethral UC patients
- Establish irAE monitoring and management plan for this patient population

---

### Priority 2 — Human Herpesvirus 8-Related Tumor (Rank 1)

**Decision: Research Question**

**Rationale:**
Virally-encoded PD-L1 upregulation via LANA provides a specific and testable biological mechanism, and pembrolizumab class-effect data in Kaposi's sarcoma establish proof-of-concept for PD-L1/PD-1 axis targeting in HHV-8 malignancies. This signal warrants structured investigation, not dismissal.

**To proceed, the following is needed:**
- Systematic review of PD-1/PD-L1 inhibitors in Kaposi's sarcoma and primary effusion lymphoma to quantify class-effect benchmark
- PD-L1 IHC and TIL characterization on HHV-8-positive tumor tissue samples
- Evaluate feasibility of a basket trial or expanded access protocol including HHV-8 tumor subtypes

---

### Priority 3 — Kidney Pelvis Sarcomatoid TCC (Rank 10)

**Decision: Research Question**

**Rationale:**
Sarcomatoid differentiation in UC is associated with high PD-L1 expression (reported 60–80%) and high TMB, defining a biologically enriched population for checkpoint inhibition. Class-effect from JAVELIN Bladder 100 applies with the same logic as prostatic urethra UC. The observational trial (NCT05431777) demonstrates clinical community awareness of this subtype.

**To proceed, the following is needed:**
- PD-L1 and TMB biomarker profiling specifically in sarcomatoid UC subtype
- Retrospective efficacy signal analysis from NCT05431777 dataset
- Consider sarcomatoid histology as a stratification factor in existing UC checkpoint inhibitor trial protocols

---

### Indications Recommended for Hold (Ranks 2–8)

- **Ranks 2–4** (middle ear neuroendocrine tumor, malignant cutaneous granular cell tumor, ectomesenchymoma): Extremely rare entities with no PD-L1 expression data, no immunotherapy precedent, and in the case of ectomesenchymoma, a pediatric population requiring additional checkpoint inhibitor safety evaluation. Predictions assessed as knowledge graph structural proximity signals.
- **Ranks 5–8** (adenosine deaminase deficiency, reticular dysgenesis, immunoerythromyeloid hypoplasia, non-severe CID): Fundamental mechanistic incompatibility. Checkpoint inhibition requires functional effector T cells to exert any effect; in severe immunodeficiency states, these cells are absent or severely depleted. Furthermore, immune activation in patients with residual or recovering lymphocytes poses unpredictable autoimmune risk. These predictions are assessed as knowledge graph false positives and should not be advanced without extraordinary mechanistic evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

