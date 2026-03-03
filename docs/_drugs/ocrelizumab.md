---
layout: default
title: Ocrelizumab
description: "Ocrelizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 415
evidence_level: L5
indication_count: 50
---

# Ocrelizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ocrelizumab |
| DrugBank ID | [DB11988](https://go.drugbank.com/drugs/DB11988) |
| Brand Names (EU) | Ocrevus |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.89% |

---

## Approved Indication (EMA)

Treatment of adult patients with relapsing forms of multiple sclerosis (RMS) with active disease defined by clinical or imaging features. Treatment of adult patients with early primary progressive multiple sclerosis (PPMS) in terms of disease duration and level of disability, and with imaging features characteristic of inflammatory activity.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HER2 positive breast carcinoma | 99.89% | DL |
| 2 | normal breast-like subtype of breast carcinoma | 99.81% | DL |
| 3 | progesterone-receptor positive breast cancer | 99.81% | DL |
| 4 | breast tumor luminal A or B | 99.81% | DL |
| 5 | progesterone-receptor negative breast cancer | 99.80% | DL |
| 6 | benign neoplasm of tongue | 98.95% | DL |
| 7 | cervical neuroblastoma | 98.93% | DL |
| 8 | benign neoplasm of hypopharynx | 98.92% | DL |
| 9 | schwannoma of jugular foramen | 98.92% | DL |
| 10 | benign neoplasm of buccal mucosa | 98.91% | DL |
| 11 | jugular foramen meningioma | 98.91% | DL |
| 12 | benign neoplasm of salivary gland | 98.90% | DL |
| 13 | inner ear neoplasm | 98.90% | DL |
| 14 | neoplasm of major salivary gland | 98.90% | DL |
| 15 | benign neoplasm of nasal cavity | 98.89% | DL |
| 16 | nasal cavity inverting papilloma | 98.89% | DL |
| 17 | benign neoplasm of floor of mouth | 98.89% | DL |
| 18 | epiglottis neoplasm | 98.89% | DL |
| 19 | benign neoplasm of oral cavity | 98.88% | DL |
| 20 | neoplasm of minor salivary gland | 98.88% | DL |

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
