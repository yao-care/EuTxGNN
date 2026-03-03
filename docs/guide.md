---
layout: default
title: User Guide
parent: Documentation
nav_order: 2
description: "How to use EuTxGNN drug repurposing reports"
permalink: /guide/
---

# User Guide
{: .fs-9 }

How to read and use EuTxGNN reports
{: .fs-6 .fw-300 }

---

## Quick Start

### 1. Find a Drug of Interest

- Use the **search function** in the navigation
- Or browse the [Drug List](/drugs/)
- Or filter by [Evidence Level](/evidence-high/)

### 2. Check Evidence Level

Each drug-indication pair has an evidence level (L1-L5):

| Level | Meaning | Confidence |
|:-----:|---------|:----------:|
| **L1** | Multiple large RCTs support | ⭐⭐⭐⭐⭐ |
| **L2** | Single RCT or multiple Phase 2 | ⭐⭐⭐⭐ |
| **L3** | Observational studies | ⭐⭐⭐ |
| **L4** | Preclinical/Mechanistic research | ⭐⭐ |
| **L5** | AI prediction only | ⭐ |

### 3. Review the Evidence

Each report contains detailed analysis and supporting data.

---

## Understanding Predictions

### Prediction Score

The TxGNN score (0-1) indicates model confidence:

| Score Range | Interpretation |
|-------------|----------------|
| 0.99+ | Very high confidence |
| 0.90-0.99 | High confidence |
| 0.70-0.90 | Moderate confidence |
| < 0.70 | Lower confidence |

### Source Types

| Source | Description |
|--------|-------------|
| TxGNN Knowledge Graph | Based on network topology |
| TxGNN Deep Learning | Based on neural network |

---

## FHIR Integration

### For Developers

EuTxGNN provides FHIR R4 compliant APIs:

```bash
# Get metadata
curl https://eutxgnn.yao.care/fhir/metadata

# Get specific drug
curl https://eutxgnn.yao.care/fhir/MedicationKnowledge/metformin.json
```

### For SMART Apps

Launch URL: `https://eutxgnn.yao.care/smart/launch.html`

Required scopes:
- `patient/MedicationRequest.read`
- `patient/Patient.read`

---

## Data Export

### CSV Format

Download predictions in CSV format from the [Downloads page](/downloads/).

### JSON Format

FHIR resources are available in JSON format via the API.

---

## Limitations to Consider

1. **Research Only**: Not for clinical decision-making
2. **Validation Required**: All predictions need clinical validation
3. **Coverage**: Limited to EMA-approved drugs with DrugBank mappings
4. **Evidence Levels**: Currently all L5 (AI prediction only)

---

## Frequently Asked Questions

### What is drug repurposing?

Finding new therapeutic uses for existing approved drugs.

### How accurate are the predictions?

TxGNN achieves high performance in validation studies, but predictions should be validated clinically.

### Can I use this for clinical decisions?

No. This is for research purposes only.

### How often is data updated?

Predictions are based on EMA data as of 2026. Updates may be made periodically.

---

## Contact

For questions or feedback, please open an issue on [GitHub](https://github.com/yao-care/EuTxGNN).
