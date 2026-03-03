---
layout: default
title: Pretomanid
description: "Pretomanid drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 471
evidence_level: L5
indication_count: 50
---

# Pretomanid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pretomanid |
| DrugBank ID | [DB05154](https://go.drugbank.com/drugs/DB05154) |
| Brand Names (EU) | Dovprela (previously Pretomanid FGK) |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.69% |

---

## Approved Indication (EMA)

Dovprela is indicated in combination with bedaquiline and linezolid, in adults, for the treatment of pulmonary extensively drug resistant (XDR), or treatment-intolerant or nonresponsive multidrug-resistant (MDR) tuberculosis (TB). Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | candidiasis | 99.69% | DL |
| 2 | leprosy | 99.27% | DL |
| 3 | coronary artery disease | 99.25% | DL |
| 4 | myocardial ischemia | 99.17% | DL |
| 5 | anomalous left coronary artery from the pulmonary artery | 99.08% | DL |
| 6 | HIV infectious disease | 98.85% | DL |
| 7 | oral candidiasis | 98.72% | DL |
| 8 | Bacteroidaceae infectious disease | 98.67% | DL |
| 9 | thrombocytopenia | 98.65% | DL |
| 10 | fascioliasis | 98.63% | DL |
| 11 | acne (disease) | 98.63% | DL |
| 12 | feline acquired immunodeficiency syndrome | 98.49% | DL |
| 13 | simian immunodeficiency virus infection | 98.49% | DL |
| 14 | marcothrombocytopenia with mitral valve insufficiency | 98.48% | DL |
| 15 | hereditary thrombocytopenia with normal platelets | 98.48% | DL |
| 16 | opisthorchiasis | 98.42% | DL |
| 17 | anaerobic bacteria infectious disease | 98.40% | DL |
| 18 | multiple endocrine neoplasia | 98.39% | DL |
| 19 | transient neonatal thrombocytopenia | 98.38% | DL |
| 20 | breast fibrocystic disease | 98.38% | DL |

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
