---
layout: default
title: Migalastat Hydrochloride
description: "Migalastat Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 383
evidence_level: L5
indication_count: 50
---

# Migalastat Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Migalastat Hydrochloride |
| DrugBank ID | [DB05018](https://go.drugbank.com/drugs/DB05018) |
| Brand Names (EU) | Galafold |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.85% |

---

## Approved Indication (EMA)

Galafold is indicated for long-term treatment of adults and adolescents aged 16 years and older with a confirmed diagnosis of Fabry disease (?-galactosidase A deficiency) and who have an amenable mutation.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hepatoportal sclerosis | 98.85% | DL |
| 2 | hepatopulmonary syndrome | 98.85% | DL |
| 3 | idiopathic copper-associated cirrhosis | 98.85% | DL |
| 4 | early-onset familial noncirrhotic portal hypertension | 98.85% | DL |
| 5 | primitive portal vein thrombosis | 98.85% | DL |
| 6 | hepatic porphyria | 98.44% | DL |
| 7 | mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 95.73% | DL |
| 8 | disorder of tyrosine metabolism | 93.94% | DL |
| 9 | teratogenic Pierre Robin syndrome | 93.57% | DL |
| 10 | nodular regenerative hyperplasia of the liver | 93.03% | DL |
| 11 | tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria | 92.99% | DL |
| 12 | exocrine pancreatic insufficiency | 91.98% | DL |
| 13 | disorder of phenylalanine metabolism | 91.94% | DL |
| 14 | pyelonephritis | 90.85% | DL |
| 15 | glycogen storage disease due to hepatic glycogen synthase deficiency | 89.95% | DL |
| 16 | muscular lipidosis | 88.31% | DL |
| 17 | neutral lipid storage myopathy | 87.75% | DL |
| 18 | lysosomal lipid storage disorder | 86.23% | DL |
| 19 | HHV-6 encephalitis | 84.58% | DL |
| 20 | Hendra virus infection | 84.58% | DL |

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
