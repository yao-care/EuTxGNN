---
layout: default
title: AI Predictions (L5)
parent: Drug Reports
nav_order: 3
has_children: true
description: "374 medicines at evidence level L5 on this site (European Union), e.g. Denosumab, Metformin, Clopidogrel, with the main predicted new indication, local EMA central authorisations and review-log entries for each."
permalink: /evidence-low/
---

# AI Prediction Only Drugs

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
This page lists **{{ site.data.evidence_tier_facts.low.count }}** of the **{{ site.data.drug_stats.total_drugs }}** medicines with a published report on this site ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Median share at L5 across the 30 TxGNN sites: {{ site.data.evidence_tier_facts.low.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}This site is above the median.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}This site is below the median.{% else %}This site is at the median.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
In the local data (EMA central authorisations), **{{ site.data.evidence_tier_facts.low.with_current }}** of these medicines have at least one authorised entry, **{{ site.data.evidence_tier_facts.low.none_current }}** have entries but none authorised, and **{{ site.data.evidence_tier_facts.low.without_data }}** are not in the local data. **{{ site.data.evidence_tier_facts.low.with_reviews }}** have entries in the review log (corrections of registration facts on the drug page). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** have a predicted indication that no other TxGNN site lists for the same medicine.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

With entries but none authorised: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Medicines with a authorised local entry are listed first.
{% endif %}

Definitions of all levels: [Methodology]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L5 Level ({{ site.data.evidence_tier_facts.low.by_level.L5 }} drugs)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicine | Level | Main predicted new indication | EMA central authorisations: authorised / total | Review log | Only on this site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}yes ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

## Statistics

| Metric | Value |
|--------|-------|
| Total L5 Drugs | {{ site.data.evidence_tier_facts.low.by_level.L5 }} |
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
