---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Mometasone
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

# Mometasone: From Topical Corticosteroid Use to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Mometasone is clinically known as a topical/intranasal corticosteroid, though no approved indication record is available in this dataset.
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma (CTCL)**,
with **no clinical trials** and only **2 case-report-level publications** currently supporting this direction — neither of which directly studies mometasone in CTCL.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this dataset. Mometasone is generically known as a mid-potency topical/inhaled corticosteroid (e.g., dermatitis, allergic rhinitis, asthma); no drug-specific indication text or MOA was retrievable. |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mometasone is not available (Data Gap). Based on known information, mometasone belongs to the topical corticosteroid class; its anti-inflammatory efficacy in common dermatologic and allergic conditions is well established, but the drug-specific MOA record needed to formally assess mechanistic relevance to CTCL is missing.

The rationale linking mometasone to primary cutaneous T-cell lymphoma is class-based rather than drug-specific: topical corticosteroids such as clobetasol and triamcinolone are guideline-recommended first-line treatments for early-stage mycosis fungoides (the most common CTCL subtype), acting through anti-inflammatory effects and induction of apoptosis in malignant T cells. Since mometasone is a mid-potency member of the same drug class, mechanistic extrapolation is plausible in principle.

However, this remains an indirect, class-level inference rather than evidence specific to mometasone. One of the two retrieved publications actually reports mometasone **failing** to control a related lymphoproliferative skin condition (cutaneous pseudolymphoma) before the patient was switched to tapinarof, and the other publication does not mention mometasone at all. This weakens rather than strengthens the direct evidentiary basis for this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proceedings (Baylor University Medical Center) | Refractory cutaneous pseudolymphoma (T-cell lymphoproliferative, CTCL-mimicking) case that **failed** treatment with mometasone and tacrolimus before responding to tapinarof. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | Journal of Cutaneous Pathology | Describes a pediatric CD8+CD56+ mycosis fungoides (CTCL subtype) case; illustrative of disease presentation but does not evaluate mometasone treatment. |

---

## EU Market Information

No marketing authorizations on file — this drug is currently not marketed according to the available regulatory data.

---

## Safety Considerations

Please refer to the SmPC for safety information. Note: TFDA label warnings/contraindications for this drug could not be retrieved (blocking data gap, DG001) and safety evaluation (Stage S1) cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4, supported only by two case reports that are either unrelated to mometasone treatment or report treatment failure, with no clinical trials specific to mometasone in CTCL. Combined with a blocking data gap on TFDA safety labeling and the drug currently being unmarketed, there is insufficient evidence and safety data to advance this candidate.

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — currently a blocking data gap (DG001)
- Drug-specific mechanism of action data for mometasone (DG002)
- Literature or trial evidence directly evaluating mometasone (not just the corticosteroid class) in CTCL/mycosis fungoides
- Clarification of regulatory/market pathway given current "not marketed" status

*Note: Nine additional predicted indications (rank 2–10, e.g., Crohn's colitis, myelodysplastic syndrome subtypes) were also generated but carry L5 evidence (model prediction only, no supporting literature or trials) and are recommended for Hold without further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

