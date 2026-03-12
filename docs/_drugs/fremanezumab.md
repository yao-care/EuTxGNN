---
layout: default
title: Fremanezumab
description: "fremanezumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 257
evidence_level: L5
indication_count: 50
---

# Fremanezumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fremanezumab |
| DrugBank ID | [DB14041](https://go.drugbank.com/drugs/DB14041) |
| Brand Names (EU) | Ajovy |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

Ajovy is indicated for prophylaxis of migraine in adults who have at least 4&nbsp;migraine days per month.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine with brainstem aura | 99.94% | DL |
| 2 | migraine disorder | 99.94% | DL |
| 3 | migraine with or without aura, susceptibility to | 99.34% | DL |
| 4 | atrophoderma vermiculata | 99.04% | DL |
| 5 | ulerythema ophryogenesis | 98.64% | DL |
| 6 | heparin cofactor 2 deficiency | 96.88% | DL |
| 7 | antithrombin deficiency type 2 | 96.37% | DL |
| 8 | factor 5 excess with spontaneous thrombosis | 96.25% | DL |
| 9 | thrombophilia | 94.31% | DL |
| 10 | amenorrhea (disease) | 92.74% | DL |
| 11 | sciatic neuropathy | 90.32% | DL |
| 12 | hemorrhagic disease of newborn | 80.75% | DL |
| 13 | severe nonproliferative diabetic retinopathy | 65.97% | DL |
| 14 | hyperemesis gravidarum (disease) | 64.24% | DL |
| 15 | hyperparathyroidism, primary, caused by water clear cell hyperplasia | 60.19% | DL |
| 16 | omphalocele (disease) | 59.79% | DL |
| 17 | sudden arrhythmia death syndrome | 59.33% | DL |
| 18 | cauda equina syndrome | 58.98% | DL |
| 19 | prekallikrein deficiency | 58.92% | DL |
| 20 | Coronavinae infectious disease | 58.76% | DL |

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
