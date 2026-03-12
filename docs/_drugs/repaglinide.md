---
layout: default
title: Repaglinide
description: "Repaglinide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 488
evidence_level: L5
indication_count: 51
---

# Repaglinide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Repaglinide |
| DrugBank ID | [DB00912](https://go.drugbank.com/drugs/DB00912) |
| Brand Names (EU) | NovoNorm, Repaglinide Krka |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.77% |

---

## Approved Indication (EMA)

Repaglinide is indicated in patients with type-2 diabetes (non-insulin-dependent diabetes mellitus (NIDDM)) whose hyperglycaemia can no longer be controlled satisfactorily by diet, weight reduction and exercise. Repaglinide is also indicated in combination with metformin in type 2 diabetes patients who are not satisfactorily controlled on metformin alone. Treatment should be initiated as an adjunct to diet and exercise to lower the blood glucose in relation to meals.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | opsismodysplasia | 98.77% | DL |
| 2 | diabetes mellitus (disease) | 98.56% | DL |
| 3 | classic stiff person syndrome | 98.48% | DL |
| 4 | focal stiff limb syndrome | 98.48% | DL |
| 5 | thiamine-responsive dysfunction syndrome | 98.47% | DL |
| 6 | drug-induced localized lipodystrophy | 97.80% | DL |
| 7 | centrifugal lipodystrophy | 97.65% | DL |
| 8 | pressure-induced localized lipoatrophy | 97.61% | DL |
| 9 | pancreatic agenesis | 97.58% | DL |
| 10 | idiopathic localized lipodystrophy | 97.43% | DL |
| 11 | autoimmune oophoritis | 93.59% | DL |
| 12 | type 1 diabetes mellitus | 92.69% | DL |
| 13 | cholangiocarcinoma, susceptibility to | 64.02% | DL |
| 14 | mitral valve prolapse, myxomatous | 60.99% | DL |
| 15 | hemoglobin C-beta-thalassemia syndrome | 60.17% | DL |
| 16 | woolly hair, autosomal recessive 3 | 59.26% | DL |
| 17 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 59.07% | DL |
| 18 | congenital temporomandibular joint ankylosis | 58.61% | DL |
| 19 | obsolete breast fibroadenosis | 58.56% | DL |
| 20 | atrial flutter (disease) | 58.23% | DL |

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
