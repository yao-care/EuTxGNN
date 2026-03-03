---
layout: default
title: Esketamine Hydrochloride
description: "Esketamine Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 225
evidence_level: L5
indication_count: 50
---

# Esketamine Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Esketamine Hydrochloride |
| DrugBank ID | [DB11823](https://go.drugbank.com/drugs/DB11823) |
| Brand Names (EU) | Spravato |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.75% |

---

## Approved Indication (EMA)

Spravato, in combination with a SSRI or SNRI, is indicated for adults with treatment-resistant Major Depressive Disorder, who have not responded to at least two different treatments with antidepressants in the current moderate to severe depressive episode.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dysthymic disorder | 99.75% | DL |
| 2 | anxiety disorder | 99.68% | DL |
| 3 | agoraphobia | 99.57% | DL |
| 4 | benign paroxysmal torticollis of infancy | 99.49% | DL |
| 5 | neurotic disorder | 98.85% | DL |
| 6 | neurotic depression | 97.83% | DL |
| 7 | melancholia | 97.74% | DL |
| 8 | vitamin B12-responsive methylmalonic acidemia | 97.32% | DL |
| 9 | obsessive-compulsive disorder | 97.31% | DL |
| 10 | Keppen-Lubinsky syndrome | 97.25% | DL |
| 11 | insomnia (disease) | 96.39% | DL |
| 12 | congenital isolated adrenocorticotropic hormone deficiency (disease) | 96.04% | DL |
| 13 | autosomal dominant slowed nerve conduction velocity | 95.54% | DL |
| 14 | schizoid personality disorder | 95.38% | DL |
| 15 | histrionic personality disorder (disease) | 95.38% | DL |
| 16 | schizotypal personality disorder | 95.38% | DL |
| 17 | paranoid personality disorder | 95.38% | DL |
| 18 | Ohdo syndrome and variants | 94.76% | DL |
| 19 | blepharophimosis - intellectual disability syndrome, Ohdo type | 93.47% | DL |
| 20 | narcissistic personality disorder | 91.36% | DL |

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
