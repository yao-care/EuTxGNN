#!/usr/bin/env python3
"""
Check PubMed for new publications related to our drug list.
Creates GitHub Issues when new papers are found.

NOTE: Filters out known/approved indications to focus on repurposing evidence.
"""

import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

import requests

from github_utils import create_issue, close_older_pubmed_issues


_KNOWN_STOPWORDS = {"of", "the", "and", "or", "with", "to", "in", "by", "for", "an", "due",  # 不含 "a"：hepatitis A
                    "disease", "disorder", "syndrome"}
_SPELLING = (("aemia", "emia"), ("haem", "hem"), ("oesoph", "esoph"), ("tumour", "tumor"),
             ("oedema", "edema"), ("paediatr", "pediatr"))


def _known_tokens(text: str) -> list:
    t = re.sub(r"\((disease|disorder)\)", " ", (text or "").lower())
    for a, b in _SPELLING:
        t = t.replace(a, b)
    return [w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w
            for w in re.findall(r"[a-z0-9]+", t)]


def is_known_indication(approved_indication: str, predicted_indication: str) -> bool:
    """Check if predicted indication is already an approved/known indication.

    2026-11-03：改成「預測適應症的每個關鍵詞（含 B、C、2 這類短字）都出現在原適應症的同一段」才算已核准
    （段落以「；」「;」或句點分隔）。舊版只要一個長字（例：hypertension、hepatitis）對到就排除，
    會把 amlodipine→pulmonary hypertension、sofosbuvir→hepatitis B 這類真正的新用途也排除掉。
    """
    if not approved_indication or not predicted_indication:
        return False
    need = {w for w in _known_tokens(predicted_indication) if w not in _KNOWN_STOPWORDS}
    if not need:
        return False
    for segment in re.split(r"[；;]|\.\s", approved_indication):
        have = set(_known_tokens(segment))
        if "non" in have and "non" not in need:
            continue  # 「Lymphoma, Non-Hodgkin」不等於 Hodgkin lymphoma
        if need <= have:
            return True
    return False

# Configuration
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "pubmed_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/EuTxGNN")
NCBI_API_KEY = os.environ.get("NCBI_API_KEY")  # Optional, for higher rate limits
RATE_LIMIT_DELAY = 0.4 if NCBI_API_KEY else 1.0  # seconds between API calls


def load_cache() -> dict:
    """Load the cache of previously seen PMIDs."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "seen_pmids": {}}


def save_cache(cache: dict):
    """Save the cache."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    cache["last_check"] = datetime.now().isoformat()
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def load_drug_list() -> list:
    """Load the drug list."""
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["drugs"]


