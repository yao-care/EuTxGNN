---
layout: default
title: Pegvaliase
description: "Pegvaliase drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 448
evidence_level: L5
indication_count: 50
---

# Pegvaliase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pegvaliase |
| DrugBank ID | [DB12839](https://go.drugbank.com/drugs/DB12839) |
| Brand Names (EU) | Palynziq |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.17% |

---

## Approved Indication (EMA)

Palynziq is indicated for the treatment of patients with phenylketonuria (PKU) aged 16 years and older who have inadequate blood phenylalanine control (blood phenylalanine levels greater than 600 micromol/l) despite prior management with available treatment options.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetic retinopathy | 99.17% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 99.16% | DL |
| 3 | diabetic cataract | 99.11% | DL |
| 4 | nuclear senile cataract | 98.97% | DL |
| 5 | cortical cataract | 98.97% | DL |
| 6 | diabetes mellitus type 2 associated cataract | 98.96% | DL |
| 7 | craniostenosis cataract | 98.96% | DL |
| 8 | tetanic cataract | 98.96% | DL |
| 9 | mature cataract | 98.96% | DL |
| 10 | immature cataract | 98.96% | DL |
| 11 | senile cataract | 98.94% | DL |
| 12 | bronchitis | 97.28% | DL |
| 13 | microvascular complications of diabetes, susceptibility to | 93.99% | DL |
| 14 | bronchial neoplasm (disease) | 93.75% | DL |
| 15 | idiopathic bronchiectasis | 92.46% | DL |
| 16 | infective urethral stricture | 92.36% | DL |
| 17 | hemorrhagic disease of newborn | 92.32% | DL |
| 18 | Chagas cardiomyopathy | 91.96% | DL |
| 19 | post-bacterial disorder | 91.91% | DL |
| 20 | postinfectious vasculitis | 91.88% | DL |

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
