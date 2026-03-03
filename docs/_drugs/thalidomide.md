---
layout: default
title: Thalidomide
description: "Thalidomide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 576
evidence_level: L5
indication_count: 50
---

# Thalidomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Thalidomide |
| DrugBank ID | [DB01041](https://go.drugbank.com/drugs/DB01041) |
| Brand Names (EU) | Thalidomide BMS (previously Thalidomide Celgene) |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.96% |

---

## Approved Indication (EMA)

Thalidomide BMS in combination with melphalan and prednisone as first line treatment of patients with untreated multiple myeloma, aged &gt;/= 65 years or ineligible for high dose chemotherapy. Thalidomide BMS is prescribed and dispensed according to the Thalidomide Celgene Pregnancy Prevention Programme (see section 4.4).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ganglioneuroblastoma (disease) | 98.96% | DL |
| 2 | vertebral anomalies and variable endocrine and T-cell dysfunction | 98.95% | DL |
| 3 | retroperitoneal neoplasm | 98.68% | DL |
| 4 | neuroblastoma | 98.66% | DL |
| 5 | brachydactyly-syndactyly syndrome | 94.22% | DL |
| 6 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 93.20% | DL |
| 7 | rheumatoid arthritis | 92.40% | DL |
| 8 | myeloid leukemia | 90.54% | DL |
| 9 | indolent plasma cell myeloma | 88.46% | DL |
| 10 | plasma cell myeloma | 85.34% | DL |
| 11 | acute lymphoblastic leukemia (disease) | 74.75% | DL |
| 12 | cholangiocarcinoma, susceptibility to | 64.32% | DL |
| 13 | GCGR-related hyperglucagonemia | 60.49% | DL |
| 14 | scalp dermatosis | 59.90% | DL |
| 15 | congenital temporomandibular joint ankylosis | 59.59% | DL |
| 16 | polydipsia | 59.20% | DL |
| 17 | mitral valve prolapse, myxomatous | 58.87% | DL |
| 18 | epidural abscess | 57.97% | DL |
| 19 | giant cell reparative granuloma | 57.02% | DL |
| 20 | pancreas, dorsal, agenesis of | 56.94% | DL |

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
