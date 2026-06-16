---
layout: default
title: Choriogonadotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Choriogonadotropin Alfa
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

# Choriogonadotropin alfa: From Assisted Reproductive Technology to Peptic Esophagitis

## One-Sentence Summary

Choriogonadotropin alfa is a recombinant form of human chorionic gonadotropin (hCG), used clinically to trigger final oocyte maturation in assisted reproductive technology (ART) procedures.
The TxGNN model predicts it may be effective for **Peptic Esophagitis**,
however **0 clinical trials** and **0 publications** currently support this direction — making this an AI-only prediction with no empirical backing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Triggering final follicular maturation and early luteinization in ART (no EU authorization data available) |
| Predicted New Indication | Peptic Esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (no authorizations found in current dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, choriogonadotropin alfa is a recombinant hCG that acts on luteinizing hormone/choriogonadotropin receptors (LHCGR), primarily expressed in gonadal tissue. Its established role is to trigger the LH surge equivalent needed for final oocyte maturation and ovulation induction in ART cycles.

The predicted link to peptic esophagitis is mechanistically weak. The hCG/LHCGR signaling axis has no known expression in esophageal mucosa. While gastroesophageal reflux disease (GERD) is indeed common during pregnancy — a high-hCG physiological state — the underlying mechanism involves progesterone-mediated lower esophageal sphincter relaxation combined with mechanical compression from the gravid uterus, rather than any direct hCG effect on esophageal tissue.

The high TxGNN score (98.44%) most likely reflects an indirect topological association in the knowledge graph: the path "hCG → pregnancy → gastrointestinal symptoms → esophagitis" creates a graph-level proximity that does not translate into a direct pharmacological mechanism. This is a recognized pattern of topological pseudo-correlation in knowledge graph-based predictions and should not be interpreted as biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU/EMA marketing authorizations found for Choriogonadotropin alfa in the current dataset.

> **Note:** Choriogonadotropin alfa (Ovitrelle®) is known to hold EMA authorization for ART indications. The absence of data here reflects a gap in the current regulatory data pipeline, not the actual regulatory status. Manual verification against the EMA product database is recommended.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> No drug interaction data, key warnings, or contraindication data were available in the current evidence pack. TFDA SmPC data retrieval is listed as a blocking data gap (DG001). Full safety review cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure AI model prediction (L5) with no supporting clinical trials or published literature. The mechanistic link between choriogonadotropin alfa and peptic esophagitis is biologically implausible — the hCG/LHCGR axis has no established role in esophageal physiology, and the TxGNN high score is attributable to indirect knowledge graph topology rather than true biological signal.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain SmPC/prescribing information to complete safety assessment before any further evaluation
- **Resolve DG002 (High):** Confirm full MOA profile via DrugBank API to verify whether any off-target receptor activity could theoretically involve esophageal tissue
- **Mechanistic pre-screen:** Conduct a literature review on LHCGR expression in gastrointestinal/esophageal tissue to formally rule out or confirm the mechanistic link
- **Reconsider top candidate:** Among the 10 predicted indications, **Raynaud disease** (Rank 4) carries the most biologically coherent rationale (pregnancy-associated symptom improvement, LHCGR expression in vascular smooth muscle, progesterone-mediated vasodilation hypothesis) and would be the preferred candidate for a focused mechanistic research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

