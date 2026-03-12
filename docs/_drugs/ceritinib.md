---
layout: default
title: Ceritinib
description: "Ceritinib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 127
evidence_level: L5
indication_count: 51
---

# Ceritinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ceritinib |
| DrugBank ID | [DB09063](https://go.drugbank.com/drugs/DB09063) |
| Brand Names (EU) | Zykadia |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.86% |

---

## Approved Indication (EMA)

Zykadia is indicated for the treatment of adult patients with anaplastic lymphoma kinase (ALK) positive advanced non small cell lung cancer (NSCLC) previously treated with crizotinib.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | fibromatosis, gingival | 99.86% | DL |
| 2 | fibroma of lung | 99.82% | DL |
| 3 | hamartoma of lung | 99.81% | DL |
| 4 | lung hilum carcinoma | 99.80% | DL |
| 5 | lung benign neoplasm | 99.80% | DL |
| 6 | pulmonary sulcus neoplasm | 99.80% | DL |
| 7 | lung germ cell tumor | 99.80% | DL |
| 8 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 99.79% | DL |
| 9 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.78% | DL |
| 10 | junctional epidermolysis bullosa | 99.77% | DL |
| 11 | ovarioleukodystrophy | 99.72% | DL |
| 12 | junctional epidermolysis bullosa, non-Herlitz type | 99.71% | DL |
| 13 | lung cancer | 99.71% | DL |
| 14 | dehydratase deficiency | 99.68% | DL |
| 15 | Ewing sarcoma | 98.81% | DL |
| 16 | amyotrohpic lateral sclerosis type 22 | 94.01% | DL |
| 17 | orbit sarcoma | 93.89% | DL |
| 18 | synovial chondromatosis | 93.89% | DL |
| 19 | ganglioneuroblastoma (disease) | 93.45% | DL |
| 20 | giant cell tumor of soft tissue | 93.43% | DL |

*Showing top 20 of 51 predictions.*

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
