---
layout: default
title: Nomegestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Nomegestrol Acetate
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

# Nomegestrol Acetate: From Progestin Therapy to Candidiasis (Low-Confidence Prediction)

## One-Sentence Summary

> Nomegestrol acetate is a synthetic progestin (19-nor-progesterone derivative) used in hormonal contraception and menopausal hormone therapy; no original indication record is available in this evidence pack. The TxGNN model assigns a high score to **Candidiasis** as a possible new indication, but **zero clinical trials and zero literature** support this link, and the underlying pharmacology actually points in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no license records in this jurisdiction |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 98.78% |
| Evidence Level | L5 (model prediction only, no corroborating studies) |
| EU Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, nomegestrol acetate is a selective progesterone receptor agonist with anti-gonadotropic and mild anti-androgenic activity, typically used as a component of combined hormonal contraceptives and in menopausal hormone therapy.

There is no known antifungal mechanism for nomegestrol acetate. More importantly, the direction of the known pharmacology runs *counter* to a therapeutic repurposing hypothesis: progestin and estrogen-progestin combinations are well documented to alter vaginal flora and are clinically associated with an **increased** risk of vulvovaginal candidiasis, not a treatment effect. The TxGNN score is numerically high, but the model's own generated rationale characterizes this as likely reflecting a comorbidity/co-occurrence signal in the knowledge graph (drug associated with a condition it can *cause or worsen*) rather than a genuine causal-therapeutic relationship.

No clinical trial or published literature was found supporting an antifungal or candidiasis-treating role for this drug. This prediction should be treated as a candidate for **model noise / false-positive filtering**, not as a repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

This drug currently has no marketing authorizations recorded in this jurisdiction (未上市 / Not marketed, 0 licenses).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: This evidence pack flags TFDA/regulatory label data — warnings and contraindications — as a **Blocking** data gap, meaning no formal safety review (S1) can currently be completed for this drug.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction has no clinical or literature support, and the drug's known pharmacology (progestin-driven vaginal flora alteration) suggests the association runs opposite to a therapeutic effect — this is a mechanistic red flag, not a repurposing signal. The drug is also not currently marketed in this jurisdiction, and core safety data (warnings/contraindications) are a **Blocking** gap, so no S1 safety screening can be performed even if the indication signal were credible.

It is also worth noting that several other top-ranked predictions for this drug in the same evidence pack (e.g., thrombophilia-related conditions, thrombotic disease) show the same pattern — high TxGNN scores driven by proximity to *adverse-effect* associations (VTE risk) rather than genuine treatment efficacy. This suggests the candidate list for this drug is currently dominated by safety-signal contamination rather than efficacy signals, and warrants cautious interpretation as a set.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action and original indication (DrugBank API query) — currently a High-severity gap (DG002)
- Any in vitro/in vivo evidence of antifungal or anti-*Candida* activity for nomegestrol acetate, if this lead is to be pursued further
- Explicit re-evaluation of whether "candidiasis" should be down-weighted or excluded as a known adverse-association artifact in the underlying knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

