---
layout: default
title: Belatacept
description: "Belatacept drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 73
evidence_level: L5
indication_count: 50
---

# Belatacept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Belatacept |
| DrugBank ID | [DB06681](https://go.drugbank.com/drugs/DB06681) |
| Brand Names (EU) | Nulojix |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.03% |

---

## Approved Indication (EMA)

Nulojix, in combination with corticosteroids and a mycophenolic acid (MPA), is indicated for prophylaxis of graft rejection in adult&nbsp;recipients of a renal transplant.&nbsp;

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | plasma cell myeloma | 97.03% | DL |
| 2 | indolent plasma cell myeloma | 96.94% | DL |
| 3 | relapsing-remitting multiple sclerosis | 96.82% | DL |
| 4 | Crohn's colitis | 96.18% | DL |
| 5 | heart disease | 94.62% | DL |
| 6 | Laubry-Pezzi syndrome | 94.06% | DL |
| 7 | hyperthyroidism | 93.81% | DL |
| 8 | genetic syndromic Pierre Robin syndrome | 93.71% | DL |
| 9 | Pierre Robin syndrome associated with a chromosomal anomaly | 93.66% | DL |
| 10 | colonic neoplasm | 93.63% | DL |
| 11 | Jeune syndrome situs inversus | 93.53% | DL |
| 12 | orofacial clefting syndrome | 93.51% | DL |
| 13 | disorder of fucoglycosan synthesis | 93.42% | DL |
| 14 | partial deletion of the long arm of chromosome 7 | 93.31% | DL |
| 15 | pulmonary valve disease | 93.03% | DL |
| 16 | primary release disorder of platelets | 92.99% | DL |
| 17 | psoriasis | 92.97% | DL |
| 18 | interventricular septum aneurysm | 92.96% | DL |
| 19 | partial deletion of the long arm of chromosome 22 | 92.94% | DL |
| 20 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 92.73% | DL |

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
