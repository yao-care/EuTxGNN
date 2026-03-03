---
layout: default
title: Guselkumab
description: "Guselkumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 279
evidence_level: L5
indication_count: 50
---

# Guselkumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Guselkumab |
| DrugBank ID | [DB11834](https://go.drugbank.com/drugs/DB11834) |
| Brand Names (EU) | Tremfya |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.84% |

---

## Approved Indication (EMA)

Adult plaque psoriasisTremfya is indicated for the treatment of moderate to severe plaque psoriasis in adults who are candidates for systemic therapy.  Paediatric plaque psoriasisTremfya is indicated for the treatment of moderate to severe plaque psoriasis in children and adolescents from the age of 6 years who are candidates for systemic therapy.&nbsp;  Psoriatic arthritisTremfya, alone or in combination with methotrexate (MTX), is indicated for the treatment of active psoriatic arthritis in ad

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 99.84% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 99.80% | DL |
| 3 | psoriasis | 99.75% | DL |
| 4 | diabetic retinopathy | 99.74% | DL |
| 5 | renal osteodystrophy | 99.73% | DL |
| 6 | ulcerative colitis (disease) | 99.70% | DL |
| 7 | congenital hypotrichosis with juvenile macular dystrophy | 99.67% | DL |
| 8 | primary release disorder of platelets | 99.61% | DL |
| 9 | Glanzmann thrombasthenia | 99.60% | DL |
| 10 | non-renal secondary hyperparathyroidism | 99.55% | DL |
| 11 | pseudo-von Willebrand disease | 99.54% | DL |
| 12 | impaired renal function disease | 99.51% | DL |
| 13 | gout | 99.51% | DL |
| 14 | benign recurrent intrahepatic cholestasis | 99.50% | DL |
| 15 | hyperparathyroidism, transient neonatal | 99.49% | DL |
| 16 | familial intrahepatic cholestasis | 99.49% | DL |
| 17 | diabetic cataract | 99.47% | DL |
| 18 | pityriasis lichenoides | 99.47% | DL |
| 19 | bone remodeling disease | 99.44% | DL |
| 20 | cholestasis | 99.39% | DL |

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
