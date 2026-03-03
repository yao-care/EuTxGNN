---
layout: default
title: Tagraxofusp
description: "Tagraxofusp drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 553
evidence_level: L5
indication_count: 51
---

# Tagraxofusp
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tagraxofusp |
| DrugBank ID | [DB14731](https://go.drugbank.com/drugs/DB14731) |
| Brand Names (EU) | Elzonris |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.73% |

---

## Approved Indication (EMA)

Elzonris&nbsp;is indicated as monotherapy for the first-line treatment of adult patients with blastic plasmacytoid dendritic cell neoplasm (BPDCN).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | esotropia | 99.73% | DL |
| 2 | pre-malignant neoplasm | 99.73% | DL |
| 3 | inner ear neoplasm | 99.72% | DL |
| 4 | benign neoplasm of tongue | 99.72% | DL |
| 5 | ductal or ductular proliferation | 99.72% | DL |
| 6 | non-seminomatous lesion | 99.72% | DL |
| 7 | bronchial adenomas/carcinoids childhood | 99.72% | DL |
| 8 | chondroid hamartoma | 99.72% | DL |
| 9 | cystic neoplasm | 99.72% | DL |
| 10 | thyroglossal duct cyst | 99.72% | DL |
| 11 | benign neoplasm of buccal mucosa | 99.72% | DL |
| 12 | cervical neuroblastoma | 99.72% | DL |
| 13 | benign neoplasm of hypopharynx | 99.72% | DL |
| 14 | tumor of testis and paratestis | 99.72% | DL |
| 15 | jugular foramen meningioma | 99.71% | DL |
| 16 | mesenchymoma | 99.71% | DL |
| 17 | HER2 positive breast carcinoma | 99.71% | DL |
| 18 | schwannoma of jugular foramen | 99.71% | DL |
| 19 | neoplasm of major salivary gland | 99.71% | DL |
| 20 | epiglottis neoplasm | 99.71% | DL |

*Showing top 20 of 51 predictions.*

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
