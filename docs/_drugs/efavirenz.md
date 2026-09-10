---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally developed and approved for **HIV-1 infection**. The TxGNN model's top-ranked prediction suggests possible relevance to **feline acquired immunodeficiency syndrome** (an FIV-related veterinary condition), but this direction is currently supported by only **1 in vitro literature study** and **2 clinical trials that are not actually about efavirenz** — evidence is weak and largely non-human.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NNRTI antiretroviral) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.80% (rank 2667/full candidate list) |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for efavirenz is not available in this evidence pack [Data Gap]. Based on known information, efavirenz belongs to the NNRTI class of antiretrovirals, and its efficacy against HIV-1 infection via direct inhibition of HIV-1 reverse transcriptase is well established.

The mechanistic rationale for extending this to feline acquired immunodeficiency syndrome rests on the fact that feline immunodeficiency virus (FIV) reverse transcriptase shares partial structural homology with HIV-1 RT. An in vitro biochemical/structural comparison study found that NNRTIs (nevirapine, efavirenz, rilpivirine) show potential inhibitory activity against FIV RT.

However, this is fundamentally a **veterinary indication** (a disease of cats), not a human indication expansion, and falls outside the typical scope of human drug repurposing evaluation. The two cited clinical trials are for an unrelated drug (dolutegravir, GSK1349572) in human HIV-1 patients and were graded "C" (low relevance) by the evidence review — they provide no support for the FIV indication. No efavirenz-specific in vivo or clinical data in cats exists in the current evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Compared dolutegravir + abacavir/lamivudine vs. Atripla (efavirenz/emtricitabine/tenofovir) in HIV-1 ART-naïve adults. **Relevance: Grade C** — studies dolutegravir, not efavirenz specifically for FIV; low relevance to the feline indication. |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Phase IIb dose-selection study of dolutegravir in HIV-1 ART-naïve adults. **Relevance: Grade C** — dolutegravir dose-finding trial, unrelated to the feline indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro structural study (Tier 3) | Journal of Veterinary Science | Biochemical/structural comparison of NNRTIs (nevirapine, efavirenz, rilpivirine) against feline and human immunodeficiency virus reverse transcriptase; investigates NNRTI potential for treating FIV-infected cats, which currently has no effective treatment. |

---

## Taiwan Market Information

Efavirenz currently holds **0 marketing authorizations** on record for this jurisdiction (market status: **未上市 / Not Marketed**). No license or approved-indication data is available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this evidence pack — notably, TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001) that prevents safety pre-screening (S1) for this drug.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level L4 rests on a single in vitro structural study; no efavirenz-specific in vivo or clinical data exists for the feline indication.
- The two cited clinical trials concern a different drug (dolutegravir) in human patients and were independently graded low relevance (Grade C).
- The predicted indication is a veterinary disease (cats), which is outside standard human drug repurposing scope and cannot proceed through this evaluation pathway as framed.

**To proceed, the following is needed:**
- Efavirenz mechanism of action (MOA) documentation (DG002, High severity)
- TFDA label warnings/contraindications (DG001, **Blocking** — required before any safety pre-screening can begin)
- If pursuing the veterinary track: efavirenz-specific in vivo/clinical data in FIV-infected cats
- **Note:** two other predicted indications in this candidate set — *AIDS related complex* (rank 5) and *congenital human immunodeficiency virus* (rank 6) — carry substantially stronger evidence (L1, multiple Phase 3 RCTs, "Proceed with Guardrails") and are human-relevant extensions of efavirenz's approved HIV-1 indication. These warrant separate, prioritized evaluation over the rank-1 candidate reviewed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

