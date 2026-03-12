---
layout: default
title: Botulinum Toxin Type A
description: "Botulinum Toxin Type A drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 89
evidence_level: L5
indication_count: 50
---

# Botulinum Toxin Type A
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Botulinum Toxin Type A |
| DrugBank ID | [DB00083](https://go.drugbank.com/drugs/DB00083) |
| Brand Names (EU) | Nuceiva |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 89.37% |

---

## Approved Indication (EMA)

Temporary improvement in the appearance of moderate to severe vertical lines between the eyebrows seen at maximum frown (glabellar lines), when the severity of the above facial lines has an important psychological impact in adults below 65 years of age.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary hereditary glaucoma | 89.37% | DL |
| 2 | parkinsonian disorder | 88.84% | DL |
| 3 | open-angle glaucoma | 88.76% | DL |
| 4 | insomnia (disease) | 87.47% | DL |
| 5 | glaucoma 1, open angle | 79.00% | DL |
| 6 | restless legs syndrome | 77.87% | DL |
| 7 | Parkinson disease | 77.69% | DL |
| 8 | paralysis agitans, juvenile, of Hunt | 77.32% | DL |
| 9 | bronchitis | 75.82% | DL |
| 10 | autosomal recessive Parkinson disease | 73.28% | DL |
| 11 | lethal infantile mitochondrial myopathy | 73.13% | DL |
| 12 | enterocolitis (disease) | 73.00% | DL |
| 13 | glaucoma | 72.80% | DL |
| 14 | irritable bowel syndrome | 72.66% | DL |
| 15 | open angle glaucoma | 71.96% | DL |
| 16 | progressive supranuclear palsy-corticobasal syndrome | 71.48% | DL |
| 17 | anxiety | 70.26% | DL |
| 18 | headache disorder | 70.23% | DL |
| 19 | sleep disorder, initiating and maintaining sleep | 69.19% | DL |
| 20 | trigeminal autonomic cephalalgia | 69.14% | DL |

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
