"""Evidence collectors for EuTxGNN drug repurposing validation."""

from .base import BaseCollector, CollectorResult
from .bundle import BundleAggregator, CandidateInfo, EvidenceBundle
from .clinicaltrials import ClinicalTrialsCollector
from .drug_bundle import (
    CollectionStatus,
    DrugBundle,
    DrugBundleAggregator,
)
from .drugbank import DrugBankCollector
from .ictrp import ICTRPCollector
from .pubmed import PubMedCollector

__all__ = [
    "BaseCollector",
    "CollectorResult",
    "BundleAggregator",
    "CandidateInfo",
    "EvidenceBundle",
    "ClinicalTrialsCollector",
    "CollectionStatus",
    "DrugBundle",
    "DrugBundleAggregator",
    "DrugBankCollector",
    "ICTRPCollector",
    "PubMedCollector",
]
