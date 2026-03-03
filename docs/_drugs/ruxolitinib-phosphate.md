---
layout: default
title: Ruxolitinib Phosphate
description: "Ruxolitinib Phosphate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 512
evidence_level: L5
indication_count: 50
---

# Ruxolitinib Phosphate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ruxolitinib Phosphate |
| DrugBank ID | [DB08877](https://go.drugbank.com/drugs/DB08877) |
| Brand Names (EU) | Opzelura |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.73% |

---

## Approved Indication (EMA)

Opzelura is indicated for the treatment of non-segmental vitiligo with facial involvement in adults and adolescents from 12 years of age.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | uterine corpus perivascular epithelioid cell tumor | 99.73% | DL |
| 2 | benign PEComa | 99.73% | DL |
| 3 | lymphangiomyoma | 99.72% | DL |
| 4 | lymphangioleiomyomatosis | 99.64% | DL |
| 5 | liposarcoma | 99.52% | DL |
| 6 | familial rhabdoid tumor | 99.49% | DL |
| 7 | lung PEComa | 99.44% | DL |
| 8 | ovarian myxoid liposarcoma | 99.39% | DL |
| 9 | primary myelofibrosis | 99.35% | DL |
| 10 | acquired hemophagocytic lymphohistiocytosis associated with malignant disease | 99.32% | DL |
| 11 | hemophagocytic syndrome associated with an infection | 99.32% | DL |
| 12 | thrombocytopenia | 99.30% | DL |
| 13 | dermatofibrosarcoma protuberans | 99.29% | DL |
| 14 | plasmacytoma | 99.22% | DL |
| 15 | hereditary thrombocytopenia with normal platelets | 99.15% | DL |
| 16 | marcothrombocytopenia with mitral valve insufficiency | 99.14% | DL |
| 17 | transient neonatal thrombocytopenia | 99.12% | DL |
| 18 | dense granule disease | 99.08% | DL |
| 19 | neurolymphomatosis | 98.86% | DL |
| 20 | rhabdoid tumor | 98.66% | DL |

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
