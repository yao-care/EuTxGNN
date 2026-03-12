---
layout: default
title: Amlodipine
description: "amlodipine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 36
evidence_level: L5
indication_count: 50
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Amlodipine |
| DrugBank ID | [DB00381](https://go.drugbank.com/drugs/DB00381) |
| Brand Names (EU) | Amlodipine |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Treatment of essential hypertension in adults: Add-on therapy Twynsta is indicated in adults whose blood pressure is not adequately controlled on amlodipine. Replacement therapy Adult patients receiving telmisartan and amlodipine from separate tablets can instead receive tablets of Twynsta containing the same component doses.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | obsolete susceptibility to ischemic stroke | 99.97% | DL |
| 2 | cerebrovascular disorder | 99.96% | DL |
| 3 | brain stem infarction | 99.94% | DL |
| 4 | Prinzmetal angina | 99.94% | DL |
| 5 | cerebral infarction | 99.91% | DL |
| 6 | pulmonary hypertension with unclear multifactorial mechanism | 99.91% | DL |
| 7 | pulmonary hypertension owing to lung disease and/or hypoxia | 99.91% | DL |
| 8 | malignant renovascular hypertension | 99.90% | DL |
| 9 | malignant hypertensive renal disease | 99.90% | DL |
| 10 | hypertensive disorder | 99.89% | DL |
| 11 | cerebral artery occlusion | 99.89% | DL |
| 12 | Braddock syndrome | 99.88% | DL |
| 13 | stroke disorder | 99.88% | DL |
| 14 | MRI defined brain infarct | 99.86% | DL |
| 15 | ABri amyloidosis | 99.84% | DL |
| 16 | intracerebral hemorrhage | 99.79% | DL |
| 17 | cerebral arterial disease | 99.78% | DL |
| 18 | chronic pulmonary heart disease | 99.69% | DL |
| 19 | spinal cord ischemia | 99.65% | DL |
| 20 | cholesterol embolism | 98.56% | DL |

*Showing top 20 of 50 predictions.*

---


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
