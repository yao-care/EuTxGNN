---
layout: default
title: Vigabatrin
description: "Vigabatrin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 632
evidence_level: L5
indication_count: 50
---

# Vigabatrin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vigabatrin |
| DrugBank ID | [DB01080](https://go.drugbank.com/drugs/DB01080) |
| Brand Names (EU) | Kigabeq |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.09% |

---

## Approved Indication (EMA)

Kigabeq is indicated in infants and children from 1 month to less than 7 years of age for:  Treatment in monotherapy of infantile spasms (West's syndrome). Treatment in combination with other antiepileptic medicinal products for patients with resistant partial epilepsy (focal onset seizures) with or without secondary generalisation, that is where all other appropriate medicinal product combinations have proved inadequate or have not been tolerated.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | West syndrome | 99.09% | DL |
| 2 | intellectual disability, X-linked, with or without seizures, arx-related | 98.66% | DL |
| 3 | episodic kinesigenic dyskinesia | 97.26% | DL |
| 4 | developmental and epileptic encephalopathy | 97.18% | DL |
| 5 | 1q44 microdeletion syndrome | 96.71% | DL |
| 6 | PURA-related severe neonatal hypotonia-seizures-encephalopathy syndrome due to a point mutation | 96.56% | DL |
| 7 | DK1-CDG | 96.47% | DL |
| 8 | microtriplication 11q24.1 | 96.31% | DL |
| 9 | CCDC115-CDG | 96.27% | DL |
| 10 | neonatal period electroclinical syndrome | 96.25% | DL |
| 11 | genetic lethal multiple congenital anomalies/dysmorphic syndrome | 96.22% | DL |
| 12 | COG2-CDG | 96.20% | DL |
| 13 | colobomatous microphthalmia - obesity - hypogenitalism - intellectual disability syndrome | 96.09% | DL |
| 14 | X-linked dominant intellectual disability-epilepsy syndrome | 96.02% | DL |
| 15 | male hypergonadotropic hypogonadism-intellectual disability-skeletal anomalies syndrome | 96.01% | DL |
| 16 | Jawad syndrome | 96.00% | DL |
| 17 | muscular hypertrophy-hepatomegaly-polyhydramnios syndrome | 95.99% | DL |
| 18 | infancy electroclinical syndrome | 95.98% | DL |
| 19 | neonatal epileptic encephalopathy | 95.91% | DL |
| 20 | craniofaciofrontodigital syndrome | 95.91% | DL |

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
