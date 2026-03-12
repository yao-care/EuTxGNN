---
layout: default
title: Pegfilgrastim
description: "Pegfilgrastim drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 445
evidence_level: L5
indication_count: 50
---

# Pegfilgrastim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pegfilgrastim |
| DrugBank ID | [DB00019](https://go.drugbank.com/drugs/DB00019) |
| Brand Names (EU) | Stimufend |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.89% |

---

## Approved Indication (EMA)

Reduction in the duration of neutropenia and the incidence of febrile neutropenia in adult patients treated with cytotoxic chemotherapy for malignancy (with the exception of chronic myeloid leukaemia and myelodysplastic syndromes).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | severe nonproliferative diabetic retinopathy | 99.89% | DL |
| 2 | diabetic retinopathy | 99.73% | DL |
| 3 | primary release disorder of platelets | 98.37% | DL |
| 4 | diabetic cataract | 98.25% | DL |
| 5 | pseudo-von Willebrand disease | 98.03% | DL |
| 6 | Glanzmann thrombasthenia | 97.69% | DL |
| 7 | drug-induced osteoporosis | 96.75% | DL |
| 8 | senile cataract | 96.37% | DL |
| 9 | nuclear senile cataract | 96.31% | DL |
| 10 | cortical cataract | 96.31% | DL |
| 11 | diabetes mellitus type 2 associated cataract | 95.56% | DL |
| 12 | mature cataract | 95.56% | DL |
| 13 | tetanic cataract | 95.56% | DL |
| 14 | immature cataract | 95.56% | DL |
| 15 | craniostenosis cataract | 95.56% | DL |
| 16 | dermatitis | 93.57% | DL |
| 17 | hemorrhagic disease of newborn | 92.26% | DL |
| 18 | acrodermatitis chronica atrophicans | 91.93% | DL |
| 19 | neonatal dermatomyositis | 91.92% | DL |
| 20 | pityriasis simplex | 91.39% | DL |

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
