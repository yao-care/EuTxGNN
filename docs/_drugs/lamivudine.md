---
layout: default
title: Lamivudine
description: "lamivudine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 326
evidence_level: L5
indication_count: 50
---

# Lamivudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lamivudine |
| DrugBank ID | [DB00709](https://go.drugbank.com/drugs/DB00709) |
| Brand Names (EU) | Epivir |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Combivir is indicated in antiretroviral combination therapy for the treatment of Human Immunodeficiency Virus (HIV) infection.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.96% | DL |
| 2 | feline acquired immunodeficiency syndrome | 99.93% | DL |
| 3 | simian immunodeficiency virus infection | 99.93% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.93% | DL |
| 5 | obsolete familial combined hyperlipidemia | 99.63% | DL |
| 6 | chronic hepatitis C virus infection | 99.11% | DL |
| 7 | hepatitis B virus infection | 97.84% | DL |
| 8 | chronic hepatitis B virus infection | 97.08% | DL |
| 9 | hepatitis C virus infection | 96.96% | DL |
| 10 | hepatoportal sclerosis | 96.33% | DL |
| 11 | idiopathic copper-associated cirrhosis | 96.33% | DL |
| 12 | early-onset familial noncirrhotic portal hypertension | 96.33% | DL |
| 13 | hepatopulmonary syndrome | 96.33% | DL |
| 14 | primitive portal vein thrombosis | 96.33% | DL |
| 15 | hepatitis E virus infection | 95.86% | DL |
| 16 | AIDS | 95.78% | DL |
| 17 | hepatitis, viral, animal | 95.76% | DL |
| 18 | hepatitis A virus infection | 95.72% | DL |
| 19 | Omsk hemorrhagic fever | 95.67% | DL |
| 20 | Kyasanur forest disease | 95.47% | DL |

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
