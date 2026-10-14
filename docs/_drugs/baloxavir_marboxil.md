---
layout: default
title: Baloxavir Marboxil
parent: AI Predictions (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Baloxavir Marboxil
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

# Baloxavir marboxil: From Influenza to Acquired Hemophagocytic Lymphohistiocytosis Associated with Malignant Disease

## One-Sentence Summary

Baloxavir marboxil is an antiviral originally authorised in the EU for treating and preventing influenza.
The TxGNN model predicts it may be effective for **acquired hemophagocytic lymphohistiocytosis associated with malignant disease**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of uncomplicated influenza in patients aged 1 year and above, and post-exposure prophylaxis of influenza in individuals aged 1 year and above |
| Predicted New Indication | Acquired hemophagocytic lymphohistiocytosis associated with malignant disease |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorisation is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Baloxavir marboxil is a prodrug of baloxavir acid, a selective inhibitor of the influenza cap-dependent endonuclease (the PA subunit of the viral polymerase). Detailed mechanism-of-action data were not available in the data compiled for this report, so this description relies on general pharmacological knowledge.

Malignancy-associated hemophagocytic lymphohistiocytosis (HLH) is driven by immune over-activation: a cytokine storm with activated CD8+ T cells and macrophages. It is not driven by influenza polymerase activity, and no plausible mechanistic link to baloxavir was identified. The high score (98.85%) is a computational prediction, most likely reflecting network proximity to infection-triggered HLH, and no trial or publication supports it.

Other predictions among the top 10 are also weakly supported:
- **Hemophagocytic syndrome associated with an infection** (98.85%) is the most biologically plausible. Viruses, including influenza, can trigger HLH, so treating the trigger could theoretically help. However, baloxavir would not address the underlying hyperinflammation, and the link is speculative.
- **Hemophagocytic syndrome, general** (94.97%) has the same considerations.
- **Hepatitis C, hepatitis E, hepatitis A and Omsk hemorrhagic fever** (92.0–95.0%) involve viruses that do not use cap-snatching, so baloxavir's target is absent. Curative antivirals already exist for hepatitis C.
- **Fatal infantile cardioencephalomyopathy due to cytochrome c oxidase deficiency** (98.55%) and **Singleton-Merten syndrome** (97.81%) have no mechanistic rationale and are likely graph-based artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004974 (cancelled) | Xofluza | Not specified | Treatment of influenza: uncomplicated influenza in patients aged 1 year and above. Post-exposure prophylaxis of influenza in individuals aged 1 year... |

## Safety Considerations

- **Drug Interactions**: 26 interactions were recorded in total, and the 20 listed in the data compiled for this report are all rated Moderate. They involve polyvalent cation-containing products, which are known to reduce absorption of baloxavir by chelation:
  - Aluminium and magnesium antacids and salts (aluminium hydroxide, magaldrate, magnesium carbonate, chloride, citrate, gluconate, hydroxide, oxide and sulfate)
  - Calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate and phosphate)
  - Iron
  - Adsorbents and protectants (attapulgite, kaolin and sucralfate)

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5) and no plausible mechanistic link, because malignancy-associated HLH is an immune-dysregulation disease rather than a cap-dependent endonuclease-driven infection. The only EU authorisation is cancelled.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank, and a mechanistic assessment of whether any antiviral effect could matter in HLH
- Warnings and contraindications from the SmPC, which are needed for safety screening
- Preclinical or observational evidence, such as case series of influenza-triggered HLH treated with baloxavir
- If the focus is infection-associated HLH, a more plausible alternative to the malignancy-associated form, a targeted literature search and a defined study population (influenza-triggered cases only)
- Route and dosage form compatibility confirmation for the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

