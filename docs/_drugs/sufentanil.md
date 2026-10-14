---
layout: default
title: Sufentanil
parent: AI Predictions (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Sufentanil
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

# Sufentanil: From Acute Moderate to Severe Pain to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Sufentanil is a potent opioid analgesic, originally authorised in the EU (as Dzuveo) for managing acute moderate to severe pain in adults.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and **0 publications** supporting this prediction; the score is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Management of acute moderate to severe pain in adult patients |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 97.41% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general pharmacology, sufentanil is a potent mu-opioid receptor agonist, and its efficacy in acute pain is the basis of its original authorisation.

The link to the predicted indication is weak. NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). Opioids can modestly influence vasopressin release, but no plausible mechanistic connection between mu-opioid agonism and correcting a constitutively active V2 receptor has been established. The high TxGNN score (0.974) should therefore be treated as a model-generated hypothesis rather than a mechanistically supported finding.

Other top-ranked predictions (for example common cold, gastroduodenitis, peptic ulcer disease and familial periodic paralysis) also lack a therapeutic rationale. Several retrieved papers describe opioid adverse effects or unrelated topics, which suggests keyword artefacts rather than real signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004335 | Dzuveo (status: cancelled) | Not specified | Management of acute moderate to severe pain in adult patients. |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationship data, not label text): kidney disease, pyoureter, liver disease, gallbladder disease. These are of particular concern given that the predicted indication is a renal-related condition.
- **Drug Interactions**: The interaction screen returned 100 records (20 reviewed here). Major-level interactions include:
  - Bupropion
  - Lorcaserin
  - Dolasetron
  - Naltrexone
  - Palonosetron

  Moderate-level interactions include morphine, naloxone, cimetidine, clarithromycin, aprepitant, atropine, hyoscyamine, glycopyrronium and dronabinol, among others. Combination with other opioids, opioid antagonists, serotonergic agents or CYP3A4 inhibitors needs careful review.
- **General class concerns**: Respiratory depression and dependence risk are well-known for potent opioids. Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no supporting literature and no plausible mechanistic link between mu-opioid agonism and the AVPR2-driven pathology of NSIAD. The only EU authorisation has been cancelled, and the knowledge graph flags kidney disease as a contraindication.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale linking sufentanil to vasopressin V2 receptor signalling
- Preclinical or in vitro evidence in NSIAD models
- Complete warnings and contraindications from the SmPC
- A formal safety assessment for renal and hepatic impairment
- Review of alternative candidate indications. Of the other predictions, only headache disorder has indirect evidence (L4), and opioids are generally discouraged there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

