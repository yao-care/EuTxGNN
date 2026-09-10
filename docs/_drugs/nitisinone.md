---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

> Nitisinone (NTBC) is used to treat Hereditary Tyrosinemia Type 1 (HT1) by blocking upstream tyrosine catabolism.
> The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**,
> with **0 clinical trials** and **2 publications** currently supporting this direction — evidence is preliminary and indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Tyrosinemia Type 1 (HT1) *(inferred from mechanistic rationale; not present in structured regulatory fields)* |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism of action data is not available in the DrugBank record for this drug. Based on the available literature and repurposing rationale, Nitisinone (NTBC) inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD), an enzyme early in the tyrosine catabolic pathway. This blockade prevents the accumulation of downstream toxic metabolites (notably succinylacetone) that drive liver and kidney damage in Hereditary Tyrosinemia Type 1 (HT1), the drug's established indication.

HT1 patients frequently develop secondary proximal renal tubular dysfunction — a Fanconi-syndrome-like presentation that is a form of secondary renal tubular acidosis (RTA) — as a direct consequence of succinylacetone toxicity. Published cohort data (Maiorana et al., 2014) show that NTBC therapy improves renal tubular function in HT1 patients, which is the biological basis for this TxGNN prediction.

Importantly, this is an **indirect** mechanism: Nitisinone does not appear to act directly on renal tubular acid-handling transporters or acid-base physiology. Its apparent benefit for RTA is a downstream consequence of removing the upstream metabolic toxin in HT1. This means the prediction is most plausible for **HT1-associated secondary RTA**, not for primary or idiopathic RTA of other etiologies (e.g., autoimmune, genetic transporter defects unrelated to tyrosine metabolism).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Cohort | Molecular Genetics and Metabolism | Early NTBC therapy in HT1 patients was associated with improvement in renal tubular dysfunction, describing the early effect of NTBC on renal tubular disease. |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Case Series | Indian Journal of Gastroenterology | Case series of 4 children with tyrosinemia treated with NTBC; patients maintained on long-term therapy showed normal liver function and no renal tubular complications. |

---

## EU Market Information

This drug currently has no EU marketing authorization on record (market status: **Not marketed**, 0 authorizations found in this evidence pack).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: Structured safety data (key warnings, contraindications, drug interactions) were not available in this evidence pack. Retrieval of the official product label is flagged as a **blocking** data gap for any further safety evaluation (see Conclusion).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this indication is limited to two observational/case-series publications (L3) describing an indirect mechanism specific to HT1-associated secondary renal tubular dysfunction, with no clinical trials directly testing Nitisinone for primary RTA. Combined with the absence of critical safety labeling data (blocking gap) and no current EU marketing authorization, the evidence does not yet support proceeding beyond a research question.

**To proceed, the following is needed:**
- TFDA/EMA-approved product label (warnings, contraindications, DDI) — currently a blocking gap (DG001)
- Formal DrugBank mechanism-of-action data (DG002)
- Clarification of scope: does the target population mean HT1-associated secondary RTA specifically, or RTA broadly? This materially changes the evidence bar
- Any clinical or case-report data on Nitisinone use in RTA outside the HT1 context, if the broader indication is intended
- Confirmation of EU/Taiwan regulatory and marketing status for this drug before any repurposing pathway is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

