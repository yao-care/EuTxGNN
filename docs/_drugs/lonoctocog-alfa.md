---
layout: default
title: Lonoctocog Alfa
description: "Lonoctocog Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 351
evidence_level: L5
indication_count: 50
---

# Lonoctocog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lonoctocog Alfa |
| DrugBank ID | [DB13998](https://go.drugbank.com/drugs/DB13998) |
| Brand Names (EU) | Afstyla |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.85% |

---

## Approved Indication (EMA)

Treatment and prophylaxis of bleeding in patients with haemophilia A (congenital factor VIII deficiency). Afstyla can be used for all age groups.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pseudo-von Willebrand disease | 99.85% | DL |
| 2 | primary release disorder of platelets | 99.84% | DL |
| 3 | Glanzmann thrombasthenia | 99.76% | DL |
| 4 | Scott syndrome | 99.44% | DL |
| 5 | symptomatic form of hemophilia in female carriers | 99.31% | DL |
| 6 | hemophilia | 99.27% | DL |
| 7 | acquired coagulation factor deficiency | 98.85% | DL |
| 8 | bleeding diathesis due to a collagen receptor defect | 98.71% | DL |
| 9 | hemorrhagic disorder due to a constitutional thrombocytopenia | 98.64% | DL |
| 10 | esophageal varices without bleeding | 98.41% | DL |
| 11 | esophageal varices with bleeding | 98.41% | DL |
| 12 | thrombotic thrombocytopenic purpura | 98.13% | DL |
| 13 | hemophilia A with vascular abnormality | 97.71% | DL |
| 14 | varicose disease | 97.63% | DL |
| 15 | factor XI deficiency | 97.12% | DL |
| 16 | familial apolipoprotein C-II deficiency | 96.51% | DL |
| 17 | fetal and neonatal alloimmune thrombocytopenia | 96.49% | DL |
| 18 | primary immunodeficiency syndrome due to p14 deficiency | 96.11% | DL |
| 19 | flood factor deficiency | 96.03% | DL |
| 20 | hemorrhagic disorder due to a platelet anomaly | 95.75% | DL |

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
