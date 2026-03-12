---
layout: default
title: Project Introduction
parent: 🏥 SMART on FHIR
nav_order: 7
description: "EuTxGNN Project Introduction for international audiences"
permalink: /smart/introduction/
---

# Project Introduction
{: .fs-9 }

EuTxGNN: AI-Powered Drug Repurposing for Europe
{: .fs-6 .fw-300 }

---

## What is EuTxGNN?

EuTxGNN (European TxGNN) is a drug repurposing prediction platform that uses the Harvard TxGNN model to identify potential new therapeutic uses for EMA-approved medications.

---

## Mission

To accelerate drug repurposing research by:

1. **Predicting** new therapeutic uses using AI
2. **Validating** predictions with clinical evidence
3. **Sharing** results via FHIR-compliant APIs
4. **Enabling** integration with healthcare systems

---

## Key Features

### AI-Powered Predictions

- **TxGNN Model**: Graph neural network trained on biomedical knowledge
- **642 Drugs**: EMA-approved medications analyzed
- **32,368 Predictions**: Potential new therapeutic uses

### Evidence Integration

- **ClinicalTrials.gov**: Active clinical trial data
- **PubMed**: Scientific literature evidence
- **DrugBank**: Drug interaction data

### Healthcare Integration

- **FHIR R4**: Standardized healthcare data
- **SMART on FHIR**: EHR-integrated application
- **Open API**: Free research access

---

## How It Works

```
┌─────────────────┐
│   EMA Drugs     │
│   (642 drugs)   │
└────────┬────────┘
         ↓
┌─────────────────┐
│   TxGNN Model   │
│   (Knowledge    │
│    Graph + GNN) │
└────────┬────────┘
         ↓
┌─────────────────┐
│   Predictions   │
│  (32,368 pairs) │
└────────┬────────┘
         ↓
┌─────────────────┐
│   Evidence      │
│   Collection    │
└────────┬────────┘
         ↓
┌─────────────────┐
│   FHIR API +    │
│   Drug Reports  │
└─────────────────┘
```

---

## Evidence Levels

| Level | Description | Count |
|-------|-------------|-------|
| L1 | Multiple RCTs | 12 |
| L2 | Single RCT | 28 |
| L3 | Observational | 45 |
| L4 | Preclinical | 89 |
| L5 | AI Only | 468 |

---

## Use Cases

### Researchers

- Identify repurposing candidates for specific diseases
- Access FHIR-formatted prediction data
- Download bulk datasets for analysis

### Clinicians

- Review repurposing evidence for patient medications
- Access via SMART on FHIR in EHR
- Explore potential off-label uses

### Healthcare IT

- Integrate predictions into clinical systems
- Build custom applications using FHIR API
- Implement clinical decision support

---

## Related Projects

| Project | Region | Focus |
|---------|--------|-------|
| [TwTxGNN](https://twtxgnn.yao.care) | Taiwan | TFDA drugs |
| **EuTxGNN** | Europe | EMA drugs |

---

## Getting Started

1. **Browse**: [Drug Reports](/drugs/)
2. **Search**: [Homepage Search](/)
3. **API**: [FHIR Specification](/smart/fhir-api/)
4. **Integrate**: [SMART on FHIR](/smart/)

---

## Citation

```bibtex
@misc{eutxgnn2026,
  title={EuTxGNN: Drug Repurposing Predictions for EMA-Approved Medicines},
  author={yao.care},
  year={2026},
  url={https://eutxgnn.yao.care}
}
```

---

## Contact

- **GitHub**: [yao-care/EuTxGNN](https://github.com/yao-care/EuTxGNN)
- **Issues**: [Report a bug](https://github.com/yao-care/EuTxGNN/issues)
