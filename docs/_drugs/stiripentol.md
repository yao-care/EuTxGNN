---
layout: default
title: Stiripentol
description: "Stiripentol drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 544
evidence_level: L5
indication_count: 52
---

# Stiripentol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Stiripentol |
| DrugBank ID | [DB09118](https://go.drugbank.com/drugs/DB09118) |
| Brand Names (EU) | Diacomit |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 98.76% |

---

## Approved Indication (EMA)

Diacomit is indicated for use in conjunction with clobazam and valproate as adjunctive therapy of refractory generalized tonic-clonic seizures in patients with severe myoclonic epilepsy in infancy (SMEI, Dravet's syndrome) whose seizures are not adequately controlled with clobazam and valproate.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | restless legs syndrome | 98.76% | DL |
| 2 | trigeminal nerve neoplasm | 97.15% | DL |
| 3 | West syndrome | 94.97% | DL |
| 4 | developmental and epileptic encephalopathy | 94.55% | DL |
| 5 | 1q44 microdeletion syndrome | 94.31% | DL |
| 6 | episodic kinesigenic dyskinesia | 94.17% | DL |
| 7 | acute encephalopathy with biphasic seizures and late reduced diffusion | 94.14% | DL |
| 8 | PURA-related severe neonatal hypotonia-seizures-encephalopathy syndrome due to a point mutation | 94.03% | DL |
| 9 | neonatal period electroclinical syndrome | 93.82% | DL |
| 10 | Wernicke-Korsakoff syndrome | 93.80% | DL |
| 11 | myoclonic epilepsy, Hartung type | 93.70% | DL |
| 12 | X-linked dominant intellectual disability-epilepsy syndrome | 93.56% | DL |
| 13 | insomnia (disease) | 93.45% | DL |
| 14 | DK1-CDG | 93.33% | DL |
| 15 | genetic lethal multiple congenital anomalies/dysmorphic syndrome | 93.30% | DL |
| 16 | infancy electroclinical syndrome | 93.30% | DL |
| 17 | microtriplication 11q24.1 | 93.09% | DL |
| 18 | sleep disorder, initiating and maintaining sleep | 93.02% | DL |
| 19 | guanidinoacetate methyltransferase deficiency | 92.91% | DL |
| 20 | CCDC115-CDG | 92.79% | DL |

*Showing top 20 of 52 predictions.*

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
