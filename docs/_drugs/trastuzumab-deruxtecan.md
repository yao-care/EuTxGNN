---
layout: default
title: Trastuzumab Deruxtecan
description: "Trastuzumab Deruxtecan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 603
evidence_level: L5
indication_count: 50
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Trastuzumab Deruxtecan |
| DrugBank ID | [DB14962](https://go.drugbank.com/drugs/DB14962) |
| Brand Names (EU) | Enhertu |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.31% |

---

## Approved Indication (EMA)

Breast cancerHER2-positive breast cancerEnhertu as monotherapy is indicated for the treatment of adult patients with unresectable or metastatic HER2-positive breast cancer who have received one or more prior anti-HER2-based regimens.HER2-low and HER2-ultralow breast cancerEnhertu as monotherapy is indicated for the treatment of adult patients with unresectable or metastatic&nbsp;  hormone receptor (HR)-positive, HER2-low or HER2-ultralow breast cancer who have received at least one endocrine the

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 99.31% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 98.92% | DL |
| 3 | diabetic retinopathy | 98.46% | DL |
| 4 | bronchitis | 98.00% | DL |
| 5 | diabetic cataract | 96.60% | DL |
| 6 | chondroid hamartoma | 95.98% | DL |
| 7 | non-seminomatous lesion | 95.98% | DL |
| 8 | ductal or ductular proliferation | 95.98% | DL |
| 9 | bronchial adenomas/carcinoids childhood | 95.98% | DL |
| 10 | tumor of testis and paratestis | 95.81% | DL |
| 11 | thyroglossal duct cyst | 95.77% | DL |
| 12 | cystic neoplasm | 95.69% | DL |
| 13 | mesenchymoma | 95.67% | DL |
| 14 | benign neoplasm of tongue | 95.60% | DL |
| 15 | cervical neuroblastoma | 95.56% | DL |
| 16 | inner ear neoplasm | 95.56% | DL |
| 17 | indolent plasma cell myeloma | 95.53% | DL |
| 18 | epiglottis neoplasm | 95.53% | DL |
| 19 | benign neoplasm of floor of mouth | 95.52% | DL |
| 20 | hemorrhagic disease of newborn | 95.51% | DL |

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
