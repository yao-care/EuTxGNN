---
layout: default
title: Valsartan
description: "valsartan drug repurposing predictions from TxGNN. Evidence level L1 with 51 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 620
evidence_level: L1
indication_count: 51
---

# Valsartan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Valsartan |
| DrugBank ID | [DB00177](https://go.drugbank.com/drugs/DB00177) |
| Brand Names (EU) | Neparvis, Valsartan |
| Evidence Level | L1 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Treatment of essential hypertension. Amlodipine/Valsartan Mylan is indicated in adults whose blood pressure is not adequately controlled on amlodipine or valsartan monotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | malignant renovascular hypertension | 99.97% | DL |
| 2 | malignant hypertensive renal disease | 99.97% | DL |
| 3 | pulmonary hypertension with unclear multifactorial mechanism | 99.97% | DL |
| 4 | pulmonary hypertension owing to lung disease and/or hypoxia | 99.97% | DL |
| 5 | hypertensive disorder | 99.97% | DL |
| 6 | Braddock syndrome | 99.96% | DL |
| 7 | chronic pulmonary heart disease | 99.58% | DL |
| 8 | Prinzmetal angina | 99.45% | DL |
| 9 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 98.50% | DL |
| 10 | brain small vessel disease 1 with or without ocular anomalies | 98.47% | DL |
| 11 | obsolete susceptibility to ischemic stroke | 98.22% | DL |
| 12 | intracerebral hemorrhage | 97.68% | DL |
| 13 | brain stem infarction | 96.95% | DL |
| 14 | cerebrovascular disorder | 95.62% | DL |
| 15 | diabetic nephropathy | 95.44% | DL |
| 16 | ABri amyloidosis | 93.55% | DL |
| 17 | cerebral artery occlusion | 92.89% | DL |
| 18 | cerebral infarction | 92.48% | DL |
| 19 | MRI defined brain infarct | 90.24% | DL |
| 20 | stroke disorder | 89.01% | DL |

*Showing top 20 of 51 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| hypertensive disorder | L1 | 20 | 0 | 10 Phase 3 trial(s) |

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
