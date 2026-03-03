---
layout: default
title: Sofosbuvir
description: "Sofosbuvir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 537
evidence_level: L5
indication_count: 50
---

# Sofosbuvir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sofosbuvir |
| DrugBank ID | [DB08934](https://go.drugbank.com/drugs/DB08934) |
| Brand Names (EU) | Sovaldi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.95% |

---

## Approved Indication (EMA)

Epclusa is indicated for the treatment of chronic hepatitis C virus (HCV) infection in patients 3 years of age and older (see sections 4.2, 4.4 and 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | chronic hepatitis C virus infection | 99.95% | DL |
| 2 | hepatitis B virus infection | 99.77% | DL |
| 3 | hepatitis C virus infection | 99.70% | DL |
| 4 | hepatitis E virus infection | 99.49% | DL |
| 5 | hepatitis, viral, animal | 99.48% | DL |
| 6 | hepatitis A virus infection | 99.48% | DL |
| 7 | Omsk hemorrhagic fever | 99.47% | DL |
| 8 | chronic hepatitis B virus infection | 99.46% | DL |
| 9 | Kyasanur forest disease | 99.45% | DL |
| 10 | HIV infectious disease | 99.23% | DL |
| 11 | simian immunodeficiency virus infection | 98.91% | DL |
| 12 | feline acquired immunodeficiency syndrome | 98.91% | DL |
| 13 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 98.74% | DL |
| 14 | primitive portal vein thrombosis | 98.14% | DL |
| 15 | early-onset familial noncirrhotic portal hypertension | 98.14% | DL |
| 16 | hepatoportal sclerosis | 98.14% | DL |
| 17 | hepatopulmonary syndrome | 98.14% | DL |
| 18 | idiopathic copper-associated cirrhosis | 98.14% | DL |
| 19 | hepatic porphyria | 97.60% | DL |
| 20 | obsolete familial combined hyperlipidemia | 97.59% | DL |

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
