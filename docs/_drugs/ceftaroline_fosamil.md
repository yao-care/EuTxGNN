---
layout: default
title: Ceftaroline Fosamil
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Ceftaroline Fosamil
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

# Ceftaroline Fosamil: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Ceftaroline fosamil is a 5th-generation cephalosporin β-lactam antibiotic (prodrug), originally approved internationally for community-acquired bacterial pneumonia and acute bacterial skin and skin structure infections (ABSSSI), including MRSA — but currently not marketed in Taiwan.
The TxGNN model predicts it may have potential for **Rheumatoid Arthritis** (highest-ranked prediction),
yet **0 clinical trials** and **0 publications** support this direction; mechanistic analysis strongly suggests the high prediction score is a knowledge graph structural artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Community-acquired bacterial pneumonia (CABP); acute bacterial skin and skin structure infections (ABSSSI), including MRSA — not available from Taiwan regulatory data |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Ceftaroline fosamil is a prodrug that is hydrolyzed in vivo to its active form, ceftaroline. It exerts bactericidal activity by binding to penicillin-binding proteins (PBPs) — including PBP2a, the key resistance determinant of MRSA — thereby inhibiting bacterial cell wall synthesis. This mechanism is entirely specific to prokaryotic biology and has no established immunomodulatory, anti-inflammatory, or disease-modifying relevance to autoimmune conditions.

Rheumatoid arthritis is a chronic, systemic autoimmune disease driven by dysregulated T-cell and B-cell responses, inflammatory cytokine cascades (TNF-α, IL-6, IL-17), and synovial hyperplasia. Unlike certain antibiotics with documented immunomodulatory properties (most notably minocycline, which has modest but real anti-inflammatory activity and has been studied in early RA), β-lactam antibiotics have no established off-target anti-inflammatory or immunomodulatory mechanism that could plausibly translate to RA disease modification.

The high TxGNN prediction scores across all 10 ranked indications (0.967–0.982) most likely reflect a **knowledge graph structural false positive**: ceftaroline has genuine clinical use in joint and bone infections (septic arthritis, osteomyelitis, prosthetic joint infections), and the KG nodes for these conditions are topologically adjacent to musculoskeletal disease nodes such as rheumatoid arthritis and osteoarthritis. The model has learned proximity without pharmacological causality. This pattern is further reinforced by the complete absence of any clinical trials or mechanistically relevant literature across all 10 predicted indications, and by the cluster of rare skeletal dysplasias (pseudoachondroplasia, brachyolmia, acromesomelic dysplasia, Hunter-Thompson type) appearing in ranks 5–9 — diseases caused by genetic mutations in cartilage/bone proteins, where antibiotic intervention has no plausible rationale whatsoever.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ceftaroline fosamil in Rheumatoid Arthritis.

---

## Literature Evidence

Currently no related literature available for Ceftaroline fosamil in Rheumatoid Arthritis.

> **Contextual Note — Osteoarthritis (Rank 2):** Two publications were retrieved under the "osteoarthritis" query, but neither constitutes repurposing evidence for degenerative joint disease. Both address ceftaroline's use in **bacterial joint and bone infections** occurring in orthopaedic patients — a recognized on-label infectious disease application, not OA disease modification. This is a terminology mismatch between "osteoarthritis" (degenerative) and "osteoarticular infection" (infectious), not evidence of an anti-arthritic effect.
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|-----|------|------|---------|
> | [27530754](https://pubmed.ncbi.nlm.nih.gov/27530754/) | 2016 | Matched Cohort | J Antimicrob Chemother | Ceftaroline vs vancomycin for long-term outpatient treatment of **osteoarticular infection**; describes effectiveness/safety in infectious, not degenerative, joint disease |
> | [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey/Expert Panel | Int J Antimicrob Agents | Expert survey on **prosthetic joint infection** antibiotic management; not related to OA disease modification |

---

## Taiwan Market Information

Ceftaroline fosamil is currently **not marketed in Taiwan**. No TFDA-authorized products exist, and no license data is available for this drug.

> For reference: Ceftaroline fosamil is approved internationally under the brand names **Teflaro** (United States, FDA) and **Zinforo** (European Union, EMA) for community-acquired bacterial pneumonia and acute bacterial skin and skin structure infections.

---

## Safety Considerations

Please refer to the SmPC for safety information. Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack. Taiwan TFDA prescribing information (仿單) has not yet been retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications lack pharmacological mechanistic support for repurposing an anti-bacterial β-lactam into non-infectious musculoskeletal or genetic disease categories. The uniformly high prediction scores (0.967–0.982) across biologically unrelated conditions — from autoimmune arthritis to rare skeletal dysplasias — are a strong signal of **knowledge graph topology bias** rather than genuine drug-disease pharmacology. No clinical trials and no mechanistically relevant literature exist for any of the 10 predicted indications.

**To proceed with any reassessment, the following would be needed:**

- Obtain Taiwan TFDA SmPC (仿單) to establish local safety profile, warnings, and contraindications
- Confirm full off-target pharmacological profile of ceftaroline (including any immunomodulatory effects, if documented in the primary literature)
- Determine whether any β-lactam antibiotic class member has established anti-inflammatory activity applicable to autoimmune diseases — if not, deprioritize this entire drug class for autoimmune repurposing
- Review KG subgraph structure around the ceftaroline node to identify and flag the "infection-adjacency" false positive pattern, which may affect other antibiotics in the dataset similarly
- Consider rerunning TxGNN predictions with infection-related disease nodes masked, to assess whether musculoskeletal predictions persist or disappear (a methodological validation step)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

