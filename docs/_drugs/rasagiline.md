---
layout: default
title: Rasagiline
description: "Rasagiline drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 480
evidence_level: L5
indication_count: 50
---

# Rasagiline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Rasagiline |
| DrugBank ID | [DB01367](https://go.drugbank.com/drugs/DB01367) |
| Brand Names (EU) | Azilect |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.90% |

---

## Approved Indication (EMA)

Azilect is indicated for the treatment of idiopathic Parkinson's disease (PD) as monotherapy (without levodopa) or as adjunct therapy (with levodopa) in patients with end-of-dose fluctuations.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hereditary late onset Parkinson disease | 99.90% | DL |
| 2 | juvenile onset Parkinson disease 19A | 99.89% | DL |
| 3 | X-linked parkinsonism-spasticity syndrome | 99.74% | DL |
| 4 | atypical juvenile parkinsonism | 99.72% | DL |
| 5 | PLA2G6-associated neurodegeneration | 99.71% | DL |
| 6 | Rasmussen subacute encephalitis | 99.56% | DL |
| 7 | Parkinson disease | 99.40% | DL |
| 8 | parkinsonian-pyramidal syndrome | 99.34% | DL |
| 9 | myelitis | 99.32% | DL |
| 10 | paralysis agitans, juvenile, of Hunt | 99.25% | DL |
| 11 | transaldolase deficiency | 99.19% | DL |
| 12 | hemiparkinsonism-hemiatrophy syndrome | 99.15% | DL |
| 13 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.01% | DL |
| 14 | congenital disorder of glycosylation with defective fucosylation | 98.84% | DL |
| 15 | Lewy body dementia | 98.83% | DL |
| 16 | fructose-1,6-bisphosphatase deficiency | 98.82% | DL |
| 17 | retinal dystrophy with or without extraocular anomalies | 98.81% | DL |
| 18 | early-onset parkinsonism-intellectual disability syndrome | 98.79% | DL |
| 19 | lethal infantile mitochondrial myopathy | 98.71% | DL |
| 20 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 98.69% | DL |

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
