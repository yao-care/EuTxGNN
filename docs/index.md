---
layout: default
title: Drug Repurposing Reports
nav_order: 1
description: "AI-powered drug repurposing predictions for 560 EMA-approved drugs. TxGNN model identifies potential new therapeutic uses with evidence-based validation."
permalink: /
---

# Drug Repurposing: From AI to Evidence
{: .fs-9 }

**EuTxGNN** uses the Harvard TxGNN model to predict drug repurposing candidates for **{{ site.data.drug_stats.total_drugs }}** EMA-approved drugs, generating **2,644** potential new therapeutic uses.
{: .fs-6 .fw-300 }

[Browse Drug Reports](/drugs/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Learn Methodology](/methodology/){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Drug Search

Enter a **drug name** or **disease name** to find repurposing predictions. Supports generic names, brand names, and disease keywords.

<style>
.drug-lookup-container { margin: 1.5rem 0; }
.lookup-search-box { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
.lookup-input-wrapper { flex: 1; position: relative; }
#lookup-input { width: 100%; padding: 0.75rem 2.5rem 0.75rem 1rem; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; }
#lookup-input:focus { outline: none; border-color: #1976D2; }
.lookup-clear-btn { position: absolute; right: 0.75rem; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; color: #999; font-size: 1.2rem; }
.lookup-search-btn { padding: 0.75rem 1.5rem; background: #1976D2; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600; }
.lookup-search-btn:hover { background: #1565C0; }
.lookup-filters { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; margin-bottom: 1rem; }
.filter-label { font-weight: 600; color: #666; }
.lookup-filters label { display: flex; align-items: center; gap: 0.25rem; cursor: pointer; }
.lookup-results { margin-top: 1rem; }
.lookup-notice { padding: 1rem; background: #f5f5f5; border-radius: 8px; color: #666; }
.result-section { margin-bottom: 1.5rem; }
.section-title { font-weight: 600; color: #333; margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 2px solid #1976D2; }
.result-card { padding: 1rem; background: #f8f9fa; border-radius: 8px; margin-bottom: 0.75rem; }
.result-header { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem; }
.drug-name { font-weight: 600; color: #1976D2; text-decoration: none; }
.drug-name:hover { text-decoration: underline; }
.level-badge { padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: white; }
.level-L1 { background: #2E7D32; }
.level-L2 { background: #66BB6A; }
.level-L3 { background: #FDD835; color: #333; }
.level-L4 { background: #FB8C00; }
.level-L5 { background: #9E9E9E; }
.result-original { font-size: 0.9rem; color: #666; margin-bottom: 0.5rem; }
.result-indications { font-size: 0.9rem; }
.ind-item { display: inline-block; margin: 0.25rem 0.5rem 0.25rem 0; }
.view-report { display: inline-block; margin-top: 0.5rem; color: #1976D2; text-decoration: none; font-weight: 500; }
.view-report:hover { text-decoration: underline; }
.result-drugs .drug-item { display: flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0; }
.score { color: #666; font-size: 0.85rem; }
.more { color: #999; font-size: 0.85rem; font-style: italic; }
</style>

<div class="drug-lookup-container">
  <div class="lookup-search-box">
    <div class="lookup-input-wrapper">
      <input type="text" id="lookup-input" placeholder="Enter drug name or disease name..." autocomplete="off">
      <button id="lookup-clear" class="lookup-clear-btn" style="display: none;">✕</button>
    </div>
    <button id="lookup-search" class="lookup-search-btn">Search</button>
  </div>
  <div class="lookup-filters">
    <span class="filter-label">Evidence Level:</span>
    <label><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
    <label><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
    <label><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
    <label><input type="checkbox" class="level-filter" value="L4" checked> L4</label>
    <label><input type="checkbox" class="level-filter" value="L5" checked> L5</label>
  </div>
  <div id="lookup-results" class="lookup-results"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js" integrity="sha384-PCSoOZTpbkikBEtd/+uV3WNdc676i9KUf01KOA8CnJotvlx8rRrETbDuwdjqTYvt" crossorigin="anonymous"></script>
<script>
  window.EUTXGNN_CONFIG = {
    searchIndexUrl: '{{ "/data/search-index.json" | relative_url }}',
    drugsBaseUrl: '{{ "/drugs/" | relative_url }}'
  };
</script>
<script src="{{ '/assets/js/drug-lookup.js' | relative_url }}"></script>

---

## Key Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">From Prediction to Evidence</strong><br>
    <span style="color: #666;">Each report integrates clinical trial IDs (NCT), literature references (PMID), and EMA approval information for complete traceability.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">Five-Level Evidence Classification</strong><br>
    <span style="color: #666;">L1 (Multiple Phase 3 RCTs) to L5 (AI prediction only) classification helps prioritize candidates for validation.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong style="font-size: 1.1rem;">EMA Drug Coverage</strong><br>
    <span style="color: #666;">Focused on {{ site.data.drug_stats.total_drugs }} EMA centrally-authorized medicines with 2,644 repurposing predictions ready for research.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong style="font-size: 1.1rem;">FHIR Integration</strong><br>
    <span style="color: #666;">FHIR R4 compliant API and SMART on FHIR app for seamless EHR integration.</span>
  </div>
</div>

---

## Evidence Level Distribution

<style>
.evidence-bar { display: flex; height: 48px; border-radius: 8px; overflow: hidden; margin: 1.5rem 0; font-size: 0.85rem; }
.bar-segment { display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; transition: all 0.3s ease; text-decoration: none; }
.bar-segment:hover { filter: brightness(1.1); }
.l5 { background: #9E9E9E; }
.chart-container { display: flex; flex-wrap: wrap; gap: 2rem; align-items: center; justify-content: center; margin: 2rem 0; }
.donut-chart { position: relative; width: 200px; height: 200px; }
.donut-chart svg { transform: rotate(-90deg); }
.donut-segment { fill: none; stroke-width: 40; transition: stroke-width 0.3s ease; cursor: pointer; }
.donut-segment:hover { stroke-width: 45; }
.donut-center { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; }
.donut-center .number { font-size: 2.5rem; font-weight: 700; color: #333; line-height: 1; }
.donut-center .label { font-size: 0.9rem; color: #666; }
.chart-legend { display: flex; flex-direction: column; gap: 0.75rem; }
.legend-item { display: flex; align-items: center; gap: 0.75rem; padding: 0.5rem 1rem; background: #f8f9fa; border-radius: 8px; text-decoration: none; color: #333; transition: transform 0.2s, box-shadow 0.2s; }
.legend-item:hover { transform: translateX(4px); box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.legend-color { width: 16px; height: 16px; border-radius: 4px; }
.legend-text { flex: 1; }
.legend-count { font-weight: 700; font-size: 1.1rem; }
</style>

{%- comment -%}2026-10-16：證據等級圖改由可收錄藥物頁即時計算（原本寫死）{%- endcomment -%}
{% assign ld = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign n1 = ld | where: "evidence_level", "L1" | size %}{% assign n2 = ld | where: "evidence_level", "L2" | size %}{% assign n3 = ld | where: "evidence_level", "L3" | size %}{% assign n4 = ld | where: "evidence_level", "L4" | size %}{% assign n5 = ld | where: "evidence_level", "L5" | size %}
{% assign tot = n1 | plus: n2 | plus: n3 | plus: n4 | plus: n5 %}{% if tot == 0 %}{% assign tot = 1 %}{% endif %}
{% assign s1 = n1 | times: 502.65 | divided_by: tot %}{% assign s2 = n2 | times: 502.65 | divided_by: tot %}{% assign s3 = n3 | times: 502.65 | divided_by: tot %}{% assign s4 = n4 | times: 502.65 | divided_by: tot %}{% assign s5 = n5 | times: 502.65 | divided_by: tot %}
{% assign o2 = s1 %}{% assign o3 = o2 | plus: s2 %}{% assign o4 = o3 | plus: s3 %}{% assign o5 = o4 | plus: s4 %}
{% assign p1 = n1 | times: 100.0 | divided_by: tot %}{% assign p2 = n2 | times: 100.0 | divided_by: tot %}{% assign p5 = n5 | times: 100.0 | divided_by: tot %}
<div class="chart-container">
  <div class="donut-chart">
    <svg viewBox="0 0 200 200">
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#2E7D32" stroke-dasharray="{{ s1 | round: 2 }} {{ 502.65 | minus: s1 | round: 2 }}" stroke-dashoffset="0" onclick="location.href='{{ '/evidence-high' | relative_url }}'" title="L1: {{ n1 }} drugs"/>
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#66BB6A" stroke-dasharray="{{ s2 | round: 2 }} {{ 502.65 | minus: s2 | round: 2 }}" stroke-dashoffset="-{{ o2 | round: 2 }}" onclick="location.href='{{ '/evidence-high' | relative_url }}'" title="L2: {{ n2 }} drugs"/>
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#FDD835" stroke-dasharray="{{ s3 | round: 2 }} {{ 502.65 | minus: s3 | round: 2 }}" stroke-dashoffset="-{{ o3 | round: 2 }}" onclick="location.href='{{ '/evidence-medium' | relative_url }}'" title="L3: {{ n3 }} drugs"/>
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#FB8C00" stroke-dasharray="{{ s4 | round: 2 }} {{ 502.65 | minus: s4 | round: 2 }}" stroke-dashoffset="-{{ o4 | round: 2 }}" onclick="location.href='{{ '/evidence-medium' | relative_url }}'" title="L4: {{ n4 }} drugs"/>
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#9E9E9E" stroke-dasharray="{{ s5 | round: 2 }} {{ 502.65 | minus: s5 | round: 2 }}" stroke-dashoffset="-{{ o5 | round: 2 }}" onclick="location.href='{{ '/evidence-low' | relative_url }}'" title="L5: {{ n5 }} drugs"/>
    </svg>
    <div class="donut-center">
      <div class="number">{{ ld.size }}</div>
      <div class="label">Drug Reports</div>
    </div>
  </div>
  <div class="chart-legend">
    <a href="{{ '/evidence-high' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #2E7D32;"></span>
      <span class="legend-text">L1 Multiple Phase 3 RCTs</span>
      <span class="legend-count">{{ n1 }}</span>
    </a>
    <a href="{{ '/evidence-high' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #66BB6A;"></span>
      <span class="legend-text">L2 Single RCT / Phase 2</span>
      <span class="legend-count">{{ n2 }}</span>
    </a>
    <a href="{{ '/evidence-medium' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #FDD835;"></span>
      <span class="legend-text">L3 Observational studies</span>
      <span class="legend-count">{{ n3 }}</span>
    </a>
    <a href="{{ '/evidence-medium' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #FB8C00;"></span>
      <span class="legend-text">L4 Preclinical / Mechanistic</span>
      <span class="legend-count">{{ n4 }}</span>
    </a>
    <a href="{{ '/evidence-low' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #9E9E9E;"></span>
      <span class="legend-text">L5 AI prediction only</span>
      <span class="legend-count">{{ n5 }}</span>
    </a>
  </div>
</div>

<div class="evidence-bar">
  <a href="{{ '/evidence-high' | relative_url }}" class="bar-segment l1" style="width: {{ p1 | round: 2 }}%; background: #2E7D32;" title="L1: {{ n1 }} drugs">L1</a>
  <a href="{{ '/evidence-high' | relative_url }}" class="bar-segment l2" style="width: {{ p2 | round: 2 }}%; background: #66BB6A;" title="L2: {{ n2 }} drugs">L2</a>
  <a href="{{ '/evidence-medium' | relative_url }}" class="bar-segment l3" style="width: 0.5%; min-width: 20px; background: #FDD835;" title="L3: {{ n3 }} drugs"></a>
  <a href="{{ '/evidence-medium' | relative_url }}" class="bar-segment l4" style="width: 0.5%; min-width: 20px; background: #FB8C00;" title="L4: {{ n4 }} drugs"></a>
  <a href="{{ '/evidence-low' | relative_url }}" class="bar-segment l5" style="width: {{ p5 | round: 2 }}%; background: #9E9E9E;" title="L5: {{ n5 }} drugs">L5: {{ n5 }}</a>
</div>

{% include d3-charts.html %}

---

## Quick Navigation

| Category | Description | Link |
|----------|-------------|------|
| **High Evidence** | L1-L2, priority for clinical evaluation | [View {{ n1 | plus: n2 }} drugs](/evidence-high/) |
| **Medium Evidence** | L3-L4, requires additional validation | [View {{ n3 | plus: n4 }} drugs](/evidence-medium/) |
| **AI Predictions** | L5, research direction reference | [View {{ n5 }} drugs](/evidence-low/) |
| **Full Drug List** | All {{ site.data.drug_stats.total_drugs }} drugs (searchable) | [Drug List](/drugs/) |
| **Health News** | Automated EU health news monitoring | [View News](/news/) |
| **Data Downloads** | CSV / JSON formats | [Downloads](/downloads/) |
| **FHIR API** | Integration endpoints | [FHIR Metadata](/fhir/metadata) |

---

## About This Project

EuTxGNN uses the **TxGNN** deep learning model published by Harvard's Zitnik Lab in *Nature Medicine* to predict potential new therapeutic uses for EMA-approved medications.

> "TxGNN is the first foundation model designed for clinician-centered drug repurposing, integrating knowledge graphs with deep learning to predict drug efficacy for rare diseases."
> <cite>— Huang et al., Nature Medicine (2024)</cite>

### Statistics

| Item | Count |
|------|-------|
| Drug Reports | {{ site.data.drug_stats.total_drugs }} |
| Repurposing Predictions | 2,644 |
| Unique Indications | 4,570 |

[Learn More](/about/) | [Methodology](/methodology/) | [Data Sources](/sources/)

---

## Data Sources

<style>
.data-source-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin: 2rem 0; padding: 1.5rem; background: #f8f9fa; border-radius: 12px; }
.data-source-card { display: flex; flex-direction: column; align-items: center; padding: 1.25rem 1rem; background: white; border-radius: 10px; text-decoration: none; color: #333; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s; }
.data-source-card:hover { transform: translateY(-4px); box-shadow: 0 6px 20px rgba(0,0,0,0.12); }
.data-source-icon { width: 48px; height: 48px; margin-bottom: 0.75rem; display: flex; align-items: center; justify-content: center; border-radius: 12px; font-size: 24px; }
.data-source-card strong { font-size: 0.95rem; margin-bottom: 0.25rem; }
.data-source-card small { font-size: 0.75rem; color: #666; text-align: center; }
</style>

<div class="data-source-grid">
  <a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDE8E8;">🧬</div>
    <strong style="color: #A51C30;">TxGNN</strong>
    <small>Harvard Zitnik Lab</small>
  </a>
  <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F8;">🏥</div>
    <strong style="color: #205493;">ClinicalTrials.gov</strong>
    <small>NIH Clinical Trials</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F5;">📚</div>
    <strong style="color: #326599;">PubMed</strong>
    <small>Biomedical Literature</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDEDEC;">💊</div>
    <strong style="color: #E74C3C;">DrugBank</strong>
    <small>Drug Database</small>
  </a>
  <a href="https://www.ema.europa.eu/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F8EE;">🇪🇺</div>
    <strong style="color: #003399;">EMA</strong>
    <small>European Medicines Agency</small>
  </a>
</div>

---

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Disclaimer</strong><br>
This report is for <strong>research purposes only</strong> and does not constitute medical advice. Drug use should follow physician guidance. Any drug repurposing decisions require complete clinical validation and regulatory review.
<br><br>
<small>Last updated: 2026-03-05 | Maintainer: 藥提醒科技有限公司 (yao.care)</small>
</div>

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

EuTxGNN is the the European Union site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, deep-learning prediction that excludes uses already recorded in the knowledge graph, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
