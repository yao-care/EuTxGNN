---
layout: default
title: Solriamfetol Hydrochloride
description: "Solriamfetol Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 538
evidence_level: L5
indication_count: 50
---

# Solriamfetol Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Solriamfetol Hydrochloride |
| DrugBank ID | [DB14754](https://go.drugbank.com/drugs/DB14754) |
| Brand Names (EU) | Sunosi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Sunosi is indicated to improve wakefulness and reduce excessive daytime sleepiness in adult patients with narcolepsy (with or without cataplexy). Sunosi is indicated to improve wakefulness and reduce excessive daytime sleepiness (EDS) in adult patients with obstructive sleep apnoea (OSA) whose EDS has not been satisfactorily treated by primary OSA therapy, such as continuous positive airway pressure (CPAP). 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | attention deficit-hyperactivity disorder | 99.99% | DL |
| 2 | faciodigitogenital syndrome | 99.99% | DL |
| 3 | insomnia (disease) | 99.97% | DL |
| 4 | attention deficit hyperactivity disorder, inattentive type | 99.96% | DL |
| 5 | chondromyxoid fibroma | 99.93% | DL |
| 6 | specific developmental disorder | 99.92% | DL |
| 7 | variably protease-sensitive prionopathy | 99.87% | DL |
| 8 | multiple system atrophy | 99.87% | DL |
| 9 | X-linked adrenoleukodystrophy | 99.83% | DL |
| 10 | postural orthostatic tachycardia syndrome | 99.83% | DL |
| 11 | disorder of peroxisomal alpha-, beta- and omega-oxidation | 99.77% | DL |
| 12 | narcolepsy | 99.76% | DL |
| 13 | narcolepsy-cataplexy syndrome | 99.75% | DL |
| 14 | Creutzfeldt-Jakob disease | 99.74% | DL |
| 15 | ACBD5 deficiency | 99.71% | DL |
| 16 | narcolepsy, susceptibility to | 99.70% | DL |
| 17 | megaconial type congenital muscular dystrophy | 99.57% | DL |
| 18 | hypersomnia (disease) | 99.46% | DL |
| 19 | circadian rhythm sleep disorder | 99.38% | DL |
| 20 | Balo concentric sclerosis | 99.21% | DL |

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
