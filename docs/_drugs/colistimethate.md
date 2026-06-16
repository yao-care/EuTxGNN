---
layout: default
title: Colistimethate
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
---

# Colistimethate
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

# Colistimethate: From Multidrug-Resistant Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Colistimethate is a last-resort polymyxin antibiotic used to treat life-threatening infections caused by multidrug-resistant (MDR) Gram-negative bacteria such as *Pseudomonas aeruginosa* and *Acinetobacter baumannii*. The TxGNN model predicts it may be effective for **Osteoarthritis**, yet **0 clinical trials** and **0 publications** currently support this direction. At present, evidence is limited entirely to model prediction (Level L5), and a Hold recommendation applies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MDR Gram-negative bacterial infections (drug not registered in Taiwan) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 97.78% |
| Evidence Level | L5 (model prediction only, no clinical studies) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Colistimethate is a prodrug that is hydrolysed in vivo to Colistin, a polymyxin-class antibiotic. Colistin binds to the lipopolysaccharide (LPS) and phospholipids in the outer membrane of Gram-negative bacteria, displacing the divalent cations (Ca²⁺, Mg²⁺) that stabilise the membrane, ultimately causing osmotic disruption and bacterial cell death.

The theoretical bridge to osteoarthritis is highly indirect: by sequestering and neutralising circulating LPS, Colistimethate could theoretically attenuate TLR4/NF-κB signalling, reduce systemic levels of pro-inflammatory cytokines (TNF-α, IL-6, IL-1β), and secondarily lessen synovial inflammation in OA joints. However, osteoarthritis is primarily a disease of mechanical stress and cartilage-matrix degradation — not of LPS-driven infection or endotoxaemia — and no experiment has tested whether Colistimethate reaches or modulates joint tissue at clinically relevant concentrations.

In practical terms, this prediction is most likely a knowledge-graph artefact. TxGNN assigns scores based on graph topology, and shared nodes between "Gram-negative infection/LPS pathway" and "musculoskeletal inflammation" clusters can produce high scores without reflecting genuine pharmacological opportunity. Colistimethate has never been studied in any musculoskeletal context, and its significant dose-limiting nephrotoxicity makes chronic non-infectious use unacceptable without strong mechanistic justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

- **Nephrotoxicity**: The most clinically significant toxicity; dose-limiting and cumulative. Requires careful renal function monitoring (serum creatinine, eGFR), dose adjustment based on creatinine clearance, and avoidance in patients with pre-existing severe renal impairment. Any repurposing scenario involving chronic dosing would face a fundamentally unfavourable risk–benefit ratio given this toxicity.
- **Neurotoxicity**: Includes peripheral neuropathy, dizziness, paraesthesia, slurred speech, and — at high doses — neuromuscular blockade potentially leading to respiratory arrest.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic, preclinical, or clinical evidence linking Colistimethate to osteoarthritis or any musculoskeletal indication; the high TxGNN score reflects shared knowledge-graph topology rather than a pharmacologically actionable connection, and the drug's well-documented nephrotoxicity and neurotoxicity profile make any chronic non-infectious use extremely high-risk without exceptional justification.

**To proceed, the following is needed:**
- Mechanistic validation: in vitro evidence that Colistin or Colistimethate modulates OA-relevant pathways (e.g., chondrocyte apoptosis, synoviocyte TLR4 signalling, MMP expression)
- Preclinical OA model data (e.g., DMM or MIA mouse model)
- Formal MOA characterisation via DrugBank API retrieval (current gap: DG002)
- TFDA prescribing information and SmPC review to confirm contraindications and complete safety profile (current gap: DG001)
- Pharmacokinetic data demonstrating adequate joint-tissue penetration at non-nephrotoxic doses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

