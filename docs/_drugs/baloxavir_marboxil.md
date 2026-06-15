---
layout: default
title: Baloxavir Marboxil
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Baloxavir Marboxil
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

# Baloxavir marboxil: From Influenza to Acquired HLH Associated with Malignant Disease

## One-Sentence Summary

Baloxavir marboxil is a novel cap-snatching endonuclease (CEN) inhibitor originally developed for the treatment of acute influenza in adults and adolescents.
The TxGNN model predicts it may be effective for **Acquired Hemophagocytic Lymphohistiocytosis (HLH) Associated with Malignant Disease**,
however, this remains a **model-only prediction (L5)** with **no supporting clinical trials or literature** currently identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute influenza (cap-snatching endonuclease inhibitor / antiviral) |
| Predicted New Indication | Acquired Hemophagocytic Lymphohistiocytosis Associated with Malignant Disease |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the system. Based on contextual information embedded in the evidence pack, Baloxavir marboxil functions as a cap-snatching endonuclease (CEN) inhibitor, selectively targeting the PA subunit of the influenza RNA-dependent RNA polymerase complex. By blocking the CEN domain, it prevents the influenza virus from cleaving host cell mRNA to generate primers for viral mRNA synthesis — a mechanism entirely specific to influenza viral replication and structurally unrelated to host immune pathways.

The predicted indication, malignancy-associated HLH, is a life-threatening hyperinflammatory syndrome driven primarily by tumor-mediated immune evasion, uncontrolled macrophage activation, and a cytokine storm (interferon-γ, IL-6, IL-18). This pathophysiology has no established dependency on viral polymerase activity. Unlike infection-triggered HLH — where reducing viral load could theoretically dampen persistent immune activation — malignancy-driven HLH does not involve active viral replication as a primary trigger. Baloxavir's CEN inhibition therefore has no recognized molecular target in this disease context.

The high TxGNN score (98.85%) most likely reflects a knowledge graph topology artifact: the HLH disease node shares graph edges with influenza-associated HLH, causing the model to elevate Baloxavir's ranking despite the absence of a direct pharmacological rationale. This pattern — where a disease concept shares a network neighborhood with an antiviral's known pathology — is a recognized source of false positives in graph-based drug repurposing models, and should not be interpreted as clinical plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Malignancy-associated HLH is mechanistically disconnected from Baloxavir's antiviral target (influenza PA-CEN); the unusually high TxGNN prediction score is attributed to a knowledge graph topology artifact — shared network proximity between influenza-related HLH and malignancy-related HLH nodes — rather than genuine pharmacological plausibility.

**To proceed, the following is needed:**
- Obtain complete drug label and safety data (EMA SmPC or equivalent regulatory dossier) to resolve current data gaps
- Retrieve DrugBank mechanism of action data for Baloxavir marboxil (DB13997) via DrugBank API
- Conduct a targeted case-report literature search for Baloxavir use in influenza-associated HLH specifically, which carries greater biological plausibility than the malignancy-associated subtype
- Consider re-prioritizing the evaluation to **Rank 2 (hemophagocytic syndrome associated with an infection)** or **Rank 5 (hemophagocytic syndrome, general)**, both of which carry a "Research Question" recommendation and a mechanistically defensible rationale — influenza is a recognized HLH trigger, and antiviral-mediated viral load reduction could theoretically attenuate immune hyperactivation
- If the infection-associated HLH angle is pursued further, a systematic review of influenza-associated HLH outcomes and any case reports of antiviral intervention would be the minimum evidence threshold before advancing to hypothesis generation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

