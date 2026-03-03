---
layout: default
title: Carfilzomib
description: "Carfilzomib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 116
evidence_level: L5
indication_count: 50
---

# Carfilzomib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Carfilzomib |
| DrugBank ID | [DB08889](https://go.drugbank.com/drugs/DB08889) |
| Brand Names (EU) | Kyprolis |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.37% |

---

## Approved Indication (EMA)

Kyprolis in combination with daratumumab and dexamethasone, with lenalidomide and dexamethasone, or with dexamethasone alone is indicated for the treatment of adult patients with multiple myeloma who have received at least one prior therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | CMM7 | 99.37% | DL |
| 2 | pediatric leptomeningeal melanoma | 99.30% | DL |
| 3 | epithelioid cell uveal melanoma | 99.23% | DL |
| 4 | vulvar melanoma (disease) | 99.19% | DL |
| 5 | melanoma | 99.03% | DL |
| 6 | indolent plasma cell myeloma | 97.94% | DL |
| 7 | intellectual disability, autosomal dominant 55, with seizures | 97.82% | DL |
| 8 | plasma cell myeloma | 97.44% | DL |
| 9 | myeloid leukemia | 97.01% | DL |
| 10 | neutrophil immunodeficiency syndrome | 95.11% | DL |
| 11 | central nervous system melanocytic neoplasm | 93.29% | DL |
| 12 | ganglioneuroblastoma (disease) | 87.49% | DL |
| 13 | retroperitoneal neoplasm | 86.04% | DL |
| 14 | vertebral anomalies and variable endocrine and T-cell dysfunction | 84.95% | DL |
| 15 | cecum villous adenoma | 83.86% | DL |
| 16 | cecum neuroendocrine tumor G1 | 83.19% | DL |
| 17 | lipoma of colon | 83.14% | DL |
| 18 | cecal disease | 82.92% | DL |
| 19 | rectosigmoid junction neoplasm | 82.91% | DL |
| 20 | benign neoplasm of cecum | 82.68% | DL |

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
