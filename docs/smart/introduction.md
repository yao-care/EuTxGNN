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
- **{{ site.data.drug_stats.total_drugs }} Drugs**: EMA-approved medications analyzed
- **{{ site.data.drug_stats.total_indications }} Predicted New Indications**: Listed on the drug pages

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
│   ({{ site.data.drug_stats.total_drugs }} drugs)   │
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
│ (drug–disease)  │
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

{% comment %}Counts come from docs/_data/drug_stats.json (scripts/generate_drug_stats.py); do not hard-code them.{% endcomment %}
{% assign lc = site.data.drug_stats.level_counts %}{% assign n_lv = lc.L1 | plus: lc.L2 | plus: lc.L3 | plus: lc.L4 | plus: lc.L5 %}{% assign n_na = site.data.drug_stats.total_drugs | minus: n_lv %}

| Level | Description | Drug Count |
|-------|-------------|-------|
| L1 | Multiple RCTs | {{ lc.L1 }} |
| L2 | Single RCT | {{ lc.L2 }} |
| L3 | Observational | {{ lc.L3 }} |
| L4 | Preclinical | {{ lc.L4 }} |
| L5 | AI Only | {{ lc.L5 }} |
| N/A | [Known uses only (no new prediction)]({{ '/known-uses/' | relative_url }}) | {{ n_na }} |

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
