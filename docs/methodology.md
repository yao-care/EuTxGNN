---
layout: default
title: Methodology
parent: Documentation
nav_order: 1
description: "EuTxGNN prediction and validation methodology"
permalink: /methodology/
---

# Methodology
{: .fs-9 }

From AI prediction to evidence validation
{: .fs-6 .fw-300 }

---

## Overall Pipeline

```
TxGNN Prediction → Data Collection → Evidence Integration → Report Generation
```

---

## Step 1: TxGNN Prediction

### Model Introduction

TxGNN uses a **knowledge graph** combined with **graph neural networks** for prediction:

1. **Knowledge Graph Construction**
   - 17,080 nodes (drugs, diseases, genes, etc.)
   - Complex inter-node relationships

2. **Graph Neural Network Training**
   - Learns latent associations between nodes
   - Predicts new drug-disease relationships

3. **Prediction Output**
   - Prediction score for each drug-disease pair
   - Higher scores indicate higher confidence

### Prediction Methods

| Method | Description | Predictions |
|--------|-------------|-------------|
| Knowledge Graph (KG) | Network topology-based associations | 718 |
| Deep Learning (DL) | Neural network score prediction | 31,650 |
| **Total** | Merged and deduplicated | **32,368** |

---

## Step 2: Drug Mapping

### EMA to DrugBank Mapping

EMA medicines are mapped to DrugBank identifiers for TxGNN compatibility:

| Step | Description |
|------|-------------|
| 1. Ingredient Extraction | Extract active substances from EMA data |
| 2. Name Normalization | Standardize drug names (remove salts, etc.) |
| 3. DrugBank Lookup | Match against DrugBank vocabulary |
| 4. Manual Review | Verify ambiguous mappings |

### Mapping Statistics

| Metric | Value |
|--------|-------|
| Total EMA Drugs | 1,543 |
| Mapped to DrugBank | 638 |
| Mapping Rate | 41.3% |

---

## Step 3: Disease Mapping

### Indication Extraction

Therapeutic indications from EMA are mapped to standardized disease terms:

1. **MeSH Terms**: EMA provides MeSH therapeutic areas
2. **Text Extraction**: Parse indication text for disease mentions
3. **Vocabulary Matching**: Match against TxGNN disease vocabulary

### Mapping Statistics

| Metric | Value |
|--------|-------|
| Unique Indications | 4,570 |
| Mapped Diseases | ~2,000 |

---

## Step 4: Evidence Levels

### Classification System

| Level | Definition | Clinical Significance |
|:-----:|------------|----------------------|
| **L1** | Multiple Phase 3 RCTs / Systematic Reviews | Strong support |
| **L2** | Single RCT or multiple Phase 2 trials | Moderate support |
| **L3** | Observational studies / Large case series | Preliminary evidence |
| **L4** | Preclinical / Mechanistic studies | Reasonable mechanism |
| **L5** | AI prediction only | Research hypothesis |

---

## Data Sources

| Source | Usage |
|--------|-------|
| EMA Medicines Database | EU approved drugs |
| Article 57 Database | Additional drug data |
| TxGNN Knowledge Graph | Drug-disease predictions |
| DrugBank | Drug identifiers |
| ClinicalTrials.gov | Clinical evidence |
| PubMed | Literature evidence |

---

## Limitations

- Predictions require clinical validation
- Limited to drugs with DrugBank mappings
- Based on TxGNN model trained primarily on US data
- Evidence levels require manual curation

---

## Citation

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023}
}
```
