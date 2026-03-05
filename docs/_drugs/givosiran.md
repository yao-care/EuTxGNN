---
layout: default
title: Givosiran
description: "givosiran drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 267
evidence_level: L5
indication_count: 50
---

# Givosiran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Givosiran |
| DrugBank ID | [DB15066](https://go.drugbank.com/drugs/DB15066) |
| Brand Names (EU) | Givlaari |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Treatment of acute hepatic porphyria (AHP) in adults and adolescents aged 12 years and older.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hepatic porphyria | 100.00% | DL |
| 2 | hepatopulmonary syndrome | 100.00% | DL |
| 3 | hepatoportal sclerosis | 100.00% | DL |
| 4 | idiopathic copper-associated cirrhosis | 100.00% | DL |
| 5 | early-onset familial noncirrhotic portal hypertension | 100.00% | DL |
| 6 | primitive portal vein thrombosis | 100.00% | DL |
| 7 | chronic hepatitis C virus infection | 99.97% | DL |
| 8 | glycogen storage disease due to hepatic glycogen synthase deficiency | 99.96% | DL |
| 9 | chronic hepatitis B virus infection | 99.94% | DL |
| 10 | porphyria due to ALA dehydratase deficiency | 99.91% | DL |
| 11 | disorder of phenylalanine metabolism | 99.90% | DL |
| 12 | hepatitis B virus infection | 99.89% | DL |
| 13 | disorder of tyrosine metabolism | 99.88% | DL |
| 14 | tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria | 99.88% | DL |
| 15 | nodular regenerative hyperplasia of the liver | 99.88% | DL |
| 16 | teratogenic Pierre Robin syndrome | 99.86% | DL |
| 17 | acute intermittent porphyria | 99.72% | DL |
| 18 | hepatitis C virus infection | 99.64% | DL |
| 19 | porphyria | 99.59% | DL |
| 20 | tetrahydrobiopterin metabolic process disease | 99.54% | DL |

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
