#!/usr/bin/env python3
"""Generate FHIR R4 resources for EuTxGNN

Generates FHIR format resource files from prediction results.

Usage:
    uv run python scripts/generate_fhir_resources.py

Prerequisites:
    Run run_kg_prediction.py first

Output:
    docs/fhir/metadata
    docs/fhir/MedicationKnowledge/*.json
    docs/fhir/ClinicalUseDefinition/*.json
"""

import json
import re
from pathlib import Path
from datetime import datetime

import pandas as pd


# EU/EMA settings
BASE_URL = "https://eutxgnn.yao.care"

JURISDICTION = {
    "coding": [{
        "system": "urn:iso:std:iso:3166",
        "code": "EU",
        "display": "European Union"
    }]
}


def slugify(text: str) -> str:
    """Convert text to URL-safe slug"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:80]


def generate_capability_statement() -> dict:
    """Generate CapabilityStatement (metadata)"""
    return {
        "resourceType": "CapabilityStatement",
        "id": "eutxgnn-fhir-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": "1.0.0",
        "name": "EuTxGNNFHIRServer",
        "title": "EuTxGNN FHIR Server",
        "status": "active",
        "experimental": True,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "EuTxGNN Project",
        "description": "FHIR R4 server providing EU drug repurposing predictions from TxGNN",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {
                    "type": "MedicationKnowledge",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "code", "type": "token"},
                        {"name": "status", "type": "token"}
                    ]
                },
                {
                    "type": "ClinicalUseDefinition",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "type", "type": "token"},
                        {"name": "subject", "type": "reference"}
                    ]
                }
            ]
        }]
    }


def generate_medication_knowledge(
    drug_id: str,
    drug_name: str,
    brand_name: str,
    drugbank_id: str
) -> dict:
    """Generate MedicationKnowledge resource"""
    slug = slugify(drug_name)
    return {
        "resourceType": "MedicationKnowledge",
        "id": slug,
        "meta": {
            "lastUpdated": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        },
        "status": "active",
        "code": {
            "coding": [
                {
                    "system": "https://www.drugbank.ca/drugs",
                    "code": drugbank_id,
                    "display": drug_name
                },
                {
                    "system": f"{BASE_URL}/drugs",
                    "code": slug,
                    "display": brand_name
                }
            ],
            "text": f"{brand_name} ({drug_name})"
        },
        "intendedJurisdiction": [JURISDICTION],
        "synonym": [brand_name] if brand_name != drug_name else [],
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/ema-product-number",
                "valueString": drug_id
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
                "valueCode": "L5"
            }
        ]
    }


def generate_clinical_use_definition(
    drug_name: str,
    brand_name: str,
    drugbank_id: str,
    indication: str,
    source: str
) -> dict:
    """Generate ClinicalUseDefinition resource"""
    drug_slug = slugify(drug_name)
    indication_slug = slugify(indication)
    resource_id = f"{drug_slug}-{indication_slug}"

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "meta": {
            "lastUpdated": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        },
        "type": "indication",
        "status": "active",
        "subject": [{"reference": f"MedicationKnowledge/{drug_slug}"}],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {
                    "text": indication
                }
            }
        },
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
                "valueCode": "L5"
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/prediction-source",
                "valueString": source
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/drugbank-id",
                "valueString": drugbank_id
            }
        ]
    }


def main():
    print("=" * 60)
    print("Generating FHIR R4 Resources for EuTxGNN")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    fhir_dir = base_dir / "docs" / "fhir"

    # Create directories
    (fhir_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "Bundle").mkdir(parents=True, exist_ok=True)

    # 1. Generate CapabilityStatement
    print("1. Generating CapabilityStatement...")
    metadata = generate_capability_statement()
    with open(fhir_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print("   Created: docs/fhir/metadata")

    # 2. Load prediction results
    print("2. Loading prediction results...")
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"   Error: Cannot find predictions at {candidates_path}")
        print("   Please run run_kg_prediction.py first")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   Loaded {len(candidates)} predictions")

    # 3. Generate MedicationKnowledge
    print("3. Generating MedicationKnowledge resources...")
    drugs_df = candidates[['license_id', 'brand_name', 'ingredient', 'drugbank_id']].drop_duplicates()
    drug_count = 0

    for _, row in drugs_df.iterrows():
        drug_id = row.get('license_id', '')
        brand_name = row.get('brand_name', '')
        ingredient = row.get('ingredient', '')
        drugbank_id = row.get('drugbank_id', '')

        if not ingredient or pd.isna(ingredient):
            continue

        resource = generate_medication_knowledge(
            drug_id=drug_id,
            drug_name=ingredient,
            brand_name=brand_name,
            drugbank_id=drugbank_id
        )
        slug = slugify(ingredient)
        filepath = fhir_dir / "MedicationKnowledge" / f"{slug}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        drug_count += 1

    print(f"   Created {drug_count} MedicationKnowledge resources")

    # 4. Generate ClinicalUseDefinition
    print("4. Generating ClinicalUseDefinition resources...")
    cud_count = 0

    for _, row in candidates.iterrows():
        ingredient = row.get('ingredient', '')
        brand_name = row.get('brand_name', '')
        drugbank_id = row.get('drugbank_id', '')
        indication = row.get('potential_indication', '')
        source = row.get('source', 'TxGNN Knowledge Graph')

        if not ingredient or not indication:
            continue
        if pd.isna(ingredient) or pd.isna(indication):
            continue

        resource = generate_clinical_use_definition(
            drug_name=ingredient,
            brand_name=brand_name,
            drugbank_id=drugbank_id,
            indication=indication,
            source=source
        )
        drug_slug = slugify(ingredient)
        indication_slug = slugify(indication)
        filename = f"{drug_slug}-{indication_slug}.json"
        filepath = fhir_dir / "ClinicalUseDefinition" / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        cud_count += 1

    print(f"   Created {cud_count} ClinicalUseDefinition resources")

    # 5. Summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  FHIR resources directory: {fhir_dir}")
    print(f"  CapabilityStatement:      1")
    print(f"  MedicationKnowledge:      {drug_count}")
    print(f"  ClinicalUseDefinition:    {cud_count}")
    print()
    print("Done!")


if __name__ == "__main__":
    main()
