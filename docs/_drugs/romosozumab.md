---
layout: default
title: Romosozumab
description: "Romosozumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 506
evidence_level: L5
indication_count: 50
---

# Romosozumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Romosozumab |
| DrugBank ID | [DB11866](https://go.drugbank.com/drugs/DB11866) |
| Brand Names (EU) | Evenity |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.46% |

---

## Approved Indication (EMA)

Evenity is indicated in treatment of severe osteoporosis in postmenopausal women at high risk of fracture.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | phosphorus metabolism disease | 99.46% | DL |
| 2 | hypercalcemia disease | 98.33% | DL |
| 3 | obsolete vitamin D deficiency | 97.83% | DL |
| 4 | nephrocalcinosis | 97.50% | DL |
| 5 | calcium-alkali syndrome | 97.44% | DL |
| 6 | primary bone dysplasia with defective bone mineralization | 97.27% | DL |
| 7 | postmenopausal osteoporosis | 95.92% | DL |
| 8 | severe nonproliferative diabetic retinopathy | 95.01% | DL |
| 9 | osteoporosis | 94.90% | DL |
| 10 | renal osteodystrophy | 94.28% | DL |
| 11 | osteomalacia (disease) | 93.47% | DL |
| 12 | pregnancy associated osteoporosis | 92.86% | DL |
| 13 | autosomal dominant neovascular inflammatory vitreoretinopathy | 92.43% | DL |
| 14 | Worth syndrome | 92.37% | DL |
| 15 | impaired renal function disease | 91.50% | DL |
| 16 | succinyl-CoA:3-ketoacid CoA transferase deficiency | 91.11% | DL |
| 17 | hypophosphatemic rickets | 89.63% | DL |
| 18 | non-renal secondary hyperparathyroidism | 89.54% | DL |
| 19 | bone remodeling disease | 88.92% | DL |
| 20 | hereditary hypophosphatemic rickets | 88.54% | DL |

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
