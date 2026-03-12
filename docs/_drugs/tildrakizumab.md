---
layout: default
title: Tildrakizumab
description: "Tildrakizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 581
evidence_level: L5
indication_count: 50
---

# Tildrakizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tildrakizumab |
| DrugBank ID | [DB14004](https://go.drugbank.com/drugs/DB14004) |
| Brand Names (EU) | Ilumetri |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.63% |

---

## Approved Indication (EMA)

Ilumetri is indicated for the treatment of adults with moderate to severe plaque psoriasis who are candidates for systemic therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | severe nonproliferative diabetic retinopathy | 99.63% | DL |
| 2 | diabetic retinopathy | 99.53% | DL |
| 3 | diabetic cataract | 99.21% | DL |
| 4 | drug-induced osteoporosis | 99.20% | DL |
| 5 | nuclear senile cataract | 98.91% | DL |
| 6 | cortical cataract | 98.91% | DL |
| 7 | senile cataract | 98.89% | DL |
| 8 | craniostenosis cataract | 98.86% | DL |
| 9 | diabetes mellitus type 2 associated cataract | 98.86% | DL |
| 10 | mature cataract | 98.86% | DL |
| 11 | tetanic cataract | 98.86% | DL |
| 12 | immature cataract | 98.86% | DL |
| 13 | dermatitis | 97.97% | DL |
| 14 | neonatal dermatomyositis | 97.52% | DL |
| 15 | amyopathic dermatomyositis | 97.40% | DL |
| 16 | acrodermatitis chronica atrophicans | 97.38% | DL |
| 17 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 97.20% | DL |
| 18 | acne keloid | 97.16% | DL |
| 19 | hydroa vacciniforme, familial | 97.03% | DL |
| 20 | acne (disease) | 96.90% | DL |

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
