---
layout: default
title: Glucarpidase
description: "Glucarpidase drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 272
evidence_level: L5
indication_count: 50
---

# Glucarpidase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Glucarpidase |
| DrugBank ID | [DB08898](https://go.drugbank.com/drugs/DB08898) |
| Brand Names (EU) | Voraxaze |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.85% |

---

## Approved Indication (EMA)

Voraxaze is indicated to reduce toxic plasma methotrexate concentration in adults and children (aged 28 days and older) with delayed methotrexate elimination or at risk of methotrexate toxicity.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetic cataract | 99.85% | DL |
| 2 | diabetic retinopathy | 99.84% | DL |
| 3 | craniostenosis cataract | 99.83% | DL |
| 4 | diabetes mellitus type 2 associated cataract | 99.83% | DL |
| 5 | immature cataract | 99.83% | DL |
| 6 | tetanic cataract | 99.83% | DL |
| 7 | mature cataract | 99.83% | DL |
| 8 | cortical cataract | 99.83% | DL |
| 9 | nuclear senile cataract | 99.83% | DL |
| 10 | senile cataract | 99.82% | DL |
| 11 | severe nonproliferative diabetic retinopathy | 99.82% | DL |
| 12 | hemorrhagic disease of newborn | 98.94% | DL |
| 13 | microvascular complications of diabetes, susceptibility to | 98.24% | DL |
| 14 | infiltrating bladder urothelial carcinoma | 98.13% | DL |
| 15 | drug-induced osteoporosis | 98.07% | DL |
| 16 | non-invasive bladder urothelial carcinoma | 98.06% | DL |
| 17 | bladder signet ring cell adenocarcinoma | 98.05% | DL |
| 18 | bladder mixed adenocarcinoma | 98.03% | DL |
| 19 | bladder colonic type adenocarcinoma | 98.03% | DL |
| 20 | bladder colloid adenocarcinoma | 98.03% | DL |

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
