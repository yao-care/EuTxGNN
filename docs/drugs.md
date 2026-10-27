---
layout: default
title: Drug List
parent: Drug Reports
nav_order: 4
description: "Complete list of EMA drugs with TxGNN repurposing predictions"
permalink: /drugs/
---
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign l1_count = listed_drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = listed_drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = listed_drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = listed_drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = listed_drugs | where: "evidence_level", "L5" | size %}
{%- comment -%}2026-10-27 build gate（drug-count-text-sync-gap）：站上各頁的藥物數讀 site.data.drug_stats；
它和實際公開藥物頁數不一致時，故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign ds = site.data.drug_stats -%}
{%- if listed_drugs.size != ds.total_drugs or l1_count != ds.level_counts.L1 or l2_count != ds.level_counts.L2 or l3_count != ds.level_counts.L3 or l4_count != ds.level_counts.L4 or l5_count != ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}

# All Drugs

{{ listed_drugs.size }} drug validation reports

---

## Evidence level breakdown

| Evidence level | Drugs | Description |
|---------|--------|------|
| **L1** | {{ l1_count }} | Multiple RCTs / systematic reviews |
| **L2** | {{ l2_count }} | Single RCT / Phase 2 trials |
| **L3** | {{ l3_count }} | Observational studies / large case series |
| **L4** | {{ l4_count }} | Preclinical / mechanistic studies |
| **L5** | {{ l5_count }} | Model prediction only |

---

## Full drug list

{% assign all_drugs = listed_drugs | sort: 'title' %}

| Drug | Evidence level | Indications |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
