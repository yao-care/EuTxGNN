---
layout: default
title: Tazobactam
description: "Tazobactam drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 558
evidence_level: L5
indication_count: 50
---

# Tazobactam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tazobactam |
| DrugBank ID | [DB01606](https://go.drugbank.com/drugs/DB01606) |
| Brand Names (EU) | Tazobactam |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.46% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pneumonia | 99.46% | DL |
| 2 | urinary tract infection (disease) | 99.12% | DL |
| 3 | Ureaplasma urethritis | 98.99% | DL |
| 4 | gonococcal urethritis | 98.99% | DL |
| 5 | bacterial arthritis | 98.79% | DL |
| 6 | uterine inflammatory disease | 98.66% | DL |
| 7 | xanthogranulomatous pyelonephritis | 98.62% | DL |
| 8 | staphylococcus aureus infection | 98.25% | DL |
| 9 | appendicitis | 95.37% | DL |
| 10 | urogenital tuberculosis | 94.94% | DL |
| 11 | streptococcal pneumonia | 94.75% | DL |
| 12 | pyelonephritis | 93.77% | DL |
| 13 | epiglottitis | 92.67% | DL |
| 14 | bronchitis | 92.44% | DL |
| 15 | pyelitis | 92.20% | DL |
| 16 | hyperamylasemia | 92.04% | DL |
| 17 | polyclonal hyperviscosity syndrome | 92.04% | DL |
| 18 | congenital analbuminemia | 90.82% | DL |
| 19 | blood group incompatibility | 89.09% | DL |
| 20 | premalignant hematological system disease | 88.12% | DL |

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
