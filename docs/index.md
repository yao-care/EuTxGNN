---
layout: default
title: Home
nav_order: 1
description: "EuTxGNN - AI-powered drug repurposing predictions for EU (EMA) approved drugs using TxGNN"
permalink: /
---

# EuTxGNN
{: .fs-9 }

AI-powered drug repurposing predictions for European Medicines Agency approved drugs
{: .fs-6 .fw-300 }

[View Predictions](/drugs/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[FHIR API](/fhir/metadata){: .btn .fs-5 .mb-4 .mb-md-0 }

---

{: .warning }
> **Research Use Only**: These predictions are for research purposes only and do not constitute medical advice. All candidates require clinical validation before therapeutic application.

---

## Key Statistics

| Metric | Value |
|--------|-------|
| Total Predictions | 32,368 |
| Unique Drugs | 638 |
| Unique Indications | 4,570 |
| KG Predictions | 718 |
| DL Predictions | 31,650 |

---

## Quick Start

### For Researchers

1. Browse [Drug Reports](/drug-reports/) by evidence level
2. Download data from [Downloads](/downloads/)
3. Read the [Methodology](/methodology/)

### For Developers

1. Access [FHIR API](/fhir/metadata) for data integration
2. Launch [SMART App](/smart/launch.html) for EHR integration
3. View source on [GitHub](https://github.com/yao-care/EuTxGNN)

---

## Evidence Levels

| Level | Definition | Count |
|:-----:|------------|-------|
| **L1** | Multiple Phase 3 RCTs | 0 |
| **L2** | Single RCT / Phase 2 | 0 |
| **L3** | Observational studies | 0 |
| **L4** | Preclinical / Case reports | 0 |
| **L5** | AI prediction only | 32,368 |

[View by Evidence Level](/drug-reports/){: .btn .btn-outline }

---

## Data Sources

| Source | Description |
|--------|-------------|
| [EMA Medicines](https://www.ema.europa.eu/) | Centrally authorized human medicines |
| [TxGNN](https://github.com/mims-harvard/TxGNN) | Drug repurposing prediction model |
| [DrugBank](https://go.drugbank.com/) | Drug target and interaction data |

---

## FHIR Integration

EuTxGNN provides FHIR R4 compliant resources:

| Resource | Endpoint |
|----------|----------|
| CapabilityStatement | [`/fhir/metadata`](/fhir/metadata) |
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}` |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}` |

---

## Citation

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

## Disclaimer

This project is for **research purposes only**. The predictions:

- Are not validated through clinical trials
- Should not be used for clinical decision-making
- Require professional medical evaluation before application
- Are provided "as is" without warranty

For medical advice, consult a qualified healthcare professional.
