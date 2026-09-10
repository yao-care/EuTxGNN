---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Fentanyl
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

# Fentanyl: From Opioid Analgesic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic opioid used clinically as an analgesic and anesthetic adjunct. The TxGNN model's top-ranked prediction is that it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis**, but this candidate is currently supported by **0 clinical trials** and **0 publications** — the mechanistic rationale actually points in the opposite direction (opioids are more commonly associated with *causing* SIADH-like dysregulation than treating it).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no formal indication or license text was captured for this drug in the current evidence pack (drug is not marketed in the evaluated jurisdiction). Generically, fentanyl is known as an opioid analgesic. |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a High-severity data gap — DrugBank MOA lookup pending). Based on general pharmacological knowledge, fentanyl is a synthetic opioid and potent μ-opioid receptor agonist, primarily used for severe acute/chronic pain management and as an anesthesia adjunct.

For this specific prediction, the mechanistic story is weak and arguably runs counter to the proposed indication. The evidence pack's own rationale notes that opioids are known to be associated with dysregulated antidiuretic hormone (ADH) secretion as an **adverse effect**, not a therapeutic one — meaning the direction of the proposed mechanism is inconsistent with treating a syndrome of inappropriate antidiuresis. No clinical trials or literature were found linking fentanyl to this indication, so the prediction currently rests entirely on the TxGNN model's statistical association, without any corroborating mechanistic or empirical support.

Given this, the reasoning underlying the drug's original opioid-analgesic use does not translate meaningfully to this new indication, and the prediction should be treated as exploratory only.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

Fentanyl currently has no marketing authorizations recorded in this evidence pack (market status: Not Marketed, 0 total licenses). No product/indication table can be generated.

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are all currently unavailable/not found in this evidence pack, including a Blocking-severity gap for TFDA label warnings and contraindications.)*

## Alternative Candidates Worth Noting

The top-ranked prediction (by TxGNN score alone) has the weakest evidentiary support in this pack. Two lower-ranked candidates have materially stronger evidence and may be more productive lines of inquiry:

| Rank | Disease | Evidence Level | Decision Stage | Note |
|------|---------|-----------------|-----------------|------|
| 4 | Myofascial pain syndrome | L2 | S2 (Research Question) | Phase 3 RCT (NCT00343733, n=120) plus a review on long-term opioid use in TMJ dysfunction; reflects fentanyl's established analgesic role rather than disease-specific mechanism. |
| 10 | Tendinitis | L3 | S1 (Research Question) | Multiple RCTs support transdermal/postoperative fentanyl for tendon/rotator-cuff surgical pain, again as generalized analgesia rather than a tendinitis-specific mechanism. |

Both are extensions of fentanyl's known analgesic use rather than novel disease-modifying indications, but they are far better supported than the rank-1 candidate above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring TxGNN prediction (nephrogenic syndrome of inappropriate antidiuresis) has no clinical trial or literature support and a mechanistic direction that may actually contradict the proposed benefit. Separately, a Blocking-severity data gap (missing TFDA/regulatory label warnings and contraindications) prevents any safety evaluation from proceeding regardless of indication.

**To proceed, the following is needed:**
- Regulatory label data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action from DrugBank — currently High-severity gap (DG002)
- If pursuing repurposing at all, redirect focus to the better-evidenced candidates (myofascial pain syndrome, tendinitis) and verify that cited trials involve fentanyl itself rather than adjunct/comparator regional anesthesia techniques
- Original approved indication and license data, to properly assess similarity between old and new indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

