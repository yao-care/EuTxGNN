---
layout: default
title: Telmisartan
description: "Telmisartan drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 563
evidence_level: L5
indication_count: 51
---

# Telmisartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Telmisartan |
| DrugBank ID | [DB00966](https://go.drugbank.com/drugs/DB00966) |
| Brand Names (EU) | Telmisartan Teva Pharma, Tolucombi |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Treatment of essential hypertension in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | obsolete susceptibility to ischemic stroke | 99.99% | DL |
| 2 | Prinzmetal angina | 99.98% | DL |
| 3 | brain stem infarction | 99.98% | DL |
| 4 | stroke disorder | 99.98% | DL |
| 5 | ABri amyloidosis | 99.97% | DL |
| 6 | cerebral infarction | 99.96% | DL |
| 7 | cerebral artery occlusion | 99.95% | DL |
| 8 | cerebrovascular disorder | 99.95% | DL |
| 9 | pulmonary hypertension owing to lung disease and/or hypoxia | 99.93% | DL |
| 10 | pulmonary hypertension with unclear multifactorial mechanism | 99.93% | DL |
| 11 | malignant renovascular hypertension | 99.93% | DL |
| 12 | malignant hypertensive renal disease | 99.93% | DL |
| 13 | intracerebral hemorrhage | 99.93% | DL |
| 14 | Braddock syndrome | 99.92% | DL |
| 15 | hypertensive disorder | 99.90% | DL |
| 16 | cerebral arterial disease | 99.90% | DL |
| 17 | MRI defined brain infarct | 99.89% | DL |
| 18 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 99.79% | DL |
| 19 | brain small vessel disease 1 with or without ocular anomalies | 99.77% | DL |
| 20 | chronic pulmonary heart disease | 99.65% | DL |

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
