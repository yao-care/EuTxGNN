---
layout: default
title: Alogliptin
description: "Alogliptin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 31
evidence_level: L5
indication_count: 51
---

# Alogliptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Alogliptin |
| DrugBank ID | [DB06203](https://go.drugbank.com/drugs/DB06203) |
| Brand Names (EU) | Incresync, Vipidia |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.01% |

---

## Approved Indication (EMA)

Incresync is indicated as a second- or third-line treatment in adult patients aged 18 years and older with type-2 diabetes mellitus:  as an adjunct to diet and exercise to improve glycaemic control in adult patients (particularly overweight patients) inadequately controlled on pioglitazone alone, and for whom metformin is inappropriate due to contraindications or intolerance; in combination with metformin (i.e. triple combination therapy) as an adjunct to diet and exercise to improve glycaemic c

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | classic stiff person syndrome | 98.01% | DL |
| 2 | focal stiff limb syndrome | 98.01% | DL |
| 3 | opsismodysplasia | 97.82% | DL |
| 4 | thiamine-responsive dysfunction syndrome | 97.76% | DL |
| 5 | diabetes mellitus (disease) | 97.52% | DL |
| 6 | drug-induced localized lipodystrophy | 96.55% | DL |
| 7 | pancreatic agenesis | 96.47% | DL |
| 8 | centrifugal lipodystrophy | 96.39% | DL |
| 9 | pressure-induced localized lipoatrophy | 96.28% | DL |
| 10 | idiopathic localized lipodystrophy | 96.08% | DL |
| 11 | autoimmune oophoritis | 87.56% | DL |
| 12 | type 1 diabetes mellitus | 86.94% | DL |
| 13 | cholangiocarcinoma, susceptibility to | 63.64% | DL |
| 14 | atrial flutter (disease) | 63.53% | DL |
| 15 | hemoglobin C-beta-thalassemia syndrome | 63.32% | DL |
| 16 | congenital temporomandibular joint ankylosis | 58.90% | DL |
| 17 | obsolete functional visual loss | 58.68% | DL |
| 18 | ocular tuberculosis | 58.16% | DL |
| 19 | pancreas, dorsal, agenesis of | 58.04% | DL |
| 20 | obsolete breast fibroadenosis | 57.87% | DL |

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
