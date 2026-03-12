---
layout: default
title: Ixazomib Citrate
description: "Ixazomib Citrate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 320
evidence_level: L5
indication_count: 50
---

# Ixazomib Citrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ixazomib Citrate |
| DrugBank ID | [DB09570](https://go.drugbank.com/drugs/DB09570) |
| Brand Names (EU) | Ninlaro |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.17% |

---

## Approved Indication (EMA)

Ninlaro in combination with lenalidomide and dexamethasone is indicated for the treatment of adult patients with multiple myeloma who have received at least one prior therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | indolent plasma cell myeloma | 96.17% | DL |
| 2 | plasma cell myeloma | 94.91% | DL |
| 3 | CMM7 | 81.96% | DL |
| 4 | pediatric leptomeningeal melanoma | 80.85% | DL |
| 5 | vulvar melanoma (disease) | 80.35% | DL |
| 6 | epithelioid cell uveal melanoma | 79.61% | DL |
| 7 | ganglioneuroblastoma (disease) | 73.87% | DL |
| 8 | melanoma | 72.89% | DL |
| 9 | retroperitoneal neoplasm | 70.99% | DL |
| 10 | vertebral anomalies and variable endocrine and T-cell dysfunction | 68.59% | DL |
| 11 | intellectual disability, autosomal dominant 55, with seizures | 61.99% | DL |
| 12 | neuroblastoma | 61.18% | DL |
| 13 | fetal growth restriction | 60.31% | DL |
| 14 | epidural abscess | 59.62% | DL |
| 15 | cholangiocarcinoma, susceptibility to | 59.61% | DL |
| 16 | GCGR-related hyperglucagonemia | 58.93% | DL |
| 17 | congenital temporomandibular joint ankylosis | 58.45% | DL |
| 18 | polydipsia | 58.00% | DL |
| 19 | dental caries | 57.03% | DL |
| 20 | atrial flutter (disease) | 56.75% | DL |

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
