---
layout: default
title: Ponatinib
description: "Ponatinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 465
evidence_level: L5
indication_count: 50
---

# Ponatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ponatinib |
| DrugBank ID | [DB08901](https://go.drugbank.com/drugs/DB08901) |
| Brand Names (EU) | Iclusig |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.30% |

---

## Approved Indication (EMA)

Iclusig is indicated in adult patients with  chronic phase, accelerated phase, or blast phase chronic myeloid leukaemia (CML) who are resistant to dasatinib or nilotinib; who are intolerant to dasatinib or nilotinib and for whom subsequent treatment with imatinib is not clinically appropriate; or who have the T315I mutation Philadelphia chromosome positive acute lymphoblastic leukaemia (Ph+ ALL) who are resistant to dasatinib; who are intolerant to dasatinib and for whom subsequent treatment wit

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | chronic myelogenous leukemia, BCR-ABL1 positive | 99.30% | DL |
| 2 | fibromatosis, gingival | 99.04% | DL |
| 3 | liposarcoma | 99.00% | DL |
| 4 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 98.98% | DL |
| 5 | ovarian myxoid liposarcoma | 98.93% | DL |
| 6 | hamartoma of lung | 98.93% | DL |
| 7 | fibroma of lung | 98.87% | DL |
| 8 | junctional epidermolysis bullosa | 98.86% | DL |
| 9 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 98.83% | DL |
| 10 | lung benign neoplasm | 98.83% | DL |
| 11 | lung hilum carcinoma | 98.81% | DL |
| 12 | Ewing sarcoma | 98.79% | DL |
| 13 | familial thrombocytosis | 98.77% | DL |
| 14 | pulmonary sulcus neoplasm | 98.75% | DL |
| 15 | lung germ cell tumor | 98.75% | DL |
| 16 | reactive thrombocytosis | 98.72% | DL |
| 17 | ovarioleukodystrophy | 98.53% | DL |
| 18 | lung cancer | 98.36% | DL |
| 19 | junctional epidermolysis bullosa, non-Herlitz type | 98.35% | DL |
| 20 | dehydratase deficiency | 98.06% | DL |

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
