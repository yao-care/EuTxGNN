---
layout: default
title: Lidocaine
description: "Lidocaine drug repurposing predictions from TxGNN. Evidence level L5 with 61 predicted indications."
parent: AI Predictions (L5)
nav_order: 343
evidence_level: L5
indication_count: 61
---

# Lidocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **61**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lidocaine |
| DrugBank ID | [DB00281](https://go.drugbank.com/drugs/DB00281) |
| Brand Names (EU) | Fortacin, Lidocaine |
| Evidence Level | L5 |
| Predicted Indications | 61 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Treatment of primary premature ejaculation in adult men.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | punctate epithelial keratoconjunctivitis | 99.99% | DL |
| 2 | papillary conjunctivitis | 99.98% | DL |
| 3 | rosacea conjunctivitis | 99.92% | DL |
| 4 | exposure keratitis | 99.87% | DL |
| 5 | atopic conjunctivitis | 99.86% | DL |
| 6 | conjunctival disorder | 99.84% | DL |
| 7 | nephrotic syndrome | 99.83% | DL |
| 8 | non-human animal disease | 99.82% | DL |
| 9 | tinea corporis | 99.82% | DL |
| 10 | sporadic idiopathic steroid-resistant nephrotic syndrome | 99.79% | DL |
| 11 | disease of orbital region | 99.77% | DL |
| 12 | rheumatic heart disease | 99.75% | DL |
| 13 | idiopathic steroid-sensitive nephrotic syndrome | 99.73% | DL |
| 14 | epicondylitis | 99.73% | DL |
| 15 | blepharoconjunctivitis | 99.72% | DL |
| 16 | disease of orbital part of eye adnexa | 99.69% | DL |
| 17 | cystic teratoma | 99.66% | DL |
| 18 | spinal cord dermoid cyst | 99.66% | DL |
| 19 | dermoid cyst of ovary | 99.61% | DL |
| 20 | viral conjunctivitis | 99.61% | DL |

*Showing top 20 of 61 predictions.*

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
