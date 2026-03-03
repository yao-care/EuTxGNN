"""Tests for FHIR resource generation."""

import pytest
import json
from pathlib import Path


class TestFHIRResources:
    """Tests for generated FHIR resources."""

    @pytest.fixture
    def fhir_dir(self):
        return Path(__file__).parent.parent / "docs" / "fhir"

    def test_metadata_exists(self, fhir_dir):
        """Test that FHIR metadata (CapabilityStatement) exists."""
        metadata_path = fhir_dir / "metadata"
        assert metadata_path.exists(), "FHIR metadata not found - run: uv run python scripts/generate_fhir_resources.py"

    def test_metadata_valid_json(self, fhir_dir):
        """Test that metadata is valid FHIR CapabilityStatement."""
        metadata_path = fhir_dir / "metadata"

        if metadata_path.exists():
            with open(metadata_path, encoding="utf-8") as f:
                data = json.load(f)

            assert data.get("resourceType") == "CapabilityStatement"
            assert data.get("fhirVersion") == "4.0.1"
            assert data.get("status") == "active"

    def test_medication_knowledge_dir_exists(self, fhir_dir):
        """Test that MedicationKnowledge directory exists."""
        mk_dir = fhir_dir / "MedicationKnowledge"
        assert mk_dir.exists(), "MedicationKnowledge directory not found"

    def test_medication_knowledge_has_resources(self, fhir_dir):
        """Test that MedicationKnowledge resources were generated."""
        mk_dir = fhir_dir / "MedicationKnowledge"

        if mk_dir.exists():
            json_files = list(mk_dir.glob("*.json"))
            assert len(json_files) > 0, "No MedicationKnowledge resources found"

    def test_clinical_use_definition_dir_exists(self, fhir_dir):
        """Test that ClinicalUseDefinition directory exists."""
        cud_dir = fhir_dir / "ClinicalUseDefinition"
        assert cud_dir.exists(), "ClinicalUseDefinition directory not found"

    def test_clinical_use_definition_has_resources(self, fhir_dir):
        """Test that ClinicalUseDefinition resources were generated."""
        cud_dir = fhir_dir / "ClinicalUseDefinition"

        if cud_dir.exists():
            json_files = list(cud_dir.glob("*.json"))
            assert len(json_files) > 0, "No ClinicalUseDefinition resources found"

    def test_sample_medication_knowledge_valid(self, fhir_dir):
        """Test that a sample MedicationKnowledge resource is valid."""
        mk_dir = fhir_dir / "MedicationKnowledge"

        if mk_dir.exists():
            json_files = list(mk_dir.glob("*.json"))
            if json_files:
                with open(json_files[0], encoding="utf-8") as f:
                    data = json.load(f)

                assert data.get("resourceType") == "MedicationKnowledge"
                assert "code" in data
                assert "status" in data

    def test_sample_clinical_use_definition_valid(self, fhir_dir):
        """Test that a sample ClinicalUseDefinition resource is valid."""
        cud_dir = fhir_dir / "ClinicalUseDefinition"

        if cud_dir.exists():
            json_files = list(cud_dir.glob("*.json"))
            if json_files:
                with open(json_files[0], encoding="utf-8") as f:
                    data = json.load(f)

                assert data.get("resourceType") == "ClinicalUseDefinition"
                assert data.get("type") == "indication"
                assert "subject" in data
