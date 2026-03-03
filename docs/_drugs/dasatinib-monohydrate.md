---
layout: default
title: Dasatinib Monohydrate
description: "Dasatinib Monohydrate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 159
evidence_level: L5
indication_count: 50
---

# Dasatinib Monohydrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dasatinib Monohydrate |
| DrugBank ID | [DB01254](https://go.drugbank.com/drugs/DB01254) |
| Brand Names (EU) | Dasatinib Accord Healthcare |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.90% |

---

## Approved Indication (EMA)

Dasatinib Accord Healthcare is indicated for the treatment of adult patients with:  newly diagnosed Philadelphia chromosome positive (Ph+) chronic myelogenous leukaemia (CML) in the chronic phase. chronic, accelerated or blast phase CML with resistance or intolerance to prior therapy including imatinib. Ph+ acute lymphoblastic leukaemia (ALL) and lymphoid blast CML with resistance or intolerance to prior therapy.  &nbsp;Dasatinib Accord Healthcare is indicated for the treatment of paediatric pat

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Ewing sarcoma | 99.90% | DL |
| 2 | myeloid leukemia | 99.68% | DL |
| 3 | liposarcoma | 99.67% | DL |
| 4 | fibromatosis, gingival | 99.65% | DL |
| 5 | dermatofibrosarcoma protuberans | 99.65% | DL |
| 6 | ovarian myxoid liposarcoma | 99.59% | DL |
| 7 | ganglioneuroblastoma (disease) | 99.59% | DL |
| 8 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.59% | DL |
| 9 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 99.58% | DL |
| 10 | hamartoma of lung | 99.56% | DL |
| 11 | fibroma of lung | 99.55% | DL |
| 12 | junctional epidermolysis bullosa | 99.53% | DL |
| 13 | lung benign neoplasm | 99.52% | DL |
| 14 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.52% | DL |
| 15 | lung hilum carcinoma | 99.50% | DL |
| 16 | lung cancer | 99.48% | DL |
| 17 | retroperitoneal neoplasm | 99.48% | DL |
| 18 | neuroblastoma | 99.48% | DL |
| 19 | pulmonary sulcus neoplasm | 99.47% | DL |
| 20 | lung germ cell tumor | 99.47% | DL |

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
