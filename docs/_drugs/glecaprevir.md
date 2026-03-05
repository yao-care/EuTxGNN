---
layout: default
title: Glecaprevir
description: "glecaprevir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 269
evidence_level: L5
indication_count: 50
---

# Glecaprevir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Glecaprevir |
| DrugBank ID | [DB13879](https://go.drugbank.com/drugs/DB13879) |
| Brand Names (EU) | Glecaprevir |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Maviret is indicated for the treatment of chronic hepatitis C virus (HCV) infection in adults and children aged 3 years and older. Maviret coated granules is indicated for the treatment of chronic hepatitis C virus (HCV) infection in children 3 years and older.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | chronic hepatitis C virus infection | 99.97% | DL |
| 2 | hepatitis C virus infection | 99.89% | DL |
| 3 | HIV infectious disease | 99.87% | DL |
| 4 | hepatitis B virus infection | 99.87% | DL |
| 5 | simian immunodeficiency virus infection | 99.81% | DL |
| 6 | feline acquired immunodeficiency syndrome | 99.81% | DL |
| 7 | hepatitis E virus infection | 99.80% | DL |
| 8 | hepatitis, viral, animal | 99.80% | DL |
| 9 | hepatitis A virus infection | 99.80% | DL |
| 10 | Omsk hemorrhagic fever | 99.79% | DL |
| 11 | Kyasanur forest disease | 99.79% | DL |
| 12 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.77% | DL |
| 13 | chronic hepatitis B virus infection | 99.26% | DL |
| 14 | obsolete familial combined hyperlipidemia | 99.06% | DL |
| 15 | fibroma of prostate | 96.98% | DL |
| 16 | benign reproductive system neoplasm | 96.79% | DL |
| 17 | Brenner tumor | 96.75% | DL |
| 18 | benign prostate phyllodes tumor | 96.62% | DL |
| 19 | male reproductive organ cancer | 96.19% | DL |
| 20 | prostate leiomyoma | 95.59% | DL |

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
