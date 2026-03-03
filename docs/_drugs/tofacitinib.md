---
layout: default
title: Tofacitinib
description: "Tofacitinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 593
evidence_level: L5
indication_count: 50
---

# Tofacitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tofacitinib |
| DrugBank ID | [DB08895](https://go.drugbank.com/drugs/DB08895) |
| Brand Names (EU) | Xeljanz |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.27% |

---

## Approved Indication (EMA)

Rheumatoid arthritisTofacitinib in combination with methotrexate (MTX) is indicated for the treatment of moderate to severe active rheumatoid arthritis (RA) in adult patients who have responded inadequately to, or who are intolerant to one or more disease-modifying antirheumatic drugs (DMARDs) (see section 5.1). Tofacitinib can be given as monotherapy in case of intolerance to MTX or when treatment with MTX is inappropriate (see sections 4.4 and 4.5). Psoriatic arthritisTofacitinib in combinatio

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.27% | DL |
| 2 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.96% | DL |
| 3 | brachydactyly-syndactyly syndrome | 98.88% | DL |
| 4 | indolent plasma cell myeloma | 96.66% | DL |
| 5 | plasma cell myeloma | 96.09% | DL |
| 6 | myeloid leukemia | 95.43% | DL |
| 7 | ganglioneuroblastoma (disease) | 79.55% | DL |
| 8 | marcothrombocytopenia with mitral valve insufficiency | 76.17% | DL |
| 9 | hereditary thrombocytopenia with normal platelets | 75.76% | DL |
| 10 | vertebral anomalies and variable endocrine and T-cell dysfunction | 75.34% | DL |
| 11 | retroperitoneal neoplasm | 75.26% | DL |
| 12 | transient neonatal thrombocytopenia | 73.38% | DL |
| 13 | dense granule disease | 70.66% | DL |
| 14 | Meester-Loeys syndrome | 65.68% | DL |
| 15 | neuroblastoma | 65.05% | DL |
| 16 | stroke disorder | 62.11% | DL |
| 17 | thrombocytopenia | 61.29% | DL |
| 18 | atrial flutter (disease) | 60.31% | DL |
| 19 | cholangiocarcinoma, susceptibility to | 59.92% | DL |
| 20 | platelet storage pool deficiency | 59.84% | DL |

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
