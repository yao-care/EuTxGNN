---
layout: default
title: Medium Evidence (L3-L4)
parent: Drug Reports
nav_order: 2
has_children: true
description: "L3-L4 level drug repurposing candidates with observational or preclinical evidence."
permalink: /evidence-medium/
---

# Medium Evidence Level Drugs

Candidates with preliminary evidence requiring further validation

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L3** | Observational studies / Large case series | Preliminary evidence, needs RCT |
| **L4** | Preclinical / Mechanistic / Case reports | Mechanism reasonable, lacks clinical validation |

---

## Drug List

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 Level ({{ l3_drugs.size }} drugs)

| Drug Name | Indications | Link |
|-----------|-------------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 Level ({{ l4_drugs.size }} drugs)

| Drug Name | Indications | Link |
|-----------|-------------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

---

## Criteria for L3-L4 Classification

### L3 Requirements

- Cohort or case-control study
- OR large case series (≥50 patients)
- Published results with quantitative outcomes

### L4 Requirements

- In vitro or animal studies showing efficacy
- OR mechanistic rationale with supporting data
- OR case reports (< 10 patients)

---

## Related Pages

- [High Evidence (L1-L2)](/evidence-high/)
- [AI Predictions (L5)](/evidence-low/)
- [Full Drug List](/drugs/)
