---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Cryopyrin-Associated Periodic Syndrome (CAPS) to Hepatic Infarction

## One-Sentence Summary

Canakinumab (Ilaris) is a fully human anti-IL-1β monoclonal antibody developed by Novartis, originally approved for cryopyrin-associated periodic syndromes (CAPS) including familial cold autoinflammatory syndrome (FCAS) and Muckle-Wells syndrome (MWS).
The TxGNN model predicts it may also be effective for **Hepatic Infarction** with a prediction score of **99.86%**;
however, currently **no clinical trials** and only **1 tangentially related publication** support this specific direction, placing it at the lowest evidence tier (**L5 — model prediction only, no actual studies**).

> ⚠️ **Note:** While hepatic infarction ranks #1 by TxGNN score, TxGNN also predicts Canakinumab for **Familial Mediterranean Fever** (rank #6) with **7 clinical trials** and **20 publications** at **L1 evidence**. Reviewers are advised to consider the full ranked list in context.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cryopyrin-Associated Periodic Syndrome (CAPS) — inferred from published literature; Taiwan regulatory data not available |
| Predicted New Indication | Hepatic Infarction |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known published information, Canakinumab is a fully human IgG1/κ monoclonal antibody that selectively binds and neutralizes interleukin-1β (IL-1β), thereby suppressing downstream pro-inflammatory cascades mediated through IL-1 receptor type I (IL-1RI). This mechanism has been clinically validated across multiple IL-1β-driven autoinflammatory diseases, including CAPS, systemic juvenile idiopathic arthritis (sJIA), familial Mediterranean fever (FMF), TNF receptor-associated periodic syndrome (TRAPS), and hyperimmunoglobulinemia D syndrome/mevalonate kinase deficiency (HIDS/MKD).

The biological rationale for hepatic infarction rests on the known role of IL-1β in hepatic ischemia-reperfusion injury (IRI). Following hepatic vascular occlusion and reperfusion, IL-1β acts as a key amplifier of the sterile inflammatory cascade, promoting Kupffer cell activation, neutrophil recruitment, and hepatocyte apoptosis. Theoretically, neutralizing IL-1β could attenuate post-ischemic tissue damage. However, this mechanistic link is highly speculative — no direct preclinical or clinical studies have examined Canakinumab specifically in the context of hepatic infarction.

The TxGNN model assigned this prediction a high rank (score 99.86%), likely capturing indirect network relationships between Canakinumab's IL-1β inhibition mechanism and hepatic inflammatory pathology rather than a direct clinical or mechanistic signal. The single literature item retrieved (PMID 37354546) concerns bempedoic acid in cardiovascular prevention and is not relevant to this indication, confirming the absence of a real evidence base.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Canakinumab in hepatic infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37354546](https://pubmed.ncbi.nlm.nih.gov/37354546/) | 2023 | RCT | JAMA | Bempedoic acid vs. placebo for primary cardiovascular prevention in statin-intolerant patients without prior cardiovascular events. **Not relevant** to Canakinumab or hepatic infarction — retrieved by indirect cardiovascular query association. |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Taiwan TFDA SmPC label warnings and contraindications were not available in this evidence pack. Drug-drug interaction data query returned no results. Full safety evaluation requires TFDA label retrieval prior to any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Canakinumab in hepatic infarction is entirely model-derived (L5) with no supporting clinical trials or directly relevant literature. Although the IL-1β pathway is biologically involved in hepatic ischemia-reperfusion injury, this mechanistic link has not been validated in any preclinical or clinical study, making advancement beyond a speculative hypothesis premature.

**To proceed, the following is needed:**
- Preclinical studies (e.g., murine hepatic IRI models) evaluating IL-1β blockade in hepatic infarction to establish proof of concept
- Mechanism of action clarification specifically in the context of hepatic vascular injury
- Taiwan TFDA SmPC retrieval for complete safety profiling (warnings, contraindications)
- Drug-drug interaction assessment in hepatic disease populations
- Identification of a clinically plausible patient subgroup (e.g., post-transplant hepatic IRI with excessive inflammatory response) where IL-1β neutralization could offer benefit
- **Prioritization recommendation:** Redirect resources toward the FMF (rank #6, L1, 7 trials) and periodic fever syndrome (rank #5, L3, 19 publications) predictions, where the mechanistic basis is established and regulatory precedent exists in other jurisdictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

