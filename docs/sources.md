---
layout: default
title: Data Sources
parent: Resources
nav_order: 1
description: "EuTxGNN data sources and references"
permalink: /sources/
---

# Data Sources
{: .fs-9 }

Databases and sources used in this project
{: .fs-6 .fw-300 }

---

## Source Overview

| Data Type | Source | Usage |
|-----------|--------|-------|
| AI Predictions | TxGNN | Drug-disease association predictions |
| EU Drug Data | EMA | Approved medicines information |
| Drug Identifiers | DrugBank | Drug mapping and metadata |
| Clinical Trials | ClinicalTrials.gov | Evidence validation |
| Literature | PubMed | Research evidence |

---

## TxGNN Model

### Introduction

TxGNN is a drug repurposing prediction model developed by Professor Marinka Zitnik's team at Harvard Medical School.

### Publication

- **Title**: A foundation model for clinician-centered drug repurposing
- **Journal**: Nature Medicine (2023)
- **DOI**: [10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

### Model Statistics

| Item | Count |
|------|-------|
| Total Nodes | 17,080 |
| Drug Nodes | 4,465 |
| Disease Nodes | 2,870 |
| Known Drug-Disease Relations | 14,573 |

### Data Access

- **Harvard Dataverse**: [TxGNN Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM)
- **GitHub**: [TxGNN Code](https://github.com/mims-harvard/TxGNN)

---

## EMA Medicines Database

### Introduction

The European Medicines Agency provides data on centrally authorized medicines.

### Data Accessed

| Dataset | Description |
|---------|-------------|
| Medicines Output | All authorized human medicines |
| Article 57 Database | Pharmaceutical product submissions |

### Access

- **EMA Website**: [Download Medicine Data](https://www.ema.europa.eu/en/medicines/download-medicine-data)

---

## DrugBank

### Introduction

DrugBank is a comprehensive drug database with detailed drug information.

### Usage in EuTxGNN

- Drug name standardization
- DrugBank ID mapping
- Drug metadata (targets, pathways)

### Access

- **Website**: [DrugBank](https://go.drugbank.com/)
- **License**: Academic use requires registration

---

## ClinicalTrials.gov

### Introduction

Registry of clinical studies conducted around the world.

### Usage in EuTxGNN

- Validating drug-disease associations
- Evidence level determination
- Clinical trial status tracking

### Access

- **Website**: [ClinicalTrials.gov](https://clinicaltrials.gov/)
- **API**: [CTGOV API](https://clinicaltrials.gov/api/)

---

## PubMed

### Introduction

Biomedical literature database from NCBI.

### Usage in EuTxGNN

- Literature evidence for predictions
- Mechanistic support
- Case reports and studies

### Access

- **Website**: [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- **API**: [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/)

---

## Citation

When using EuTxGNN data, please cite:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## License Information

| Source | License |
|--------|---------|
| TxGNN | See original repository |
| EMA Data | Open data |
| DrugBank | Academic license |
| EuTxGNN Generated Data | CC BY 4.0 |
