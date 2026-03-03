---
layout: default
title: Sodium Oxybate
description: "Sodium Oxybate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 535
evidence_level: L5
indication_count: 50
---

# Sodium Oxybate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sodium Oxybate |
| DrugBank ID | [DB09072](https://go.drugbank.com/drugs/DB09072) |
| Brand Names (EU) | Xyrem |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Treatment of narcolepsy with cataplexy in adult patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | insomnia (disease) | 100.00% | DL |
| 2 | obsolete neurogenic bladder (disease) | 99.83% | DL |
| 3 | sleep disorder, initiating and maintaining sleep | 99.78% | DL |
| 4 | cauda equina syndrome | 99.60% | DL |
| 5 | Wernicke-Korsakoff syndrome | 99.36% | DL |
| 6 | restless legs syndrome | 99.26% | DL |
| 7 | attention deficit-hyperactivity disorder | 98.74% | DL |
| 8 | acute encephalopathy with biphasic seizures and late reduced diffusion | 98.70% | DL |
| 9 | faciodigitogenital syndrome | 98.63% | DL |
| 10 | Balo concentric sclerosis | 98.55% | DL |
| 11 | attention deficit hyperactivity disorder, inattentive type | 98.53% | DL |
| 12 | narcolepsy without cataplexy | 98.30% | DL |
| 13 | Creutzfeldt-Jakob disease | 98.23% | DL |
| 14 | specific developmental disorder | 97.98% | DL |
| 15 | narcolepsy-cataplexy syndrome | 97.84% | DL |
| 16 | chondromyxoid fibroma | 97.71% | DL |
| 17 | narcolepsy | 97.32% | DL |
| 18 | central nervous system disease | 96.63% | DL |
| 19 | X-linked adrenoleukodystrophy | 96.61% | DL |
| 20 | alcohol withdrawal | 96.52% | DL |

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
