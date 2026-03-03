---
layout: default
title: AI Predictions (L5)
parent: Drug Reports
nav_order: 3
description: "L5 level drug repurposing candidates with AI prediction only, no clinical evidence yet."
permalink: /evidence-low/
---

# AI Prediction Only Drugs

TxGNN model predictions without clinical evidence - research hypotheses for exploration

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L5** | AI prediction only, no clinical evidence | Research hypothesis, requires validation |

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Caution:</strong> L5 predictions are based on knowledge graph analysis only. They should NOT be used for clinical decision-making and require rigorous validation before any therapeutic application.
</div>

---

## Statistics

| Metric | Value |
|--------|-------|
| Total L5 Predictions | 32,368 |
| Unique Drugs | 638 |
| Unique Indications | 4,570 |

---

## Highest Confidence Predictions

These L5 predictions have the highest TxGNN scores:

| Drug | Indication | Score |
|------|------------|-------|
| TRAVOPROST | visceral calciphylaxis | 0.9999 |
| CAPLACIZUMAB | primary release disorder of platelets | 0.9999 |
| ROMIPLOSTIM | primary release disorder of platelets | 0.9999 |
| CAPLACIZUMAB | pseudo-von Willebrand disease | 0.9999 |
| AZATHIOPRINE | rheumatoid arthritis | 0.9999 |
| TRAVOPROST | arterial thoracic outlet syndrome | 0.9999 |
| CAPLACIZUMAB | Glanzmann thrombasthenia | 0.9999 |
| INFLIXIMAB | Crohn disease | 0.9999 |
| ADALIMUMAB | psoriatic arthritis | 0.9999 |
| USTEKINUMAB | inflammatory bowel disease | 0.9999 |

---

## Research Applications

L5 predictions can be useful for:

1. **Hypothesis Generation**: Starting points for research
2. **Literature Review**: Prioritize which associations to investigate
3. **Grant Writing**: Preliminary data for research proposals
4. **Drug Discovery**: Identify candidates for preclinical testing

---

## Validation Pathway

To upgrade from L5 to higher evidence levels:

```
L5 (AI Prediction)
    ↓ Literature search
L4 (Preclinical/Mechanistic)
    ↓ Observational studies
L3 (Cohort/Case-control)
    ↓ Phase 2 trials
L2 (Single RCT)
    ↓ Multiple Phase 3 trials
L1 (Strong Evidence)
```

---

## Download L5 Data

All L5 predictions available at:

- [CSV Download](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/repurposing_candidates.csv)
- [FHIR API](/fhir/metadata)

---

## Related Pages

- [High Evidence (L1-L2)](/evidence-high/)
- [Medium Evidence (L3-L4)](/evidence-medium/)
- [Full Drug List](/drugs/)
