---
layout: default
title: Dulaglutide
description: "Dulaglutide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 185
evidence_level: L5
indication_count: 51
---

# Dulaglutide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dulaglutide |
| DrugBank ID | [DB09045](https://go.drugbank.com/drugs/DB09045) |
| Brand Names (EU) | Trulicity |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 97.05% |

---

## Approved Indication (EMA)

Trulicity is indicated for the treatment of patients 10 years and above&nbsp;with insufficiently controlled type&nbsp;2 diabetes mellitus as an adjunct to diet and exercise  as monotherapy when metformin is considered inappropriate due to intolerance or contraindications in addition to other medicinal products for the treatment of diabetes.  For study results with respect to combinations, effects on glycaemic control and cardiovascular events, and the populations studied, see sections 4.4, 4.5 a

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | opsismodysplasia | 97.05% | DL |
| 2 | focal stiff limb syndrome | 97.05% | DL |
| 3 | classic stiff person syndrome | 97.05% | DL |
| 4 | thiamine-responsive dysfunction syndrome | 96.81% | DL |
| 5 | diabetes mellitus (disease) | 96.57% | DL |
| 6 | drug-induced localized lipodystrophy | 95.62% | DL |
| 7 | pancreatic agenesis | 95.55% | DL |
| 8 | centrifugal lipodystrophy | 95.37% | DL |
| 9 | pressure-induced localized lipoatrophy | 95.29% | DL |
| 10 | idiopathic localized lipodystrophy | 94.99% | DL |
| 11 | autoimmune oophoritis | 69.57% | DL |
| 12 | cholangiocarcinoma, susceptibility to | 65.61% | DL |
| 13 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 64.93% | DL |
| 14 | hemoglobin C-beta-thalassemia syndrome | 64.30% | DL |
| 15 | type 1 diabetes mellitus | 63.72% | DL |
| 16 | atrial flutter (disease) | 63.47% | DL |
| 17 | pancreas, dorsal, agenesis of | 61.12% | DL |
| 18 | familial chronic myelocytic leukemia-like syndrome | 60.46% | DL |
| 19 | lymphopenic hypergammaglobulinemia, antibody deficiency, autoimmune hemolytic anemia, and glomerulonephritis | 59.90% | DL |
| 20 | mitral valve prolapse, myxomatous | 59.70% | DL |

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
