---
layout: default
title: Sodium Zirconium Cyclosilicate
description: "Sodium Zirconium Cyclosilicate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 536
evidence_level: L5
indication_count: 50
---

# Sodium Zirconium Cyclosilicate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sodium Zirconium Cyclosilicate |
| DrugBank ID | [DB14048](https://go.drugbank.com/drugs/DB14048) |
| Brand Names (EU) | Lokelma |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 93.41% |

---

## Approved Indication (EMA)

Lokelma is indicated for the treatment of hyperkalaemia in adult patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | breast fibrocystic disease | 93.41% | DL |
| 2 | benign mammary dysplasia | 92.30% | DL |
| 3 | blunt duct adenosis of breast | 91.85% | DL |
| 4 | apocrine adenosis of breast | 91.85% | DL |
| 5 | breast abscess | 90.98% | DL |
| 6 | fat necrosis of breast | 90.98% | DL |
| 7 | lactation disease | 90.79% | DL |
| 8 | breast adenosis | 90.55% | DL |
| 9 | heparin cofactor 2 deficiency | 88.67% | DL |
| 10 | antithrombin deficiency type 2 | 88.55% | DL |
| 11 | bronchitis | 88.54% | DL |
| 12 | factor 5 excess with spontaneous thrombosis | 88.17% | DL |
| 13 | HIV infectious disease | 87.67% | DL |
| 14 | gout | 86.88% | DL |
| 15 | female breast carcinoma | 86.57% | DL |
| 16 | vulvovaginitis | 86.10% | DL |
| 17 | ulceration of vulva | 85.55% | DL |
| 18 | thrombophilia | 85.47% | DL |
| 19 | simian immunodeficiency virus infection | 85.44% | DL |
| 20 | feline acquired immunodeficiency syndrome | 85.44% | DL |

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
