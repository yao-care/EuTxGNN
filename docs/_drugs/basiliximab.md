---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Basiliximab
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

# Basiliximab: From Transplant Rejection Prevention to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab is a chimeric anti-CD25 (IL-2Rα) monoclonal antibody, originally developed for prevention of acute rejection following solid organ transplantation by selectively blocking T-cell activation.
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma** (multiple myeloma), with **3 clinical trials** and **3 publications** currently supporting this direction.
The core hypothesis is that CD25 blockade can selectively deplete regulatory T cells (Tregs) during autologous stem cell transplantation, thereby restoring anti-myeloma immune surveillance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Transplant rejection prevention (solid organ / HSCT) |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed (0 authorizations on record) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from structured data sources. Based on known information, Basiliximab is a chimeric monoclonal antibody that targets CD25 — the alpha subunit of the interleukin-2 receptor (IL-2Rα) — expressed on activated T cells. By competitively blocking CD25, it prevents IL-2–driven clonal T-cell expansion, thereby suppressing acute transplant rejection. This mechanism is well-established across solid organ transplantation contexts.

In the multiple myeloma (plasma cell myeloma) setting, the repurposing rationale is mechanistically compelling. CD25 is also constitutively expressed on regulatory T cells (Tregs), which inhibit cytotoxic immune responses against myeloma cells. During autologous stem cell transplantation (ASCT) — the standard of care for eligible MM patients — Tregs reconstitute rapidly and are thought to blunt the graft-versus-myeloma (GvM) effect. Selectively depleting these Tregs with Basiliximab at the time of ASCT could therefore restore anti-tumor immune surveillance and improve long-term disease control.

The mechanistic bridge is well-supported: a published Phase 1 trial (PMID 31940591) directly tested this hypothesis in MM patients undergoing ASCT, demonstrating that Treg depletion via CD25 blockade is both feasible and biologically rational. Additionally, in allogeneic HSCT settings, GvHD prevention with Basiliximab directly enables successful engraftment — a prerequisite for any graft-versus-myeloma benefit — extending the drug's relevance across the full HSCT treatment continuum for myeloma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Treg depletion via Basiliximab in MM patients undergoing ASCT — evaluated safety and feasibility of regulatory T-cell reduction to enhance anti-myeloma immune response post-transplant |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab + cyclosporine for GvHD prevention after nonmyeloablative allogeneic transplantation for hematologic malignancies — established IL-2R blockade safety profile in the HSCT context |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | N/A | Terminated | 10 | Basiliximab vs. cyclosporine alone for GvHD prevention after transplant — terminated early due to poor enrollment; limited interpretability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Phase 1 Trial Report | Journal for Immunotherapy of Cancer | Direct evidence in MM: Tregs reconstitute rapidly post-ASCT and suppress anti-myeloma immune responses; Basiliximab-based Treg depletion strategy demonstrated in MM patients undergoing ASCT |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Prospective Observational Study | Bone Marrow Transplantation | Basiliximab well tolerated and effective for steroid-refractory acute GvHD after allogeneic SCT in 17 patients (including MM cases) — supports long-term IL-2R blockade safety in HSCT |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case Report | American Journal of Kidney Diseases | Kidney transplantation in 4 MM patients with renal failure using Basiliximab induction — demonstrates transplant management feasibility in MM survivors with improved long-term outcomes |

---

## EU Market Information

No EMA marketing authorizations are on record for Basiliximab in this dataset (market status: not marketed, 0 authorizations).

> **Note:** Basiliximab (Simulect®) is known to hold regulatory approvals in multiple jurisdictions worldwide. This absence is likely a **data gap** in the current dataset rather than a true lack of authorization. Please verify current authorization status directly via the [EMA product database](https://www.ema.europa.eu/en/medicines).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 1 trial (NCT01526096, n=30) directly tested Basiliximab-mediated Treg depletion in MM patients undergoing ASCT, with published results (PMID 31940591) confirming biological plausibility and initial safety; a completed Phase 2 trial further established the drug's tolerability in HSCT-related settings. The mechanistic hypothesis is coherent, the evidence reaches L2, and the clinical context (ASCT in MM) is directly aligned.

**To proceed, the following is needed:**
- Retrieve full mechanism of action data from DrugBank to complete the mechanistic link analysis (currently a High-severity data gap)
- Obtain SmPC safety warnings and contraindications from the formal prescribing label — currently a **Blocking** data gap that prevents formal safety screening
- Review the full efficacy outcome data from NCT01526096 (PMID 31940591 is available; confirm Treg depletion depth, relapse rates, and immune reconstitution data)
- Design a Phase 2 proof-of-concept trial specifically measuring anti-myeloma efficacy endpoints (PFS, MRD negativity) following Treg depletion — current evidence focuses on safety and immune feasibility, not tumor response
- Define patient selection criteria: ASCT-eligible MM patients, baseline Treg quantification, and post-depletion immune monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

