"""Base classes for evidence collectors."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class CollectorResult:
    """Standardized result from a collector."""

    source: str
    query: dict
    data: list[dict]
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    success: bool = True
    error_message: str | None = None
    result_count: int = 0

    def __post_init__(self):
        self.result_count = len(self.data)


class BaseCollector(ABC):
    """Abstract base class for evidence collectors."""

    source_name: str = "base"

    @abstractmethod
    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """
        Search for evidence related to a drug-disease pair.

        Args:
            drug: Drug name (generic or brand name)
            disease: Disease/indication name (optional for drug-only searches)

        Returns:
            CollectorResult with search results
        """
        pass

    def batch_search(
        self, pairs: list[tuple[str, str]], delay: float = 0.5
    ) -> list[CollectorResult]:
        """
        Search for multiple drug-disease pairs.

        Args:
            pairs: List of (drug, disease) tuples
            delay: Delay between requests in seconds

        Returns:
            List of CollectorResults
        """
        import time

        results = []
        for drug, disease in pairs:
            result = self.search(drug, disease)
            results.append(result)
            if delay > 0:
                time.sleep(delay)
        return results

    def _make_result(
        self,
        query: dict,
        data: list[dict],
        success: bool = True,
        error_message: str | None = None,
    ) -> CollectorResult:
        """Create a standardized CollectorResult."""
        return CollectorResult(
            source=self.source_name,
            query=query,
            data=data,
            success=success,
            error_message=error_message,
        )
