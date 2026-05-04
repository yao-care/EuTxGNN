---
layout: default
title: Interferon Beta-1A
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Interferon Beta-1A
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

# Interferon beta-1a: From Multiple Sclerosis to Jeune Syndrome Situs Inversus

## One-Sentence Summary

Interferon beta-1a is a recombinant cytokine widely established as a disease-modifying therapy for relapsing-remitting multiple sclerosis (RRMS), exerting its effects through immunomodulation to reduce relapse frequency and slow disease progression.
The TxGNN model predicts it may be effective for **Jeune Syndrome Situs Inversus** (rank 1, score 97.47%),
however **no clinical trials** and **no publications** currently support this specific indication — this is a pure AI model prediction at Evidence Level **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple sclerosis (relapsing-remitting); original indications not recorded in this Evidence Pack |
| Predicted New Indication | Jeune Syndrome Situs Inversus |
| TxGNN Prediction Score | 97.47% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Interferon beta-1a is a recombinant form of the endogenous cytokine IFN-β, primarily approved for relapsing-remitting multiple sclerosis. Its known biological actions include suppression of pro-inflammatory T-cell activity, reduction of cytokine-driven inflammation, inhibition of leukocyte trafficking across the blood–brain barrier, and upregulation of anti-inflammatory mediators — all targeting immune-mediated neuroinflammation.

Jeune Syndrome Situs Inversus (asphyxiating thoracic dystrophy with situs inversus) is a rare autosomal-recessive ciliopathy caused by loss-of-function mutations in genes encoding intraflagellar transport (IFT) complex components, most commonly *DYNC2H1*. The disease mechanism involves structural defects of primary cilia, leading to skeletal dysplasia, narrow thorax, and organ laterality reversal. This is a fundamentally developmental and structural disorder with no known immune-mediated component.

There is no established pharmacological pathway by which IFN-β-1a could repair ciliary architecture, rescue IFT gene function, or correct organ situs. The high TxGNN prediction score (97.47%) most likely reflects over-representation of rare-disease nodes within the knowledge graph — rare diseases tend to have high inter-connectivity — rather than a genuine drug–disease pharmacological relationship. This prediction should be regarded as a knowledge-graph artifact, not a credible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Interferon beta-1a is currently not marketed in Taiwan. No marketing authorizations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No authorizations found |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Jeune Syndrome Situs Inversus is a genetic ciliopathy driven by IFT complex dysfunction, with no immunological disease mechanism; IFN-β-1a has no plausible pathway to address ciliary structural defects, IFT gene mutations, or organ laterality reversal. All 10 top-ranked TxGNN predictions for this drug involve either structural chromosomal anomalies, developmental syndromes, or congenital malformations — none of which are mechanistically linked to IFN-β immunomodulation — suggesting a systematic model artefact rather than actionable repurposing signals.

**To proceed, the following is needed:**
- Basic science evidence (in vitro or animal models) demonstrating any effect of IFN-β signalling on IFT complex function or ciliogenesis
- Identification of any proposed biological mechanism linking type I interferon pathways to ciliopathy rescue
- Expert curation to determine whether any lower-ranked TxGNN predictions for Interferon beta-1a carry stronger mechanistic and clinical rationale
- TFDA prescribing information (SmPC) to complete the safety profile before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

