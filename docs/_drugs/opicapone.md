---
layout: default
title: Opicapone
description: "Opicapone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 423
evidence_level: L5
indication_count: 50
---

# Opicapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Opicapone |
| DrugBank ID | [DB11632](https://go.drugbank.com/drugs/DB11632) |
| Brand Names (EU) | Ongentys |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.63% |

---

## Approved Indication (EMA)

Ongentys is indicated as adjunctive therapy to preparations of levodopa/ DOPA decarboxylase inhibitors (DDCI) in adult patients with Parkinson’s disease and end-of-dose motor fluctuations who cannot be stabilised on those combinations.Ongentys is indicated as adjunctive therapy to preparations of levodopa/ DOPA decarboxylase inhibitors (DDCI) in adult patients with Parkinson’s disease and end-of-dose motor fluctuations who cannot be stabilised on those combinations.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | juvenile onset Parkinson disease 19A | 99.63% | DL |
| 2 | hereditary late onset Parkinson disease | 98.90% | DL |
| 3 | Rasmussen subacute encephalitis | 98.64% | DL |
| 4 | atypical juvenile parkinsonism | 98.57% | DL |
| 5 | X-linked parkinsonism-spasticity syndrome | 98.32% | DL |
| 6 | myelitis | 98.15% | DL |
| 7 | PLA2G6-associated neurodegeneration | 97.61% | DL |
| 8 | paralysis agitans, juvenile, of Hunt | 97.30% | DL |
| 9 | Parkinson disease | 96.96% | DL |
| 10 | transaldolase deficiency | 96.01% | DL |
| 11 | hemiparkinsonism-hemiatrophy syndrome | 95.99% | DL |
| 12 | fructose-1,6-bisphosphatase deficiency | 95.73% | DL |
| 13 | Lewy body dementia | 95.69% | DL |
| 14 | lethal infantile mitochondrial myopathy | 95.44% | DL |
| 15 | parkinsonian-pyramidal syndrome | 95.33% | DL |
| 16 | X-linked intellectual disability-ataxia-apraxia syndrome | 94.35% | DL |
| 17 | early-onset parkinsonism-intellectual disability syndrome | 94.21% | DL |
| 18 | X-linked intellectual disability-cerebellar hypoplasia syndrome | 93.27% | DL |
| 19 | CLCN4-related X-linked intellectual disability syndrome | 92.47% | DL |
| 20 | hydrocephaly-cerebellar agenesis syndrome | 91.94% | DL |

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
