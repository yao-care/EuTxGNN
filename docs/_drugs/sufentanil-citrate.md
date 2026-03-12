---
layout: default
title: Sufentanil Citrate
description: "Sufentanil Citrate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 545
evidence_level: L5
indication_count: 50
---

# Sufentanil Citrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sufentanil Citrate |
| DrugBank ID | [DB00708](https://go.drugbank.com/drugs/DB00708) |
| Brand Names (EU) | Dzuveo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.41% |

---

## Approved Indication (EMA)

Dzuveo is indicated for the management of acute moderate to severe pain in adult patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 97.41% | DL |
| 2 | common cold | 96.82% | DL |
| 3 | gastroduodenitis | 86.77% | DL |
| 4 | peptic ulcer disease | 84.98% | DL |
| 5 | exercise-induced malignant hyperthermia | 83.65% | DL |
| 6 | headache disorder | 80.97% | DL |
| 7 | trigeminal autonomic cephalalgia | 79.58% | DL |
| 8 | familial periodic paralysis | 75.71% | DL |
| 9 | nephrogenic diabetes insipidus | 74.79% | DL |
| 10 | obsolete rare pulmonary disease | 74.52% | DL |
| 11 | allergic urticaria | 74.04% | DL |
| 12 | nasal cavity disease | 73.73% | DL |
| 13 | acute laryngopharyngitis | 70.84% | DL |
| 14 | Jeune syndrome | 70.70% | DL |
| 15 | pharyngitis | 70.63% | DL |
| 16 | hypokalemic periodic paralysis | 69.78% | DL |
| 17 | malignant hyperthermia of anesthesia | 69.38% | DL |
| 18 | malignant hyperthermia, susceptibility to | 69.32% | DL |
| 19 | subarachnoid hemorrhage (disease) | 67.29% | DL |
| 20 | hereditary renal hypouricemia | 66.80% | DL |

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
