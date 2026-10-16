---
layout: default
title: Eptifibatide
parent: AI Predictions (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Eptifibatide: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Prevention of early myocardial infarction in adults with unstable ang…"
---

# Eptifibatide
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

# Eptifibatide: From Unstable Angina / Non-ST-Elevation Myocardial Infarction to Rheumatoid Arthritis

## One-Sentence Summary

Eptifibatide is an injectable antiplatelet drug, originally used to prevent early myocardial infarction in patients with unstable angina or non-Q-wave myocardial infarction.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of early myocardial infarction in adults with unstable angina or non-Q-wave myocardial infarction (used with acetylsalicylic acid and unfractionated heparin) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | ✗ Cancelled only (no valid authorizations) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eptifibatide is a glycoprotein IIb/IIIa (αIIbβ3) antagonist. It blocks the final common pathway of platelet aggregation, which is why it works in acute coronary syndromes, where platelet-driven clots cause heart muscle damage.

The link to rheumatoid arthritis is hypothetical. Platelet activation is thought to contribute to synovial inflammation, so blocking platelet function could in theory influence joint inflammation. However, none of the data compiled for this report test this idea. The very high model score probably reflects patterns in the knowledge graph rather than demonstrated therapeutic benefit. Rheumatoid arthritis is a chronic autoimmune disease, whereas eptifibatide is a short-acting drug for acute care, so the clinical fit is also unclear.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Status | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004104 | Eptifibatide Accord | Cancelled | Eptifibatide Accord is intended for use with acetylsalicylic acid and unfractionated heparin. Eptifibatide Accord is in... |
| EMEA/H/C/000230 | Integrilin | Cancelled | Integrilin is intended for use with acetylsalicylic acid and unfractionated heparin. Integrilin is indicated for the pr... |

---

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links eptifibatide to thrombocytopenia, blood coagulation disease and impaired renal function as contraindications. These should be verified against the official product information.
- **Drug Interactions**: The data compiled for this report list 100 interactions. The main ones are:
  - **Major**: deferasirox, ibritumomab tiuxetan, tositumomab (I-131)
  - **Moderate**: acetylsalicylic acid, dexfenfluramine, fenfluramine, sibutramine
  - Other interactions with unclassified severity include pantoprazole, omeprazole, morphine, prednisone and simvastatin.
- **Bleeding risk**: As a potent antiplatelet agent, eptifibatide carries a systemic bleeding risk. This is a particular concern for any chronic or repeated use.

Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for rheumatoid arthritis is very high, but there is no trial, publication or other supporting evidence (L5). The mechanistic link is speculative, the drug is no longer marketed in the EU, and the bleeding risk and many interactions call for caution.

**Of note:** Among the other predictions, **hemoglobinopathy / sickle cell disease** has the strongest support (L2). It has a Phase 1/2 randomized, placebo-controlled trial ([NCT00834899](https://clinicaltrials.gov/study/NCT00834899), terminated with 13 participants), a Phase I study ([PMID 17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/)), a pilot study in acute pain episodes ([PMID 23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/)) and an inflammation analysis ([PMID 29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/)). These support safety and biological plausibility, but not efficacy, and it should be evaluated as a separate research question.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking GPIIb/IIIa blockade to rheumatoid arthritis
- Mechanism of action data confirmed from DrugBank
- Warnings and contraindications from the EMA product information, since the data compiled for this report lack them
- Assessment of route and regimen feasibility, given that eptifibatide is an acute intravenous therapy and the EU authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

