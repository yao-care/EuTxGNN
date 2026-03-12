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

Candidates with strong clinical trial evidence for priority evaluation

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L1** | Multiple Phase 3 RCTs / Systematic Reviews | Strong support, consider clinical use |
| **L2** | Single RCT or multiple Phase 2 trials | Moderate support, design validation trial |

---

## Drug List

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

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
