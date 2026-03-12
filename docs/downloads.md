---
layout: default
title: Downloads
parent: Resources
nav_order: 2
description: "Download EuTxGNN drug repurposing prediction data including evidence summaries and complete datasets."
permalink: /downloads/
---

# Data Downloads

Open data for research use under CC BY 4.0 license.

---

## Quick Downloads

### Summary Data

| File | Format | Description |
|------|--------|-------------|
| [Drug Mapping](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/drug_mapping.csv) | CSV | DrugBank mapping for 638 drugs |
| [Predictions](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/repurposing_candidates.csv) | CSV | All 32,368 predictions |
| [Indication Mapping](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/indication_mapping.csv) | CSV | Disease mapping results |

### Complete Dataset

<p style="margin: 1.5rem 0;">
  <a href="https://github.com/yao-care/EuTxGNN/tree/main/data/processed" target="_blank" rel="noopener" style="display: inline-block; padding: 0.75rem 1.5rem; background: #24292e; color: white; text-decoration: none; border-radius: 4px; font-weight: 600;">
    Browse All Data on GitHub
  </a>
</p>

---

## Data Schema

### repurposing_candidates.csv

| Column | Description |
|--------|-------------|
| `license_id` | EMA product number |
| `brand_name` | Commercial name |
| `ingredient` | Active substance (INN) |
| `drugbank_id` | DrugBank identifier |
| `potential_indication` | Predicted indication |
| `source` | Prediction source (KG or DL) |
| `score` | Prediction confidence (0-1) |

### drug_mapping.csv

| Column | Description |
|--------|-------------|
| `ingredient` | Active substance name |
| `drugbank_id` | Mapped DrugBank ID |
| `drugbank_name` | DrugBank drug name |
| `match_type` | Mapping method used |

---

## FHIR Resources

FHIR R4 resources are available at:

| Resource | Endpoint | Count |
|----------|----------|-------|
| CapabilityStatement | [/fhir/metadata](/fhir/metadata) | 1 |
| MedicationKnowledge | /fhir/MedicationKnowledge/ | 733 |
| ClinicalUseDefinition | /fhir/ClinicalUseDefinition/ | 32,368 |

---

## External Data Sources

These datasets were used to build EuTxGNN:

| Source | URL |
|--------|-----|
| TxGNN Knowledge Graph | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) |
| EMA Medicines Database | [EMA Website](https://www.ema.europa.eu/en/medicines/download-medicine-data) |
| DrugBank | [DrugBank](https://go.drugbank.com/) |

---

## Citation

When using this data, please cite:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023}
}
```

---

## License

All EuTxGNN generated data is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Original TxGNN data is subject to its own license terms.
