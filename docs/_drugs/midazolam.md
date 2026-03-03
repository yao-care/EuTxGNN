---
layout: default
title: Midazolam
description: "Midazolam drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 380
evidence_level: L5
indication_count: 50
---

# Midazolam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Midazolam |
| DrugBank ID | [DB00683](https://go.drugbank.com/drugs/DB00683) |
| Brand Names (EU) | Buccolam |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.74% |

---

## Approved Indication (EMA)

Treatment of prolonged, acute, convulsive seizures in infants from 3 months to adults.BUCCOLAM must only be used by parents/carers where the patient has been diagnosed to have epilepsy.For infants between 3-6 months of age treatment should be in a hospital setting where monitoring is possible and resuscitation equipment is available. See section 4.2.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | insomnia (disease) | 99.74% | DL |
| 2 | anxiety | 99.35% | DL |
| 3 | myofascial pain syndrome | 97.92% | DL |
| 4 | obsessive-compulsive disorder | 95.69% | DL |
| 5 | tendinitis | 93.55% | DL |
| 6 | benign paroxysmal torticollis of infancy | 93.49% | DL |
| 7 | anxiety disorder | 92.83% | DL |
| 8 | agoraphobia | 92.75% | DL |
| 9 | myositis fibrosa | 92.52% | DL |
| 10 | idiopathic granulomatous myositis | 92.52% | DL |
| 11 | dysthymic disorder | 92.01% | DL |
| 12 | paranoid personality disorder | 91.95% | DL |
| 13 | histrionic personality disorder (disease) | 91.95% | DL |
| 14 | schizotypal personality disorder | 91.95% | DL |
| 15 | schizoid personality disorder | 91.95% | DL |
| 16 | fibromyalgia | 88.87% | DL |
| 17 | sleep disorder, initiating and maintaining sleep | 88.58% | DL |
| 18 | Asperger syndrome | 87.93% | DL |
| 19 | inclusion body myositis | 83.12% | DL |
| 20 | attention deficit-hyperactivity disorder | 81.19% | DL |

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
