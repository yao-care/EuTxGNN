---
layout: default
title: Pomalidomide
description: "Pomalidomide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 464
evidence_level: L5
indication_count: 50
---

# Pomalidomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pomalidomide |
| DrugBank ID | [DB08910](https://go.drugbank.com/drugs/DB08910) |
| Brand Names (EU) | Pomalidomide Accord |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 93.96% |

---

## Approved Indication (EMA)

Pomalidomide Accord in combination with bortezomib and dexamethasone is indicated in the treatment of adult patients with multiple myeloma who have received at least one prior treatment regimen including lenalidomide. Pomalidomide Accord in combination with dexamethasone is indicated in the treatment of adult patients with relapsed and refractory multiple myeloma who have received at least two prior treatment regimens, including both lenalidomide and bortezomib, and have demonstrated disease pro

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | indolent plasma cell myeloma | 93.96% | DL |
| 2 | plasma cell myeloma | 92.01% | DL |
| 3 | CMM7 | 74.95% | DL |
| 4 | pediatric leptomeningeal melanoma | 73.55% | DL |
| 5 | vulvar melanoma (disease) | 73.32% | DL |
| 6 | epithelioid cell uveal melanoma | 72.21% | DL |
| 7 | melanoma | 63.30% | DL |
| 8 | cholangiocarcinoma, susceptibility to | 60.26% | DL |
| 9 | congenital temporomandibular joint ankylosis | 59.62% | DL |
| 10 | polydipsia | 59.25% | DL |
| 11 | ganglioneuroblastoma (disease) | 58.68% | DL |
| 12 | atrial flutter (disease) | 58.09% | DL |
| 13 | myeloid leukemia | 57.66% | DL |
| 14 | GCGR-related hyperglucagonemia | 57.22% | DL |
| 15 | epidural abscess | 56.12% | DL |
| 16 | dental caries | 56.05% | DL |
| 17 | mitral valve stenosis | 55.71% | DL |
| 18 | conduct disorder | 55.70% | DL |
| 19 | fetal growth restriction | 55.40% | DL |
| 20 | anuria | 54.85% | DL |

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
