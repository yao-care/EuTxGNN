"""Tests for drug and disease mapping modules."""

import pytest
from pathlib import Path


class TestDrugBankMapper:
    """Tests for DrugBank mapping functionality."""

    def test_import_drugbank_mapper(self):
        """Test that DrugBank mapper functions can be imported."""
        from txgnn.mapping.drugbank_mapper import load_drugbank_vocab, map_ingredient_to_drugbank
        assert load_drugbank_vocab is not None
        assert map_ingredient_to_drugbank is not None

    def test_load_drugbank_vocab(self):
        """Test loading DrugBank vocabulary."""
        from txgnn.mapping.drugbank_mapper import load_drugbank_vocab

        vocab_path = Path(__file__).parent.parent / "data" / "external" / "drugbank_vocab.csv"
        if vocab_path.exists():
            df = load_drugbank_vocab(vocab_path)
            assert df is not None
            assert len(df) > 0


class TestDiseaseMapper:
    """Tests for disease mapping functionality."""

    def test_import_disease_mapper(self):
        """Test that disease mapper functions can be imported."""
        from txgnn.mapping.disease_mapper import extract_indications, translate_indication
        assert extract_indications is not None
        assert translate_indication is not None

    def test_extract_indications_basic(self):
        """Test basic indication extraction."""
        from txgnn.mapping.disease_mapper import extract_indications

        # Test with common disease terms
        text = "Treatment of hypertension and diabetes mellitus"
        indications = extract_indications(text)

        # Should return a list
        assert isinstance(indications, list)


class TestNormalizer:
    """Tests for drug name normalization."""

    def test_import_normalizer(self):
        """Test that normalizer functions can be imported."""
        from txgnn.mapping.normalizer import normalize_ingredient, extract_ingredients
        assert normalize_ingredient is not None
        assert extract_ingredients is not None

    def test_normalize_basic(self):
        """Test basic drug name normalization."""
        from txgnn.mapping.normalizer import normalize_ingredient

        # Test normalization
        result = normalize_ingredient("METFORMIN HYDROCHLORIDE")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_extract_ingredients(self):
        """Test extracting multiple ingredients."""
        from txgnn.mapping.normalizer import extract_ingredients

        result = extract_ingredients("Aspirin; Caffeine")
        assert isinstance(result, list)
