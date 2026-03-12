---
layout: default
title: Voclosporin
description: "Voclosporin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 637
evidence_level: L5
indication_count: 50
---

# Voclosporin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Voclosporin |
| DrugBank ID | [DB11693](https://go.drugbank.com/drugs/DB11693) |
| Brand Names (EU) | Lupkynis |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 95.42% |

---

## Approved Indication (EMA)

Lupkynis is indicated in combination with mycophenolate mofetil for the treatment of adult patients with active class III, IV or V (including mixed class III/V and IV/V) lupus nephritis (LN).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 95.42% | DL |
| 2 | Glanzmann thrombasthenia | 94.87% | DL |
| 3 | pseudo-von Willebrand disease | 94.57% | DL |
| 4 | dermatitis | 94.18% | DL |
| 5 | renal osteodystrophy | 94.16% | DL |
| 6 | exanthem (disease) | 93.88% | DL |
| 7 | severe nonproliferative diabetic retinopathy | 93.40% | DL |
| 8 | neonatal dermatomyositis | 92.94% | DL |
| 9 | acrodermatitis chronica atrophicans | 92.91% | DL |
| 10 | non-renal secondary hyperparathyroidism | 92.86% | DL |
| 11 | amyopathic dermatomyositis | 92.71% | DL |
| 12 | impaired renal function disease | 92.68% | DL |
| 13 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 92.05% | DL |
| 14 | indolent plasma cell myeloma | 91.84% | DL |
| 15 | hyperparathyroidism, transient neonatal | 91.66% | DL |
| 16 | acne keloid | 91.65% | DL |
| 17 | hydroa vacciniforme, familial | 91.62% | DL |
| 18 | bronchitis | 91.56% | DL |
| 19 | plasma cell myeloma | 91.33% | DL |
| 20 | ulcerative colitis (disease) | 91.06% | DL |

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
