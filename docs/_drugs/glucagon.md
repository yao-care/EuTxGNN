---
layout: default
title: Glucagon
description: "Glucagon drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 271
evidence_level: L5
indication_count: 50
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Glucagon |
| DrugBank ID | [DB00040](https://go.drugbank.com/drugs/DB00040) |
| Brand Names (EU) | Baqsimi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.24% |

---

## Approved Indication (EMA)

Baqsimi is indicated for the treatment of severe hypoglycaemia in adults, adolescents, and children aged 4 years and over with diabetes mellitus.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | irritable bowel syndrome | 99.24% | DL |
| 2 | cauda equina syndrome | 98.78% | DL |
| 3 | obsolete neurogenic bladder (disease) | 97.28% | DL |
| 4 | acute laryngopharyngitis | 94.48% | DL |
| 5 | nasal cavity disease | 94.31% | DL |
| 6 | pharyngitis | 93.78% | DL |
| 7 | primary hereditary glaucoma | 91.02% | DL |
| 8 | open-angle glaucoma | 90.16% | DL |
| 9 | filariasis | 90.01% | DL |
| 10 | large intestine disease | 89.86% | DL |
| 11 | small intestine disease | 89.22% | DL |
| 12 | obsolete rare pulmonary disease | 89.21% | DL |
| 13 | gastroenteritis | 89.18% | DL |
| 14 | pulmonary edema | 88.08% | DL |
| 15 | dermatitis | 86.29% | DL |
| 16 | esotropia | 86.00% | DL |
| 17 | pityriasis simplex | 85.03% | DL |
| 18 | seborrheic dermatitis | 84.87% | DL |
| 19 | acrodermatitis chronica atrophicans | 84.22% | DL |
| 20 | rhinitis | 84.00% | DL |

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
