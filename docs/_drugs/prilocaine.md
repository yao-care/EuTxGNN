---
layout: default
title: Prilocaine
description: "Prilocaine drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 472
evidence_level: L5
indication_count: 51
---

# Prilocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Prilocaine |
| DrugBank ID | [DB00750](https://go.drugbank.com/drugs/DB00750) |
| Brand Names (EU) | Fortacin, Prilocaine |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.78% |

---

## Approved Indication (EMA)

Treatment of primary premature ejaculation in adult men.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | papillary conjunctivitis | 99.78% | DL |
| 2 | manic bipolar affective disorder | 99.76% | DL |
| 3 | bronchitis | 99.64% | DL |
| 4 | migraine disorder | 99.42% | DL |
| 5 | neuralgia | 99.34% | DL |
| 6 | migraine with brainstem aura | 99.33% | DL |
| 7 | atopic eczema | 99.31% | DL |
| 8 | allergic asthma | 99.29% | DL |
| 9 | rhinitis | 99.28% | DL |
| 10 | rosacea conjunctivitis | 99.24% | DL |
| 11 | intrinsic asthma | 99.16% | DL |
| 12 | nasal cavity disease | 99.06% | DL |
| 13 | pharyngitis | 99.00% | DL |
| 14 | transient ischemic attack (disease) | 98.99% | DL |
| 15 | conjunctivitis | 98.97% | DL |
| 16 | cauda equina syndrome | 98.83% | DL |
| 17 | acute laryngopharyngitis | 98.81% | DL |
| 18 | atopic conjunctivitis | 98.80% | DL |
| 19 | blepharoconjunctivitis | 98.73% | DL |
| 20 | Tourette syndrome | 98.71% | DL |

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
