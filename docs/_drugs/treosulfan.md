---
layout: default
title: Treosulfan
description: "Treosulfan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 607
evidence_level: L5
indication_count: 50
---

# Treosulfan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Treosulfan |
| DrugBank ID | [DB11678](https://go.drugbank.com/drugs/DB11678) |
| Brand Names (EU) | Trecondi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.01% |

---

## Approved Indication (EMA)

Treosulfan in combination with fludarabine is indicated as part of conditioning treatment prior to allogeneic haematopoietic stem cell transplantation (alloHSCT) in adult patients&nbsp;and in paediatric patients older than one month with malignant and non-malignant diseases.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetic cataract | 99.01% | DL |
| 2 | cortical cataract | 98.96% | DL |
| 3 | nuclear senile cataract | 98.96% | DL |
| 4 | immature cataract | 98.95% | DL |
| 5 | craniostenosis cataract | 98.95% | DL |
| 6 | tetanic cataract | 98.95% | DL |
| 7 | diabetes mellitus type 2 associated cataract | 98.95% | DL |
| 8 | mature cataract | 98.95% | DL |
| 9 | diabetic retinopathy | 98.93% | DL |
| 10 | senile cataract | 98.92% | DL |
| 11 | severe nonproliferative diabetic retinopathy | 98.90% | DL |
| 12 | odontogenic cyst | 96.61% | DL |
| 13 | bronchial adenomas/carcinoids childhood | 96.60% | DL |
| 14 | chondroid hamartoma | 96.60% | DL |
| 15 | ductal or ductular proliferation | 96.60% | DL |
| 16 | non-seminomatous lesion | 96.60% | DL |
| 17 | pre-malignant neoplasm | 96.58% | DL |
| 18 | tumor of testis and paratestis | 96.56% | DL |
| 19 | thyroglossal duct cyst | 96.53% | DL |
| 20 | nasopharyngeal teratoma | 96.52% | DL |

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
