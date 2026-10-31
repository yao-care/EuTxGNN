---
layout: default
title: Caspofungin
parent: AI Predictions (L5)
nav_order: 133
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Caspofungin: predicted new indication Gastrin secretion abnormality (evidence level L5). Approved use: Invasive candidiasis"
monitor_inn: "Caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Caspofungin: From Invasive Fungal Infections to Gastrin Secretion Abnormality
{: .text-alpha }

## One-Sentence Summary

Caspofungin is an intravenous antifungal originally used to treat invasive candidiasis, invasive aspergillosis that has not responded to other treatments, and suspected fungal infections in febrile, neutropaenic patients.
The TxGNN model predicts it may be effective for **gastrin secretion abnormality**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive candidiasis; invasive aspergillosis refractory to or intolerant of other antifungals; empirical therapy for presumed fungal infections in febrile, neutropaenic patients (adults and children) |
| Predicted New Indication | Gastrin secretion abnormality |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Caspofungin belongs to the echinocandin class, which inhibits fungal beta-(1,3)-D-glucan synthase, an enzyme needed to build the fungal cell wall. Its efficacy in invasive fungal infections is established.

This mechanism does not obviously extend to gastrin secretion abnormality. Mammalian cells have no beta-glucan synthase, so the drug has no known target in the pathways that regulate gastrin release. The high TxGNN score (0.9944) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Nothing in the data compiled for this report shows a biological, clinical, or literature link between caspofungin and gastrin regulation, so the prediction is best treated as a hypothesis-generating signal only.

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (these come from drug-disease links in the TxGNN knowledge graph, not from the product label): liver disease, gallbladder disease, and potassium deficiency disease.
- **Drug Interactions**: 81 interacting drugs are recorded. Those with a graded severity are:
  - **Major**: dexamethasone
  - **Moderate**: naltrexone
  - Many other recorded interactions have no severity grade. Examples are pantoprazole, omeprazole, lansoprazole, simvastatin, amphotericin B, vancomycin, prednisone, hydrocortisone, and potassium chloride.

Label warnings and contraindications were not available for this report. Please refer to the SmPC for the full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no registered trials and no publications, and no plausible mechanistic link to gastrin regulation. The EU authorization for the product is also cancelled.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking caspofungin to gastrin secretion, supported by preclinical data
- Label-based safety data (warnings and contraindications) and mechanism of action data

**Note on other predictions:** This report covers the top-ranked prediction only. Other predictions in the same list have more support. Neonatal candidiasis in particular has two Phase 2 trials, a meta-analysis, and an extension-of-indication rationale that rated it "Proceed with Guardrails". If the goal is to find a repurposing opportunity for caspofungin, that candidate is a better one to evaluate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

