---
layout: default
title: Nepafenac
description: "Nepafenac drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 398
evidence_level: L5
indication_count: 50
---

# Nepafenac
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nepafenac |
| DrugBank ID | [DB06802](https://go.drugbank.com/drugs/DB06802) |
| Brand Names (EU) | Nevanac |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.85% |

---

## Approved Indication (EMA)

Nevanac is indicated for:  prevention and treatment of postoperative pain and inflammation associated with cataract surgery; reduction in the risk of postoperative macular oedema associated with cataract surgery in diabetic patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | eye disease | 99.85% | DL |
| 2 | optic papillitis | 99.84% | DL |
| 3 | hypotrichosis simplex of the scalp | 99.84% | DL |
| 4 | seborrheic keratosis | 99.83% | DL |
| 5 | von Hippel anomaly | 99.82% | DL |
| 6 | congenital hypotrichosis milia | 99.82% | DL |
| 7 | mcpherson robertson cammarano syndrome | 99.82% | DL |
| 8 | lagophthalmos | 99.81% | DL |
| 9 | vulvar inverted follicular keratosis | 99.81% | DL |
| 10 | vitreous detachment | 99.81% | DL |
| 11 | microblepharon-ablephara syndrome | 99.81% | DL |
| 12 | luxation of globe | 99.81% | DL |
| 13 | conjunctival degeneration | 99.81% | DL |
| 14 | isolated optic neuritis | 99.81% | DL |
| 15 | recurrent idiopathic neuroretinitis | 99.81% | DL |
| 16 | optic perineuritis | 99.81% | DL |
| 17 | chronic relapsing inflammatory optic neuropathy | 99.81% | DL |
| 18 | episcleritis periodica fugax | 99.81% | DL |
| 19 | nodular episcleritis | 99.81% | DL |
| 20 | total internal ophthalmoplegia | 99.80% | DL |

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
