---
layout: default
title: Fidaxomicin
parent: AI Predictions (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

# Fidaxomicin: Original Indication Not Available — Predicted New Indication: Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is not currently marketed in the region covered by this evidence pack (0 authorizations, market status "Not marketed"), and its original indication/MOA data are not available in this dataset. The TxGNN model's top prediction is **Staphylococcal Scalded Skin Syndrome**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and the model's own rationale flags the mechanistic link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — evidence pack has no license/indication data for this region (drug not marketed) |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Fidaxomicin is not available in this evidence pack (flagged as data gap DG002, High severity). Based on general pharmacology, Fidaxomicin is a narrow-spectrum macrolide antibiotic that inhibits bacterial RNA polymerase and is essentially not absorbed systemically after oral dosing — its activity is confined to the gut lumen, which is why it is used for luminal *Clostridioides difficile* infection.

For the top-ranked prediction, the evidence pack's own rationale explicitly weighs against mechanistic plausibility: Staphylococcal Scalded Skin Syndrome is driven by an exfoliative toxin from *S. aureus* rather than by an eradicable infection burden, and it requires a drug that reaches the skin or neutralizes circulating toxin. Since Fidaxomicin is not systemically absorbed, it cannot reach the skin lesions or the toxin. The rationale text states this connection is "mechanistically weak, reflecting only a high TxGNN score with no clinical or literature support."

Among the 10 candidates in this evidence pack, only rank 8 (*Staphylococcus aureus pneumonia*, L4) has any literature backing (one 2019 review), though the same systemic-absorption limitation applies there too. All 10 candidates carry a "Hold" recommendation, and 9 of 10 have no clinical or literature evidence whatsoever (L5). This is a case where the model's high similarity score is not corroborated by mechanism or external evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Fidaxomicin has no marketing authorization in the region covered by this evidence pack (market status: Not marketed; 0 authorizations on record).

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps in this evidence pack — including a **Blocking**-severity gap, DG001, for TFDA label warnings/contraindications, which prevents any S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has zero clinical or literature evidence (L5), and the model's own mechanistic rationale argues against plausibility given Fidaxomicin's lack of systemic absorption. The drug is also not currently marketed in this region, and a Blocking-severity data gap (missing label warnings/contraindications) prevents even an initial safety assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label/SmPC warnings and contraindications before any S1 safety evaluation can proceed
- Resolve DG002 (High): confirm mechanism of action via DrugBank or equivalent source
- Original indication and regulatory history for Fidaxomicin (not present in this evidence pack)
- If pursuing repurposing, consider re-evaluating rank 8 (*S. aureus* pneumonia, L4) instead, as it is the only candidate with any literature support — though systemic bioavailability remains a fundamental barrier for all candidates in this list
- Independent confirmation of mechanistic plausibility before allocating further review resources to this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

