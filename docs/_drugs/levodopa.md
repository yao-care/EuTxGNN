---
layout: default
title: Levodopa
description: "Levodopa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 341
evidence_level: L5
indication_count: 50
---

# Levodopa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Levodopa |
| DrugBank ID | [DB01235](https://go.drugbank.com/drugs/DB01235) |
| Brand Names (EU) | Inbrija |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.66% |

---

## Approved Indication (EMA)

Stalevo is indicated for the treatment of adult patients with Parkinson's disease and end-of-dose motor fluctuations not stabilised on levodopa / dopa-decarboxylase (DDC)-inhibitor treatment.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | juvenile onset Parkinson disease 19A | 99.66% | DL |
| 2 | hereditary late onset Parkinson disease | 99.55% | DL |
| 3 | atypical juvenile parkinsonism | 99.20% | DL |
| 4 | X-linked parkinsonism-spasticity syndrome | 99.17% | DL |
| 5 | Rasmussen subacute encephalitis | 99.06% | DL |
| 6 | PLA2G6-associated neurodegeneration | 98.75% | DL |
| 7 | myelitis | 98.47% | DL |
| 8 | hemiparkinsonism-hemiatrophy syndrome | 98.28% | DL |
| 9 | transaldolase deficiency | 98.20% | DL |
| 10 | Parkinson disease | 98.13% | DL |
| 11 | parkinsonian-pyramidal syndrome | 98.13% | DL |
| 12 | paralysis agitans, juvenile, of Hunt | 98.03% | DL |
| 13 | fructose-1,6-bisphosphatase deficiency | 97.81% | DL |
| 14 | progressive supranuclear palsy-corticobasal syndrome | 97.58% | DL |
| 15 | Lewy body dementia | 97.25% | DL |
| 16 | early-onset parkinsonism-intellectual disability syndrome | 97.11% | DL |
| 17 | multiple system atrophy, parkinsonian type | 97.02% | DL |
| 18 | postencephalitic Parkinson disease | 96.56% | DL |
| 19 | X-linked intellectual disability-ataxia-apraxia syndrome | 96.46% | DL |
| 20 | lethal infantile mitochondrial myopathy | 96.27% | DL |

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
