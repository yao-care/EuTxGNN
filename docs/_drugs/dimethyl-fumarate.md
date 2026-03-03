---
layout: default
title: Dimethyl Fumarate
description: "Dimethyl Fumarate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 175
evidence_level: L5
indication_count: 50
---

# Dimethyl Fumarate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dimethyl Fumarate |
| DrugBank ID | [DB08908](https://go.drugbank.com/drugs/DB08908) |
| Brand Names (EU) | Tecfidera |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.76% |

---

## Approved Indication (EMA)

Tecfidera is indicated for the treatment of adult and paediatric patients aged 13 years and older with relapsing remitting multiple sclerosis (RRMS).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | relapsing-remitting multiple sclerosis | 98.76% | DL |
| 2 | progressive multiple sclerosis | 90.67% | DL |
| 3 | schwannoma of jugular foramen | 89.67% | DL |
| 4 | cervical neuroblastoma | 89.67% | DL |
| 5 | benign neoplasm of buccal mucosa | 89.44% | DL |
| 6 | jugular foramen meningioma | 89.31% | DL |
| 7 | benign neoplasm of tongue | 89.27% | DL |
| 8 | benign neoplasm of hypopharynx | 89.26% | DL |
| 9 | inner ear neoplasm | 89.23% | DL |
| 10 | benign neoplasm of floor of mouth | 89.19% | DL |
| 11 | nasal cavity inverting papilloma | 89.07% | DL |
| 12 | epiglottis neoplasm | 89.06% | DL |
| 13 | benign neoplasm of nasal cavity | 89.04% | DL |
| 14 | neoplasm of major salivary gland | 89.02% | DL |
| 15 | vestibulocochlear nerve neoplasm | 89.00% | DL |
| 16 | skull base neoplasm | 89.00% | DL |
| 17 | benign neoplasm of salivary gland | 88.93% | DL |
| 18 | benign neoplasm of oral cavity | 88.92% | DL |
| 19 | abducens nerve neoplasm | 88.84% | DL |
| 20 | cystic neoplasm | 88.79% | DL |

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
