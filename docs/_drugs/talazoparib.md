---
layout: default
title: Talazoparib
description: "Talazoparib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 554
evidence_level: L5
indication_count: 50
---

# Talazoparib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Talazoparib |
| DrugBank ID | [DB11760](https://go.drugbank.com/drugs/DB11760) |
| Brand Names (EU) | Talzenna |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.98% |

---

## Approved Indication (EMA)

Treatment with Talzenna should be initiated and supervised by a physician experienced in the use of anticancer medicinal products. Patient selection Breast cancer: Patients should be selected for the treatment of breast cancer with Talzenna based on the presence of deleterious or suspected deleterious germline BRCA mutations determined by an experienced laboratory using a validated test method. Genetic counselling for patients with BRCA mutations should be performed according to local regulation

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HER2 positive breast carcinoma | 98.98% | DL |
| 2 | HIV infectious disease | 98.47% | DL |
| 3 | progesterone-receptor negative breast cancer | 98.34% | DL |
| 4 | normal breast-like subtype of breast carcinoma | 98.34% | DL |
| 5 | progesterone-receptor positive breast cancer | 98.34% | DL |
| 6 | breast tumor luminal A or B | 98.30% | DL |
| 7 | multiple endocrine neoplasia | 98.27% | DL |
| 8 | primary release disorder of platelets | 98.08% | DL |
| 9 | feline acquired immunodeficiency syndrome | 98.07% | DL |
| 10 | simian immunodeficiency virus infection | 98.07% | DL |
| 11 | breast fibrocystic disease | 97.69% | DL |
| 12 | pseudo-von Willebrand disease | 97.43% | DL |
| 13 | cytomegalovirus infection | 97.41% | DL |
| 14 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 97.38% | DL |
| 15 | malignant catarrh | 97.32% | DL |
| 16 | infectious bovine rhinotracheitis | 97.32% | DL |
| 17 | Glanzmann thrombasthenia | 97.30% | DL |
| 18 | female breast carcinoma | 97.27% | DL |
| 19 | drug-induced osteoporosis | 97.16% | DL |
| 20 | benign mammary dysplasia | 97.05% | DL |

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