def search_pubmed(drug_name: str, indication: str = "", days_back: int = 7) -> list:
    """Search PubMed for recent publications."""
    # Build search query
    query_parts = [f'"{drug_name}"[Title/Abstract]']
    if indication:
        # Clean up indication text
        indication = indication.split("(")[0].strip()
        if indication and len(indication) > 3:
            query_parts.append(f'"{indication}"[Title/Abstract]')

    query = " AND ".join(query_parts)

    params = {
        "db": "pubmed",
        "term": query,
        "datetype": "edat",  # Entry date
        "reldate": days_back,  # Last N days
        "retmode": "json",
        "retmax": 50,
        "sort": "date"
    }

    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    try:
        response = requests.get(ESEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        id_list = data.get("esearchresult", {}).get("idlist", [])
        return id_list
    except requests.RequestException as e:
        print(f"Error searching PubMed for {drug_name}: {e}")
        return []


def _clean_indication(name: str) -> str:
    name = re.sub(r"\s*\((disease|disorder)\)\s*", " ", name, flags=re.I)
    return re.sub(r"\s+", " ", name).strip().replace('"', "")


def search_pubmed_predicted(inn: str, indications: list, days_back: int = 7) -> list:
    """2026-10-16：查「INN AND (預測新適應症1 OR …)」，只抓和預測有關的新文獻。"""
    terms = [f'"{_clean_indication(i)}"[Title/Abstract]' for i in indications if len(_clean_indication(i)) > 3]
    if not terms:
        return []
    query = f'"{inn}"[Title/Abstract] AND (' + " OR ".join(terms) + ")"
    params = {
        "db": "pubmed",
        "term": query,
        "datetype": "edat",
        "reldate": days_back,
        "retmode": "json",
        "retmax": 50,
        "sort": "date",
    }
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY
    try:
        response = requests.get(ESEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
        return response.json().get("esearchresult", {}).get("idlist", [])
    except requests.RequestException as e:
        print(f"Error searching PubMed for {inn}: {e}")
        return []


ROLE_PATTERNS = [
    (r"refractory|relapsed|after failure|inadequate response|switch(ing)? (from|to)|prior (therapy|treatment)|resistant to", "drug may be prior/frontline therapy, not the tested intervention"),
    (r"conditioning|myeloablative|before (stem cell|bone marrow) transplant|transplant(ation)? regimen", "drug may be used as transplant conditioning"),
    (r"versus|vs\.?|compared with|comparator|placebo-controlled", "comparative study — check whether the drug is the comparator arm"),
    (r"adverse|toxicity|induced|associated with .* use|case of .* after", "may describe an adverse effect rather than efficacy"),
]


def _role_flags(text: str) -> str:
    """N-02：標出「藥只是前線治療／條件療法／對照組／不良反應」等需要人工判讀的情況（以標題關鍵字判斷，僅供提示）。"""
    t = (text or "").lower()
    return "; ".join(msg for pat, msg in ROLE_PATTERNS if re.search(pat, t))


def matched_indications(papers: list, indications: list) -> list:
    """以論文標題（與摘要，有抓到時）比對命中哪些預測新適應症；比對不到就回傳空串列。"""
    hits = []
    for p in papers:
        hits += [i for i in paper_hits(p, indications) if i not in hits]
    return hits


def _norm_text(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w]+", " ", (text or "").lower())).strip()


def paper_hits(paper: dict, indications: list) -> list:
    """2026-11-03：論文標題或摘要直接出現哪個預測新適應症（標點與空白正規化後比對片語）。"""
    text = " " + _norm_text(paper.get("title", "") + " " + paper.get("abstract", "")) + " "
    hits = []
    for i in indications or []:
        ci = _norm_text(_clean_indication(i))
        if ci and f" {ci} " in text and i not in hits:
            hits.append(i)
    return hits


def fetch_abstracts(papers: list) -> None:
    """用 efetch 補上摘要（只對準備開 issue 的論文呼叫）；失敗時維持只用標題比對。"""
    if not papers:
        return
    params = {"db": "pubmed", "id": ",".join(p["pmid"] for p in papers), "retmode": "xml", "rettype": "abstract"}
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY
    try:
        import xml.etree.ElementTree as ET
        response = requests.get(EFETCH_URL, params=params, timeout=60)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        abstracts = {}
        for art in root.iter("PubmedArticle"):
            pmid = art.findtext(".//MedlineCitation/PMID", default="")
            parts = ["".join(a.itertext()) for a in art.iter("AbstractText")]
            abstracts[pmid] = " ".join(parts)
        for p in papers:
            p["abstract"] = abstracts.get(p["pmid"], "")
    except (requests.RequestException, ValueError) as e:  # ET.ParseError 是 ValueError 的子類別
        print(f"Error fetching abstracts: {e}")


def get_paper_details(pmids: list) -> list:
    """Get details for a list of PMIDs."""
    if not pmids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json"
    }

    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    try:
        response = requests.get(ESUMMARY_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        result = data.get("result", {})
        papers = []

        for pmid in pmids:
            paper_data = result.get(pmid, {})
            if paper_data and "title" in paper_data:
                papers.append({
                    "pmid": pmid,
                    "title": paper_data.get("title", ""),
                    "source": paper_data.get("source", ""),
                    "pubdate": paper_data.get("pubdate", ""),
                    "authors": [a.get("name", "") for a in paper_data.get("authors", [])[:3]]
                })

        return papers
    except requests.RequestException as e:
        print(f"Error getting paper details: {e}")
        return []


def create_github_issue(drug_name: str, new_papers: list, indications: list = None, skipped: int = 0):
    """Create a GitHub Issue for new papers found.

    2026-11-03：new_papers 只含標題／摘要直接命中預測適應症的論文，indications 只含真正命中的預測；
    skipped＝同一輪沒有直接命中的新論文數（只寫入快取）。
    """
    indications = indications or []
    ind_label = "; ".join(indications[:2]) + (" …" if len(indications) > 2 else "")
    title = f"📚 New Publications: {drug_name} ({len(new_papers)} papers)"
    if ind_label:
        title += f" → {ind_label}"  # 接在數量後面，github_utils 以「：…(」擷取藥名才對得上

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue for {drug_name} with {len(new_papers)} new papers")
        for paper in new_papers[:3]:
            print(f"  - PMID {paper['pmid']}: {paper['title'][:60]}...")
        return

    # Close older issues for this drug before creating a new one
    closed_count = close_older_pubmed_issues(drug_name)
    if closed_count > 0:
        print(f"  → Closed {closed_count} older issue(s) for {drug_name}")

    # Format paper details
    paper_details = []
    for paper in new_papers:
        authors = ", ".join(paper["authors"]) + (" et al." if len(paper["authors"]) >= 3 else "")
        hit = paper_hits(paper, indications)
        where = "title" if paper_hits({"title": paper["title"]}, hit) else "abstract"
        role = _role_flags(paper["title"])
        paper_details.append(
            f"### PMID: {paper['pmid']}\n"
            f"- **Title**: {paper['title']}\n"
            f"- **Matched predicted indication**: {'; '.join(hit) + f' (in {where})' if hit else '-'}\n"
            + (f"- **⚠ Role flag**: {role}\n" if role else "")
            + f"- **Journal**: {paper['source']}\n"
            f"- **Publication Date**: {paper['pubdate']}\n"
            f"- **Authors**: {authors}\n"
            f"- **Link**: https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/\n"
        )

    skipped_note = (f"_{skipped} other new publication(s) without the predicted indication in the title or abstract "
                    f"were recorded in the cache only._\n") if skipped else ""

    body = f"""## 📚 New Publications Detected

This issue was automatically created by GitHub Actions.

### Drug Name
{drug_name}

### Predicted New Indication(s)
{chr(10).join("- " + x for x in indications) if indications else "-"}

### PMIDs
{", ".join(p["pmid"] for p in new_papers)}

### Data Source
PubMed

### Evidence Type
New Academic Publications

### Details
Found **{len(new_papers)}** new publications mentioning a predicted indication in the title or abstract:

{"".join(paper_details)}
{skipped_note}
### Suggested Actions
- [ ] Review paper abstracts
- [ ] Evaluate publication type (RCT, observational, case report, etc.)
- [ ] Evaluate if drug report evidence level needs updating
- [ ] Add publication information to report

---
*Auto-detected at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Create the issue with deduplication check
    labels = ["auto-detected", "needs-review", "pubmed"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("PubMed Evidence Checker")
    print("(Filtering out known/approved indications)")
    print(f"Started at: {datetime.now().isoformat()}")
    print(f"NCBI API Key: {'Configured' if NCBI_API_KEY else 'Not configured (slower rate limit)'}")
    print("=" * 60)

    # Load data
    cache = load_cache()
    drugs = load_drug_list()

    print(f"Loaded {len(drugs)} drugs from drug list")
    print(f"Last check: {cache.get('last_check', 'Never')}")

    # Check each drug
    new_findings = []
    seen_pmids = cache.get("seen_pmids", {})
    skipped_known = 0

    for i, drug in enumerate(drugs):
        drug_name = drug["name"]
        indication = drug.get("predicted_indication", "")
        approved_indication = drug.get("approved_indication", "")

        predicted = drug.get("predicted_indications") or []
        # 2026-11-03：已核准用途排除逐一套在預測清單上（drug_list 有 approved_indication 時才會作用）
        if approved_indication:
            known = [x for x in predicted if is_known_indication(approved_indication, x)]
            predicted = [x for x in predicted if x not in known]
            if known and not predicted:
                skipped_known += 1
                continue

        print(f"\n[{i+1}/{len(drugs)}] Checking: {drug_name}")

        if not predicted or not drug.get("inn"):
            continue
        pmids = search_pubmed_predicted(drug["inn"], predicted, days_back=7)
        time.sleep(RATE_LIMIT_DELAY)

        if not pmids:
            continue

        # Filter to truly new papers
        drug_seen = seen_pmids.get(drug_name, [])
        is_initial_discovery = not drug_seen  # First time checking this drug
        new_pmids = [p for p in pmids if p not in drug_seen]

        if new_pmids:
            # Get paper details
            papers = get_paper_details(new_pmids)
            time.sleep(RATE_LIMIT_DELAY)

            if papers:
                # Skip issue creation for initial discovery
                if is_initial_discovery:
                    print(f"  Initial discovery: {len(papers)} papers (baseline established)")
                # Skip if only 1 paper - wait for more evidence
                elif len(papers) < 2:
                    print(f"  Only {len(papers)} paper found - below threshold")
                else:
                    # 2026-11-03：標題或摘要直接命中預測適應症的論文才開 issue；其餘只寫入快取
                    fetch_abstracts(papers)
                    time.sleep(RATE_LIMIT_DELAY)
                    hit_papers = [p for p in papers if paper_hits(p, predicted)]
                    if not hit_papers:
                        print(f"  {len(papers)} new papers, none directly mention a predicted indication - cache only")
                    else:
                        hits = matched_indications(hit_papers, predicted)
                        print(f"  Found {len(hit_papers)} new papers matching {hits}!")
                        new_findings.append({
                            "drug": drug_name,
                            "papers": hit_papers,
                            "indications": hits,
                            "skipped": len(papers) - len(hit_papers),
                        })

            # Update seen PMIDs
            drug_seen.extend(new_pmids)

        seen_pmids[drug_name] = drug_seen

    # Update cache
    cache["seen_pmids"] = seen_pmids
    save_cache(cache)

    # Create issues for new findings
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Skipped (known indications): {skipped_known}")

    if new_findings:
        print(f"New findings: {len(new_findings)}")
        print("\nCreating Issues...")
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["papers"], finding["indications"], finding.get("skipped", 0))
    else:
        print("No new papers found.")

    print(f"\nCompleted at: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
