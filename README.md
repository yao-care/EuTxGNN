# EuTxGNN

EU (EMA) drug repurposing predictions using TxGNN knowledge graph and deep learning.

## Overview

EuTxGNN predicts potential new therapeutic uses for European Medicines Agency (EMA) approved drugs using the [TxGNN](https://www.nature.com/articles/s41591-023-02233-1) framework.

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Predictions | 32,368 |
| Unique Drugs | 638 |
| Unique Indications | 4,570 |
| FHIR Resources | 33,000+ |

## Quick Start

```bash
# Install dependencies
uv sync

# Run predictions (if not already done)
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/merge_predictions.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py

# Run tests
uv run pytest tests/ -v
```

## Project Structure

```
EuTxGNN/
├── config/
│   └── fields.yaml          # EMA field mappings
├── data/
│   ├── external/             # DrugBank/disease vocabularies
│   ├── processed/            # Prediction results
│   └── raw/                  # EMA source data
├── docs/
│   ├── fhir/                 # FHIR R4 resources
│   ├── smart/                # SMART on FHIR app
│   └── index.md              # Documentation site
├── scripts/
│   ├── process_fda_data.py   # EMA data processing
│   ├── run_kg_prediction.py  # KG predictions
│   ├── merge_predictions.py  # Merge KG + DL results
│   └── generate_fhir_resources.py
├── src/txgnn/
│   ├── collectors/           # Evidence collectors
│   ├── data/                 # Data loaders
│   ├── mapping/              # Drug/disease mapping
│   └── predict/              # Prediction models
└── tests/                    # Test suite
```

## Data Sources

- **EMA Medicines Database**: Centrally authorized human medicines
- **Article 57 Database**: EU pharmaceutical submissions
- **TxGNN Knowledge Graph**: Drug-disease relationships
- **DrugBank**: Drug identifiers and synonyms

## FHIR API

FHIR R4 compliant resources available at `/fhir/`:

- `GET /fhir/metadata` - CapabilityStatement
- `GET /fhir/MedicationKnowledge/{id}` - Drug information
- `GET /fhir/ClinicalUseDefinition/{id}` - Repurposing predictions

## Deployment

Push to `main` branch triggers GitHub Pages deployment via `.github/workflows/pages.yml`.

## Disclaimer

**Research Use Only**: These predictions are for research purposes only and do not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.

## Citation

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023}
}
```

## License

For research purposes only.
