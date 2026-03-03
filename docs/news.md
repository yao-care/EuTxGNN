---
layout: default
title: 📰 Health News
nav_order: 3
description: "Automated health news monitoring for EuTxGNN drugs and indications"
permalink: /news/
---

# Health News Monitoring

Automated tracking of health news related to EuTxGNN drugs and indications
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
      let html = `<p style="color: #666; font-size: 0.9em;">Updated: ${new Date(data.fetched_at).toLocaleString()} | Total: ${data.total_items} items | Relevant: ${data.relevant_items} items</p>`;
      html += '<div class="news-list">';

      data.items.slice(0, 20).forEach(item => {
        const drugs = item.matched_drugs && item.matched_drugs.length > 0
          ? `<span class="drug-tag">${item.matched_drugs.join(', ')}</span>`
          : '';
        const diseases = item.matched_diseases && item.matched_diseases.length > 0
          ? `<span class="disease-tag">${item.matched_diseases.join(', ')}</span>`
          : '';

        html += `
          <div class="news-item">
            <h4><a href="${item.link}" target="_blank" rel="noopener">${item.title}</a></h4>
            <p class="news-meta">
              <span class="source">${item.source}</span>
              ${item.pub_date ? `<span class="date">${item.pub_date}</span>` : ''}
            </p>
            ${item.description ? `<p class="description">${item.description.substring(0, 200)}${item.description.length > 200 ? '...' : ''}</p>` : ''}
            <div class="tags">
              ${drugs}
              ${diseases}
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
}
.disease-tag {
  background: #fff3cd;
  color: #856404;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.85rem;
}
</style>

---

## News Sources

| Source | Region | Update Frequency |
|--------|--------|------------------|
| EMA News | EU | Every 6 hours |
| EMA Human Medicines | EU | Every 6 hours |
| ECDC News | EU | Every 6 hours |
| ECDC Risk Assessments | EU | Every 6 hours |
| ECDC Guidance | EU | Every 6 hours |

---

## How It Works

1. **Automated Fetching**: GitHub Actions fetches news every 6 hours from official RSS feeds
2. **Keyword Matching**: System matches 638 EMA drugs and 21 disease categories
3. **Relevance Filtering**: Only news mentioning tracked drugs/diseases are shown
4. **Direct Links**: Click any headline to read the full article on the source website

---

## Data Access

- **JSON Data**: [GitHub - eu_health_news.json](https://github.com/yao-care/EuTxGNN/blob/main/data/news/eu_health_news.json)
- **Synonyms**: [GitHub - synonyms.json](https://github.com/yao-care/EuTxGNN/blob/main/data/news/synonyms.json)

---

## Disclaimer

News content is automatically collected from official European health agency RSS feeds (EMA, ECDC). EuTxGNN does not endorse or verify the accuracy of external news reports. This feature is for research awareness only.

For medical information, consult qualified healthcare professionals.
