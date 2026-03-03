---
layout: default
title: Agomelatine
description: "Agomelatine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 23
evidence_level: L5
indication_count: 50
---

# Agomelatine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Agomelatine |
| DrugBank ID | [DB06594](https://go.drugbank.com/drugs/DB06594) |
| Brand Names (EU) | Valdoxan |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Treatment of major depressive episodes in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | anxiety disorder | 99.98% | DL |
| 2 | endogenous depression | 99.98% | DL |
| 3 | unipolar depression | 99.97% | DL |
| 4 | benign paroxysmal torticollis of infancy | 99.96% | DL |
| 5 | major depressive disorder | 99.96% | DL |
| 6 | agoraphobia | 99.95% | DL |
| 7 | neurotic disorder | 99.90% | DL |
| 8 | melancholia | 99.88% | DL |
| 9 | neurotic depression | 99.88% | DL |
| 10 | Ohdo syndrome and variants | 99.87% | DL |
| 11 | dysthymic disorder | 99.86% | DL |
| 12 | ligneous conjunctivitis | 99.83% | DL |
| 13 | blepharophimosis - intellectual disability syndrome, Ohdo type | 99.82% | DL |
| 14 | Keppen-Lubinsky syndrome | 99.81% | DL |
| 15 | congenital isolated adrenocorticotropic hormone deficiency (disease) | 99.73% | DL |
| 16 | autosomal dominant slowed nerve conduction velocity | 99.69% | DL |
| 17 | phobic disorder | 99.67% | DL |
| 18 | vitamin B12-responsive methylmalonic acidemia | 99.51% | DL |
| 19 | post-traumatic stress disorder | 99.32% | DL |
| 20 | postpartum depression | 99.32% | DL |

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
