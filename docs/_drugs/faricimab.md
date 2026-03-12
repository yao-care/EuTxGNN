---
layout: default
title: Faricimab
description: "Faricimab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 237
evidence_level: L5
indication_count: 50
---

# Faricimab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Faricimab |
| DrugBank ID | [DB15303](https://go.drugbank.com/drugs/DB15303) |
| Brand Names (EU) | Vabysmo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.88% |

---

## Approved Indication (EMA)

Vabysmo is indicated for the treatment of adult patients with:  neovascular (wet) age-related macular degeneration (nAMD), visual impairment due to diabetic macular oedema (DME), visual impairment due to macular oedema secondary to retinal vein occlusion (branch RVO or central RVO).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 98.88% | DL |
| 2 | pseudo-von Willebrand disease | 98.74% | DL |
| 3 | Glanzmann thrombasthenia | 98.39% | DL |
| 4 | drug-induced osteoporosis | 97.79% | DL |
| 5 | esotropia | 97.74% | DL |
| 6 | severe nonproliferative diabetic retinopathy | 97.25% | DL |
| 7 | HER2 positive breast carcinoma | 96.90% | DL |
| 8 | diabetic retinopathy | 96.75% | DL |
| 9 | respiratory syncytial virus infectious disease | 96.38% | DL |
| 10 | fetal and neonatal alloimmune thrombocytopenia | 96.08% | DL |
| 11 | breast tumor luminal A or B | 95.73% | DL |
| 12 | progesterone-receptor positive breast cancer | 95.72% | DL |
| 13 | normal breast-like subtype of breast carcinoma | 95.72% | DL |
| 14 | progesterone-receptor negative breast cancer | 95.64% | DL |
| 15 | progressive multiple sclerosis | 95.47% | DL |
| 16 | diabetic cataract | 95.05% | DL |
| 17 | non-syndromic esophageal malformation | 94.56% | DL |
| 18 | senile cataract | 93.88% | DL |
| 19 | nuclear senile cataract | 93.82% | DL |
| 20 | cortical cataract | 93.82% | DL |

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
