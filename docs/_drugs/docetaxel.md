---
layout: default
title: Docetaxel
description: "Docetaxel drug repurposing predictions from TxGNN. Evidence level L5 with 54 predicted indications."
parent: AI Predictions (L5)
nav_order: 177
evidence_level: L5
indication_count: 54
---

# Docetaxel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **54**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Docetaxel |
| DrugBank ID | [DB01248](https://go.drugbank.com/drugs/DB01248) |
| Brand Names (EU) | Docetaxel Accord, Docetaxel Kabi, Taxotere |
| Evidence Level | L5 |
| Predicted Indications | 54 |
| Top Prediction Score | 99.90% |

---

## Approved Indication (EMA)

Breast cancer Taxotere in combination with doxorubicin and cyclophosphamide is indicated for the adjuvant treatment of patients with:  operable node-positive breast cancer; operable node-negative breast cancer.  For patients with operable node-negative breast cancer, adjuvant treatment should be restricted to patients eligible to receive chemotherapy according to internationally established criteria for primary therapy of early breast cancer. Taxotere in combination with doxorubicin is indicated

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | female breast carcinoma | 99.90% | DL |
| 2 | Ewing sarcoma | 99.90% | DL |
| 3 | well-differentiated fetal adenocarcinoma of the lung | 99.84% | DL |
| 4 | small cell lung carcinoma | 99.83% | DL |
| 5 | primary pulmonary lymphoma | 99.83% | DL |
| 6 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.80% | DL |
| 7 | pulmonary blastoma | 99.80% | DL |
| 8 | rhabdomyosarcoma (disease) | 99.79% | DL |
| 9 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.76% | DL |
| 10 | parameningeal embryonal rhabdomyosarcoma | 99.76% | DL |
| 11 | hereditary breast ovarian cancer syndrome | 99.75% | DL |
| 12 | prostate embryonal rhabdomyosarcoma | 99.74% | DL |
| 13 | extrahepatic bile duct rhabdomyosarcoma | 99.73% | DL |
| 14 | liver sarcoma | 99.73% | DL |
| 15 | uterine corpus sarcoma | 99.72% | DL |
| 16 | synovial chondromatosis | 99.67% | DL |
| 17 | orbit sarcoma | 99.67% | DL |
| 18 | giant cell tumor of soft tissue | 99.59% | DL |
| 19 | sarcoma, avian | 99.56% | DL |
| 20 | lung mixed small cell and squamous cell carcinoma | 99.44% | DL |

*Showing top 20 of 54 predictions.*

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
