---
layout: default
title: Carbidopa
description: "Carbidopa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 115
evidence_level: L5
indication_count: 50
---

# Carbidopa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Carbidopa |
| DrugBank ID | [DB00190](https://go.drugbank.com/drugs/DB00190) |
| Brand Names (EU) | Carbidopa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.27% |

---

## Approved Indication (EMA)

Stalevo is indicated for the treatment of adult patients with Parkinson's disease and end-of-dose motor fluctuations not stabilised on levodopa / dopa-decarboxylase (DDC)-inhibitor treatment.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hereditary late onset Parkinson disease | 99.27% | DL |
| 2 | X-linked parkinsonism-spasticity syndrome | 98.83% | DL |
| 3 | juvenile onset Parkinson disease 19A | 98.51% | DL |
| 4 | Rasmussen subacute encephalitis | 98.43% | DL |
| 5 | PLA2G6-associated neurodegeneration | 97.60% | DL |
| 6 | atypical juvenile parkinsonism | 97.45% | DL |
| 7 | transaldolase deficiency | 97.40% | DL |
| 8 | hemiparkinsonism-hemiatrophy syndrome | 97.40% | DL |
| 9 | myelitis | 97.40% | DL |
| 10 | fructose-1,6-bisphosphatase deficiency | 97.09% | DL |
| 11 | parkinsonian-pyramidal syndrome | 96.01% | DL |
| 12 | Lewy body dementia | 95.99% | DL |
| 13 | paralysis agitans, juvenile, of Hunt | 95.60% | DL |
| 14 | Parkinson disease | 95.56% | DL |
| 15 | progressive supranuclear palsy-corticobasal syndrome | 95.36% | DL |
| 16 | early-onset parkinsonism-intellectual disability syndrome | 95.17% | DL |
| 17 | X-linked intellectual disability-ataxia-apraxia syndrome | 94.87% | DL |
| 18 | X-linked intellectual disability-cerebellar hypoplasia syndrome | 93.72% | DL |
| 19 | multiple system atrophy, parkinsonian type | 93.46% | DL |
| 20 | CLCN4-related X-linked intellectual disability syndrome | 93.18% | DL |

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
