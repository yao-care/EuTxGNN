---
layout: default
title: Elvitegravir
description: "elvitegravir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 203
evidence_level: L5
indication_count: 50
---

# Elvitegravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Elvitegravir |
| DrugBank ID | [DB09101](https://go.drugbank.com/drugs/DB09101) |
| Brand Names (EU) | Elvitegravir |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

Treatment of human immunodeficiency virus 1 (HIV 1) infection in adults aged 18 years and over who are antiretroviral treatment-naïve or are infected with HIV 1 without known mutations associated with resistance to any of the three antiretroviral agents in Stribild.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.94% | DL |
| 2 | feline acquired immunodeficiency syndrome | 99.89% | DL |
| 3 | simian immunodeficiency virus infection | 99.89% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.87% | DL |
| 5 | AIDS | 99.55% | DL |
| 6 | congenital human immunodeficiency virus | 98.98% | DL |
| 7 | AIDS related complex | 98.98% | DL |
| 8 | chronic hepatitis C virus infection | 98.73% | DL |
| 9 | hepatitis C virus infection | 96.83% | DL |
| 10 | hepatitis E virus infection | 95.75% | DL |
| 11 | hepatitis A virus infection | 95.63% | DL |
| 12 | Omsk hemorrhagic fever | 95.60% | DL |
| 13 | obsolete familial combined hyperlipidemia | 95.57% | DL |
| 14 | Kyasanur forest disease | 95.49% | DL |
| 15 | hepatitis, viral, animal | 95.46% | DL |
| 16 | hepatitis B virus infection | 95.44% | DL |
| 17 | fibroma of prostate | 94.38% | DL |
| 18 | Brenner tumor | 94.34% | DL |
| 19 | benign reproductive system neoplasm | 94.21% | DL |
| 20 | benign prostate phyllodes tumor | 94.00% | DL |

*Showing top 20 of 50 predictions.*

---


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
