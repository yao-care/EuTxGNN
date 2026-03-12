---
layout: default
title: Tasimelteon
description: "Tasimelteon drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 556
evidence_level: L5
indication_count: 51
---

# Tasimelteon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tasimelteon |
| DrugBank ID | [DB09071](https://go.drugbank.com/drugs/DB09071) |
| Brand Names (EU) | Hetlioz |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.48% |

---

## Approved Indication (EMA)

Hetlioz is indicated for the treatment of Non-24-Hour Sleep-Wake Disorder (Non-24) in totally blind adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bilateral parasagittal parieto-occipital polymicrogyria | 99.48% | DL |
| 2 | insomnia (disease) | 99.47% | DL |
| 3 | amyotrophic lateral sclerosis | 99.36% | DL |
| 4 | endogenous depression | 99.36% | DL |
| 5 | axial spondylometaphyseal dysplasia | 99.23% | DL |
| 6 | monomelic amyotrophy | 99.22% | DL |
| 7 | amyotrophic lateral sclerosis, susceptibility to | 99.19% | DL |
| 8 | lower motor neuron syndrome with late-adult onset | 99.17% | DL |
| 9 | Mills syndrome | 99.15% | DL |
| 10 | amyotrohpic lateral sclerosis type 22 | 99.13% | DL |
| 11 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 99.10% | DL |
| 12 | autosomal dominant mitochondrial myopathy with exercise intolerance | 99.06% | DL |
| 13 | lethal arthrogryposis-anterior horn cell disease syndrome | 99.05% | DL |
| 14 | anxiety disorder | 98.74% | DL |
| 15 | sleep disorder, initiating and maintaining sleep | 98.60% | DL |
| 16 | benign paroxysmal torticollis of infancy | 98.57% | DL |
| 17 | childhood apraxia of speech | 98.55% | DL |
| 18 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 98.40% | DL |
| 19 | rhabdoid tumor | 98.39% | DL |
| 20 | familial generalized lentiginosis | 98.36% | DL |

*Showing top 20 of 51 predictions.*

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
