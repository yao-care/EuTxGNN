---
layout: default
title: Neratinib
description: "Neratinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 399
evidence_level: L5
indication_count: 50
---

# Neratinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Neratinib |
| DrugBank ID | [DB11828](https://go.drugbank.com/drugs/DB11828) |
| Brand Names (EU) | Nerlynx |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.81% |

---

## Approved Indication (EMA)

Nerlynx is indicated for the extended adjuvant treatment of adult patients with early stage hormone receptor positive HER2-overexpressed/amplified breast cancer and who are less than one year from the completion of prior adjuvant trastuzumab based therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HER2 positive breast carcinoma | 99.81% | DL |
| 2 | normal breast-like subtype of breast carcinoma | 99.68% | DL |
| 3 | progesterone-receptor positive breast cancer | 99.68% | DL |
| 4 | progesterone-receptor negative breast cancer | 99.67% | DL |
| 5 | breast tumor luminal A or B | 99.67% | DL |
| 6 | synovium cancer | 98.08% | DL |
| 7 | tenosynovial giant cell tumor | 97.38% | DL |
| 8 | malignant giant cell tumor | 96.07% | DL |
| 9 | tenosynovial giant cell tumor, localized type | 95.80% | DL |
| 10 | fibroblastic neoplasm | 95.56% | DL |
| 11 | kidney fibrosarcoma | 95.53% | DL |
| 12 | conventional fibrosarcoma | 95.51% | DL |
| 13 | benign PEComa | 95.43% | DL |
| 14 | lymphangiomyoma | 95.40% | DL |
| 15 | heart fibrosarcoma | 95.34% | DL |
| 16 | uterine corpus perivascular epithelioid cell tumor | 95.33% | DL |
| 17 | low grade fibromyxoid sarcoma | 95.29% | DL |
| 18 | dermatofibrosarcoma protuberans | 95.11% | DL |
| 19 | cutaneous undifferentiated pleomorphic sarcoma | 94.70% | DL |
| 20 | malignant tenosynovial giant cell tumor | 94.69% | DL |

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
