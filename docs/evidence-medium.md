---
layout: default
title: Medium Evidence (L3-L4)
parent: Drug Reports
nav_order: 2
has_children: true
description: "43 medicines at evidence level L3–L4 on this site (European Union), e.g. Abatacept, Brentuximab Vedotin, Cilastatin, with the main predicted new indication, local EMA central authorisations and review-log entries for each."
permalink: /evidence-medium/
---

# Medium Evidence Level Drugs

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
This page lists **{{ site.data.evidence_tier_facts.medium.count }}** of the **{{ site.data.drug_stats.total_drugs }}** medicines with a published report on this site ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Median share at L3–L4 across the 30 TxGNN sites: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}This site is above the median.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}This site is below the median.{% else %}This site is at the median.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
In the local data (EMA central authorisations), **{{ site.data.evidence_tier_facts.medium.with_current }}** of these medicines have at least one authorised entry, **{{ site.data.evidence_tier_facts.medium.none_current }}** have entries but none authorised, and **{{ site.data.evidence_tier_facts.medium.without_data }}** are not in the local data. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** have entries in the review log (corrections of registration facts on the drug page). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** have a predicted indication that no other TxGNN site lists for the same medicine.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

With entries but none authorised: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definitions of all levels: [Methodology]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

Candidates with preliminary evidence requiring further validation

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L3** | Observational studies / Large case series | Preliminary evidence, needs RCT |
| **L4** | Preclinical / Mechanistic / Case reports | Mechanism reasonable, lacks clinical validation |

---

## Drug List

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 Level ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} drugs)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicine | Level | Main predicted new indication | EMA central authorisations: authorised / total | Review log | Only on this site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}yes ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 Level ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} drugs)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicine | Level | Main predicted new indication | EMA central authorisations: authorised / total | Review log | Only on this site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}yes ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

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
