---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Deferiprone
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

# Deferiprone: From Transfusional Iron Overload to Hepatic Porphyria

## One-Sentence Summary

Deferiprone is an oral iron chelator established for treating transfusional iron overload in patients with thalassemia major, targeting toxic intracellular iron accumulation in the heart, liver, and other organs.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, particularly subtypes where excess hepatic iron worsens porphyrin-driven oxidative damage.
Currently **0 registered clinical trials** and **2 preclinical publications** support this direction, placing the evidence at **L4** (mechanism/animal model level).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Transfusional iron overload in thalassemia major |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (0 licenses in regulatory database) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Deferiprone (known as L1) is an oral bidentate iron chelator that binds ferric iron (Fe³⁺) in a 3:1 molar ratio and forms a stable complex excreted renally. Its key pharmacological advantage over deferoxamine is membrane permeability: deferiprone enters cells and removes iron from intracellular compartments, including cardiac myocytes, hepatocytes, and erythroid precursors. This property underlies its proven superiority over deferoxamine in clearing myocardial iron in thalassemia major patients.

In hepatic porphyria — specifically **Congenital Erythropoietic Porphyria (CEP)** and **Porphyria Cutanea Tarda (PCT)** — hepatic iron overload functions as a pathogenic cofactor. Excess intracellular iron catalyzes Fenton-type reactions, generating reactive oxygen species that amplify oxidative damage from accumulating non-physiological porphyrin isomers. This worsens both skin photosensitivity and chronic hemolytic anemia. Deferiprone's ability to chelate intracellular iron provides a mechanistically coherent rationale: reducing the iron substrate for Fenton chemistry could attenuate the porphyrin-iron oxidative cascade in iron-overloaded subtypes.

However, **"hepatic porphyria" is a heterogeneous diagnostic category** that includes diseases with fundamentally different pathophysiology. The mechanistic rationale applies selectively to iron-driven subtypes (CEP, PCT). Acute hepatic porphyrias — Acute Intermittent Porphyria (AIP), Variegate Porphyria (VP), and Hereditary Coproporphyria (HCP) — are triggered by enzyme deficiencies in the heme synthesis pathway and are not primarily iron-mediated. Deferiprone is unlikely to provide benefit in these subtypes and the prediction should be interpreted with this heterogeneity in mind.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Animal model + possible case series | *Blood* | Iron chelation rescued hemolytic anemia and skin photosensitivity in a CEP mouse model (UROS-deficient); results suggest that iron reduction — targeting the Fenton cascade — may be a viable therapeutic strategy in CEP |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Animal experiment | *Hepatology* | Deferiprone reduced hepatic uroporphyrin (URO) accumulation in Hfe⁻/⁻ mice given ALA (a PCT model); efficacy was comparable to iron-deficient diet, validating iron depletion as a mechanistic intervention in PCT-like uroporphyria |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Two data gaps have been identified that affect safety evaluation:
> - **DG001 (Blocking):** TFDA labeling warnings and contraindications are unavailable — full S1 safety screening cannot be completed.
> - **DG002 (High):** MOA documentation is absent — limits mechanistic link analysis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence is preclinical (L4: animal models only), and the target population within "hepatic porphyria" is narrow — the mechanistic rationale holds for iron-overloaded subtypes (CEP, PCT) but not for acute hepatic porphyrias. Without human clinical data and with critical safety data gaps unresolved, this candidate is not ready to advance.

**To proceed, the following is needed:**
- **Subtype specificity:** Restrict the repurposing target to CEP and/or PCT with documented iron overload, rather than the broader "hepatic porphyria" grouping
- **Safety gap resolution (DG001):** Retrieve SmPC or TFDA labeling to complete contraindication and warning review
- **MOA documentation (DG002):** Obtain structured DrugBank MOA data to strengthen the mechanistic rationale dossier
- **Human case evidence:** Identify published case reports or retrospective series of CEP/PCT patients who received deferiprone, to establish whether preclinical benefits translate clinically
- **Biomarker eligibility criteria:** Define serum ferritin and transferrin saturation thresholds as inclusion criteria for any future pilot study, ensuring iron overload is confirmed in enrolled patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

