---
layout: default
title: Bevacizumab
description: "Bevacizumab drug repurposing predictions from TxGNN. Evidence level L5 with 70 predicted indications."
parent: AI Predictions (L5)
nav_order: 78
evidence_level: L5
indication_count: 70
---

# Bevacizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **70**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bevacizumab |
| DrugBank ID | [DB00112](https://go.drugbank.com/drugs/DB00112) |
| Brand Names (EU) | Avastin, Avzivi, Lytenava, Mvasi |
| Evidence Level | L5 |
| Predicted Indications | 70 |
| Top Prediction Score | 99.90% |

---

## Approved Indication (EMA)

Mvasi in combination with fluoropyrimidine-based chemotherapy is indicated for treatment of adult patients with metastatic carcinoma of the colon or rectum. Mvasi in combination with paclitaxel is indicated for first-line treatment of adult patients with metastatic breast cancer. For further information as to human epidermal growth factor receptor 2 (HER2) status, please refer to section 5.1. Mvasi, in addition to platinum-based chemotherapy, is indicated for first-line treatment of adult patien

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | epiglottis neoplasm | 99.90% | DL |
| 2 | benign neoplasm of tongue | 99.90% | DL |
| 3 | tumor of testis and paratestis | 99.90% | DL |
| 4 | benign neoplasm of hypopharynx | 99.90% | DL |
| 5 | benign neoplasm of floor of mouth | 99.90% | DL |
| 6 | cervical neuroblastoma | 99.89% | DL |
| 7 | cystic neoplasm | 99.89% | DL |
| 8 | nasal cavity inverting papilloma | 99.89% | DL |
| 9 | mesenchymoma | 99.89% | DL |
| 10 | schwannoma of jugular foramen | 99.89% | DL |
| 11 | thyroglossal duct cyst | 99.89% | DL |
| 12 | inner ear neoplasm | 99.89% | DL |
| 13 | ductal or ductular proliferation | 99.89% | DL |
| 14 | bronchial adenomas/carcinoids childhood | 99.89% | DL |
| 15 | chondroid hamartoma | 99.89% | DL |
| 16 | non-seminomatous lesion | 99.89% | DL |
| 17 | odontogenic cyst | 99.89% | DL |
| 18 | pre-malignant neoplasm | 99.89% | DL |
| 19 | jugular foramen meningioma | 99.89% | DL |
| 20 | vestibulocochlear nerve neoplasm | 99.89% | DL |

*Showing top 20 of 70 predictions.*

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
