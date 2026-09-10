---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: From Familial Hypercholesterolemia to Aortic Malformation

## One-Sentence Summary

Inclisiran is a PCSK9-targeting siRNA therapeutic used for LDL-cholesterol lowering, most extensively studied in familial hypercholesterolemia (FH). Among 10 TxGNN-predicted new indications reviewed for this candidate, only **Aortic Malformation** advanced beyond a pure AI prediction, supported by **2 ongoing Phase 3 clinical trials**; the other 9 candidates (including "potassium deficiency disease," which scored highest on the model) have **no clinical trial or literature support at all** and several are flagged as likely keyword/disease-label mismatches.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Familial Hypercholesterolemia (inferred from associated trial context; no TFDA-approved label text available) |
| Predicted New Indication | Aortic Malformation |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Inclisiran is not available in this evidence pack (DrugBank MOA field is a data gap). Based on information embedded in the associated trial and rationale records, Inclisiran is a small interfering RNA (siRNA) that silences hepatic PCSK9 expression, reducing LDL-receptor degradation and thereby lowering circulating LDL-cholesterol. Its established use is in familial hypercholesterolemia and related dyslipidemias.

The predicted new indication, "aortic malformation," is mechanistically plausible only in a loose sense: sustained LDL-C reduction could theoretically slow atherosclerotic vascular disease, but the term "malformation" typically denotes a structural congenital anomaly rather than an acquired atherosclerotic process — a mismatch the model itself does not resolve.

Critically, the two supporting trials (NCT06597019, NCT06597006) are titled around **heterozygous and homozygous familial hypercholesterolemia in children**, not aortic malformation. Both were graded "B" relevance specifically because the disease label attached to them needs manual confirmation — it is plausible the trials were indexed under an aortic-valve/vascular complication of FH rather than a true congenital malformation. This should be resolved before any downstream decision relies on this evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recruiting | 51 | Double-blind Inclisiran vs. placebo (Year 1) followed by open-label Inclisiran (Year 2) in children 6–<12 years with heterozygous familial hypercholesterolemia and elevated LDL-C; evaluates safety, tolerability, and efficacy |
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recruiting | 9 | Companion study in children 2–<12 years with homozygous familial hypercholesterolemia and elevated LDL-C; same double-blind/open-label design |

Both trials are ongoing (estimated completion 2029-04-15) and were not designed with "aortic malformation" as a stated primary indication — this label needs verification against the source registry entry.

---

## Literature Evidence

Currently no related literature available for the "Aortic Malformation" indication.

*(Note: a separate candidate indication in this evidence pack, "migraine with or without aura, susceptibility to," returned 20 PubMed hits, but on review these are epilepsy-genetics and neuroinflammation papers unrelated to Inclisiran or PCSK9 biology — a keyword mismatch, not supporting evidence, and therefore not reported as a viable repurposing lead.)*

---

## Taiwan Market Information

Inclisiran currently has no marketing authorization on record in Taiwan (market status: 未上市; 0 licenses). No dosage form or approved indication text is available for this drug in the current dataset.

---

## Safety Considerations

Please refer to the SmPC for safety information. No verified key warnings, contraindications, or drug-drug interaction data are currently available for Inclisiran in this evidence pack (TFDA label data collection is flagged as a blocking data gap).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Of 10 TxGNN-predicted indications for Inclisiran, "Aortic Malformation" is the only one with any real-world clinical evidence (2 Phase 3 trials, L2), while all others remain pure model predictions (L5) with explicitly stated absence of mechanistic or evidentiary support. However, the supporting trials appear to target pediatric familial hypercholesterolemia rather than aortic malformation itself, so the evidence cannot yet be taken at face value.

**To proceed, the following is needed:**
- TFDA label/warning and contraindication data (currently blocking — DG001)
- DrugBank mechanism-of-action confirmation (DG002)
- Manual verification of the actual disease/endpoint definitions in NCT06597019 and NCT06597006 against the "aortic malformation" label
- Wait for interim or completed results from both trials (currently recruiting, estimated completion 2029)
- Drug-drug interaction and safety monitoring data before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

