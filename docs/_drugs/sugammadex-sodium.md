---
layout: default
title: Sugammadex Sodium
description: "Sugammadex Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 546
evidence_level: L5
indication_count: 50
---

# Sugammadex Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sugammadex Sodium |
| DrugBank ID | [DB06206](https://go.drugbank.com/drugs/DB06206) |
| Brand Names (EU) | Sugammadex Fresenius Kabi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.49% |

---

## Approved Indication (EMA)

Reversal of neuromuscular blockade induced by rocuronium or vecuronium in adults. For the paediatric population: sugammadex is only recommended for routine reversal of rocuronium induced blockade in children and adolescents aged 2 to 17 years.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | breast fibrocystic disease | 98.49% | DL |
| 2 | Prinzmetal angina | 98.39% | DL |
| 3 | peripheral arterial disease | 98.06% | DL |
| 4 | blunt duct adenosis of breast | 97.82% | DL |
| 5 | apocrine adenosis of breast | 97.82% | DL |
| 6 | thrombotic disease | 97.50% | DL |
| 7 | tendinitis | 97.42% | DL |
| 8 | antithrombin deficiency type 2 | 97.42% | DL |
| 9 | benign mammary dysplasia | 97.42% | DL |
| 10 | female breast carcinoma | 97.30% | DL |
| 11 | factor 5 excess with spontaneous thrombosis | 97.30% | DL |
| 12 | epiglottitis | 97.26% | DL |
| 13 | ischemic disease | 97.25% | DL |
| 14 | angiodysplasia | 97.22% | DL |
| 15 | idiopathic granulomatous myositis | 97.19% | DL |
| 16 | myositis fibrosa | 97.19% | DL |
| 17 | hemoglobinopathy | 97.17% | DL |
| 18 | fibrocartilaginous embolism | 97.12% | DL |
| 19 | venous thromboembolism | 97.12% | DL |
| 20 | breast adenosis | 97.09% | DL |

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
