---
layout: default
title: Amifampridine Phosphate
description: "Amifampridine Phosphate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 34
evidence_level: L5
indication_count: 50
---

# Amifampridine Phosphate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Amifampridine Phosphate |
| DrugBank ID | [DB11640](https://go.drugbank.com/drugs/DB11640) |
| Brand Names (EU) | Amifampridine SERB |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Symptomatic treatment of Lambert-Eaton myasthenic syndrome (LEMS) in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | glaucoma | 99.71% | DL |
| 2 | acute intermittent porphyria | 99.32% | DL |
| 3 | esophageal varices without bleeding | 98.77% | DL |
| 4 | esophageal varices with bleeding | 98.77% | DL |
| 5 | porphyria | 98.51% | DL |
| 6 | Lambert-Eaton myasthenic syndrome | 98.44% | DL |
| 7 | primary immunodeficiency syndrome due to p14 deficiency | 98.39% | DL |
| 8 | paraneoplastic limbic encephalitis | 98.31% | DL |
| 9 | paraneoplastic polyneuropathy | 98.26% | DL |
| 10 | varicose disease | 98.08% | DL |
| 11 | paraneoplastic cerebellar degeneration | 97.99% | DL |
| 12 | Steel syndrome | 97.71% | DL |
| 13 | Barth syndrome | 97.62% | DL |
| 14 | autosomal dominant keratitis | 97.58% | DL |
| 15 | erythropoietic uroporphyria associated with myeloid malignancy | 97.51% | DL |
| 16 | hereditary photodermatosis | 97.41% | DL |
| 17 | pancreatitis | 97.28% | DL |
| 18 | autosomal dominant Alport syndrome | 96.94% | DL |
| 19 | monilethrix | 96.59% | DL |
| 20 | severe congenital neutropenia | 96.56% | DL |

*Showing top 20 of 50 predictions.*

---

## About TxGNN Predictions

### Prediction Sources

| Source | Description |
|--------|-------------|
| **KG** | Knowledge Graph - Network topology-based associations |
| **DL** | Deep Learning - Neural network score prediction |

### Evidence Levels

| Level | Definition |
|:-----:|------------|
| L1 | Multiple Phase 3 RCTs / Systematic Reviews |
| L2 | Single RCT or multiple Phase 2 trials |
| L3 | Observational studies / Large case series |
| L4 | Preclinical / Mechanistic / Case reports |
| **L5** | AI prediction only (current) |

---

## Clinical Validation Needed

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Research Use Only:</strong> These predictions are computational hypotheses that require clinical validation. They should NOT be used for clinical decision-making.
</div>

### Next Steps for Validation

1. **Literature Review**: Search PubMed for existing evidence
2. **Clinical Trial Search**: Check ClinicalTrials.gov for ongoing studies
3. **Mechanistic Analysis**: Evaluate biological plausibility
4. **Preclinical Studies**: Conduct in vitro/in vivo validation
5. **Clinical Trials**: Design and conduct human studies

---

## Data Access

- **FHIR API**: `/fhir/ClinicalUseDefinition/`
- **CSV Download**: [All Predictions](/downloads/)
- **GitHub**: [yao-care/EuTxGNN](https://github.com/yao-care/EuTxGNN)

---

## Citation

If using this data, please cite:

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

<div style="background: #f8f9fa; padding: 1rem; border-radius: 4px; font-size: 0.9rem;">
<strong>Disclaimer:</strong> This report is for research purposes only and does not constitute medical advice. Drug repurposing predictions require rigorous clinical validation before any therapeutic application.
</div>
