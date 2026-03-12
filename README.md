# EuTxGNN - Drug Repurposing Predictions for EMA-Approved Medicines

[![Website](https://img.shields.io/badge/Website-eutxgnn.yao.care-blue)](https://eutxgnn.yao.care)
[![FHIR R4](https://img.shields.io/badge/FHIR-R4-orange)](https://eutxgnn.yao.care/fhir/metadata)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Drug repurposing predictions for European Medicines Agency (EMA) approved drugs using the [TxGNN](https://www.nature.com/articles/s41591-023-02233-1) knowledge graph framework.

## Disclaimer

- **Research Use Only**: Results are for research purposes only and do not constitute medical advice
- All repurposing candidates require clinical validation before any therapeutic application

## Project Overview

### Prediction Statistics

| Metric | Value |
|--------|-------|
| **Drug Reports** | 642 |
| **Unique Drugs** | 638 |
| **Repurposing Candidates** | 32,368 |
| **FHIR Resources** | 33,000+ |

### Evidence Level Distribution

| Evidence Level | Reports | Description |
|----------------|---------|-------------|
| **L1** | 12 | Multiple Phase 3 RCTs |
| **L2** | 28 | Single RCT or multiple Phase 2 |
| **L3** | 45 | Observational studies |
| **L4** | 89 | Preclinical/mechanistic studies |
| **L5** | 468 | AI prediction only |

---

## Prediction Methods

Following TxGNN's design, two prediction methods are available:

| Method | Speed | Precision | Requirements | Results |
|--------|-------|-----------|--------------|---------|
| Knowledge Graph | Fast (seconds) | Lower | None | [GitHub Release](https://github.com/yao-care/EuTxGNN/releases) |
| Deep Learning | Slow (hours) | Higher | Conda + PyTorch + DGL | On request |

**Key Difference**: The KG method queries known drug-disease relationships; the DL method uses neural networks to infer potential relationships and calculate confidence scores.

### Knowledge Graph Method

```bash
uv run python scripts/run_kg_prediction.py
```

Directly queries drug-disease relationships from the TxGNN knowledge graph.

**Output**: `data/processed/repurposing_candidates.csv`

| Metric | Value |
|--------|-------|
| EMA Total Medicines | 1,847 |
| Active Ingredients Extracted | 892 |
| DrugBank Mapping Rate | 71.5% |
| Disease Mapping Rate | 48.2% |
| Repurposing Candidates | 32,368 |
| Unique Drugs | 638 |
| Potential New Indications | 4,570 |

### Deep Learning Method

```bash
# Requires conda environment with PyTorch + DGL
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

Uses the TxGNN pretrained neural network to calculate prediction scores.

---

## TxGNN Score Interpretation

TxGNN scores represent model confidence in drug-disease associations, ranging from 0 to 1.

### Score Distribution

| Threshold | Predictions | Percentage | Meaning |
|-----------|-------------|------------|---------|
| ≥ 0.9999 | ~500 | 0.002% | Highest confidence, model's strongest predictions |
| ≥ 0.999 | ~2,500 | 0.01% | Very high confidence |
| ≥ 0.99 | ~15,000 | 0.07% | High confidence, worth prioritizing |
| ≥ 0.9 | ~120,000 | 0.6% | Medium-high confidence |

### Choosing a Threshold

```bash
# Only most relevant predictions (highest confidence)
uv run python scripts/regenerate_drug.py metformin --min-score 0.9999

# Balance exploration and precision (recommended)
uv run python scripts/regenerate_drug.py metformin --min-score 0.999 --top-n 0

# Broad exploration (may include noise)
uv run python scripts/regenerate_drug.py metformin --min-score 0.99 --top-n 10
```

### Evidence Level Definitions

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| L1 | Phase 3 RCT or systematic review | Supports clinical use |
| L2 | Phase 2 RCT | Consider for use |
| L3 | Phase 1 or observational study | Evaluate after supplementation |
| L4 | Case report or preclinical | Not recommended yet |
| L5 | AI prediction only, no clinical evidence | Requires further research |

### Important Notes

1. **High score ≠ Clinical efficacy**: TxGNN scores are knowledge graph-based predictions requiring clinical validation
2. **Low score ≠ Ineffective**: The model may not have learned certain associations
3. **Use with verification**: Leverage this project's tools to review clinical trials, literature, and other evidence

---

## Verification Workflow

```bash
# Verify all predictions for a single drug
uv run python scripts/regenerate_drug.py ibuprofen --min-score 0.999

# Validate data pipeline integrity
uv run python scripts/validate_data_pipeline.py --drug ibuprofen
```

### Pipeline Architecture

```
TxGNN Predictions (one drug, multiple indications)
      ↓
┌─────────────────────────────────────┐
│ Step 1: DrugBundle Collector        │
│   Drug level: EMA, DDI, DrugBank    │
│   Indication level: ClinicalTrials, │
│                     PubMed, ICTRP   │
│   → drug_bundle.json                │
├─────────────────────────────────────┤
│ Step 2: Evidence Pack Generator     │
│   Programmatic data transfer (100%) │
│   + LLM analysis (L1-L5 grading)    │
│   → drug_evidence_pack.json/md      │
├─────────────────────────────────────┤
│ Step 3: Report Generator            │
│   → Individual drug report pages    │
│   → FHIR ClinicalUseDefinition      │
└─────────────────────────────────────┘
```

---

## Data Sources

| Source | Description | Usage |
|--------|-------------|-------|
| **EMA Medicines Database** | Centrally authorized human medicines | Drug list, approval status |
| **TxGNN Knowledge Graph** | 17,080 nodes, 80,127 relationships | Drug-disease predictions |
| **DrugBank** | Drug identifiers and synonyms | Identifier mapping |
| **ClinicalTrials.gov** | Clinical trial registry | Evidence collection |
| **PubMed** | Biomedical literature | Literature evidence |
| **ICTRP** | WHO international trials | Additional trial data |

---

## FHIR API

FHIR R4 compliant resources available at `https://eutxgnn.yao.care/fhir/`:

| Endpoint | Description |
|----------|-------------|
| `GET /fhir/metadata` | CapabilityStatement |
| `GET /fhir/MedicationKnowledge/{drug}.json` | Drug information (642 resources) |
| `GET /fhir/ClinicalUseDefinition/{drug}-{disease}.json` | Predictions (32,368 resources) |

### Example

```bash
# Get capability statement
curl https://eutxgnn.yao.care/fhir/metadata

# Get drug information
curl https://eutxgnn.yao.care/fhir/MedicationKnowledge/metformin.json

# Get specific prediction
curl https://eutxgnn.yao.care/fhir/ClinicalUseDefinition/metformin-type-2-diabetes-mellitus.json
```

---

## SMART on FHIR

EuTxGNN provides a SMART on FHIR application for EHR integration:

- **Launch URL**: `https://eutxgnn.yao.care/smart/launch.html`
- **Redirect URL**: `https://eutxgnn.yao.care/smart/app.html`
- **Scopes**: `launch`, `patient/Patient.read`, `patient/MedicationRequest.read`

Test with [SMART App Launcher](https://launch.smarthealthit.org/).

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/yao-care/EuTxGNN.git
cd EuTxGNN

# Install dependencies
uv sync

# Download TxGNN data
mkdir -p data
curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"

# Run prediction pipeline
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py

# Build documentation site locally
cd docs && bundle exec jekyll serve
```

---

## Project Structure

```
EuTxGNN/
├── config/
│   └── fields.yaml              # EMA field mappings
├── data/
│   ├── external/                # DrugBank/disease vocabularies
│   ├── processed/               # Prediction results
│   └── raw/                     # EMA source data
├── docs/
│   ├── _drugs/                  # 642 individual drug reports
│   ├── fhir/                    # FHIR R4 resources (33,000+)
│   ├── smart/                   # SMART on FHIR application
│   └── index.md                 # Documentation homepage
├── scripts/
│   ├── process_fda_data.py      # EMA data processing
│   ├── run_kg_prediction.py     # KG predictions
│   ├── build_drug_reports.py    # Generate drug reports
│   └── generate_fhir_resources.py
├── src/txgnn/
│   ├── collectors/              # Evidence collectors
│   ├── data/                    # Data loaders
│   ├── mapping/                 # Drug/disease mapping
│   └── predict/                 # Prediction models
└── tests/                       # Test suite
```

---

## Deployment

Push to `main` branch triggers automatic deployment:

1. **GitHub Pages**: Documentation site at `eutxgnn.yao.care`
2. **Link Check**: Validates all internal/external links
3. **Evidence Check**: Monitors for new clinical evidence

---

## Related Projects

| Project | Region | Drugs | Link |
|---------|--------|-------|------|
| **TwTxGNN** | Taiwan (TFDA) | 191 | [twtxgnn.yao.care](https://twtxgnn.yao.care) |
| **EuTxGNN** | EU (EMA) | 642 | [eutxgnn.yao.care](https://eutxgnn.yao.care) |

---

## Citation

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-1}
}
```

If you use EuTxGNN in your research, please also cite:

```bibtex
@misc{eutxgnn2026,
  title={EuTxGNN: Drug Repurposing Predictions for EMA-Approved Medicines},
  author={yao.care},
  year={2026},
  url={https://eutxgnn.yao.care}
}
```

---

## License

MIT License - For research purposes only.

---

## Support

- **Documentation**: [eutxgnn.yao.care](https://eutxgnn.yao.care)
- **Issues**: [GitHub Issues](https://github.com/yao-care/EuTxGNN/issues)
- **FHIR API**: [/fhir/metadata](https://eutxgnn.yao.care/fhir/metadata)
