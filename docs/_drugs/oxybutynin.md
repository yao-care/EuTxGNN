---
layout: default
title: Oxybutynin
description: "Oxybutynin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 430
evidence_level: L5
indication_count: 50
---

# Oxybutynin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Oxybutynin |
| DrugBank ID | [DB01062](https://go.drugbank.com/drugs/DB01062) |
| Brand Names (EU) | Kentera (previously Oxybutynin Nicobrand) |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.86% |

---

## Approved Indication (EMA)

Symptomatic treatment of urge incontinence and/or increased urinary frequency and urgency as may occur in adult patients with unstable bladder.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | cauda equina syndrome | 99.86% | DL |
| 2 | overactive bladder (disease) | 99.78% | DL |
| 3 | restless legs syndrome | 99.74% | DL |
| 4 | obsolete neurogenic bladder (disease) | 99.69% | DL |
| 5 | gastroduodenitis | 99.62% | DL |
| 6 | peptic ulcer disease | 99.31% | DL |
| 7 | low compliance bladder | 97.88% | DL |
| 8 | nephrogenic syndrome of inappropriate antidiuresis | 97.46% | DL |
| 9 | insomnia (disease) | 96.90% | DL |
| 10 | attention deficit-hyperactivity disorder | 95.11% | DL |
| 11 | faciodigitogenital syndrome | 94.96% | DL |
| 12 | familial episodic pain syndrome with predominantly upper body involvement | 92.62% | DL |
| 13 | transient tic disorder | 92.45% | DL |
| 14 | migraine disorder | 92.12% | DL |
| 15 | migraine with brainstem aura | 92.02% | DL |
| 16 | sleep disorder, initiating and maintaining sleep | 91.77% | DL |
| 17 | bladder neck obstruction | 91.33% | DL |
| 18 | communication disorder | 90.67% | DL |
| 19 | stereotypic movement disorder | 90.61% | DL |
| 20 | fetal nicotine spectrum disorder | 90.61% | DL |

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
