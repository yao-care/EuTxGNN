---
layout: default
title: L-Lysine
description: "L-Lysine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 324
evidence_level: L5
indication_count: 50
---

# L-Lysine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | L-Lysine |
| DrugBank ID | [DB00123](https://go.drugbank.com/drugs/DB00123) |
| Brand Names (EU) | L-Lysine |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.77% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | gastroparesis (disease) | 99.77% | DL |
| 2 | congenital prothrombin deficiency | 99.13% | DL |
| 3 | obsolete vitamin D deficiency | 99.02% | DL |
| 4 | dyspepsia | 98.68% | DL |
| 5 | familial visceral myopathy | 98.37% | DL |
| 6 | vitamin deficiency disorder | 98.21% | DL |
| 7 | hypophosphatemic rickets | 97.98% | DL |
| 8 | renal tubular acidosis | 97.80% | DL |
| 9 | biotin metabolic disease | 97.80% | DL |
| 10 | postgastrectomy syndrome | 97.30% | DL |
| 11 | albinism-deafness syndrome | 97.15% | DL |
| 12 | postmenopausal osteoporosis | 96.99% | DL |
| 13 | intestinal obstruction | 96.96% | DL |
| 14 | myopathic intestinal pseudoobstruction | 96.67% | DL |
| 15 | unclassified intestinal pseudoobstruction | 96.67% | DL |
| 16 | stomach disease | 96.66% | DL |
| 17 | neuronal intestinal dysplasia, type B | 96.53% | DL |
| 18 | acne (disease) | 96.49% | DL |
| 19 | familial isolated hypoparathyroidism due to impaired PTH secretion | 96.19% | DL |
| 20 | hereditary hypophosphatemic rickets | 95.88% | DL |

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
