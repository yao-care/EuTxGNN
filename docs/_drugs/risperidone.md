---
layout: default
title: Risperidone
description: "risperidone drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 499
evidence_level: L1
indication_count: 50
---

# Risperidone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Risperidone |
| DrugBank ID | [DB00734](https://go.drugbank.com/drugs/DB00734) |
| Brand Names (EU) | Okedi |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Treatment of schizophrenia in adults for whom tolerability and effectiveness has been established with oral risperidone.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.98% | DL |
| 2 | autism spectrum disorder | 99.78% | DL |
| 3 | autism susceptibility 1 | 99.77% | DL |
| 4 | gaze palsy, familial horizontal, with progressive scoliosis | 99.76% | DL |
| 5 | asperger syndrome, susceptibility to | 99.74% | DL |
| 6 | amelocerebrohypohidrotic syndrome | 99.69% | DL |
| 7 | Phelan-McDermid syndrome | 99.59% | DL |
| 8 | trichotillomania | 99.51% | DL |
| 9 | major affective disorder | 99.11% | DL |
| 10 | bipolar disorder | 98.89% | DL |
| 11 | Tourette syndrome | 98.76% | DL |
| 12 | intellectual disability | 98.72% | DL |
| 13 | autism, susceptibility to | 98.65% | DL |
| 14 | chromosome 15q11.2 deletion syndrome | 98.59% | DL |
| 15 | 16q24.3 microdeletion syndrome | 98.59% | DL |
| 16 | schizophrenia | 98.55% | DL |
| 17 | occipital pachygyria and polymicrogyria | 98.32% | DL |
| 18 | attention deficit-hyperactivity disorder | 98.26% | DL |
| 19 | distal 17p13.3 microdeletion syndrome | 98.20% | DL |
| 20 | epsilon-trimethyllysine hydroxylase deficiency | 98.14% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| manic bipolar affective disorder | L1 | 20 | 0 | 10 Phase 3 trial(s) |

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
