---
layout: default
title: Cabazitaxel
description: "Cabazitaxel drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 104
evidence_level: L5
indication_count: 50
---

# Cabazitaxel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cabazitaxel |
| DrugBank ID | [DB06772](https://go.drugbank.com/drugs/DB06772) |
| Brand Names (EU) | Jevtana |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Jevtana in combination with prednisone or prednisolone is indicated for the treatment of patients with hormone-refractory metastatic prostate cancer previously treated with a docetaxel-containing regimen.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | female breast carcinoma | 99.92% | DL |
| 2 | sickle cell-hemoglobin d disease syndrome | 99.89% | DL |
| 3 | hereditary persistence of fetal hemoglobin-sickle cell disease syndrome | 99.89% | DL |
| 4 | sickle cell-beta-thalassemia disease syndrome | 99.89% | DL |
| 5 | sickle cell-hemoglobin c disease syndrome | 99.89% | DL |
| 6 | sickle cell-hemoglobin E disease syndrome | 99.89% | DL |
| 7 | HIV infectious disease | 99.82% | DL |
| 8 | hyperthyroidism | 99.77% | DL |
| 9 | neuroblastoma | 99.75% | DL |
| 10 | rheumatoid arthritis | 99.72% | DL |
| 11 | collagenopathy | 99.72% | DL |
| 12 | lymphocytic hypereosinophilic syndrome | 99.70% | DL |
| 13 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.69% | DL |
| 14 | myeloid leukemia | 99.69% | DL |
| 15 | simian immunodeficiency virus infection | 99.69% | DL |
| 16 | feline acquired immunodeficiency syndrome | 99.69% | DL |
| 17 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 99.67% | DL |
| 18 | ganglioneuroblastoma (disease) | 99.65% | DL |
| 19 | retroperitoneal neoplasm | 99.62% | DL |
| 20 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.59% | DL |

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
