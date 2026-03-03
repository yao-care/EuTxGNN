---
layout: default
title: Fostamatinib Disodium
description: "Fostamatinib Disodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 256
evidence_level: L5
indication_count: 50
---

# Fostamatinib Disodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fostamatinib Disodium |
| DrugBank ID | [DB12010](https://go.drugbank.com/drugs/DB12010) |
| Brand Names (EU) | Tavlesse |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.83% |

---

## Approved Indication (EMA)

Tavlesse is indicated for the treatment of chronic immune thrombocytopenia (ITP) in adult patients who are refractory to other treatments.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | thrombocytopenia due to immune destruction | 99.83% | DL |
| 2 | autosomal thrombocytopenia with normal platelets | 99.45% | DL |
| 3 | non-syndromic esophageal malformation | 99.05% | DL |
| 4 | syndromic constitutional thrombocytopenia | 98.97% | DL |
| 5 | glaucoma | 98.70% | DL |
| 6 | biotin metabolic disease | 98.69% | DL |
| 7 | primary hereditary glaucoma | 98.60% | DL |
| 8 | open-angle glaucoma | 98.45% | DL |
| 9 | filariasis | 98.42% | DL |
| 10 | vitamin deficiency disorder | 98.25% | DL |
| 11 | esophageal disease | 97.88% | DL |
| 12 | neonatal thrombocytopenia | 97.86% | DL |
| 13 | tinea nigra | 97.80% | DL |
| 14 | anogenital human papillomavirus infection | 97.62% | DL |
| 15 | herpes simplex virus keratitis | 97.59% | DL |
| 16 | HER2 positive breast carcinoma | 97.52% | DL |
| 17 | photosensitivity disease | 97.47% | DL |
| 18 | female breast carcinoma | 97.05% | DL |
| 19 | esotropia | 96.96% | DL |
| 20 | progesterone-receptor negative breast cancer | 96.62% | DL |

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
