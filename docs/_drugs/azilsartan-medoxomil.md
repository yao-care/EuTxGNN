---
layout: default
title: Azilsartan Medoxomil
description: "Azilsartan Medoxomil drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 66
evidence_level: L5
indication_count: 50
---

# Azilsartan Medoxomil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Azilsartan Medoxomil |
| DrugBank ID | [DB08822](https://go.drugbank.com/drugs/DB08822) |
| Brand Names (EU) | Edarbi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.04% |

---

## Approved Indication (EMA)

Edarbi is indicated for the treatment of essential hypertension in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hypertensive disorder | 98.04% | DL |
| 2 | pulmonary hypertension with unclear multifactorial mechanism | 97.78% | DL |
| 3 | pulmonary hypertension owing to lung disease and/or hypoxia | 97.78% | DL |
| 4 | malignant renovascular hypertension | 97.69% | DL |
| 5 | malignant hypertensive renal disease | 97.69% | DL |
| 6 | Braddock syndrome | 97.22% | DL |
| 7 | cerebrovascular disorder | 94.56% | DL |
| 8 | obsolete susceptibility to ischemic stroke | 92.74% | DL |
| 9 | chronic pulmonary heart disease | 91.79% | DL |
| 10 | brain stem infarction | 87.67% | DL |
| 11 | hypotrichosis simplex of the scalp | 85.01% | DL |
| 12 | intracerebral hemorrhage | 84.97% | DL |
| 13 | congenital hypotrichosis milia | 81.18% | DL |
| 14 | cerebral artery occlusion | 78.67% | DL |
| 15 | ABri amyloidosis | 77.18% | DL |
| 16 | alopecia | 74.58% | DL |
| 17 | MRI defined brain infarct | 70.91% | DL |
| 18 | diffuse alopecia areata | 70.86% | DL |
| 19 | primary hereditary glaucoma | 60.50% | DL |
| 20 | congenital temporomandibular joint ankylosis | 60.15% | DL |

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
