---
layout: default
title: Saxagliptin
description: "Saxagliptin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 517
evidence_level: L5
indication_count: 51
---

# Saxagliptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Saxagliptin |
| DrugBank ID | [DB06335](https://go.drugbank.com/drugs/DB06335) |
| Brand Names (EU) | Onglyza |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.09% |

---

## Approved Indication (EMA)

Add-on combination therapy Onglyza is indicated in adult patients aged 18 years and older with type-2 diabetes mellitus to improve glycaemic control: as monotherapy:  in patients inadequately controlled by diet and exercise alone and for whom metformin is inappropriate due to contraindications or intolerance;  as dual oral therapy:  in combination with metformin, when metformin alone, with diet and exercise, does not provide adequate glycaemic control; in combination with a sulphonylurea, when t

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | opsismodysplasia | 98.09% | DL |
| 2 | classic stiff person syndrome | 97.66% | DL |
| 3 | focal stiff limb syndrome | 97.66% | DL |
| 4 | diabetes mellitus (disease) | 97.59% | DL |
| 5 | thiamine-responsive dysfunction syndrome | 97.50% | DL |
| 6 | drug-induced localized lipodystrophy | 96.35% | DL |
| 7 | pancreatic agenesis | 96.24% | DL |
| 8 | centrifugal lipodystrophy | 96.12% | DL |
| 9 | pressure-induced localized lipoatrophy | 96.02% | DL |
| 10 | idiopathic localized lipodystrophy | 95.75% | DL |
| 11 | autoimmune oophoritis | 85.22% | DL |
| 12 | type 1 diabetes mellitus | 82.18% | DL |
| 13 | cholangiocarcinoma, susceptibility to | 64.35% | DL |
| 14 | hemoglobin C-beta-thalassemia syndrome | 61.09% | DL |
| 15 | mitral valve prolapse, myxomatous | 58.43% | DL |
| 16 | obsolete breast fibroadenosis | 58.15% | DL |
| 17 | congenital temporomandibular joint ankylosis | 57.74% | DL |
| 18 | atrial flutter (disease) | 57.73% | DL |
| 19 | obsolete functional visual loss | 57.67% | DL |
| 20 | familial chronic myelocytic leukemia-like syndrome | 57.62% | DL |

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
