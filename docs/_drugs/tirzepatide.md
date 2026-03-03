---
layout: default
title: Tirzepatide
description: "Tirzepatide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 586
evidence_level: L5
indication_count: 50
---

# Tirzepatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tirzepatide |
| DrugBank ID | [DB15171](https://go.drugbank.com/drugs/DB15171) |
| Brand Names (EU) | Mounjaro |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.75% |

---

## Approved Indication (EMA)

Type 2 diabetes mellitus Mounjaro is indicated for the treatment of adults with insufficiently controlled type 2 diabetes mellitus as an adjunct to diet and exercise  as monotherapy when metformin is considered inappropriate due to intolerance or contraindications in addition to other medicinal products for the treatment of diabetes.  For study results with respect to combinations, effects on glycaemic control and the populations studied, see sections 4.4, 4.5 and 5.1. Weight management Mounjaro

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | gout | 96.75% | DL |
| 2 | osteoarthritis | 95.92% | DL |
| 3 | pseudoachondroplasia | 94.81% | DL |
| 4 | osteoarthritis susceptibility | 94.63% | DL |
| 5 | benign prostatic hyperplasia (disease) | 94.04% | DL |
| 6 | rheumatoid arthritis | 93.60% | DL |
| 7 | acromesomelic dysplasia, Hunter-Thompson type | 93.53% | DL |
| 8 | brachyolmia | 93.13% | DL |
| 9 | brachyolmia-amelogenesis imperfecta syndrome | 92.86% | DL |
| 10 | myosclerosis | 92.82% | DL |
| 11 | idiopathic granulomatous myositis | 91.97% | DL |
| 12 | myositis fibrosa | 91.97% | DL |
| 13 | headache disorder | 91.73% | DL |
| 14 | Prinzmetal angina | 91.72% | DL |
| 15 | tendinitis | 91.61% | DL |
| 16 | arthropathy | 91.59% | DL |
| 17 | trigeminal autonomic cephalalgia | 91.10% | DL |
| 18 | female breast carcinoma | 91.03% | DL |
| 19 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 91.02% | DL |
| 20 | brachydactyly-syndactyly syndrome | 90.69% | DL |

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
