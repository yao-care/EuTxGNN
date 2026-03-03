---
layout: default
title: Health News
nav_order: 5
description: "Automated health news monitoring for EuTxGNN drugs and indications"
permalink: /news/
---

# Health News Monitoring

Automated tracking of health news related to EuTxGNN drugs and indications

---

## News Sources

| Source | Region | Update Frequency |
|--------|--------|------------------|
| EMA News | EU | Daily |
| EMA Press Releases | EU | As published |
| ECDC | EU | Daily |
| WHO Europe | Europe | Daily |
| Medscape | Global | Daily |

---

## Latest Updates

<div style="background: #f8f9fa; padding: 1rem; border-radius: 8px;">
<p>News monitoring is automated via GitHub Actions. Check the <a href="https://github.com/yao-care/EuTxGNN/tree/main/data/news">news data folder</a> for the latest collected news.</p>
</div>

---

## How It Works

1. **Keyword Monitoring**: System tracks 638 drugs and 4,570 indications
2. **Source Crawling**: RSS feeds and news APIs are checked regularly
3. **Matching**: News mentioning drugs or diseases are flagged
4. **Linking**: Matched news connects to relevant drug reports

---

## Monitored Keywords

### Drug Examples

- Metformin, Atorvastatin, Adalimumab
- Infliximab, Rituximab, Pembrolizumab
- Semaglutide, Trastuzumab, etc.

### Disease Examples

- Diabetes, Hypertension, Cancer
- Alzheimer disease, Multiple sclerosis
- Crohn disease, Psoriasis, etc.

---

## Data Access

News data is available at:

- [GitHub: news data](https://github.com/yao-care/EuTxGNN/tree/main/data/news)
- Format: JSON with matched drugs/diseases

---

## Disclaimer

News content is automatically collected from public sources. EuTxGNN does not endorse or verify the accuracy of external news reports. This feature is for research awareness only.

For medical information, consult qualified healthcare professionals.
