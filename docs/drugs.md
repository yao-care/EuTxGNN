---
layout: default
title: Drug List
parent: Drug Reports
nav_order: 4
description: "Complete list of EuTxGNN drug repurposing predictions with evidence levels and search functionality."
permalink: /drugs/
---

# Drug List

638 drugs with repurposing predictions from TxGNN

---

## Search and Filter

<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
  <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center;">
    <div>
      <label for="search-input" style="font-weight: 600; margin-right: 0.5rem;">Search:</label>
      <input type="text" id="search-input" placeholder="Enter drug name..." style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; width: 200px;">
    </div>
    <div>
      <label style="font-weight: 600; margin-right: 0.5rem;">Evidence Level:</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L4" checked> L4</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L5" checked> L5</label>
    </div>
  </div>
</div>

---

## Statistics

| Metric | Value |
|--------|-------|
| Total Drugs | 638 |
| Total Predictions | 32,368 |
| Unique Indications | 4,570 |
| KG Predictions | 718 |
| DL Predictions | 31,650 |

---

## Top Predictions by Score

| Drug | Indication | Score | Source |
|------|------------|-------|--------|
| TRAVOPROST | visceral calciphylaxis | 0.9999 | DL |
| CAPLACIZUMAB | primary release disorder of platelets | 0.9999 | DL |
| ROMIPLOSTIM | primary release disorder of platelets | 0.9999 | DL |
| AZATHIOPRINE | rheumatoid arthritis | 0.9999 | DL |
| INFLIXIMAB | Crohn disease | 0.9999 | KG |

---

## Browse by Category

### Oncology Drugs

Drugs with cancer-related predictions.

### Cardiovascular Drugs

Drugs with cardiovascular predictions.

### Neurological Drugs

Drugs with neurological predictions.

### Immunological Drugs

Drugs with immune-related predictions.

---

## Data Access

All predictions are available via:

- **FHIR API**: `/fhir/ClinicalUseDefinition/`
- **CSV Download**: [See Downloads page](/downloads/)
- **GitHub**: [yao-care/EuTxGNN](https://github.com/yao-care/EuTxGNN)

---

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px;">
<strong>Disclaimer:</strong> These predictions are for research purposes only and require clinical validation before any therapeutic application.
</div>
