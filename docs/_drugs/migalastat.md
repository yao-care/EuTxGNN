---
layout: default
title: Migalastat
parent: AI Predictions (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Migalastat
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

# Migalastat: From Fabry Disease to Primitive Portal Vein Thrombosis

## One-sentence summary

Migalastat was originally approved for treatment of Fabry disease (an X-linked hereditary lysosomal storage disorder), with a mechanism of action as a pharmacological chaperone that can stabilize mutant α-galactosidase A enzyme.
The TxGNN model predicts it may be effective for **primitive portal vein thrombosis**,
but there are currently **no clinical trials** and **no literature** supporting this direction, with evidence level L5 (pure model prediction), and the evidence package's own mechanism analysis has clearly indicated that there is no direct molecular mechanism connection between the two.

---

## Quick overview

| Item | Content |
|------|---------|
| Original indication | Fabry disease (inferred from evidence package mechanism description; official MOA field awaiting formal confirmation) |
| Predicted new indication | Primitive portal vein thrombosis |
| TxGNN prediction score | 98.85% |
| Evidence level | L5 (model prediction, no clinical/literature evidence) |
| Taiwan market status | Not marketed |
| Number of approvals | 0 |
| Recommended decision | Hold |

---

## Why is this prediction questionable?

According to the mechanism description in the evidence package, migalastat is a pharmacological chaperone that specifically binds and stabilizes mutant α-galactosidase A enzyme, thereby restoring enzyme activity, which is the core mechanism of its therapeutic action in Fabry disease. However, the official mechanism of action (MOA) field of the drug itself is currently blank, constituting one of the data gaps in this assessment (DG002), and it is recommended that this be completed via DrugBank API.

Primitive portal vein thrombosis's primary mechanism involves coagulation dysfunction or local blood flow obstruction, with no known molecular pathway overlap with α-galactosidase A enzyme stabilization. The mechanism association analysis within the evidence package (repurposing_rationale) also clearly indicates: "High TxGNN scores may reflect rare disease clustering characteristics in the knowledge graph rather than mechanism correspondence."

Notably, each of the top 10 candidate indications listed in this assessment (primitive portal vein thrombosis, hepatic portal sclerosis, hepatopulmonary syndrome, familial non-cirrhotic portal hypertension, idiopathic copper-related cirrhosis, hepatic porphyria, mitochondrial oxidative phosphorylation disorder, tyrosine metabolism disorder, Pierre Robin sequence, hepatic nodular regenerative hyperplasia) has its mechanism association annotated by the evidence package itself as "weak" or "no direct molecular association." This strongly suggests that this batch of predictions results from rare disease/metabolic disorder clustering effects in the knowledge graph, rather than genuinely pharmacologically grounded drug repurposing hypotheses, and should be viewed with caution.

---

## Clinical trial evidence

No relevant clinical trials are currently registered

---

## Literature evidence

No relevant literature is currently available

---

## Taiwan market information

This drug has **not yet obtained any approval** in Taiwan (0 approved records); its market status is "Not marketed." Therefore, domestic approved indications, dosage forms, or approval numbers cannot be provided.

---

## Safety considerations

Please refer to the originator's SmPC (EU/US package insert) for safety information. Since this drug is Not marketed in Taiwan and EMA package insert warnings/contraindications data is a blocking data gap (DG001), S1 safety initial assessment cannot currently be completed.

---

## Conclusion and next steps

**Decision: Hold**

**Rationale:**

This candidate has only TxGNN model score support (L5, no clinical trials, no literature), and the mechanism analysis within the evidence package has self-annotated "weak mechanism association / no direct association"; meanwhile, the drug is Not marketed in Taiwan and TFDA safety data represents a blocking data gap, so it currently does not meet conditions for proceeding to the next stage of assessment.

**To proceed further, the following are required:**
- Complete TFDA package insert warnings and contraindications data (DG001, blocking gap, requiring download and parsing of TFDA package insert PDF)
- Verify official mechanism of action (MOA) data via DrugBank API (DG002)
- Conduct independent literature searches for higher-ranked candidate indications (such as primitive portal vein thrombosis) to confirm whether there are mechanism hypotheses or case reports not yet captured
- If mechanism rationale and safety data cannot be adequately supplemented, it is recommended to defer this batch of candidates and prioritize candidate drugs with higher evidence levels (L1-L3)

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

