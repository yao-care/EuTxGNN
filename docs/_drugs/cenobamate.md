---
layout: default
title: Cenobamate
description: "Cenobamate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 126
evidence_level: L5
indication_count: 50
---

# Cenobamate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cenobamate |
| DrugBank ID | [DB06119](https://go.drugbank.com/drugs/DB06119) |
| Brand Names (EU) | Ontozry |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.33% |

---

## Approved Indication (EMA)

Adjunctive treatment of focal-onset seizures with or without secondary generalisation in adult patients with epilepsy who have not been adequately controlled despite a history of treatment with at least 2 anti-epileptic medicinal products.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | partial epilepsy | 98.33% | DL |
| 2 | guanidinoacetate methyltransferase deficiency | 97.83% | DL |
| 3 | status epilepticus | 97.48% | DL |
| 4 | visual epilepsy | 97.13% | DL |
| 5 | beta-ketothiolase deficiency | 97.06% | DL |
| 6 | Rett syndrome, congenital variant | 96.12% | DL |
| 7 | 14q12 microdeletion syndrome | 96.04% | DL |
| 8 | startle epilepsy | 95.90% | DL |
| 9 | eating seizures | 95.90% | DL |
| 10 | thinking seizures | 95.90% | DL |
| 11 | orgasm-induced seizures | 95.90% | DL |
| 12 | micturation-induced seizures | 95.90% | DL |
| 13 | audiogenic seizures | 95.90% | DL |
| 14 | adolescent/adult onset autosomal dominant epilepsy with auditory features | 95.64% | DL |
| 15 | reading seizures | 94.93% | DL |
| 16 | epilepsy with generalized tonic-clonic seizures | 94.20% | DL |
| 17 | partial motor epilepsy | 93.42% | DL |
| 18 | trigeminal nerve neoplasm | 91.18% | DL |
| 19 | epilepsy | 90.65% | DL |
| 20 | restless legs syndrome | 87.22% | DL |

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
