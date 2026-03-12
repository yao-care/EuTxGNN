---
layout: default
title: Elbasvir
description: "elbasvir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 198
evidence_level: L5
indication_count: 50
---

# Elbasvir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Elbasvir |
| DrugBank ID | [DB11574](https://go.drugbank.com/drugs/DB11574) |
| Brand Names (EU) | Elbasvir |
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
| 2 | hepatitis C virus infection | 99.80% | DL |
| 3 | hepatitis B virus infection | 99.71% | DL |
| 4 | hepatitis E virus infection | 99.66% | DL |
| 5 | hepatitis A virus infection | 99.65% | DL |
| 6 | hepatitis, viral, animal | 99.65% | DL |
| 7 | Omsk hemorrhagic fever | 99.64% | DL |
| 8 | Kyasanur forest disease | 99.63% | DL |
| 9 | HIV infectious disease | 99.61% | DL |
| 10 | feline acquired immunodeficiency syndrome | 99.46% | DL |
| 11 | simian immunodeficiency virus infection | 99.46% | DL |
| 12 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.32% | DL |
| 13 | fibroma of prostate | 98.24% | DL |
| 14 | benign reproductive system neoplasm | 98.12% | DL |
| 15 | Brenner tumor | 98.12% | DL |
| 16 | benign prostate phyllodes tumor | 98.06% | DL |
| 17 | male reproductive organ cancer | 97.77% | DL |
| 18 | chronic hepatitis B virus infection | 97.71% | DL |
| 19 | prostate leiomyoma | 97.43% | DL |
| 20 | obsolete familial combined hyperlipidemia | 97.37% | DL |

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
