---
layout: default
title: Aliskiren
description: "aliskiren drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 30
evidence_level: L1
indication_count: 50
---

# Aliskiren
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Aliskiren |
| DrugBank ID | [DB09026](https://go.drugbank.com/drugs/DB09026) |
| Brand Names (EU) | Rasilez |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Treatment of essential hypertension.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hypertensive disorder | 99.98% | DL |
| 2 | pulmonary hypertension owing to lung disease and/or hypoxia | 99.98% | DL |
| 3 | pulmonary hypertension with unclear multifactorial mechanism | 99.98% | DL |
| 4 | malignant hypertensive renal disease | 99.98% | DL |
| 5 | malignant renovascular hypertension | 99.98% | DL |
| 6 | Braddock syndrome | 99.97% | DL |
| 7 | chronic pulmonary heart disease | 99.78% | DL |
| 8 | cerebrovascular disorder | 99.19% | DL |
| 9 | obsolete susceptibility to ischemic stroke | 98.78% | DL |
| 10 | brain stem infarction | 97.97% | DL |
| 11 | intracerebral hemorrhage | 96.69% | DL |
| 12 | hypotrichosis simplex of the scalp | 96.63% | DL |
| 13 | cerebral artery occlusion | 96.19% | DL |
| 14 | MRI defined brain infarct | 95.73% | DL |
| 15 | congenital hypotrichosis milia | 95.52% | DL |
| 16 | ABri amyloidosis | 94.79% | DL |
| 17 | cerebral infarction | 94.29% | DL |
| 18 | alopecia | 93.37% | DL |
| 19 | diffuse alopecia areata | 92.82% | DL |
| 20 | cerebral arterial disease | 90.04% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| hypertensive disorder | L1 | 20 | 0 | 9 Phase 3 trial(s), 1 Phase 2 trial(s) |

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
