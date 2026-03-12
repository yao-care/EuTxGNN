---
layout: default
title: Urea (13C)
description: "Urea (13C) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 617
evidence_level: L5
indication_count: 50
---

# Urea (13C)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Urea (13C) |
| DrugBank ID | [DB03904](https://go.drugbank.com/drugs/DB03904) |
| Brand Names (EU) | Pylobactell |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.61% |

---

## Approved Indication (EMA)

This medicinal product is for diagnostic use only. For in vivo diagnosis of gastroduodenal Helicobacter pylori (H. pylori) infection.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | exanthem (disease) | 99.61% | DL |
| 2 | dermatitis | 98.21% | DL |
| 3 | seborrheic dermatitis | 97.64% | DL |
| 4 | acne keloid | 97.55% | DL |
| 5 | neonatal dermatomyositis | 97.48% | DL |
| 6 | acrodermatitis chronica atrophicans | 97.42% | DL |
| 7 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 97.15% | DL |
| 8 | amyopathic dermatomyositis | 97.12% | DL |
| 9 | hydroa vacciniforme, familial | 96.61% | DL |
| 10 | acne (disease) | 95.53% | DL |
| 11 | dermatitis, atopic | 91.27% | DL |
| 12 | seborrheic keratosis | 90.06% | DL |
| 13 | vulvar inverted follicular keratosis | 86.78% | DL |
| 14 | familial pityriasis rubra pilaris | 75.40% | DL |
| 15 | familial acanthosis nigricans | 75.29% | DL |
| 16 | urticaria, familial localized heat | 74.40% | DL |
| 17 | pityriasis simplex | 73.52% | DL |
| 18 | X-linked keloid scarring-reduced joint mobility-increased optic cup-to-disc ratio syndrome | 72.62% | DL |
| 19 | severe dermatitis-multiple allergies-metabolic wasting syndrome | 72.62% | DL |
| 20 | van den Bosch syndrome | 72.35% | DL |

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
