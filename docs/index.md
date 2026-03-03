---
layout: default
title: Drug Repurposing Reports
nav_order: 1
description: "AI-powered drug repurposing predictions for 642 EMA-approved drugs. TxGNN model identifies potential new therapeutic uses with evidence-based validation."
permalink: /
---

# Drug Repurposing: From AI to Evidence
{: .fs-9 }

**EuTxGNN** uses the Harvard TxGNN model to predict drug repurposing candidates for **642** EMA-approved drugs, generating **32,368** potential new therapeutic uses.
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

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0"></script>
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
    <span style="color: #666;">Focused on 642 EMA centrally-authorized medicines with 32,368 repurposing predictions ready for research.</span>
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

<div class="chart-container">
  <div class="donut-chart">
    <svg viewBox="0 0 200 200">
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#9E9E9E" stroke-dasharray="502.65 502.65" stroke-dashoffset="0" onclick="location.href='{{ '/evidence-low' | relative_url }}'"/>
    </svg>
    <div class="donut-center">
      <div class="number">642</div>
      <div class="label">Drug Reports</div>
    </div>
  </div>
  <div class="chart-legend">
    <a href="{{ '/evidence-high' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #2E7D32;"></span>
      <span class="legend-text">L1 Multiple Phase 3 RCTs</span>
      <span class="legend-count">0</span>
    </a>
    <a href="{{ '/evidence-high' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #66BB6A;"></span>
      <span class="legend-text">L2 Single RCT / Phase 2</span>
      <span class="legend-count">0</span>
    </a>
    <a href="{{ '/evidence-medium' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #FDD835;"></span>
      <span class="legend-text">L3 Observational studies</span>
      <span class="legend-count">0</span>
    </a>
    <a href="{{ '/evidence-medium' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #FB8C00;"></span>
      <span class="legend-text">L4 Preclinical / Mechanistic</span>
      <span class="legend-count">0</span>
    </a>
    <a href="{{ '/evidence-low' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #9E9E9E;"></span>
      <span class="legend-text">L5 AI prediction only</span>
      <span class="legend-count">642</span>
    </a>
  </div>
</div>

<div class="evidence-bar">
  <a href="{{ '/evidence-low' | relative_url }}" class="bar-segment l5" style="width: 100%" title="L5: 642 drugs">L5: 642 drugs (AI prediction only)</a>
</div>

{% include d3-charts.html %}

---

## Quick Navigation

| Category | Description | Link |
|----------|-------------|------|
| **High Evidence** | L1-L2, priority for clinical evaluation | [View](/evidence-high/) |
| **Medium Evidence** | L3-L4, requires additional validation | [View](/evidence-medium/) |
| **AI Predictions** | L5, research direction reference | [View 642 drugs](/evidence-low/) |
| **Full Drug List** | All 642 drugs (searchable) | [Drug List](/drugs/) |
| **Data Downloads** | CSV / JSON formats | [Downloads](/downloads/) |
| **FHIR API** | Integration endpoints | [FHIR Metadata](/fhir/metadata) |

---

## About This Project

EuTxGNN uses the **TxGNN** deep learning model published by Harvard's Zitnik Lab in *Nature Medicine* to predict potential new therapeutic uses for EMA-approved medications.

> "TxGNN is the first foundation model designed for clinician-centered drug repurposing, integrating knowledge graphs with deep learning to predict drug efficacy for rare diseases."
> <cite>— Huang et al., Nature Medicine (2023)</cite>

### Statistics

| Item | Count |
|------|-------|
| Drug Reports | 642 |
| Repurposing Predictions | 32,368 |
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
<small>Last updated: 2026-03-03 | Maintainer: EuTxGNN Research Team</small>
</div>
