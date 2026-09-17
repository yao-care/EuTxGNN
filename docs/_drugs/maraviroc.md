---
layout: default
title: Maraviroc
parent: AI Predictions (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Maraviroc
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Maraviroc is a CCR5 antagonist originally used to treat HIV-1 infection (CCR5-tropic strains) by blocking viral entry into immune cells.
> The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**, with a prediction score of **99.82%**,
> but **no clinical trials and no supporting literature** currently exist for this indication — the drug's own repurposing rationale explicitly notes there is no known biological connection.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (CCR5-tropic strains) — inferred from known drug class; not present in this evidence pack's license data |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on background information referenced in the repurposing rationale, Maraviroc is a **CCR5 antagonist**, acting on HIV-1 co-receptor binding to block viral entry and on chemokine-mediated immune cell trafficking. Its efficacy in HIV-1 infection is well established in this drug class.

Multiple endocrine neoplasia (MEN), however, is driven by germline mutations in the **RET** or **MEN1** genes, causing tumor development across endocrine glands. There is no known mechanistic overlap between CCR5 signaling and RET/MEN1-driven tumorigenesis.

The evidence pack's own rationale is explicit on this point: *"與多發性內分泌腫瘤(MEN)之腫瘤發生機轉（RET/MEN1基因突變）無已知生物學連結，純屬TxGNN高分預測，無機轉支持"* — i.e., this is a high-scoring statistical prediction from the TxGNN model with **no mechanistic or biological support**. It should be treated as a research hypothesis at most, not a plausible repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations currently registered — this drug is **not marketed** in this jurisdiction (`market_status: Not marketed`, `total_licenses: 0`).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-level prediction — a TxGNN score with zero supporting clinical trials or literature. The rationale text itself confirms there is no known biological link between Maraviroc's CCR5-antagonist mechanism and MEN pathogenesis, so there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/regulatory label (warnings, contraindications) — currently a **blocking** data gap (DG001)
- Full mechanism of action (MOA) data via DrugBank — currently a **high-severity** data gap (DG002)
- Preclinical or mechanistic studies directly linking CCR5 antagonism to RET/MEN1-driven tumorigenesis
- If no such mechanistic link can be established, this candidate should be deprioritized in favor of other predicted indications in this drug's portfolio (e.g., HER2-positive breast carcinoma, rank 10, which has direct CCL5/CCR5-ERK pathway evidence and may warrant separate evaluation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

