---
layout: default
title: Dapagliflozin
description: "Dapagliflozin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 152
evidence_level: L5
indication_count: 50
---

# Dapagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dapagliflozin |
| DrugBank ID | [DB06292](https://go.drugbank.com/drugs/DB06292) |
| Brand Names (EU) | Dapagliflozin Viatris |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.20% |

---

## Approved Indication (EMA)

Type 2 diabetes mellitus Dapagliflozin Viatris is indicated in adults and children aged 10 years and above for the treatment of insufficiently controlled type 2 diabetes mellitus as an adjunct to diet and exercise - as monotherapy when metformin is considered inappropriate due to intolerance. - in addition to other medicinal products for the treatment of type 2 diabetes. For study results with respect to combination of therapies, effects on glycaemic control, cardiovascular and renal events, and

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | classic stiff person syndrome | 98.20% | DL |
| 2 | focal stiff limb syndrome | 98.20% | DL |
| 3 | opsismodysplasia | 98.06% | DL |
| 4 | thiamine-responsive dysfunction syndrome | 98.03% | DL |
| 5 | diabetes mellitus (disease) | 97.88% | DL |
| 6 | drug-induced localized lipodystrophy | 97.03% | DL |
| 7 | centrifugal lipodystrophy | 96.90% | DL |
| 8 | pressure-induced localized lipoatrophy | 96.82% | DL |
| 9 | idiopathic localized lipodystrophy | 96.67% | DL |
| 10 | pancreatic agenesis | 96.59% | DL |
| 11 | autoimmune oophoritis | 90.43% | DL |
| 12 | type 1 diabetes mellitus | 90.33% | DL |
| 13 | diabetes mellitus, insulin-dependent, X-linked, susceptibility to | 63.16% | DL |
| 14 | atrial flutter (disease) | 62.71% | DL |
| 15 | cholangiocarcinoma, susceptibility to | 62.23% | DL |
| 16 | hemoglobin C-beta-thalassemia syndrome | 62.05% | DL |
| 17 | retinal dystrophy with or without extraocular anomalies | 61.78% | DL |
| 18 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 59.39% | DL |
| 19 | congenital temporomandibular joint ankylosis | 59.12% | DL |
| 20 | permanent neonatal diabetes mellitus | 59.03% | DL |

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
