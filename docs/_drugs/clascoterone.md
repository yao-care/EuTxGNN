---
layout: default
title: Clascoterone
description: "Clascoterone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 138
evidence_level: L5
indication_count: 50
---

# Clascoterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Clascoterone |
| DrugBank ID | [DB12499](https://go.drugbank.com/drugs/DB12499) |
| Brand Names (EU) | Winlevi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 94.82% |

---

## Approved Indication (EMA)

Adults&nbsp;Winlevi is indicated for the treatment of acne vulgaris. Adolescents (from 12 to &lt;&nbsp;18&nbsp;years of age)&nbsp;Winlevi is indicated for the treatment of facial acne vulgaris.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | candidiasis | 94.82% | DL |
| 2 | migraine disorder | 92.11% | DL |
| 3 | migraine with brainstem aura | 91.39% | DL |
| 4 | migraine with or without aura, susceptibility to | 89.40% | DL |
| 5 | leprosy | 88.87% | DL |
| 6 | atrophoderma vermiculata | 86.78% | DL |
| 7 | oral candidiasis | 86.71% | DL |
| 8 | progeria-short stature-pigmented nevi syndrome | 86.02% | DL |
| 9 | adrenal gland hyperfunction | 85.90% | DL |
| 10 | multiple endocrine neoplasia | 85.51% | DL |
| 11 | ulerythema ophryogenesis | 85.35% | DL |
| 12 | progeroid syndrome, Petty type | 85.25% | DL |
| 13 | commissural lip fistula | 84.89% | DL |
| 14 | osteoradionecrosis of the mandible | 84.86% | DL |
| 15 | burning mouth syndrome | 84.83% | DL |
| 16 | oral leukoedema | 84.83% | DL |
| 17 | hyperargininemia | 84.79% | DL |
| 18 | carbamoyl phosphate synthetase I deficiency disease | 84.79% | DL |
| 19 | Leydig cell hypoplasia due to LH resistance | 82.66% | DL |
| 20 | bone marrow neoplasm | 82.59% | DL |

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
