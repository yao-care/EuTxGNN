---
layout: default
title: Sebelipase Alfa
description: "Sebelipase Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 518
evidence_level: L5
indication_count: 51
---

# Sebelipase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sebelipase Alfa |
| DrugBank ID | [DB11563](https://go.drugbank.com/drugs/DB11563) |
| Brand Names (EU) | Kanuma |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.80% |

---

## Approved Indication (EMA)

Kanuma is indicated for long-term enzyme replacement therapy (ERT) in patients of all ages with lysosomal acid lipase (LAL) deficiency.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Scheie syndrome | 99.80% | DL |
| 2 | Hurler syndrome | 99.79% | DL |
| 3 | growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | 99.75% | DL |
| 4 | cholesteryl ester storage disease | 99.72% | DL |
| 5 | Wolman disease with hypolipoproteinemia and acanthocytosis | 99.72% | DL |
| 6 | Gaucher disease | 99.71% | DL |
| 7 | lysosomal storage disease with skeletal involvement | 99.64% | DL |
| 8 | autosomal ichthyosis syndrome with fatal disease course | 99.64% | DL |
| 9 | Tay-Sachs disease | 99.63% | DL |
| 10 | Wolman disease | 99.63% | DL |
| 11 | benign neoplasm of adrenal gland | 99.60% | DL |
| 12 | adult Krabbe disease | 99.54% | DL |
| 13 | mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 99.50% | DL |
| 14 | Krabbe disease | 99.44% | DL |
| 15 | cholesterol metabolism disease | 99.43% | DL |
| 16 | lysosomal acid lipase deficiency | 99.42% | DL |
| 17 | metachromatic leukodystrophy | 99.40% | DL |
| 18 | encephalopathy due to prosaposin deficiency | 99.38% | DL |
| 19 | infantile neuronal ceroid lipofuscinosis | 99.27% | DL |
| 20 | alpha-mannosidosis | 99.26% | DL |

*Showing top 20 of 51 predictions.*

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
