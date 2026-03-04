---
layout: default
title: AI Predictions (L5)
parent: Drug Reports
nav_order: 3
has_children: true
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

## Drug List

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 Level ({{ l5_drugs.size }} drugs)

| Drug Name | Indications | Link |
|-----------|-------------|------|
{% for drug in l5_drugs limit:100 %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

{% if l5_drugs.size > 100 %}
*Showing first 100 of {{ l5_drugs.size }} drugs. See [Full Drug List](/drugs/) for all.*
{% endif %}

---

## Statistics

| Metric | Value |
|--------|-------|
| Total L5 Drugs | {{ l5_drugs.size }} |
| Total Predictions | 32,368 |
| Unique Indications | 4,570 |

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
