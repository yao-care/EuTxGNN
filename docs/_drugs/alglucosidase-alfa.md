---
layout: default
title: Alglucosidase Alfa
description: "Alglucosidase Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 28
evidence_level: L5
indication_count: 50
---

# Alglucosidase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Alglucosidase Alfa |
| DrugBank ID | [DB01272](https://go.drugbank.com/drugs/DB01272) |
| Brand Names (EU) | Myozyme |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.47% |

---

## Approved Indication (EMA)

Myozyme is indicated for long-term enzyme-replacement therapy (ERT) in patients with a confirmed diagnosis of Pompe disease (acid-?-glucosidase deficiency). In patients with late-onset Pompe disease the evidence of efficacy is limited.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | adult polyglucosan body disease | 99.47% | DL |
| 2 | glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form | 99.32% | DL |
| 3 | glycogen storage disease due to glycogen branching enzyme deficiency, fatal perinatal neuromuscular form | 99.32% | DL |
| 4 | congenital entropion | 99.22% | DL |
| 5 | congenital ectropion | 99.17% | DL |
| 6 | congenital Horner syndrome (disease) | 99.17% | DL |
| 7 | ptosis-vocal cord paralysis syndrome | 99.15% | DL |
| 8 | camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye | 99.11% | DL |
| 9 | epiblepharon | 99.11% | DL |
| 10 | ptosis-strabismus-ectopic pupils syndrome | 99.10% | DL |
| 11 | tricarboxylic acid cycle disorder | 99.07% | DL |
| 12 | ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome | 99.01% | DL |
| 13 | mucopolysaccharidosis | 98.97% | DL |
| 14 | jaw-winking syndrome | 98.97% | DL |
| 15 | disease of transporter activity | 98.97% | DL |
| 16 | glycogen storage disease | 98.92% | DL |
| 17 | glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form | 98.81% | DL |
| 18 | glycogen storage disease due to glycogen branching enzyme deficiency, childhood neuromuscular form | 98.81% | DL |
| 19 | glycogen storage disease due to glycogen branching enzyme deficiency, childhood combined hepatic and myopathic form | 98.81% | DL |
| 20 | glycogen storage disease due to glycogen branching enzyme deficiency, progressive hepatic form | 98.81% | DL |

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
