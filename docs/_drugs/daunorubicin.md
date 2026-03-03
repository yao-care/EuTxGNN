---
layout: default
title: Daunorubicin
description: "Daunorubicin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 160
evidence_level: L5
indication_count: 50
---

# Daunorubicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Daunorubicin |
| DrugBank ID | [DB00694](https://go.drugbank.com/drugs/DB00694) |
| Brand Names (EU) | Daunorubicin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.82% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute lymphoblastic/lymphocytic leukemia | 99.82% | DL |
| 2 | Hodgkins lymphoma | 99.81% | DL |
| 3 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.80% | DL |
| 4 | ganglioneuroblastoma (disease) | 99.80% | DL |
| 5 | neuroblastoma | 99.78% | DL |
| 6 | ALK-positive large B-cell lymphoma | 99.78% | DL |
| 7 | adenosarcoma | 99.77% | DL |
| 8 | retroperitoneal neoplasm | 99.77% | DL |
| 9 | small cell lung carcinoma | 99.76% | DL |
| 10 | primary pulmonary lymphoma | 99.76% | DL |
| 11 | pulmonary blastoma | 99.76% | DL |
| 12 | well-differentiated fetal adenocarcinoma of the lung | 99.75% | DL |
| 13 | upper aerodigestive tract neoplasm | 99.74% | DL |
| 14 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.73% | DL |
| 15 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.73% | DL |
| 16 | leukemia, lymphocytic, susceptibility to | 99.72% | DL |
| 17 | obsolete Hodgkin's granuloma | 99.71% | DL |
| 18 | uterine ligament adenosarcoma | 99.69% | DL |
| 19 | myeloid leukemia | 99.67% | DL |
| 20 | osteopathia striata with cranial sclerosis | 99.63% | DL |

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
