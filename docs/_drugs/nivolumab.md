---
layout: default
title: Nivolumab
description: "Nivolumab drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 408
evidence_level: L5
indication_count: 52
---

# Nivolumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nivolumab |
| DrugBank ID | [DB09035](https://go.drugbank.com/drugs/DB09035) |
| Brand Names (EU) | Opdivo, Opdualag |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 98.63% |

---

## Approved Indication (EMA)

Opdualag is indicated for the first line treatment of advanced (unresectable or metastatic) melanoma in adults and adolescents 12 years of age and older with tumour cell PD L1 expression &lt; 1%.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | metastatic melanoma | 98.63% | DL |
| 2 | non-cutaneous melanoma | 98.41% | DL |
| 3 | epithelioid cell melanoma | 98.36% | DL |
| 4 | CDK4 linked melanoma | 98.28% | DL |
| 5 | amelanotic skin melanoma | 98.28% | DL |
| 6 | lentigo maligna melanoma | 98.28% | DL |
| 7 | malignant melanoma of the mucosa | 98.28% | DL |
| 8 | superficial spreading melanoma | 98.28% | DL |
| 9 | balloon cell malignant melanoma | 98.28% | DL |
| 10 | acral lentiginous melanoma (disease) | 98.28% | DL |
| 11 | nodular malignant melanoma | 98.28% | DL |
| 12 | eyelid melanoma | 98.27% | DL |
| 13 | scrotum melanoma | 98.25% | DL |
| 14 | choroideremia | 98.18% | DL |
| 15 | choroidal dystrophy, central areolar | 97.36% | DL |
| 16 | intestinal obstruction in the newborn due to guanylate cyclase 2C deficiency | 97.09% | DL |
| 17 | Richter syndrome | 90.76% | DL |
| 18 | metastatic neoplasm | 90.26% | DL |
| 19 | malignant spiradenoma | 90.22% | DL |
| 20 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 88.16% | DL |

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
