---
layout: default
title: Risdiplam
description: "Risdiplam drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 498
evidence_level: L5
indication_count: 50
---

# Risdiplam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Risdiplam |
| DrugBank ID | [DB15305](https://go.drugbank.com/drugs/DB15305) |
| Brand Names (EU) | Evrysdi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.45% |

---

## Approved Indication (EMA)

Evrysdi is indicated for the treatment of 5q spinal muscular atrophy (SMA) in patients with a clinical diagnosis of SMA Type 1, Type 2 or Type 3 or with one to four SMN2 copies. &nbsp;

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acne (disease) | 99.45% | DL |
| 2 | drug-induced osteoporosis | 97.72% | DL |
| 3 | zinc, elevated plasma | 97.32% | DL |
| 4 | common wart | 97.21% | DL |
| 5 | metastatic melanoma | 96.84% | DL |
| 6 | dermatitis | 96.62% | DL |
| 7 | non-cutaneous melanoma | 96.18% | DL |
| 8 | acrodermatitis chronica atrophicans | 96.11% | DL |
| 9 | epithelioid cell melanoma | 95.93% | DL |
| 10 | eyelid melanoma | 95.88% | DL |
| 11 | scrotum melanoma | 95.75% | DL |
| 12 | neonatal dermatomyositis | 95.74% | DL |
| 13 | multiple endocrine neoplasia | 95.58% | DL |
| 14 | choroideremia | 95.51% | DL |
| 15 | acne keloid | 95.40% | DL |
| 16 | CDK4 linked melanoma | 95.39% | DL |
| 17 | superficial spreading melanoma | 95.39% | DL |
| 18 | malignant melanoma of the mucosa | 95.39% | DL |
| 19 | nodular malignant melanoma | 95.39% | DL |
| 20 | amelanotic skin melanoma | 95.39% | DL |

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
