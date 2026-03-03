---
layout: default
title: Teprotumumab
description: "Teprotumumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 571
evidence_level: L5
indication_count: 51
---

# Teprotumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Teprotumumab |
| DrugBank ID | [DB06343](https://go.drugbank.com/drugs/DB06343) |
| Brand Names (EU) | Tepezza |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.79% |

---

## Approved Indication (EMA)

Treatment of moderate to severe thyroid eye disease (TED).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | monosomy X | 99.79% | DL |
| 2 | esophageal varices with bleeding | 99.64% | DL |
| 3 | esophageal varices without bleeding | 99.64% | DL |
| 4 | mixed gonadal dysgenesis | 99.50% | DL |
| 5 | mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 99.44% | DL |
| 6 | Turner syndrome due to structural X chromosome anomalies | 99.37% | DL |
| 7 | mosaic monosomy X | 99.37% | DL |
| 8 | sex chromosome disorder of sex development | 99.34% | DL |
| 9 | varicose disease | 99.33% | DL |
| 10 | X chromosome number anomaly | 99.32% | DL |
| 11 | gonadal dysgenesis | 99.02% | DL |
| 12 | Turner syndrome | 99.02% | DL |
| 13 | 46,XY disorder of gonadal development | 99.01% | DL |
| 14 | male infertility due to gonadal dysgenesis | 98.91% | DL |
| 15 | exocrine pancreatic insufficiency | 98.91% | DL |
| 16 | precocious puberty | 98.82% | DL |
| 17 | ichthyosis, X-linked, without steroid sulfatase deficiency | 98.77% | DL |
| 18 | disorder of other vitamins and cofactors metabolism and transport | 98.63% | DL |
| 19 | dappled diaphyseal dysplasia | 98.62% | DL |
| 20 | xanthomatosis (disease) | 98.59% | DL |

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
