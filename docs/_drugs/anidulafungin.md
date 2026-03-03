---
layout: default
title: Anidulafungin
description: "Anidulafungin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 41
evidence_level: L5
indication_count: 51
---

# Anidulafungin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Anidulafungin |
| DrugBank ID | [DB00362](https://go.drugbank.com/drugs/DB00362) |
| Brand Names (EU) | Ecalta |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.85% |

---

## Approved Indication (EMA)

Treatment of invasive candidiasis in adults and paediatric patients aged 1 month to &lt; 18 years.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | impetigo | 98.85% | DL |
| 2 | malignant pleural mesothelioma | 98.75% | DL |
| 3 | staphylococcal scalded skin syndrome | 98.73% | DL |
| 4 | pleural empyema (disease) | 98.52% | DL |
| 5 | malignant visceral pleura tumor | 98.45% | DL |
| 6 | bullous impetigo | 98.40% | DL |
| 7 | malignant epithelioid mesothelioma | 98.37% | DL |
| 8 | sarcomatoid mesothelioma | 98.26% | DL |
| 9 | hordeolum | 98.23% | DL |
| 10 | Clostridium infectious disease | 98.22% | DL |
| 11 | pleural neoplasm | 98.08% | DL |
| 12 | inhalational botulism | 97.65% | DL |
| 13 | toxin-mediated infectious botulism | 97.64% | DL |
| 14 | cysticercosis | 97.34% | DL |
| 15 | staphylococcal pneumonia | 97.02% | DL |
| 16 | coenurosis | 96.89% | DL |
| 17 | lymph node palisaded myofibroblastoma | 96.86% | DL |
| 18 | abdominal cystic lymphangioma | 96.86% | DL |
| 19 | celiac trunk compression syndrome | 96.86% | DL |
| 20 | abdominal ectopic pregnancy | 96.86% | DL |

*Showing top 20 of 51 predictions.*

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
