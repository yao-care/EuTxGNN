---
layout: default
title: Metformin
description: "Metformin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 371
evidence_level: L5
indication_count: 50
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Metformin |
| DrugBank ID | [DB00331](https://go.drugbank.com/drugs/DB00331) |
| Brand Names (EU) | Metformin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.45% |

---

## Approved Indication (EMA)

Synjardy is indicated in adults and children aged 10 years and above for the treatment of type 2 diabetes mellitus as an adjunct to diet and exercise:•&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; in patients insufficiently controlled on their maximally tolerated dose of metformin alone•&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; in combination with other medicinal products for the treatment of diabetes, in patients insufficiently controlled with metformin and these medicinal

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | focal stiff limb syndrome | 99.45% | DL |
| 2 | classic stiff person syndrome | 99.45% | DL |
| 3 | diabetes mellitus (disease) | 99.43% | DL |
| 4 | opsismodysplasia | 99.40% | DL |
| 5 | thiamine-responsive dysfunction syndrome | 99.40% | DL |
| 6 | drug-induced localized lipodystrophy | 99.06% | DL |
| 7 | centrifugal lipodystrophy | 98.99% | DL |
| 8 | pressure-induced localized lipoatrophy | 98.96% | DL |
| 9 | pancreatic agenesis | 98.91% | DL |
| 10 | idiopathic localized lipodystrophy | 98.90% | DL |
| 11 | homozygous familial hypercholesterolemia | 92.30% | DL |
| 12 | autoimmune oophoritis | 83.94% | DL |
| 13 | hypervitaminosis | 82.40% | DL |
| 14 | type 1 diabetes mellitus | 79.77% | DL |
| 15 | pulmonary atresia-intact ventricular septum syndrome | 77.36% | DL |
| 16 | pulmonic stenosis (disease) | 76.27% | DL |
| 17 | genetic vascular tumor | 73.85% | DL |
| 18 | arterial duct anomaly | 73.33% | DL |
| 19 | proximal 16p11.2 microdeletion syndrome | 73.09% | DL |
| 20 | subaortic stenosis, membranous | 71.88% | DL |

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
