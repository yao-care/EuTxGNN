---
layout: default
title: Perampanel
description: "Perampanel drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 454
evidence_level: L5
indication_count: 50
---

# Perampanel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Perampanel |
| DrugBank ID | [DB08883](https://go.drugbank.com/drugs/DB08883) |
| Brand Names (EU) | Fycompa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Fycompa is indicated for the adjunctive treatment of partial-onset seizures with or without secondarily generalised seizures in adult and adolescent patients from 12 years of age with epilepsy. Fycompa is indicated for the adjunctive treatment of primary generalised tonic-clonic seizures in adult and adolescent patients from 12 years of age with idiopathic generalised epilepsy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | visual epilepsy | 99.92% | DL |
| 2 | orgasm-induced seizures | 99.86% | DL |
| 3 | eating seizures | 99.86% | DL |
| 4 | micturation-induced seizures | 99.86% | DL |
| 5 | thinking seizures | 99.86% | DL |
| 6 | startle epilepsy | 99.86% | DL |
| 7 | audiogenic seizures | 99.86% | DL |
| 8 | reading seizures | 99.83% | DL |
| 9 | partial epilepsy | 99.80% | DL |
| 10 | beta-ketothiolase deficiency | 99.79% | DL |
| 11 | status epilepticus | 99.77% | DL |
| 12 | Rett syndrome, congenital variant | 99.73% | DL |
| 13 | 14q12 microdeletion syndrome | 99.73% | DL |
| 14 | guanidinoacetate methyltransferase deficiency | 99.64% | DL |
| 15 | partial motor epilepsy | 99.44% | DL |
| 16 | adolescent/adult onset autosomal dominant epilepsy with auditory features | 99.09% | DL |
| 17 | epilepsy | 99.01% | DL |
| 18 | epilepsy with generalized tonic-clonic seizures | 99.00% | DL |
| 19 | trigeminal nerve neoplasm | 98.69% | DL |
| 20 | trigeminal neuralgia | 97.25% | DL |

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
