---
layout: default
title: Parecoxib Sodium
description: "Parecoxib Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 440
evidence_level: L5
indication_count: 50
---

# Parecoxib Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Parecoxib Sodium |
| DrugBank ID | [DB08439](https://go.drugbank.com/drugs/DB08439) |
| Brand Names (EU) | Dynastat |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.55% |

---

## Approved Indication (EMA)

For the short-term treatment of postoperative pain in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.55% | DL |
| 2 | migraine with brainstem aura | 99.46% | DL |
| 3 | migraine with or without aura, susceptibility to | 99.38% | DL |
| 4 | pulmonary hypertension | 99.09% | DL |
| 5 | headache disorder | 98.90% | DL |
| 6 | kyphoscoliotic heart disease | 98.81% | DL |
| 7 | trigeminal autonomic cephalalgia | 98.68% | DL |
| 8 | atrophoderma vermiculata | 98.64% | DL |
| 9 | rheumatoid arthritis | 98.35% | DL |
| 10 | ulerythema ophryogenesis | 98.33% | DL |
| 11 | benign prostatic hyperplasia (disease) | 98.25% | DL |
| 12 | tendinitis | 97.93% | DL |
| 13 | alopecia | 97.89% | DL |
| 14 | peripheral vascular disease | 97.84% | DL |
| 15 | congenital hypotrichosis milia | 97.79% | DL |
| 16 | fibromyalgia | 97.71% | DL |
| 17 | myositis fibrosa | 97.70% | DL |
| 18 | idiopathic granulomatous myositis | 97.70% | DL |
| 19 | hypotrichosis simplex of the scalp | 97.67% | DL |
| 20 | diffuse alopecia areata | 97.59% | DL |

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
