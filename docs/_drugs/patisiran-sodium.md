---
layout: default
title: Patisiran Sodium
description: "Patisiran Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 442
evidence_level: L5
indication_count: 50
---

# Patisiran Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Patisiran Sodium |
| DrugBank ID | [DB14582](https://go.drugbank.com/drugs/DB14582) |
| Brand Names (EU) | Onpattro |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 90.65% |

---

## Approved Indication (EMA)

Onpattro is indicated for the treatment of hereditary transthyretin-mediated amyloidosis (hATTR amyloidosis) in adult patients with stage 1 or stage 2 polyneuropathy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatitis | 90.65% | DL |
| 2 | hydroa vacciniforme, familial | 90.08% | DL |
| 3 | amyopathic dermatomyositis | 90.07% | DL |
| 4 | acne keloid | 90.04% | DL |
| 5 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 90.01% | DL |
| 6 | neonatal dermatomyositis | 89.92% | DL |
| 7 | acrodermatitis chronica atrophicans | 89.14% | DL |
| 8 | Smouldering systemic mastocytosis | 85.13% | DL |
| 9 | overactive bladder (disease) | 84.90% | DL |
| 10 | lymphoadenopathic mastocytosis with eosinophilia | 84.62% | DL |
| 11 | systemic mastocytosis | 84.61% | DL |
| 12 | angioedema | 84.01% | DL |
| 13 | gastrin secretion abnormality | 83.02% | DL |
| 14 | low compliance bladder | 81.08% | DL |
| 15 | hepatic infarction | 79.63% | DL |
| 16 | HER2 positive breast carcinoma | 79.19% | DL |
| 17 | peliosis hepatis | 79.18% | DL |
| 18 | hepatic veno-occlusive disease | 79.01% | DL |
| 19 | bladder neck obstruction | 78.55% | DL |
| 20 | mixed-type autoimmune hemolytic anemia | 78.44% | DL |

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
