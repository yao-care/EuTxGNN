---
layout: default
title: Sevelamer
description: "Sevelamer drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 526
evidence_level: L5
indication_count: 50
---

# Sevelamer
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sevelamer |
| DrugBank ID | [DB00658](https://go.drugbank.com/drugs/DB00658) |
| Brand Names (EU) | Renagel |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 92.46% |

---

## Approved Indication (EMA)

Renagel is indicated for the control of hyperphosphataemia in adult patients receiving  haemodialysis or peritoneal dialysis. Renagel should be used within the context of a multiple therapeutic approach, which could include calcium supplements, 1,25 - dihydroxy Vitamin D3 or one of its analogues to control the development of renal bone disease.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | breast fibrocystic disease | 92.46% | DL |
| 2 | blunt duct adenosis of breast | 89.91% | DL |
| 3 | apocrine adenosis of breast | 89.91% | DL |
| 4 | benign mammary dysplasia | 88.89% | DL |
| 5 | HIV infectious disease | 87.16% | DL |
| 6 | AIDS | 86.40% | DL |
| 7 | breast abscess | 83.58% | DL |
| 8 | fat necrosis of breast | 83.58% | DL |
| 9 | lactation disease | 83.42% | DL |
| 10 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 83.18% | DL |
| 11 | simian immunodeficiency virus infection | 82.81% | DL |
| 12 | feline acquired immunodeficiency syndrome | 82.81% | DL |
| 13 | breast adenosis | 82.21% | DL |
| 14 | congestive heart failure | 80.22% | DL |
| 15 | AIDS related complex | 79.81% | DL |
| 16 | congenital human immunodeficiency virus | 79.81% | DL |
| 17 | acute pulmonary heart disease | 79.40% | DL |
| 18 | ulceration of vulva | 79.27% | DL |
| 19 | vulvar neoplasm | 78.93% | DL |
| 20 | vulvitis | 77.84% | DL |

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
