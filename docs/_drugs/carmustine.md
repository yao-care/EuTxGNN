---
layout: default
title: Carmustine
description: "Carmustine drug repurposing predictions from TxGNN. Evidence level L5 with 87 predicted indications."
parent: AI Predictions (L5)
nav_order: 119
evidence_level: L5
indication_count: 87
---

# Carmustine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **87**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Carmustine |
| DrugBank ID | [DB00262](https://go.drugbank.com/drugs/DB00262) |
| Brand Names (EU) | Carmustine medac (previously Carmustine Obvius) |
| Evidence Level | L5 |
| Predicted Indications | 87 |
| Top Prediction Score | 98.92% |

---

## Approved Indication (EMA)

Carmustine is indicated n adults&nbsp;in the following malignant neoplasms as a single agent or in combination with other antineoplastic agents and/or other therapeutic measures (radiotherapy, surgery):  Brain tumours (glioblastoma, brain-stem gliomas, medulloblastoma, astrocytoma and ependymoma), brain metastases Secondary therapy in non-Hodgkin’s lymphoma and Hodgkin’s disease as conditioning treatment prior to autologous haematopoietic progenitor cell transplantation (HPCT) in malignant haema

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | lymphosarcoma | 98.92% | DL |
| 2 | lymph node cancer | 98.49% | DL |
| 3 | astrocytoma (excluding glioblastoma) | 97.13% | DL |
| 4 | adult astrocytic tumour | 96.88% | DL |
| 5 | cauda equina neoplasm | 96.70% | DL |
| 6 | reticulum cell sarcoma | 96.20% | DL |
| 7 | lymphoma, non-Hodgkin, familial | 95.96% | DL |
| 8 | childhood cerebral astrocytoma | 94.61% | DL |
| 9 | B-cell neoplasm | 94.10% | DL |
| 10 | lymphoma | 94.01% | DL |
| 11 | subependymal giant cell astrocytoma | 93.23% | DL |
| 12 | astrocytic tumor | 93.10% | DL |
| 13 | interdigitating dendritic cell sarcoma | 92.42% | DL |
| 14 | non-Hodgkin lymphoma | 91.90% | DL |
| 15 | colon adenocarcinoma | 91.65% | DL |
| 16 | subcutaneous panniculitis-like T-cell lymphoma | 90.68% | DL |
| 17 | cerebellar astrocytoma | 89.98% | DL |
| 18 | T-cell/histiocyte rich large B cell lymphoma | 89.60% | DL |
| 19 | low grade astrocytic tumor | 89.42% | DL |
| 20 | childhood astrocytic tumor | 89.33% | DL |

*Showing top 20 of 87 predictions.*

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
