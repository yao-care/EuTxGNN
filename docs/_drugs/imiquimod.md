---
layout: default
title: Imiquimod
description: "Imiquimod drug repurposing predictions from TxGNN. Evidence level L5 with 60 predicted indications."
parent: AI Predictions (L5)
nav_order: 296
evidence_level: L5
indication_count: 60
---

# Imiquimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **60**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Imiquimod |
| DrugBank ID | [DB00724](https://go.drugbank.com/drugs/DB00724) |
| Brand Names (EU) | Aldara, Zyclara |
| Evidence Level | L5 |
| Predicted Indications | 60 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Imiquimod cream is indicated for the topical treatment of :  External genital and perianal warts (condylomata acuminata) in adults. Small superficial basal cell carcinomas (sBCCs) in adults. Clinically typical, nonhyperkeratotic, nonhypertrophic actinic keratoses (AKs) on the face or scalp in immunocompetent adult patients when size or number of lesions limit the efficacy and/or acceptability of cryotherapy and other topical treatment options are contraindicated or less appropriate.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pre-malignant neoplasm | 99.92% | DL |
| 2 | benign neoplasm of buccal mucosa | 99.91% | DL |
| 3 | cervical neuroblastoma | 99.91% | DL |
| 4 | odontogenic cyst | 99.91% | DL |
| 5 | benign neoplasm of tongue | 99.91% | DL |
| 6 | nasopharyngeal teratoma | 99.91% | DL |
| 7 | cystic neoplasm | 99.91% | DL |
| 8 | inner ear neoplasm | 99.91% | DL |
| 9 | neoplasm of major salivary gland | 99.91% | DL |
| 10 | schwannoma of jugular foramen | 99.91% | DL |
| 11 | benign neoplasm of hypopharynx | 99.91% | DL |
| 12 | thyroglossal duct cyst | 99.91% | DL |
| 13 | ductal or ductular proliferation | 99.91% | DL |
| 14 | non-seminomatous lesion | 99.91% | DL |
| 15 | chondroid hamartoma | 99.91% | DL |
| 16 | bronchial adenomas/carcinoids childhood | 99.91% | DL |
| 17 | benign neoplasm of salivary gland | 99.91% | DL |
| 18 | jugular foramen meningioma | 99.91% | DL |
| 19 | benign neoplasm of floor of mouth | 99.90% | DL |
| 20 | epiglottis neoplasm | 99.90% | DL |

*Showing top 20 of 60 predictions.*

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
