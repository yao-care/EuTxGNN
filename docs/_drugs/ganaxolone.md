---
layout: default
title: Ganaxolone
description: "Ganaxolone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 261
evidence_level: L5
indication_count: 50
---

# Ganaxolone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ganaxolone |
| DrugBank ID | [DB05087](https://go.drugbank.com/drugs/DB05087) |
| Brand Names (EU) | Ztalmy |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 94.85% |

---

## Approved Indication (EMA)

Ztalmy is indicated for the adjunctive treatment of epileptic seizures associated with cyclin-dependent kinase-like 5 (CDKL5) deficiency disorder (CDD) in patients 2 to 17 years of age. Ztalmy may be continued in patients 18 years of age and older.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | alcohol withdrawal delirium | 94.85% | DL |
| 2 | hallucinogen abuse | 93.07% | DL |
| 3 | barbiturate abuse | 93.07% | DL |
| 4 | antidepressant type abuse | 93.07% | DL |
| 5 | phencyclidine abuse | 82.76% | DL |
| 6 | alcohol withdrawal | 81.80% | DL |
| 7 | autism spectrum disorder | 79.30% | DL |
| 8 | gaze palsy, familial horizontal, with progressive scoliosis | 77.04% | DL |
| 9 | asperger syndrome, susceptibility to | 76.13% | DL |
| 10 | autism susceptibility 1 | 75.45% | DL |
| 11 | drug dependence | 74.69% | DL |
| 12 | alcohol-related disorders | 73.30% | DL |
| 13 | amelocerebrohypohidrotic syndrome | 73.06% | DL |
| 14 | Wernicke-Korsakoff syndrome | 72.65% | DL |
| 15 | autism, susceptibility to | 72.05% | DL |
| 16 | intellectual disability | 70.95% | DL |
| 17 | adenosarcoma | 70.71% | DL |
| 18 | uterine ligament adenosarcoma | 70.67% | DL |
| 19 | 16q24.3 microdeletion syndrome | 70.06% | DL |
| 20 | chromosome 15q11.2 deletion syndrome | 69.93% | DL |

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
