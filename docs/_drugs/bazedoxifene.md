---
layout: default
title: Bazedoxifene
description: "Bazedoxifene drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 71
evidence_level: L5
indication_count: 50
---

# Bazedoxifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bazedoxifene |
| DrugBank ID | [DB06401](https://go.drugbank.com/drugs/DB06401) |
| Brand Names (EU) | Conbriza |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.99% |

---

## Approved Indication (EMA)

Conbriza is indicated for the treatment of postmenopausal osteoporosis in women at increased risk of fracture. A significant reduction in the incidence of vertebral fractures has been demonstrated; efficacy on hip fractures has not been established. When determining the choice of Conbriza or other therapies, including oestrogens, for an individual postmenopausal woman, consideration should be given to menopausal symptoms, effects on uterine and breast tissues, and cardiovascular risks and benefi

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | heparin cofactor 2 deficiency | 98.99% | DL |
| 2 | postmenopausal osteoporosis | 98.75% | DL |
| 3 | antithrombin deficiency type 2 | 98.66% | DL |
| 4 | Worth syndrome | 98.64% | DL |
| 5 | amenorrhea (disease) | 98.45% | DL |
| 6 | factor 5 excess with spontaneous thrombosis | 98.36% | DL |
| 7 | pregnancy associated osteoporosis | 98.35% | DL |
| 8 | autosomal dominant neovascular inflammatory vitreoretinopathy | 98.24% | DL |
| 9 | thrombophilia | 97.69% | DL |
| 10 | primary release disorder of platelets | 97.48% | DL |
| 11 | pseudo-von Willebrand disease | 97.37% | DL |
| 12 | succinyl-CoA:3-ketoacid CoA transferase deficiency | 97.32% | DL |
| 13 | severe nonproliferative diabetic retinopathy | 96.67% | DL |
| 14 | acne (disease) | 96.17% | DL |
| 15 | Glanzmann thrombasthenia | 94.60% | DL |
| 16 | drug-induced osteoporosis | 93.74% | DL |
| 17 | duodenal ulcer (disease) | 91.18% | DL |
| 18 | duodenogastric reflux | 89.82% | DL |
| 19 | fetal and neonatal alloimmune thrombocytopenia | 89.77% | DL |
| 20 | duodenal obstruction | 89.64% | DL |

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
