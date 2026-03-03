---
layout: default
title: Trastuzumab Emtansine
description: "Trastuzumab Emtansine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 604
evidence_level: L5
indication_count: 50
---

# Trastuzumab Emtansine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Trastuzumab Emtansine |
| DrugBank ID | [DB05773](https://go.drugbank.com/drugs/DB05773) |
| Brand Names (EU) | Kadcyla |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.90% |

---

## Approved Indication (EMA)

Early Breast Cancer (EBC) Kadcyla, as a single agent, is indicated for the adjuvant treatment of adult patients with HER2-positive early breast cancer who have residual invasive disease, in the breast and/or lymph nodes, after neoadjuvant taxane-based and HER2-targeted therapy. Metastatic Breast Cancer (MBC) Kadcyla, as a single agent, is indicated for the treatment of adult patients with HER2-positive, unresectable locally advanced or metastatic breast cancer who previously received trastuzumab

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HER2 positive breast carcinoma | 99.90% | DL |
| 2 | progesterone-receptor positive breast cancer | 99.82% | DL |
| 3 | normal breast-like subtype of breast carcinoma | 99.82% | DL |
| 4 | progesterone-receptor negative breast cancer | 99.82% | DL |
| 5 | breast tumor luminal A or B | 99.81% | DL |
| 6 | synovium cancer | 97.50% | DL |
| 7 | tenosynovial giant cell tumor | 96.73% | DL |
| 8 | tenosynovial giant cell tumor, localized type | 96.17% | DL |
| 9 | malignant giant cell tumor | 96.05% | DL |
| 10 | human herpesvirus 8-related tumor | 95.54% | DL |
| 11 | ectomesenchymoma | 95.52% | DL |
| 12 | malignant cutaneous granular cell skin tumor | 95.47% | DL |
| 13 | benign neoplasm of tongue | 95.47% | DL |
| 14 | cervical neuroblastoma | 95.45% | DL |
| 15 | schwannoma of jugular foramen | 95.45% | DL |
| 16 | benign neoplasm of hypopharynx | 95.43% | DL |
| 17 | benign neoplasm of buccal mucosa | 95.42% | DL |
| 18 | jugular foramen meningioma | 95.40% | DL |
| 19 | neoplasm of major salivary gland | 95.38% | DL |
| 20 | kidney pelvis sarcomatoid transitional cell carcinoma | 95.37% | DL |

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
