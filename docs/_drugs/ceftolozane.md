---
layout: default
title: Ceftolozane
description: "Ceftolozane drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 124
evidence_level: L5
indication_count: 50
---

# Ceftolozane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ceftolozane |
| DrugBank ID | [DB09050](https://go.drugbank.com/drugs/DB09050) |
| Brand Names (EU) | Ceftolozane |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.91% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | urinary tract infection (disease) | 99.91% | DL |
| 2 | gonococcal urethritis | 99.89% | DL |
| 3 | Ureaplasma urethritis | 99.89% | DL |
| 4 | uterine inflammatory disease | 99.88% | DL |
| 5 | xanthogranulomatous pyelonephritis | 99.88% | DL |
| 6 | hyperamylasemia | 99.52% | DL |
| 7 | polyclonal hyperviscosity syndrome | 99.52% | DL |
| 8 | urogenital tuberculosis | 99.50% | DL |
| 9 | congenital analbuminemia | 99.44% | DL |
| 10 | blood group incompatibility | 99.22% | DL |
| 11 | premalignant hematological system disease | 99.11% | DL |
| 12 | monoclonal gammopathy | 99.06% | DL |
| 13 | hematological disease associated with an acquired peripheral neuropathy | 98.96% | DL |
| 14 | congenital hematological disorder | 98.59% | DL |
| 15 | septicemic plague | 98.55% | DL |
| 16 | epiglottitis | 98.12% | DL |
| 17 | hematopoietic and lymphoid system neoplasm | 97.58% | DL |
| 18 | pyelitis | 96.42% | DL |
| 19 | laryngitis | 96.40% | DL |
| 20 | abdominal tuberculosis | 95.46% | DL |

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
