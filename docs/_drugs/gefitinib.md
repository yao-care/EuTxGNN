---
layout: default
title: Gefitinib
description: "Gefitinib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 263
evidence_level: L5
indication_count: 51
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Gefitinib |
| DrugBank ID | [DB00317](https://go.drugbank.com/drugs/DB00317) |
| Brand Names (EU) | Iressa |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.89% |

---

## Approved Indication (EMA)

Iressa is indicated for the treatment of adult patients with locally advanced or metastatic non-small-cell lung cancer with activating mutations of epidermal-growth-factor-receptor tyrosine kinase.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | fibromatosis, gingival | 99.89% | DL |
| 2 | fibroma of lung | 99.86% | DL |
| 3 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 99.86% | DL |
| 4 | hamartoma of lung | 99.86% | DL |
| 5 | lung hilum carcinoma | 99.86% | DL |
| 6 | lung benign neoplasm | 99.85% | DL |
| 7 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.84% | DL |
| 8 | lung germ cell tumor | 99.84% | DL |
| 9 | pulmonary sulcus neoplasm | 99.84% | DL |
| 10 | junctional epidermolysis bullosa | 99.84% | DL |
| 11 | ovarioleukodystrophy | 99.81% | DL |
| 12 | lung cancer | 99.81% | DL |
| 13 | junctional epidermolysis bullosa, non-Herlitz type | 99.81% | DL |
| 14 | dehydratase deficiency | 99.78% | DL |
| 15 | Ewing sarcoma | 99.37% | DL |
| 16 | uterine corpus sarcoma | 97.11% | DL |
| 17 | giant cell tumor of soft tissue | 95.60% | DL |
| 18 | orbit sarcoma | 95.57% | DL |
| 19 | synovial chondromatosis | 95.57% | DL |
| 20 | sarcoma, avian | 95.36% | DL |

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
