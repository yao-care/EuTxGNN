---
layout: default
title: Spironolactone
description: "Spironolactone drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 543
evidence_level: L5
indication_count: 53
---

# Spironolactone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Spironolactone |
| DrugBank ID | [DB00421](https://go.drugbank.com/drugs/DB00421) |
| Brand Names (EU) | Qaialdo |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.26% |

---

## Approved Indication (EMA)

In the management of refractory oedema associated with congestive cardiac failure; hepatic cirrhosis with ascites and oedema, malignant ascites, nephrotic syndrome, diagnosis and treatment of primary aldosteronism, essential hypertension. Neonates, children and adolescents should only be treated under guidance of a paediatric specialist (see sections 5.1 and 5.2). 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hypotrichosis simplex of the scalp | 99.26% | DL |
| 2 | congenital hypotrichosis milia | 99.04% | DL |
| 3 | diffuse alopecia areata | 98.41% | DL |
| 4 | alopecia | 97.83% | DL |
| 5 | hypertensive disorder | 97.75% | DL |
| 6 | malignant hypertensive renal disease | 97.54% | DL |
| 7 | malignant renovascular hypertension | 97.54% | DL |
| 8 | pulmonary hypertension owing to lung disease and/or hypoxia | 97.33% | DL |
| 9 | pulmonary hypertension with unclear multifactorial mechanism | 97.33% | DL |
| 10 | Braddock syndrome | 96.64% | DL |
| 11 | chronic pulmonary heart disease | 95.55% | DL |
| 12 | Waterhouse-Friderichsen syndrome | 85.58% | DL |
| 13 | primary hereditary glaucoma | 84.05% | DL |
| 14 | acute pulmonary heart disease | 81.18% | DL |
| 15 | pregnancy associated osteoporosis | 78.56% | DL |
| 16 | Worth syndrome | 75.84% | DL |
| 17 | autosomal dominant neovascular inflammatory vitreoretinopathy | 75.68% | DL |
| 18 | open-angle glaucoma | 74.40% | DL |
| 19 | congestive heart failure | 74.04% | DL |
| 20 | postmenopausal osteoporosis | 73.28% | DL |

*Showing top 20 of 53 predictions.*

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
