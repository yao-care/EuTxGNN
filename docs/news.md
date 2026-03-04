---
layout: default
title: 📰 Health News
nav_order: 3
description: "Automated health news monitoring for EuTxGNN drugs and indications"
permalink: /news/
---

# Health News Monitoring

News about diseases with **linked drug repurposing reports** — click drug tags to view predictions
{: .fs-6 .fw-300 }

---

## Latest News

<div id="news-container">
  <p>Loading news...</p>
</div>

<script>
async function loadNews() {
  const container = document.getElementById('news-container');
  try {
    const response = await fetch('https://raw.githubusercontent.com/yao-care/EuTxGNN/main/data/news/eu_health_news.json');
    const data = await response.json();

    if (data.items && data.items.length > 0) {
      // Filter: show news with diseases (which have related_drugs)
      const relevantNews = data.items.filter(item =>
        item.matched_diseases && item.matched_diseases.length > 0
      );

      let html = `<p style="color: #666; font-size: 0.9em;">Updated: ${new Date(data.fetched_at).toLocaleString()} | Disease-related news: ${relevantNews.length} items</p>`;

      if (relevantNews.length === 0) {
        html += '<p class="no-news">No disease-related news at this time. Check back later.</p>';
        container.innerHTML = html;
        return;
      }

      html += '<div class="news-list">';

      relevantNews.slice(0, 20).forEach(item => {
        // Disease tags
        const diseases = item.matched_diseases.map(d =>
          `<span class="disease-tag">${d.name}</span>`
        ).join(' ');

        // Related drugs from diseases (with links to reports)
        const relatedDrugSlugs = new Set();
        item.matched_diseases.forEach(d => {
          (d.related_drugs || []).forEach(slug => relatedDrugSlugs.add(slug));
        });
        const relatedDrugs = Array.from(relatedDrugSlugs).slice(0, 5).map(slug =>
          `<a href="/drugs/${slug}/" class="drug-tag">${slug} →</a>`
        ).join(' ');

        // Directly matched drugs (if any)
        const directDrugs = (item.matched_drugs || []).map(d =>
          `<a href="${d.url}" class="drug-tag direct">${d.name} →</a>`
        ).join(' ');

        html += `
          <div class="news-item">
            <h4><a href="${item.link}" target="_blank" rel="noopener">${item.title} <span class="external-icon">↗</span></a></h4>
            <p class="news-meta">
              <span class="source">${item.source}</span>
              ${item.pub_date ? `<span class="date">${item.pub_date}</span>` : ''}
            </p>
            ${item.description ? `<p class="description">${item.description.substring(0, 200)}${item.description.length > 200 ? '...' : ''}</p>` : ''}
            <div class="tags">
              ${diseases}
            </div>
            <div class="related-drugs">
              <span class="related-label">Related drugs:</span> ${directDrugs} ${relatedDrugs}
            </div>
          </div>
        `;
      });

      html += '</div>';
      container.innerHTML = html;
    } else {
      container.innerHTML = '<p>No relevant news at this time. Check back later.</p>';
    }
  } catch (error) {
    container.innerHTML = '<p>Unable to load news. Please check the <a href="https://github.com/yao-care/EuTxGNN/tree/main/data/news">data folder</a> directly.</p>';
    console.error('Error loading news:', error);
  }
}

loadNews();
</script>

<style>
.news-list {
  margin-top: 1rem;
}
.news-item {
  padding: 1rem;
  margin-bottom: 1rem;
  border: 1px solid #e1e4e8;
  border-radius: 8px;
  background: #fafbfc;
}
.news-item h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
}
.news-item h4 a {
  color: #0366d6;
  text-decoration: none;
}
.news-item h4 a:hover {
  text-decoration: underline;
}
.external-icon {
  font-size: 0.8em;
  opacity: 0.6;
  margin-left: 2px;
}
.news-meta {
  font-size: 0.85rem;
  color: #666;
  margin-bottom: 0.5rem;
}
.news-meta .source {
  background: #e1e4e8;
  padding: 2px 6px;
  border-radius: 3px;
  margin-right: 8px;
}
.description {
  font-size: 0.95rem;
  color: #444;
  margin-bottom: 0.5rem;
}
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.drug-tag {
  background: #d4edda;
  color: #155724;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.85rem;
  text-decoration: none;
  display: inline-block;
  transition: all 0.2s ease;
}
.drug-tag:hover {
  background: #28a745;
  color: white;
  text-decoration: none;
}
.disease-tag {
  background: #fff3cd;
  color: #856404;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.85rem;
  text-decoration: none;
  display: inline-block;
  transition: all 0.2s ease;
}
.disease-tag:hover {
  background: #ffc107;
  color: #333;
  text-decoration: none;
}
.no-news {
  text-align: center;
  padding: 2rem;
  color: #666;
  background: #f8f9fa;
  border-radius: 8px;
}
.related-drugs {
  margin-top: 0.5rem;
  padding-top: 0.5rem;
  border-top: 1px dashed #e1e4e8;
}
.related-label {
  font-size: 0.8rem;
  color: #666;
  margin-right: 0.5rem;
}
.drug-tag.direct {
  background: #28a745;
  color: white;
}
</style>

---

## News Sources

| Source | Region | Type |
|--------|--------|------|
| Google News UK | United Kingdom | Media health news |
| Google News Germany | Germany | Media health news |
| Google News France | France | Media health news |
| Google News Spain | Spain | Media health news |
| Google News Italy | Italy | Media health news |
| EMA News | EU | Official agency |
| EMA Human Medicines | EU | Drug approvals |
| ECDC News | EU | Disease control |

---

## How It Works

1. **Automated Fetching**: GitHub Actions fetches news every 6 hours from official RSS feeds
2. **Disease Matching**: System matches 21 disease categories (cancer, diabetes, hypertension, etc.)
3. **Drug Relations**: Each disease links to drugs with repurposing predictions for that condition
4. **Direct Links**: Click drug tags → view repurposing report | Click headline → read original article

---

## Data Access

- **JSON Data**: [GitHub - eu_health_news.json](https://github.com/yao-care/EuTxGNN/blob/main/data/news/eu_health_news.json)
- **Synonyms**: [GitHub - synonyms.json](https://github.com/yao-care/EuTxGNN/blob/main/data/news/synonyms.json)

---

## Related Links

| Resource | Description |
|----------|-------------|
| [Drug Reports](/drugs/) | Browse all 642 EMA drug repurposing reports |
| [High Evidence (L1-L2)](/evidence-high/) | Predictions with clinical trial support |
| [Data Downloads](/downloads/) | Download prediction data in CSV/JSON |
| [Methodology](/methodology/) | Learn about TxGNN prediction model |
| [FHIR API](/fhir/metadata) | Integration endpoints for EHR systems |
| [EMA Website](https://www.ema.europa.eu/){:target="_blank"} | Official European Medicines Agency |
| [ECDC Website](https://www.ecdc.europa.eu/){:target="_blank"} | European Centre for Disease Prevention and Control |

---

## Disclaimer

News content is automatically collected from official European health agency RSS feeds (EMA, ECDC). EuTxGNN does not endorse or verify the accuracy of external news reports. This feature is for research awareness only.

For medical information, consult qualified healthcare professionals.
