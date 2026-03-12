---
layout: default
title: Deutetrabenazine
description: "Deutetrabenazine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 169
evidence_level: L5
indication_count: 50
---

# Deutetrabenazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Deutetrabenazine |
| DrugBank ID | [DB12161](https://go.drugbank.com/drugs/DB12161) |
| Brand Names (EU) | Austedo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.73% |

---

## Approved Indication (EMA)

Treatment of moderate to severe tardive dyskinesia in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | psychogenic movement disorders | 98.73% | DL |
| 2 | tremor-nystagmus-duodenal ulcer syndrome | 98.70% | DL |
| 3 | primary orthostatic tremor | 98.68% | DL |
| 4 | benign paroxysmal tonic upgaze of childhood with ataxia | 98.59% | DL |
| 5 | chronic tic disorder | 98.31% | DL |
| 6 | extrapyramidal and movement disease | 98.26% | DL |
| 7 | benign shuddering attacks | 98.26% | DL |
| 8 | polycystic kidney disease 3 with or without polycystic liver disease | 97.88% | DL |
| 9 | acute intermittent porphyria | 97.73% | DL |
| 10 | Hirschsprung disease | 97.60% | DL |
| 11 | lingual-facial-buccal dyskinesia | 97.41% | DL |
| 12 | renal-hepatic-pancreatic dysplasia | 97.25% | DL |
| 13 | miscellaneous movement disorder due to neurodegenerative disease | 97.16% | DL |
| 14 | karyomegalic interstitial nephritis | 96.96% | DL |
| 15 | Joubert syndrome with renal defect | 96.79% | DL |
| 16 | thoracic malformation | 96.59% | DL |
| 17 | adult familial nephronophthisis-spastic quadriparesia syndrome | 96.45% | DL |
| 18 | Huntington disease-like syndrome due to C9ORF72 expansions | 95.56% | DL |
| 19 | juvenile Huntington disease | 95.02% | DL |
| 20 | glutaric acidemia type 3 | 94.55% | DL |

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
