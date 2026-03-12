---
layout: default
title: Erlotinib
description: "Erlotinib drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 223
evidence_level: L5
indication_count: 52
---

# Erlotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Erlotinib |
| DrugBank ID | [DB00530](https://go.drugbank.com/drugs/DB00530) |
| Brand Names (EU) | Tarceva |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 95.77% |

---

## Approved Indication (EMA)

Non-small cell lung cancer (NSCLC) Tarceva is also indicated for switch maintenance treatment in patients with locally advanced or metastatic non-small cell lung cancer with EGFR activating mutations and stable disease after first-line chemotherapy. Tarceva is also indicated for the treatment of patients with locally advanced or metastatic non-small cell lung cancer after failure of at least one prior chemotherapy regimen. In patients with tumours without EGFR activating mutations, Tarceva is in

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Ewing sarcoma | 95.77% | DL |
| 2 | fibromatosis, gingival | 95.27% | DL |
| 3 | fibroma of lung | 95.12% | DL |
| 4 | hamartoma of lung | 95.07% | DL |
| 5 | lung benign neoplasm | 95.00% | DL |
| 6 | lung hilum carcinoma | 94.96% | DL |
| 7 | pulmonary sulcus neoplasm | 94.51% | DL |
| 8 | lung germ cell tumor | 94.51% | DL |
| 9 | lung cancer | 94.33% | DL |
| 10 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 93.34% | DL |
| 11 | junctional epidermolysis bullosa | 92.89% | DL |
| 12 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 92.60% | DL |
| 13 | ovarioleukodystrophy | 92.18% | DL |
| 14 | junctional epidermolysis bullosa, non-Herlitz type | 90.62% | DL |
| 15 | salivary gland type cancer of the breast | 90.05% | DL |
| 16 | dehydratase deficiency | 89.87% | DL |
| 17 | breast papillomatosis | 89.53% | DL |
| 18 | uterine corpus sarcoma | 89.02% | DL |
| 19 | giant adenofibroma of the breast | 88.84% | DL |
| 20 | diabetic mastopathy | 88.84% | DL |

*Showing top 20 of 52 predictions.*

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
