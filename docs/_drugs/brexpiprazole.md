---
layout: default
title: Brexpiprazole
description: "Brexpiprazole drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 91
evidence_level: L5
indication_count: 50
---

# Brexpiprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Brexpiprazole |
| DrugBank ID | [DB09128](https://go.drugbank.com/drugs/DB09128) |
| Brand Names (EU) | Rxulti |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.87% |

---

## Approved Indication (EMA)

Rxulti is indicated for the treatment of schizophrenia in adult and adolescents aged 13 years and older.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | anxiety disorder | 98.87% | DL |
| 2 | dysthymic disorder | 98.53% | DL |
| 3 | benign paroxysmal torticollis of infancy | 98.30% | DL |
| 4 | agoraphobia | 98.23% | DL |
| 5 | neurotic disorder | 97.73% | DL |
| 6 | neurotic depression | 97.11% | DL |
| 7 | melancholia | 97.07% | DL |
| 8 | endogenous depression | 96.14% | DL |
| 9 | Keppen-Lubinsky syndrome | 96.05% | DL |
| 10 | schizophrenia | 96.03% | DL |
| 11 | Ohdo syndrome and variants | 94.97% | DL |
| 12 | retinal dystrophy with or without extraocular anomalies | 94.75% | DL |
| 13 | congenital isolated adrenocorticotropic hormone deficiency (disease) | 94.50% | DL |
| 14 | vitamin B12-responsive methylmalonic acidemia | 94.30% | DL |
| 15 | autosomal dominant slowed nerve conduction velocity | 94.01% | DL |
| 16 | major depressive disorder | 94.00% | DL |
| 17 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 93.95% | DL |
| 18 | hydranencephaly (disease) | 93.62% | DL |
| 19 | syndromic myopia | 93.58% | DL |
| 20 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 93.49% | DL |

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
