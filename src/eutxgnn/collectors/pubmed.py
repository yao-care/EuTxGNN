"""PubMed evidence collector using NCBI E-utilities."""

import os
import re
import time
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode, quote
from xml.etree import ElementTree as ET

from .base import BaseCollector, CollectorResult


class PubMedCollector(BaseCollector):
    """Collector for PubMed biomedical literature."""

    source_name = "pubmed"

    # NCBI E-utilities endpoints
    ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    # Publication type classifications
    RCT_TYPES = [
        "Randomized Controlled Trial",
        "Controlled Clinical Trial",
        "Clinical Trial, Phase III",
        "Clinical Trial, Phase IV",
    ]

    REVIEW_TYPES = [
        "Systematic Review",
        "Meta-Analysis",
        "Review",
    ]

    OBSERVATIONAL_TYPES = [
        "Observational Study",
        "Cohort Studies",
        "Case-Control Studies",
        "Clinical Trial, Phase II",
    ]

    def __init__(self, max_results: int = 20, api_key: str | None = None):
        """
        Initialize the collector.

        Args:
            max_results: Maximum number of results per query
            api_key: NCBI API key (optional, increases rate limit)
        """
        self.max_results = max_results
        self.api_key = api_key or os.environ.get("NCBI_API_KEY")
        self._last_request_time = 0
        # Rate limit: 3/sec without key, 10/sec with key
        self._min_interval = 0.1 if self.api_key else 0.34

    def _rate_limit(self):
        """Enforce rate limiting between requests."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self._min_interval:
            time.sleep(self._min_interval - elapsed)
        self._last_request_time = time.time()

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """
        Search PubMed for literature about a drug-disease pair.

        Args:
            drug: Drug name
            disease: Disease/indication name

        Returns:
            CollectorResult with article data
        """
        query = {"drug": drug, "disease": disease}

        try:
            # Build search query
            search_terms = [f'"{drug}"[Title/Abstract]']
            if disease:
                search_terms.append(f'"{disease}"[Title/Abstract]')

            search_query = " AND ".join(search_terms)

            # Step 1: ESearch to get PMIDs
            pmids = self._esearch(search_query)

            if not pmids:
                return self._make_result(query, [])

            # Step 2: EFetch to get article details
            articles = self._efetch(pmids)

            return self._make_result(query, articles)

        except (URLError, HTTPError) as e:
            return self._make_result(
                query, [], success=False, error_message=str(e)
            )
        except Exception as e:
            return self._make_result(
                query, [], success=False, error_message=f"Unexpected error: {e}"
            )

    def _esearch(self, query: str) -> list[str]:
        """
        Search PubMed and return PMIDs.

        Args:
            query: Search query

        Returns:
            List of PMIDs
        """
        self._rate_limit()

        params = {
            "db": "pubmed",
            "term": query,
            "retmax": self.max_results,
            "retmode": "xml",
            "sort": "relevance",
        }

        if self.api_key:
            params["api_key"] = self.api_key

        url = f"{self.ESEARCH_URL}?{urlencode(params, quote_via=quote)}"
        req = Request(url, headers={"User-Agent": "EuTxGNN-Collector/1.0"})

        with urlopen(req, timeout=30) as response:
            root = ET.fromstring(response.read())

        pmids = [id_elem.text for id_elem in root.findall(".//Id") if id_elem.text]
        return pmids

    def _efetch(self, pmids: list[str]) -> list[dict]:
        """
        Fetch article details for given PMIDs.

        Args:
            pmids: List of PubMed IDs

        Returns:
            List of article dictionaries
        """
        if not pmids:
            return []

        self._rate_limit()

        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "xml",
        }

        if self.api_key:
            params["api_key"] = self.api_key

        url = f"{self.EFETCH_URL}?{urlencode(params)}"
        req = Request(url, headers={"User-Agent": "EuTxGNN-Collector/1.0"})

        with urlopen(req, timeout=60) as response:
            root = ET.fromstring(response.read())

        articles = []
        for article in root.findall(".//PubmedArticle"):
            medline = article.find(".//MedlineCitation")
            if medline is None:
                continue

            pmid = medline.findtext(".//PMID", "")
            article_elem = medline.find(".//Article")
            if article_elem is None:
                continue

            # Extract basic info
            title = article_elem.findtext(".//ArticleTitle", "")
            abstract_texts = article_elem.findall(".//AbstractText")
            abstract = " ".join(
                (t.text or "") + "".join((c.text or "") + (c.tail or "") for c in t)
                for t in abstract_texts
            )

            # Journal info
            journal = article_elem.find(".//Journal")
            journal_name = journal.findtext(".//Title", "") if journal else ""
            pub_date = journal.find(".//PubDate") if journal else None
            year = pub_date.findtext("Year", "") if pub_date is not None else ""

            # Authors
            author_list = article_elem.find(".//AuthorList")
            authors = []
            if author_list is not None:
                for author in author_list.findall("Author"):
                    last_name = author.findtext("LastName", "")
                    fore_name = author.findtext("ForeName", "")
                    if last_name:
                        authors.append(f"{last_name} {fore_name}".strip())

            # Publication types
            pub_types = []
            for pt in article_elem.findall(".//PublicationType"):
                if pt.text:
                    pub_types.append(pt.text)

            # MeSH terms
            mesh_terms = []
            for mesh in medline.findall(".//MeshHeading/DescriptorName"):
                if mesh.text:
                    mesh_terms.append(mesh.text)

            articles.append({
                "pmid": pmid,
                "title": title,
                "abstract": abstract[:1000] if abstract else "",  # Limit length
                "journal": journal_name,
                "year": year,
                "authors": authors[:5],  # Limit to first 5
                "publication_types": pub_types,
                "mesh_terms": mesh_terms[:10],  # Limit to 10
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            })

        return articles

    def classify_article(self, article: dict) -> str:
        """
        Classify article by evidence tier.

        Args:
            article: Article dictionary

        Returns:
            Tier classification ("Tier1", "Tier2", "Tier3")
        """
        pub_types = article.get("publication_types", [])

        # Tier 1: RCTs, systematic reviews, meta-analyses
        for pt in pub_types:
            if any(rct.lower() in pt.lower() for rct in self.RCT_TYPES):
                return "Tier1"
            if any(rev.lower() in pt.lower() for rev in self.REVIEW_TYPES[:2]):  # SR, MA
                return "Tier1"

        # Tier 2: Cohort, case-control, Phase 1-2
        for pt in pub_types:
            if any(obs.lower() in pt.lower() for obs in self.OBSERVATIONAL_TYPES):
                return "Tier2"

        # Tier 3: Everything else
        return "Tier3"

    def evaluate_evidence_level(self, articles: list[dict]) -> str:
        """
        Evaluate evidence level based on literature.

        Args:
            articles: List of article dictionaries

        Returns:
            Evidence level (L1-L5)
        """
        if not articles:
            return "L5"

        tier1_count = sum(1 for a in articles if self.classify_article(a) == "Tier1")
        tier2_count = sum(1 for a in articles if self.classify_article(a) == "Tier2")

        if tier1_count >= 3:
            return "L1"  # Multiple high-quality studies
        elif tier1_count >= 1:
            return "L2"  # At least one RCT/SR
        elif tier2_count >= 3:
            return "L3"  # Multiple observational studies
        elif tier2_count >= 1 or len(articles) >= 3:
            return "L4"  # Some evidence
        else:
            return "L5"  # Minimal evidence
