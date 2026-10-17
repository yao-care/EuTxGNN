---
layout: default
title: Fosaprepitant
parent: AI Predictions (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fosaprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Prevention of nausea and vomiting associated with highly and moderate…"
monitor_inn: "Fosaprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fosaprepitant was originally used to prevent nausea and vomiting caused by highly and moderately emetogenic cancer chemotherapy.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of nausea and vomiting associated with highly and moderately emetogenic cancer chemotherapy in adults and paediatric patients aged 6 months and older (given as part of a combination therapy) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Fosaprepitant is known to be a prodrug of aprepitant, a neurokinin-1 (NK1) receptor antagonist, and its efficacy in chemotherapy-induced nausea and vomiting is established. This is general pharmacological knowledge, not part of the compiled data.

The link to the predicted indication is weak. NSIAD arises from gain-of-function mutations in the vasopressin V2 receptor (AVPR2), and no established pathway connects NK1 receptor blockade to V2 receptor signalling. The high TxGNN score reflects a pattern in a knowledge graph and is not backed by clinical or literature evidence. Until a mechanistic hypothesis and supporting data exist, this prediction should be treated as a computational lead only.

Other predicted indications in the model output (pneumocystosis, leprosy, cryptococcal meningitis, multiple endocrine neoplasia, intracranial abscess, Plasmodium falciparum malaria, echinococcosis, hyperargininemia) also lack any clinical or literature support. The only one with any supporting publication is retinitis (rank 7), where a single preclinical mouse study reports that fosaprepitant blocks UVR-B-induced NK1 receptor expression in ocular tissues. That evidence is indirect, since it concerns UV-induced ocular damage rather than retinitis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000743 | Ivemend (status: cancelled) | Not specified | Prevention of nausea and vomiting associated with highly and moderately emetogenic cancer chemotherapy in adults and paediatric patients aged 6 months and older. Ivemend 150 mg is given as part... |

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: The TxGNN knowledge graph lists a drug-disease contraindication edge with **liver failure**.
- **Drug Interactions**: 100 interactions were found in the DDI query. Those listed in the data are mostly of Moderate severity. Two are **Major**:
  - **Eliglustat**
  - **Naloxegol**

  Moderate-level examples include corticosteroids (dexamethasone, hydrocortisone, betamethasone, budesonide, triamcinolone), proton pump inhibitors (rabeprazole, lansoprazole), clarithromycin, cimetidine, miconazole, and several antidiabetic agents (pioglitazone, saxagliptin, glimepiride, nateglinide).

Label warnings and contraindications were not available. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5), and no plausible mechanistic link between NK1 antagonism and the vasopressin V2 receptor pathway has been identified. The only EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a testable hypothesis connecting NK1 signalling to NSIAD
- Preclinical or case-level evidence in NSIAD or related V2 receptor models
- SmPC warnings and contraindications to complete safety screening
- Review of liver-failure contraindication and the Major interactions (eliglustat, naloxegol) if any development is considered
- Clarification of the current EU regulatory status, given the cancelled authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

