---
layout: default
title: High Evidence (L1-L2)
parent: Drug Reports
nav_order: 1
has_children: true
description: "L1-L2 level drug repurposing candidates with strong clinical evidence support."
permalink: /evidence-high/
---

# High Evidence Level Drugs

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L1 | plus: site.data.drug_stats.level_counts.L2 %}
This page lists **{{ pd_m }}** of the **{{ site.data.drug_stats.total_drugs }}** medicines with a published report on this site ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%). Level definitions: [Methodology]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

Candidates with strong clinical trial evidence for priority evaluation

Which of these drugs have trial evidence for their predicted new indication, and how many registered trials are cited? See [EU medicines with clinical-trial evidence for a new indication]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L1** | Multiple Phase 3 RCTs / Systematic Reviews | Strong support, consider clinical use |
| **L2** | Single RCT or multiple Phase 2 trials | Moderate support, design validation trial |

---

## Drug List

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 Level ({{ l1_drugs.size }} drugs)

| Drug Name | Indications | Link |
|-----------|-------------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 Level ({{ l2_drugs.size }} drugs)

| Drug Name | Indications | Link |
|-----------|-------------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

---

## Related Pages

- [Medium Evidence (L3-L4)](/evidence-medium/)
- [AI Predictions (L5)](/evidence-low/)
- [Full Drug List](/drugs/)
