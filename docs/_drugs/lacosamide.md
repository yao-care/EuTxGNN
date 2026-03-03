---
layout: default
title: Lacosamide
description: "Lacosamide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 325
evidence_level: L5
indication_count: 50
---

# Lacosamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lacosamide |
| DrugBank ID | [DB06218](https://go.drugbank.com/drugs/DB06218) |
| Brand Names (EU) | Lacosamide UCB |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Lacosamide UCB is indicated as monotherapy and adjunctive therapy in the treatment of partial-onset seizures with or without secondary generalisation in adults, adolescents and children from 4 years of age with epilepsy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.96% | DL |
| 2 | Tourette syndrome | 99.95% | DL |
| 3 | trichotillomania | 99.92% | DL |
| 4 | nephrogenic syndrome of inappropriate antidiuresis | 99.91% | DL |
| 5 | migraine disorder | 99.87% | DL |
| 6 | insomnia (disease) | 99.83% | DL |
| 7 | migraine with brainstem aura | 99.82% | DL |
| 8 | myofascial pain syndrome | 99.81% | DL |
| 9 | obsessive-compulsive disorder | 99.78% | DL |
| 10 | papillary conjunctivitis | 99.72% | DL |
| 11 | allergic asthma | 99.70% | DL |
| 12 | transient ischemic attack (disease) | 99.69% | DL |
| 13 | anxiety disorder | 99.68% | DL |
| 14 | angioedema | 99.68% | DL |
| 15 | fibromyalgia | 99.68% | DL |
| 16 | schizoid personality disorder | 99.67% | DL |
| 17 | histrionic personality disorder (disease) | 99.67% | DL |
| 18 | paranoid personality disorder | 99.67% | DL |
| 19 | schizotypal personality disorder | 99.67% | DL |
| 20 | intrinsic asthma | 99.67% | DL |

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
