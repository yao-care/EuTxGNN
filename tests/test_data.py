"""Tests for data loading and processing."""

import pytest
import json
from pathlib import Path


class TestDataFiles:
    """Tests for required data files."""

    @pytest.fixture
    def data_dir(self):
        return Path(__file__).parent.parent / "data"

    def test_node_csv_exists(self, data_dir):
        """Test that TxGNN node.csv exists."""
        node_path = data_dir / "node.csv"
        assert node_path.exists(), "node.csv not found - run: curl -L -o data/node.csv 'https://dataverse.harvard.edu/api/access/datafile/7144482'"

    def test_kg_csv_exists(self, data_dir):
        """Test that TxGNN kg.csv exists."""
        kg_path = data_dir / "kg.csv"
        assert kg_path.exists(), "kg.csv not found - run: curl -L -o data/kg.csv 'https://dataverse.harvard.edu/api/access/datafile/7144484'"

    def test_external_vocab_files(self, data_dir):
        """Test that external vocabulary files exist."""
        external_dir = data_dir / "external"

        required_files = [
            "drugbank_vocab.csv",
            "disease_vocab.csv",
            "drug_disease_relations.csv"
        ]

        for filename in required_files:
            filepath = external_dir / filename
            assert filepath.exists(), f"{filename} not found - run: uv run python scripts/prepare_external_data.py"

    def test_processed_files(self, data_dir):
        """Test that processed data files exist."""
        processed_dir = data_dir / "processed"

        required_files = [
            "eu_integrated_drugs.json",
            "repurposing_candidates.csv",
            "drug_mapping.csv"
        ]

        for filename in required_files:
            filepath = processed_dir / filename
            assert filepath.exists(), f"{filename} not found"

    def test_eu_integrated_drugs_valid_json(self, data_dir):
        """Test that EU integrated drugs file is valid JSON."""
        filepath = data_dir / "processed" / "eu_integrated_drugs.json"

        if filepath.exists():
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)

            assert "metadata" in data
            assert "ema_drugs" in data
            assert isinstance(data["ema_drugs"], list)


class TestConfigFiles:
    """Tests for configuration files."""

    @pytest.fixture
    def config_dir(self):
        return Path(__file__).parent.parent / "config"

    def test_fields_yaml_exists(self, config_dir):
        """Test that fields.yaml exists (not template)."""
        fields_path = config_dir / "fields.yaml"
        assert fields_path.exists(), "fields.yaml not found - copy from fields.yaml.template and configure"

    def test_fields_yaml_not_template(self, config_dir):
        """Test that fields.yaml is configured (not raw template)."""
        import yaml

        fields_path = config_dir / "fields.yaml"
        if fields_path.exists():
            with open(fields_path, encoding="utf-8") as f:
                content = f.read()

            # Should not contain template placeholders
            assert "{Country}" not in content
            assert "TODO:" not in content

            # Should have EU/EMA configuration
            config = yaml.safe_load(content)
            assert config.get("country_code") == "EU"
            assert config.get("regulatory_agency") == "EMA"
