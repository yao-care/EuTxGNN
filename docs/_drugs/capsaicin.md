---
layout: default
title: Capsaicin
description: "Capsaicin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 114
evidence_level: L5
indication_count: 51
---

# Capsaicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Capsaicin |
| DrugBank ID | [DB06774](https://go.drugbank.com/drugs/DB06774) |
| Brand Names (EU) | Qutenza |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.86% |

---

## Approved Indication (EMA)

Qutenza is indicated for the treatment of peripheral neuropathic pain in adults either alone or in combination with other medicinal products for pain.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | neuralgia | 98.86% | DL |
| 2 | otitis externa | 98.76% | DL |
| 3 | post-bacterial disorder | 98.73% | DL |
| 4 | postinfectious vasculitis | 98.71% | DL |
| 5 | infective urethral stricture | 98.70% | DL |
| 6 | post-infectious syndrome | 98.66% | DL |
| 7 | Chagas cardiomyopathy | 98.61% | DL |
| 8 | papillary conjunctivitis | 98.59% | DL |
| 9 | infection-related hemolytic uremic syndrome | 98.52% | DL |
| 10 | tinea corporis | 98.06% | DL |
| 11 | rosacea conjunctivitis | 96.63% | DL |
| 12 | rosacea | 96.53% | DL |
| 13 | atopic conjunctivitis | 96.28% | DL |
| 14 | lichen disease | 95.89% | DL |
| 15 | glossodynia | 95.58% | DL |
| 16 | coccygodynia | 95.48% | DL |
| 17 | blepharoconjunctivitis | 95.22% | DL |
| 18 | rhinitis | 95.00% | DL |
| 19 | cauda equina syndrome | 94.98% | DL |
| 20 | pityriasis simplex | 94.69% | DL |

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
