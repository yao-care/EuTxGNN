---
layout: default
title: Insulin Human
description: "Insulin Human drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 309
evidence_level: L5
indication_count: 50
---

# Insulin Human
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Insulin Human |
| DrugBank ID | [DB00030](https://go.drugbank.com/drugs/DB00030) |
| Brand Names (EU) | Protaphane |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Treatment of diabetes mellitus.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | type 1 diabetes mellitus | 99.88% | DL |
| 2 | autoimmune oophoritis | 99.84% | DL |
| 3 | diabetes mellitus (disease) | 99.81% | DL |
| 4 | focal stiff limb syndrome | 99.81% | DL |
| 5 | classic stiff person syndrome | 99.81% | DL |
| 6 | thiamine-responsive dysfunction syndrome | 99.80% | DL |
| 7 | opsismodysplasia | 99.79% | DL |
| 8 | drug-induced localized lipodystrophy | 99.72% | DL |
| 9 | centrifugal lipodystrophy | 99.70% | DL |
| 10 | pressure-induced localized lipoatrophy | 99.70% | DL |
| 11 | pancreatic agenesis | 99.70% | DL |
| 12 | idiopathic localized lipodystrophy | 99.68% | DL |
| 13 | diabetic ketoacidosis | 98.40% | DL |
| 14 | permanent neonatal diabetes mellitus | 98.35% | DL |
| 15 | diabetes mellitus, insulin-dependent, X-linked, susceptibility to | 96.16% | DL |
| 16 | IDDM 1 | 94.48% | DL |
| 17 | type 2 diabetes mellitus | 75.80% | DL |
| 18 | pancreatitis | 74.15% | DL |
| 19 | venous insufficiency (disease) | 73.85% | DL |
| 20 | acute kidney failure | 70.50% | DL |

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
