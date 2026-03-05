---
layout: default
title: Grazoprevir
description: "grazoprevir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 277
evidence_level: L5
indication_count: 50
---

# Grazoprevir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Grazoprevir |
| DrugBank ID | [DB11575](https://go.drugbank.com/drugs/DB11575) |
| Brand Names (EU) | Grazoprevir |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

ZEPATIER is indicated for the treatment of chronic hepatitis C (CHC) in adult and paediatric patients 12 years of age and older who weigh at least 30 kg (see sections 4.2, 4.4 and 5.1). For hepatitis C virus (HCV) genotype-specific activity see sections 4.4 and 5.1.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | chronic hepatitis C virus infection | 99.94% | DL |
| 2 | hepatitis C virus infection | 99.79% | DL |
| 3 | HIV infectious disease | 99.73% | DL |
| 4 | hepatitis B virus infection | 99.73% | DL |
| 5 | hepatitis E virus infection | 99.64% | DL |
| 6 | hepatitis A virus infection | 99.63% | DL |
| 7 | hepatitis, viral, animal | 99.63% | DL |
| 8 | Omsk hemorrhagic fever | 99.62% | DL |
| 9 | Kyasanur forest disease | 99.61% | DL |
| 10 | simian immunodeficiency virus infection | 99.61% | DL |
| 11 | feline acquired immunodeficiency syndrome | 99.61% | DL |
| 12 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.51% | DL |
| 13 | chronic hepatitis B virus infection | 98.17% | DL |
| 14 | obsolete familial combined hyperlipidemia | 97.12% | DL |
| 15 | fibroma of prostate | 96.06% | DL |
| 16 | benign reproductive system neoplasm | 95.84% | DL |
| 17 | Brenner tumor | 95.79% | DL |
| 18 | benign prostate phyllodes tumor | 95.70% | DL |
| 19 | male reproductive organ cancer | 95.03% | DL |
| 20 | prostate leiomyoma | 94.29% | DL |

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
