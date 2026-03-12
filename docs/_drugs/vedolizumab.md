---
layout: default
title: Vedolizumab
description: "Vedolizumab drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 624
evidence_level: L5
indication_count: 52
---

# Vedolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vedolizumab |
| DrugBank ID | [DB09033](https://go.drugbank.com/drugs/DB09033) |
| Brand Names (EU) | Entyvio |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 94.51% |

---

## Approved Indication (EMA)

Ulcerative colitis Entyvio is indicated for the treatment of adult patients with moderately to severely active ulcerative colitis who have had an inadequate response with, lost response to, or were intolerant to either conventional therapy or a tumour necrosis factor alpha (TNF?) antagonist. Crohn’s disease Entyvio is indicated for the treatment of adult patients with moderately to severely active Crohn’s disease who have had an inadequate response with, lost response to, or were intolerant to e

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | severe nonproliferative diabetic retinopathy | 94.51% | DL |
| 2 | dermatitis | 93.57% | DL |
| 3 | neonatal dermatomyositis | 92.73% | DL |
| 4 | acne keloid | 92.33% | DL |
| 5 | acrodermatitis chronica atrophicans | 92.23% | DL |
| 6 | hydroa vacciniforme, familial | 92.18% | DL |
| 7 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 92.06% | DL |
| 8 | amyopathic dermatomyositis | 91.72% | DL |
| 9 | bronchitis | 91.02% | DL |
| 10 | drug-induced osteoporosis | 87.14% | DL |
| 11 | primary release disorder of platelets | 79.83% | DL |
| 12 | psoriasis | 74.91% | DL |
| 13 | pseudo-von Willebrand disease | 74.33% | DL |
| 14 | diabetic retinopathy | 73.57% | DL |
| 15 | anus disease | 72.49% | DL |
| 16 | acute lichenoid pityriasis | 71.92% | DL |
| 17 | parapsoriasis | 71.60% | DL |
| 18 | pityriasis lichenoides | 71.49% | DL |
| 19 | inflammatory bowel disease | 69.54% | DL |
| 20 | pityriasis simplex | 68.73% | DL |

*Showing top 20 of 52 predictions.*

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
