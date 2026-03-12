---
layout: default
title: Irbesartan
description: "Irbesartan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 314
evidence_level: L5
indication_count: 50
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Irbesartan |
| DrugBank ID | [DB01029](https://go.drugbank.com/drugs/DB01029) |
| Brand Names (EU) | Irbesartan Teva |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.31% |

---

## Approved Indication (EMA)

Treatment of essential hypertension. Treatment of renal disease in patients with hypertension and type 2 diabetes mellitus as part of an antihypertensive medicinal product regimen.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | malignant hypertensive renal disease | 99.31% | DL |
| 2 | malignant renovascular hypertension | 99.31% | DL |
| 3 | pulmonary hypertension with unclear multifactorial mechanism | 99.25% | DL |
| 4 | pulmonary hypertension owing to lung disease and/or hypoxia | 99.25% | DL |
| 5 | Braddock syndrome | 98.99% | DL |
| 6 | hypertensive disorder | 98.97% | DL |
| 7 | Prinzmetal angina | 98.87% | DL |
| 8 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 98.72% | DL |
| 9 | brain small vessel disease 1 with or without ocular anomalies | 98.66% | DL |
| 10 | diabetic nephropathy | 97.09% | DL |
| 11 | chronic pulmonary heart disease | 96.53% | DL |
| 12 | obsolete susceptibility to ischemic stroke | 95.70% | DL |
| 13 | brain stem infarction | 95.05% | DL |
| 14 | intracerebral hemorrhage | 94.63% | DL |
| 15 | cerebral infarction | 93.73% | DL |
| 16 | cerebral arterial disease | 90.39% | DL |
| 17 | cerebral artery occlusion | 89.83% | DL |
| 18 | MRI defined brain infarct | 86.14% | DL |
| 19 | ABri amyloidosis | 82.94% | DL |
| 20 | cerebrovascular disorder | 82.24% | DL |

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
