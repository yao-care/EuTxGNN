---
layout: default
title: Ferric Maltol
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Ferric Maltol
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

# Ferric Maltol: From Iron Deficiency Therapy to Plummer-Vinson Syndrome

> **Note on original indication**: `original_indications` and EU license data are both empty in this Evidence Pack. The "oral iron replacement" framing below is drawn from the drug's mechanistic description in the repurposing rationale, not from a confirmed regulatory indication text. This should be verified before proceeding.

## One-Sentence Summary

Ferric maltol is an oral ferric iron compound; based on the available evidence pack, its confirmed original indication and formal marketing status could not be established (not currently marketed in the EU per this dataset). The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome** (a chronic iron-deficiency condition with esophageal web), but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no licenses on file; drug described only as an oral ferric iron compound) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Ferric maltol is not available in this evidence pack. Based on the information that is available, Ferric maltol is an oral trivalent (ferric) iron compound formulated for improved tolerability and absorption relative to conventional oral iron salts.

Plummer-Vinson (Paterson-Kelly) syndrome is pathophysiologically defined by chronic iron-deficiency anemia accompanied by esophageal web formation and dysphagia. Since iron repletion is the established causal treatment for the anemia component of this syndrome, an oral iron compound is mechanistically well-aligned with this indication — this is best understood as an extension of a known pharmacological action to a related, rarer diagnosis, rather than a novel mechanistic hypothesis. No direct clinical trial or literature evidence for Ferric maltol in Plummer-Vinson syndrome specifically was found; the rationale rests entirely on mechanistic plausibility and the TxGNN association score.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Not currently marketed in the EU; no marketing authorisations are on file for this drug in the evidence pack (`total_licenses = 0`).

## Safety Considerations

Please refer to the SmPC for safety information.

*(No key warnings, contraindications, or drug-drug interaction data were returned from the queried sources for Ferric maltol.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model score (L5 — no clinical trials, no literature) and a plausible-but-unverified mechanistic argument. There is also a **Blocking** data gap on regulatory safety labeling (TFDA/SmPC warnings and contraindications) and a **High**-severity gap on confirmed mechanism of action, so the candidate cannot proceed past the research-question stage.

**To proceed, the following is needed:**
- Confirmed original indication and marketing history for Ferric maltol (source data currently empty)
- Official label/SmPC warnings, contraindications, and drug interaction data (currently blocking S1 safety screening)
- Verified mechanism of action from DrugBank or manufacturer labeling
- Targeted literature/trial search specifically for iron therapy in Plummer-Vinson syndrome (general iron-deficiency-anemia literature was not queried here and may exist even though disease-specific trials do not)

*Lower-ranked candidates (ranks 2–10: e.g., vitamin B12/folate-independent megaloblastic anemia, IRIDA syndrome, biotin metabolic disease, diabetic retinopathy, ariboflavinosis, Keshan disease, non-syndromic esophageal malformation, folic acid deficiency anemia, protein-energy malnutrition) all carry mechanistic contradictions or no plausible mechanistic link per the rationale notes provided, and are assessed at decision stage S0 / Hold — they are not carried forward in this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

