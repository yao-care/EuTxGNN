---
layout: default
title: Glycopyrronium
description: "Glycopyrronium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 274
evidence_level: L5
indication_count: 50
---

# Glycopyrronium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Glycopyrronium |
| DrugBank ID | [DB00986](https://go.drugbank.com/drugs/DB00986) |
| Brand Names (EU) | Glycopyrronium |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.84% |

---

## Approved Indication (EMA)

Bevespi Aerosphere is indicated as a maintenance bronchodilator treatment to relieve symptoms in adult patients with chronic obstructive pulmonary disease (COPD).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | irritable bowel syndrome | 98.84% | DL |
| 2 | cauda equina syndrome | 98.51% | DL |
| 3 | obsolete neurogenic bladder (disease) | 97.73% | DL |
| 4 | neurocirculatory asthenia | 96.91% | DL |
| 5 | migraine disorder | 96.08% | DL |
| 6 | migraine with brainstem aura | 95.68% | DL |
| 7 | open-angle glaucoma | 95.61% | DL |
| 8 | autonomic nervous system disease | 95.55% | DL |
| 9 | primary hereditary glaucoma | 95.30% | DL |
| 10 | dysthymic disorder | 93.68% | DL |
| 11 | common cold | 93.27% | DL |
| 12 | dysautonomia | 92.51% | DL |
| 13 | headache disorder | 90.90% | DL |
| 14 | familial mitral valve prolapse | 90.49% | DL |
| 15 | mitral valve prolapse (disease) | 90.45% | DL |
| 16 | insomnia (disease) | 89.67% | DL |
| 17 | MVP1 | 89.48% | DL |
| 18 | multiple system atrophy | 89.27% | DL |
| 19 | trigeminal autonomic cephalalgia | 89.19% | DL |
| 20 | atrophoderma vermiculata | 88.78% | DL |

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
