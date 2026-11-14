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

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
This page lists **{{ pd_m }}** of the **{{ site.data.drug_stats.total_drugs }}** medicines with a published report on this site ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%). Level definitions: [Methodology]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

TxGNN model predictions without clinical evidence - research hypotheses for exploration

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L5** | AI prediction only, no clinical evidence | Research hypothesis, requires validation |

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Caution:</strong> L5 predictions are model predictions only, with no clinical evidence. They should NOT be used for clinical decision-making and require rigorous validation before any therapeutic application.
</div>

---

## Drug List

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 Level ({{ l5_drugs.size }} drugs)

| Drug Name | Indications | Link |
|-----------|-------------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

---

## Statistics

| Metric | Value |
|--------|-------|
| Total L5 Drugs | {{ l5_drugs.size }} |
| Total Predictions | {{ site.data.drug_stats.total_indications }} |
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
