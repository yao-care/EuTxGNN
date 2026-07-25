---
layout: default
title: About
parent: Documentation
nav_order: 3
description: "About the EuTxGNN drug repurposing prediction project"
permalink: /about/
---

# About EuTxGNN

EuTxGNN is a drug repurposing prediction system for European Medicines Agency (EMA) approved drugs, powered by the TxGNN framework.

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

EuTxGNN is the the European Union site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, dual knowledge-graph and
deep-learning prediction, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.

---

## What is Drug Repurposing?

Drug repurposing (also known as drug repositioning) is the process of identifying new therapeutic uses for existing approved drugs. This approach offers several advantages:

- **Reduced Development Time**: Existing drugs have known safety profiles
- **Lower Costs**: Bypasses early-stage development
- **Higher Success Rates**: Known pharmacokinetics and toxicology

---

## The TxGNN Model

TxGNN is a graph neural network model developed for drug repurposing, published in [Nature Medicine (2023)](https://www.nature.com/articles/s41591-023-02233-1).

### Key Features

- **Knowledge Graph Integration**: Combines multiple biomedical databases
- **Graph Neural Networks**: Learns drug-disease relationships from network structure
- **Explainable AI**: Provides interpretable predictions with supporting evidence

---

## EuTxGNN Pipeline

```
EMA Data → Drug Normalization → DrugBank Mapping → TxGNN Prediction → FHIR Output
```

### Data Processing

1. **EMA Medicines Database**: Download authorized human medicines
2. **Article 57 Database**: Additional pharmaceutical product data
3. **Drug Normalization**: Standardize drug names to INN format
4. **DrugBank Mapping**: Map to DrugBank identifiers

### Prediction

1. **Knowledge Graph (KG)**: Network-based association discovery
2. **Deep Learning (DL)**: Neural network score prediction
3. **Evidence Integration**: Combine with clinical trial and literature data

### Output

1. **FHIR Resources**: Standardized clinical data format
2. **Web Interface**: Browse predictions online
3. **SMART App**: EHR integration capability

---

## Data Sources

| Source | Description | Update Frequency |
|--------|-------------|------------------|
| EMA Medicines | Centrally authorized medicines | Daily |
| Article 57 | EU pharmaceutical submissions | Periodic |
| TxGNN KG | Biomedical knowledge graph | Static (2023) |
| DrugBank | Drug database | Periodic |

---

## Technical Stack

- **Python 3.12+**: Core processing
- **TxGNN**: Prediction model
- **FHIR R4**: Clinical data standard
- **Jekyll**: Documentation site
- **GitHub Actions**: CI/CD

---

## Limitations

- Predictions are computational and require clinical validation
- Limited to drugs with DrugBank mappings
- Based on TxGNN model trained on US data
- Not all EMA drugs have sufficient data for prediction

---

## Contact

For questions or feedback, please open an issue on the project repository.

---

## License

This project is for research purposes only. See the repository for license details.
