---
layout: default
title: Nilotinib
description: "Nilotinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 403
evidence_level: L5
indication_count: 50
---

# Nilotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nilotinib |
| DrugBank ID | [DB04868](https://go.drugbank.com/drugs/DB04868) |
| Brand Names (EU) | Nilotinib Accord |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.31% |

---

## Approved Indication (EMA)

Nilotinib Accord is indicated for the treatment of: - adult and paediatric patients with newly diagnosed Philadelphia chromosome positive chronic myelogenous leukaemia (CML) in the chronic phase, - adult patients with chronic phase and accelerated phase Philadelphia chromosome positive CML with resistance or intolerance to prior therapy including imatinib. Efficacy data in patients with CML in blast crisis are not available, - paediatric patients with chronic phase Philadelphia chromosome positi

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatofibrosarcoma protuberans | 99.31% | DL |
| 2 | liposarcoma | 98.85% | DL |
| 3 | ovarian myxoid liposarcoma | 98.74% | DL |
| 4 | Ewing sarcoma | 98.45% | DL |
| 5 | ganglioneuroblastoma (disease) | 97.02% | DL |
| 6 | heart fibrosarcoma | 97.01% | DL |
| 7 | vertebral anomalies and variable endocrine and T-cell dysfunction | 96.94% | DL |
| 8 | kidney fibrosarcoma | 96.90% | DL |
| 9 | fibroblastic neoplasm | 96.90% | DL |
| 10 | conventional fibrosarcoma | 96.79% | DL |
| 11 | low grade fibromyxoid sarcoma | 96.61% | DL |
| 12 | uterine corpus sarcoma | 96.36% | DL |
| 13 | retroperitoneal neoplasm | 96.22% | DL |
| 14 | vulva sarcoma | 95.61% | DL |
| 15 | neuroblastoma | 95.59% | DL |
| 16 | myeloid leukemia | 95.35% | DL |
| 17 | chronic myelogenous leukemia, BCR-ABL1 positive | 94.87% | DL |
| 18 | liver fibrosarcoma | 94.81% | DL |
| 19 | fibromatosis, gingival | 94.64% | DL |
| 20 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 94.33% | DL |

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
