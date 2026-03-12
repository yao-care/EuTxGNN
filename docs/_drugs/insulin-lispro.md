---
layout: default
title: Insulin Lispro
description: "Insulin Lispro drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 310
evidence_level: L5
indication_count: 51
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Insulin Lispro |
| DrugBank ID | [DB00046](https://go.drugbank.com/drugs/DB00046) |
| Brand Names (EU) | Humalog, Lyumjev (previously Liumjev) |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.83% |

---

## Approved Indication (EMA)

For the treatment of adults and children with diabetes mellitus who require insulin for the maintenance of normal glucose homeostasis. Humalog is also indicated for the initial stabilisation of diabetes mellitus.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | type 1 diabetes mellitus | 99.83% | DL |
| 2 | autoimmune oophoritis | 99.78% | DL |
| 3 | thiamine-responsive dysfunction syndrome | 99.37% | DL |
| 4 | classic stiff person syndrome | 99.36% | DL |
| 5 | focal stiff limb syndrome | 99.36% | DL |
| 6 | diabetes mellitus (disease) | 99.35% | DL |
| 7 | opsismodysplasia | 99.34% | DL |
| 8 | drug-induced localized lipodystrophy | 99.09% | DL |
| 9 | pancreatic agenesis | 99.09% | DL |
| 10 | centrifugal lipodystrophy | 99.04% | DL |
| 11 | pressure-induced localized lipoatrophy | 99.03% | DL |
| 12 | idiopathic localized lipodystrophy | 98.97% | DL |
| 13 | diabetic ketoacidosis | 97.63% | DL |
| 14 | permanent neonatal diabetes mellitus | 97.46% | DL |
| 15 | diabetes mellitus, insulin-dependent, X-linked, susceptibility to | 91.10% | DL |
| 16 | IDDM 1 | 89.19% | DL |
| 17 | glaucoma | 79.66% | DL |
| 18 | venous insufficiency (disease) | 73.91% | DL |
| 19 | atrial flutter (disease) | 67.97% | DL |
| 20 | hemoglobin C-beta-thalassemia syndrome | 67.50% | DL |

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
