---
layout: default
title: Plerixafor
description: "plerixafor drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 462
evidence_level: L2
indication_count: 50
---

# Plerixafor
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Plerixafor |
| DrugBank ID | [DB06809](https://go.drugbank.com/drugs/DB06809) |
| Brand Names (EU) | Plerixafor Accord |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Adult patients Plerixafor Accord is indicated in combination with granulocyte-colony stimulating factor (G-CSF) to enhance mobilisation of haematopoietic stem cells to the peripheral blood for collection and subsequent autologous transplantation in adult patients with lymphoma or multiple myeloma whose cells mobilise poorly (see section 4.2). Paediatric patients (1 to less than 18 years) Plerixafor Accord is indicated in combination with G-CSF to enhance mobilisation of haematopoietic stem cells

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | plasma cell myeloma | 99.98% | DL |
| 2 | indolent plasma cell myeloma | 99.97% | DL |
| 3 | CMM7 | 99.34% | DL |
| 4 | pediatric leptomeningeal melanoma | 99.30% | DL |
| 5 | epithelioid cell uveal melanoma | 99.27% | DL |
| 6 | bronchitis | 99.22% | DL |
| 7 | vulvar melanoma (disease) | 99.17% | DL |
| 8 | myeloid leukemia | 99.02% | DL |
| 9 | melanoma | 98.96% | DL |
| 10 | cecum villous adenoma | 98.92% | DL |
| 11 | cecum neuroendocrine tumor G1 | 98.89% | DL |
| 12 | rectosigmoid junction neoplasm | 98.88% | DL |
| 13 | colonic neoplasm | 98.88% | DL |
| 14 | lipoma of colon | 98.88% | DL |
| 15 | cecal disease | 98.87% | DL |
| 16 | colon leiomyoma | 98.86% | DL |
| 17 | benign neoplasm of cecum | 98.84% | DL |
| 18 | colonic lymphangioma | 98.83% | DL |
| 19 | cavernous hemangioma of colon | 98.61% | DL |
| 20 | intellectual disability, autosomal dominant 55, with seizures | 97.84% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| plasma cell myeloma | L2 | 20 | 1 | 1 Phase 3 trial(s), 9 Phase 2 trial(s) |

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
