---
layout: default
title: Pretomanid
parent: AI Predictions (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
---

# Pretomanid
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

# Pretomanid: From Drug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

Pretomanid is an anti-tuberculosis drug, used in combination with bedaquiline and linezolid for extensively drug-resistant (XDR) or treatment-intolerant/nonresponsive multidrug-resistant (MDR) pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **candidiasis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
This is a computational prediction only, and no mechanistic basis for antifungal activity has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary XDR, or treatment-intolerant/nonresponsive MDR, tuberculosis (in combination with bedaquiline and linezolid, adults) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Pretomanid is a nitroimidazooxazine prodrug. It is activated in *Mycobacterium tuberculosis* by the F420-dependent enzyme Ddn (deazaflavin-dependent nitroreductase). Once activated, it is thought to release nitric oxide (respiratory poisoning) and to inhibit mycolic acid synthesis.

This mechanism does not support the prediction. Fungi such as *Candida* lack the mycobacterial activation pathway and mycolic acid synthesis, so antifungal activity is not expected. The very high TxGNN score (0.997) most likely reflects relationships in the knowledge graph rather than biological rationale. It should be treated as a hypothesis only, and the report found no trials or literature to support it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005167 (cancelled) | Dovprela (previously Pretomanid FGK) | Not specified | Dovprela is indicated in combination with bedaquiline and linezolid, in adults, for the treatment of pulmonary extensively drug resistant (XDR), or treatment-intolerant or nonresponsive... |

---

## Safety Considerations

- **Drug Interactions**: 14 interactions were recorded. Major-level interactions are listed with:
  - Dexamethasone
  - Lumacaftor
  - Apalutamide
  - Dabrafenib
  - Mitotane
  - Lorlatinib
  - Enzalutamide

  Moderate-level interactions are listed with empagliflozin, sitagliptin, somatotropin, somatrem, baricitinib, clofarabine and methotrexate.

Warnings and contraindications from the product information were not available. Please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based on the model score alone. There are no clinical trials or literature, and pretomanid's mechanism, which depends on a mycobacterial activation pathway, gives no reason to expect antifungal activity. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- In vitro antifungal susceptibility testing against *Candida* species as a first step
- Evidence that fungi have a pathway able to activate pretomanid
- Mechanism of action data and the product information warnings and contraindications (SmPC)
- Clarification of the status of the cancelled EU authorization

---

### Note on Other Predictions

Other predictions were also reviewed for context. All are Hold, except Bacteroidaceae infectious disease, which is a Research Question:

- **Leprosy** (99.27%): plausible in principle because of the biological relation between mycobacteria, but none of the retrieved publications addresses leprosy, and no leprosy-specific evidence was found.
- **Bacteroidaceae infection** (98.67%): the most plausible of the hypotheses because of the nitroimidazole scaffold, but no direct evidence was found and existing nitroimidazoles already cover this use.
- **HIV infection** (98.85%): the literature concerns TB/HIV co-infection, not treatment of HIV itself, and is already within the approved TB scope. Drug interactions with antiretrovirals are a relevant consideration.
- **Cardiac conditions, thrombocytopenia, oral candidiasis and fascioliasis**: no plausible mechanistic link. The thrombocytopenia prediction may reflect an adverse-event association with the combination regimen.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

