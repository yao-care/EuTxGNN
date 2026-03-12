---
layout: default
title: Canagliflozin
description: "Canagliflozin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 108
evidence_level: L5
indication_count: 50
---

# Canagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Canagliflozin |
| DrugBank ID | [DB08907](https://go.drugbank.com/drugs/DB08907) |
| Brand Names (EU) | Invokana |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.92% |

---

## Approved Indication (EMA)

Vokanamet is indicated in adults aged 18 years and older with type 2 diabetes mellitus as an adjunct to diet and exercise to improve glycaemic control:  in patients not adequately controlled on their maximally tolerated doses of metformin alone in patients on their maximally tolerated doses of metformin along with other glucose lowering medicinal products including insulin, when these do not provide adequate glycaemic control. in patients already being treated with the combination of canaglifloz

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | classic stiff person syndrome | 97.92% | DL |
| 2 | focal stiff limb syndrome | 97.92% | DL |
| 3 | opsismodysplasia | 97.81% | DL |
| 4 | thiamine-responsive dysfunction syndrome | 97.70% | DL |
| 5 | diabetes mellitus (disease) | 97.56% | DL |
| 6 | drug-induced localized lipodystrophy | 96.59% | DL |
| 7 | centrifugal lipodystrophy | 96.43% | DL |
| 8 | pressure-induced localized lipoatrophy | 96.33% | DL |
| 9 | idiopathic localized lipodystrophy | 96.16% | DL |
| 10 | pancreatic agenesis | 96.04% | DL |
| 11 | autoimmune oophoritis | 82.37% | DL |
| 12 | type 1 diabetes mellitus | 80.96% | DL |
| 13 | homozygous familial hypercholesterolemia | 72.18% | DL |
| 14 | atrial flutter (disease) | 62.85% | DL |
| 15 | cholangiocarcinoma, susceptibility to | 61.95% | DL |
| 16 | hemoglobin C-beta-thalassemia syndrome | 60.80% | DL |
| 17 | congenital temporomandibular joint ankylosis | 59.09% | DL |
| 18 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 58.43% | DL |
| 19 | sudden arrhythmia death syndrome | 58.13% | DL |
| 20 | polydipsia | 57.52% | DL |

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
