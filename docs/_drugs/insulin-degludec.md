---
layout: default
title: Insulin Degludec
description: "Insulin Degludec drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 305
evidence_level: L5
indication_count: 50
---

# Insulin Degludec
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Insulin Degludec |
| DrugBank ID | [DB09564](https://go.drugbank.com/drugs/DB09564) |
| Brand Names (EU) | Tresiba |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.44% |

---

## Approved Indication (EMA)

Xultophy is indicated for the treatment of adults with type-2 diabetes mellitus to improve glycaemic control in combination with oral glucose-lowering medicinal products when these alone or combined with a GLP-1 receptor agonist or basal insulin do not provide adequate glycaemic control.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | type 1 diabetes mellitus | 99.44% | DL |
| 2 | autoimmune oophoritis | 99.23% | DL |
| 3 | opsismodysplasia | 99.12% | DL |
| 4 | diabetes mellitus (disease) | 99.10% | DL |
| 5 | thiamine-responsive dysfunction syndrome | 99.10% | DL |
| 6 | focal stiff limb syndrome | 99.08% | DL |
| 7 | classic stiff person syndrome | 99.08% | DL |
| 8 | drug-induced localized lipodystrophy | 98.65% | DL |
| 9 | pancreatic agenesis | 98.61% | DL |
| 10 | centrifugal lipodystrophy | 98.60% | DL |
| 11 | pressure-induced localized lipoatrophy | 98.58% | DL |
| 12 | idiopathic localized lipodystrophy | 98.52% | DL |
| 13 | diabetic ketoacidosis | 97.69% | DL |
| 14 | permanent neonatal diabetes mellitus | 96.67% | DL |
| 15 | diabetes mellitus, insulin-dependent, X-linked, susceptibility to | 88.47% | DL |
| 16 | pancreatitis | 88.35% | DL |
| 17 | IDDM 1 | 87.25% | DL |
| 18 | acute kidney failure | 72.13% | DL |
| 19 | alcoholic cardiomyopathy | 69.97% | DL |
| 20 | glaucoma | 69.44% | DL |

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
