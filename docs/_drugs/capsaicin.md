---
layout: default
title: Capsaicin
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Capsaicin
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

# Capsaicin: From Neuropathic Pain to Otitis Externa

## One-Sentence Summary

Capsaicin is a TRPV1 receptor agonist derived from hot peppers, recognized globally as a topical analgesic for neuropathic and musculoskeletal pain, with no registered indications in the current regulatory dataset.
The TxGNN model's top prediction identifies **Otitis Externa** as a potential new indication; however, the sole supporting literature (PMID 12769482) uses capsaicin as an inflammation-*inducing* tool in animal models — the mechanistic direction is opposite to therapeutic intent.
With **0 clinical trials** and **1 preclinical publication** (tool compound role, not therapeutic use), the evidence level is **L5** and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in current dataset (global use: neuropathic pain, musculoskeletal pain) |
| Predicted New Indication | Otitis Externa |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed (0 authorizations in dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Formal mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, capsaicin is the active pungent compound in chili peppers and a highly selective agonist at the TRPV1 (Transient Receptor Potential Vanilloid 1) channel — a calcium-permeable ion channel expressed on peripheral nociceptors. Its paradoxical analgesic effect proceeds in two phases: acute TRPV1 activation triggers an initial burning sensation, followed by sustained calcium influx that depletes neuropeptides (substance P, CGRP) from C-fiber endings and renders them transiently unresponsive. This "desensitization" mechanism underpins approved pharmaceutical products such as the Qutenza 8% patch, used for postherpetic neuralgia and diabetic peripheral neuropathy in multiple jurisdictions.

TRPV1 receptors are expressed beyond skin tissue, including in the epithelium of the external auditory canal and in mastoid cells. TxGNN's high prediction score (98.76%) likely reflects this tissue co-expression pattern within the underlying knowledge graph, creating a topologically plausible neurophysiological link between capsaicin's receptor targets and otitis externa pathology.

The critical problem is mechanistic directionality. Otitis externa is an inflammatory condition of the ear canal, and the only literature in this dataset (PMID 12769482) explicitly employs capsaicin to **provoke** acute ear inflammation in rodents as a positive-control model — it is a reagent for causing the disease, not treating it. Capsaicin's initial TRPV1 activation phase amplifies neurogenic inflammation before desensitization sets in; applying it to an already-inflamed and potentially infected ear canal would very likely intensify pain and worsen local inflammation acutely. There is no evidence that subsequent desensitization would produce a net therapeutic benefit in this context. The prediction score reflects co-expression correlations rather than a validated therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Capsaicin in Otitis Externa.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12769482](https://pubmed.ncbi.nlm.nih.gov/12769482/) | 2003 | Animal Model / Preclinical | Methods in Molecular Biology | Capsaicin used to **induce** acute ear inflammation in rodent models (positive control for neurogenic inflammation assays). This is a tool compound application — the mechanistic direction is opposite to a therapeutic role. |

---

## EU Market Information

No marketing authorizations for Capsaicin are recorded in the current regulatory dataset (total authorizations: 0; market status: not marketed).

> **Note:** Capsaicin-based pharmaceutical products are known to hold marketing authorizations in multiple international jurisdictions (e.g., Qutenza 179 mg cutaneous patch for peripheral neuropathic pain). The absence of records here may reflect dataset scope limitations and should be verified against the full EMA product database before drawing regulatory conclusions.

---

## Safety Considerations

Formal safety data (warnings, contraindications, drug interactions) is not available in this dataset. Please refer to the SmPC for complete safety information.

In addition, the following topical safety concern is relevant to the predicted indication: capsaicin causes intense burning and local neurogenic inflammation upon first application to sensitized tissue. Direct application to an already-inflamed, potentially infected external ear canal would be expected to cause severe acute pain and could worsen existing inflammation — representing a significant safety barrier independent of the mechanistic direction concern noted above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction for otitis externa is mechanistically reversed — the only available literature uses capsaicin specifically to *cause* ear canal inflammation as an experimental model tool, and there are no clinical trials or positive preclinical studies to suggest a therapeutic benefit.

**To proceed, the following is needed:**
- Positive therapeutic preclinical data demonstrating capsaicin *treating* (rather than inducing) otitis externa, specifically assessing the desensitization phase in an infected/inflamed ear canal environment
- Tolerability and safety data for topical capsaicin in the external ear canal
- Formal MOA documentation from DrugBank API (Data Gap DG002)
- Product monograph download and parsing to complete safety review (Data Gap DG001)

**Alternative predictions with stronger evidence (from this same dataset):**

| Rank | Indication | Evidence Level | Trial | Rationale |
|------|-----------|---------------|-------|-----------|
| 2 | Post-bacterial disorder | L4 | [NCT06807164](https://clinicaltrials.gov/study/NCT06807164) (Phase 2, n=123, Recruiting) | Three-arm RCT directly comparing capsaicin vs. Serratus Plane Block vs. Botox-A for chronic post-mastectomy neuropathic pain; TRPV1 desensitization mechanism is directly applicable |
| 5 | Post-infectious syndrome | L4 | 3 observational trials + 4 mechanism papers | TRPV1 sensitization in post-infectious IBS documented in clinical cohort (PMID 29051514); TRPV1-resolvin interaction supports desensitization strategy (PMID 33023902) |

These two indications represent meaningfully stronger repurposing candidates and would benefit from dedicated evidence packs and deeper review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

