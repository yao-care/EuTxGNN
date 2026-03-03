---
layout: default
title: Pitolisant
description: "Pitolisant drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 461
evidence_level: L5
indication_count: 50
---

# Pitolisant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pitolisant |
| DrugBank ID | [DB11642](https://go.drugbank.com/drugs/DB11642) |
| Brand Names (EU) | Wakix |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Wakix is indicated in adults, adolescents and children from the age of 6 years for the treatment of narcolepsy with or without cataplexy (see also section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | insomnia (disease) | 99.71% | DL |
| 2 | attention deficit-hyperactivity disorder | 99.36% | DL |
| 3 | faciodigitogenital syndrome | 99.29% | DL |
| 4 | X-linked adrenoleukodystrophy | 99.03% | DL |
| 5 | disorder of peroxisomal alpha-, beta- and omega-oxidation | 98.87% | DL |
| 6 | ACBD5 deficiency | 98.65% | DL |
| 7 | Creutzfeldt-Jakob disease | 98.55% | DL |
| 8 | narcolepsy-cataplexy syndrome | 98.49% | DL |
| 9 | narcolepsy | 98.42% | DL |
| 10 | narcolepsy, susceptibility to | 98.21% | DL |
| 11 | megaconial type congenital muscular dystrophy | 97.64% | DL |
| 12 | hypersomnia (disease) | 96.98% | DL |
| 13 | Balo concentric sclerosis | 96.90% | DL |
| 14 | circadian rhythm sleep disorder | 96.73% | DL |
| 15 | chondromyxoid fibroma | 96.61% | DL |
| 16 | narcolepsy without cataplexy | 94.96% | DL |
| 17 | variably protease-sensitive prionopathy | 94.78% | DL |
| 18 | central nervous system disease | 94.77% | DL |
| 19 | attention deficit hyperactivity disorder, inattentive type | 94.48% | DL |
| 20 | Wernicke-Korsakoff syndrome | 93.65% | DL |

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
