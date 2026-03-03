---
layout: default
title: Norelgestromin
description: "Norelgestromin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 411
evidence_level: L5
indication_count: 50
---

# Norelgestromin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Norelgestromin |
| DrugBank ID | [DB06713](https://go.drugbank.com/drugs/DB06713) |
| Brand Names (EU) | Norelgestromin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.51% |

---

## Approved Indication (EMA)

Female contraception. Evra is intended for women of fertile age. The safety and efficacy has been established in women aged 18 to 45 years.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | amenorrhea (disease) | 99.51% | DL |
| 2 | acne (disease) | 98.49% | DL |
| 3 | breast fibrocystic disease | 97.51% | DL |
| 4 | apocrine adenosis of breast | 96.25% | DL |
| 5 | blunt duct adenosis of breast | 96.25% | DL |
| 6 | benign mammary dysplasia | 95.88% | DL |
| 7 | breast abscess | 95.41% | DL |
| 8 | fat necrosis of breast | 95.41% | DL |
| 9 | lactation disease | 95.21% | DL |
| 10 | primary ovarian failure | 95.12% | DL |
| 11 | breast adenosis | 94.98% | DL |
| 12 | scalp dermatosis | 94.41% | DL |
| 13 | tetragametic chimerism | 93.79% | DL |
| 14 | ovarian remnant syndrome | 93.49% | DL |
| 15 | anovulation | 93.49% | DL |
| 16 | symptomatic form of fragile X syndrome in female carrier | 93.46% | DL |
| 17 | partial trisomy/tetrasomy of the short arm of chromosome 12 | 93.45% | DL |
| 18 | partial trisomy/tetrasomy of the short arm of chromosome 18 | 93.44% | DL |
| 19 | partial trisomy/tetrasomy of the short arm of chromosome 5 | 93.38% | DL |
| 20 | polysomy of X chromosome | 93.25% | DL |

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
