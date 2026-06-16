---
layout: default
title: Cetrorelix
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Cetrorelix
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

# Cetrorelix: From Controlled Ovarian Stimulation to Hypertrichosis

## One-Sentence Summary

Cetrorelix (Cetrotide) is a synthetic GnRH antagonist used clinically in assisted reproductive technology (ART) to prevent premature LH surges during controlled ovarian stimulation.
The TxGNN model predicts it may be effective for **Hypertrichosis**,
however **no clinical trials** and **no publications** currently support this direction — the prediction rests solely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Controlled ovarian stimulation (ART/IVF — GnRH antagonist protocol) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Cetrorelix is a synthetic decapeptide that competitively and reversibly blocks GnRH receptors in the pituitary gland, suppressing the release of LH and FSH, and consequently reducing gonadal production of androgens and estrogens. This mechanism underlies its approved use in IVF protocols (marketed as Cetrotide in the EU).

The predicted link to hypertrichosis likely originates from a mechanistic extrapolation: reduced androgens → reduced androgenic hair follicle stimulation. This logic applies to **hirsutism** (androgen-dependent excessive hair growth), where GnRH analogues are sometimes used off-label. However, **hypertrichosis** is clinically distinct — it is defined as excessive hair growth that is *not* androgen-driven. Causes include genetic mutations, medications (e.g., cyclosporine, minoxidil), or paraneoplastic syndromes. There is no known receptor pathway connecting GnRH antagonism to non-androgenic follicle hyper-activation.

The TxGNN model may be conflating hypertrichosis with hirsutism, or detecting a spurious graph proximity between these entities in the knowledge graph. Without any supporting clinical trials or literature, and given the weak mechanistic rationale, this prediction is classified as **L5** and the recommended action is **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No authorizations on file. Cetrorelix is not currently registered in Taiwan.

> **Note:** Cetrorelix is known to be approved and marketed in the EU as **Cetrotide** (for controlled ovarian stimulation). EU authorization data was not captured in this Evidence Pack and should be retrieved separately from the EMA product database.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.98%), hypertrichosis is a non-androgenic condition for which GnRH antagonism has no established mechanistic basis; the score likely reflects a knowledge graph artefact or conflation with hirsutism rather than a genuine repurposing signal. Zero supporting evidence (no trials, no literature) confirms an L5 classification.

**To proceed, the following is needed:**
- Mechanistic clarification: confirm whether TxGNN graph proximity reflects a true biological path or a hirsutism/hypertrichosis ontology overlap
- Retrieve Cetrotide SmPC from EMA to populate safety warnings and contraindications (currently all [Data Gap])
- Retrieve Taiwan TFDA registration data to complete regulatory profile
- If the hirsutism hypothesis is the actual target, redirect the query to search Cetrorelix evidence under **hirsutism** and **androgen excess** conditions instead
- Consider prioritizing **Rank 9 (Aromatase Excess Syndrome, L4, "Research Question")** as a more mechanistically coherent repurposing candidate for near-term follow-up
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

