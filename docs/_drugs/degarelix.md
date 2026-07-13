---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Advanced Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix (Firmagon) is a GnRH receptor antagonist clinically used for advanced hormone-sensitive prostate cancer, acting by competitively blocking pituitary GnRH receptors to suppress testosterone production.
The TxGNN model's top prediction is **Hypertrichosis**, with a score of 99.99% — however, this prediction carries a **known mechanism mismatch**: hypertrichosis is defined as non-androgen-dependent excessive hair growth, distinct from androgen-driven hirsutism.
**No clinical trials and no relevant literature** currently exist for this pairing; the prediction is rated **L5** (model prediction only).

> ⚠️ **Editorial Note**: Among the 10 ranked predictions, **Central Precocious Puberty 1 (Rank 9)** is the only indication with genuine biological plausibility (GnRH-dependent pathophysiology directly targeted by Degarelix's mechanism). The rank 1 prediction is reported here per protocol; see the Conclusion section for the actionable finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced prostate cancer (not registered in Taiwan; sourced from general medical knowledge — Taiwan regulatory data unavailable) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (MOA field: Data Gap). Based on widely published pharmacology, Degarelix is a synthetic decapeptide GnRH receptor antagonist that competitively and reversibly blocks GnRH receptors in the anterior pituitary. This suppresses LH and FSH secretion, leading to a rapid and sustained reduction in serum testosterone — without the initial androgen surge ("flare effect") seen with GnRH agonists. Its approved use is advanced hormone-sensitive prostate cancer, where testosterone suppression is the therapeutic goal.

The TxGNN model's connection to hypertrichosis likely reflects the known role of androgens in regulating androgen-sensitive hair follicles. In theory, androgen suppression could reduce hair growth in conditions driven by excessive androgens (i.e., **hirsutism**). However, **hypertrichosis is defined as excessive hair growth that is independent of androgen stimulation** — it is a distinct clinical entity from hirsutism, driven by genetic factors, medications (e.g., minoxidil, phenytoin), or metabolic conditions. Degarelix's androgen-lowering mechanism has no established pathway in non-androgen-dependent hypertrichosis.

The most probable explanation is that the TxGNN knowledge graph conflates hypertrichosis and hirsutism due to shared terminology in disease ontologies. The mechanism-indication pairing is biologically mismatched, and this prediction should not be pursued clinically. Critically, **Rank 9 (Central Precocious Puberty 1)** represents the one indication in this list where Degarelix's GnRH-antagonist mechanism directly and specifically addresses the disease pathophysiology, and is the candidate warranting further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Degarelix in hypertrichosis.

---

## Literature Evidence

Currently no related literature available for Degarelix in hypertrichosis.

---

## Taiwan Market Information

Degarelix is not registered in Taiwan (0 licenses, market status: 未上市). No authorization data is available for display.

> For reference: Degarelix is marketed internationally as **Firmagon** (Ferring Pharmaceuticals) and has received approval in multiple jurisdictions including the EU and the United States for advanced prostate cancer. Taiwan regulatory data was not captured in this Evidence Pack.

---

## Cytotoxicity

Degarelix is an antineoplastic agent (GnRH receptor antagonist) used for prostate cancer. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal therapy / Endocrine therapy (GnRH receptor antagonist — not conventional cytotoxic) |
| Myelosuppression Risk | Low (hormonal therapy; not myelosuppressive by mechanism) |
| Emetogenicity Classification | Minimal to low |
| Monitoring Items | Serum testosterone, PSA, liver function tests, QTc interval (QT prolongation risk), bone mineral density with long-term use |
| Handling Protection | Standard pharmaceutical handling; no cytotoxic precautions required (not an alkylating agent or antimetabolite) |

---

## Safety Considerations

Safety data (warnings, contraindications, drug interactions) was not available in this Evidence Pack. Please refer to the Firmagon SmPC for complete safety information.

---

## Conclusion and Next Steps

### For Rank 1 — Hypertrichosis

**Decision: Hold**

**Rationale:**
The mechanism-indication pairing is biologically mismatched: Degarelix suppresses androgens, but hypertrichosis is by definition non-androgen-dependent. No clinical trials or literature support this pairing. This prediction is very likely an artefact of the TxGNN knowledge graph conflating hypertrichosis with hirsutism.

**Actions:**
- Do not proceed with hypertrichosis as a repurposing candidate.
- Flag this disease pair as a known false positive for model calibration review.

---

### ⭐ Actionable Candidate — Rank 9: Central Precocious Puberty 1 (CPP1)

**Decision: Research Question (Escalate to S1)**

**Rationale:**
Central precocious puberty (CPP) is a GnRH-**dependent** condition: premature activation of the hypothalamic-pituitary-gonadal (HPG) axis drives early puberty. Degarelix's mechanism — direct, competitive GnRH receptor blockade at the pituitary — is precisely targeted at the upstream driver of CPP. Unlike the GnRH agonist standard of care (leuprolide, triptorelin), GnRH antagonists like Degarelix avoid the initial testosterone/estrogen flare seen at treatment initiation, potentially offering a faster onset of hormonal suppression. Related GnRH antagonists (cetrorelix, relugolix, linzagolix) have precedent in GnRH-axis indications beyond prostate cancer.

**To proceed, the following is needed:**
- Systematic literature search specifically for "Degarelix AND precocious puberty" and "GnRH antagonist AND central precocious puberty" to characterize the existing evidence base (the current Evidence Pack returned 0 results, but the search query used only the exact indication name)
- Safety profile review (obtain SmPC/TFDA label data — currently Blocking data gap DG001)
- MOA documentation from DrugBank API (currently High severity data gap DG002)
- Pediatric dosing and formulation assessment: Degarelix is currently available as a subcutaneous injection for adults; pediatric pharmacokinetics and acceptable injection frequency for children must be evaluated
- Comparison with approved CPP treatments (leuprolide SC/IM, triptorelin) on efficacy endpoints and tolerability in pediatric populations
- QTc prolongation risk assessment in pediatric patients (known adult concern)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

