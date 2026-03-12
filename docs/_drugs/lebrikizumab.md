---
layout: default
title: Lebrikizumab
description: "Lebrikizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 333
evidence_level: L5
indication_count: 50
---

# Lebrikizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lebrikizumab |
| DrugBank ID | [DB11914](https://go.drugbank.com/drugs/DB11914) |
| Brand Names (EU) | Ebglyss |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.94% |

---

## Approved Indication (EMA)

Ebglyss is indicated for the treatment of moderate-to-severe atopic dermatitis in adults and adolescents 12 years and older with a body weight of at least 40 kg who are candidates for systemic therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | severe nonproliferative diabetic retinopathy | 97.94% | DL |
| 2 | drug-induced osteoporosis | 97.67% | DL |
| 3 | diabetic retinopathy | 96.84% | DL |
| 4 | primary release disorder of platelets | 96.50% | DL |
| 5 | dermatitis | 95.97% | DL |
| 6 | pseudo-von Willebrand disease | 95.50% | DL |
| 7 | Glanzmann thrombasthenia | 95.46% | DL |
| 8 | neonatal dermatomyositis | 95.26% | DL |
| 9 | psoriasis | 95.13% | DL |
| 10 | HER2 positive breast carcinoma | 95.12% | DL |
| 11 | acrodermatitis chronica atrophicans | 95.02% | DL |
| 12 | amyopathic dermatomyositis | 94.96% | DL |
| 13 | acne keloid | 94.93% | DL |
| 14 | diabetic cataract | 94.79% | DL |
| 15 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 94.67% | DL |
| 16 | hydroa vacciniforme, familial | 94.50% | DL |
| 17 | cortical cataract | 94.15% | DL |
| 18 | nuclear senile cataract | 94.15% | DL |
| 19 | senile cataract | 94.01% | DL |
| 20 | immature cataract | 93.85% | DL |

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
